---
 TutorialInfo:
   Topic: Create a TechDraw template using a Python macro
   Level: Basic skills of Python and svg-structures are helpful
   FCVersion: 0.21 and later
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

**Note:** When FreeCAD was migrated from **freecadweb.org** to **freecad.org** this page was updated accordingly and the resulting SVG code is no longer compatible with FreeCAD versions older than v0.21. For those versions you need to manually change {{Incode|freecad.org}} to {{Incode|freecadweb.org}} on the namespace declaration line in the resulting SVG code, otherwise the editable texts are not recognized.

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
:   **xmlns:freecad=**\"\...=Svg_Namespace\": External link to FreeCAD\'s [Svg Namespace](Svg_Namespace.md) wiki page. The link is not used to retrieve information or values at runtime, but it is the key to activate the custom attributes, e.g. those for editable texts.
:   \"freecad:\" will be prefixed to said custom attribute names.
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
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}

## Python code\... 

Coding starts with a framework containing a separate main function:

 {{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2024 Your name LGPL


def main():
    """Here is where the magic happens"""
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}

### \... to create a blank page 

The process of creating a template consists of:

-   Locate the template folder.
-   Open a file for writing to create an svg-file from scratch, write the header line and close the file as a first step.
-   And then repeatedly open the file to append further segments, closing it again each time.

The macro is made of several functions which are called from the main section.
Additional functions could be inserted before the EndSvg function and the needed calls are put before the EndSvg() call.
We need to have an eye on the number of spaces used with the write operations for a correct indentation.

#### pathToTemplate()

Before any code is generated a folder is needed to store the new template file, and a file name has to be set.

The user should have selected a template folder. Its path is then stored in the TechDraw preferences.  It is not necessary to know where the preferences are store, because FreeCAD has commands to address needed parameters directly.

 {{Code| |code=
def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file
}}

**parameter_path** receives the path to the \"folder\" within the configuration file where \"TemplateDir\" parameter can be found.  **template_path** receives the content of \"TemplateDir\" which is the path to the template directory.
**template_name** recieves the name of the template to be created.

Now the template name needs to be linked to the template path in a way that is compatible to unix based OSs and Windows. This is done with the \"os.path.join\" command and stored into the **template_file**. To enable this command an \"import os\" instruction is required.

#### createSvgFile()

This creates a new Template file and saves the xml head line.

 {{Code| |code=
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close
}}

#### startSvg()

This appends the template file and creates the svg opening tag including its attributes.
Each write instruction contains one single line of svg code ending with \"\\n\", the marker for CR/LF.

 {{Code| |code=
def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close
}}

#### endSvg()

This further appends the template file and creates the svg closing tag; This eventually finishes the template code.

 {{Code| |code=
def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close
}}

#### main()

The main() function calls the functions and hands over some parameters.

 {{Code| |code=
def main():
    """This one creates an empty A3 template"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return
}}

In this example {{Incode|format_width}} and {{Incode|format_height}} are hard coded dimensions, both unnecessary lines mark the points where other means of retrieving format data could put their content.


<div class="mw-collapsible mw-collapsed toccolours">

#### The complete blank page macro 

This macro consists of the above code segments, ready to run.


<div class="mw-collapsible-content">

 {{Code| |code=
#! python
# -*- coding: utf-8 -*-
# (c) 2024 Your name LGPL

import os  # to enable the use of os.path.join()


# - SVG creation -
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close

def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file

def main():
    """This one creates an empty A3 template"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
}}


</div>


</div>

### \... to create a page with some ink 

To make a drawing out of a blank page we need:

-   Frames i.e. rectangles created with the **rect** instruction.
-   A title block and more made of lines created with the **path** instruction.
-   Simple texts for indexes and labeling title block cells.
-   Editable texts like part number or part name.

Normally these graphical elements are used repeatedly and so the generating code is put into four functions:

-   svgRect() for rectangular frame elements.
-   svgPath() for straight line elements.
-   svgText() for static texts.
-   ediText() for editable texts.

All functions are placed inside the above macro before the main() function and their related function calls are inserted in the main() function between {{Incode|startSvg(...)}} and {{Incode|endSvg(...)}}.

#### svgRect()

To draw a rectangle we just need to call the **svgRect** function and hand over the values for width, height, and position of the upper left corner. That is better readable in this place than if svg_line would contain the whole svg code line.

 {{Code| |code=
def svgRect(width, height, x, y):
    # Generates an svg-instruction to draw a rectangle with the given values
    svg_line = (
        "<rect width=\"" + width + "\" height=\"" + height + "\" x=\"" + x
        + "\" y=\"" + y + "\" />"
        )
    return svg_line
}}

The svg instruction is split to stay within the recommended Python line length, it will result in a single svg line nevertheless.

#### svgPath()

To draw a line we just need to call the **svgPath** function and hand over the coordinates of the start point and the endpoint of a line.

Instead of the end point coordinates we can hand over a tag to draw a horizontal (h) or vertical (v) line followed by the length of the line or the tag to draw a horizontal (H) or vertical (V) line followed by the x or y ordinate of the end point.

Each path starts at the origin and the first action is a movement with \"raised pen\" (not drawing) to the start point. In this case the relative movement and the absolute movement are the same and so it is irrelevant whether the m-tag is upper or lower case.

 {{Code| |code=
def svgPath(x1, y1, x2, y2):
    # Generates an svg-instruction to draw a path element (line) with the given values
    if x2 == "v" or x2 == "V" or x2 == "h" or x2 == "H":
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " " + x2 + " " + y2 + "\" />")
    else:
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " l " + x2 + "," + y2 + "\" />")
    return svg_line
}}

#### svgText()

To draw a piece of text we just need to call the **svgText** function and hand over the coordinates of the text\'s anchor point, the text string itself, and optionally an angle for rotated text. To rotate texts a transformation instruction has to be inserted in each text tag separately; the rotation centers are set to the same coordinates as the related text anchor points.

(The text alignment is controlled by the surrounding group tag or left-aligned as default).

 {{Code| |code=
def svgText(x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place a text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated texts
    """
    if str_angle == "0":
        svg_line = ("<text x=\"" + x + "\" y=\"" + y + "\">" + str_value + "</text>")
    else:
        svg_line = (
            "<text x=\"" + x + "\" y=\"" + y + "\" transform=\"rotate(" + str_angle
            + "," + x + "," + y + ")\">" + str_value + "</text>"
            )
    return svg_line
}}

#### ediText()

To draw a piece of editable text we just need to call the **ediText** function and hand over a name, the coordinates of the text\'s anchor point, the text string itself, and optionally an angle for rotated text. To rotate texts a transformation instruction has to be inserted in each text tag separately; the rotation centers are set to the same coordinates as the related text anchor points.

FreeCAD creates a dictionary object with every inserted template, and each entry has a name (key) and a value.

(The text alignment is controlled by the surrounding group tag or left-aligned as default).

 {{Code| |code=
def ediText(entry_name, x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place an editable text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated editable texts
    """
    if str_angle == "0":
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\">  <tspan>" + str_value + "</tspan>  </text>"
            )
    else:
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\" transform=\"rotate(" + str_angle + "," + x + "," + y + ")\">  <tspan>"
            + str_value + "</tspan>  </text>"
            )
    return svg_line
}}

### createXxxx functions 

These functions start with code to open a file in append mode and to write the group opening tag.

Then follows a section to set and calculate values, and with write instructions that call the above functions to generate svg-code.

And finally the group closing tag followed by an instruction to close the file.

 {{Code| |code=
def createFrame(file_path, sheet_width, sheet_height):
    # Creates rectangles for sheet frame and drawing area
    t = open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round\">\n")
    #- upper left corner of inner Frame, drawing area
    frame_x = str(20)
    frame_y = str(10)
    #- frame dimensions
    frame_width = str(int(sheet_width) - 20 - 10)
    frame_height = str(int(sheet_height) - 10 - 10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    #- upper left corner outer frame, sheet frame
    frame_x = str(15)
    frame_y = str(5)
    #- frame dimensions
    frame_width = str(int(sheet_width)-20)
    frame_height = str(int(sheet_height)-10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
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
# (c) 2024 Your name LGPL

import os  # to enable the use of os.path.join()


# - SVG creation -
def createSvgFile(file_path):
    # Create a file and insert a header line (with t as the space saving variant of template)
    t = open(file_path, "w")  # w = write, overwrites existing files
    t.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
    t.close

def startSvg(file_path, sheet_width, sheet_height):
    # Create svg-tag including namespace and format definitions
    t = open(file_path, "a", encoding="utf-8")
    # a = append, new lines are added at the end of an existing file
    # encoding="utf-8", helps with special characters if the Python interpreter is in ASCII mode
    t.write("\n" + "\n")
    t.write("<svg\n")
    #- Namespace declarations
    t.write("  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"\n")
    t.write("  xmlns:freecad=\"http://www.freecad.org/wiki/index.php?title=Svg_Namespace\"\n")
    #- Format definition
    t.write("  width =\"" + sheet_width + "mm\"\n")
    t.write("  height=\"" + sheet_height + "mm\"\n")
    t.write("  viewBox=\"0 0 " + sheet_width + " " + sheet_height + "\">\n")
    # identical values for width and height and Viewbox' width and height
    # will synchronise mm and svg-units
    t.close

def endSvg(file_path):
    # Create closing svg-tag
    t = open(file_path, "a", encoding="utf-8")
    t.write("</svg>")
    t.close

def svgRect(width, height, x, y):
    # Ggenerates an svg-instruction to draw a rectangle with the given values
    svg_line = (
        "<rect width=\"" + width + "\" height=\"" + height + "\" x=\"" + x
        + "\" y=\"" + y + "\" />"
        )
    return svg_line

def svgPath(x1, y1, x2, y2):
    # Generates an svg-instruction to draw a path element (line) with the given values
    if x2 == "v" or x2 == "V" or x2 == "h" or x2 == "H":
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " " + x2 + " " + y2 + "\" />")
    else:
        svg_line = ("<path d=\"m " + x1 + "," + y1 + " l " + x2 + "," + y2 + "\" />")
    return svg_line

def svgText(x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place a text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated texts
    """
    if str_angle == "0":
        svg_line = ("<text x=\"" + x + "\" y=\"" + y + "\">" + str_value + "</text>")
    else:
        svg_line = (
            "<text x=\"" + x + "\" y=\"" + y + "\" transform=\"rotate(" + str_angle
            + "," + x + "," + y + ")\">" + str_value + "</text>"
            )
    return svg_line

def ediText(entry_name, x, y, str_value, str_angle="0"):
    """
    Generates an svg-instruction to place an editable text element with the given values.
    Optional str_angle enables vertical and arbitrarily rotated editable texts
    """
    if str_angle == "0":
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\">  <tspan>" + str_value + "</tspan>  </text>"
            )
    else:
        svg_line = (
            "<text freecad:editable=\"" + entry_name + "\" x=\"" + x + "\" y=\"" + y
            + "\" transform=\"rotate(" + str_angle + "," + x + "," + y + ")\">  <tspan>"
            + str_value + "</tspan>  </text>"
            )
    return svg_line

def createFrame(file_path, sheet_width, sheet_height):
    # Creates rectangles for sheet frame and drawing area
    t = open(file_path, "a", encoding="utf-8")
    t.write("    <g id=\"drawing-frame\"\n")
    t.write("      style=\"fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round\">\n")
    #- calculate upper left corner of inner Frame, drawing area
    frame_x = str(20)
    frame_y = str(10)
    #- frame dimensions
    frame_width = str(int(sheet_width) - 20 - 10)
    frame_height = str(int(sheet_height) - 10 - 10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    #- calculate upper left corner outer frame, sheet frame
    frame_x = str(15)
    frame_y = str(5)
    #- frame dimensions
    frame_width = str(int(sheet_width)-20)
    frame_height = str(int(sheet_height)-10)
    #- frame rectangle
    t.write("      " + svgRect(frame_width, frame_height, frame_x, frame_y) + "\n")
    t.write("    </g>\n\n")
    t.close

def createTitleBlock(file_path, sheet_width, sheet_height):
    """Creates a title block and transfers it to the position according to the sheet dimensions"""
    #- calculate title block origin (lower left corner), offset from page origin
    tbX = str(int(sheet_width) - 10 - 180)  # 180 according to DIN EN ISO 7200
    tbY = str(int(sheet_height) - 10)
    t = open(file_path, "a", encoding="utf-8")
    #- group to transfer all included title block elements at once
    t.write("    <g id=\"titleblock\"\n")
    t.write("      transform=\"translate(" + tbX + "," + tbY + ")\">\n")
    #- sub-group of title block line framework
    t.write("      <g id=\"titleblock-frame\"\n")
    t.write("        style=\"fill:none;stroke:#000000;stroke-width:0.35;\
stroke-linecap:miter;stroke-miterlimit:4\">\n")
    t.write("        " + svgPath("  0","  0","  0","-63") + "\n")
    t.write("        " + svgPath("  0","-63","180","  0") + "\n")
    t.write("        " + svgPath("  0","-30","h","155") + "\n")
    t.write("        " + svgPath("155","  0","v","-63") + "\n")
    t.write("      </g>\n")
    #- sub-group of title block static texts (left-aligned by default)
    t.write("      <g id=\"titleblock-text-non-editable\"\n")
    t.write("        style=\"font-size:5.0;text-anchor:start;fill:#000000;\
font-family:osifont\">\n")
    t.write("        " + svgText("  4.5","-43.5 ","Some static text") + "\n")
    t.write("        " + svgText("  4.5","-13.5 ","More static text") + "\n")
    t.write("        " + svgText("162.5","-3.5 ","Vertical static text","-90") + "\n")
    t.write("      </g>\n")
    t.write("    </g>\n\n")
    t.close

def createEditableText(file_path, sheet_width, sheet_height):
    """Creates editable texts positioned according to the page origin"""
    #- calculate offset to titleblock origin
    edX = int(sheet_width) - 10 - 180 # 180 according to DIN EN ISO 7200
    edY = int(sheet_height) - 10
    t = open(file_path, "a", encoding="utf-8")
    #- group editable texts using the same attributes
    t.write("    <g id=\"titleblock-editable-texts\"\n")
    t.write("      style=\"font-size:7.0;text-anchor:start;fill:#0000d0;\
font-family:osifont\">\n")
    t.write(
        "      " + ediText("EdiText-1",str(edX + 60),str(edY - 43.5),"Some editable text") + "\n"
        )
    t.write(
        "      " + ediText("EdiText-2",str(edX + 60),str(edY - 13.5),"More editable text") + "\n"
        )
    t.write(
        "      " + ediText("EdiText-3",str(edX + 173),str(edY - 4.5),"90° editable text","-90")
        + "\n"
        )
    t.write("    </g>\n\n")
    t.close

def pathToTemplate(template_name):
    """Link a given template name to the path of the template folder"""
    #- Get the path to the template folder that is set in the FreeCAD parameters
    parameter_path = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/TechDraw/Files")
    template_path = parameter_path.GetString("TemplateDir")
    #- Link template_path and template_name for any OS
    path_to_file = os.path.join(template_path, template_name)  # to join path segments OS neutral
    return path_to_file

def main():
    """This one creates an A3 template with simple frame and title block"""
    #- Set the name of the template file and get its location
    template_file = pathToTemplate("MyTemplate.svg")  # Change the template name here
    #- Here starts the compiling of the svg file
    createSvgFile(template_file)  # overwrites existing File
    #- Set sheet format (DIN A3)
    format_width  = "420"
    format_height = "297"
    startSvg(template_file, format_width, format_height)  # adds svg start tag
    createFrame(template_file, format_width, format_height)
    createTitleBlock(template_file, format_width, format_height)
    createEditableText(template_file, format_width, format_height)
    endSvg(template_file)  # adds svg end tag
    # At this point a new SVG-file is generated and saved
    return

if __name__ == '__main__':
    # This will be true only if the file is "executed"
    # but not if imported as module
    main()
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
        <text x="162.5" y="-3.5 " transform="rotate(-90,162.5,-3.5 )">Vertical static text</text>
      </g>
    </g>

    <g id="titleblock-editable-texts"
      style="font-size:7.0;text-anchor:start;fill:#0000d0;font-family:osifont">
      <text freecad:editable="EdiText-1" x="290" y="243.5">  <tspan>Some editable text</tspan>  </text>
      <text freecad:editable="EdiText-2" x="290" y="273.5">  <tspan>More editable text</tspan>  </text>
      <text freecad:editable="EdiText-3" x="403" y="282.5" transform="rotate(-90,403,282.5)">  <tspan>90° editable text</tspan>  </text>
    </g>

</svg>
}}


</div>


</div>

And what it should look like when inserted (plus magnified title block):

 <img alt="" src=images/TechDraw_TemplateGenerator.png  style="width:600px;"> 

To color the editable texts in blue is just a personal choice to easier distinguish static and editable texts on the finished drawing.



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateGenerator
