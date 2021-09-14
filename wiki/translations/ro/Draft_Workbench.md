# Draft Workbench/ro




 

<img alt="Draft workbench icon" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduction

## Introducere

Atelierul Draft vă permite desenarea rapidă a unor obiecte bidimensionale în documentul curent şi oferă mai multe unelte pentru modificarea lor ulterioară. De asemenea, oferă instrumente pentru a defini un plan de lucru, o rețea și un sistem de ancorare pentru a controla precis poziția geometriei dvs.

Obiectele create 2D pot fi folosite pentru redactarea generală într-un mod similar cu Inkscape sau Autocad. Aceste forme 2D pot fi de asemenea utilizate ca componente de bază ale obiectelor 3D create cu alte ateliere de lucru, de exemplu, [ Part](Part_Workbench.md) și [Arch Workbench](Arch_Workbench.md). Este, de asemenea, posibilă transformarea de obiecte Draft în [ Sketches](Sketcher_Workbench.md), ceea ce înseamnă că formele pot fi de asemenea utilizate cu [PartDesign Workbench](PartDesign_Workbench.md) pentru crearea de corpuri solide.

FreeCAD este în primul rând o aplicație de modelare 3D și, prin urmare, instrumentele sale 2D nu sunt la fel de avansate ca în cazul altor programe de desenare. Dacă obiectivul dvs. principal este producerea de desene complexe 2D și fișiere [DXF](DXF.md) și nu aveți nevoie de modelare 3D, vă recomandăm să luați în considerare un program software dedicat pentru redactarea tehnică, cum ar fi [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), TurboCad, ș.a.m.d.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Desenarea obiectelor 

Aceste unelte se folosesc la crearea obiectelor.

-   <img alt="" src=images/Draft_Line.png  style="width:32px;"> [Linie din 2 puncte](Draft_Line/ro.md): Trasează un segment de linie definit prin 2 puncte.
-   <img alt="" src=images/Draft_Wire.png  style="width:32px;"> [Fir/Poliline](Draft_Wire/ro.md): Desenează o linie formată din mai multe segmente.
-   <img alt="" src=images/Draft_Circle.png  style="width:32px;"> [Cerc](Draft_Circle/ro.md): Trasează un cerc definit prin centru şi rază.
-   <img alt="" src=images/Draft_Arc.png  style="width:32px;"> [Arc](Draft_Arc/ro.md): Desenează un arc cu definit prin centru, rază, unghiul iniţial şi cel final.
-   <img alt="" src=images/Draft_Ellipse.png  style="width:32px;"> [Ellipse](Draft_Ellipse/ro.md): Desenează o elipsă definită prin două puncte, definind colțuri diagonale ale unei casete rectangulare în care se va încadra elipsa
-   <img alt="" src=images/Draft_Polygon.png  style="width:32px;"> [Poligon](Draft_Polygon/ro.md): Desenează un poligon regulat definit prin centrul, rază și numărul de laturi.
-   <img alt="" src=images/Draft_Rectangle.png  style="width:32px;"> [Rectangle](Draft_Rectangle/ro.md): Trasează un dreptunghi folosind ca repere capetele diagonalei.
-   <img alt="" src=images/Draft_Text.png  style="width:32px;"> [Text](Draft_Text/ro.md): Adaugă o casetă text cu mai multe linii de scriere.
-   <img alt="" src=images/Draft_Dimension.png  style="width:32px;"> [Dimensiuni](Draft_Dimension/ro.md): Introduce o dimensiune de cotare.
-   <img alt="" src=images/Draft_BSpline.png  style="width:32px;"> [BSpline](Draft_BSpline/ro.md): Trasează o curbă (B-Spline) folosind o serie de puncte.
-   <img alt="" src=images/Draft_Point.png  style="width:32px;"> [Punct](Draft_Point/ro.md): Inserează un punct.
-   <img alt="" src=images/Draft_ShapeString.png  style="width:32px;"> [ShapeString](Draft_ShapeString/ro.md): Instrumentul ShapeString introduce o formă compusă reprezentând un șir de text într-un punct dat în documentul curent
-   <img alt="" src=images/Draft_Facebinder.png  style="width:32px;"> [Facebinder](Draft_Facebinder/ro.md):Creează un obiect nou din fațetele selectate pe obiectele existente
-   <img alt="" src=images/Draft_BezCurve.png  style="width:32px;"> [Bezier Curve](Draft_BezCurve/ro.md): Desenează o curbă Bezier definită printr-o serie de puncte
-   <img alt="" src=images/Draft_Label.png  style="width:32px;"> [Label](Draft_Label/ro.md): Plasează o etichetă cu o săgeată care indică un element selectat {{Version/ro | 0.17}}

## Annotation objects 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): draws a multi-line text annotation.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): draws a dimension annotation.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): places a label with an arrow pointing to a selected element.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): opens an editor to change the annotation style of these objects. <small>(v0.19)</small> 

## Modificarea obiectelor 

Aceste unelte modifică obiectele existente. Ţinta lor sunt obiectele selectate, iar dacă nu exista nici un obiect selectat veţi fi invitat să selectaţi unul.

Multe instrumente de operare (mutare, rotire, matrice etc.) lucrează și pe obiecte solide ([Part](Part_Workbench.md), [PartDesign](PartDesign_Workbench.md), [Arch](Arch_Workbench.md), etc.).

-   <img alt="" src=images/Draft_Move.png  style="width:32px;"> [Muta](Draft_Move/ro.md): Mută obiectele dintr-o locaţie în alta.
-   <img alt="" src=images/Draft_Rotate.png  style="width:32px;"> [Rotire](Draft_Rotate/ro.md): Roteşte obiectele de la un unghi iniţial la un unghi final.
-   <img alt="" src=images/Draft_Offset.png  style="width:32px;"> [Expandare](Draft_Offset/ro.md): Mută segmentele unui obiect la o anumită distanţă constantă.
-   <img alt="" src=images/Draft_Trimex.png  style="width:32px;"> [Taie/Extinde (Trimex)](Draft_Trimex/ro.md): Taie sau extinde un obiect.
-   <img alt="" src=images/Draft_Upgrade.png  style="width:32px;"> [Unire](Draft_Upgrade/ro.md): Uneşte obiectele intr-un singur obiect mai complex.
-   <img alt="" src=images/Draft_Downgrade.png  style="width:32px;"> [Explodare](Draft_Downgrade/ro.md): Sparge un obiect complex în părţi (obiecte mai simple).
-   <img alt="" src=images/Draft_Scale.png  style="width:32px;"> [Scalare](Draft_Scale/ro.md): Scalează obiectele selectate în jurul punctului de bază.
-   <img alt="" src=images/Draft_PutOnSheet.png  style="width:32px;"> [Desenare](Draft_Drawing/ro.md): Transferă şi transcrie obiectele selectate pe o [foaie de desen](Drawing_Workbench/ro.md).
-   <img alt="" src=images/Draft_Edit.png  style="width:32px;"> [Editare](Draft_Edit/ro.md): Editează obiectul selectat.
-   <img alt="" src=images/Draft_WireToBSpline.png  style="width:32px;"> [Polilinie in BSpline](Draft_WireToBSpline/ro.md): Converteşte o polilinie într-o curbă (BSpline) şi viceversa.
-   <img alt="" src=images/Draft_AddPoint.png  style="width:32px;"> [Adauga punct](Draft_AddPoint/ro.md): Inserează un punct intr-o polilinie sau curbă (BSpline).
-   <img alt="" src=images/Draft_DelPoint.png  style="width:32px;"> [Sterge point](Draft_DelPoint/ro.md): Şterge un punct dintr-o polilinie sau curbă (BSpline).
-   <img alt="" src=images/Draft_Shape2DView.png  style="width:32px;"> [Vizualizare 2D a formei](Draft_Shape2DView/ro.md): Creează un obiect 2D care reprezintă proiecţia unui obiect 3D.
-   <img alt="" src=images/Draft_Draft2Sketch.png  style="width:32px;"> [Ciorna in schita](Draft_Draft2Sketch/ro.md): Converteşte un obiect 2D (Draft) în schiţă şi viceversa.
-   <img alt="" src=images/Draft_Array.png  style="width:32px;"> [Multimi](Draft_Array/ro.md): Creează o matrice de simetrie polară sau rectangulară multiplicând obiectele selectate.
-   <img alt="" src=images/Draft_PathArray.png  style="width:32px;"> [Path Array](Draft_PathArray/ro.md): Creează o serie de obiecte prin plasarea copiilor de-a lungul unei traiectorii
-   <img alt="" src=images/Draft_Clone.png  style="width:32px;"> [Clonare](Draft_Clone/ro.md): Clonează obiectele selectate.
-   <img alt="" src=images/Draft_Mirror.png  style="width:32px;"> [Mirror](Draft_Mirror/ro.md): Simetrizează obiectele selectate
-   <img alt="" src=images/Draft_Stretch.png  style="width:32px;"> [Stretch](Draft_Stretch/ro.md): Extinde obiectele selectate{{Version/ro|0.17}}

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

## Utilitare

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a Layer in the current document, to which objects can be added to control object visibility and color. It replaces Draft VisGroup. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Working Plane Proxy](Draft_WorkingPlaneProxy.md): create a proxy object to store the current [Working Plane](Draft_SelectPlane.md) position.
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle display mode](Draft_ToggleDisplayMode.md): switches the display mode of selected objects between \"Flat Lines\" and \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Add to group](Draft_AddToGroup.md): quickly adds selected objects to an existing [Std Group](Std_Group.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group contents](Draft_SelectGroup.md): selects the contents of a selected [Std Group](Std_Group.md) or [Draft Layer](Draft_Layer.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): add selected objects to the Construction group.
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

## Additional tools 

O serie de instrumente suplimentare sunt oferite de un meniu **Draft → Utilities**, sau cu clic-dreapta în meniul contextual, în funcţie de obiectele selectate:

-   <img alt="" src=images/Draft_SelectPlane.png  style="width:32px;"> [Setează planului de lucru](Draft_SelectPlane/ro.md): Setează un plan de lucru din vizualizarea standard sau pe faţa selectată.
-   <img alt="" src=images/Draft_FinishLine.png  style="width:32px;"> [Termină linia](Draft_FinishLine/ro.md): Încheie desenarea poliliniei sau curbei curente [Draft Wire](Draft_Wire.md) or [Draft BSpline](Draft_BSpline.md), fără a o închide.
-   <img alt="" src=images/Draft_CloseLine.png  style="width:32px;"> [Închide linia](Draft_CloseLine/ro.md): Termină desenarea poliliniei sau curbei curente [Draft Wire](Draft_Wire.md) or [Draft BSpline](Draft_BSpline.md) şi o închide.
-   <img alt="" src=images/Draft_UndoLine.png  style="width:32px;"> [Undo linie](Draft_UndoLine/ro.md): Elimină ultimul segment al poliliniei.
-   <img alt="" src=images/Draft_ToggleConstructionMode.png  style="width:32px;"> [Comută modul Construcţie](Draft_ToggleConstructionMode/ro.md): Comută modul Construcţie în ciornă (activ/inactiv).
-   <img alt="" src=images/Draft_ToggleContinueMode.png  style="width:32px;"> [Comută modul continuu](Draft_ToggleContinueMode/ro.md): Comută modul continuu (activ/inactiv).
-   <img alt="" src=images/Draft_ApplyStyle.png  style="width:32px;"> [Aplica stil](Draft_Apply/ro.md): Aplică stilul şi culoarea curente obiectelor selectate.
-   <img alt="" src=images/Draft_ToggleDisplayMode.png  style="width:32px;"> [Comută modul de afişare](Draft_ToggleDisplayMode/ro.md): Comută modul de afişare pentru obiectele afişate între \"linii plane\" şi \"reţele\".
-   <img alt="" src=images/Draft_AddToGroup.png  style="width:32px;"> [Adaugă la grup](Draft_AddToGroup/ro.md): Adaugă rapid obiectele selectate la un grup existent [Std Group](Std_Group.md) or [Draft VisGroup](Draft_VisGroup.md).
-   <img alt="" src=images/Draft_SelectGroup.png  style="width:32px;"> [Selectează grupul](Draft_SelectGroup/ro.md): Selectează elementele componente ale unui grup ales.
-   <img alt="" src=images/Draft_ToggleSnap.png  style="width:32px;"> [Comută ancorele](Draft_ToggleSnap/ro.md): Comută [ancorarea obiectelor](Draft_Snap/ro.md) (activă/inactivă).
-   <img alt="" src=images/Draft_ToggleGrid.png  style="width:32px;"> [Comuta grila](Draft_ToggleGrid/ro.md): Comută grila (activă/inactivă).
-   <img alt="" src=images/Draft_ShowSnapBar.png  style="width:32px;"> [Arată bara de ancore](Draft_ShowSnapBar/ro.md): Afişează sau ascunde bara de [ancorare](Draft_Snap/ro.md).
-   <img alt="" src=images/Draft_Heal.png  style="width:32px;"> [Heal](Draft_Heal.md): Rezolvă problemele din fișierele foarte vechi
-   <img alt="" src=images/Draft_FlipDimension.png  style="width:32px;"> [Flip Dimension](Draft_FlipDimension/ro.md): Întoarce orientarea textului dimensiunii [dimension](Draft_Dimension/ro.md)
-   <img alt="" src=images/Draft_VisGroup.png  style="width:32px;"> [VisGroup](Draft_VisGroup/ro.md): Creează un VisGroup in documentul curent
-   <img alt="" src=images/Draft_Slope.png  style="width:32px;"> [Slope](Draft_Slope/ro.md): Schimbă panta Liniilor sau firelor selectate {{Version/ro|0.17}}
-   <img alt="" src=images/Draft_AutoGroup.png  style="width:32px;"> [AutoGroup](Draft_AutoGroup/ro.md): Automat plasează noi obiecte în grupul dat {{Version/ro|0.17}}
-   <img alt="" src=images/Draft_SetWorkingPlaneProxy.png  style="width:32px;"> [Set Working Plane Proxy](Draft_SetWorkingPlaneProxy.md): Adaugă un obiect proxy în documentul de salvat la [Working Plane](Draft_SelectPlane.md) position <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_ToggleConstructionMode.png  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): Adaugă obiectele selectate la grupul Construcții <small>(v0.17)</small> 

## Caracteristici suplimentare 

-   [Coordinates](Draft_Coordinates.md):

introduceți coordonatele în loc să faceți clic pe vizualizarea 3D pentru a defini un nou punct.

-   [Constraining](Draft_Constrain.md):

limitați pointerul la mișcări orizontale sau verticale în raport cu un punct anterior.

-   [Snapping](Draft_Snap.md):

plasați noi puncte pe locuri speciale pe obiecte existente sau pe grilă.

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

## Preferințe

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferences](Draft_Preferences.md): Preferințe disponibile în Atelierul Draft Workbench.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import-Export Preferences](Import_Export_Preference.md): preferințele disponibile pentru importul și exportul în diferite formate de fișiere.

## Formate de fişiere 

Atelierul Desen 2D (Draft) înzestrează FreeCAD cu importul şi exportul următoarele formate de fişiere:

-   [Autodesk .DXF](Draft_DXF.md): Importă şi exportă fişiere [Drawing Exchange Format](http://en.wikipedia.org/wiki/AutoCAD_DXF), create cu aplicaţii CAD bidimensionale (2D)., a se vedea și [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md).
-   [Autodesk .DWG](Draft_DXF.md): imports and exports DWG files via the DXF importer, when the [ODA Converter](Extra_python_modules#ODA_Converter_(previously_Teigha_Converter).md) utility is installed. See also [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md).
-   [SVG (geometrice)](Draft_SVG.md): Importă şi exportă fişiere [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics), create cu programe de desenare vectorială.
-   [Open Cad format .OCA](Draft_OCA.md): Importă şi exportă fişiere OCA/GCAD, un potenţial [format nou al fişierelor open CAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT.md): Importă fişiere DAT care descriu [profile Airfoil](http://www.ae.illinois.edu/m-selig/ads/coord_database.html).

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

## Script

Instrumentele de proiectare pot fi utilizate în [macros](macros.md) și din consola [Python](Python.md) utilizând [API-ul de proiect](API-ul_de_proiect.md).

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

## Îndrumătoare

-   [Îndrumător de folosire a Atelierului Desen 2D](Draft_tutorial/ro.md)
-   [Vechiul îndrumător de folosire a AtelieruluiDesen2D](Draft_tutorial_Outdated/ro.md)
-   [Îndrumător modelare 3D a fonturilor cu ShapeString](Draft_ShapeString_tutorial/ro.md)





 

[Category:Workbenches](Category:Workbenches.md)
