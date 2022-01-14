# <img alt="Entwurf Arbeitsbereich Symbol" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/de


{{TOCright}}

## Einführung

Die <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> **Arbeitsbereich Entwurf** ist in erster Linie auf die Erstellung und Änderung von 2D Objekten in FreeCAD ausgerichtet. Er ist jedoch nicht auf die XY Ebene des globalen Koordinatensystems begrenzt. Seine Objekte können eine beliebige Ausrichtung und Position im 3D Raum haben, und einige Entwurfsobjekte können entweder planar oder nicht-planar sein.

Entwurfsobjekte können für das allgemeine Entwerfen verwendet werden, ähnlich dem was mit Inkscape oder AutoCAD getan werden kann. Sie können aber auch die Grundlage für die Erstellung von 3D Objekten in anderen Arbeitsbereichen bilden. Ein [Entwurf Draht](Draft_Wire/de.md) kann den Pfad einer [Architektur Wand](Arch_Wall/de.md) definieren, ein [Entwurf Polygon](Draft_Polygon/de.md) kann mit [Part Extrudieren](Part_Extrude/de.md) extrudiert werden, usw. Viele der [Entwurfsmodifizierungswerkzeuge](#Modifikation.md) können auch auf 2D und 3D Objekte angewendet werden, die mit anderen Arbeitsbereichen erstellt wurden. Du kannst z.B. eine [Skizze](Sketcher_Workbench/de.md) [verschieben](Draft_Move/de.md) oder ein [Entwurf OrthoAnordnung](Draft_OrthoArray/de.md) aus einem [Part](Part_Workbench/de.md) Objekt erstellen.

Der Arbeitsbereich Entwurf bietet auch Werkzeuge zur Definition einer [Arbeitsebene](Draft_SelectPlane/de.md), eines [Gitters](Draft_Snap_Grid/de.md) und eines [Fangsystems](Draft_Snap/de.md), um die Position der Geometrie präzise zu steuern.

Wenn dein Hauptziel die Erstellung komplexer 2D-Zeichnungen und [DXF](DXF.md) Dateien ist und du keine 3D Modellierung benötigst, ist FreeCAD möglicherweise nicht die richtige Wahl für dich. Vielleicht möchtest du stattdessen ein spezielles Softwareprogramm für technisches Zeichnen in Betracht ziehen, wie [LibreCAD](https://de.wikipedia.org/wiki/LibreCAD) oder [QCad](https://de.wikipedia.org/wiki/QCad).

![](images/Draft_Workbench_Example.png ) 
*Das Bild zeigt das [Giter](Draft_Snap_Grid/de.md), das an der XY Ebene ausgerichtet ist.<br>
Links, in weiß, mehrere planare Objekte.<br>
Rechts ein nicht-planarer [Entwurf Draht](Draft_Wire/de.md), der als Pfadobjekt einer [Entwurf PfadAnordnung](Draft_PathArray/de.md) verwendet wird.*

## Entwerfen

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linie](Draft_Line/de.md): erzeugt eine gerade Linie.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polylinie](Draft_Wire/de.md): erzeugt eine Polylinie, eine Folge von mehreren miteinander verbundenen Liniensegmenten.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Verrundung](Draft_Fillet/de.md): erzeugt eine Verrundung, eine abgerundete Ecke, oder eine Fase, eine gerade Kante, zwischen zwei [Entwurf Linien](Draft_Line/de.md). {{Version/de|0.19}}

-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> Bogen Werkzeuge

:\* <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Bogen](Draft_Arc/de.md): erstellt einen Kreisbogen aus einem Zentrum, einem Radius, einem Startwinkel und einem Öffnungswinkel.

:\* <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Bogen durch 3 Punkte](Draft_Arc_3Points/de.md): erzeugt einen Kreisbogen aus drei Punkten, die seinen Umfang definieren. {{Version/de|0.19}}

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Kreis](Draft_Circle/de.md): erzeugt einen Kreis aus einem Zentrum und einem Radius.

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/de.md): erstellt eine Ellipse aus zwei Punkten, die ein Rechteck definieren, in das die Ellipse passen soll.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rechteck](Draft_Rectangle/de.md): erzeugt ein Rechteck aus zwei Punkten.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon/de.md): erzeugt ein regelmäßiges Polygon aus einem Zentrum und einem Radius.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline/de.md): erstellt eine B-Spline Kurve aus mehreren Punkten.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> Bézier Werkzeuge

:\* <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Kubische Bézierkurve](Draft_CubicBezCurve/de.md): erzeugt eine Bézierkurve dritten Grades. {{Version/de|0.19}}

:\* <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézierkurve](Draft_BezCurve/de.md): erstellt eine Bézierkurve aus mehreren Punkten.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/de.md): erzeugt einen einfachen Punkt.

-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Flächenbinder](Draft_Facebinder/de.md): erstellt ein Oberflächenobjekt aus ausgewählten Flächen.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [FormZeichenfolge](Draft_ShapeString/de.md): erstellt eine Verbundform, die eine Textzeichenfolge darstellt.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Hatch](Draft_Hatch.md): creates hatches on the planar faces of a selected object. <small>(v0.20)</small> 

## Anmerkung

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text/de.md): erstellt einen mehrzeiligen Text an einer bestimmten Stelle.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Bemaßung](Draft_Dimension/de.md): erzeugt eine lineare, radiale oder winklige Bemaßung.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Beschriftung](Draft_Label/de.md): erstellt einen mehrzeiligen Text mit einer 2-Segment Führungslinie und einem Pfeil.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Anmerkungssstile\...](Draft_AnnotationStyleEditor/de.md): erlaubt dir, Stile zu definieren, die die visuellen Eigenschaften von beschriftungsähnlichen Objekten beeinflussen. {{Version/de|0.19}}

## Änderung

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Move](Draft_Move.md): moves or copies selected objects from one point to another.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotate](Draft_Rotate.md): rotates or copies selected objects around a center point by a given angle.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): scales or copies selected objects around a base point.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Mirror](Draft_Mirror.md): creates mirrored copies from selected objects.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Offset](Draft_Offset.md): offsets each segment of a selected object over a given distance, or creates an offset copy of the selected object.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex.md): trims or extends a selected object.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Stretch](Draft_Stretch.md): stretches objects by moving selected points.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): creates linked copies, clones, of selected objects.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> Array tools

:\* <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Array](Draft_OrthoArray.md): creates an orthogonal array from a selected object. It can optionally create a [Link](App_Link.md) array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar array](Draft_PolarArray.md): creates an array from a selected object by placing copies along a circumference. It can optionally create a [Link](App_Link.md) array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Circular array](Draft_CircularArray.md): creates an array from a selected object by placing copies along concentric circumferences. It can optionally create a [Link](App_Link.md) array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path array](Draft_PathArray.md): creates an array from a selected object by placing copies along a path.

:\* <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path Link array](Draft_PathLinkArray.md): idem, but create a [Link](App_Link.md) array instead of a regular array. <small>(v0.19)</small> 

:\* <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array from a selected object by placing copies at the points from a point compound.

:\* <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Point Link array](Draft_PointLinkArray.md): idem, but create a [Link](App_Link.md) array instead of a regular array. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): puts selected objects in Draft Edit mode. In this mode the properties of objects can be edited graphically.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): temporarily highlights selected objects, or the base objects of selected objects.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): joins [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md) into a single wire.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): splits a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md) at a specified point or edge.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades selected objects.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades selected objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Wire to B-spline](Draft_WireToBSpline.md): converts [Draft Wires](Draft_Wire.md) to [Draft BSplines](Draft_BSpline.md) and vice versa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): converts [Draft](Draft_Workbench.md) objects to [Sketcher Sketches](Sketcher_NewSketch.md) and vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Set slope](Draft_Slope.md): slopes selected [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md) by increasing, or decreasing, the Z coordinate of all points after the first one.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip dimension](Draft_FlipDimension.md): rotates the dimension text of selected [Draft Dimensions](Draft_Dimension.md) 180° around the dimension line.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D view](Draft_Shape2DView.md): creates 2D projections from selected objects.

## Entwurf Ablage 

Die Entwurf Fach Werkzeugleiste erscheint beim Start des Arbeitsbereichs und ermöglicht die Auswahl der Arbeitsebene zusammen mit einigen visuellen Eigenschaften wie Linienfarbe, Formfarbe, Textgröße, Linienbreite und automatische Gruppe.

![](images/Draft_tray_default.png )

-   ![](images/Draft_tray_button_plane.png ) [Ebene wählen](Draft_SelectPlane/de.md): wählt die aktuelle Arbeitsebene des Entwurfs aus. Auch im Menü verfügbar: **Entwurf → Hilfsmittel → <img src="images/Draft_SelectPlane.svg" width=16px> Ebene wählen**.

-   ![](images/Draft_tray_button_style.png ) [Set style](Draft_SetStyle.md): sets the default style for new objects. Also available in the menu: **Draft → Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Set style**. <small>(v0.19)</small> 

-   ![](images/Draft_tray_button_construction.png ) [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off. Also available in the menu: **Draft → Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode**.

-   ![](images/Draft_tray_button_layer.png ) [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_Snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Entwurf Fang Werkzeugleiste 

Die Entwurf Fang Werkzeugleiste erlaubt das Auswählen der aktiven Fangoption. Die zu den aktiven Optionen gehörenden Schaltflächen bleiben niedergedrückt. Für allgemeine Informationen zum Fangen siehe: [Entwurf Fang](Draft_Snap/de.md)

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular point on edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces or edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at 0°, 45°, 90° and 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap WorkingPlane](Draft_Snap_WorkingPlane.md): projects the snap point onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

## Entwurf Werkzeugleiste Hilfswerkzeuge 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a [Draft Layer](Draft_Layer.md). <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> [Add a new named group](Draft_AddNamedGroup.md): creates a named [Std Group](Std_Group.md) and moves selected objects to that group. <small>(v0.20)</small> 

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Move to group\...](Draft_AddToGroup.md): moves objects to a [Std Group](Std_Group.md). It can also ungroup objects.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group](Draft_SelectGroup.md): selects the contents of [Std Groups](Std_Group.md) or group-like [Arch](Arch_Workbench.md) objects.

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md).

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle normal/wireframe display](Draft_ToggleDisplayMode.md): switches the **Display Mode** property of selected objects between {{Value|Flat Lines}} and {{Value|Wireframe}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Create working plane proxy](Draft_WorkingPlaneProxy.md): creates a working plane proxy to save the current [Draft working plane](Draft_SelectPlane.md).

## Zusätzliche Werkzeuge 

Weitere Werkzeuge die, abhängig vom ausgewählten Objekt, über das Menü **Entwurf → Hilfsprogramme** oder über das Rechtsklick Kontextmenü, je nach ausgewähltem Objekt.

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Apply current style](Draft_ApplyStyle.md): applies the current style settings to selected objects.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): switches continue mode on or off.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Show snap toolbar](Draft_ShowSnapBar.md): shows the [Draft Snap toolbar](#Draft_Snap_toolbar.md).

## Zusätzliche Funktionen 


<div class="mw-translate-fuzzy">

-   [Arbeitsebene](Draft_SelectPlane/de.md): die Ebene in der [3D Ansicht](3D_view/de.md), in der neue Entwurfsobjekte erstellt werden.
-   [Fangen](Draft_Snap/de.md): wählt exakte geometrische Punkte auf vorhandenen Objekten oder auf dem Gitter aus, die durch diese definiert sind.
-   [Beschränken](Draft_Constrain/de.md): für jeden nachfolgenden Punkt kannst du die Bewegung des Mauszeigers auf die X, Y oder Z Richtung beschränken.
-   [Konstruktionsmodus](Draft_ToggleConstructionMode/de.md): platziert neue Entwurfsobjekte in einer eigenen Gruppe, was das Ausblenden oder Löschen erleichtert.
-   [Muster](Draft_Pattern/de.md): Entwurfsobjekte mit einer **Make Face** Eigenschaft können ein Schraffurmuster anstelle einer einfarbigen Fläche anzeigen.


</div>

## Baumansicht Kontextmenü 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Default options 

If there is an active document the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Merge layer duplicates](Draft_Layer#Layer_container_options.md): merges all layers with the same base label. This does not work in FreeCAD version 0.19.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer#Layer_container_options.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): activates the selected layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Context_menu.md): updates the **View Data** property of the working plane proxy with the current [3D view](3D_view.md) camera settings.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Context_menu.md): updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.

## 3D Ansicht Kontextmenü 

The following additional options are available in the [3D view](3D_view.md) context menu:

### Default options 

If there is an active document the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

## Veraltete Werkzeuge 

Diese Werkzeuge sind veraltet, aber weiterhin verfügbar.

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): creates an orthogonal array from a selected object. The created array can be turned into a [polar array](Draft_PolarArray.md) or a [circular array](Draft_CircularArray.md) by changing its **Array Type** property. {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): inserts views of selected objects into a [drawing](Drawing_Workbench.md) page. {{Obsolete|0.17}}

## Einstellungen


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Einstellungen](Draft_Preferences/de.md): allgemeine Einstellungen für die Arbeitsfläche und die Zeichenwerkzeuge.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Einstellungen](Import_Export_Preferences/de.md): Einstellungen für den Import von und Export in verschiedene Dateiformate.


</div>

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): preferences available for importing from and exporting to different file formats.

## Dateiformate


<div class="mw-translate-fuzzy">

Dies sind Funktionen zum Öffnen, Importieren oder Exportieren von anderen Dateiformaten. Das Öffnen wird ein neues Dokument mit dem Inhalt der Datei öffnen, während das Importieren den Dateiinhalt am gegenwärtigen Dokument anhängen wird. Exportieren wird die ausgewählten Objekte in einer Datei speichern. Wenn nichts ausgewählt ist, werden alle Objekte exportiert werden. Seien Sie sich bewusst, dass der Zweck des Draftmoduls ist, mit 2D Objekten zu arbeiten, daher konzentrieren sich jene Importroutinen nur auf 2D Objekte, und obwohl DXF und OCA Formate auch Objektdefinitionen im 3D Raum unterstützen (Objekte sind nicht notwendigerweise flach), werden sie volumetrische Objekte wie Polygonnetze, 3D Flächen, usw. nicht importieren, sondern eher Linien, Kreise, Texte oder flache Formen. Zurzeit unterstützte Dateiformate sind:


</div>


<div class="mw-translate-fuzzy">

-   [Autodesk .DXF](Draft_DXF/de.md): Importiert und exportiert [Zeichnungstauschformat (drawing exchange format)](http://en.wikipedia.org/wiki/AutoCAD_DXF) Dateien, die mit 2D CAD Anwendungen erstellt wurden
-   [Autodesk .DWG](Draft_DXF/de.md): Importiert und exportiert DWG Dateien mit dem DXF Importeur, wenn der [ODA Konverter](Extra_python_modules/de.md) installiert ist. Siehe auch [FreeCAD und DWG Import](FreeCAD_and_DWG_Import/de.md).
-   [SVG](Draft_SVG/de.md): Importiert und exportiert [Skalierbare Vektorgrafiken](https://de.wikipedia.org/wiki/Scalable_Vector_Graphics), also Dateien, die mit Vektor Zeichenprogrammen erstellt wurden.
-   [Open Cad Format .OCA](Draft_OCA/de.md): Importiert und exportiert OCA/GCAD Dateien, ein potentiell neues, [offenes CAD Datei Format](http://groups.google.com/group/open_cad_format).
-   [Tragflächenprofil Daten Format .DAT](Draft_DAT/de.md): Importiert DAT Dateien, die [Tragflächenprofile](http://www.ae.illinois.edu/m-selig/ads/coord_database.html) (engl.: Airfoil profiles) beschreiben.


</div>

## Einheitentests


<div class="mw-translate-fuzzy">

Siehe auch: [Test Arbeitsbereich](Testing/de.md).


</div>


<div class="mw-translate-fuzzy">

Um die Einheitentests des Arbeitsbereichs auszuführen, führen Folgendes vom Betriebssystemterminal aus.


</div>


```python
freecad -t TestDraft
```

## Skripten


<div class="mw-translate-fuzzy">

Die Entwurfswerkzeuge können in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch die [Draft API](Draft_API/de.md) aufgerufen werden.


</div>

Der Arbeitsbereich enthält ein Modul zur Erstellung von Mustern aller Objekte in einem neuen Dokument. {{Version/de|0.19}}


<div class="mw-translate-fuzzy">

Verwende dies, um zu testen, ob alle Objekte korrekt ausgegeben werden.


</div>


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```


<div class="mw-translate-fuzzy">

Der Einblick in den Code dieses Moduls ist nützlich, um zu verstehen, wie die Programmierschnittstelle zu verwenden ist.


</div>

## Tutorials


<div class="mw-translate-fuzzy">

## Tutorien

-   [Entwurf Tutorium](Draft_tutorial/de.md)
-   [Entwurf FormZeichenkette Tutorium](Draft_ShapeString_tutorial.md)


</div>





 

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Draft Workbench/de
