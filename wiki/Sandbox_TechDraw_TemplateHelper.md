# Sandbox:TechDraw TemplateHelper
{{TOCright}}

## Introduction

This document is about creating a drawing template and to insert into a FreeCAD file using a Python macro.

I managed to automate my drawing generation with a Python script which

:\* generates a temporary svg template of the desired size (DIN A formats so far\...)

:\* inserts this temporary template into the active FreeCAD document

:\* fills some values into the editable text fields

The development was somehow chaotic, because I\'m still learning Python and some solution may seen to be a little odd - but it works at least\...

Now I\'d like to share what I have learned and coded so far and rewrite it in a tidier way.

I think it is better to show how to solve certain problems rather than just presenting a somehow finished macro.

Anyone is invited to borrow some code and develop similar or hopefully better tools that make handling drawings easier.

This sandbox is to start my documentation. At some further state it may be split into several pages for easier use.

## Task list 

To automatically generate a drawing page we need to know

:\* how to insert a template into a FreeCAD document

:\* how to set up a user interface to set some page parameters

:\* how to generate a template

:\* how to manipulate editable texts

## Insert a page and template 

Usually a template will be inserted into the active FreeCAD document which means a FreeCAD must be running and a file must be opened.

As this macro is launched from within a FreeCAD file the only variables that needs to be set are

:\* templatePath, the path to the template folder and

:\* templateName, the name of the template to be inserted.

(MyTemplate.svg is the name for the generated template in a following section. Change it to test the macro with your favourite template.)

(This has still to be done manually before running the macro as long as I\'m not sure where to read the path variable \...)

An object to address the active document is introduced and named activeDoc.

And finally two variables are filled with the names of the generated page and template. (I prefer 2 digits for the numbers in contrast to FreeCAD)

### Insert just one page and template 


<div class="mw-collapsible mw-collapsed toccolours">

Code to add a page and insert a template


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- set the template path to the directory where your templates are stored
templatePath = "/Users/.../FreeCAD/Templates/"
templateName = "MyTemplate.svg"

# --- Main section ---

# -- Add a page and a template to the active document --

activeDoc = App.activeDocument()

newPage = 'Page01'
newTemplate = 'Template01'

# add a page object to the active document
activeDoc.addObject('TechDraw::DrawPage',newPage)

# add a template object to the active document
activeDoc.addObject('TechDraw::DrawSVGTemplate',newTemplate)

# load the svg template into the template object
activeDoc.getObject(newTemplate).Template = templatePath+templateName

# add the template object to the page's object list
activeDoc.getObject(newPage).Template = activeDoc.getObject(newTemplate)

# rename 'Page' to 'Sheet'
activeDoc.getObject(newPage).Label = 'Sheet ' + newPage[4:]

# open the page object for editing
activeDoc.getObject(newPage).ViewObject.doubleClicked()
}}

:\* A page object and a template object are added to the active document\'s object list.

:\* The content of the svg document is loaded into the template object.

:\* The template object is put onto the page\'s objects list.

:\* Drawings are on sheets rather than on pages and so they are renamed.

:   Since the property \"Name\" cannot be changed the property \"Label\" must be altered.
    -   Finally the drawing view is opened and activated for editing.


</div>


</div>

### Insert more than just one page and template 

The above code works for single pages only. It needs some extra lines to detect existing pages and to increment the page number.

The macro tries to read the property label of Page01 to detect if page01 exists. If it doesn\'t it will be created.

If it exists the page number will be incremented and the next try to detect a page starts.


<div class="mw-collapsible mw-collapsed toccolours">

Code to check for existing pages to add a first page or yet another


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- set the template path to the directory where your templates are stored
templatePath = "/Users/.../FreeCAD/Templates/"
templateName = "MyTemplate.svg"

# --- Main section ---

# -- Add a page and a template to the active document --

activeDoc = App.activeDocument()

newPage = 'Page01' # first page name to start search

# to find the current page number to create
pageCount = 1
pageFound = True
while pageFound:
    try:
        print(activeDoc.getObject(newPage).Label)
    except AttributeError:
        print(newPage + " to be created")
        pageFound = False
    else:
        pageCount = pageCount + 1
        if pageCount < 10:
            newPage = newPage[0:4] + '0' + str(pageCount)
        else:
            newPage = newPage[0:4] + str(pageCount)

# set template number according to page number
newTemplate = ('Template' + newPage[4:])

# add a page object to the active document
activeDoc.addObject('TechDraw::DrawPage',newPage)

# add a template object to the active document
activeDoc.addObject('TechDraw::DrawSVGTemplate',newTemplate)

# load the svg template into the template object
activeDoc.getObject(newTemplate).Template = templatePath+templateName

# add the template object to the page's object list
activeDoc.getObject(newPage).Template = activeDoc.getObject(newTemplate)

# rename 'Page' to 'Sheet'
activeDoc.getObject(newPage).Label = 'Sheet ' + newPage[4:]

# open the page object for editing
activeDoc.getObject(newPage).ViewObject.doubleClicked()
}}


</div>


</div>

I recommend to save the file after each added page.

## Generate a template 

A template provides a background for the drawing tasks. The template\'s dimensions are used by the printer drivers to scale the drawing correctly.

The templates are svg-files and so the macro has to write lines of svg code (which is a subset of xml code).

### Generate a simple blank page template 

This macro shows the principle how an svg-file can be put together. (Format is A3)


<div class="mw-collapsible mw-collapsed toccolours">

Code to create a simple svg-file


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- set the template path to the directory where your templates are stored
templatePath = "/Users/.../FreeCAD/Templates/"
templateName = "MyTemplate.svg"

# - SVG creation -

#- Create a file and insert a header line
#   (with t as the space saving variant of template)
def CreateSvgFile(filePath):
    t=open(filePath,"w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(filePath):
    t=open(filePath,"a") # a = append, new lines are added at the end of an existing file
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(filePath):
    t=open(filePath,"a")
    t.write("</svg>")
    t.close

# --- Main section ---

CreateSvgFile(templatePath+templateName) # overwrites existing File

# Set sheet format (DIN A3)
formatWidth  = "420"
formatHeight = "297"

StartSvg(templatePath+templateName)  # adds Start tag and namespaces
CreateSheet(templatePath+templateName, formatWidth, formatHeight)
EndSvg(templatePath+templateName)
# At this point a new SVG-file is generated and saved
}}


:   The result, a simple template for a blank page (A3 landscape):


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width ="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}


:   The main principle is to open a file for writing and so start an svg-file from scratch, write the header line and close the file as a first step.
:   After that the file will be repeatedly opened to append further segments and closed again after appending.
:   (The FreeCAD namespace is an investment into the future when editable texts come into play)


</div>


</div>

Now some ink will be added to the blank page:

### Add code segments to\... 

The following code segments are to be added to the above code. They should placed between the svg-tags.

They are usually split in a part to collect data for parameter values and one part to create the Python code lines with given parameters.

All functions dealing with **formatWidth** and **formatHeight** can create svg-code to match each DIN format from A4 to A0.

#### \... create frames 

Code segments (to create the svg-instructions) to draw two rectangles, one for a sheet frame and one around the drawing area.


<div class="mw-collapsible mw-collapsed toccolours">

Additional code to create frames


<div class="mw-collapsible-content">


{{Code| |code=
# - SVG creation -
class ToteBag:
    pass
# This class is empty to act as a container for several variables
#- one bag for drawing borders
borders = ToteBag()

#- set default values - custom values may be added 
def setDINBorderValues(format):
    borders.drawingAreaTop    = 10 # distance from page boundary
    borders.drawingAreaBottom = 10
    borders.drawingAreaLeft   = 20
    borders.drawingAreaRight  = 10
    borders.sheetFrameTop     = 5  # distance from drawing area border
    borders.sheetFrameBottom  = 5
    borders.sheetFrameLeft    = 5
    borders.sheetFrameRight   = 5

#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine

#- Frame creation
def CreateFrame(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight

    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(dAL)
    drawingY=str(dAT)
    #- lower right corner
    drawingWidth=str(int(shWidth)-dAR)
    drawingHeight=str(int(shHeight)-dAB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(shWidth)-dAL-dAR)
    drawingHeight=str(int(shHeight)-dAT-dAB)
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(dAL-sFL)
    drawingY=str(dAT-sFT)
    #- lower right corner
    drawingWidth=str(int(shWidth)-dAR+sFR)
    drawingHeight=str(int(shHeight)-dAB+sFB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(shWidth)-dAL-dAR+sFL+sFR)
    drawingHeight=str(int(shHeight)-dAT-dAB+sFT+sFB)
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

# --- Main section ---

#borders = ToteBag()
setDINBorderValues('A3')

CreateFrame(templatePath+templateName, formatWidth, formatHeight)
}}


:   Each write instruction has to start with a specific number of blank spaces for the correct indentation of the resulting svg-file.
:   The toteBag class is used to collect and distribute global values. I\'m not sure yet if this really makes sense\...


</div>


</div>

#### \... to add index fields 

Code segments to calculate a few parameters based on sheet dimensions and then create code to place the separator lines, index letters and numbers and a few lines to help folding this drawing and placing a puncher. Additional functions to create several path and text instructions for the svg-file.


<div class="mw-collapsible mw-collapsed toccolours">

Additional code to create index fields


<div class="mw-collapsible-content">


{{Code| |code=
# SVG creation

#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine

#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine

#- Indexes and folding marks creation
def CreateDecoration(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"index-separators\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.25;\
stroke-linecap:round\">\n")
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight
    drawingX=str(dAL)
    drawingY=str(dAT)
    drawingWidth=str(int(shWidth)-dAL-dAR)
    drawingHeight=str(int(shHeight)-dAT-dAB)

    #- starting point values of center lines
    indexCenter=str(int(drawingWidth)/2+dAL)
    indexMiddle=str(int(drawingHeight)/2+dAT)
    indexLeft=str(dAL+5)
    indexRight=str(int(drawingWidth)+dAL-5)
    indexUpper=str(dAT+5)
    indexLower=str(int(drawingHeight)+dAT-5)

    #- centre and middle markings of drawing area
    if shWidth=="210": # format=="DIN-A4":
        indexLeft=str(dAL)
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-15")+"\n")
    elif shWidth=="420": # format=="DIN-A3":
        indexLeft=str(dAL+5)
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-20")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")
    else :
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-10")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")

    #- starting point values of separator lines
    indexLeft =str(dAL)
    indexRight=str(int(drawingWidth)+dAL)
    indexUpper=str(dAT)
    indexLower=str(int(drawingHeight)+dAT)

    #- set number of horizontal and vertical indexes
    if shWidth=="420": # format=="DIN-A3":
        indexCountX=8
        indexCountY=6
    elif shWidth=="594": # format=="DIN-A2":
        indexCountX=12
        indexCountY=8
    elif shWidth=="841": # format=="DIN-A1":
        indexCountX=16
        indexCountY=12
    elif shWidth=="1189": # format=="DIN-A0":
        indexCountX=24
        indexCountY=16
    else :
        indexCountX=0
        indexCountY=0

    #- indexCenter and indexMiddle contain strings but floating point
    #   numbers are needed to calculate
    floatCenter=int(drawingWidth)/2+dAL
    floatMiddle=int(drawingHeight)/2+dAT

    #- horizontal index separators
    max=int(indexCountX/2-1)
    for value in range(0,max):
        indexX=str(floatCenter+(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")
        indexX=str(floatCenter-(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")

    #- vertical index separators
    max=int(indexCountY/2-1)
    for value in range(0,max):
        indexY=str(floatMiddle+(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")
        indexY=str(floatMiddle-(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")

    t.write("    </g>\n")

    t.write("    <g id=\"indexes\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:middle;fill:#000000;\
    font-family:osifont\">\n")

    #- position point values of indexes
    indexLeft=str(dAL-sFL/2)
    indexRight=str(int(drawingWidth)+dAL+sFR/2)
    indexUpper=str(dAT-1)
    indexLower=str(int(drawingHeight)+dAT+sFB-1)

    #- horizontal indexes, numbers
    max=int(indexCountX/2)
    for value in range(0,max):
        indexX=str(floatCenter+value*50+25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2+value+1)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2+value+1)))+"\n")
        indexX=str(floatCenter-value*50-25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2-value)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2-value)))+"\n")

    #- vertical indexes, letters
    max=int(indexCountY/2)
    for value in range(0,max):
        indexY=str(floatMiddle+value*50+25)
        if int(indexCountY/2+value+1)>9 :  # to avoid the letter J
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
        else :
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
        indexY=str(floatMiddle-value*50-25)
        t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2-value)))+"\n")
        t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2-value)))+"\n")

    t.write("    </g>\n\n")

    #- puncher mark
    t.write("    <g id=\"puncher mark\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if shWidth in["1189", "841", "594"] : # A3 and A4 have extended middle markings
        t.write("        "+svgpath(str(dAL-sFL),str(int(formatHeight)-(297/2)),"h","-10")+"\n")
    t.write("    </g>\n\n")

    #- folding marks
    t.write("    <g id=\"folding marks\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if shWidth=="420": # DIN-A3
        t.write("        "+svgpath("125",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("125",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("230",str(dAT-sFT),"v","-5")+"\n")
        t.write("        "+svgpath("230",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
    elif shWidth=="594": # DIN-A2
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("402",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("402",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","123","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"123","h","  5")+"\n")
    elif shWidth=="841": # DIN-A1
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("651",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("651",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","297","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"297","h","  5")+"\n")
    elif shWidth=="1189": # DIN-A0
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("590",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("590",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("780",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("780",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("999",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("999",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","247","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"247","h","  5")+"\n")
        t.write("        "+svgpath("  5","544","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"544","h","  5")+"\n")

    t.write("    </g>\n\n")
    t.close

# --- Main section ---

CreateDecoration(templatePath+templateName, formatWidth, formatHeight)
}}


:   Comment.
:   More comments.


</div>


</div>

#### \... create title block elements 

Code segments (to create the svg-instructions) to draw

:\* a title block outline

:\* the inner segmentation

:\* static texts like e.g.labels for the text boxes

:\* editable texts, at least their placeholders

The first two points can be combined if only one line type and a single thickness is use.

All except the editable texts can be drawn in relation to the svg-file\'s origin as the base point of the title block and then be grouped to move them to the desired position in a single step.


<div class="mw-collapsible mw-collapsed toccolours">

Additional code to create a title block


<div class="mw-collapsible-content">


{{Code| |code=
#- Title block movable
def CreateTitleBlock(filePath,shWidth,shHeight):
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- lower left corner
    tbX=str(int(shWidth)-dAR-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(shHeight)-dAB)
    #- group to move allelements in one step
    t=open(filePath,"a")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    t.write("      \n\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0"," -4","h","155")+"\n")
    t.write("        "+svgpath("  0","-16","h","155")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("  0","-46.5","h"," 50")+"\n")
    t.write("        "+svgpath(" 25"," -4","v","-26")+"\n")
    t.write("        "+svgpath(" 50"," -4","v","-59")+"\n")
    t.write("        "+svgpath("140"," -4","v","-12")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("        "+svgpath("160","  0","v","-63")+"\n")
    t.write("        "+svgpath("155"," -7","h"," 25")+"\n")
    t.write("        "+svgpath("155","-14","h"," 25")+"\n")
    t.write("        "+svgpath("155","-21","h"," 25")+"\n")
    t.write("        "+svgpath("155","-28","h"," 25")+"\n")
    t.write("        "+svgpath("155","-35","h"," 25")+"\n")
    t.write("        "+svgpath("155","-42","h"," 25")+"\n")
    t.write("        "+svgpath("155","-49","h"," 25")+"\n")
    t.write("        "+svgpath("155","-56","h"," 25")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:2.5;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")

    t.write("        "+svgtext("  1.5","-60  ","Author Name:")+"\n")
    t.write("        "+svgtext("  1.5","-52  ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-43.5 ","Supervisor Name:")+"\n")
    t.write("        "+svgtext("  1.5","-35.5 ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-27  ","Format:")+"\n")
    t.write("        "+svgtext("  1.5","-13  ","Scale:")+"\n")
    t.write("        "+svgtext(" 26.5","-13  ","Weight:")+"\n")
    t.write("        "+svgtext(" 51.5","-27  ","Company:")+"\n")
    t.write("        "+svgtext(" 51.5","-13  ","Version:")+"\n")
    t.write("        "+svgtext("141.5","-13  ","Sheet")+"\n")
    t.write("      </g>\n")
    #- revision indexes, centered
    t.write("      <g id=\"titleblock-revision-indexes\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:middle;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("157.5"," -1.5  ","A")+"\n")
    t.write("        "+svgtext("157.5"," -8.5  ","B")+"\n")
    t.write("        "+svgtext("157.5","-15.5  ","C")+"\n")
    t.write("        "+svgtext("157.5","-22.5  ","D")+"\n")
    t.write("        "+svgtext("157.5","-29.5  ","E")+"\n")
    t.write("        "+svgtext("157.5","-36.5  ","F")+"\n")
    t.write("        "+svgtext("157.5","-43.5  ","G")+"\n")
    t.write("        "+svgtext("157.5","-50.5  ","H")+"\n")
    t.write("        "+svgtext("157.5","-57.5  ","I")+"\n")
    t.write("      </g>\n")t.write("    </g>\n\n")
    t.close


# --- Main section ---

CreateTitleBlock(templatePath+templateName, formatWidth, formatHeight)
}}

Now there will be a supergroup \"title block\" containing the groups \"titleblock-frame\", \"titleblock-text-non-editable\", and\"titleblock-revision-indexes\" in the resulting svg-file.


</div>


</div>

The editable texts are put into a separate group as they require absolute coordinates


<div class="mw-collapsible mw-collapsed toccolours">

Additional code to create a editable texts


<div class="mw-collapsible-content">


{{Code| |code=
#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine

#- Title block editable texts
def CreateEditableText(filePath,shWidth,shHeight):
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- offsets for editable texts
    edX=int(shWidth)-dAR-180 # 180 according to DIN EN ISO 7200
    edY=int(shHeight)-dAB

    t=open(filePath,"a")
    t.write("    <g id=\"titleblock-editable-owner\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")

    t.write("      "+FCeditext("Owner",str(edX+60),str(edY-27.0),"Owner")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-address\"\n")
    t.write("      style=\"font-size:2.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Address-1",str(edX+60),str(edY-23.5),"Address1")+"\n")
    t.write("      "+FCeditext("Address-2",str(edX+60),str(edY-20.0),"Address2")+"\n")
    t.write("      "+FCeditext("MailTo",   str(edX+60),str(edY-16.5),"MailTo")+"\n")
    t.write("      "+FCeditext("Copyright",str(edX+2), str(edY-1.0), "Copyright")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-medium\"\n")
    t.write("      style=\"font-size:5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Author",    str(edX+2),  str(edY-55.0),"Author")+"\n")
    t.write("      "+FCeditext("AuDate",    str(edX+7),  str(edY-47.5),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("Supervisor",str(edX+2),  str(edY-38.5),"Supervisor")+"\n")
    t.write("      "+FCeditext("SvDate",    str(edX+7),  str(edY-31.0),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("SubTitle",  str(edX+64), str(edY-42.0),"Sub-title")+"\n")
    t.write("      "+FCeditext("Version",   str(edX+60), str(edY-8.0), "Version")+"\n")
    t.write("      "+FCeditext("Revision-A",str(edX+162),str(edY-1.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-B",str(edX+162),str(edY-8.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-C",str(edX+162),str(edY-15.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-D",str(edX+162),str(edY-22.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-E",str(edX+162),str(edY-29.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-F",str(edX+162),str(edY-36.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-G",str(edX+162),str(edY-43.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-H",str(edX+162),str(edY-50.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-I",str(edX+162),str(edY-57.5),"______")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-centered\"\n")
    t.write("      style=\"font-size:5;text-anchor:middle;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Format", str(edX+12), str(edY-21),"A3")+"\n")
    t.write("      "+FCeditext("Sheets", str(edX+148),str(edY-8), "1 / 1")+"\n")
    t.write("      "+FCeditext("Scale",  str(edX+12), str(edY-8), "1 : 1")+"\n")
    t.write("      "+FCeditext("Weight", str(edX+35), str(edY-8), "___ kg")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-Large\"\n")
    t.write("      style=\"font-size:7;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Title",   str(edX+62),str(edY-50),"Drawing Title")+"\n")
    t.write("      "+FCeditext("PtNumber",str(edX+62),str(edY-32),"Part Number")+"\n")
    t.write("    </g>\n\n")
    t.close

# --- Main section ---

CreateEditableText(templatePath+templateName, formatWidth, formatHeight)
}}


</div>


</div>

### The resulting macro 

All sections put together give a macro like this:

:   (Don\'t forget to edit the template path and start the macro from within FreeCAD.)


<div class="mw-collapsible mw-collapsed toccolours">

Complete code to create a template


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- set the template path to the directory where your templates are stored
templatePath = "/Users/.../FreeCAD/Templates/"
templateName = "MyTemplate.svg"

# - SVG creation -

class ToteBag:
    pass
# This class is empty to act as a container for several variables
#- one bag for drawing borders
borders = ToteBag()

#- set values according to DIN XXX
def setDINBorderValues(format):
    borders.drawingAreaTop    = 10 # distance from page boundary
    borders.drawingAreaBottom = 10
    borders.drawingAreaLeft   = 20
    borders.drawingAreaRight  = 10
    borders.sheetFrameTop     = 5  # distance from drawing area border
    borders.sheetFrameBottom  = 5
    borders.sheetFrameLeft    = 5
    borders.sheetFrameRight   = 5

#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine

#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine

#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine

#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine

#- Create a file and insert a header line
def CreateSvgFile(filePath):
    t=open(filePath,"w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(filePath):
    t=open(filePath,"a") # a = append, new lines are added at the end of an existing file
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(filePath):
    t=open(filePath,"a")
    t.write("</svg>")
    t.close

#- Frame creation
def CreateFrame(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(dAL)
    drawingY=str(dAT)
    #- lower right corner
    drawingWidth=str(int(shWidth)-dAR)
    drawingHeight=str(int(shHeight)-dAB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(shWidth)-dAL-dAR)
    drawingHeight=str(int(shHeight)-dAT-dAB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(dAL-sFL)
    drawingY=str(dAT-sFT)
    #- lower right corner
    drawingWidth=str(int(shWidth)-dAR+sFR)
    drawingHeight=str(int(shHeight)-dAB+sFB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(shWidth)-dAL-dAR+sFL+sFR)
    drawingHeight=str(int(shHeight)-dAT-dAB+sFT+sFB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

#- Indexes and folding marks creation
def CreateDecoration(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"index-separators\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.25;\
stroke-linecap:round\">\n")
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight
    drawingX=str(dAL)
    drawingY=str(dAT)
    drawingWidth=str(int(shWidth)-dAL-dAR)
    drawingHeight=str(int(shHeight)-dAT-dAB)

    #- starting point values of center lines
    indexCenter=str(int(drawingWidth)/2+dAL)
    indexMiddle=str(int(drawingHeight)/2+dAT)
    indexLeft=str(dAL+5)
    indexRight=str(int(drawingWidth)+dAL-5)
    indexUpper=str(dAT+5)
    indexLower=str(int(drawingHeight)+dAT-5)

    #- centre and middle markings of drawing area
    if shWidth=="210": # format=="DIN-A4":
        indexLeft=str(dAL)
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-15")+"\n")
    elif shWidth=="420": # format=="DIN-A3":
        indexLeft=str(dAL+5)
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-20")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")
    else :
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-10")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")

    #- starting point values of separator lines
    indexLeft =str(dAL)
    indexRight=str(int(drawingWidth)+dAL)
    indexUpper=str(dAT)
    indexLower=str(int(drawingHeight)+dAT)

    #- set number of horizontal and vertical indexes
    if shWidth=="420": # format=="DIN-A3":
        indexCountX=8
        indexCountY=6
    elif shWidth=="594": # format=="DIN-A2":
        indexCountX=12
        indexCountY=8
    elif shWidth=="841": # format=="DIN-A1":
        indexCountX=16
        indexCountY=12
    elif shWidth=="1189": # format=="DIN-A0":
        indexCountX=24
        indexCountY=16
    else :
        indexCountX=0
        indexCountY=0

    #- indexCenter and indexMiddle contain strings but floating point
    #   numbers are needed to calculate
    floatCenter=int(drawingWidth)/2+dAL
    floatMiddle=int(drawingHeight)/2+dAT

    #- horizontal index separators
    max=int(indexCountX/2-1)
    for value in range(0,max):
        indexX=str(floatCenter+(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")
        indexX=str(floatCenter-(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")

    #- vertical index separators
    max=int(indexCountY/2-1)
    for value in range(0,max):
        indexY=str(floatMiddle+(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")
        indexY=str(floatMiddle-(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")

    t.write("    </g>\n")

    t.write("    <g id=\"indexes\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:middle;fill:#000000;\
    font-family:osifont\">\n")

    #- position point values of indexes
    indexLeft=str(dAL-sFL/2)
    indexRight=str(int(drawingWidth)+dAL+sFR/2)
    indexUpper=str(dAT-1)
    indexLower=str(int(drawingHeight)+dAT+sFB-1)

    #- horizontal indexes, numbers
    max=int(indexCountX/2)
    for value in range(0,max):
        indexX=str(floatCenter+value*50+25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2+value+1)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2+value+1)))+"\n")
        indexX=str(floatCenter-value*50-25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2-value)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2-value)))+"\n")

    #- vertical indexes, letters
    max=int(indexCountY/2)
    for value in range(0,max):
        indexY=str(floatMiddle+value*50+25)
        if int(indexCountY/2+value+1)>9 :  # to avoid the letter J
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
        else :
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
        indexY=str(floatMiddle-value*50-25)
        t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2-value)))+"\n")
        t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2-value)))+"\n")

    t.write("    </g>\n\n")

    #- puncher mark
    t.write("    <g id=\"puncher mark\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if shWidth in["1189", "841", "594"] : # A3 and A4 have extended middle markings
        t.write("        "+svgpath(str(dAL-sFL),str(int(formatHeight)-(297/2)),"h","-10")+"\n")
    t.write("    </g>\n\n")

    #- folding marks
    t.write("    <g id=\"folding marks\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if shWidth=="420": # DIN-A3
        t.write("        "+svgpath("125",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("125",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("230",str(dAT-sFT),"v","-5")+"\n")
        t.write("        "+svgpath("230",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
    elif shWidth=="594": # DIN-A2
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("402",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("402",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","123","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"123","h","  5")+"\n")
    elif shWidth=="841": # DIN-A1
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("651",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("651",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","297","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"297","h","  5")+"\n")
    elif shWidth=="1189": # DIN-A0
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("590",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("590",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("780",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("780",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("999",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("999",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","247","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"247","h","  5")+"\n")
        t.write("        "+svgpath("  5","544","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"544","h","  5")+"\n")

    t.write("    </g>\n\n")
    t.close

#- Title block movable
def CreateTitleBlock(filePath,shWidth,shHeight):
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- lower left corner
    tbX=str(int(shWidth)-dAR-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(shHeight)-dAB)
    #- group to move allelements in one step
    t=open(filePath,"a")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    t.write("      \n\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0"," -4","h","155")+"\n")
    t.write("        "+svgpath("  0","-16","h","155")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("  0","-46.5","h"," 50")+"\n")
    t.write("        "+svgpath(" 25"," -4","v","-26")+"\n")
    t.write("        "+svgpath(" 50"," -4","v","-59")+"\n")
    t.write("        "+svgpath("140"," -4","v","-12")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("        "+svgpath("160","  0","v","-63")+"\n")
    t.write("        "+svgpath("155"," -7","h"," 25")+"\n")
    t.write("        "+svgpath("155","-14","h"," 25")+"\n")
    t.write("        "+svgpath("155","-21","h"," 25")+"\n")
    t.write("        "+svgpath("155","-28","h"," 25")+"\n")
    t.write("        "+svgpath("155","-35","h"," 25")+"\n")
    t.write("        "+svgpath("155","-42","h"," 25")+"\n")
    t.write("        "+svgpath("155","-49","h"," 25")+"\n")
    t.write("        "+svgpath("155","-56","h"," 25")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:2.5;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")

    t.write("        "+svgtext("  1.5","-60  ","Author Name:")+"\n")
    t.write("        "+svgtext("  1.5","-52  ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-43.5 ","Supervisor Name:")+"\n")
    t.write("        "+svgtext("  1.5","-35.5 ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-27  ","Format:")+"\n")
    t.write("        "+svgtext("  1.5","-13  ","Scale:")+"\n")
    t.write("        "+svgtext(" 26.5","-13  ","Weight:")+"\n")
    t.write("        "+svgtext(" 51.5","-27  ","Owner:")+"\n")
    t.write("        "+svgtext(" 51.5","-13  ","Version:")+"\n")
    t.write("        "+svgtext("141.5","-13  ","Sheet")+"\n")
    t.write("      </g>\n")
    #- revision indexes, centered
    t.write("      <g id=\"titleblock-revision-indexes\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:middle;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("157.5"," -1.5  ","A")+"\n")
    t.write("        "+svgtext("157.5"," -8.5  ","B")+"\n")
    t.write("        "+svgtext("157.5","-15.5  ","C")+"\n")
    t.write("        "+svgtext("157.5","-22.5  ","D")+"\n")
    t.write("        "+svgtext("157.5","-29.5  ","E")+"\n")
    t.write("        "+svgtext("157.5","-36.5  ","F")+"\n")
    t.write("        "+svgtext("157.5","-43.5  ","G")+"\n")
    t.write("        "+svgtext("157.5","-50.5  ","H")+"\n")
    t.write("        "+svgtext("157.5","-57.5  ","I")+"\n")
    t.write("      </g>\n")

    t.write("    </g>\n\n")
    t.close

#- Title block editable texts
def CreateEditableText(filePath,shWidth,shHeight):
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- offsets for editable texts
    edX=int(shWidth)-dAR-180 # 180 according to DIN EN ISO 7200
    edY=int(shHeight)-dAB

    t=open(filePath,"a")
    t.write("    <g id=\"titleblock-editable-owner\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")

    t.write("      "+FCeditext("Owner",str(edX+60),str(edY-27.0),"Owner")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-address\"\n")
    t.write("      style=\"font-size:2.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Address-1",str(edX+60),str(edY-23.5),"Address1")+"\n")
    t.write("      "+FCeditext("Address-2",str(edX+60),str(edY-20.0),"Address2")+"\n")
    t.write("      "+FCeditext("MailTo",   str(edX+60),str(edY-16.5),"MailTo")+"\n")
    t.write("      "+FCeditext("Copyright",str(edX+2), str(edY-1.0), "Copyright")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-medium\"\n")
    t.write("      style=\"font-size:5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Author",    str(edX+2),  str(edY-55.0),"Author")+"\n")
    t.write("      "+FCeditext("AuDate",    str(edX+7),  str(edY-47.5),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("Supervisor",str(edX+2),  str(edY-38.5),"Supervisor")+"\n")
    t.write("      "+FCeditext("SvDate",    str(edX+7),  str(edY-31.0),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("SubTitle",  str(edX+64), str(edY-42.0),"Sub-title")+"\n")
    t.write("      "+FCeditext("Version",   str(edX+60), str(edY-8.0), "Version")+"\n")
    t.write("      "+FCeditext("Revision-A",str(edX+162),str(edY-1.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-B",str(edX+162),str(edY-8.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-C",str(edX+162),str(edY-15.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-D",str(edX+162),str(edY-22.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-E",str(edX+162),str(edY-29.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-F",str(edX+162),str(edY-36.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-G",str(edX+162),str(edY-43.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-H",str(edX+162),str(edY-50.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-I",str(edX+162),str(edY-57.5),"______")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-centered\"\n")
    t.write("      style=\"font-size:5;text-anchor:middle;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Format", str(edX+12), str(edY-21),"A3")+"\n")
    t.write("      "+FCeditext("Sheets", str(edX+148),str(edY-8), "1 / 1")+"\n")
    t.write("      "+FCeditext("Scale",  str(edX+12), str(edY-8), "1 : 1")+"\n")
    t.write("      "+FCeditext("Weight", str(edX+35), str(edY-8), "___ kg")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-Large\"\n")
    t.write("      style=\"font-size:7;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Title",   str(edX+62),str(edY-50),"Drawing Title")+"\n")
    t.write("      "+FCeditext("PtNumber",str(edX+62),str(edY-32),"Part Number")+"\n")
    t.write("    </g>\n\n")
    t.close

# --- Main section ---

CreateSvgFile(templatePath+templateName) # overwrites existing File

# Set sheet format (DIN A3)
formatWidth  = "420"
formatHeight = "297"

#borders = ToteBag()
setDINBorderValues('DIN')

StartSvg(templatePath+templateName)  # adds Start tag and namespaces
CreateSheet(templatePath+templateName, formatWidth, formatHeight)
CreateFrame(templatePath+templateName, formatWidth, formatHeight)
CreateDecoration(templatePath+templateName, formatWidth, formatHeight)
CreateTitleBlock(templatePath+templateName, formatWidth, formatHeight)
CreateEditableText(templatePath+templateName, formatWidth, formatHeight)
EndSvg(templatePath+templateName)
# At this point a new SVG-file is generated and saved
}}


</div>


</div>

The tote bag concept could be used to shorten function calls as the needed parameters could be distributed by global classes\...

And this is the resulting Page:

<img alt="TechDraw page A3" src=images/TechDraw_TemplateHelper_A3.png  style="width:400px;">

## Set up a user interface 

A single format template generator is a bit lame and so a way to choose a format is needed.

As a user interface a pop-up window with a list to choose from would be nice, but let\'s start simple:

### A simple user interface window 

There are some changes in coming versions of Python or Qt and so some principles described in the FreeCAD wiki will not be supported anymore.

If FreeCAD has Python 3.4 or later pre-installed then deprecation warnings are shown in the console window to remind us that some code should be modified to still work in the future.

This is my try to code future-proof.


<div class="mw-collapsible mw-collapsed toccolours">

This opens a window on the screen - no more, no less


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
# imports and constants
from PySide2.QtWidgets import QDialog

class InputWindow(QDialog):
    """
    docstring for InputWindow.
    """
    def __init__(self):
        super(InputWindow, self).__init__()
        self.initUI()

    def initUI(self):
        # now make the window visible
        self.show()


def main():

    form = InputWindow()
    form.exec_()

main()
}}

The action will take place within the initUI function in further steps. And the main part is a function itself to get a bit more object oriented\...


</div>


</div>

### A user interface window with buttons 

Like the one above plus OK and cancel buttons and adjusted window dimensions.


<div class="mw-collapsible mw-collapsed toccolours">

This opens a window on the screen which can be closed with an OK or a cancel button.


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
# imports and constants
from PySide2.QtWidgets import QDialog, QPushButton

class InputWindow(QDialog):
    """
    docstring for InputWindow.
    """
    def __init__(self):
        super(InputWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.result = "Cancelled" # Default return status
        # the window has 640 x 480 pixels and is centered by default
        #- allways larger
        # self.setMinimumWidth(700)
        # self.setMinimumHeight(800)
        #- allways smaller
        self.setMaximumWidth(400)
        self.setMaximumHeight(350)
        print(self.width(), self.height()) # just to check dimensions
        self.setWindowTitle('Input window')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # cancel button
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.clicked.connect(self.onCancel)
        self.cancelButton.setAutoDefault(False) # no AutoDefault with okButton!
        self.cancelButton.move(100, 300)
        # OK button
        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.onOk)
        self.okButton.move(200, 300)

        # now make the window visible
        self.show()

    def onCancel(self):
        self.result = "Cancelled"
        self.close()
    def onOk(self):
        self.result = "OK"
        self.close()


def main():

    form = InputWindow()
    form.exec_()
    print(form.result)

main()
}}

Each button launches a function setting a result value and closing the window.

:   Two print instructions to check if it does what it should\...


</div>


</div>

### A user interface window with combo-box 

Like the one above plus a label and a combo-box to select a sheet format.


<div class="mw-collapsible mw-collapsed toccolours">

This opens a window on the screen which can used to select a sheet format.


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
# imports and constants
from PySide2.QtWidgets import QDialog, QPushButton, QLabel, QComboBox

class InputWindow(QDialog):
    """
    docstring for InputWindow.
    """
    def __init__(self):
        super(InputWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.result = "Cancelled" # Default return status
        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(350)
        self.setWindowTitle('Input window')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # create some labels
        self.labelFormat = QLabel("Set drawing format: ", self)
        self.labelFormat.setFont('osifont') # set to a non-proportional font
        self.labelFormat.move(20, 20)
        # set up lists for pop-ups
        self.FormatList = ("ISO A0","ISO A1","ISO A2","ISO A3","ISO A4",\
"ANSI A","ANSI B","ANSI C","ANSI D","ANSI E",\
"Arch A","Arch B","Arch C","Arch D","Arch E","Arch E1")
        # create some result containers and set default values
        self.ResultFormat = self.FormatList.index("ISO A4") #"ISO A4"
        # create some input elements
        #- set up pop-up menu - ComboBox - Format
        self.popupFormat = QComboBox(self)
        self.popupFormat.move(200, 20)
        self.popupFormat.addItems(self.FormatList)
        self.popupFormat.setCurrentIndex(self.FormatList.index("ISO A4"))
        self.popupFormat.activated[str].connect(self.onPopupFormat)

        #- cancel button
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.clicked.connect(self.onCancel)
        self.cancelButton.setAutoDefault(False) # no AutoDefault with okButton!
        self.cancelButton.move(100, 300)
        #- OK button
        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.onOk)
        self.okButton.move(200, 300)

        # now make the window visible
        self.show()

    def onPopupFormat(self, selectedText):
        self.ResultFormat = selectedText

    def onCancel(self):
        self.result = "Cancelled"
        self.close()
    def onOk(self):
        self.result = "OK"
        self.close()


def main():

    form = InputWindow()
    form.exec_()
    if form.result == "Cancelled":
        pass
    else:
        print(form.result)
        print(form.ResultFormat)

main()
}}

The combo-box is setting another result value without closing the window.

:   Two print instructions to check if it does what it should\...


</div>


</div>

## Manipulate editable texts 

Whenever a new page is generated and inserted, default values are used for the editable texts.

To change the values we use the green handlers and change them one by one. That is acceptable for one page, but quickly becomes annoying if the file contains several pages (sheets) and it would be fine to change entries, that are identical on all pages, in one step.

What do we need beforehand:

:\* a FreeCAD file containing one or more pages that are named/labeled in a compatible way

:\* editable text objects for each page which must be named/labeled identical on all pages

Steps to achieve the goal:

:\# scan the active document for drawing pages

:\# read the values of the first page as default values

:\# use a user interface to check and change the values

:\# distribute the values to all pages

### Look for existing Pages 


<div class="mw-collapsible mw-collapsed toccolours">

Code to search and count pages in the active document


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
def existingPages():
    # this counts existing pages in the active document
    NrOfPages=0
    for Entry in App.ActiveDocument.Objects:
        if Entry.Name[:4] == "Page":
            NrOfPages += 1
    return NrOfPages

def main(NrOfPages):
    # this handles the editable texts
    print("Number of Pages:" + str(NrOfPages))

# decide to run the main part or quit
HowMany = existingPages()

if HowMany > 0 :
    main(HowMany)
else:
    print("Nothing to do - No page found")
}}


</div>


</div>

### Read and write editable texts 

Now that we can be sure that there are pages in the active document it is time to read and write some editable texts.

All entries for part number, title, and subtitle should be identical on all pages within a document. to achieve this the values are read from the first page and distributed to the following page. (In preparation for the next step the values are written to the first page as well)


<div class="mw-collapsible mw-collapsed toccolours">

The above code extended to read entries from the first pages and copy them to the following pages


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
def existingPages():
    # this counts existing pages in the active document
    NrOfPages=0
    for Entry in App.ActiveDocument.Objects:
        if Entry.Name[:4] == "Page":
            NrOfPages += 1
    return NrOfPages

def main(NrOfPages):
    # this handles the editable texts
    print("Number of Pages:" + str(NrOfPages))
    ActiveDoc = App.ActiveDocument
    #- read first page's editable texts (dictionary)
    EdTexts   = ActiveDoc.Page01.Template.EditableTexts

    #- set start PageName
    #- Fill in the editale texts on each page
    while NrOfPages > 0:
        if NrOfPages < 10:
            # insert leading zero
            PageName = ("Page"+ "0"+ str(NrOfPages))
        else:
            PageName = ("Page"+ str(NrOfPages))

        #- read current page's editable texts (dictionary)
        EdiTexts = ActiveDoc.getObject(PageName).Template.EditableTexts
        #- replace current page's values with first page's values
        EdiTexts["PtNumber"] = EdTexts["PtNumber"]
        EdiTexts["Title"]    = EdTexts["Title"]
        EdiTexts["SubTitle"] = EdTexts["SubTitle"]
        #- update current page's editable texts
        ActiveDoc.getObject(PageName).Template.EditableTexts = EdiTexts
        NrOfPages -= 1

# --- Launch area ---
# decide to run the main part or quit
HowMany = existingPages()
if HowMany > 0 :
    main(HowMany)
else:
    print("Nothing to do - No page found")
}}


</div>


</div>

### Add a user interface 

Between reading and writing there should be the opportunity to check and modify the values.

We create a gui window and use the first page\'s entries as default values. The entry fields offer some choices to select from (right mouse button) or the entries can be overwritten.


<div class="mw-collapsible mw-collapsed toccolours">

The above code extended to create a user interface and to handle input data


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
# import statements
from PySide2.QtWidgets import (QDialog, QPushButton, QLabel, QComboBox,
                                QLineEdit, QAction)

# UI Class definition
class TitleBlockEntries(QDialog):
    """
    docstring for InputWindow.
    """
    def __init__(self):
        super(TitleBlockEntries, self).__init__()
        self.initUI()
    def initUI(self):

        InputDocument = App.ActiveDocument
        EdiTexts      = InputDocument.Page01.Template.EditableTexts

        self.result = "Cancelled" # Default return status
        # the window has 640 x 480 pixels and is centered by default
        #- setting window dimensions this way keeps the window centered
        self.setMaximumWidth(400)
        self.setMaximumHeight(350)
        self.setWindowTitle("Title-block entries")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # create some labels
        self.labelPartNr = QLabel("Part number: ", self)
        self.labelPartNr.setFont('osifont') # set to a non-proportional font
        self.labelPartNr.move(20, 20)
        self.labelPartNr = QLabel("Title: ", self)
        self.labelPartNr.setFont('osifont')
        self.labelPartNr.move(20, 60)
        self.labelPartNr = QLabel("Sub-title: ", self)
        self.labelPartNr.setFont('osifont')
        self.labelPartNr.move(20, 80)
        # create some input elements
        #- set up text input field - Part Number
        self.inputPartNr = QLineEdit(self)
        self.inputPartNr.setText(EdiTexts["PtNumber"])
        self.inputPartNr.setFixedWidth(150)
        self.inputPartNr.move(160, 20)
        # set contextual menu options for text editing widget
        #- set text field to some preformatted string
        self.NumberAction1 = QAction(self)
        self.NumberAction1.setText("load new project dummy")
        self.NumberAction1.triggered.connect(self.onPopMenuAction1)
        # remove all text
        self.NumberAction2 = QAction(self)
        self.NumberAction2.setText("clear")
        self.NumberAction2.triggered.connect(self.onPopMenuAction2)
        #- define RMB-menu and add options
        self.inputPartNr.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.inputPartNr.addAction(self.NumberAction1)
        self.inputPartNr.addAction(self.NumberAction2)

        #- set up text input field - Title
        self.inputTitle = QLineEdit(self)
        self.inputTitle.setText(EdiTexts["Title"])
        self.inputTitle.setFixedWidth(190)
        self.inputTitle.move(160, 60)
        # set contextual menu options for text editing widget
        #- set text field to some preformatted string
        self.TitleAction3 = QAction(self)
        self.TitleAction3.setText("load title dummy")
        self.TitleAction3.triggered.connect(self.onPopMenuAction3)
        #- remove all text
        self.TitleAction4 = QAction(self)
        self.TitleAction4.setText("clear")
        self.TitleAction4.triggered.connect(self.onPopMenuAction4)
        # define RMB-menu and add options
        self.inputTitle.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.inputTitle.addAction(self.TitleAction3)
        self.inputTitle.addAction(self.TitleAction4)

        # set up text input field - SubTitle
        self.inputSubTitle = QLineEdit(self)
        self.inputSubTitle.setText(EdiTexts["SubTitle"])
        self.inputSubTitle.setFixedWidth(160)
        self.inputSubTitle.move(160, 80)
        # set contextual menu options for text editing widget
        # nothing but devider
        # menu dividers
        self.SubTitleDivider = QAction(self)
        self.SubTitleDivider.setText('')
        self.SubTitleDivider.triggered.connect(self.onPopMenuDivider)
        # define RMB-menu and add options
        self.inputSubTitle.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.inputSubTitle.addAction(self.SubTitleDivider)

        # cancel button
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.clicked.connect(self.onCancel)
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.move(100, 280)
        # OK button
        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.onOk)
        self.okButton.setAutoDefault(True)
        self.okButton.move(200, 280)
        # now make the window visible
        self.show()

    def onPopMenuAction1(self):
        # load some text into field
        self.inputPartNr.setText("F21-XX-001")
    def onPopMenuDivider(self):
        # this option is the divider and is really there as a spacer on the menu list
        # consequently it has no functional code to execute if user selects it
        pass
    def onPopMenuAction2(self):
        # clear the text from the field
        self.inputPartNr.setText("")
    def onPopMenuAction3(self):
        # load some text into field
        self.inputTitle.setText("Enter name")
    def onPopMenuAction4(self):
        # load some text into field
        self.inputTitle.setText("")

    def onCancel(self):
        self.result = "Cancelled"
        self.close()
    def onOk(self):
        self.result = "OK"
        self.close()

def existingPages():
    # this counts existing pages in the active document
    NrOfPages=0
    for Entry in App.ActiveDocument.Objects:
        if Entry.Name[:4] == "Page":
            NrOfPages += 1
    return NrOfPages

def main(NrOfPages):
    # this handles the editable texts
    print("Number of Pages:" + str(NrOfPages))
    ActiveDoc = App.ActiveDocument

    # Launch input window
    form = TitleBlockEntries()
    form.exec_()
    # deal with the results
    if form.result == "Cancelled":
        pass # steps to handle when selecting Cancel

    if form.result == "OK":
        # steps to handle when selecting OK
        #- Fill in the editable texts on each page
        while NrOfPages > 0:
            if NrOfPages < 10:
                # insert leading zero
                PageName = ("Page"+ "0"+ str(NrOfPages))
            else:
                PageName = ("Page"+ str(NrOfPages))
            #- read current page's editable texts (dictionary)
            EdTexts = ActiveDoc.getObject(PageName).Template.EditableTexts
            #- replace values with gui results
            EdTexts["PtNumber"] = form.inputPartNr.text()
            EdTexts["Title"]    = form.inputTitle.text()
            EdTexts["SubTitle"] = form.inputSubTitle.text()
            # print (EdiTexts) # use for debugging only
            #- update current page's editable texts
            ActiveDoc.getObject(PageName).Template.EditableTexts = EdTexts
            NrOfPages -= 1
        

# --- Launch area ---
# decide to run the main part or quit
HowMany = existingPages()

if HowMany > 0 :
    main(HowMany)
else:
    print("Nothing to do - No page found")
}}


</div>


</div>

More results:

## Combined code 

### Generate A3 template and insert it 

Just copy this code and paste it into an empty \*.py file, edit the template path, save and start the macro from within FreeCAD:


<div class="mw-collapsible mw-collapsed toccolours">

Complete code to create an A3 template and insert it into the active document


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- set the template path to the directory where your templates are stored
templatePath = "/Users/.../FreeCAD/Templates/"
templateName = "MyTemplate.svg"

# - SVG creation -

class ToteBag:
    pass
# This class is empty to act as a container for several variables
#- one bag for drawing borders
borders = ToteBag()

#- set values according to DIN XXX
def setDINBorderValues(format):
    borders.drawingAreaTop    = 10 # distance from page boundary
    borders.drawingAreaBottom = 10
    borders.drawingAreaLeft   = 20
    borders.drawingAreaRight  = 10
    borders.sheetFrameTop     = 5  # distance from drawing area border
    borders.sheetFrameBottom  = 5
    borders.sheetFrameLeft    = 5
    borders.sheetFrameRight   = 5

#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine

#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine

#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine

#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine

#- Create a file and insert a header line
def CreateSvgFile(filePath):
    t=open(filePath,"w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(filePath):
    t=open(filePath,"a") # a = append, new lines are added at the end of an existing file
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(filePath):
    t=open(filePath,"a")
    t.write("</svg>")
    t.close

#- Frame creation
def CreateFrame(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(dAL)
    drawingY=str(dAT)
    #- lower right corner
    drawingWidth=str(int(shWidth)-dAR)
    drawingHeight=str(int(shHeight)-dAB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(shWidth)-dAL-dAR)
    drawingHeight=str(int(shHeight)-dAT-dAB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(dAL-sFL)
    drawingY=str(dAT-sFT)
    #- lower right corner
    drawingWidth=str(int(shWidth)-dAR+sFR)
    drawingHeight=str(int(shHeight)-dAB+sFB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(shWidth)-dAL-dAR+sFL+sFR)
    drawingHeight=str(int(shHeight)-dAT-dAB+sFT+sFB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

#- Indexes and folding marks creation
def CreateDecoration(filePath,shWidth,shHeight):
    t=open(filePath,"a")
    t.write("    <g id=\"index-separators\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.25;\
stroke-linecap:round\">\n")
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight
    drawingX=str(dAL)
    drawingY=str(dAT)
    drawingWidth=str(int(shWidth)-dAL-dAR)
    drawingHeight=str(int(shHeight)-dAT-dAB)

    #- starting point values of center lines
    indexCenter=str(int(drawingWidth)/2+dAL)
    indexMiddle=str(int(drawingHeight)/2+dAT)
    indexLeft=str(dAL+5)
    indexRight=str(int(drawingWidth)+dAL-5)
    indexUpper=str(dAT+5)
    indexLower=str(int(drawingHeight)+dAT-5)

    #- centre and middle markings of drawing area
    if shWidth=="210": # format=="DIN-A4":
        indexLeft=str(dAL)
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-15")+"\n")
    elif shWidth=="420": # format=="DIN-A3":
        indexLeft=str(dAL+5)
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-20")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")
    else :
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-10")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")

    #- starting point values of separator lines
    indexLeft =str(dAL)
    indexRight=str(int(drawingWidth)+dAL)
    indexUpper=str(dAT)
    indexLower=str(int(drawingHeight)+dAT)

    #- set number of horizontal and vertical indexes
    if shWidth=="420": # format=="DIN-A3":
        indexCountX=8
        indexCountY=6
    elif shWidth=="594": # format=="DIN-A2":
        indexCountX=12
        indexCountY=8
    elif shWidth=="841": # format=="DIN-A1":
        indexCountX=16
        indexCountY=12
    elif shWidth=="1189": # format=="DIN-A0":
        indexCountX=24
        indexCountY=16
    else :
        indexCountX=0
        indexCountY=0

    #- indexCenter and indexMiddle contain strings but floating point
    #   numbers are needed to calculate
    floatCenter=int(drawingWidth)/2+dAL
    floatMiddle=int(drawingHeight)/2+dAT

    #- horizontal index separators
    max=int(indexCountX/2-1)
    for value in range(0,max):
        indexX=str(floatCenter+(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")
        indexX=str(floatCenter-(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")

    #- vertical index separators
    max=int(indexCountY/2-1)
    for value in range(0,max):
        indexY=str(floatMiddle+(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")
        indexY=str(floatMiddle-(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")

    t.write("    </g>\n")

    t.write("    <g id=\"indexes\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:middle;fill:#000000;\
    font-family:osifont\">\n")

    #- position point values of indexes
    indexLeft=str(dAL-sFL/2)
    indexRight=str(int(drawingWidth)+dAL+sFR/2)
    indexUpper=str(dAT-1)
    indexLower=str(int(drawingHeight)+dAT+sFB-1)

    #- horizontal indexes, numbers
    max=int(indexCountX/2)
    for value in range(0,max):
        indexX=str(floatCenter+value*50+25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2+value+1)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2+value+1)))+"\n")
        indexX=str(floatCenter-value*50-25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2-value)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2-value)))+"\n")

    #- vertical indexes, letters
    max=int(indexCountY/2)
    for value in range(0,max):
        indexY=str(floatMiddle+value*50+25)
        if int(indexCountY/2+value+1)>9 :  # to avoid the letter J
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
        else :
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
        indexY=str(floatMiddle-value*50-25)
        t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2-value)))+"\n")
        t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2-value)))+"\n")

    t.write("    </g>\n\n")

    #- puncher mark
    t.write("    <g id=\"puncher mark\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if shWidth in["1189", "841", "594"] : # A3 and A4 have extended middle markings
        t.write("        "+svgpath(str(dAL-sFL),str(int(formatHeight)-(297/2)),"h","-10")+"\n")
    t.write("    </g>\n\n")

    #- folding marks
    t.write("    <g id=\"folding marks\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if shWidth=="420": # DIN-A3
        t.write("        "+svgpath("125",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("125",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("230",str(dAT-sFT),"v","-5")+"\n")
        t.write("        "+svgpath("230",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
    elif shWidth=="594": # DIN-A2
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("402",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("402",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","123","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"123","h","  5")+"\n")
    elif shWidth=="841": # DIN-A1
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("651",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("651",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","297","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"297","h","  5")+"\n")
    elif shWidth=="1189": # DIN-A0
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("590",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("590",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("780",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("780",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("999",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("999",str(int(formatHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","247","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"247","h","  5")+"\n")
        t.write("        "+svgpath("  5","544","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(formatWidth)-dAR+sFR),"544","h","  5")+"\n")

    t.write("    </g>\n\n")
    t.close

#- Title block movable
def CreateTitleBlock(filePath,shWidth,shHeight):
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- lower left corner
    tbX=str(int(shWidth)-dAR-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(shHeight)-dAB)
    #- group to move allelements in one step
    t=open(filePath,"a")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    t.write("      \n\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0"," -4","h","155")+"\n")
    t.write("        "+svgpath("  0","-16","h","155")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("  0","-46.5","h"," 50")+"\n")
    t.write("        "+svgpath(" 25"," -4","v","-26")+"\n")
    t.write("        "+svgpath(" 50"," -4","v","-59")+"\n")
    t.write("        "+svgpath("140"," -4","v","-12")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("        "+svgpath("160","  0","v","-63")+"\n")
    t.write("        "+svgpath("155"," -7","h"," 25")+"\n")
    t.write("        "+svgpath("155","-14","h"," 25")+"\n")
    t.write("        "+svgpath("155","-21","h"," 25")+"\n")
    t.write("        "+svgpath("155","-28","h"," 25")+"\n")
    t.write("        "+svgpath("155","-35","h"," 25")+"\n")
    t.write("        "+svgpath("155","-42","h"," 25")+"\n")
    t.write("        "+svgpath("155","-49","h"," 25")+"\n")
    t.write("        "+svgpath("155","-56","h"," 25")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:2.5;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")

    t.write("        "+svgtext("  1.5","-60  ","Author Name:")+"\n")
    t.write("        "+svgtext("  1.5","-52  ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-43.5 ","Supervisor Name:")+"\n")
    t.write("        "+svgtext("  1.5","-35.5 ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-27  ","Format:")+"\n")
    t.write("        "+svgtext("  1.5","-13  ","Scale:")+"\n")
    t.write("        "+svgtext(" 26.5","-13  ","Weight:")+"\n")
    t.write("        "+svgtext(" 51.5","-27  ","Owner:")+"\n")
    t.write("        "+svgtext(" 51.5","-13  ","Version:")+"\n")
    t.write("        "+svgtext("141.5","-13  ","Sheet")+"\n")
    t.write("      </g>\n")
    #- revision indexes, centered
    t.write("      <g id=\"titleblock-revision-indexes\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:middle;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("157.5"," -1.5  ","A")+"\n")
    t.write("        "+svgtext("157.5"," -8.5  ","B")+"\n")
    t.write("        "+svgtext("157.5","-15.5  ","C")+"\n")
    t.write("        "+svgtext("157.5","-22.5  ","D")+"\n")
    t.write("        "+svgtext("157.5","-29.5  ","E")+"\n")
    t.write("        "+svgtext("157.5","-36.5  ","F")+"\n")
    t.write("        "+svgtext("157.5","-43.5  ","G")+"\n")
    t.write("        "+svgtext("157.5","-50.5  ","H")+"\n")
    t.write("        "+svgtext("157.5","-57.5  ","I")+"\n")
    t.write("      </g>\n")

    t.write("    </g>\n\n")
    t.close

#- Title block editable texts
def CreateEditableText(filePath,shWidth,shHeight):
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- offsets for editable texts
    edX=int(shWidth)-dAR-180 # 180 according to DIN EN ISO 7200
    edY=int(shHeight)-dAB

    t=open(filePath,"a")
    t.write("    <g id=\"titleblock-editable-owner\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")

    t.write("      "+FCeditext("Owner",str(edX+60),str(edY-27.0),"Owner")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-address\"\n")
    t.write("      style=\"font-size:2.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Address-1",str(edX+60),str(edY-23.5),"Address1")+"\n")
    t.write("      "+FCeditext("Address-2",str(edX+60),str(edY-20.0),"Address2")+"\n")
    t.write("      "+FCeditext("MailTo",   str(edX+60),str(edY-16.5),"MailTo")+"\n")
    t.write("      "+FCeditext("Copyright",str(edX+2), str(edY-1.0), "Copyright")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-medium\"\n")
    t.write("      style=\"font-size:5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Author",    str(edX+2),  str(edY-55.0),"Author")+"\n")
    t.write("      "+FCeditext("AuDate",    str(edX+7),  str(edY-47.5),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("Supervisor",str(edX+2),  str(edY-38.5),"Supervisor")+"\n")
    t.write("      "+FCeditext("SvDate",    str(edX+7),  str(edY-31.0),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("SubTitle",  str(edX+64), str(edY-42.0),"Sub-title")+"\n")
    t.write("      "+FCeditext("Version",   str(edX+60), str(edY-8.0), "Version")+"\n")
    t.write("      "+FCeditext("Revision-A",str(edX+162),str(edY-1.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-B",str(edX+162),str(edY-8.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-C",str(edX+162),str(edY-15.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-D",str(edX+162),str(edY-22.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-E",str(edX+162),str(edY-29.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-F",str(edX+162),str(edY-36.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-G",str(edX+162),str(edY-43.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-H",str(edX+162),str(edY-50.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-I",str(edX+162),str(edY-57.5),"______")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-centered\"\n")
    t.write("      style=\"font-size:5;text-anchor:middle;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Format", str(edX+12), str(edY-21),"A3")+"\n")
    t.write("      "+FCeditext("Sheets", str(edX+148),str(edY-8), "1 / 1")+"\n")
    t.write("      "+FCeditext("Scale",  str(edX+12), str(edY-8), "1 : 1")+"\n")
    t.write("      "+FCeditext("Weight", str(edX+35), str(edY-8), "___ kg")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-Large\"\n")
    t.write("      style=\"font-size:7;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Title",   str(edX+62),str(edY-50),"Drawing Title")+"\n")
    t.write("      "+FCeditext("PtNumber",str(edX+62),str(edY-32),"Part Number")+"\n")
    t.write("    </g>\n\n")
    t.close

# --- Main section ---

CreateSvgFile(templatePath+templateName) # overwrites existing File

# Set sheet format (DIN A3)
formatWidth  = "420"
formatHeight = "297"

#borders = ToteBag()
setDINBorderValues('DIN')

StartSvg(templatePath+templateName)  # adds Start tag and namespaces
CreateSheet(templatePath+templateName, formatWidth, formatHeight)
CreateFrame(templatePath+templateName, formatWidth, formatHeight)
CreateDecoration(templatePath+templateName, formatWidth, formatHeight)
CreateTitleBlock(templatePath+templateName, formatWidth, formatHeight)
CreateEditableText(templatePath+templateName, formatWidth, formatHeight)
EndSvg(templatePath+templateName)
# At this point a new SVG-file is generated and saved
# and shall be attached to the active document

# -- Add a page and a template to the active document --

activeDoc = App.activeDocument()

# add a page to the active document
newPage = 'Page01' # first page name to start search

# to find the current page number to create
pageCount = 1
pageFound = True
while pageFound:
    try:
        print(activeDoc.getObject(newPage).Label)
    except AttributeError:
        print(newPage + " to be created")
        pageFound = False
    else:
        pageCount = pageCount + 1
        if pageCount < 10:
            newPage = newPage[0:4] + '0' + str(pageCount)
        else:
            newPage = newPage[0:4] + str(pageCount)

# set template number according to page number
newTemplate = ('Template' + newPage[4:])

# add a page object to the active document
activeDoc.addObject('TechDraw::DrawPage',newPage)

# add a template object to the active document
activeDoc.addObject('TechDraw::DrawSVGTemplate',newTemplate)

# load the svg template into the template object
activeDoc.getObject(newTemplate).Template = templatePath+templateName

# add the template object to the page's object list
activeDoc.getObject(newPage).Template = activeDoc.getObject(newTemplate)

# rename 'Page' to 'Sheet'
activeDoc.getObject(newPage).Label = 'Sheet ' + newPage[4:]

# open the page object for editing
activeDoc.getObject(newPage).ViewObject.doubleClicked()

}}


</div>


</div>

### Select format and generate a template then insert it 

This combines the tasks to set up an input window to select the sheet format, to generate a template with the chosen dimensions, and to insert it into our active document.


<div class="mw-collapsible mw-collapsed toccolours">

Complete code to select the sheet format, generate a template with the chosen dimensions, and insert it into the active document (In this macro the sheet dimensions are no longer handed over to the functions as parameter but will be read from a global variable)


<div class="mw-collapsible-content">


{{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
# imports and constants
from PySide2.QtWidgets import QDialog, QPushButton, QLabel, QComboBox
#- set the template path to the directory where your templates are stored
templatePath = "/Users/.../FreeCAD/Templates/"
templateName = "MyTemplate.svg"

# - SVG creation -

class ToteBag:
    pass
# This class is empty to act as a container for several variables

borders = ToteBag() #- one bag for drawing border offsets#- one bag for page dimensions
sheetFormat = ToteBag() #- one bag for page dimensions

class InputWindow(QDialog):
    """
    docstring for InputWindow.
    """
    def __init__(self):
        super(InputWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.result = "Cancelled" # Default return status
        # the window has 640 x 480 pixels and is centered by default
        #- set window dimensions
        self.setMaximumWidth(400)
        self.setMaximumHeight(350)
        self.setWindowTitle('Input window')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # create some labels
        self.labelFormat = QLabel("Set drawing format: ", self)
        self.labelFormat.setFont('osifont') # set to a non-proportional font
        self.labelFormat.move(20, 20)
        # set up lists for pop-ups
        self.FormatList = ("ISO A0","ISO A1","ISO A2","ISO A3","ISO A4",\
"ANSI A","ANSI B","ANSI C","ANSI D","ANSI E",\
"Arch A","Arch B","Arch C","Arch D","Arch E","Arch E1")
        # create some result containers and set default values
        self.ResultFormat = "ISO A4"
        # create some input elements
        #- set up pop-up menu - ComboBox - Format
        self.popupFormat = QComboBox(self)
        self.popupFormat.move(200, 20)
        self.popupFormat.addItems(self.FormatList)
        self.popupFormat.setCurrentIndex(self.FormatList.index("ISO A4"))
        self.popupFormat.activated[str].connect(self.onPopupFormat)

        #- cancel button
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.clicked.connect(self.onCancel)
        self.cancelButton.setAutoDefault(False) # no AutoDefault with okButton!
        self.cancelButton.move(100, 300)
        #- OK button
        self.okButton = QPushButton('OK', self)
        self.okButton.clicked.connect(self.onOk)
        self.okButton.move(200, 300)

        # now make the window visible
        self.show()

    def onPopupFormat(self, selectedText):
        self.ResultFormat = selectedText

    def onCancel(self):
        self.result = "Cancelled"
        self.close()
    def onOk(self):
        self.result = "OK"
        self.close()

#- set values according to ISO, ANSI, Arch
def setBorderValues(format):
    # customise values if needed
    print(format)
    if format[0:3] == "ANS":
        borders.drawingAreaTop    = 10 # distance from page boundary
        borders.drawingAreaBottom = 10
        borders.drawingAreaLeft   = 20
        borders.drawingAreaRight  = 10
        borders.sheetFrameTop     = 5  # distance from drawing area border
        borders.sheetFrameBottom  = 5
        borders.sheetFrameLeft    = 5
        borders.sheetFrameRight   = 5
    elif format[0:3] == "Arc":
        borders.drawingAreaTop    = 10 # distance from page boundary
        borders.drawingAreaBottom = 10
        borders.drawingAreaLeft   = 20
        borders.drawingAreaRight  = 10
        borders.sheetFrameTop     = 5  # distance from drawing area border
        borders.sheetFrameBottom  = 5
        borders.sheetFrameLeft    = 5
        borders.sheetFrameRight   = 5
    else:
        borders.drawingAreaTop    = 10 # distance from page boundary
        borders.drawingAreaBottom = 10
        borders.drawingAreaLeft   = 20
        borders.drawingAreaRight  = 10
        borders.sheetFrameTop     = 5  # distance from drawing area border
        borders.sheetFrameBottom  = 5
        borders.sheetFrameLeft    = 5
        borders.sheetFrameRight   = 5

def SetSheetDimensions(format):
    if format[0:3] == "ANS":
        if format[-1:0] == "A":
            sheetFormat.width  = "216"
            sheetFormat.height = "279"
        elif format[-1:0] == "B":
            sheetFormat.width  = "432"
            sheetFormat.height = "279"
        elif format[-1:0] == "C":
            sheetFormat.width  = "559"
            sheetFormat.height = "432"
        elif format[-1:0] == "D":
            sheetFormat.width  = "864"
            sheetFormat.height = "559"
        else: # E
            sheetFormat.width  = "1118"
            sheetFormat.height = "864"
    elif format[0:3] == "Arc":
        if format[-1:0] == "A":
            sheetFormat.width  = "229"
            sheetFormat.height = "305"
        elif format[-1:0] == "B":
            sheetFormat.width  = "457"
            sheetFormat.height = "305"
        elif format[-1:0] == "C":
            sheetFormat.width  = "610"
            sheetFormat.height = "457"
        elif format[-1:0] == "D":
            sheetFormat.width  = "914"
            sheetFormat.height = "610"
        elif format[-1:0] == "E":
            sheetFormat.width  = "1219"
            sheetFormat.height = "914"
        else: # E1
            sheetFormat.width  = "1067"
            sheetFormat.height = "762"
    else: # ISO
        if format[-1:] == "4":
            sheetFormat.width  = "210"
            sheetFormat.height = "297"
        elif format[-1:] == "3":
            sheetFormat.width  = "420"
            sheetFormat.height = "297"
        elif format[-1:] == "2":
            sheetFormat.width  = "594"
            sheetFormat.height = "420"
        elif format[-1:] == "1":
            sheetFormat.width  = "841"
            sheetFormat.height = "594"
        else: # A0
            sheetFormat.width  = "1189"
            sheetFormat.height = "841"
    print(format, sheetFormat.width, sheetFormat.height)

#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine

#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine

#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine

#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine

#- Create a file and insert a header line
def CreateSvgFile(filePath):
    t=open(filePath,"w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(filePath):
    t=open(filePath,"a") # a = append, new lines are added at the end of an existing file
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(filePath):
    #- set sheet dimensions
    sWidth  = sheetFormat.width
    sHeight = sheetFormat.height
    t=open(filePath,"a")
    t.write("  width =\""+sWidth+"mm\"\n")
    t.write("  height=\""+sHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+sWidth+" "+sHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(filePath):
    t=open(filePath,"a")
    t.write("</svg>")
    t.close

#- Frame creation
def CreateFrame(filePath):
    t=open(filePath,"a")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    #- set sheet dimensions
    sWidth  = sheetFormat.width
    sHeight = sheetFormat.height
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(dAL)
    drawingY=str(dAT)
    #- lower right corner
    drawingWidth=str(int(sWidth)-dAR)
    drawingHeight=str(int(sHeight)-dAB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(sWidth)-dAL-dAR)
    drawingHeight=str(int(sHeight)-dAT-dAB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(dAL-sFL)
    drawingY=str(dAT-sFT)
    #- lower right corner
    drawingWidth=str(int(sWidth)-dAR+sFR)
    drawingHeight=str(int(sHeight)-dAB+sFB)
    t.write("      \n")
    #- frame dimensions
    drawingWidth=str(int(sWidth)-dAL-dAR+sFL+sFR)
    drawingHeight=str(int(sHeight)-dAT-dAB+sFT+sFB)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

#- Indexes and folding marks creation
def CreateDecoration(filePath):
    t = open(filePath,"a")
    t.write("    <g id=\"index-separators\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.25;\
stroke-linecap:round\">\n")
    #- set sheet dimensions
    sWidth  = sheetFormat.width
    sHeight = sheetFormat.height
    #- set frame offsets
    dAT = borders.drawingAreaTop
    dAB = borders.drawingAreaBottom
    dAL = borders.drawingAreaLeft
    dAR = borders.drawingAreaRight
    sFT = borders.sheetFrameTop
    sFB = borders.sheetFrameBottom
    sFL = borders.sheetFrameLeft
    sFR = borders.sheetFrameRight

    drawingX=str(dAL)
    drawingY=str(dAT)
    drawingWidth=str(int(sWidth)-dAL-dAR)
    drawingHeight=str(int(sHeight)-dAT-dAB)

    #- starting point values of center lines
    indexCenter=str(int(drawingWidth)/2+dAL)
    indexMiddle=str(int(drawingHeight)/2+dAT)
    indexLeft=str(dAL+5)
    indexRight=str(int(drawingWidth)+dAL-5)
    indexUpper=str(dAT+5)
    indexLower=str(int(drawingHeight)+dAT-5)

    #- centre and middle markings of drawing area
    if sWidth=="210": # format=="DIN-A4":
        indexLeft=str(dAL)
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-15")+"\n")
    elif sWidth=="420": # format=="DIN-A3":
        indexLeft=str(dAL+5)
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-20")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")
    else :
        t.write("        "+svgpath(indexCenter,indexUpper,"v","-10")+"\n")
        t.write("        "+svgpath(indexCenter,indexLower,"v"," 10")+"\n")
        t.write("        "+svgpath(indexLeft,indexMiddle,"h","-10")+"\n")
        t.write("        "+svgpath(indexRight,indexMiddle,"h"," 10")+"\n")

    #- starting point values of separator lines
    indexLeft =str(dAL)
    indexRight=str(int(drawingWidth)+dAL)
    indexUpper=str(dAT)
    indexLower=str(int(drawingHeight)+dAT)

    #- set number of horizontal and vertical indexes
    # this needs to be extended for American formats
    if sWidth=="420": # format=="DIN-A3":
        indexCountX=8
        indexCountY=6
    elif sWidth=="594": # format=="DIN-A2":
        indexCountX=12
        indexCountY=8
    elif sWidth=="841": # format=="DIN-A1":
        indexCountX=16
        indexCountY=12
    elif sWidth=="1189": # format=="DIN-A0":
        indexCountX=24
        indexCountY=16
    else :
        indexCountX=0
        indexCountY=0

    #- indexCenter and indexMiddle contain strings but floating point
    #   numbers are needed to calculate
    floatCenter=int(drawingWidth)/2+dAL
    floatMiddle=int(drawingHeight)/2+dAT

    #- horizontal index separators
    max=int(indexCountX/2-1)
    for value in range(0,max):
        indexX=str(floatCenter+(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")
        indexX=str(floatCenter-(value+1)*50)
        t.write("        "+svgpath(indexX,indexUpper,"v"," -5")+"\n")
        t.write("        "+svgpath(indexX,indexLower,"v","  5")+"\n")

    #- vertical index separators
    max=int(indexCountY/2-1)
    for value in range(0,max):
        indexY=str(floatMiddle+(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")
        indexY=str(floatMiddle-(value+1)*50)
        t.write("        "+svgpath(indexLeft, indexY,"h"," -5")+"\n")
        t.write("        "+svgpath(indexRight,indexY,"h","  5")+"\n")

    t.write("    </g>\n")

    t.write("    <g id=\"indexes\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:middle;fill:#000000;\
    font-family:osifont\">\n")

    #- position point values of indexes
    indexLeft=str(dAL-sFL/2)
    indexRight=str(int(drawingWidth)+dAL+sFR/2)
    indexUpper=str(dAT-1)
    indexLower=str(int(drawingHeight)+dAT+sFB-1)

    #- horizontal indexes, numbers
    max=int(indexCountX/2)
    for value in range(0,max):
        indexX=str(floatCenter+value*50+25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2+value+1)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2+value+1)))+"\n")
        indexX=str(floatCenter-value*50-25)
        t.write("        "+svgtext(indexX,indexUpper,str(int(indexCountX/2-value)))+"\n")
        t.write("        "+svgtext(indexX,indexLower,str(int(indexCountX/2-value)))+"\n")

    #- vertical indexes, letters
    max=int(indexCountY/2)
    for value in range(0,max):
        indexY=str(floatMiddle+value*50+25)
        if int(indexCountY/2+value+1)>9 :  # to avoid the letter J
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+2)))+"\n")
        else :
            t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
            t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2+value+1)))+"\n")
        indexY=str(floatMiddle-value*50-25)
        t.write("        "+svgtext(indexLeft,indexY,chr(64+int(indexCountY/2-value)))+"\n")
        t.write("        "+svgtext(indexRight,indexY,chr(64+int(indexCountY/2-value)))+"\n")

    t.write("    </g>\n\n")

    #- puncher mark
    t.write("    <g id=\"puncher mark\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if sWidth in["1189", "841", "594"] : # A3 and A4 have extended middle markings
        t.write("        "+svgpath(str(dAL-sFL),str(int(sHeight)-(297/2)),"h","-10")+"\n")
    t.write("    </g>\n\n")

    #- folding marks
    t.write("    <g id=\"folding marks\"\n")
    t.write("      style=\"fill:none;stroke:#b0b0b0;stroke-width:0.25;\
    stroke-linecap:miter;stroke-miterlimit:4\">\n")
    if sWidth=="420": # DIN-A3
        t.write("        "+svgpath("125",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("125",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("230",str(dAT-sFT),"v","-5")+"\n")
        t.write("        "+svgpath("230",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
    elif sWidth=="594": # DIN-A2
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("402",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("402",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","123","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"123","h","  5")+"\n")
    elif sWidth=="841": # DIN-A1
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("651",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("651",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","297","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"297","h","  5")+"\n")
    elif sWidth=="1189": # DIN-A0
        t.write("        "+svgpath("210",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("210",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("400",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("400",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("590",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("590",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("780",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("780",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("999",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("999",str(int(sHeight)-dAB+sFB),"v","  5")+"\n")
        t.write("        "+svgpath("105",str(dAT-sFT),"v"," -5")+"\n")
        t.write("        "+svgpath("  5","247","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"247","h","  5")+"\n")
        t.write("        "+svgpath("  5","544","h"," -5")+"\n")
        t.write("        "+svgpath(str(int(sWidth)-dAR+sFR),"544","h","  5")+"\n")

    t.write("    </g>\n\n")
    t.close

#- Title block movable
def CreateTitleBlock(filePath):
    #- set sheet dimensions
    sWidth  = sheetFormat.width
    sHeight = sheetFormat.height
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- lower left corner
    tbX=str(int(sWidth)-dAR-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(sHeight)-dAB)
    #- group to move allelements in one step
    t=open(filePath,"a")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    t.write("      \n\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0"," -4","h","155")+"\n")
    t.write("        "+svgpath("  0","-16","h","155")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("  0","-46.5","h"," 50")+"\n")
    t.write("        "+svgpath(" 25"," -4","v","-26")+"\n")
    t.write("        "+svgpath(" 50"," -4","v","-59")+"\n")
    t.write("        "+svgpath("140"," -4","v","-12")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("        "+svgpath("160","  0","v","-63")+"\n")
    t.write("        "+svgpath("155"," -7","h"," 25")+"\n")
    t.write("        "+svgpath("155","-14","h"," 25")+"\n")
    t.write("        "+svgpath("155","-21","h"," 25")+"\n")
    t.write("        "+svgpath("155","-28","h"," 25")+"\n")
    t.write("        "+svgpath("155","-35","h"," 25")+"\n")
    t.write("        "+svgpath("155","-42","h"," 25")+"\n")
    t.write("        "+svgpath("155","-49","h"," 25")+"\n")
    t.write("        "+svgpath("155","-56","h"," 25")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:2.5;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("  1.5","-60  ","Author Name:")+"\n")
    t.write("        "+svgtext("  1.5","-52  ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-43.5 ","Supervisor Name:")+"\n")
    t.write("        "+svgtext("  1.5","-35.5 ","Date:")+"\n")
    t.write("        "+svgtext("  1.5","-27  ","Format:")+"\n")
    t.write("        "+svgtext("  1.5","-13  ","Scale:")+"\n")
    t.write("        "+svgtext(" 26.5","-13  ","Weight:")+"\n")
    t.write("        "+svgtext(" 51.5","-27  ","Owner:")+"\n")
    t.write("        "+svgtext(" 51.5","-13  ","Version:")+"\n")
    t.write("        "+svgtext("141.5","-13  ","Sheet")+"\n")
    t.write("      </g>\n")
    #- revision indexes, centered
    t.write("      <g id=\"titleblock-revision-indexes\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:middle;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("157.5"," -1.5  ","A")+"\n")
    t.write("        "+svgtext("157.5"," -8.5  ","B")+"\n")
    t.write("        "+svgtext("157.5","-15.5  ","C")+"\n")
    t.write("        "+svgtext("157.5","-22.5  ","D")+"\n")
    t.write("        "+svgtext("157.5","-29.5  ","E")+"\n")
    t.write("        "+svgtext("157.5","-36.5  ","F")+"\n")
    t.write("        "+svgtext("157.5","-43.5  ","G")+"\n")
    t.write("        "+svgtext("157.5","-50.5  ","H")+"\n")
    t.write("        "+svgtext("157.5","-57.5  ","I")+"\n")
    t.write("      </g>\n")

    t.write("    </g>\n\n")
    t.close

#- Title block editable texts
def CreateEditableText(filePath):
    #- set sheet dimensions
    sWidth  = sheetFormat.width
    sHeight = sheetFormat.height
    #- set frame offsets
    dAB = borders.drawingAreaBottom
    dAR = borders.drawingAreaRight

    #- offsets for editable texts
    edX=int(sWidth)-dAR-180 # 180 according to DIN EN ISO 7200
    edY=int(sHeight)-dAB

    t=open(filePath,"a")
    t.write("    <g id=\"titleblock-editable-owner\"\n")
    t.write("      style=\"font-size:3.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")

    t.write("      "+FCeditext("Owner",str(edX+60),str(edY-27.0),"Owner")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-address\"\n")
    t.write("      style=\"font-size:2.5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Address-1",str(edX+60),str(edY-23.5),"Address1")+"\n")
    t.write("      "+FCeditext("Address-2",str(edX+60),str(edY-20.0),"Address2")+"\n")
    t.write("      "+FCeditext("MailTo",   str(edX+60),str(edY-16.5),"MailTo")+"\n")
    t.write("      "+FCeditext("Copyright",str(edX+2), str(edY-1.0), "Copyright")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-medium\"\n")
    t.write("      style=\"font-size:5;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Author",    str(edX+2),  str(edY-55.0),"Author")+"\n")
    t.write("      "+FCeditext("AuDate",    str(edX+7),  str(edY-47.5),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("Supervisor",str(edX+2),  str(edY-38.5),"Supervisor")+"\n")
    t.write("      "+FCeditext("SvDate",    str(edX+7),  str(edY-31.0),"YYYY/MM/DD")+"\n")
    t.write("      "+FCeditext("SubTitle",  str(edX+64), str(edY-42.0),"Sub-title")+"\n")
    t.write("      "+FCeditext("Version",   str(edX+60), str(edY-8.0), "Version")+"\n")
    t.write("      "+FCeditext("Revision-A",str(edX+162),str(edY-1.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-B",str(edX+162),str(edY-8.5), "______")+"\n")
    t.write("      "+FCeditext("Revision-C",str(edX+162),str(edY-15.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-D",str(edX+162),str(edY-22.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-E",str(edX+162),str(edY-29.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-F",str(edX+162),str(edY-36.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-G",str(edX+162),str(edY-43.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-H",str(edX+162),str(edY-50.5),"______")+"\n")
    t.write("      "+FCeditext("Revision-I",str(edX+162),str(edY-57.5),"______")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-centered\"\n")
    t.write("      style=\"font-size:5;text-anchor:middle;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Format", str(edX+12), str(edY-21),"A3")+"\n")
    t.write("      "+FCeditext("Sheets", str(edX+148),str(edY-8), "1 / 1")+"\n")
    t.write("      "+FCeditext("Scale",  str(edX+12), str(edY-8), "1 : 1")+"\n")
    t.write("      "+FCeditext("Weight", str(edX+35), str(edY-8), "___ kg")+"\n")
    t.write("    </g>\n")

    t.write("    <g id=\"titleblock-editable-Large\"\n")
    t.write("      style=\"font-size:7;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("Title",   str(edX+62),str(edY-50),"Drawing Title")+"\n")
    t.write("      "+FCeditext("PtNumber",str(edX+62),str(edY-32),"Part Number")+"\n")
    t.write("    </g>\n\n")
    t.close

def main():
    templateFile = templatePath+templateName

    # Gui to select some presets
    form = InputWindow()
    form.exec_()
    if form.result == "Cancelled":
        pass
    else:
        print(form.result)
        print(form.ResultFormat)
        setBorderValues(form.ResultFormat)
        SetSheetDimensions(form.ResultFormat)

        CreateSvgFile(templateFile) # overwrites existing File
        StartSvg(templateFile)  # adds Start tag and namespaces
        CreateSheet(templateFile)
        CreateFrame(templateFile)
        CreateDecoration(templateFile)
        CreateTitleBlock(templateFile)
        CreateEditableText(templateFile)
        EndSvg(templateFile)
        # At this point a new SVG-file is generated and saved
        # and shall be attached to the active document

        # -- Add a page and a template to the active document --

        activeDoc = App.activeDocument()
        # add a page to the active document
        newPage = "Page01" # first page name to start search
        # to find the current page number to create
        pageCount = 1
        pageFound = True
        while pageFound:
            try:
                print(activeDoc.getObject(newPage).Label)
            except AttributeError:
                print(newPage + " to be created")
                pageFound = False
            else:
                pageCount = pageCount + 1
                if pageCount < 10:
                    newPage = newPage[0:4] + '0' + str(pageCount)
                else:
                    newPage = newPage[0:4] + str(pageCount)

        # set template number according to page number
        newTemplate = ('Template' + newPage[4:])
        # add a page object to the active document
        activeDoc.addObject('TechDraw::DrawPage',newPage)
        # add a template object to the active document
        activeDoc.addObject('TechDraw::DrawSVGTemplate',newTemplate)
        # load the svg template into the template object
        activeDoc.getObject(newTemplate).Template = templatePath+templateName
        # add the template object to the page's object list
        activeDoc.getObject(newPage).Template = activeDoc.getObject(newTemplate)
        # rename 'Page' to 'Sheet'
        activeDoc.getObject(newPage).Label = 'Sheet ' + newPage[4:]
        # open the page object for editing
        activeDoc.getObject(newPage).ViewObject.doubleClicked()

main()
}}


</div>


</div>




This is a sandbox / Dies ist eine Sandbox



---
![](images/Right_arrow.png) [documentation index](../README.md) > Sandbox:TechDraw TemplateHelper
