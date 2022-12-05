# Draft Snap/de
{{TOCright}}

## Beschreibung


<div class="mw-translate-fuzzy">

Die <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereich](Draft_Workbench/de.md) Werkzeuge ermöglichen dir Punkte und Abstände zu greifen, durch klicken auf die [3D Ansicht](3D_view/de.md) mit dem Mauszeiger oder durch eingeben von Koordinaten im [Aufgabenbereich](Task_panel/de.md) des Werkzeugs.


</div>


<div class="mw-translate-fuzzy">

Das Fangen ist mit den meisten [Entwurf](Draft_Workbench/de.md) und [Architektur Arbeitsbereich](Arch_Workbench/de.md) Werkzeugen verfügbar.


</div>

![](images/Draft_Snap_Endpoint_example.png )


<div class="mw-translate-fuzzy">



*Linie gefangen senkrecht zu einer anderen Linie*


</div>

## Snap tools 

These tools are available in the Draft snap toolbar and in the [Draft snap widget](Draft_snap_widget.md).

Note that circular edges do not have to be full circles.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Fang umschalten](Draft_Snap_Lock/de.md): schaltet [Objektfang](Draft_Snap/de.md) global ein oder aus.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Endpunkt](Draft_Snap_Endpoint/de.md): fängt an den Endpunkten von Linien-, Bogen- und Splinesegmenten.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Mittenpunkt](Draft_Snap_Midpoint/de.md): fängt auf den Mittenpunkt von Linien- und Bogensegmenten.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Mittelpunkt](Draft_Snap_Center/de.md): fängt auf den Mittelpunkt von Bögen und Kreisen.
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Winkel](Draft_Snap_Angle/de.md): fängt an den speziellen Himmelsrichtungen von Kreisen und Bögen, bei 45° und 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Schnittpunkt](Draft_Snap_Intersection/de.md): fängt den Schnittpunkt von zwei Linien- oder Bogensegmenten. Fahre mit der Maus über die beiden gewünschten Objekte, um deren Schnittfang zu aktivieren.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Rechtwinklig](Draft_Snap_Perpendicular/de.md): auf Linien- und Bogensegmenten, fängt rechtwinklig zum letzten Punkt.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Erweiterung](Draft_Snap_Extension/de.md): fängt eine imaginäre Linie ein, die über die Endpunkte von Liniensegmenten hinausgeht. Fahre mit der Maus über das gewünschte Objekt, um den Erweiterungsfang zu aktivieren.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallel](Draft_Snap_Parallel/de.md): fängt auf einer imaginären Linie parallel zu einem Liniensegment. Fahre mit der Maus über das gewünschte Objekt, um den Parallelfang zu aktivieren.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Spezial](Draft_Snap_Special/de.md): fängt an speziellen, durch das Objekt definierten Punkten. <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Nächste](Draft_Snap_Near/de.md): fängt den nächstgelegenen Punkt oder die nächstgelegene Kante des Objekts ein.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Rechtwinklig](Draft_Snap_Ortho/de.md): fängt an imaginären Linien, die den letzten Punkt kreuzen und sich bei 0°, 45° und 90° ausdehnen.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Gitter](Draft_Snap_Grid/de.md): fängt an den Schnittpunkten der Gitterlinien, wenn das Gitter sichtbar ist.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Arbeitsebene](Draft_Snap_WorkingPlane/de.md): setzt den gefangenen Punkt immer auf die aktuelle [Arbeitsebene](Draft_SelectPlane/de.md), auch wenn du auf einen Punkt außerhalb dieser Arbeitsebene fängst.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Abmessungen](Draft_Snap_Dimensions/de.md): zeigt temporäre X- und Y-Dimensionen während des Fangvorgangs an.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Umschalten Gitter](Draft_Snap_Grid.md): schaltet die Sichtbarkeit des Gitters ein und aus.


</div>

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular points on faces (<small>(v1.0)</small> ) and edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces and edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at multiples of 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap WorkingPlane](Draft_Snap_WorkingPlane.md): projects snap points onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

## Erweitertes Fangen 


<div class="mw-translate-fuzzy">

-   Zusätzliche Fangplätze können durch die Kombination zweier Fangmethoden, wie [Entwurf Ortho](Draft_Snap_Ortho/de.md) und [Entwurf Erweiterung](Draft_Snap_Extension/de.md), erzielt werden, die dir einen Fangpunkt am Schnittpunkt ihrer imaginären Linien liefert.
-   Andere Fangpositionen können durch die Verwendung von [Entwurf Beschränken](Draft_Constrain/de.md) erreicht werden, d.h. durch Halten von **Shift** oder Drücken von **X**, **Y** oder **Z** während des Zeichnens.
-   Drücke während des Zeichnens **Q**, um einen \"Haltepunkt\" an der aktuellen Position des Cursors einzufügen. Du kannst dann rechtwinklig zu diesen Haltepunkten und an den Schnittpunkten ihrer rechtwinkligen Achsen fangen. Wenn [Entwurfsmittelpunkt](Draft_Snap_Midpoint/de.md) das Fangverhalten aktiviert ist, kannst du auch am mittleren Abstand zwischen zwei beliebigen Haltepunkten fangen. <small>(v0.17)</small> 


</div>

![](images/Draft_Snap_example_cycling_1.png ) 
*Snap cycling 1: The red rectangle was created first therefore it has snap priority. Without snap cycling you cannot snap to the green rectangle where it is overlapped by the red rectangle.*

![](images/Draft_Snap_example_cycling_2.png ) 
*Snap cycling 2: After using the snap cycle key once the green rectangle receives snap priority. Snapping to the midpoint of the overlapped green edge is now possible.*

## Hinweise


<div class="mw-translate-fuzzy">

-   Es ist ratsam, nur die Fangmethoden zu aktivieren, die du wirklich benötigst. Wenn zu viele aktiviert werden, kann dies die Arbeit verlangsamen.
-   Es ist keine gute Idee, den [Nächsten](Draft_Snap_Near/de.md) Fang permanent aktiv zu haben.


</div>

## Einstellungen

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

Note that after changing some preferences you must restart FreeCAD.


<div class="mw-translate-fuzzy">

-   Der maximale Abstand, bei dem ein Punkt als Fangpunkt betrachtet wird, kann spontan durch Drücken von **[** (erhöhen) oder **]** (verringern) Tasten geändert werden.

Diese Einstellung wird gespeichert: **|Werkzeuge → Parameter bearbeiten... → BasisAnwendung → Einstellungen → Mod → Entwurf → FangBereich**.

-   Die genannten Tasten können in den [Entwurf Einstellungen](Draft_Preferences/de.md) angepasst werden: **Bearbeiten → Einstellungen... → Entwurf → Einstellungen der Benutzeroberfläche → Befehlsinterne Tastenkombinationen**.


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/de
