#!/usr/bin/env python

#***************************************************************************
#*   Copyright (c) 2021 Yorik van Havre <yorik@uncreated.net>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

"""
migrate.py - MediaWiki to Markdown migration tool

This tool allows to download all pages and images from a MediaWiki instance,
and save all images and pages as markdown files. It keeps track of page versions,
so it can update an existing download by just updating what has changed.

Basic command-line usage:
-------------------------

    migrate.py --init

    See bottom of file for available functions

Python usage:
-------------

First time:

    from migrate import MediaWiki
    wiki = MediaWiki()
    wiki.getPageNames() # not strictly needed, done automatically by next step
    wiki.getAllPages() # this writes to disk cache, so it can be interrupted/resumed
    wiki.writeAllPages() # write md files
    wiki.getAllImages() # fetches and saves all images

You will get two json files: a text cache and a revision set.

Next times:

    from migrate import MediaWiki
    wiki = MediaWiki() # this loads filecache.json
    oldrevisions = wiki.readRevisions() # this loads the latest revision set
    wiki.getPageNames() # this fetches new page names, if any
    newrevisions = wiki.getRevisions()
    wiki.updateRevisions(oldrevisions,newrevisions) # this writes to disk cache like getAllPages
    wiki.writeAllPages() # write md files - overwrites everything
    wiki.getAllImages() # fetches and saves all images - existing ones are not overwritten
"""

# write threads: https://www.pythontutorial.net/advanced-python/python-threading/

import requests
import sys
import os
import re
import json
from datetime import datetime, date
import pypandoc
import threading
from PySide2 import QtCore
import FreeCAD
import git
import inspect

unhandledTemplates = [] # holder for unhandled templates
BASE_URL = "https://wiki.freecadweb.org"
THREADS = 4 # number of threads for file writing
WIKIFOLDER = "wiki"
CATEGORY_COLUMNS = 3 # the number of columns on category pages
PART_API_PAGES = ["Vertex","Edge","Wire","Face","Shell","Solid","CompSolid","Compound",
                  "Arc","Circle","Line","Ellipse","Cone","BSplineCurve","BSplineSurface",
                  "BezierCurve","Cylinder","Point","Sphere","Shape"]
# templates that are safe to remove entirely
UNUSED_TEMPLATES = ["Userdocnavi","Powerdocnavi","Arch Tools navi","\\#translation:","clear",
                   "Part Tools navi","Draft Tools navi","UnfinishedDocu","Tutorials navi",
                   "Arch_Tools_navi"]


class MediaWiki:

    """MediaWiki([url]) - A class to represent an online MediaWiki instance.
       default url is wiki.freecadweb.org"""

    def __init__(self,url=BASE_URL):

        if not url.endswith("api.php"):
            if not url.endswith("/"):
                url += "/"
            url += "api.php"
        self.url = url
        self.cachefile = os.path.join(os.path.dirname(__file__),"cache.json")
        self.session = requests.Session()
        self.pagenames = []
        self.pagecount = 0
        self.pagecontents = {}
        self.readCache()
        self.imagecount = 0
        self.images = {}
        self.wikifolder = WIKIFOLDER
        self.output = os.path.join(os.path.dirname(__file__),self.wikifolder)
        if not os.path.exists(self.output):
            os.mkdir(self.output)
        self.imagefolder = "images"
        self.translationfolder = "translations"
        self.rootpage = "README.md"
        self.workbenches = self.getWorkbenches()
        self.icon_function = os.path.join(self.imagefolder,"type_method.svg")
        self.icon_module = os.path.join(self.imagefolder,"type_module.svg")
        self.icon_type = os.path.join(self.imagefolder,"type_class.svg")
        self.icon_builtin = os.path.join(self.imagefolder,"Type_enum.svg")
        self.icon_nav = os.path.join(self.imagefolder,"Right_arrow.png")


    ### UTILS


    def printProgress(self,count=None,total=100,text=""):

        """printProgress([count,total,text]):
        Prints a progress bar indicating the current progresses (count/total)
        and optionally an info text. Calling printProgress() terminates with a
        newline"""

        sys.stdout.flush()
        if count is None:
            sys.stdout.write("\r"+" ".ljust(72)+"\r")
            return
        sys.stdout.write(('\r'+text+' '+str(int((count/total)*100))+'%').ljust(72))


    def getWorkbenches(self):

        """getWorkbenches():
        Returns a list of workbenches from FreeCAD"""
        appm = os.path.join(FreeCAD.getHomePath(),"Mod")
        userm = os.path.join(FreeCAD.getUserAppDataDir(),"Mod")
        mods = []
        for mod in os.listdir(appm):
            if os.path.isdir(os.path.join(appm,mod)):
                mods.append(mod)
        for umod in os.listdir(userm):
            if os.path.isdir(os.path.join(userm,mod)):
                if not mod in mods:
                    mods.append(mod)
        return mods


    def getWorkbench(self,page):

        """getWorkbench(page):
        Returns the workbench this page belongs to"""

        if not ("Workbench" in page):
            for w in self.workbenches:
                if page.replace(" ","_").startswith(w+"_"):
                    return w
        return None


    ### CACHE OPERATIONS


    def writeCache(self):

        """writeCache():
        Writes the contents of self.pagecontents to disk"""

        if self.pagecontents:
            with open(self.cachefile,'w',encoding='utf8') as jfile:
                json.dump(self.pagecontents, jfile, ensure_ascii = False)


    def readCache(self):

        """readCache():
        Reads the contents of self.pagecontents from disk"""

        if os.path.exists(self.cachefile):
            with open(self.cachefile) as jfile:
                self.pagecontents = json.load(jfile)
                self.pagenames = list(self.pagecontents.keys())
                self.pagecount = len(self.pagecontents)


    ### PAGE OPERATIONS


    def getPageCount(self):

        """getPageCount():
        Returns the number of content pages.
        Also stores the total in self.pagecount"""

        params = { "action": "query",
                   "meta": "siteinfo",
                   "formatversion": "2",
                   "format": "json",
                   "siprop": "statistics",
                 }
        result = self.session.get(url=self.url, params=params)
        data = result.json()
        pagecount = data["query"]["statistics"]["articles"]
        self.pagecount = pagecount
        return pagecount


    def getPageNames(self):

        """getPageNames():
        Returns a list of all pages of the wiki.
        Also stores the list in self.pagenames"""

        pages = []
        count = 1
        apfrom = None
        params = { "action": "query",
                   "format": "json",
                   "list": "allpages",
                   "aplimit": "500",
                 }
        if not self.pagecount:
            self.getPageCount()
        while True:
            self.printProgress(len(pages),self.pagecount,"Getting pages list...")
            if apfrom:
                params["apfrom"] = apfrom
            else:
                if "apfrom" in params:
                    break
            result = self.session.get(url=self.url, params=params)
            data = result.json()
            pages.extend([page["title"].replace(" ","_") for page in data["query"]["allpages"]])
            apfrom = None
            if "continue" in data:
                if "apcontinue" in data["continue"]:
                    if data["continue"]["apcontinue"]:
                        apfrom = data["continue"]["apcontinue"]
                        count += 1
            else:
                break
        self.printProgress()
        self.pagenames = list(pages)
        self.pagecount = len(self.pagenames)
        return pages


    def getPage(self,name):

        """getPage(name):
        Returns the wiki content of a page and a revision ID.
        Also stores it in self.pagecontents[name]"""

        params = { "action": "parse",
                   "format": "json",
                   "page": name,
                   "prop": "wikitext|revid",
                   "formatversion": "2",
                 }
        result = self.session.get(url=self.url, params=params)
        data = result.json()
        if "parse" in data:
            wikitext = data["parse"]["wikitext"]
            revision = data["parse"]["revid"]
            self.pagecontents[name] = wikitext
        else:
            #print("Page",BASE_URL+"/"+name,"not found")
            if name in self.pagenames:
                self.pagenames.remove(name)
            if name in self.pagecontents:
                del self.pagecontents[name]
            return None,None
        return wikitext,revision


    def getAllPages(self,pageset=None):

        """getAllPages([pageset])
        Gets the contents of all of the wiki pages
        and stores everything in self.pagecontents. If pageset is
        not given, all pages from self.pagenames are retrieved"""

        revfile = os.path.join(os.path.dirname(__file__),"revisions_tmp.json")
        revisions = self.readRevisions(revfile)
        overwrite = True
        if not pageset:
            overwrite = False
            if not self.pagenames:
                self.getPageNames()
                self.getCategories()
            pageset = self.pagenames
        count = 1
        for page in pageset:
            self.printProgress(count,len(pageset),"Getting page "+page[:64]+"...")
            if overwrite or (not page in self.pagecontents):
                text,revid = self.getPage(page)
                if text:
                    revisions[page] = revid
                    if count % 10 == 0:
                        self.writeCache()
                        self.writeRevisions(revisions,revfile)
            count += 1
        self.writeCache()
        self.printProgress()
        if os.path.exists(revfile):
            os.remove(revfile)
        self.writeRevisions(revisions)
        return revisions


    ### CATEGORIES


    def getCategories(self):

        """getCategories():
        Returns a list of categories of the whole wiki.
        Also stores the list in self.pagenames"""

        categories = []
        count = 1
        acfrom = None
        params = { "action": "query",
                   "format": "json",
                   "list": "allcategories",
                   "aclimit": "500",
                 }
        while True:
            if acfrom:
                params["acfrom"] = acfrom
            else:
                if "acfrom" in params:
                    break
            result = self.session.get(url=self.url, params=params)
            data = result.json()
            categories.extend(["Category:"+c["*"] for c in data["query"]["allcategories"]])
            acfrom = None
            if "continue" in data:
                if "accontinue" in data["continue"]:
                    if data["continue"]["accontinue"]:
                        acfrom = data["continue"]["accontinue"]
                        count += 1
            else:
                break
        self.pagenames.extend(categories)
        self.writeCache()
        return categories


    def getCategoryContents(self,name):

        """getCategoryContents():
        Returns a list of pages that use the given category"""

        if not name.startswith("Category:"):
            name = "Category:"+name
        members = []
        count = 1
        cmfrom = None
        params = { "action": "query",
                   "format": "json",
                   "list": "categorymembers",
                   "cmtitle": name,
                   "cmlimit": "5000",
                 }

        # perfomr only one big query (cmcontinue is bugged)
        result = self.session.get(url=self.url, params=params)
        data = result.json()
        for m in data["query"]["categorymembers"]:
            if ("title" in m) and m["title"]:
                members.append(m["title"])
        return members

        # cmcontinue is apparently bugged in categorymembers...
        while True:
            if cmfrom:
                params["cmfrom"] = cmfrom
            else:
                if "cmfrom" in params:
                    break
            result = self.session.get(url=self.url, params=params)
            data = result.json()
            members.extend([m["title"] for m in data["query"]["categorymembers"]])
            cmfrom = None
            if "continue" in data:
                #print(data["continue"])
                if "cmcontinue" in data["continue"]:
                    if data["continue"]["cmcontinue"]:
                        cmfrom = data["continue"]["cmcontinue"]
                        count += 1
            else:
                break
        return members


    def formatCategoryContents(self,name):

        cpages = self.getCategoryContents(name)

        # mediawiki table - obsolete, pandoc does not support it?
        #result = "{|\n"
        #col = 1
        #for p in cpages:
        #    result += "| [["+p+"]]\n"
        #    if col == CATEGORY_COLUMNS:
        #        result += "|-\n"
        #        col = 1
        #    else:
        #        col += 1
        #result += "|}\n"

        result = "|"
        for i in range(CATEGORY_COLUMNS):
            result += "     |"
        result += "\n|"
        for i in range(CATEGORY_COLUMNS):
            result += " --- |"
        result += "\n|"
        col = 1
        for p in cpages:
            result += " ["+p+"]("+self.wikifolder+"/"+p.replace(":","_")+".md) |"
            if col == CATEGORY_COLUMNS:
                result += "\n|"
                col = 1
            else:
                col += 1
        return result


    def getPageCategory(self,page):

        """getPageCategory(self,page):
        Returns the first category a page belongs to, or None"""

        if "API" in page:
            return "API"
        if page in self.pagecontents:
            content = self.pagecontents[page]
            cats = re.findall("Category:(.*?)[{}\[]",content)
            if cats:
                return cats[0]
            if re.findall("Arch Tools navi",content):
                return "Arch"
        return None


    def getPageCategories(self,page):

        """getPageCategories(self,page):
        Returns the categories a page belongs to"""

        cats = []
        if "API" in page:
            cats.append("API")
        if page in self.pagecontents:
            content = self.pagecontents[page]
            if "Tutorials navi" in content:
                cats.append("Tutorials")
            cs = re.findall("Category:(.*?)[{}\[]",content)
            for c in cs:
                if not c in cats:
                    cats.append(c)
            tcs = re.findall("\{\{(.*?) Tools navi",content)
            for tc in tcs:
                if not tc in cats:
                    cats.append(tc)
        return cats


    def getLinks(self,page):

        """getLinks(page):
        Returns the links found in a page as md links: [...](...)"""

        links = []
        pagefile = os.path.join(self.output,page.replace(" ","_").replace(":","_")+".md")
        if os.path.exists(pagefile):
            with open(pagefile) as f:
                for line in f:
                    ll = re.findall("\[.*?\]\(.*?\)",line)
                    for l in ll:
                        if not ".png" in l:
                            if not ".jpg" in l:
                                if not "http" in l:
                                    links.append(l)
        return links

    ### IMAGE OPERATIONS


    def getImageCount(self):

        """getImageCount():
        Returns the number of images.
        Also stores the total in self.imagecount"""

        params = { "action": "query",
                   "meta": "siteinfo",
                   "formatversion": "2",
                   "format": "json",
                   "siprop": "statistics",
                 }
        result = self.session.get(url=self.url, params=params)
        data = result.json()
        imagecount = data["query"]["statistics"]["images"]
        self.imagecount = imagecount
        return imagecount


    def getImageNames(self):

        """getImageNames():
        Returns a list of all images of the wiki.
        Also stores the paths in self.images"""

        images = {}
        count = 1
        aifrom = None
        params = { "action": "query",
                   "format": "json",
                   "list": "allimages",
                   "ailimit": "100",
                 }
        if not self.imagecount:
            self.getImageCount()
        while True:
            self.printProgress(count,self.imagecount,"Getting images list...")
            if aifrom:
                params["aifrom"] = aifrom
            else:
                if "aifrom" in params:
                    break
            result = self.session.get(url=self.url, params=params)
            data = result.json()
            for image in data["query"]["allimages"]:
                images[image["name"]] = image["url"]
                count += 1
            aifrom = None
            if "continue" in data:
                if "aicontinue" in data["continue"]:
                    if data["continue"]["aicontinue"]:
                        aifrom = data["continue"]["aicontinue"]
            else:
                break
        self.printProgress()
        self.images = images
        self.imagecount = len(self.images.keys())
        return images


    def getImage(self,name,overwrite=False,basepath=None):

        """getImage(name,[overwrite,basepath]):
        Downloads and saves the given image in an images subfolder.
        If no basepath is given, the current dir is used.
        If overwrite is True, file is downloaded again"""

        if not basepath:
            basepath = self.output
        basedir = os.path.join(basepath,self.imagefolder)
        if not os.path.isdir(basedir):
            os.mkdir(basedir)
        filename = os.path.join(basedir,name)
        if overwrite or (not os.path.exists(filename)):
            filecontents = requests.get(self.images[name])
            with open(filename,"wb") as imagefile:
                imagefile.write(filecontents.content)


    def getAllImages(self,overwrite=False,basepath=None):

        """getAllImages([overwrite]):
        Saves all images to disk.
        If no basepath is given, the current dir is used.
        If overwrite is True, file is downloaded again"""

        if not basepath:
            basepath = self.output
        if not self.images:
            self.getImageNames()
        count = 1
        for name in self.images.keys():
            self.printProgress(count,self.imagecount,"Downloading "+name+"...")
            self.getImage(name,overwrite,basepath)
            count += 1


    ### REVISION OPERATIONS


    def getRevisions(self):

        """getRevisions():
        Returns a list of revisions for the pages stored in self.pagenames"""

        revisions = {}
        count = 1
        apfrom = None
        params = { "action": "query",
                   "format": "json",
                   "prop": "revisions",
                   "rvprop": "ids",
                   "rvslots": "main",
                   "formatversion": "2",
                 }
        if not self.pagenames:
            self.getPageNames()
        self.printProgress(0,100,"Getting pages revisions...")
        titles = ""
        for page in self.pagenames:
            if titles:
                titles += "|"
            titles += page
            count += 1
            if count % 10 != 0:
                params["titles"] = titles
                result = self.session.get(url=self.url, params=params)
                data = result.json()
                for page in data["query"]["pages"]:
                    if "revisions" in page:
                        revisions[page["title"]] = page["revisions"][0]["revid"]
                self.printProgress(count,self.pagecount,"Getting pages revisions...")
                titles = ""
        self.printProgress()
        return revisions


    def writeRevisions(self,revisions,filename=None):

        """writeRevisions(revisions,[filename]):
        Writes the contents of revisions to disk. If no filename is
        given, one is created automatically from the current timestamp"""

        if not filename:
            d = str(datetime.now())
            fp = os.path.dirname(__file__)
            filename = os.path.join(fp,"revisions_"+d+".json")
        with open(filename,'w',encoding='utf8') as jfile:
            json.dump(revisions, jfile, ensure_ascii = False)


    def readRevisions(self,filename=None):

        """readRevisions([filename]):
        Returns a revisions dictionary previously stored in a file. If
        no filename is given, the latest one is taken"""

        data = {}
        if not filename:
            files = os.listdir(os.path.dirname(__file__))
            jsonfiles = [f for f in files if (f.endswith(".json") and f.startswith("revision"))]
            jsonfiles.sort(key=os.path.getmtime, reverse=True)
            filename = os.path.join(os.path.dirname(__file__),jsonfiles[0])
            print("Opening",os.path.basename(filename))
        if os.path.exists(filename):
            with open(filename) as jfile:
                data = json.load(jfile)
        return data


    def updateRevisions(self,oldrevision,newrevision):

        """updateRevisions(oldrevision,newrevision):
        Reads again the pages that need an update"""

        pageset = []
        for page,revid in newrevision.items():
            if page in oldrevision:
                if oldrevision[page] == revid:
                    continue
            pageset.append(page)
        print(len(pageset),"pages (",int((len(pageset)/len(self.pagenames))*100),"% ) to update...")
        self.getAllPages(pageset)
        return pageset


    ### MARKDOWN OPERATIONS


    def getMarkdown(self,page,clean=True):

        """getMarkdown(page,wikitext,[clean]):
        Returns a markdown version of a text in wiki format.
        If clean is false, raw pandoc output is returned. clean
        can also be a numeric debug value to pass to cleanMarkdown()"""

        wikitext = self.pagecontents[page]
        xargs = ['--atx-headers'] # pandoc arguments
        try:
            fmt = 'markdown+hard_line_breaks+pipe_tables'
            result = pypandoc.convert_text(wikitext, fmt, format='mediawiki', extra_args=xargs)
        except:
            print("Error converting",page)
            return None
        if clean:
            result = self.cleanMarkdown(result,debug=clean)
        if page.startswith("Category:"):
            # add list of pages
            cpages = self.formatCategoryContents(page)
            cpages = "\n\n### Contents\n\n" + cpages
            result += cpages
        result = self.addTitle(page,result)
        result = self.addFooter(page,result)
        return result


    def addTitle(self,page,mdtext):

        """addTitle(self,page,result):
        adds the page title to the given markdown"""

        # insert page title
        if mdtext.startswith("<img"):
            #print("img replace")
            mdtext = mdtext.split("\n")
            mdtext[0] = "# "+ mdtext[0].replace("128","64") + " " + page.replace("_"," ")
            mdtext = "\n".join(mdtext)
        elif "\n---\n\n" in mdtext:
            #print("yaml replace")
            mdtext = mdtext.replace("\n---\n\n","\n---\n\n# "+page.replace("_"," ")+"\n\n")
        else:
            #print("std replace")
            mdtext = "# "+page.replace("_"," ")+"\n"+mdtext
        return mdtext


    def addFooter(self,page,mdtext):

        """addFooter(self,mdtext):
        adds a footer with navigation links to the bottom of the page"""

        breadcrumb = " > "
        footer = "\n\n\n\n---\n"
        footer += "![]("+self.icon_nav+") "
        footer += "[documentation index](../"+self.rootpage+")"
        c = self.getPageCategories(page)
        w = self.getWorkbench(page)
        for cat in c:
            if cat != w:
                footer += breadcrumb + "[" + cat + "](Category_" + cat + ".md)"
        if w:
            footer += breadcrumb + "[" + w + "](" + w + "_Workbench.md)"
        footer += breadcrumb + page.replace("_"," ") + "\n"
        mdtext += footer
        return mdtext


    def cleanMarkdown(self,mdtext,imagepath=None,debug=0):

        """cleanMarkdown(mdtext,[imagepath,debug]):
        Returns a cleaned version of the given markdown text.
        Imagepath indicates the location of images relative to this page
        (default = "images"). debug (default = 0) is used to control the
        level of cleaning done. 0 means disabled (all cleaning is perfomed),
        1 = first cleaning step, 2 = 2 first cleaning steps, etc. Check the code
        to see what each step does."""

        global unhandledTemplates

        result = mdtext
        flags = re.DOTALL|re.MULTILINE
        if not imagepath:
            imagepath = self.imagefolder
        if (not debug) or (debug is True):
            debug = 100000

        if debug >= 1:
            # path replacements
            result = re.sub("\!\[(.*?)\]\(",r"![\1]("+imagepath+"/",result) # add /image to image paths
        if debug >= 1.5:
            result = re.sub(" \"wikilink\"",".md",result) # add .md to wiki page links

        if debug >= 2:
            # template that are simply removed
            result = re.sub("\`.*?\`\{\=html\}","",result)
            result = re.sub("<!--.*?-->","",result,flags=flags)
            result = re.sub("{{Docnav.*?}}","",result,flags=flags)
            result = re.sub("{{Page in progress}}","",result,flags=flags)
            result = re.sub("{{\#translation\:}}","",result,flags=flags)
            result = re.sub("{{\\\#translation\:}}","",result,flags=flags)
            result = re.sub("{{UnfinishedDocu.*?}}","",result,flags=flags)

        if debug >= 3:
            # templates that get turned into italic text
            result = re.sub("{{Caption\|(.*?)}}",r"\n*\1*",result,flags=flags)

        if debug >= 4:
            # templates that get turned into bold text
            result = re.sub("{{KEY\|(.*?)}}",r"**\1**",result,flags=flags)
            result = re.sub("{{Button\|(.*?)}}",r"**\1**",result,flags=flags)
            result = re.sub("{{MenuCommand\|(.*?)}}",r"**\1**",result,flags=flags)
            result = re.sub("{{PropertyData\|(.*?)}}",r"**\1**",result,flags=flags)
            result = re.sub("{{PropertyView\|(.*?)}}",r"**\1**",result,flags=flags)
            result = re.sub("{{Emphasis\|(.*?)}}",r"**\1**",result,flags=flags)
            result = re.sub("{{VeryImportantMessage\|(.*?)}}",r"**\1**",result,flags=flags)
            result = re.sub("{{FileName\|(.*?)}}",r"**\1**",result,flags=flags)


        if debug >= 5:
            # templates that get turned into <small> text
            result = re.sub("{{Version\|(.*?)}}",r"<small>(v\1)</small> ",result,flags=flags)
            result = re.sub("{{version\|(.*?)}}",r"<small>(v\1)</small> ",result,flags=flags)
            result = re.sub("{{VersionPlus\|(.*?)}}",r"<small>(v\1)</small> ",result,flags=flags)

        if debug >= 6:
            # templates that get turned into a newline char
            result = re.sub("{{Clear}}",r"\n",result,flags=flags)

        # all other templates are simply converted to normal text (see below)

        if debug >= 7:
            # turning GuiCommand block into YAML
            if "{{GuiCommand" in result:
                guicommandblk = re.findall("```{\=mediawiki}.*?{{GuiCommand(.*?)}}\n```",result,flags=flags)
                if guicommandblk:
                    guicommandblk = guicommandblk[0]
                    guicommandblk = re.sub("\|(.*?)\=(.*?)",r"   \1:\2",guicommandblk) # fixing GuiCommand contents
                    result = re.sub("```{\=mediawiki}.*?{{GuiCommand(.*?)}}\n```",r"---\n- GuiCommand:"+guicommandblk+"---\n",result,flags=flags)
                    result = "---"+"---".join(result.split("---")[1:]) # removing empty line before yaml block

        if debug >= 7.5:
            # turning TutorialInfo block into YAML
            if "{{TutorialInfo" in result:
                tutblk = re.findall("{{TutorialInfo(.*?)}}\n",result,flags=flags)
                if tutblk:
                    tutblk = tutblk[0]
                    tutblk = tutblk.strip()
                    tutblk = re.sub("\|(.*?)\=(.*?)",r"   \1:\2",tutblk) # fixing GuiCommand contents
                    tutblk = "---\n- TutorialInfo:"+tutblk+"\n---\n\n"
                    result = re.sub("{{TutorialInfo.*?}}\n","",result,flags=flags)
                    result = tutblk + result

        if debug >= 8:
            # remove code fences
            result = re.sub("\`","",result)
            result = re.sub("\{\=mediawiki\}","",result)
            result = re.sub("\{\:mediawiki\}","",result)

        if debug >= 9:
            # creating new code fences
            result = re.sub("{{Code\|code\=(.*?)}}",r"```python\1```",result,flags=flags) # replace {{Code}} templates
            result = re.sub("{{incode\|(.*?)}}",r"`\1`",result,flags=flags) # replace {{incode}} templates
            result = re.sub(" \`\`\`",r" \n```",result,flags=flags) # make sure all ``` are on a new line
            result = re.sub("{{TRUE}}",r"`True`",result,flags=flags) # replace {{TRUE}} templates
            result = re.sub("{{FALSE}}",r"`False`",result,flags=flags) # replace {{TRUE}} templates

        if debug >= 10:
            # fixing links
            result = re.sub("(!\[.*?\]\(.*?)\".*?\"(\))",r"\1\2",result) # remove image path descriptions
            for l1 in re.findall("\[\[Image\:.*?\|.*?px\]\]",result):
                iml1 = re.findall("Image\:(.*?)\|",l1)[0]
                iml2 = re.findall("\|(.*?)px\]\]",l1)[0]
                l2 = "<img src=\""+imagepath+"/"+iml1.replace(" ","_")+"\" width="+iml2+"px>"
                result = result.replace(l1,l2)
            result = re.sub("\[\[Image\:(.*?)\|(.*?)\]\]",r"![]("+imagepath+"/\1)",result)
            result = re.sub("\[\[(.*?)\|(.*?)\]\]",r"[\2](\1.md)",result)
            result = re.sub(r"\]\(.*?\.",lambda x:x.group().replace(" ","_"),result) # replace spaces by underscores in all remaining links
            result = re.sub("!\[(.*?)\]\((.*?)\){width=\"(.*?)\"}",r'<img alt="\1" src=\2 style="width:\3px;">',result) # fix img sizes
            #for l in re.findall("\[.*?\]\(.*?\)",result):
            #    print("   ",l)

        if debug >= 11:
            # fixing misc formatting glitches
            result = re.sub("\n-   \n","\n-",result,flags=flags) # condensing newlines in bullet point lists
            result = re.sub("\n    \n    ","",result,flags=flags) # condensate empty lines
            result = re.sub("\n\n\n\(v",r" (v",result,flags=flags) # condensate badly formatted version templates
            result = re.sub("\n:\n","",result,flags=flags) # condensate remaining : lines
            result = re.sub("\n\n\n\n-","\n-",result,flags=flags) # condensate bad - lists
        if debug >= 11.5:
            result = re.sub("(<img.*?>.*?)(\*.*?\*\n)",r"\1\n\2",result) # put captions on a newline
            result = re.sub("\[(.*?)\]\(image:(.*?)\.md\)",r"![\1]("+imagepath+r"/\2)",result) # fix image: links
        if debug >= 11.7:
            result = re.sub("([0-9]+)px\]\(File\:(.*?)\.md\)",r'<img src='+imagepath+r'/\2 style="width:\1px">',result) # fix File: links
            result = re.sub("\:(\w+\.md\))",r"_\1",result) # rename Namespace:Page to Namespace_Page

        if debug >= 12:
            # removing other leftovers
            result = re.sub("\\\_\\\_NOTOC\\\_\\\_","",result,flags=flags) # removing __NOTOC__ entries
            result = re.sub("\{\#.*?\}","",result,flags=flags) # removing {#...} tags
            result = re.sub("\:\\\*","   *",result) # fix second-level bullets

        if debug >= 13:
            # removing all remaining templates
            for template in re.findall("{{.*?}}",result,flags=flags):
                if template.strip("{").strip("}").strip() in UNUSED_TEMPLATES:
                    result = re.sub(template,"",result,flags=flags) # remove all remaining templates
                else:
                    #print("WARNING: Unhandled template:",template)
                    try:
                        template = re.findall("{{(.*?)[|}]",template,flags=flags)[0].strip()
                    except:
                        print("error in template:",template)
                        sys.exit(1)
                    if not template in unhandledTemplates:
                        unhandledTemplates.append(template)

        if debug >= 14:
            # remove horizontal lines
            result = re.sub(r"(-)\1{3,}","",result)

        if debug >= 15:
            # remove category links (included in footer)
            # result = re.sub("Category:","<img src=\""+imagepath+"/Property.png\" style=\"width:16px\"> ",result) # Replace Category: with icon
            result = re.sub("\[Category\:.*?md\)","",result)


        return result.strip()


    def writeMarkdown(self,page,overwrite=True,basepath=None,clean=True):

        """writeMarkdown(page,[overwrite,basepath,clean]):
        Writes the given page as a .md file. If basepath is
        not given, file is written in the current dir.
        If overwrite is False, existing files are skipped.
        If clean is false, raw pandoc output is returned"""

        if not basepath:
            basepath = self.output
        if not os.path.exists(basepath):
            print("base path",basepath,"does not exist")
            return page
        result = self.getMarkdown(page,clean)
        if not result:
            print("Error writing page:",page)
            return page
        if "REDIRECT" in result.split("\n")[0]:
            truepage = re.findall("\((.*?)\.md\)",result)
            if not truepage:
                truepage = re.findall("\((.*?)[\"\)]",result)
            if not truepage[0].strip() in self.pagecontents:
                print("Error:redirecting to",truepage[0].strip())
                return page
            result = self.getMarkdown(truepage[0].strip(),clean)
        if not result:
            print("Error writing page:",page)
            return page
        else:
            filename = page
            if "/" in filename:
                filename = os.path.join(self.output,self.translationfolder,page.split("/")[-1],page.split("/")[0])
                transpath = os.path.dirname(filename)
                if not os.path.exists(transpath):
                    if not os.path.exists(os.path.join(self.output,self.translationfolder)):
                        os.mkdir(os.path.join(self.output,self.translationfolder))
                    os.mkdir(transpath)
            filename += ".md"
            filename = os.path.join(basepath,filename)
            filename = filename.replace(" ","_")
            filename = filename.replace(":","_")
            if overwrite or (not os.file.exists(filename)):
                with open(filename,"w") as mdfile:
                    mdfile.write(result)
            return None


    def writeAllPages(self,overwrite=True,basepath=None,threads=THREADS):

        """writeAllPages([overwrite,basepath,threads]):
        Writes all pages to markdown files. Returns
        a list of pages which couldn't be written for some reason.
        If basepath is not given, file is written in the current dir.
        If overwrite is False, existing files are skipped. basepath is
        where to write the page (default to self.wikipath). threads is
        the number of threads to use (default is THREADS global constant)"""

        global unhandledTemplates

        errors = []
        count = 1
        if not basepath:
            basepath = self.output
        if threads < 2:
            # single-thread
            for page in self.pagenames:
                self.printProgress(count,len(self.pagenames),"Saving page "+page+"...")
                r = self.writeMarkdown(page,overwrite,basepath)
                if r:
                    errors.append(r)
                count += 1
        else:
            print("Using",threads,"threads...")
            # multi-thread
            while count <= len(self.pagenames):
                basket = []
                for i in range(threads):
                    n = count-1
                    if n < len(self.pagenames):
                        page = self.pagenames[n]
                        self.printProgress(count,len(self.pagenames),"Saving page "+page+"...")
                        t = threading.Thread(target=self.writeMarkdown,args=(page,overwrite,basepath))
                        basket.append(t)
                        t.start()
                    count += 1
                for t in basket:
                    t.join()
        self.printProgress()
        print("All done!\n")
        print("SUMMARY:\n")
        if unhandledTemplates:
            print("unhandled templates: ",unhandledTemplates)
            print("\n")
        if errors:
            print("page with write errors: ",errors)
        return errors


    def updateReadme(self):

        """updateReadme():
        Updates the main page with a list of available translations"""

        mainpage = os.path.join(os.path.dirname(__file__),"README.md")
        tfolder = os.path.join(self.output,self.translationfolder)
        column = 1
        output = ""
        for lcode in os.listdir(tfolder):
            lfolder = os.path.join(tfolder,lcode)
            if (lcode != "en") and os.path.isdir(lfolder) and ("Main_Page.md" in os.listdir(lfolder)):
                l = QtCore.QLocale(lcode)
                lname = l.languageToString(l.language())
                if ("-" in lcode) or ("_" in lcode):
                    lname += " ("+l.country().name.decode("utf8")+")"
                ltr = l.nativeLanguageName()
                #print(lname)
                output += "| ![Flag "+lcode+"]("+self.wikifolder+"/"+self.imagefolder
                output += "/Flag-"+lcode+".jpg) ["+lname+" / "+ltr+"]("+self.wikifolder+"/"
                output += self.translationfolder+"/"+lcode+"/Main_Page.md) "
                if column == 3:
                    output += "|\n"
                    column = 1
                else:
                    column += 1
        output += "\n\n\n\n## Get involved"
        f = open(mainpage,"r")
        b = f.read()
        f.close()
        #b = b.replace("## Get involved",output)
        b = re.sub("\|\ \!\[Flag.*?\#\# Get involved",output,b,flags=re.DOTALL|re.MULTILINE)
        f = open(mainpage,"w")
        f.write(b)
        f.close()


### API docs


    def getAPIPages(self):

        """getAPIPages():
        Returns a list of API pages"""

        pages = [p for p in os.listdir(self.output) if (p.endswith("_API.md") and (not "Category" in p))]
        pages.extend([p + "_API.md" for p in PART_API_PAGES])
        return pages


    def rebuildAllAPI(self):

        """rebuildAllAPI():
        Rebuilds all the API pages"""

        apipages = self.getAPIPages()
        for apipage in apipages:
            self.rebuildAPIPage(apipage)


    def rebuildAPIPage(self,apipage):

        """rebuildAPIPage(apipage):
        Rebuilds an API page"""

        def make_icon(icon):
            return "<img src=\""+icon+"\" style=\"width:16px;\"> "

        apipages = self.getAPIPages()
        modname = apipage.split("_")[0]
        md = "# " + modname + " API\n\n"
        module = None
        if modname == "Object":
            d = FreeCAD.newDocument()
            module = d.addObject("App::FeaturePython","Test")
        elif modname == "ViewObject":
            import FreeCADGui
            d = FreeCAD.newDocument()
            o = d.addObject("App::FeaturePython","Test")
            module = o.ViewObject
        elif modname == "Selection":
            #import FreeCADGui
            #module = FreeCADGui.Selection
            pass # TODO : handle this
        elif modname in ["Console","Vector","Matrix","Base","Placement"]:
            module = getattr(FreeCAD,modname)
        elif modname == "TopoShape":
            import Part
            module = Part.Shape
        elif modname in PART_API_PAGES:
            import Part
            module = getattr(Part,modname)
        else:
            import importlib
            try:
                module = importlib.import_module(modname)
            except:
                print("Unable to import module",modname)
        if module:
            import inspect
            if module.__doc__:
                md += module.__doc__
            else:
                md += "This page is an auto-generated Python API documentation, "
                md += "including variables, classes and functions for module " + modname + "\n"
            md += "\n\n\n\n"
            builtins = ""
            modules = ""
            types = ""
            others = ""
            for membername in [m for m in dir(module) if not(m.startswith("_"))]:
                member = getattr(module,membername)
                membertype = str(type(member))
                memberattrs = None
                if callable(member):
                    try:
                        memberattrs = str(inspect.signature(member))
                    except:
                        pass
                mmd = "#### "
                if ("builtin" in membertype) or ("function" in membertype):
                     mmd += make_icon(self.icon_function)
                elif("module" in membertype):
                    mmd += make_icon(self.icon_module)
                elif("Type" in membertype):
                    mmd += make_icon(self.icon_type)
                else:
                    mmd += make_icon(self.icon_builtin)
                if (membername+"_API.md") in apipages:
                    mmd += "[" + membername +"](" + membername +"_API.md)"
                else:
                    mmd += membername
                if memberattrs:
                    mmd += " <small>" + memberattrs + "</small>"
                mmd += "\n\n"
                if member.__doc__:
                    d = member.__doc__.strip()
                    d = re.sub("---+"," ",d)
                    if d.startswith(membername):
                        d = re.sub(membername+".*?\:","",d).strip()
                    #d = re.sub("    ","",d)
                    mmd += d
                mmd += "\n\n\n\n"
                if ("builtin" in membertype) or ("function" in membertype):
                    builtins += mmd
                elif("module" in membertype):
                    modules += mmd
                elif("Type" in membertype):
                    types += mmd
                else:
                    others += mmd
            if types:
                md += "### Attributes\n\n" + types        
            if builtins:
                md += "### Functions\n\n" + builtins
            md += others
            if modules:
                md += "### Modules\n\n" + modules
        md += "\n\n"
        md = self.addFooter(apipage[:-3],md)
        fname = os.path.join(self.output,apipage)
        with open(fname,"w") as apifile:
            apifile.write(md)
        print("Regenerated",apipage)


    def rebuildTOC(self):

        """rebuildTOC():
        Rebuilds the Online Help TOC page"""

        tocpage = "Online_Help_Toc.md"
        fname = os.path.join(self.output,tocpage)
        hubs = ["User hub","Workbenches","Power users hub","Developer hub",
                "Manual Summary","Category_API"]
        hubnames = ["Users documentation","Workbenches","Power users documentation",
                    "Developers documentation","Manual","API documentation"]
        skipped = ["Wikipedia","WikiPages","Hubs","Documentation index","Workbenches",
                   "Here","Developer Documentation","Manual.md",tocpage,"Speeding_up"]
        md = ""
        for i in range(5):
            md += "- [" + hubnames[i] + "](" + hubs[i].replace(" ","_") + ".md)\n"
            for l in self.getLinks(hubs[i]):
                title = l[1].upper() + l[2:]
                if title.startswith("Std Base"):
                    title = "Standard tools"+title[8:]
                l = "[" + title
                l = l[:l.index("(")+1] + l[l.index("(")+1].upper() + l[l.index("(")+2:]
                if (i == 0) and ("Workbench" in l):
                    continue
                if any(sk in l for sk in skipped):
                    continue
                if not l in md:
                    md += "    - " + l + "\n"
        with open(fname,"w") as tocfile:
            tocfile.write(md)
        print("Regenerated",tocpage)



### GENERAL FUNCTIONS (USABLE THROUGH COMMAND-LINE)



def init():

    """performs an initial import. Doesn't write anything to disk"""

    wiki = MediaWiki()
    wiki.getPageNames()
    wiki.getCategories()
    wiki.getAllPages()
    print("All done!")


def update():

    """performs a full update of the local contents from the wiki, updates pages and images on disk"""

    wiki = MediaWiki()
    oldrevisions = wiki.readRevisions()
    wiki.getPageNames()
    wiki.getCategories()
    if not wiki.pagecontents:
        wiki.getAllPages()
    newrevisions = wiki.getRevisions()
    pageset = wiki.updateRevisions(oldrevisions,newrevisions)
    print("Writing",len(pageset),"pages...")
    errors = []
    count = 1
    for page in pageset:
        wiki.printProgress(count,len(pageset),"Saving page "+page+"...")
        r = wiki.writeMarkdown(page,overwrite=True)
        if r:
            errors.append(r)
        count += 1
    wiki.printProgress()
    wiki.getAllImages()
    wiki.updateReadme()
    wiki.rebuildAllAPI()
    wiki.rebuildTOC()
    print("All done!\n")
    if errors:
        print("page with write errors: ",errors)
    push()


def test(page=None,clean=True):

    """creates a couple of pages for testing"""

    w = MediaWiki()
    if page:
        w.writeMarkdown(page,clean=clean)
    else:
        w.writeMarkdown("Main_Page",clean=clean)
        w.writeMarkdown("User_hub",clean=clean)
        w.writeMarkdown("Arch_Workbench",clean=clean)
        w.writeMarkdown("BIM_Workbench",clean=clean)
        w.writeMarkdown("Arch_Wall",clean=clean)
        w.writeMarkdown("Draft_Line",clean=clean)
        w.writeMarkdown("Part_Extrude",clean=clean)
        #w.writeMarkdown("Arch_Workbench",basepath=os.path.dirname(__file__)+"/orig",clean=False)
        #w.writeMarkdown("Arch_Wall",basepath=os.path.dirname(__file__)+"/orig",clean=False)
        #w.writeMarkdown("Draft_Line",basepath=os.path.dirname(__file__)+"/orig",clean=False)
        #w.writeMarkdown("Part_Extrude",basepath=os.path.dirname(__file__)+"/orig",clean=False)

def testpage(page):

    """gets and rebuilds a single page (for debugging use)"""

    wiki = MediaWiki()
    wiki.getPage(page)
    wiki.writeCache()
    wiki.writeMarkdown(page)
    print("Wrote",page)

def writepages():

    """writes all pages to disk, overwriting existing ones"""

    wiki = MediaWiki()
    #wiki.update()
    wiki.writeAllPages()


def writeimages():

    """downloads and write all images. Existing images are skipped"""

    wiki = MediaWiki()
    #wiki.update()
    wiki.getAllImages()


def updatereadme():

    """updates the README.md with the list of translations"""

    wiki = MediaWiki()
    wiki.updateReadme()


def push():

    """pushes to the remote git repo, if configured"""

    txt = "update " + str(date.today())
    repo = git.Repo(os.path.curdir)
    repo.git.add(WIKIFOLDER)
    repo.index.commit(txt)
    origin = repo.remote(name='origin')
    origin.push()
    print("Successfully committed",txt)



### COMMAND-LINE USAGE



if __name__ == "__main__":

    args = sys.argv[1:]

    # execute function
    if len(args) == 1:
        arg = args[0]
        if arg.startswith("--"):
            arg = arg[2:]
            if arg in globals():
                if callable(globals()[arg]):
                    globals()[arg]()
                    exit(0)

    # execute function with argument
    elif len(args) == 2:
        arg1 = args[0]
        arg2 = args[1]
        if arg1.startswith("--"):
            arg1 = arg1[2:]
            if arg1 in globals():
                if callable(globals()[arg1]):
                    globals()[arg1](arg2)
                    exit(0)

    # print help text
    funcs = "    Available functions:\n\n"
    for name in list(globals().keys()):
        if (name not in ["MediaWiki","Wrn","Log","Msg","Err","datetime","date",
                         "removeFromPath","FCADLogger","IntEnum","Scheme"]):
            if callable(globals()[name]):
                if globals()[name].__doc__:
                    funcs += "    --" + name + " : " + globals()[name].__doc__ + "\n"
    print(__doc__.replace("    See bottom of file for available functions",funcs))
