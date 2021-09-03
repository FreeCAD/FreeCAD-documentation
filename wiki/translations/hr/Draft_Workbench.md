


 

<img alt="Draft workbench icon" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduction

The <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Draft Workbench](Draft_Workbench.md) allows you to draw simple 2D objects, and offers several tools to modify them afterwards. It also provides tools to define a working plane, a grid, and a snapping system to precisely control the position of your geometry.

The created 2D objects can be used for general drafting in a way similar as is done with Inkscape or Autocad. These 2D shapes can also be used as the base components of 3D objects created with other workbenches, for example, the <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Part](Part_Workbench.md) and <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Arch Workbenches](Arch_Workbench.md). Conversion of Draft objects to <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Sketches](Sketcher_Workbench.md) is also possible, which means that the shapes can also be used with the <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Workbench](PartDesign_Workbench.md) for the creation of solid bodies.

FreeCAD is primarily a 3D modelling application, and thus its 2D tools aren\'t as advanced as in other drawing programs. If your primary goal is the production of complex 2D drawings and [DXF](DXF.md) files, and you don\'t need 3D modelling, you may wish to consider a dedicated software program for technical drafting such as [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), or others.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

### Crtanje Objekata 

These are tools for creating objects.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Line](Draft_Line.md): draws a line segment between two points.
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyline](Draft_Wire.md): draws a line made of multiple line segments (polyline).
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Fillet](Draft_Fillet.md): draws a fillet (rounded corner) or a chamfer (straight line) between two simple [Lines](Draft_Line.md). <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc.md): draws an arc segment from center, radius, start angle and end angle.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc 3Points](Draft_Arc_3Points.md): draws a circular arc segment from three points that are located in the circumference. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Circle](Draft_Circle.md): draws a circle from center and radius.
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse.md): draws an ellipse from two corner points.
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle.md): draws a rectangle from two corner points.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon.md): draws a regular polygon from center, radius, and number of sides.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline.md): draws a B-Spline from a series of points.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bezier Curve](Draft_CubicBezCurve.md): draws a Bezier curve of third degree by dragging two points. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bezier Curve](Draft_BezCurve.md): draws a Bezier curve from a series of points.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point.md): inserts a point object.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facebinder](Draft_Facebinder.md): creates a new object from selected faces on existing objects.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [ShapeString](Draft_ShapeString.md): inserts a compound shape representing a text string at a given point.

## Annotation objects 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): draws a multi-line text annotation.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): draws a dimension annotation.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): places a label with an arrow pointing to a selected element.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): opens an editor to change the annotation style of these objects. <small>(v0.19)</small> 

### Preinači Objekte 

These are tools for modifying existing objects. They work on selected objects, but if no object is selected, you will be invited to select one.

Many operation tools (move, rotate, array, etc.) also work on solid objects ([Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), [Arch](Arch_Workbench.md), etc.).

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move.md): moves objects from one location to another.
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): rotates objects from a start angle to an end angle.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): scales selected objects around a base point.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): mirrors the selected objects.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset.md): offsets segments of an object a certain distance.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trim/Extend (Trimex)](Draft_Trimex.md): trims or extends an object.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): stretches the selected objects.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): clones the selected objects.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Array tools.
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Ortho Array](Draft_OrthoArray.md): creates an orthogonal array from the selected object. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar Array](Draft_PolarArray.md): creates an array in a polar pattern, that is, sweeping an angle. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Circular Array](Draft_CircularArray.md): creates an array in a circular pattern, that is, starting from a center and moving outwards radially. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md): creates an array of objects by placing the copies along a path.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path LinkArray](Draft_PathLinkArray.md): like <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array of objects by placing the copies at certain points.
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Point LinkArray](Draft_PointLinkArray.md): like <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): edits a selected object.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): enters an edit mode that allows editing different objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): joins lines together into a single wire.
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): splits a wire into two at a point.
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades objects into a higher-level object.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades objects into lower-level objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Wire to BSpline](Draft_WireToBSpline.md): converts a wire to a B-Spline and vice-versa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): converts a Draft object to a [Sketcher Workbench](Sketcher_Workbench.md) Sketch and vice-versa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Slope](Draft_Slope.md): changes the elevation slope of the currently selected [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip Dimension](Draft_FlipDimension.md): flips the orientation of the text of a [Draft Dimension](Draft_Dimension.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md): creates a 2D object which is a flattened 2D view of a 3D object.

## Draft Tray 

The [Draft Tray](Draft_Tray.md) allows selecting the working plane, defining style settings, toggling construction mode, and specifying the active layer or group.

![](images/Draft_tray_default.png )

Its tools are also available in the **Draft → Utilities** menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Select Plane](Draft_SelectPlane.md): selects the current Draft working plane.

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Draft Snap toolbar 

The Draft Snap toolbar allows selecting the active snap options. The buttons belonging to active options stay depressed. For general information about snapping see: [Draft Snap](Draft_Snap.md).

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Toggle snap](Draft_Snap_Lock.md): toggles [object snapping](Draft_Snap.md) globally on or off.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of line, arc and spline segments.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Midpoint](Draft_Snap_Midpoint.md): snaps to the middle point of line and arc segments.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Center](Draft_Snap_Center.md): snaps to the center point of circles, arcs and faces, [WP proxies](Draft_WorkingPlaneProxy.md) and [Building parts](Arch_BuildingPart.md)
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Angle](Draft_Snap_Angle.md): snaps to the special cardinal points of circles and arcs, at 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two line or arc segments. Hover the mouse over the two desired objects to activate their intersection snaps.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Perpendicular](Draft_Snap_Perpendicular.md): on line and arc segments, snaps perpendicularly to the latest point.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Extension](Draft_Snap_Extension.md): snaps on an imaginary line that extends beyond the endpoints of line segments. Hover the mouse over the desired object to activate its extension snap.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallel](Draft_Snap_Parallel.md): snaps on an imaginary line parallel to a line segment. Hover the mouse over the desired object to activate its parallel snap.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Special](Draft_Snap_Special.md): snaps on special points defined by the object.
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Near](Draft_Snap_Near.md): snaps to the closest point or edge on the nearest object.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortho](Draft_Snap_Ortho.md): snaps on imaginary lines that cross the last point, and extend at 0°, 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Grid](Draft_Snap_Grid.md): snaps to the intersections of the grid lines, if the grid is visible.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Working plane](Draft_Snap_WorkingPlane.md): always places the snapped point on the current [working plane](Draft_SelectPlane.md), even if you snap to a point outside that working plane.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions while snapping.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle grid](Draft_ToggleGrid.md): toggles the visibility of the grid on or off.

### Uslužni alati 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a Layer in the current document, to which objects can be added to control object visibility and color. It replaces Draft VisGroup. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Working Plane Proxy](Draft_WorkingPlaneProxy.md): create a proxy object to store the current [Working Plane](Draft_SelectPlane.md) position.
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle display mode](Draft_ToggleDisplayMode.md): switches the display mode of selected objects between \"Flat Lines\" and \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Add to group](Draft_AddToGroup.md): quickly adds selected objects to an existing [Std Group](Std_Group.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group contents](Draft_SelectGroup.md): selects the contents of a selected [Std Group](Std_Group.md) or [Draft Layer](Draft_Layer.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): add selected objects to the Construction group.
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

## Additional tools 

The **Draft → Utilities** menu contains several tools. Most of them can also be accessed from toolbars or the [Draft Tray](Draft_Tray.md) and have already been mentioned above. For the following tools this is not the case:

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): toggles the Draft continue mode on or off.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Apply current style](Draft_ApplyStyle.md): applies the current style to selected objects and groups.
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Show snap bar](Draft_ShowSnapBar.md): shows the [Draft Snap toolbar](#Draft_Snap_toolbar.md).

## Additional features 

-   [Working plane](Draft_SelectPlane.md): allows you to select a surface on which to build your shapes.
-   [Snapping](Draft_Snap.md): place new points on special places on existing objects or on the grid.
-   [Constraining](Draft_Constrain.md): limits the cursor to horizontal or vertical movements relative to a previous point.
-   [Construction mode](Draft_ToggleConstructionMode.md): places created geometry objects in a dedicated group making it easier to switch them on and off.
-   [Pattern](Draft_Pattern.md): Draft objects with a face can display a hatch pattern.

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options 

If there is a selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Selection options 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Obsolete tools 

These commands are obsolete but still available:

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): creates a polar or rectangular array from selected objects. {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

### Postavke

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferences](Draft_Preferences.md): general preferences for the working plane and the drawing tools.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): preferences available for importing from and exporting to different file formats.

## File formats 

These are functions for opening, importing or exporting other file formats. Opening will open a new document with the contents of the file, while importing will append the contents of the file to the current document. Export will save the selected objects to a file. If nothing is selected, all objects will be exported. Be aware that the purpose of the Draft Workbench is to work with 2D objects, so those import routines focus only on 2D objects, and although DXF and OCA formats also support object definitions in 3D space (objects are not necessarily flat), they will not import volumetric objects such as meshes, 3D surfaces, etc., but rather lines, circles, texts or flat shapes. Currently supported file formats are: The Draft Workbench provides FreeCAD with importers and exporters for the following file formats:

-   [Autodesk .DXF](Draft_DXF.md): imports and exports [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF) files created with 2D CAD applications. See also [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md).
-   [Autodesk .DWG](Draft_DXF.md): imports and exports DWG files via the DXF importer, when the [ODA Converter](Extra_python_modules#ODA_Converter_(previously_Teigha_Converter).md) utility is installed. See also [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md).
-   [Scalable Vector Graphics .SVG](Draft_SVG.md): imports and exports [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) files created with vector drawing applications.
-   [Open Cad format .OCA](Draft_OCA.md): imports and exports OCA/GCAD files, a potentially new [open CAD file format](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT.md): imports DAT files describing [Airfoil profiles](http://www.ae.illinois.edu/m-selig/ads/coord_database.html).

### Install importers 

-   [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md): Imports and exports DWG files
-   [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md): Imports and exports DXF files

## Unit tests 


**See also:**

[Test Workbench](Test_Workbench.md).

To run the unit tests of the workbench execute the following from the operating system terminal. 
```python
freecad -t TestDraft
```

## Scripting

The Draft tools can be used in [macros](macros.md) and from the [Python](Python.md) console by using the [Draft API](Draft_API.md).

The workbench includes a module to create samples of all objects in a new document. <small>(v0.19)</small> 

Use this to test that all objects are produced correctly. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Inspecting the code of this module is useful to understand how to use the programming interface. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Where `$INSTALLDIR` is the toplevel directory where the software was installed; for example, in Linux it may be `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Test objects for the [Draft Workbench](Draft_Workbench.md).*

## Tutorials

-   [Draft tutorial](Draft_tutorial.md)
-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
