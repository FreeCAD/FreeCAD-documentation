# Path ToolShape/en
{{TOCright}}

## Description

ToolShapes are a core part of the [Path Tools](Path_Tools.md) system. ToolShapes are the templates from which ToolBits are created. They represent the specific physical shape of a tool. A ToolShape does not completely describe the bit - for that some additional parameters are needed which will be added when an actual bit is parameterized from the template.

Initially ToolShapes are just FreeCAD documents with a single Body created from the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Part Design ](PartDesign_Workbench.md) workbench.

Creating new ToolShapes is an advanced topic. The most commonly needed ToolShapes already exist and are provided with the FreeCAD installation at:

-   On Linux it is usually `/usr/lib64/FreeCAD/Mod/Path/Tools/Shape`
-   On Windows it is usually `C:\Program Files\FreeCAD\Mod\Path\Tools\Shape`
-   On macOS it is usually `/Applications/FreeCAD/Mod/Path/Tools/Shape`

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
2.  Open the <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md).
3.  Create a [Body](PartDesign_Body.md) and give the Body a label you want to show up in the bit selection.
4.  Create a <img alt="" src=images/PartDesign_NewSketch.svg  style="width:16px;"> [Sketch](PartDesign_NewSketch.md) on the XZ plane and draw half the profile of the bit.
5.  Constrain the bottom most center of the bit on the origin `(0,0)`. This will be the center of the axis on which the G-code will rotate the bit.
    -   Note: Do not add dimensional constraints at this time.
6.  Close the Sketch.
7.  <img alt="" src=images/PartDesign_Revolution.svg  style="width:16px;"> [Revolve](PartDesign_Revolution.md) the Sketch around the vertical Sketch axis.
8.  Open the <img alt="" src=images/Workbench_Path.svg  style="width:16px;"> [Path Workbench](Path_Workbench.md).
9.  Select the Sketch in the [Tree view](Tree_view.md). This ensures that the PropertyBag created in the next step will be nested in the Body.
10. Select the **Path → Utils → PropertyBag** option from the menu.
11. A PropertyBag named {{Value|Attributes}} is created. This PropertyBag will be used to control the dimensions in the Sketch.
12. Double-click the PropertyBag in the [Tree view](Tree_view.md).
13. The **Property Bag** task panel opens.
14. Click the **Add...** button.
15. The **Create Property** dialog opens.
16. Create a property named {{Value|Diameter}}. This property is mandatory for ToolBits. Property names are case-sensitive and may not contain spaces.
17. Select {{Value|Shape}} from the **Group** dropdown list.
18. Select the appropriate **Type**.
19. Optionally specify a **ToolTip**.
20. Click the **OK** button.
21. In the **Property Bag** task panel enter a value for the **Diameter** property.
22. Similarly add all other required properties.
23. Click the **OK** button in the **Property Bag** task panel when done.
24. Double-click the Sketch in the [Tree view](Tree_view.md).
25. Add dimensional constraints and apply the properties from the created PropertyBag. For example to apply the **Diameter** property:
    1.  Double-click a dimension.
    2.  Click the <img alt="" src=images/Bound-expression.svg  style="width:16px;"> icon.
    3.  Enter {{Value|<<Attributes>>.Diameter}} in the **Formula editor**.
    4.  Click the **OK** button twice.
26. Repeat this until the Sketch is fully constrained.
27. Save the {{FileName|FCStd}} file where FreeCAD expects to find ToolBit files. See [Description](#Description.md) above.

-   Note 1. If you are denied access to the folder on Windows, start FreeCAD in ADMINISTRATOR mode.
-   Note 2. The Body of the ToolBit must be the first object in the [Tree view](Tree_view.md). These instructions ensure that this is the case.

## Tool Thumbnail Images 

ToolBits will have a small icon image of the tool in the [Tree view](Tree_view.md) if the file is saved with thumbnails active.

Important notes:

-   Before saving the document make sure you have Save Thumbnail selected, and Add program logo deselected in FreeCAD\'s preferences.
-   Also make sure to switch to Front View and Fit content to screen
-   Whatever you see when saving the document will end up being the visual representation of the template





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolShape/en
