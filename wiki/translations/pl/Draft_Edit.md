---
- GuiCommand:/pl
   Name:Draft Edit
   Name/pl:Rysunek Roboczy: Edytuj
   MenuLocation:Modyfikacja → Edytuj
   Workbenches:[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   Shortcut:**D** **E**
   SeeAlso:[Edytuj](Std_Edit/pl.md)
---

# Draft Edit/pl

## Description

The <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> **Draft Edit** command puts selected objects in Draft Edit mode. In this mode the properties of objects can be edited graphically. Typically nodes can be moved and in some cases context menu options can be selected. The command can handle most Draft objects, but also some other objects. See [Supported objects](#Supported_objects.md). Supported Draft objects can also be put in Draft Edit mode with the [Std Edit](Std_Edit.md) command.

![](images/Draft_Edit_example.png ) 
*4 objects in Draft Edit mode: a Draft Wire (red), a Draft Arc (black), a Draft BSpline (green) and a Draft BezCurve (magenta)*

## Usage

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  Optionally select one or more objects. Note that although multiple objects can be in Draft Edit mode, objects can only be edited one at a time.
2.  There are several ways to invoke the command:
    -   If you have not yet selected an object: double-click an object in the [Tree view](Tree_view.md). This only works for supported Draft objects.
    -   Press the **<img src="images/Draft_Edit.svg" width=16px> [Draft Edit](Draft_Edit.md)** button.
    -   Select the **Modification → <img src="images/Draft_Edit.svg" width=16px> Edit** option from the menu.
    -   Use the keyboard shortcut: **D** then **E**.
3.  If you have not yet selected an object: select an object in the [3D view](3D_view.md).
4.  The selected objects are marked with temporary nodes, and the [Main task panel](#Main_task_panel.md) opens. See [Options](#Options.md) for more information.
5.  Optionally use a node or edge context menu. These context menus are only available for some Draft objects. See [Supported objects](#Supported_objects.md) for more information.
    -   Do one of the following:
        -   On all operating systems: hold down **E** and click the node or edge. To use **E** you may have to click in the [3D view](3D_view.md) once to ensure that it has the focus.
        -   On Windows: hold down **Alt** and click the node or edge.
        -   On Linux: hold down **Shift**+**Alt**, **Ctrl**+**Alt** or **Alt**, and click the node or edge.
        -   On macOS: hold down **Option** and click the node or edge.
    -   Select an option from the context menu.
    -   If the selected option requires point input:
        -   The [Edit node task panel](#Edit_node_task_panel.md) opens. See [Options](#Options.md) for more information.
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
6.  Optionally move a node:
    -   Click the node in the [3D view](3D_view.md).
    -   The [Edit node task panel](#Edit_node_task_panel.md) opens. See [Options](#Options.md) for more information.
    -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   The result depends on the object and the selected node.
7.  Press **Esc** or the **Close** button (the button at the top of the task panel, without the image) to finish the command.

## Options

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

### Main task panel 

-   Press **Esc** or the **Close** button to finish the command.

### Edit node task panel 

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   To use polar coordinates enter a value for the **Length** and a value for the **Angle**, and press **Enter** after each.
-   Check the **Angle** checkbox to constrain the pointer to the specified angle.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.

## Supported objects 

### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Draft Line](Draft_Line.md) and <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) 

-   If the start or end node of an open wire is moved so that they coincide, the wire is closed.
-   Node context menu: {{Value|Delete point}}. At least two points must remain.
-   Edge context menu: {{Value|Add point}}, {{Value|Close/Open wire}} (<small>(v1.0)</small> ) and {{Value|Reverse wire}} (<small>(v0.20)</small> ).

### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Draft Arc](Draft_Arc.md) and <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Draft Arc 3Points](Draft_Arc_3Points.md) 

-   Center node context menu: {{Value|Move arc}}.
-   Start node context menu: {{Value|Set first angle}}.
-   End node context menu: {{Value|Set last angle}}.
-   Mid node context menu: {{Value|Set radius}}.
-   Edge context menu: {{Value|Invert arc}}.

### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Draft Circle](Draft_Circle.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Draft Ellipse](Draft_Ellipse.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Draft Polygon](Draft_Polygon.md) 

-   No context menus for this object.

### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Draft BSpline](Draft_BSpline.md) 

-   If the start or end node of an open spline is moved so that they coincide, the spline is closed.
-   Node context menu: {{Value|Delete point}}. At least two points must remain for an open spline. For a closed spline the minimum number of points is three.
-   Edge context menu: {{Value|Add point}}, {{Value|Close/Open spline}} (<small>(v1.0)</small> ) and {{Value|Reverse spline}} (<small>(v1.0)</small> ).

### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Draft CubicBezCurve](Draft_CubicBezCurve.md) and <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Draft BezCurve](Draft_BezCurve.md) 

-   If the start or end node of an open curve is moved so that they coincide, the curve is closed.
-   Node context menu: {{Value|Delete point}}, {{Value|Make sharp}}, {{Value|Make tangent}} and {{Value|Make symmetric}}.
-   Edge context menu: {{Value|Add point}}, {{Value|Close/Open curve}} (<small>(v1.0)</small> ) and {{Value|Reverse curve}} (<small>(v1.0)</small> ).

### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Dimension](Draft_Dimension.md) 

-   Angular dimensions cannot be edited.
-   The start and end nodes of parametric dimensions cannot be moved.
-   No context menus for this object.

### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Arch Wall](Arch_Wall.md) 

-   A single node to control the height of the wall is displayed above the **Placement** of the wall.
-   No context menus for this object.

### <img alt="" src=images/Arch_Structure.svg  style="width:24px;"> [Arch Structure](Arch_Structure.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Arch Window](Arch_Window.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Space.svg  style="width:24px;"> [Arch Space](Arch_Space.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Panel_Cut.svg  style="width:24px;"> [Arch Panel Cut](Arch_Panel_Cut.md) 

-   No context menus for this object.

### <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:24px;"> [Arch Panel Sheet](Arch_Panel_Sheet.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Box](Part_Box.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Part Cylinder](Part_Cylinder.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Part Sphere](Part_Sphere.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cone](Part_Cone.md) 

-   No context menus for this object.

### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Part Line](Part_Line.md) 

-   No context menus for this object.

### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Sketch](Sketcher_NewSketch.md) 

-   Only sketches that contain a single unconstrained line can be edited.
-   No context menus for this object.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The color of the temporary nodes is the same as the color of the snap symbols. This color can be changed in the preferences: **Edit → Preferences... → Draft → Visual settings → Visual Settings → Color**. Note that this color is not used for the temporary nodes displayed for [Draft BezCurves](Draft_BezCurve.md). These nodes use the **Line Color** of the curve instead.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

There is no Python method to Draft Edit objects. To emulate the results of the command geometric properties of objects have to be modified.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Edit/pl
