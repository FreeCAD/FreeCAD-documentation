# Release process
**'''<big>NOTE: 
1) THIS PAGE NEEDS TO BE ADAPTED TO FREECAD <br/>
2) PLEASE DO NOT TRANSLATE THIS PAGE <br/>
3) THIS PAGE IS MISSING TECHNICAL DETAIL (git commands, bash commands etc...)</big>'''**

The aim of this page is to gather ideas and organize things so official releases of FreeCAD require less work, and therefore can happen more often. This topic is discussed on this [forum thread](http://forum.freecadweb.org/viewtopic.php?f=8&t=6441).

## General ideas 

-   The \"target release\" field of the [tracker](http://www.freecadweb.org/tracker) should be used more, even on bugs that are not assigned to anybody, to mark bugs that we find important to solve before a release, or features we are working on, so others are aware of \"how close\" we are to release. This appears on the [roadmap](http://freecadweb.org/tracker/roadmap_page.php).
-   We should find a way to process the list below (A \"tickable\" list somewhere?)

## Planning

-   Ideally official releases should happen each 3 to 6 months
-   A signal should be emitted (by [jriegel](User:Jriegel.md)?) before the release (3 weeks?) so:
    -   No more new feature gets introduced, only bug fixes
    -   The strings are collected and uploaded to crowdin for translation
    -   The documentation can be fully updated
    -   The release notes can be prepared/finished

# Release management 

Preparing FreeCAD for a release

## Release Day - 3 weeks - Feature Freeze 

1.  Forum post announcing the feature freeze and asking for testing
2.  Start changing the version number in the FreeCAD docs
3.  Announce to all Workbench maintainers on FreeCAD-Addons know to prepare
4.  Announce to all Macro creators on FreeCAD-Macros know to prepare
5.  Asking wiki editors/translators to prepare for upcoming release. Make sure relevant pages are up-to-date and reaching completion:

:   

    :   [Workbench\_KEY](Workbench_KEY.md)
    :   [Workbench\_ICON](Workbench_ICON.md)

## Release Day - 2 weeks - String Freeze 

1.  Update and commit new .ts files
2.  Push translation files to Crowdin, use [Crowdin Scripts](Crowdin_Scripts.md)
3.  Send a message to all FreeCAD translators about the deadline of the upcoming release \-- set the deadline for delivering the translations to e.g. \"Release Day -3 day\"
    -   To message all translators on Crowdin: Log in to Crowdin and make an announcement (TODO: add link here)

## Release Day - 1 week 

1.  Send the final version of the (short) release announcement to all translators, asking them to translate it into their languages \-- set the deadline for delivering the translations to e.g. \"Release Day -1 day\"

## Release Day - 3 days 

1.  Finish the release notes
2.  Finish PR spiel for the forum and wiki/website.
3.  Announce to all FC translators [(see Release t-2 weeks)]({{PAGENAME}}#Release_Day_-_2_weeks.md) that the deadline for their translations is about to pass

## Release Day - 2 days 

-   Update years in source files
-   Update the python API doc pages - [yorik](User:Yorik.md)

## Release Day - 1 day 

-   Commit a new splash and about screen image, and update all versions in a number of source code locations:

:\* README.md

:\* appveyor.yml

:\* CMakeLists.txt

:\* src/Tools/offlinedoc/buildqhelp.py

:\* src/XDGData/org.freecadweb.FreeCAD.appdata.xml

:\* vagrant/Xenial/generate_yaml.sh

:\* vagrant/Xenial/bin/launcher

:\* vagrant/generate_yaml.sh

:\* vagrant/FreeCAD.sh

:\* Prepare a packager\'s release files and alert the packagers.

-   Tag the new release

:\* TODO: relevant git commands

## Release Day 

### Pre Release 


<div class="mw-collapsible mw-collapsed toccolours">

**Steps to take for Pre-Release**


<div class="mw-collapsible-content">

-   Prepare signed source tarballs and upload both the tarballs and the signatures to SourceForge. X.Y.Z refers to the version being released.

1.  Check out from git from the release tag:

:   gelevant git command


<li>

Change to the Release\_X.Y.Z directory:


</li>


:   cd Release_X.Y.Z


<li>

Rename freecad directory to freecad-X.Y.Z:


</li>


:   mv freecad freecad-X.Y.Z


<li>

Run the tar process - we need this file for all of the compression types we want so we do this first:


</li>


:   tar -cvf freecad-X.Y.Z.tar freecad-X.Y.Z/


<li>

Compress the files:


</li>


:   XZ: xz -k -e -v -z freecad-X.Y.Z.tar
:   7Zip: 7z a freecad-X.Y.Z.tar.7z freecad-X.Y.Z.tar
:   BZ2: bzip2 -k freecad-X.Y.Z.tar.bz2
:   GZ: gzip -c freecad-X.Y.Z.tar > freecad-X.Y.Z.tar.gz


<li>

GPG Sign the files:


</li>


:    --sign --detach-sign --armor freecad-X.Y.Z.tar.7z
:    --sign --detach-sign --armor freecad-X.Y.Z.tar.gz
:    --sign --detach-sign --armor freecad-X.Y.Z.tar.xz
:    --sign --detach-sign --armor freecad-X.Y.Z.tar.bz2


<li>

Verify the files:


</li>


:   gpg --verify freecad-X.Y.Z.tar.7z.asc freecad-X.Y.Z.tar.7z
:   gpg --verify freecad-X.Y.Z.tar.bz2.asc freecad-X.Y.Z.tar.bz2
:   gpg --verify freecad-X.Y.Z.tar.gz.asc freecad-X.Y.Z.tar.gz
:   gpg --verify freecad-X.Y.Z.tar.xz.asc freecad-X.Y.Z.tar.xz


<li>

Create the new directory on Sourceforge for the X.Y.Z version. Set it to staging:


</li>


:   Under TODO: verify find the correct path [sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad/freecad/X.Y.Z](sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad/freecad/X.Y.Z)
:   OR
:   TODO: verify find the correct path [sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad-devel/freecad/X.Y.Z](sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad-devel/freecad/X.Y.Z)


<li>

Upload to SourceForge:


</li>


:   Select FreeCAD directories, then the version number:
:   Eg to: TODO: verify find the correct path [sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad/freecad/X.Y.Z](sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad/freecad/X.Y.Z)
:   OR
:   TODO: verify find the correct path [sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad-devel/freecad/X.Y.Z](sftp://frs.sourceforge.net/home/frs/project/f/fr/freecad-devel/freecad/X.Y.Z)


</ol>

-   Send a Release post to the forum.


</div>


</div>

#### Translations

1.  Pull Translations from Crowdin using the [Crowdin Scripts](Crowdin_Scripts.md) (which will pull all Crowdin maintained languages)

### Post Release 

1.  Update the current version in the wiki

    :   [Download](Download.md) page
    :   [Installing on Linux](Installing_on_Linux.md) page
    :   Template: [Template:Stable-Version](Template:Stable-Version.md)
    :   Template: [Template:Development-Version](Template:Development-Version.md)
    :   Template: [Template:DownloadUnixStable](Template:DownloadUnixStable.md)
    :   Template: [Template:DownloadMacStable](Template:DownloadMacStable.md)
    :   Template: [Template:DownloadWindowsStable](Template:DownloadWindowsStable.md)
    :   [AppImage](AppImage.md)
    :   Where else?
2.  Release announcement to the forum
3.  Unleash the translators, asking them to send their translated release announcements to local media
4.  Update external locations that feature FreeCAD
    -   [Freshcode](http://freshcode.club/projects/freecad) ([could be automated if we set up Github correctly](https://github.com/luzpaz/FreeCAD-dependencies/issues/5))
    -   Check sourceforge
    -   Check [repology](https://repology.org/metapackage/freecad/badges) and track distros that haven\'t updated to the latest stable

### After Specific releases 

1.  Things that have to be done / updated after a specific release (remove them as soon as they\'re done)

## Tasks

**NOTE: These need to be integrated in to the above**

These are the tasks required for each release, with the name of the person responsible for it. Add your name if you want to take care of a task!

-   Giving the signal to the release (3 weeks before?)
-   Gathering the strings to translate and uploading them on crowdin via [Crowdin Scripts](Crowdin_Scripts.md) - [yorik](User:Yorik.md)
-   Announce on the forum and on social networks that translation is needed (this needs to be done several times) - [yorik](User:Yorik.md)
-   Set the splashscreen - [yorik](User:Yorik.md)
-   Unassigned - Update dependencies in README
-   Unassigned - Change the version number in the FreeCAD code
-   Unassigned - Check that all workbenches pages on the wiki are up-to-date (all their commands are listed), list missing pages
-   Unassigned - Manage the updates of the wiki
-   Unassigned - Manage the release notes (ex. [Release\_notes\_0.xx](Release_notes_0.xx.md))
-   Unassigned - Update ChangeLog.txt (we refer people to mantisbt changelog)
-   Merge back the translations from crowdin - [yorik](User:Yorik.md)
-   Unassigned - Check the german translation
-   Unassigned - Check the french translation
-   Unassigned - Check the other translations that have reached 100% (add them here)
-   Unassigned - Tag the exact release commit in git
-   Unassigned - Make the Windows 32bit build
-   Unassigned - Make the Windows 64bit build
-   Unassigned - Make the MacOS build
-   Unassigned - Make the Ubuntu stable build
-   Unassigned - Make the appImage build
-   Unassigned - Make the flatpak build
-   Unassigned - Make the snap build
-   Unassigned - Check the Windows 32bit build
-   Unassigned - Check the Windows 64bit build
-   Unassigned - Check the MacOS build
-   Unassigned - Check the Ubuntu build
-   Unassigned - Check the appImage build
-   Unassigned - Check the flatpak build
-   Unassigned - Check the snap build
-   Unassigned - Communicate the release to package managers of linux distributions (debian, fedora, arch)
-   Unassigned - Communicate the release to package managers of MacOS (homebrew, macports, fink)
-   Unassigned - Communicate the release to package managers of Windows (chocolatey)
-   Update the release numbers on the tracker - [yorik](User:Yorik.md)
-   Update the release numbers and download locations on the main web page for all languages - [yorik](User:Yorik.md)
-   Unassigned - Official release announcement on the FreeCAD web page
-   Unassigned - Spread it around. see chapter Publicity
-   Unassigned - Update the example splash for all \*.appdata.xml (ex. [FreeCAD/package/fedora/freecad.appdata.xml](https://github.com/FreeCAD/FreeCAD/blob/master/package/fedora/freecad.appdata.xml))
-   Try to bump all 3rd party deps to the minimum version to build FreeCAD in the package ecosystem via <https://github.com/luzpaz/FreeCAD-dependencies>

## Publicity

This is a raw list of sites and blogs that have at some point mentioned FreeCAD. It is mostly harvested from <http://forum.freecadweb.org/viewtopic.php?f=8&t=143> (until June 29th 2014). Feel free to add more pages or assign one or more pages to yourself to take care of notifying them about a new release of FreeCAD.


<div class="mw-collapsible mw-collapsed toccolours">

**Links for PR**


<div class="mw-collapsible-content">

### Social networks 

-   <http://plus.google.com/107660967460246172334/posts>
-   [yorik](User:Yorik.md) - <http://www.facebook.com/FreeCAD> (also updates <http://twitter.com/FreeCADNews> automatically)

### News Sites 

-   <http://makezine.com/>
-   <http://www.webupd8.org/>
-   <http://libregraphicsworld.org/>
-   <http://www.techrepublic.com/>
-   <http://www.linuxjournal.com/>
-   <http://www.reddit.com/r/freecad> (or <http://www.reddit.com/r/cad/>)
-   <http://hackaday.com/contact-hack-a-day/>
-   <http://www.linuxformat.com/>
-   <http://www.inside3dp.com/>
-   <http://diy3dprinting.blogspot.com/>

### Other Sites 

-   <http://www.bld3r.com/>
-   <http://forum.lulzbot.com/viewforum.php?f=30>
-   <http://cad.about.com/>
-   <http://en.wikipedia.org/wiki/FreeCAD>
-   <http://forum.diigiit.com/>

### Spanish

-   <http://www.taringa.net/>

### Blogs

-   <http://www.junauza.com/>
-   <http://www.blender3darchitect.com/>
-   <http://linuxaideddesign.blogspot.de/>
-   <http://www.techdrivein.com/>
-   <http://sliptonic.com/>
-   <http://opensourcedesigntools.blogspot.de/>
-   <http://yorik.uncreated.net> - [yorik](User:Yorik.md)

### French

-   <http://www.linuxgraphic.org/>
-   <http://www.freecad-france.com/>

### Portugese

-   <http://www.geosaber.com.br/> (not sure how appropriate/relevant)

### Spanish 

-   <http://www.iearobotics.com/blog/>

### Italian

-   <http://ingegnerialibera.altervista.org/blog/doku.php>

### Polish

-   <http://www.ubucentrum.net>
-   <http://wkupiesila.blogspot.com>
-   <http://cadblog.pl>
-   <http://jakilinux.org/>

### Chinese

-   <http://www.lirui.name/post/208.html>


</div>


</div>




[Category:Roadmap](Category:Roadmap.md) [Category:Administration](Category:Administration.md)

---
[documentation index](../README.md) > Release process
