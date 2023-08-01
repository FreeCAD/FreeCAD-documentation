---
- GuiCommand:
   Name: Draft SelectPlane
   Name/de: Draft EbeneAuswählen
   MenuLocation: Dienstprogramme - Ebene wählen
   Workbenches: [Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut: **W** **P**
   SeeAlso: [Draft ArbeitsebenenProxy](Draft_WorkingPlaneProxy/de.md)
---

# Draft SelectPlane/de



## Beschreibung


<div class="mw-translate-fuzzy">

Der <img alt="" src=images/Workbench_Draft.svg  style="width:24px;">[Entwurf Arbeitsbereich](Draft_Workbench/de.md) verfügt über ein Bearbeitungsebenensystem. Eine Ebene in der [3D Ansicht](3D_view/de.md) zeigt an, wo eine Entwurfsform erstellt wird. Es gibt mehrere Möglichkeiten, die Bearbeitungsebene zu definieren:

-   Von einer ausgewählten Fläche.
-   Von drei ausgewählten Knoten.
-   Aus der gegenwärtigen Sicht.
-   Von einer Voreinstellung: oben, vorne oder seitlich.
-   Keine, in diesem Fall wird die Bearbeitungsebene beim Starten eines Befehls automatisch an die aktuelle Ansicht oder an eine Fläche angepasst, wenn Du mit dem Zeichnen auf einer vorhandenen Fläche beginnst.


</div>

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">



*Unterschiedliche Arbeitsebenen können eingestellt werden, auf denen Formen gezeichnet werden können.*


</div>

## Usage with pre-selection 


<div class="mw-translate-fuzzy">

1.  Wähle eine Fläche eines vorhandenen Objekts in der [3D Ansicht](3D_view/de.md) aus, oder halte **strg** gedrückt und wähle drei Ecken eines Objekts. {{Version/de|0.17}}
2.  Drücke die Taste **<img src="images/Draft_SelectPlane.svg" width=16px> [WähleEbene](Draft_SelectPlane/de.md)**, oder klicke mit der rechten Maustaste und wähle **Hilfsmittel→ <img src="images/Draft_SelectPlane.svg" width=16px>. [WähleEbene](Draft_SelectPlane/de.md)**.


</div>

## Usage with post-selection 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut: **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md) for the supported objects.
    -   Select one or more subelements. You can select:
        -   A flat face.
        -   Three vertices.
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/Draft_SelectPlane.svg" width=16px> [WähleEbene](Draft_SelectPlane/de.md)
**, oder verwende **Entwurf** → **Hilfsmittel** → **<img src="images/Draft_SelectPlane.svg" width=16px> [WähleEbene](Draft_SelectPlane/de.md)** aus dem oberen Menü, oder das Tastaturkürzel **W** und dann **P**
2.  Wähle den Versatz, den Rasterabstand und die Hauptlinien
3.  Wähle eine der Voreinstellungen: **<img src="images/View-top.svg" width=16px> XY (oben)**, **<img src="images/View-front.svg" width=16px>  XZ (vorne)**, **<img src="images/View-right.svg" width=16px> YZ (Seite)**, **<img src="images/View-isometric.svg" width=16px> Ansicht**, oder **<img src="images/View-axonometric.svg" width=16px> Auto**.


</div>



## Optionen


<div class="mw-translate-fuzzy">

-   Drücke die **<img src="images/View-top.svg" width=16px> XY (top)** Taste um die Bearbeitungsebene in der XY Ebene festzulegen.

Um auf dieser Ebene leicht zeichnen zu können, solltest Du die Ansicht nach oben oder unten setzen (das Normal liegt in der positiven oder negativen Z Richtung). Drücke **2** oder **5**, um schnell zu diesen Ansichten zu wechseln.

-   Drücke die **<img src="images/View-front.svg" width=16px> XZ (front)** Taste, um die Bearbeitungsebene in der XZ Ebene festzulegen. Um auf dieser Ebene leicht zeichnen zu können, solltest Du die Ansicht nach vorne oder hinten setzen (das Normal liegt in negativer oder positiver Y Richtung). Drücke **1** oder **4**, um schnell zu diesen Ansichten zu wechseln.
-   Drücke die Taste {**<img src="images/View-right.svg" width=16px> YZ (side)** Taste, um die Bearbeitungsebene in der YZ Ebene einzustellen. Um auf dieser Ebene leicht zeichnen zu können, solltest Du die Ansicht auf die linke oder rechte Seite setzen. (das Normal liegt in positiver oder negativer X Richtung). Drücke  **3**} oder **6**, um schnell zu diesen Ansichten zu wechseln.
-   Drücke die **<img src="images/View-isometric.svg" width=16px> View** Taste , um die Bearbeitungsebene auf die aktuelle 3D Ansicht, senkrecht zur Kameraachse und durch den Ursprung (0,0,0) verlaufend, zu setzen.
-   Drücke die **<img src="images/View-axonometric.svg" width=16px> Auto** Taste , um eine aktuelle Bearbeitungsebene aufzuheben und automatisch eine Bearbeitungsebene zu setzen, wenn ein Werkzeug verwendet wird. Wenn ein Zeichenwerkzeug ausgewählt ist, wird das Gitter automatisch auf die aktuelle Ansicht aktualisiert; wenn die Ansicht gedreht wird und ein anderes Werkzeug ausgewählt wird, wird das Gitter in der neuen Ansicht neu gezeichnet. Dies entspricht dem Drücken von **<img src="images/View-isometric.svg" width=16px> View** automatisch vor der Verwendung eines Werkzeugs.
-   Setze den Wert \"Versatz\", um die Bearbeitungsebene in einem bestimmten senkrechten Abstand von der von dir gewählten Ebene zu setzen.
-   Setze den Wert \"Rasterabstand\", um den Abstand zwischen den einzelnen Linien im Raster zu definieren.
-   Setze den Wert \"Hauptlinie alle\", um eine etwas dickere Linie im Raster bei setzen des Wertes zu zeichnen. Zum Beispiel, wenn der Rasterabstand beispielsweise 0,5 m beträgt und alle 20 Linien eine Hauptlinie vorhanden ist, wird alle 10 m eine etwas dickere Linie sein.
-   Klicke auf das Kontrollkästchen \"Mittelebene auf Ansicht\", um die Ebene und das Gitter in der 3D Ansicht näher an die Kameraansicht zu zeichnen.
-   Drücke **Esc** oder die {{button|Close}} Taste, um den aktuellen Befehl abzubrechen.


</div>



## Hinweise

-   It can be useful to align the [3D view](3D_view.md) with the selected Draft working plane. For example after switching the working plane to Front you may want to switch to the [Front view](Std_ViewFront.md) as well.
-   The grid can be toggled with the [Draft ToggleGrid](Draft_ToggleGrid.md) command.
-   By double-clicking [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) in the [Tree view](Tree_view.md) you can quickly switch between working planes.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   The grid settings in the task panel as well as several other grid settings are available as preferences: **Edit → Preferences... → Draft → Grid and snapping → Grid**.
-   To use the grid the **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid** option must be selected. After changing this preference you must restart FreeCAD.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Du kannst auf die aktuelle Bearbeitungsebene Entwurf zugreifen und Transformationen darauf anwenden:


</div>


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui

workplane = App.DraftWorkingPlane

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()

workplane.alignToPointAndAxis(v1, v2, 17)
Gui.Snapper.toggleGrid()
Gui.Snapper.toggleGrid()
```


<div class="mw-translate-fuzzy">

Du kannst deine eigenen Ebenen erstellen und sie unabhängig von der aktuellen Arbeitsebene verwenden. Dies ist nützlich, wenn du Berechnungen oder Projektionen in diesen anderen Ebenen durchführen musst.


</div>


```python
import WorkingPlane

my_plane = WorkingPlane.plane()

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()
my_plane.alignToPointAndAxis(v1, v2, 17)

projection = my_plane.projectPoint(App.Vector(10, 15, 2))
print(projection)
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/de
