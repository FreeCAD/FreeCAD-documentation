# Draft Workbench/sv




 

<img alt="Draft workbench icon" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduction

Rit modulen är ett pågående arbete och är en ganska experimentell modul som har gjorts för att lägga till grundläggande 2d ritfunktionalitet till FreeCAD. Den är helt och hållet skriven i python, och är även tänkt att fungera som en presentation om hur mycket du kan utöka FreeCAD endast med hjälp av python, utan att ens röra källkoden.

The created 2D objects can be used for general drafting in a way similar as is done with Inkscape or Autocad. These 2D shapes can also be used as the base components of 3D objects created with other workbenches, for example, the <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Part](Part_Workbench.md) and <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Arch Workbenches](Arch_Workbench.md). Conversion of Draft objects to <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Sketches](Sketcher_Workbench.md) is also possible, which means that the shapes can also be used with the <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Workbench](PartDesign_Workbench.md) for the creation of solid bodies.

FreeCAD is primarily a 3D modelling application, and thus its 2D tools aren\'t as advanced as in other drawing programs. If your primary goal is the production of complex 2D drawings and [DXF](DXF.md) files, and you don\'t need 3D modelling, you may wish to consider a dedicated software program for technical drafting such as [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), or others.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

### Rita objekt 

Detta är verktyg för att rita objekt.

-   <img alt="" src=images/Draft_Line.png  style="width:32px;"> [2-punkt Linje](Draft_Line/sv.md): Ritar ett linjesegment mellan 2 punkter
-   <img alt="" src=images/Draft_Wire.png  style="width:32px;"> [Tråd (multi-punkts linje)](Draft_Wire/sv.md): Ritar en linje som består av flera linjesegment
-   <img alt="" src=images/Draft_Circle.png  style="width:32px;"> [Cirkel](Draft_Circle/sv.md): Ritar en cirkel med hjälp av centrum och radie
-   <img alt="" src=images/Draft_Arc.png  style="width:32px;"> [Cirkelbåge](Draft_Arc/sv.md): Ritar en cirkelbåge med hjälp av centrum, radie, startvinkel och slutvinkel
-   <img alt="" src=images/Draft_Ellipse.png  style="width:32px;"> [Ellipse](Draft_Ellipse/sv.md): Draws an ellipse from two corner points
-   <img alt="" src=images/Draft_Polygon.png  style="width:32px;"> [Polygon](Draft_Polygon/sv.md): Ritar en regelbunden polygon med center och en radie
-   <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> [Rektangel](Draft_Rectangle/sv.md): Ritar en rektangel från 2 motsatta punkter (hörnen)
-   <img alt="" src=images/Draft_Text.png  style="width:32px;"> [Text](Draft_Text/sv.md): Ritar en text annotering med flera rader
-   <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> [Dimension](Draft_Dimension/sv.md): Ritar en måttsättning
-   <img alt="" src=images/Draft_BSpline.png  style="width:32px;"> [BSpline](Draft_BSpline/sv.md): Ritar en B-Spline från en serie med punkter
-   <img alt="" src=images/Draft_Point.png  style="width:32px;"> [Point](Draft_Point/sv.md): Inserts a point object
-   <img alt="" src=images/Draft_ShapeString.png  style="width:32px;"> [ShapeString](Draft_ShapeString/sv.md): The ShapeString tool inserts a compound shape representing a text string at a given point in the current document
-   <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> [Facebinder](Draft_Facebinder/sv.md): Creates a new object from selected faces on existing objects
-   <img alt="" src=images/Draft_BezCurve.png  style="width:32px;"> [Bezier Curve](Draft_BezCurve/sv.md): Draws a Bezier curve from a series of points
-   <img alt="" src=images/Draft_Label.png  style="width:32px;"> [Label](Draft_Label/sv.md): Places a label with an arrow pointing to a selected element {{Version/sv|0.17}}

## Annotation objects 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): draws a multi-line text annotation.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): draws a dimension annotation.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): places a label with an arrow pointing to a selected element.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): opens an editor to change the annotation style of these objects. <small>(v0.19)</small> 

### Förändra objekt 

Detta är verktyg för att förändra existerande objekt. De arbetar med valda objekt, men om inget objekt är valt, så ombes du att välja ett.

Many operation tools (move, rotate, array, etc.) also work on solid objects ([Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), [Arch](Arch_Workbench.md), etc.).

-   <img alt="" src=images/Draft_Move.png  style="width:32px;"> [Flytta](Draft_Move/sv.md): Flyttar objekt från en plats till en annan
-   <img alt="" src=images/Draft_Rotate.png  style="width:32px;"> [Rotera](Draft_Rotate/sv.md): Roterar objekt från en startvinkel till en slutvinkel
-   <img alt="" src=images/Draft_Offset.png  style="width:32px;"> [Offset](Draft_Offset/sv.md): Flyttar ett objekts segment ett visst avstånd
-   <img alt="" src=images/Draft_Trimex.png  style="width:32px;"> [Trimma/förläng (Trimex)](Draft_Trimex/sv.md): Trimmar eller förlänger ett objekt
-   <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> [Uppgradera](Draft_Upgrade/sv.md): Förenar objekt till ett objekt med högre nivå
-   <img alt="" src=images/Draft_Downgrade.png  style="width:32px;"> [Nedgradera](Draft_Downgrade/sv.md): Splittrar objekt till enklare objekt
-   <img alt="" src=images/Draft_Scale.png  style="width:32px;"> [Skala](Draft_Scale/sv.md): Skalar valda objekt runt en baspunkt
-   <img alt="" src=images/Draft_PutOnSheet.png  style="width:32px;"> [Ritning](Draft_Drawing/sv.md): Skriver valda objekt till ett [Ritningsark](Drawing_Workbench/sv.md)
-   <img alt="" src=images/Draft_Edit.png  style="width:32px;"> [Redigera](Draft_Edit/sv.md): Redigerar ett valt objekt
-   <img alt="" src=images/Draft_WireToBSpline.png  style="width:32px;"> [Wire to BSpline](Draft_WireToBSpline/sv.md): Converts a wire to a BSpline and vice-versa
-   <img alt="" src=images/Draft_AddPoint.png  style="width:32px;"> [Add point](Draft_AddPoint/sv.md): Adds a point to a wire or BSpline
-   <img alt="" src=images/Draft_DelPoint.png  style="width:32px;"> [Delete point](Draft_DelPoint/sv.md): Delete a point from a wire or BSpline
-   <img alt="" src=images/Draft_Shape2DView.png  style="width:32px;"> [Shape 2D View](Draft_Shape2DView/sv.md): Creates a 2D object which is a flattened 2D view of another 3D object
-   <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch/sv.md): Converts a Draft object to Sketch and vice-versa
-   <img alt="" src=images/Draft_Array.png  style="width:32px;"> [Array](Draft_Array/sv.md): Creates a polar or rectangular array from selected objects
-   <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> [Path Array](Draft_PathArray/sv.md): Creates an array of objects by placing the copies along a path
-   <img alt="" src=images/Draft_Clone.png  style="width:32px;"> [Clone](Draft_Clone/sv.md): Clones the selected objects
-   <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Mirror](Draft_Mirror/sv.md): Mirrors the selected objects
-   <img alt="" src=images/Draft_Stretch.png  style="width:32px;"> [Stretch](Draft_Stretch/sv.md): Stretches the selected objects {{Version/sv|0.17}}

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

## Draft utility tools toolbar 

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

### Gemensamt beteende 

!!FUZZY!!

-   [Snäpp](Draft_Snap/sv.md): tillåter dig att placera nya punkter på speciella platser på existerande objekt

-   [Begränsning](Draft_Constrain/sv.md): Tillåter att nya punkter placeras horisontellt eller vertikalt i relation till tidigare punkter

-   [Arbeta med manuella koordinater](Draft_Coordinates/sv.md): tillåter att du matar in koordinaterna manuellt istället för att klicka på skärmen

-   Kopiering: Alla ändringsverktyg kan antingen ändra de valda objekten eller skapa en förändrad kopiaav dem. Genom att trycka på **ALT** tangenten medan verktyget används kommer att skapa en kopia

-   [Konstruktionsläge](Draft_ToggleConstructionMode/sv.md): Tillåter dig att skilja viss geometri åt från resten, för att lätt kunna stänga på/av

-   [Arbetsplan](Draft_SelectPlane/sv.md): Alla skisskommandon kan användas på valfritt plani i 3D rymden. Det gällande arbetsplanet kan konfigureras på ett lätt sätt

-   Alla nyligen skapade objekt kommer att anta gällande Rit [färg och bredd](Draft_Linestyle/sv.md)

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

## Preferences

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferences](Draft_Preferences.md): general preferences for the working plane and the drawing tools.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): preferences available for importing from and exporting to different file formats.

### Import & export 

Detta är funktioner för att öppna, importera eller exportera andra filformat. Öppna kommet att öppna ett nytt dokument med filens innehåll, medan importera kommer att lägga till filinnehållet till det nuvarande dokumentet. Exportera kommer att spara de valda objekten till en fil. Om inget är valt, så kommer alla objekt att exporteras. Var uppmärksam på att eftersom tanken med Ritmodulen är att arbeta med 2d objekt, så fokuserar dessa importerare endast på 2d objekt, och, fastän DXF och OCA formaten stödjer objektdefinitioner i 3D rymden (objekt är inte nödvändigtvis platta), så kommer de inte att importera volymetriska objekt som nät, 3D ytor, etc, utan snarare linjer, cirklar, text eller flata former. För närvarande så stöds följande filformat:

-   [Autodesk .DXF](Draft_DXF/sv.md): Importerar och exporterar DXF filer som har skapats med andra CAD applikationer

-   [SVG (som geometri)](Draft_SVG/sv.md): Importerar och exporterar SVG filer som har skapats med vektorbaserade ritapplikationer

-   [Open Cad format .OCA](Draft_OCA/sv.md): Importerar och exporterar OCA/GCAD files, ett potentiellt nytt [öppet CAD filformat](http://groups.google.com/group/open_cad_format)

-   [Airfoil Data Format .DAT](Draft_DAT.md) Importerar DAT filer som beskriver [Vingprofiler](http://www.ae.illinois.edu/m-selig/ads/coord_database.html)

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

### API

Se [Skiss API](Draft_API/sv.md) sidan för en komplett beskrivning av Skissfunktionerna som du kan använda i skript och makron

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

### Tutorials

-   [Draft tutorial](Draft_tutorial/sv.md)
-   [Draft tutorial Outdated](Draft_tutorial_Outdated/sv.md)


{{docnav/sv|Raytracing_Workbench/sv|Robot_Workbench/sv}}


 

[Category:Workbenches](Category:Workbenches.md)
