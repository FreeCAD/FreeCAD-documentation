---
- GuiCommand:/de
   Name:Draft Stretch
   Name/de:Draft Strecken
   MenuLocation:Änderung → Strecken
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**S** **H**
   Version:0.17
---

# Draft Stretch/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Stretch.svg  style="width:24px;"> **Draft Strecken** dehnt Objekte, indem es ausgewählte Punkte bewegt.

<img alt="" src=images/Draft_Stretch_Example.jpg  style="width:400px;"> 
*Strecken von drei Draft-Drähten*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).


<div class="mw-translate-fuzzy">

1.  Wähle ein Objekt aus, das Du dehnen möchtest.
2.  Drücke die Taste **<img src="images/Draft_Stretch.svg" width=16px> [[Draft Stretch]]**. Wenn kein Objekt ausgewählt ist, wirst Du aufgefordert, eines auszuwählen.
3.  Klicke auf einen Punkt in der 3D Ansicht, oder gib eine Koordinate ein und drücke die Taste **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** .
4.  Klicke auf einen zweiten Punkt in der 3D Ansicht, oder gib eine Koordinate and drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Taste. Die ersten beiden Punkte definieren ein Auswahlrechteck. Die von diesem Rechteck eingeschlossenen Eckpunkte des ursprünglichen Objekts werden hervorgehoben.
5.  Klicke auf einen dritten Punkt in der 3D Ansicht, oder gib eine Koordinate und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Taste.
6.  Klicke auf einen vierten Punkt in der 3D Ansicht, oder gib eine Koordinate und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen** Taste. Das zweite Punktpaar definiert eine Linie, deren Abstand und Richtung verwendet wird, um die an den markierten Punkten angebrachte Figur zu strecken.


</div>



## Optionen

Die hier genannten Tastaturkürzel für einzelne Zeichen können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md).

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, the coordinates of the second point of the displacement are relative to the first point, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   Um die Anzahl der Dezimalstellen für die Eingabe der Koordinaten zu ändern: **Bearbeiten → Eigenschaften... → Allgemein → Einheiten → Einheiten-Einstellungen → Anzahl der Nachkommastellen**



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python-Methode, um Objekte zu strecken. Um die Ergebnisse des Befehls Draft Strecken zu emulieren, müssen die geometrische Eigenschaften der Objekte geändert werden.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Stretch/de
