 




 

## Description

ToolShapes are a core part of the [Path Tools](Path_Tools.md) system. ToolShapes are the templates from which ToolBits are created. They represent the specific physical shape of a tool. A ToolShape does not completely describe the bit - for that some additional parameters are needed which will be added when an actual bit is parameterized from the template.

Initially ToolShapes are just FreeCAD documents with a single Body created from the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench.md) workbench.

Creating new ToolShapes is an advanced topic. The most commonly needed ToolShapes already exist and are provided with the FreeCAD installation at

-   On Linux it is usually `/usr/lib64/FreeCAD/Mod/Path/Tools/Shape`
-   On Windows it is usually `C:\Program Files\FreeCAD\Mod\Path\Tools\Shape`
-   On macOS it is usually `/Applications/FreeCAD/Mod/Path/Tools/Shape` {{ColoredText||Red|--> has to be revised}}

They are:

:   
    {{FileName|ballend.fcstd}}
    

:   
    {{FileName|bullnose.fcstd}}
    

:   
    {{FileName|chamfer.fcstd}}
    

:   
    {{FileName|drill.fcstd}}
    

:   
    {{FileName|endmill.fcstd}}
    

:   
    {{FileName|probe.fcstd }}
    

:   
    {{FileName|slittingsaw.fcstd}}
    

:   
    {{FileName|thread-mill.fcstd }}
    

:   
    {{FileName|v-bit.fcstd}}
    

These can be found in the {{FileName|/Mod/Path/Tools/Shape/}} subdirectory where FreeCAD was installed.

## Usage

1.  Create a new FreeCAD document
2.  Open the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench.md) workbench
3.  Create a body and give the body a label you want to show up in the bit selection.
4.  Create a sketch in the XZ plane and draw half the profile of the bit.
    -   Put the top center of the bit on the origin `(0,0)`
5.  For any constraint serving as a parameter for the tool (like overall Length) create a named constraint
    -   The name is the label of the input field
    -   Names are split at CamelCase boundaries into words in the edit dialog
    -   Use a `;` in the name to add help text which will show up as the entry fields tool tip
    -   If the tool is used by legacy ops it should at least have one constraint called Diameter
    -   Use construction lines for constraints that are not directly accessible, like Diameter and Angle
    -   Any unnamed constraint will not be editable for a specific tool
6.  Once the sketch is fully constrained, close the sketch
7.  Revolve the sketch around the z-axis
8.  Save the document as a new file in the Shape directory

## Tool Thumbnail Images 

Toolbits will have a small icon image of the tool in the tree if the image is saved with thumbnails active.

Important notes:

-   Before saving the document make sure you have Save Thumbnail selected, and Add program logo deselected in FreeCAD\'s preferences.
-   Also make sure to switch to Front View and Fit content to screen
-   Whatever you see when saving the document will end up being the visual representation of the template

## Options




 {{Path_Tools_navi}} 
