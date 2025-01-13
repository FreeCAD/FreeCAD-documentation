# <img alt="Symbol des Arbeitsbereichs Draft" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/de






## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> **Draft** ist in erster Linie auf die Erstellung und Änderung von 2D-Objekten in FreeCAD ausgerichtet. Er ist jedoch nicht auf die XY-Ebene des globalen Koordinatensystems begrenzt. Seine Objekte können eine beliebige Ausrichtung und Position im 3D-Raum haben, und einige Draft-Objekte können entweder planar oder nicht-planar sein.

Draft-Objekte können für allgemeines Zeichnen verwendet werden, ähnlich dem, was mit Inkscape oder AutoCAD erstellt werden kann. Sie können aber auch die Grundlage für die Erstellung von 3D-Objekten in anderen Arbeitsbereichen bilden. Ein [Draft-Linienzug](Draft_Wire/de.md) kann den Pfad einer [Arch-Wand](Arch_Wall/de.md) definieren, ein [Draft-Vieleck](Draft_Polygon/de.md) kann mit [Part-Extrudieren](Part_Extrude/de.md) extrudiert werden, usw. Viele der [Draft-Änderungswerkzeuge](#Verändern.md) können auch auf 2D- und 3D-Objekte angewendet werden, die mit anderen Arbeitsbereichen erstellt wurden. Man kann z.B. eine [Skizze](Sketcher_Workbench/de.md) [verschieben](Draft_Move/de.md) oder eine [rechtwinklige Draft-Anordnung](Draft_OrthoArray/de.md) aus einem [Part](Part_Workbench/de.md)-Objekt erstellen.

Der Arbeitsbereich Draft enthält auch Werkzeuge zum Festlegen einer [Arbeitsebene](Draft_SelectPlane/de.md), eines [Rasters](Draft_Snap_Grid/de.md) und eines [Einrastsystems](Draft_Snap/de.md), zum präzisen Positionieren von Geometrie.

Wenn das Hauptziel die Erstellung komplexer 2D-Zeichnungen und [DXF](DXF/de.md)-Dateien ist und keine 3D-Modelle benötigt werden, ist FreeCAD möglicherweise nicht die richtige Wahl. Stattdessen sollte man eine spezielle (Software-)Anwendung für technisches Zeichnen in Betracht ziehen, wie [LibreCAD](https://de.wikipedia.org/wiki/LibreCAD) oder [QCad](https://de.wikipedia.org/wiki/QCad).

![](images/Draft_Workbench_Example.png ) 
*Das Bild zeigt das [Raster](Draft_Snap_Grid/de.md), das an der XY-Ebene ausgerichtet ist.<br>
Links, in weiß, mehrere planare Objekte.<br>
Rechts ein nicht-planarer [Draft-Linienzug](Draft_Wire/de.md), der als Pfadobjekt einer [Draft-Pfad-Anordnung](Draft_PathArray/de.md) verwendet wird.*



## Zeichnen

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linie](Draft_Line/de.md): erstellt eine gerade Linie.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Linienzug](Draft_Wire/de.md): erstellt einen Linienzug (auch Polylinie oder Draht genannt), eine Folge von mehreren miteinander verbundenen Linienabschnitten.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Verrundung](Draft_Fillet/de.md): erstellt eine Verrundung (eine abgerundete Ecke) oder eine Fase (eine gerade Kante) zwischen zwei [Draft-Linien](Draft_Line/de.md).

-   <img alt="" src=images/Draft_Arc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Bogenwerkzeuge:

  - <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Bogen](Draft_Arc/de.md): erstellt einen Kreisbogen aus einem Mittelpunkt, einem Radius, einem Startwinkel und einem Öffnungswinkel.

  - <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Bogen durch 3 Punkte](Draft_Arc_3Points/de.md): erstellt einen Kreisbogen aus drei Punkten, die seinen Umfang festlegen.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Kreis](Draft_Circle/de.md): erstellt einen Kreis aus Mittelpunkt und Radius.

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/de.md): erstellt eine Ellipse aus zwei Punkten, die ein Rechteck definieren, in das die Ellipse hineinpasst.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rechteck](Draft_Rectangle/de.md): erstellt ein Rechteck aus zwei Punkten.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Vieleck](Draft_Polygon/de.md): erstellt ein regelmäßiges Vieleck aus Mittelpunkt und Radius.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline/de.md): erstellt eine B-Spline-Kurve aus mehreren Punkten.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Bézier-Werkzeuge:

  - <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Kubische Bézierkurve](Draft_CubicBezCurve/de.md): erstellt eine Bézierkurve dritten Grades.

  - <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézierkurve](Draft_BezCurve/de.md): erstellt eine Bézierkurve aus mehreren Punkten.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/de.md): erstellt einen einfachen Punkt.

-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Flächenbinder](Draft_Facebinder/de.md): erstellt ein Oberflächenobjekt aus ausgewählten Flächen.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Textform](Draft_ShapeString/de.md): erstellt eine Verbundform, die eine Textzeichenfolge darstellt.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Schraffur](Draft_Hatch/de.md): erstellt eine Schraffur auf den ebenen Flächen eines ausgewählten Objekts.



## Beschriften

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text/de.md): erstellt einen mehrzeiligen Text an einer bestimmten Stelle.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Maß](Draft_Dimension/de.md): erstellt ein Längenmaß, ein Radienmaß oder ein Winkelmaß.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Hinweis](Draft_Label/de.md): erstellt einen mehrzeiligen Text an einer zweiteiligen Hinweislinie mit Pfeilspitze.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Beschriftungsstile\...](Draft_AnnotationStyleEditor/de.md): erlaubt Stile zu definieren, die die visuellen Eigenschaften von beschriftungsähnlichen Objekten beeinflussen.



## Verändern

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Verschieben](Draft_Move/de.md): verschiebt oder kopiert ausgewählte Objekte von einem Punkt zu einem anderen.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Drehen](Draft_Rotate/de.md): dreht oder kopiert ausgewählte Objekte, einem gegebenen Winkel entsprechend, um einen Drehpunkt herum.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skalieren](Draft_Scale/de.md): skaliert oder kopiert ausgewählte Objekte von einem Basispunkt aus.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Spiegeln](Draft_Mirror/de.md): erstellt gespiegelte Kopien von ausgewählten Objekten.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Versatz](Draft_Offset/de.md): versetzt jedes Teilstück eines ausgewählten Objekts um einen gegebenen Abstand oder erstellt eine versetzte Kopie des ausgewählten Objekts.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trimex](Draft_Trimex/de.md): beschneidet oder verlängert (trims or extends) ein ausgewähltes Objekt.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Strecken](Draft_Stretch/de.md): streckt Objekte durch Verschieben ausgewählter Punkte.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Klonen](Draft_Clone/de.md): erstellt verknüpfte Kopien, Klone, von ausgewählten Objekten.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Anordnungswerkzeuge:

  - <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [RechtwinkligeAnordnung](Draft_OrthoArray/de.md): erstellt eine rechtwinklige Anordnung aus einem ausgewählten Objekt. Wahlweise kann eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array) erstellt werden.

  - <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polare Anordnung](Draft_PolarArray/de.md): erstellt eine Anordnung aus einem ausgewählten Objekt, indem Kopien entlang eines Kreisumfangs positioniert werden. Wahlweise kann eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array) erstellt werden.

  - <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Kreisanordnung](Draft_CircularArray/de.md): erstellt eine Anordnung aus einem ausgewählten Objekt, indem Kopien an konzentrischen Kreisumfängen entlang positioniert werden. Wahlweise kann eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array) erstellt werden.

  - <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path array](Draft_PathArray/de.md): erstellt eine Anordnung aus einem ausgewählten Objekt, indem Kopien entlang eines Pfades positioniert werden.

  - <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [PfadVerknüpfungsanordnung](Draft_PathLinkArray/de.md): wie vorher, erstellt aber eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array) anstatt einer normalen Anordnung.

  - <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Punkt-Anordnung](Draft_PointArray/de.md): erstellt eine Anordnung aus einem ausgewählten Objekt, indem Kopien an den Punkten eines Punktverbundes positioniert werden.

  - <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [PunktVerknüpfungsanordnung](Draft_PointLinkArray/de.md): wie vorher, erstellt aber eine Verknüpfungsanordnung ([Link](App_Link/de.md)-Array) anstatt einer normalen Anordnung.

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Bearbeiten](Draft_Edit/de.md): setzt die ausgewählten Objekte in den Draft-Bearbeitungsmodus. In diesem Modus können die Eigenschaften graphisch bearbeitet werden.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Unterement hervorheben](Draft_SubelementHighlight/de.md): hebt ausgewählte Objekte oder die Basisobjekte der ausgewählten Objekte zeitweilig hervor.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Verbinden](Draft_Join/de.md): verbindet [Draft-Linien](Draft_Line/de.md) und [Draft-Linienzüge](Draft_Wire/de.md) zu einem einzigen Linienzug.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Teilen](Draft_Split/de.md): teilt eine [Draft-Linie](Draft_Line/de.md) oder einen [Draft-Linienzug](Draft_Wire/de.md) an einem bestimmten Punkt oder an einer bestimmten Kante.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Hochstufen](Draft_Upgrade/de.md): stuft ausgewählte Objekte hoch.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Zurückstufen](Draft_Downgrade/de.md): stuft ausgewählte Objekte zurück.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Linienzug zu B-spline](Draft_WireToBSpline/de.md): wandelt [Draft-Linienzüge](Draft_Wire/de.md) in [Draft-B-Splines](Draft_BSpline/de.md) und zurück.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Zeichnung zu Skizze](Draft_Draft2Sketch/de.md): wandelt Draft-Objekte in [Sketcher-Skizzen](Sketcher_NewSketch/de.md) und zurück.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Neigung festlegen](Draft_Slope/de.md): neigt ausgewählte [Draft-Linien](Draft_Line/de.md) oder [Draft-Linienzüge](Draft_Wire/de.md), indem die Werte der Z-Koordinaten aller Punkte nach dem ersten erhöht oder verringert werden.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Maß umkehren](Draft_FlipDimension/de.md): dreht den Maßtext ausgewählter [Draft-Maße](Draft_Dimension/de.md) um 180° um die Maßlinie herum.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Form2DAnsicht](Draft_Shape2DView/de.md): erstellt 2D-Projektionen von ausgewählten Objekten.



## Draft Fach 

Das [Draft Fach](Draft_Tray.md) ermöglicht die Auswahl einer Arbeitsebene, Stileinstellungen festzulegen, den Konstruktionsmodus umzuschalten und das Festlegen eines aktiven Layers oder einer Gruppe.

![](images/Draft_tray_default.png )

-   ![](images/Draft_tray_button_plane.png ) [Ebene auswählen](Draft_SelectPlane/de.md): legt die aktuelle Draft-Arbeitsebene fest. Auch im Menü verfügbar: **Dienstprogramme → <img src="images/Draft_SelectPlane.svg" width=16px> Ebene auswählen**.

-   ![](images/Draft_tray_button_style.png ) [Stil festlegen](Draft_SetStyle/de.md): setzt den Standard Stil für neue Objekte. Auch verfügbar im Menü: **Draft → Dienstprogramme → <img src="images/Draft_SetStyle.svg" width=16px> Stil festlegen**.

-   ![](images/Draft_tray_button_construction.png ) [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off. Also available in the menu: **Draft → Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode**.

-   ![](images/Draft_tray_button_layer.png ) [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [BIM](BIM_Workbench.md) object.



## Draft-Widget Beschriftungsmaßstab 

Mit dem [Draft-Widget Beschriftungsmaßstab](Draft_annotation_scale_widget/de.md) kann der Maßstab der Draft-Beschriftungen festgelegt werden.

![](images/Draft_annotation_scale_widget_button.png )



## Draft-Widget Einrasten 

Das [Draft-Widget Einrasten](Draft_snap_widget.md) kann als Alternative zur [Symbolleiste Draft-Einrasten](#Symbolleiste_Draft_Einrasten.md) dienen.

![](images/Draft_snap_widget_button.png )



## Symbolleiste Draft-Einrasten 

Die Symbolleiste Draft-Einrasten erlaubt das Auswählen der aktiven Einrast-Option. Die zu den aktiven Optionen gehörenden Schaltflächen bleiben niedergedrückt. Für allgemeine Informationen zum Einrasten siehe: [Draft Einrasten](Draft_Snap/de.md)

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [EinrastenSperren](Draft_Snap_Lock/de.md): aktiviert oder deaktiviert das Einrasten global.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [EinrastenAufEndpunkt](Draft_Snap_Endpoint/de.md): rastet auf Endpunkten von Kanten ein.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [EinrastenAufMittelpunkt](Draft_Snap_Midpoint/de.md): rastet auf Mittelpunkten von Kanten ein.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [EinrastenAufZentrum](Draft_Snap_Center/de.md): Rastet auf Mittelpunkten von Flächen oder kreisförmigen Kanten ein sowie auf den Punkten der {{PropertyData/de|Placement}} von [Draft-Arbeitsebenen-Proxies](Draft_WorkingPlaneProxy/de.md) und [Arch-Gebäudeteilen](Arch_BuildingPart/de.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [EinrastenAufWinkel](Draft_Snap_Angle/de.md): rastet auf bestimmten Hauptpunkten von kreisförmigen Kanten ein; auf Vielfachen von 30° und 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [EinrastenAufSchnittpunkt](Draft_Snap_Intersection/de.md): rastet auf den Schnittpunkt zweier Kanten ein.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [EinrastenSenkrecht](Draft_Snap_Perpendicular/de.md): rastet auf senkrechten Punkten auf Flächen ein ({{Version/de|0.21}}) und auf Kanten.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [EinrastenAufVerlängerung](Draft_Snap_Extension/de.md): rastet auf einer virtuellen Geraden ein, die über die Endpunkte gerader Kanten hinaus verläuft.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [EinrastenParallel](Draft_Snap_Parallel/de.md): rastet auf einer virtuellen Geraden parallel zu einer geraden Kante ein.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [EinrastenSpezial](Draft_Snap_Special/de.md): rastet auf Punkten ein, die durch das Objekt bestimmt werden.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [EinrastenInDerNähe](Draft_Snap_Near/de.md): rastet auf dem am nächsten liegenden Punkt einer Fläche oder Kante ein.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [EinrastenOrtho](Draft_Snap_Ortho/de.md): rastet auf virtuellen Geraden ein, die durch den vorherigen Punkt verläuft, unter einem Winkel, der ein Vielfaches von 45° ist.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [EinrastenAufRaster](Draft_Snap_Grid/de.md): rastet auf den Schnittstellen von Rasterlinien ein.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [EinrastenAufArbeitsebene](Draft_Snap_WorkingPlane/de.md): projiziert Einrastpunkte auf die aktuelle [Arbeitsebene](Draft_SelectPlane/de.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [EinrastenAufMaße](Draft_Snap_Dimensions/de.md): zeigt die temporären X- und Y-Maße an.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [RasterUmschalten](Draft_ToggleGrid/de.md): ändert die Sichtbarkeit des Rasters.



## Symbolleiste Draft-Hilfswerkzeuge 

-   <img alt="" src=images/Draft_LayerManager.svg  style="width:32px;"> [Layer verwalten\...](Draft_LayerManager/de.md): ermöglicht die Verwaltung der Layer in einem Dokument. {{Version/de|0.21}}

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> [BenannteGruppeHinzufügen](Draft_AddNamedGroup/de.md): erstellt eine benannte [Std Gruppe](Std_Group/de.md) und fügt ausgewählte Objekte dieser Gruppe hinzu.

Der Befehl <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> [ZurGruppeHinzufügen\...](Draft_AddToGroup/de.md): verschiebt Objekte in eine [Std Gruppe](Std_Group/de.md). Er kann auch Objekte aus einer Gruppe entfernen.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [GruppeWählen](Draft_SelectGroup/de.md): wählt den Inhalt von [Std Gruppen](Std_Group/de.md) oder gruppenartigen [BIM](BIM_Workbench/de.md)-Objekten aus.

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to construction group](Draft_AddConstruction.md): moves objects to the [Draft construction group](Draft_ToggleConstructionMode.md).

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle normal/wireframe display](Draft_ToggleDisplayMode.md): switches the **Display Mode** property of selected objects between {{Value|Flat Lines}} and {{Value|Wireframe}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Create working plane proxy](Draft_WorkingPlaneProxy.md): creates a working plane proxy to save the current [Draft working plane](Draft_SelectPlane.md).



## Zusätzliche Werkzeuge 

Das Menü **Draft → Dienstprogramme** enthält mehrere Werkzeuge. Die meisten davon können auch über Symbolleisten oder das [Draft-Tray](Draft_Tray/de.md) erreicht werden und wurden schon weiter oben erwähnt. Für die folgenden Werkzeuge it dies nicht der Fall:

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Aktuellen Stil anwenden](Draft_ApplyStyle/de.md): wendet die aktuellen Stileinstellungen auf die ausgewählten Objekte an.

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a [Draft Layer](Draft_Layer.md).

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Show snap toolbar](Draft_ShowSnapBar.md): shows the [Draft snap toolbar](#Draft_snap_toolbar.md).



## Zusätzliche Funktionen 

-   [Arbeitsebene](Draft_SelectPlane/de.md): die Ebene in der [3D-Ansicht](3D_view/de.md), in der neue Draft-Objekte erstellt werden.
-   [Einrasten](Draft_Snap/de.md): wählt exakte geometrische Punkte auf vorhandenen Objekten aus bzw. durch sie festgelegte Punkte oder legt sie auf dem Raster fest.
-   [Beschränken](Draft_Constrain/de.md): für jeden nachfolgenden Punkt kann die Bewegung des Mauszeigers auf die X-, Y- oder Z-Richtung eingeschränkt werden.
-   [Konstruktionsmodus](Draft_ToggleConstructionMode/de.md): platziert neue Draft-Objekte in einer eigenen Gruppe, was das Ausblenden oder Löschen erleichtert.
-   [Muster](Draft_Pattern/de.md): Draft-Objekte mit einer {{PropertyData/de|Make Face}} können ein SVG-Muster anstelle einer einfarbigen Fläche anzeigen.



## Kontextmenü der Baumansicht 

Die folgenden zusätzlichen Optionen stehen nur im Kontextmenü der [Baumansicht](Tree_view/de.md) zur Verfügung:

### Default options 

For most Draft objects the following option is available:

-   Edit: edits the object. Depending on the object type either [Draft Edit](Draft_Edit.md) or a dedicated edit solution is used. <small>(v0.21)</small> 

If there is an active document the context menu contains an additional sub-menu:

-   Utilities: a subset of the tools available in the main Draft Utilities menu.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Merge layer duplicates](Draft_Layer#Layer_container_options.md): merges all layers with the same base label.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer#Layer_container_options.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): activates the selected layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Text options 

For a [Draft Text](Draft_Text.md) and a [Draft Label](Draft_Label.md) that contains one or more hyperlinks, to a local or remote file or an URL, this additional option is available:

-   Open hyperlinks: the hyperlinks are opened in the appropriate application (as defined by the OS). There is a warning in the case of multiple hyperlinks. <small>(v1.0)</small> 

### Wire options 

For a [Draft Line](Draft_Line.md) and a [Draft Wire](Draft_Wire.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten: flattens the wire on the current [Draft working plane](Draft_SelectPlane.md). This option does not work properly in {{VersionMinus|0.19}}.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Context_menu.md): updates the **View Data** property of the working plane proxy with the current [3D view](3D_view.md) camera settings.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Context_menu.md): updates the **Visibility Map** property of the working plane proxy with the current visibility state of objects in the document.



## Kontextmenü der 3D-Ansicht 

Die folgenden zusätzlichen Optionen stehen nur im Kontextmenü der [3D-Ansicht](3D_view/de.md) zur Verfügung:

### Default options 

If there is an active document the context menu contains one additional sub-menu:

-   Utilities: a subset of the tools available in the main Draft Utilities menu.

### Text options 

See [above](#Text_options.md).



## Veraltete Werkzeuge 

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Anordnung](Draft_Array/de.md): Erstellt eine rechtwinklige Anordnung aus einem Ausgewählten Objekt. Die erstellte Anordnung kann in eine [PolareAnordnung](Draft_PolarArray/de.md) oder eine [circular array](Draft_CircularArray.md) gewandelt werden, indem ihre {{PropertyData/de|Array Type}} geändert wird. Nicht mehr enthalten in {{VersionPlus/de|0.21}}.

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): inserts views of selected objects into a [drawing](Drawing_Workbench.md) page. Not available in <small>(v0.21)</small> .

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): switches continue mode on or off. Not available in <small>(v1.0)</small> .



## Einstellungen

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Einstellungen](Draft_Preferences/de.md): allgemeine Einstellungen für den Arbeitsbereich Draft.

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): preferences available for importing from and exporting to different file formats.



## Dateiformate

Der Arbeitsbereich Draft stellt FreeCAD Import- und Export-Hilfsprogramme für verschiedene Dateiformate zur Verfügung. Diese werden von den Befehlen [Std Import](Std_Import/de.md) und [Std Export](Std_Export/de.md) verwendet.

-   [Autodesk .DXF](Draft_DXF/de.md): Importiert und exportiert [Drawing-Exchange-Format](http://en.wikipedia.org/wiki/AutoCAD_DXF)-Dateien
-   [Autodesk .DWG](Draft_DXF/de.md): Importiert und exportiert DWG Dateien mit einem externen DWG-Konverter. Siehe auch [FreeCAD- und DWG-Import](FreeCAD_and_DWG_Import/de.md).
-   [Scalable Vector Graphics .SVG](Draft_SVG/de.md): Importiert und exportiert [Skalierbare Vektorgrafiken](https://de.wikipedia.org/wiki/Scalable_Vector_Graphics).
-   [Open Cad Format .OCA](Draft_OCA/de.md): Importiert und exportiert [OCA/GCAD](http://groups.google.com/group/open_cad_format)-Dateien.
-   [Tragflächenprofil Daten Format .DAT](Draft_DAT/de.md): Importiert DAT Dateien, die Tragflächenprofile (engl.: Airfoil profiles) beschreiben.



## Einheitentests

Siehe auch: Arbeitsbereich [Test Framework](Testing/de.md).

Um die Einheitentests des Arbeitsbereichs auszuführen, gibt man Folgendes im Terminal des Betriebssystems ein:


```python
freecad -t TestDraft
```



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Der Arbeitsbereich enthält ein Modul zur Erstellung von Mustern aller Objekte in einem neuen Dokument.

Verwende dies, um zu testen, ob alle Objekte korrekt erstellt werden:


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Der Einblick in den Code dieses Moduls kann helfen, um die Programmierschnittstelle zu verstehen.



## Tutorien

-   [Draft Tutorium](Draft_tutorial/de.md)
-   [Draft FormZeichenkette Tutorium](Draft_ShapeString_tutorial.md)



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Draft](Category_Draft.md) > Draft Workbench/de
