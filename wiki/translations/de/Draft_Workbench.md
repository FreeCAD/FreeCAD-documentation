
{{Page in progress}}

 

<img alt="Entwurf Arbeitsbereich Symbol" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Einführung

Der <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Arbeitsbereich Entwurf](Draft_Module/de.md) erlaubt dir das Zeichnen einfacher 2D Objekte und bietet verschiedene Werkzeuge, um sie anschließend zu ändern. Es bietet auch Werkzeuge zur Festlegung einer Bearbeitungsebene, eines Rasters und eines Objektfangsystems, um die Position deiner Geometrie präzise zu steuern.

Die erzeugten 2D Objekte können ähnlich wie mit Inkscape oder Autocad für allgemeine Zeichnungserstellung verwendet werden. Diese 2D Formen können auch als Basiskomponenten von 3D Objekten verwendet werden, die mit anderen Arbeitsbereichen erstellt wurden, z.B. dem <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Part](Part_Workbench/de.md) und <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Arch Arbeitsbereichen](Arch_Workbench/de.md). Konvertierung von Entwurfsobjekten nach <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Skizzen](Sketcher_Workbench/de.md) ist auch möglich, d.h. die Formen können auch mit der <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) für die Erzeugung von Volumenkörpern verwendet werden.

FreeCAD ist in erster Linie eine 3D Modellierungsanwendung, und daher sind seine 2D Werkzeuge nicht so fortschrittlich wie in anderen Zeichenprogrammen. Wenn dein primäres Ziel die Erstellung komplexer 2D Zeichnungen und [DXF](DXF/de.md) Dateien ist und du keine 3D Modellierung benötigst, solltest du ein spezielles Softwareprogramm für technisches Zeichnen wie [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), oder andere in Betracht ziehen.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Zeichnen von Objekten {#zeichnen_von_objekten}

Dies sind Werkzeuge zum Erstellen von Objekten.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Linie](Draft_Line/de.md): Zeichnet ein Liniensegment zwischen zwei Punkten.
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polylinie](Draft_Wire/de.md): Zeichnet eine Linie, die aus mehreren Liniensegmenten besteht (Polylinie).
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Verrundung](Draft_Fillet/de.md): Zeichnet eine Verrundung (abgerundete Ecke) oder eine Fase (gerade Linie) zwischen zwei einfachen [Linien](Draft_Line/de.md). {{Version/de|0.19}}
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Bogen](Draft_Arc/de.md): zeichnet ein Bogensegment aus Mittelpunkt, Radius, Startwinkel und Endwinkel.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Bogen 3Punkte](Draft_Arc_3Points/de.md): zeichnet ein Kreisbogensegment aus drei Punkten, die sich am Umfang befinden. {{Version/de|0.19}}
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Kreis](Draft_Circle/de.md): zeichnet einen Kreis aus Mitte und Radius.
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/de.md): Zeichnet eine Ellipse aus zwei Eckpunkten
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rechteck](Draft_Rectangle/de.md): Zeichnet ein Rechteck aus zwei Eckpunkten.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygon](Draft_Polygon/de.md): zeichnet ein regelmäßiges Polygon aus Mittelpunkt, Radius und Anzahl der Seiten.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [BSpline](Draft_BSpline/de.md): zeichnet eine B-Spline aus einer Reihe von Punkten.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Kubische Bézierkurve](Draft_CubicBezCurve.md): zeichnet eine Bézierkurve dritten Grades, indem zwei Punkte gezogen werden. {{Version/de|0.19}}
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Bézierkurve](Draft_BezCurve/de.md): zeichnet eine Bézierkurve aus einer Reihe von Punkten.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Punkt](Draft_Point/de.md): Fügt ein Punktobjekt ein.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Flächenbinder](Draft_Facebinder/de.md): erstellt ein neues Objekt aus ausgewählten Flächen auf vorhandenen Objekten.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [FormZeichenfolge](Draft_ShapeString/de.md): fügt eine Verbundform, die eine Textzeichenfolge darstellt, an einem bestimmten Punkt ein.

## Anmerkungsobjekte

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text/de.md): zeichnet eine mehrzeilige Textanmerkung.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Abmessung](Draft_Dimension/de.md): zeichnet eine Bemaßungsanmerkung.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Schild](Draft_Label/de.md): platziert ein Schild mit einem Pfeil, der auf ein ausgewähltes Element zeigt. {{Version/de|0.17}}
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Anmerkungsstileditor](Draft_AnnotationStyleEditor/de.md): öffnet einen Editor, um den Annotationsstil dieser Objekte zu ändern. {{Version/de|0.19}}

## Objekte ändern {#objekte_ändern}

Dies sind Werkzeuge zur Modifikation bestehender Objekte. Sie arbeiten mit ausgewählten Objekten, aber wenn kein Objekt ausgewählt ist, werden Sie aufgefordert, eines auszuwählen.

Viele Bearbeitungswerkzeuge (Verschieben, Drehen, Anordnung, usw.) funktionieren auch mit Festkörperobjekten ([Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md), [Arch](Arch_Workbench/de.md), usw.).

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Verschieben](Draft_Move/de.md): Bewegt Objekte von einem Punkt zu einem anderen
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Drehen](Draft_Rotate/de.md): Rotiert Objekte von einem Ausgangswinkel zu einem Endwinkel
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Skalieren](Draft_Scale/de.md): Dimensioniert ein ausgewähltes Objekt in Bezug zu einem bestimmten Punkt
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Spiegeln](Draft_Mirror/de.md): Spiegelt die ausgewählten Objekte
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Versetzen](Draft_Offset/de.md): Bewegt Segmente eines Objekts um einen bestimmten Wert
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Stutzen/Strecken (Trimex)](Draft_Trimex/de.md): stutzt oder dehnt ein Objekt
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Dehnen](Draft_Stretch/de.md): Dehnt die ausgewählten Objekte {{Version/de|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Klonen](Draft_Clone/de.md): Klont die ausgewählten Objekte
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Anordnungswerkzeuge
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Orthogonal Anordnung](Draft_OrthoArray/de.md): erzeugt eine orthogonale Anordnung aus dem ausgewählten Objekt. Es kann auch [Anwendungsverknüpfung](App_Link/de.md) Kopien erzeugen. {{Version/de|0.19}}
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polare Anordnung](Draft_PolarArray/de.md): erzeugt eine Anordnung in einem polaren Muster, d.h. Austragen mit einem Winkel.Es kann auch [Anwendungsverknüpfung](App_Link/de.md) Kopien erzeugen. {{Version/de|0.19}}
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Zirkulare Anordnung](Draft_CircularArray/de.md):erzeugt eine Anordnung in einem kreisförmigen Muster, d.h. ausgehend von einem Zentrum, das sich radial nach außen bewegt. Es kann auch [Anwendungsverknüpfung](App_Link/de.md) Kopien erstellen. {{Version/de|0.19}}
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Pfad Anordnung](Draft_PathArray/de.md): Erzeugt eine Anordnung von Objekten, indem die Kopien entlang eines Pfades platziert werden.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Pfad VerbindeAnordnung](Draft_PathLinkArray.md): wie <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Pfad Anordnung](Draft_PathArray/de.md), erstellt jedoch [Anwendungsverknüpfung](App_Link/de.md) anstelle von regulären Kopien. {{Version/de|0.19}}
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Punkt VerknüpfeAnordnung](Draft_PointLinkArray/de.md): wie <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Punkt Anordnung](Draft_PointArray/de.md), erstellt jedoch [Anwendungsverknüpfung](App_Link/de.md) anstelle von regulären Kopien. {{Version/de|0.19}}

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Bearbeiten](Draft_Edit/de.md): Verändert ein ausgewähltes Objekt.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Unterelement markieren](Draft_SubelementHighlight/de.md): ruft einen Bearbeitungsmodus auf, in dem verschiedene Objekte bearbeitet werden können. {{Version/de|0.19}}

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Verbinden](Draft_Join/de.md): verbindet Linien zu einem einzigen Draht. {{Version/de|0.18}}
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Teilen](Draft_Split/de.md): teilt einen Draht an einem Punkt in zwei Teile. {{Version/de|0.18}}
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Hochstufen](Draft_Upgrade/de.md): Vereinigt mehrere Objekte in ein Objekt der nächst höheren Ebene
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Herabstufen](Draft_Downgrade/de.md): Teilt ein Objekt in einzelne der nächst niedrigeren Ebene

-   <img alt="" src=images/Draft_WireToBSpline.png  style="width:32px;"> [Draht zu BSpline](Draft_WireToBSpline/de.md): Konvertiert einen Draht in ein BSpline und umgekehrt
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Entwurf zu Skizze](Draft_Draft2Sketch/de.md): konvertiert ein Draft Objekt in eine [Arbeitsbereich Skizze](Sketcher_Workbench/de.md) Skizze und umgekehrt.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Neigung](Draft_Slope/de.md): ändert die Höhenneigung der aktuell ausgewählten [Entwurf Linie](Draft_Line/de.md) or [Entwurf Draht](Draft_Wire/de.md). {{Version/de|0.17}}
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Abmessung kippen](Draft_FlipDimension/de.md): dreht die Ausrichtung des Textes eines [Entwurf Abmessung](Draft_Dimension/de.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Form in 2D Ansicht](Draft_Shape2DView/de.md): Erstellt ein 2D Objekt, das eine abgeflachte 2D Ansicht eines anderen 3D Objekts ist.

## Entwurf Ablage {#entwurf_ablage}

Die Entwurf Fach Werkzeugleiste erscheint beim Start des Arbeitsbereichs und ermöglicht die Auswahl der Arbeitsebene zusammen mit einigen visuellen Eigenschaften wie Linienfarbe, Formfarbe, Textgröße, Linienbreite und automatische Gruppe.

![](images/Draft_tray_default.png )

Its tools are also available in the {{MenuCommand|Draft → Utilities}} menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Arbeitsebene](Draft_SelectPlane/de.md): legt eine Arbeitsebene aus einer Standardansicht oder einer ausgewählten Fläche fest.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Konstruktionsmodus](Draft_ToggleConstructionMode/de.md): schaltet den Entwurf Konstruktionsmodus ein oder aus.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Stileinstellungen](Draft_ApplyStyle/de.md): Lege Standardstile für neue Objekte fest und wende den aktuellen Stil und die aktuelle Farbe auf ausgewählte Objekte an.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGruppe](Draft_AutoGroup/de.md): automatisch neue Objekte in einer gegebenen <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Std Gruppe](Std_Group/de.md), <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Entwurf Schicht](Draft_Layer/de.md), oder eines der gruppenartigen Objekte der [Arch Arbeitsbereich](Arch_Workbench/de.md), wie <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arch GebäudeTeil](Arch_BuildingPart/de.md) platzieren.


{{Version/de|0.17}}

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget {#draft_annotation_scale_widget}

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget {#draft_snap_widget}

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Entwurf Fang Werkzeugleiste {#entwurf_fang_werkzeugleiste}

Die [Entwurf Fang](Draft_Snap/de.md) Werkzeugleiste ermöglicht die Auswahl des aktuellen Fangmodus. Seine Schaltfläche gedrückt halten, wenn ein Modus aktiv ist.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Umschalten Fang](Draft_Snap_Lock.md): Schaltet [Objekt Fang](Draft_Snap/de.md) global ein oder aus.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Endpunkt](Draft_Snap_Endpoint/de.md): fängt an den Endpunkten von Linien-, Bogen- und Splinesegmenten.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Mittelpunkt](Draft_Snap_Midpoint/de.md): fängt am Mittelpunkt von Linien- und Bogensegmenten.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Zentrum](Draft_Snap_Center/de.md): fängt am Zentrumspunkt von Kreisen, Bögen und Flächen, [ArbeitsEbenen proxies](Draft_WorkingPlaneProxy/de.md) und [Gebäude Teile](Arch_BuildingPart/de.md)
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Winkel](Draft_Snap_Angle/de.md): fängt an den speziellen Himmelsrichtungen von Kreisen und Bögen, bei 45° und 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Schnittpunkt](Draft_Snap_Intersection/de.md): fängt auf dem Schnittpunkt zweier Linien- oder Bogensegmente. Fahre mit der Maus über die beiden gewünschten Objekte, um deren Schnittpunktfang zu aktivieren.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Senkrecht](Draft_Snap_Perpendicular/de.md): auf Linien- und Bogensegmenten, fängt senkrecht zum letzten Punkt.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Erweiterung](Draft_Snap_Extension/de.md): fängt auf einer imaginären Linie, die sich über die Endpunkte von Liniensegmenten hinaus erstreckt. Fahre mit der Maus über das gewünschte Objekt, um den Erweiterungsfang zu aktivieren.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallel](Draft_Snap_Parallel/de.md): fängt auf einer imaginären Linie parallel zu einem Liniensegment. Fahre mit der Maus über das gewünschte Objekt, um dessen Parallelfang zu aktivieren.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Spezial](Draft_Snap_Special/de.md): fängt spezielle Punkte ein, die durch das Objekt definiert sind. {{Version/de|0.17}}
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Nächster](Draft_Snap_Near/de.md): fängt den nächstgelegenen Punkt oder die nächstgelegene Kante auf dem nächstgelegenen Objekt.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortho](Draft_Snap_Ortho/de.md): fängt an imaginäre Linien, die den letzten Punkt kreuzen und sich bei 0°, 45° und 90° erstrecken.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Umschalten Gitter](Draft_Snap_Grid/de.md): Schaltet die Sichtbarkeit des Gitters ein oder aus.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Arbeitsebene](Draft_Snap_WorkingPlane/de.md): Platziert den gefangenen Punkt immer auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md), auch wenn du an einem Punkt außerhalb dieser Arbeitsebene fängst.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Bemaßungen](Draft_Snap_Dimensions/de.md): zeigt temporäre X und Y Bemaßungen während des Fangens an.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Umschalten Gitter](Draft_ToggleGrid/de.md): schaltet die Sichtbarkeit des Gitters ein oder aus.

## Entwurf Werkzeugleiste Hilfswerkzeuge {#entwurf_werkzeugleiste_hilfswerkzeuge}

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Schicht](Draft_Layer/de.md): erstellt eine Schicht im aktuellen Dokument, zu der Objekte hinzugefügt werden können, um die Sichtbarkeit und Farbe der Objekte zu steuern. Sie ersetzt [SichtGruppe](Draft_VisGroup/de.md). {{Version/de|0.19}}
-   <img alt="" src=images/Draft_SetWorkingPlaneProxy.svg  style="width:32px;"> [Arbeitsebenen Proxy](Draft_WorkingPlaneProxy/de.md): Erstelle ein Proxyobjekt zum speichern der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) Position. {{Version/de|0.17}}
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Anzeigemodus umschalten](Draft_ToggleDisplayMode/de.md): schaltet den Anzeigemodus der ausgewählten Objekte zwischen \"Flache Linien\" und \"Drahtgitter\" um.
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Zur Gruppe hinzufügen](Draft_AddToGroup/de.md): fügt ausgewählte Objekte schnell zu einer bestehenden [Std Gruppe](Std_Group/de.md) oder [Entwurf SichtGruppe](Draft_VisGroup/de.md) hinzu..
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Gruppeninhalt auswählen](Draft_SelectGroup/de.md): wählt den Inhalt einer ausgewählten [Std Gruppe](Std_Group/de.md) oder [Entwurf SichtGruppe](Draft_VisGroup/de.md) aus.
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Zur Konstruktionsgruppe hinzufügen](Draft_AddConstruction/de.md): ausgewählte Objekte zur Konstruktionsgruppe hinzufügen. {{Version/de|0.17}}
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heilen](Draft_Heal/de.md): heilt problematische Entwurf Objekte, aus sehr alten Dateien.

## Zusätzliche Werkzeuge {#zusätzliche_werkzeuge}

Weitere Werkzeuge die, abhängig vom ausgewählten Objekt, über das Menü {{MenuCommand|Entwurf → Hilfsprogramme}} oder über das Rechtsklick Kontextmenü, je nach ausgewähltem Objekt.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Kontinuierlichen Modus umschalten](Draft_ToggleContinueMode/de.md): schaltet den Entwurfsfortsetzungsmodus ein oder aus.
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Zeige Fangleiste](Draft_ShowSnapBar/de.md): zeigt oder blendet die [Entwurf Fang](Draft_Snap/de.md) Werkzeugleiste ein oder aus.

## Zusätzliche Funktionen {#zusätzliche_funktionen}

-   [Koordinaten](Draft_Coordinates/de.md): Koordinaten eingeben, anstatt auf die 3D-Ansicht zu klicken, um einen neuen Punkt zu definieren.
-   [Beschränken](Draft_Constrain/de.md): den Zeiger auf horizontale oder vertikale Bewegungen in Bezug auf einen vorherigen Punkt beschränken.
-   [Fangen](Draft_Snap/de.md): neue Punkte an speziellen Stellen auf bestehenden Objekten oder auf dem Gitter platzieren.
-   [Kopiermodus](Draft_Copying/de.md): Alle Modifikationswerkzeuge können entweder die ausgewählten Objekte modifizieren oder eine modifizierte Kopie davon erstellen.
    Durch Drücken und Halten von **Alt** während das Objekt modifiziert wird, z.B. während das Objekt geändert wird, z.B. verschoben oder gedreht, erstellt eine Kopie, wenn die Taste losgelassen wird.
-   [Konstruktionsmodus](Draft_ToggleConstructionMode/de.md): Erlaubt dir, Geometrien getrennt vom Rest zu erstellen, indem man sie einfach ein- und ausschalten.
-   [Arbeitsebene](Draft_SelectPlane/de.md): Erlaubt dir, eine Oberfläche zu wählen, auf welcher du deine Formen baust.

## Baumansicht Kontextmenü {#baumansicht_kontextmenü}

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Auswahlmöglichkeiten

If there is a selection the context menu contains one additional sub-menu:

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

### Wire options {#wire_options}

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options {#layer_container_options}

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options {#layer_options}

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options {#working_plane_proxy_options}

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D Ansicht Kontextmenü {#d_ansicht_kontextmenü}

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options {#no_selection_options}

If there is no selection the context menu contains one additional sub-menu:

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

### Selection options {#selection_options}

If there is a selection the context menu contains two additional sub-menus:

-    {{MenuCommand|Draft}}: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

## Veraltete Werkzeuge {#veraltete_werkzeuge}

Diese Werkzeuge sind veraltet, aber weiterhin verfügbar.

-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [VisGruppe](Draft_VisGroup/de.md): erzeugt eine VisGruppe im aktuellen Dokument. Diese wurde ersetzt durch <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Schicht](Draft_Layer/de.md). {{Obsolete/de|0.19}}
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Linie beenden](Draft_FinishLine/de.md): beendet die Zeichnung des aktuellen [Entwurf Draht](Draft_Wire/de.md) oder [Entwurf BSpline](Draft_BSpline/de.md), ohne sie zu schließen. {{Obsolete/de|0.19}}
-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Linie schließen](Draft_CloseLine/de.md): beendet die Zeichnung des aktuellen [Entwurf Draht](Draft_Wire/de.md) oder [Entwurf BSpline](Draft_BSpline/de.md), und schließt ihn. {{Obsolete/de|0.19}}
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Linie rückgängig](Draft_UndoLine/de.md): macht das letzte Segment eines [Entwurf Draht](Draft_Wire/de.md) rückgängig. {{Obsolete/de|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Einstellungen

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Einstellungen](Draft_Preferences/de.md): allgemeine Einstellungen für die Arbeitsfläche und die Zeichenwerkzeuge.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Einstellungen](Import_Export_Preferences/de.md): Einstellungen für den Import von und Export in verschiedene Dateiformate.

## Dateiformate

Dies sind Funktionen zum Öffnen, Importieren oder Exportieren von anderen Dateiformaten. Das Öffnen wird ein neues Dokument mit dem Inhalt der Datei öffnen, während das Importieren den Dateiinhalt am gegenwärtigen Dokument anhängen wird. Exportieren wird die ausgewählten Objekte in einer Datei speichern. Wenn nichts ausgewählt ist, werden alle Objekte exportiert werden. Seien Sie sich bewusst, dass der Zweck des Draftmoduls ist, mit 2D Objekten zu arbeiten, daher konzentrieren sich jene Importroutinen nur auf 2D Objekte, und obwohl DXF und OCA Formate auch Objektdefinitionen im 3D Raum unterstützen (Objekte sind nicht notwendigerweise flach), werden sie volumetrische Objekte wie Polygonnetze, 3D Flächen, usw. nicht importieren, sondern eher Linien, Kreise, Texte oder flache Formen. Zurzeit unterstützte Dateiformate sind:

-   [Autodesk .DXF](Draft_DXF/de.md): Importiert und exportiert [Zeichnungstauschformat (drawing exchange format)](http://en.wikipedia.org/wiki/AutoCAD_DXF) Dateien, die mit 2D CAD Anwendungen erstellt wurden
-   [Autodesk .DWG](Draft_DXF/de.md): Importiert und exportiert DWG Dateien mit dem DXF Importeur, wenn der [ODA Konverter](Extra_python_modules/de.md) installiert ist. Siehe auch [FreeCAD und DWG Import](FreeCAD_and_DWG_Import/de.md).
-   [SVG](Draft_SVG/de.md): Importiert und exportiert [Skalierbare Vektorgrafiken](https://de.wikipedia.org/wiki/Scalable_Vector_Graphics), also Dateien, die mit Vektor Zeichenprogrammen erstellt wurden.
-   [Open Cad Format .OCA](Draft_OCA/de.md): Importiert und exportiert OCA/GCAD Dateien, ein potentiell neues, [offenes CAD Datei Format](http://groups.google.com/group/open_cad_format).
-   [Tragflächenprofil Daten Format .DAT](Draft_DAT/de.md): Importiert DAT Dateien, die [Tragflächenprofile](http://www.ae.illinois.edu/m-selig/ads/coord_database.html) (engl.: Airfoil profiles) beschreiben.

### Importeure installieren {#importeure_installieren}

-   [FreeCAD und DWG Import](FreeCAD_and_DWG_Import/de.md): Importiert und exportiert DWG Dateien
-   [FreeCAD und DXF Import](FreeCAD_and_DXF_Import/de.md): Importiert und exportiert DXF Dateien

## Einheitentests


**Siehe auch:**

[Test Arbeitsbereich](Test_Workbench.md).

Um die Einheitentests des Arbeitsbereichs auszuführen, führen Folgendes vom Betriebssystemterminal aus. 
```python
freecad -t TestDraft
```

## Skripten

Die Entwurfswerkzeuge können in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch die [Draft API](Draft_API/de.md) aufgerufen werden.

Der Arbeitsbereich enthält ein Modul zur Erstellung von Mustern aller Objekte in einem neuen Dokument. {{Version/de|0.19}}

Verwende dies, um zu testen, ob alle Objekte korrekt ausgegeben werden. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Der Einblick in den Code dieses Moduls ist nützlich, um zu verstehen, wie die Programmierschnittstelle zu verwenden ist. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Wobei `$INSTALLDIR` das Hauptverzeichnis ist, in dem die Software installiert wurde; unter Linux kann es beispielsweise `/usr/share/freecad` sein.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Testobjekte für den [Entwurf Arbeitsbereich](Draft_Workbench/de.md).*

## Tutorien

-   [Entwurf Tutorium](Draft_tutorial/de.md)
-   [Entwurf FormZeichenkette Tutorium](Draft_ShapeString_tutorial.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
