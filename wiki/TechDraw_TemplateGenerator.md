---
 TutorialInfo:
   Topic: Template generation with Python macro
   Level: Basic skills of Python and svg-structures are helpful
   FCVersion: 0.19.1 and later
   Time: 
   Author: User:FBXL5
   SeeAlso: Macro_TemplateHelper
---

# TechDraw TemplateGenerator

 



## Introduction

This tutorial describes how to generate a simple template to use with the TechDraw workbench out of some lines of Python code.

Any text editor can be used to code. My choice is Atom, but FreeCAD\'s built-in editor works well, too.

The following code examples can be copied and pasted into an empty text file and then saved under a name of your choice as a \*.py or \*.FCMacro file.

A template provides a background for the drawing tasks and its dimensions are used by the printer drivers to scale the drawing correctly.

The templates are svg-files and so a macro has to compose some lines of svg code (which is a subset of xml code).

## Structure of a simple blank page 

The SVG format is a subset of the XML format. That is why an SVG file, like any XML file, consists of two parts:

-   Head, a format declaration
-   Body, containing the information what to show and where to place it

:   (I don\'t know why there should be a headline, the svg-file is still a valid template file without it\...)

### Head

The head is just one line to declare which version of the XML language an interpreter should use to handle the instructions in the body.

 {{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
}}

### Body

The Body starts with an opening tag which contains information about name spaces and about the size of the template and where to place it. And it finishes with a closing tag.

 {{Code|lang=xml|code=
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}

:   **xmlns=**\"<http://www.w3.org/2000/svg>\": External link to the xml name space to look up standard xml commands
:   **version=**\"1.1\": Used xml version is 1.1
:   **xmlns:freecad=**\"[Svg Namespace](https://wiki.freecad.org/index.php?title=Svg_Namespace)\": External link to FreeCAD\'s name space extension to look up special commands that are only used inside a FreeCAD environment e.g. for editable texts.
:   \"freecad:\" will be prefixed to attribute names to have them handled by said special commands.
:   **width=**\"420mm\": Width of the drawing area
:   **height=**\"297mm\": Height of the drawing area
:   **viewBox=**\"0 0 420 297\": Position of the upper left corner (0;0) and the lower right corner (420;297) in the svg construction space (in svg units).
:   Width, height, and viewBox in this combination set 1 svg-unit to 1 mm for the whole document. A dimensional unit can be omitted from now on.
:   In this case 420 and 297 give an A3 page. Customise these values to generate other page sizes.

For a blank page size DIN A3 in landscape orientation that\'s all.

 {{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}

## Python code\... 

Before any code is generated a folder is needed to store the new template file.

The user should have selected a template folder. Its path is then stored in the TechDraw preferences.  It is not necessary to know where the preferences are store, because FreeCAD has commands to address needed parameters directly.


{{Code| |code=
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
template_file = os.path.join(template_path, template_name)
}}

**parameter_path** receives the path to the \"folder\" within the configuration file where \"TemplateDir\" parameter can be found.  **template_path** receives the content of \"TemplateDir\" which is the path to the template directory.  **template_name** recieves the name of the template to be created.

Now the template name needs to be linked to the template path in a way that is compatible to unix based OSs and Windows. This is done with the \"os.path.join\" command and stored into the **template_file**.

### \... to create a blank page 


<div class="mw-collapsible mw-collapsed toccolours">

This macro shows the principle how an svg-file can be put together. (Format is A3)


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- Get the path to the template folder that is set in the FreeCAD parameters
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
#- Link template_path and template_name for any OS
template_file = os.path.join(template_path, template_name)

# - SVG creation -

#- Create a file and insert a header line
#   (with t as the space saving variant of template)
def CreateSvgFile(file_path):
    t=open(file_path, "w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

# --- Main section ---

CreateSvgFile(template_file) # overwrites existing File

# Set sheet format (DIN A3)
formatWidth  = "420"
formatHeight = "297"

StartSvg(template_file)  # adds Start tag and namespaces
CreateSheet(template_file, formatWidth, formatHeight)
EndSvg(template_file)
# At this point a new SVG-file is generated and saved
}}


</div>


</div>


:   The main principle is:
    -   to open a file for writing and so start an svg-file from scratch, write the header line and close the file as a first step.
    -   and then to repeatedly open the file to append further segments and then close it again after appending.
:   
:   The macro is made of several functions which are called from the main section.
:   Additional functions could be inserted before the EndSvg function and the needed calls are put before the EndSvg() call.
:   We need to have an eye on the number of spaces used with the write operations for a correct indentation.

### \... to create a page with some ink 

To make a drawing out of a blank page we need:

  - Frames i.e. rectangles created with the **rect** instruction

  - a title block and more made of lines created with the **path** instruction

  - simple texts for indexes and labeling title block cells

  - editable texts like part number or part name

Normally these graphical elements are used repeatedly and so the generating code is put into functions.

### svgrect function 

To draw a rectangle we just need to call the **svgrect** function and hand over the values for width, height, and position of the upper left corner. That is better readable than the content of the svgline which had to be used instead.

 {{Code| |code=
#- Function to generate an svg-instruction to draw a rectangle with the given values
def svgrect(width,height,x,y):
    svgLine=("<rect width=\""+width+"\" height=\""+height+"\" x=\""+x+"\" y=\""+y+"\" />")
    return svgLine
}}

### svgpath function 

To draw a line we just need to call the **svgpath** function and hand over the coordinates of the start point and the endpoint of a line.

Instead of the end point coordinates we can hand over a tag to draw a horizontal (h) or vertical (v) line followed by the length of the line or the tag to draw a horizontal (H) or vertical (V) line followed by the x or y ordinate of the end point.

Each path starts at the origin and the first action is a movement with \"raised pen\" (not drawing) to the start point. In this case the relative movement and the absolute movement are the same and so it is irrelevant whether the m-tag is upper or lower case.

 {{Code| |code=
#- Function to generate an svg-instruction to draw a path element (line) with the given values
def svgpath(x1,y1,x2,y2):
    if x2=="v" or x2=="V" or x2=="h" or x2=="H":
        svgLine=("<path d=\"m "+x1+","+y1+" "+x2+" "+y2+"\" />")
    else:
        svgLine=("<path d=\"m "+x1+","+y1+" l "+x2+","+y2+"\" />")
    return svgLine
}}

### svgtext function 

To draw a piece of text we just need to call the **svgtext** function and hand over the coordinates of the text\'s anchor point and the text string itself.

(The text alignment is controlled by the surrounding group tag or left-aligned as default).

 {{Code| |code=
#- Function to generate an svg-instruction to place a text element with the given values
def svgtext(posX,posY,strValue):
    svgLine=("<text x=\""+posX+"\" y=\""+posY+"\">"+strValue+"</text>")
    return svgLine
}}

### FCeditext function 

To draw a piece of editable text we just need to call the **FCeditext** function and hand over a name, the coordinates of the text\'s anchor point, and the text string itself.

FreeCAD creates a dictionary object with every inserted template, and each entry has a name (key) and a value.

(The text alignment is controlled by the surrounding group tag or left-aligned as default).

 {{Code| |code=
#- Function to generate an svg-instruction to place an editable text element with the given values
def FCeditext(entryName,posX,posY,strValue):
    svgLine=("<text freecad:editable=\""+entryName+"\" x=\""+posX+"\" y=\""+posY \
    +"\">  <tspan>"+strValue+"</tspan>  </text>")
    return svgLine
}}

### CreateXxxx functions 

These functions start with code to open a file in append mode and to write the group opening tag.

Then follows a section to set and calculate values and with write instructions that call the above functions to generate svg-code.

And finally the group closing tag followed by an instruction to close the file.

 {{Code| |code=
#- Frame creation
def CreateFrame(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(20)
    drawingY=str(10)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20-10)
    drawingHeight=str(int(shHeight)-10-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(15)
    drawingY=str(5)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20)
    drawingHeight=str(int(shHeight)-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close
}}

### Resulting macro 


<div class="mw-collapsible mw-collapsed toccolours">

This macro adds some basic graphical elements needed for proper templates i.e. line elements, texts, and editable texts.


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2021 Your name LGPL
#
#
#- Get the path to the template folder that is set in the FreeCAD parameters
parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
template_path = parameter_path.GetString("TemplateDir")
template_name = "MyTemplate.svg"
#- Link template_path and template_name for any OS
template_file = os.path.join(template_path, template_name)

# - SVG creation -

#- Create a file and insert a header line
#   (with t as the space saving variant of template)
def CreateSvgFile(file_path):
    t=open(file_path, "w") # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

#- Create opening svg-tag
#   Namespace section
def StartSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n"+"\n")
    t.write("<svg\n")
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    t.close
#   Sheet size section
def CreateSheet(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("  width =\""+shWidth+"mm\"\n")
    t.write("  height=\""+shHeight+"mm\"\n")
    t.write("  viewBox=\"0 0 "+shWidth+" "+shHeight+"\">\n")
    t.close
    # identical values for width and height and Viewbox' width and height will synchronise mm and svg-units

#- Create closing svg-tag
def EndSvg(file_path):
    t=open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

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

#- Frame creation
def CreateFrame(file_path, shWidth, shHeight):
    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;\
stroke-linecap:round\">\n")
    # inner Frame, drawing area
    #- upper left corner
    drawingX=str(20)
    drawingY=str(10)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20-10)
    drawingHeight=str(int(shHeight)-10-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    # outer frame
    #- upper left corner
    drawingX=str(15)
    drawingY=str(5)
    #- frame dimensions
    drawingWidth=str(int(shWidth)-20)
    drawingHeight=str(int(shHeight)-10)
    #- frame rectangle
    t.write("      "+svgrect(drawingWidth,drawingHeight,drawingX,drawingY)+"\n")
    t.write("    </g>\n\n")
    t.close

#- Title block movable
def CreateTitleBlock(file_path, shWidth, shHeight):

    #- lower left corner
    tbX=str(int(shWidth)-10-180) # 180 according to DIN EN ISO 7200
    tbY=str(int(shHeight)-10)
    #- group to transform all elements at once
    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate("+tbX+","+tbY+")\">\n")
    #- title block
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        "+svgpath("  0","  0","  0","-63")+"\n")
    t.write("        "+svgpath("  0","-63","180","  0")+"\n")
    t.write("        "+svgpath("  0","-30","h","155")+"\n")
    t.write("        "+svgpath("155","  0","v","-63")+"\n")
    t.write("      </g>\n")
    #- small texts, left-aligned
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")
    t.write("        "+svgtext("  4.5","-43.5 ","Some static text")+"\n")
    t.write("        "+svgtext("  4.5","-13.5 ","More static text")+"\n")
    t.write("      </g>\n")

    t.write("    </g>\n\n")
    t.close

#- Title block editable texts
def CreateEditableText(file_path, shWidth, shHeight):

    #- offsets for editable texts
    edX=int(shWidth)-10-180 # 180 according to DIN EN ISO 7200
    edY=int(shHeight)-10

    t=open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"titleblock-editable-texts\"\n")
    t.write("      style=\"font-size:7.0;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write("      "+FCeditext("EdiText-1",str(edX+60),str(edY-43.5),"Some editable text")+"\n")
    t.write("      "+FCeditext("EdiText-2",str(edX+60),str(edY-13.5),"More editable text")+"\n")
    t.write("    </g>\n\n")
    t.close

# --- Main section ---

CreateSvgFile(template_file) # overwrites existing File

# Set sheet format (A3)
formatWidth  = "420"
formatHeight = "297"

StartSvg(template_file)  # adds Start tag and namespaces
CreateSheet(template_file, formatWidth, formatHeight)
CreateFrame(template_file, formatWidth, formatHeight)
CreateTitleBlock(template_file, formatWidth, formatHeight)
CreateEditableText(template_file, formatWidth, formatHeight)
EndSvg(template_file)
# At this point a new SVG-file is generated and saved
}}

And this is the svg-code coming out of this macro:

 {{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width ="420mm"
  height="297mm"
  viewBox="0 0 420 297">
    <g id="drawing-frame"
      style="fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round">
      <rect width="390" height="277" x="20" y="10" />
      <rect width="400" height="287" x="15" y="5" />
    </g>

    <g id="titleblock"
      transform="translate(230,287)">
      <g id="titleblock-frame"
        style="fill:none;stroke:#000000;stroke-width:0.35;stroke-linecap:miter;stroke-miterlimit:4">
        <path d="m   0,  0 l   0,-63" />
        <path d="m   0,-63 l 180,  0" />
        <path d="m   0,-30 h 155" />
        <path d="m 155,  0 v -63" />
      </g>
      <g id="titleblock-text-non-editable"
        style="font-size:5.0;text-anchor:start;fill:#000000;font-family:osifont">
        <text x="  4.5" y="-43.5 ">Some static text</text>
        <text x="  4.5" y="-13.5 ">More static text</text>
      </g>
    </g>

    <g id="titleblock-editable-texts"
      style="font-size:7.0;text-anchor:start;fill:#0000d0;font-family:osifont">
      <text freecad:editable="EdiText-1" x="290" y="243.5">  <tspan>Some editable text</tspan>  </text>
      <text freecad:editable="EdiText-2" x="290" y="273.5">  <tspan>More editable text</tspan>  </text>
    </g>

</svg>
}}


</div>


</div>

And what it should look like when inserted (plus magnified title block):

 <img alt="" src=images/TechDraw_TemplateGenerator.png  style="width:600px;">



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateGenerator
