# Path ToolShape
## Description

ToolShapes are a core part of the [Path Tools](Path_Tools.md) system. ToolShapes are the templates from which ToolBits are created. They represent the specific physical shape of a tool. A ToolShape does not completely describe the bit - for that some additional parameters are needed which will be added when an actual bit is parameterized from the template.

Initially ToolShapes are just FreeCAD documents with a single Body created from the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design ](PartDesign_Workbench.md) workbench.

Creating new ToolShapes is an advanced topic. The most commonly needed ToolShapes already exist and are provided with the FreeCAD installation at:

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
    {{FileName|probe.fcstd}}
    

:   
    {{FileName|slittingsaw.fcstd}}
    

:   
    {{FileName|thread-mill.fcstd}}
    

:   
    {{FileName|v-bit.fcstd}}
    

These can be found in the {{FileName|/Mod/Path/Tools/Shape/}} subdirectory where FreeCAD was installed.

## Usage

1.  Create a new FreeCAD document.
2.  Open the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design](PartDesign_Workbench.md) workbench.
3.  Create a body and give the body a label you want to show up in the bit selection.
4.  Create a sketch in the XZ plane and draw half the profile of the bit.
5.  In the Combo View Window, switch to Model View so you can see the file structure organization.
6.  While in Sketch mode, constrain the bottom most center of the bit on the origin `(0,0)`. This will be the center of the axis on which the GCODE will rotate the bit.
    -   NOTE: Do not add dimensional constraints at this time.
7.  Close the Sketch.
8.  Revolve the Sketch around the vertical Sketch axis and hit \"OK\" to exit.
9.  Return to the Combo View window in the File Tree and click the arrow to the left of the Revolution so you see the embedded Sketch.
    -   Highlight the Sketch in the FileTree Window.
10. Navigate to the <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Path Workbench](Path_Workbench.md).
11. With the Sketch still highlighted, go to the Menu\>Path\>Utils and select PropertyBag
12. An \"Attributes\" icon in the FileTree will be created below Sketch in the Combo View window which is the \"PropertyBag\" that controls variables within the Sketch.
13. Double click \"Attributes\" icon in the File Tree to open the Property Bag window.
14. Click \"Add\...\" button.
15. Create one variable called \"Diameter\" in the Name Field (a variable named \"Diameter\" is mandatory for Toolbits). All variables are case-sensitive and may not contain spaces.
16. Type \"Shape\" in the Group Field.
17. Select the appropriate variable type.
    -   ToolTip comments is an optional field.
18. Click \"OK\".
19. In the Property Bag window, enter the Value (diameter) you assigned to the \"Diameter\" property.
    -   Add as many Property variables as needed to fully define your Sketch. This includes entering all required dimensions, angles etc. until all fields are completed.
    -   If you have FreeCad set up to work in metric units, you can still enter dimensions in inches units if you desire. FreeCad will change \"in\" to \"mm\" automatically.
20. Click \"OK\" when done.
21. Return to the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> Sketch Workbench to edit the ToolBit. (You may double click \"Sketch\" listed under \"Revolution\" in the Combo View File Tree.)
22. Constrain the dimensions within the Sketch using the Property Bag you made in steps above.
    -   Select a feature such as a line, arc or points in the drawing. Assign a length, radius, dimension etc to the feature as to apply a constraint.
    -   When assigning a value to the feature, click on the little round blue circle instead of entering the value directly. This is where you can invoke the attributes assigned to your recently created PropertyBag.
    -   A formula Editor will open and type in in the following: \"\<\>.Diameter\" (or your appropriate variable name) and hit the \"OK\" button.
    -   The Length field will be greyed out indicating that the field is a fixed constraint in the Attributed Property Bag. Also, the constrained dimensions will be colored Orange indicating that the parameters are kept in an external Property Bag.
    -   Repeat the above constraint assignment procedure above until the Sketch is fully constrained.
23. Save the file as a \*.FCStd file where Freecad expects to find ToolBit Shape files. By default, it is in C://Program Files/Freecad 0.19) \>Mod\>Path\>Tools\>Shape in Windows 10.
    -   EndNote 1. If you are denied access to this file in Windows, start FreeCad in ADMINISTRATOR mode and it will allow access to the folder. You are finally done! Use this new custom built ToolShape in the normal fashion in addition to the standard ToolBits using the PATH workbench.
    -   EndNote 2. The BODY of the Toolbit MUST be listed FIRST in the Combo View FileTree hierarchical structure. These instructions will produce this important structural order to create a successful ToolBit Shape.

## Tool Thumbnail Images 

Toolbits will have a small icon image of the tool in the tree if the image is saved with thumbnails active.

Important notes:

-   Before saving the document make sure you have Save Thumbnail selected, and Add program logo deselected in FreeCAD\'s preferences.
-   Also make sure to switch to Front View and Fit content to screen
-   Whatever you see when saving the document will end up being the visual representation of the template

## Options




 {{Path_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolShape
