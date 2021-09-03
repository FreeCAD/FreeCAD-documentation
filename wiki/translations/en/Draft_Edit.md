---
- GuiCommand:
   Name:Draft Edit
   MenuLocation:Modification → Edit<br>Utilities → Edit
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**D** **E**
   SeeAlso:[Std Edit](Std_Edit.md)
---

## Description

The <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> **Draft Edit** command puts selected objects in Draft Edit mode. In this mode the properties of objects can be edited graphically. Typically nodes can be moved and in some cases context menu options can be selected. The command can handle most Draft objects, but also some other objects. See [Supported objects](#Supported_objects.md). Supported Draft objects can also be put in Draft Edit mode with the [Std Edit](Std_Edit.md) command.

![](images/Draft_Edit_example.png ) *4 objects in Draft Edit mode: a Draft Wire (red), a Draft Arc (black), a Draft BSpline (green) and a Draft BezCurve (magenta)*

## Usage

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  Optionally select one or more objects. Note that although multiple objects can be in Draft Edit mode, objects can only be edited one at a time.
2.  There are several ways to invoke the command:
    -   If you have not yet selected an object: double-click an object in the [Tree view](Tree_view.md). This only work for supported Draft objects.
    -   Press the **<img src="images/Draft_Edit.svg" width=16px> [Draft Edit](Draft_Edit.md)** button.
    -   Select the {{MenuCommand|Modification → <img src="images/Draft_Edit.svg" width=16px> Edit}} option from the menu.
    -   Select the {{MenuCommand|Utilities → <img src="images/Draft_Edit.svg" width=16px> Edit}} option from the menu.
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
        -   The [Node task panel](#Node_task_panel.md) opens. See [Options](#Options.md) for more information.
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
6.  Optionally move a node:
    -   Click the node in the [3D view](3D_view.md).
    -   The [Node task panel](#Node_task_panel.md) opens. See [Options](#Options.md) for more information.
    -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   The result depends on the object and the selected node.
7.  Press **Esc** or the **Close** button to finish the command.

## Options

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).

### Main task panel {#main_task_panel}

-   Press **O** or the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button to finish the command. If a single [Draft Wire](Draft_Wire.md) has been selected the wire is closed.
-   Press **Esc** or the **Close** button to finish the command.

### Node task panel {#node_task_panel}

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   To use polar coordinates enter a value for the {{MenuCommand|Length}} and a value for the {{MenuCommand|Angle}}, and press **Enter** after each.
-   Check the {{MenuCommand|Angle}} checkbox to constrain the pointer to the specified angle.
-   The {{MenuCommand|Relative}} checkbox has no purpose for this command.
-   Press **G** or click the {{MenuCommand|Global}} checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   The {{MenuCommand|Continue}} checkbox has no purpose for this command.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   The {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button has no purpose for this command.

## Supported objects {#supported_objects}

### <img alt="" src=images/Draft_Line.svg  style="width:24px;"> [Draft Line](Draft_Line.md) and <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) {#draft_line.svg_draft_line_and_draft_wire.svg_draft_wire}

-   If the start or end node of an open wire is moved so that they coincide, the wire is closed.
-   Node context menu: {{Value|delete point}}. At least two points must remain.
-   Edge context menu: {{Value|add point}}, {{Value|reverse wire}} (<small>(v0.20)</small> ).

### <img alt="" src=images/Draft_Arc.svg  style="width:24px;"> [Draft Arc](Draft_Arc.md) and <img alt="" src=images/Draft_Arc_3Points.svg  style="width:24px;"> [Draft Arc 3Points](Draft_Arc_3Points.md) {#draft_arc.svg_draft_arc_and_draft_arc_3points.svg_draft_arc_3points}

-   Center node context menu: {{Value|move arc}}.
-   Start node context menu: {{Value|set first angle}}.
-   End node context menu: {{Value|set last angle}}.
-   Mid node context menu: {{Value|set radius}}.
-   Edge context menu: {{Value|invert arc}}. Currently this does not work.

### <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> [Draft Circle](Draft_Circle.md) {#draft_circle.svg_draft_circle}

-   No context menus for this object.

### <img alt="" src=images/Draft_Ellipse.svg  style="width:24px;"> [Draft Ellipse](Draft_Ellipse.md) {#draft_ellipse.svg_draft_ellipse}

-   No context menus for this object.

### <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) {#draft_rectangle.svg_draft_rectangle}

-   No context menus for this object.

### <img alt="" src=images/Draft_Polygon.svg  style="width:24px;"> [Draft Polygon](Draft_Polygon.md) {#draft_polygon.svg_draft_polygon}

-   No context menus for this object.

### <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [Draft BSpline](Draft_BSpline.md) {#draft_bspline.svg_draft_bspline}

-   If the start or end node of an open spline is moved so that they coincide, the spline is closed.
-   Node context menu: {{Value|delete point}}. At least two points must remain for an open spline. For a closed spline the minimum number of points is three.
-   Edge context menu: {{Value|add point}}.

### <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> [Draft CubicBezCurve](Draft_CubicBezCurve.md) and <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;"> [Draft BezCurve](Draft_BezCurve.md) {#draft_cubicbezcurve.svg_draft_cubicbezcurve_and_draft_bezcurve.svg_draft_bezcurve}

-   If the start or end node of an open curve is moved so that they coincide, the curve is closed.
-   Node context menu: {{Value|make sharp}}, {{Value|make tangent}}, {{Value|make symmetric}} and {{Value|delete point}}.
-   Edge context menu: {{Value|add point}}.

### <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Dimension](Draft_Dimension.md) {#draft_dimension.svg_draft_dimension}

-   Angular dimensions cannot be edited.
-   The start and end nodes of parametric dimensions cannot be moved.
-   No context menus for this object.

### <img alt="" src=images/Arch_Wall.svg  style="width:24px;"> [Arch Wall](Arch_Wall.md) {#arch_wall.svg_arch_wall}

-   A single node to control the height of the wall is displayed above the **Placement** of the wall.
-   No context menus for this object.

### <img alt="" src=images/Arch_Structure.svg  style="width:24px;"> [Arch Structure](Arch_Structure.md) {#arch_structure.svg_arch_structure}

-   No context menus for this object.

### <img alt="" src=images/Arch_Window.svg  style="width:24px;"> [Arch Window](Arch_Window.md) {#arch_window.svg_arch_window}

-   No context menus for this object.

### <img alt="" src=images/Arch_Space.svg  style="width:24px;"> [Arch Space](Arch_Space.md) {#arch_space.svg_arch_space}

-   No context menus for this object.

### <img alt="" src=images/Arch_Panel_Cut.svg  style="width:24px;"> [Arch Panel Cut](Arch_Panel_Cut.md) {#arch_panel_cut.svg_arch_panel_cut}

-   No context menus for this object.

### <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:24px;"> [Arch Panel Sheet](Arch_Panel_Sheet.md) {#arch_panel_sheet.svg_arch_panel_sheet}

-   No context menus for this object.

### <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Box](Part_Box.md) {#part_box.svg_part_box}

-   No context menus for this object.

### <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [Part Cylinder](Part_Cylinder.md) {#part_cylinder.svg_part_cylinder}

-   No context menus for this object.

### <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [Part Sphere](Part_Sphere.md) {#part_sphere.svg_part_sphere}

-   No context menus for this object.

### <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cone](Part_Cone.md) {#part_cone.svg_part_cone}

-   No context menus for this object.

### <img alt="" src=images/Part_Line.svg  style="width:24px;"> [Part Line](Part_Line.md) {#part_line.svg_part_line}

-   No context menus for this object.

### <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Sketch](Sketcher_NewSketch.md) {#sketcher_newsketch.svg_sketcher_sketch}

-   Only sketches that contain a single unconstrained line can be edited. Currently this does not work properly.
-   No context menus for this object.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The color of the temporary nodes is the same as the color of the snap symbols. This color can be changed in the preferences: {{MenuCommand|Edit → Preferences... → Draft → Visual settings → Visual Settings → Color}}. Note that this color is not used for the temporary nodes displayed for [Draft BezCurves](Draft_BezCurve.md). These nodes use the **Line Color** of the curve instead.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

There is no Python method to Draft Edit objects. To emulate the results of the command geometric properties of objects have to be modified.





 
