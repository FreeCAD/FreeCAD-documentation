# Manual:Navigating in the 3D view/de
{{Manual:TOC/de}}

### Ein Wort zum 3D Raum 

Wenn dies dein erster Kontakt mit einer 3D Anwendung ist, musst du dich zuerst mit einigen Konzepten vertraut machen. Wenn nicht, kannst du diesen Abschnitt sicher überspringen.

Der FreeCAD 3D Raum ist ein [Euklidischer Raum](https://en.wikipedia.org/wiki/Euclidean_space). Er hat einen Ursprungspunkt und drei Achsen: X, Y und Z. Wenn du deine Szene von oben betrachtest, zeigt die X Achse konventionell nach rechts, die Y Achse nach hinten und die Z Achse nach oben. In der unteren rechten Ecke der FreeCAD Ansicht kannst Du immer sehen, von wo aus du die Szene betrachtest:

![](images/Axes_orientation.png )

Der Punkt, an dem sich die drei Achsen treffen, ist der Ursprung. Es ist der Punkt, an dem der Wert aller Koordinaten Null ist. Für jede beliebige Achse wird bei Bewegung in einer Richtung der Koordinatenwert erhöht und bei Bewegung in der entgegengesetzten Richtung verringert sich der Koordinatenwert. Jeder Punkt jedes im 3D-Raum vorhandenen Objekts kann über seine (x, y, z) Koordinaten lokalisiert werden. Zum Beispiel wird ein Punkt mit den Koordinaten (2, 3, 1) bei +2 Einheiten auf der X-Achse, +3 Einheiten auf der Y-Achse und +1 Einheit auf der Z-Achse liegen:

![](images/3dspace_coordinates.jpg )

Du kannst diese Szene aus jedem Winkel betrachten, als ob du eine Kamera in der Hand hättest. Diese Kamera kann nach links, rechts, oben und unten bewegt (schwenken), um das, worauf sie zeigt, gedreht (drehen) und näher an die Szene herangeführt oder von ihr entfernt werden (zoomen).

### Die FreeCAD 3D Ansicht 

#### Mausnavigation

Das Navigieren in der FreeCAD [3D-Ansicht](3D_view/de.md) kann mit einer Maus, einem 3D-Navigator, der Tastatur, einem Touchpad oder einer Kombination aus diesen erfolgen. FreeCAD stellt mehrere [Navigationsmodi](Mouse_navigation/de.md) zur Verfügung, die die drei grundlegenden Operationen zur Steuerung der Ansicht (Schwenken, Drehen und Zoomen) bestimmen und wie die Auswahl von Objekten auf dem Bildschirm erfolgt. Die Navigationsmodi werden über die Ansicht \"Einstellungen\" oder direkt durch einen Rechtsklick auf eine beliebige Stelle in der [3D-Ansicht](3D_view/de.md) aufgerufen:

![](images/FreeCAD-v0-18-NavigationModePopup.png )

Jeder dieser Modi ordnet diesen vier Operationen unterschiedliche Maustasten oder Maus + Tastatur-Kombinationen oder Mausgesten zu. Die folgende Tabelle zeigt die wichtigsten verfügbaren Modi:

++++++
| Betriebsart              | Schwenken                                                                                                                                                                                                          | Drehen                                                                                                                                                                                                       | Zoom                                                                                                                                                                            | Auswahl                                                                                         |
+==========================+====================================================================================================================================================================================================================+==============================================================================================================================================================================================================+=================================================================================================================================================================================+=================================================================================================+
| OpenInventor             | ![Drücke mittlere Maustaste](images/Pan-mouse.svg )                                                                                                                                            | ![Drücke linke Maustaste](images/Select-mouse.svg )                                                                                                                                         | ![Drehe Mausrad](images/Zoom-mouse.svg )                                                                                                                                |                                                                                  |
|                          |                                                                                                                                                                                                                    |                                                                                                                                                                                                              |                                                                                                                                                                                 | **Strg**                                                                                    |
|                          |                                                                                                                                                                                                                    |                                                                                                                                                                                                              |                                                                                                                                                                                 |                                                                                              |
|                          |                                                                                                                                                                                                                    |                                                                                                                                                                                                              |                                                                                                                                                                                 | halten und ziehen ![Drücke linke Maustaste](images/Select-mouse.svg )          |
++++++
| CAD **(voreingestellt)** | ![Drücke mittlere Maustaste](images/Pan-mouse.svg ) oder ![Drücke rechte Maustaste + STRG Taste](images/Pan-mouse-CTRL.svg )                                    | ![Halte mittlere dann linke Maustaste](images/Rotate-mouse.svg ) oder ![Drücke rechte Maustaste + SHIFT Taste](images/Rotate-mouse-SHIFT.svg ) | ![Drehe Mausrad](images/Zoom-mouse.svg ) oder ![Drücke rechte Maustaste + STRG + SHIFT Taste](images/Zoom-mouse-CTRL-SHIFT.svg ) | ![Drücke linke Maustaste](images/Select-mouse.svg )                            |
++++++
| Blender                  |                                                                                                                                                                                                     | ![Drücke mittlere Maustaste](images/Pan-mouse.svg )                                                                                                                                      | ![Drehe mittlere Maustaste](images/Zoom-mouse.svg )                                                                                                          | ![Drücke linke Maustaste](images/Select-mouse.svg )                            |
|                          | **Shift**                                                                                                                                                                                                      |                                                                                                                                                                                                              |                                                                                                                                                                                 |                                                                                                 |
|                          |                                                                                                                                                                                                                 |                                                                                                                                                                                                              |                                                                                                                                                                                 |                                                                                                 |
|                          | halten und ziehen ![Drücke mittlere Maustaste](images/Pan-mouse.svg ) oder ziehe ![Drücke linke + rechte Maustaste und ziehe](images/Mouse_LMB%2BRMB.svg ) |                                                                                                                                                                                                              |                                                                                                                                                                                 |                                                                                                 |
++++++
| Touchpad                 |                                                                                                                                                                                                     |                                                                                                                                                                                               |                                                                                                                                                                  | ![Drücke Touchpad (Maus) linke Taste](images/Select-touchpad.png ) |
|                          | **Shift**                                                                                                                                                                                                      | **Alt**                                                                                                                                                                                                  | **PgUp**                                                                                                                                                                    |                                                                                                 |
|                          |                                                                                                                                                                                                                 |                                                                                                                                                                                                           |                                                                                                                                                                              |                                                                                                 |
|                          | halten und ziehen ![Touchpad (Maus) -Zeiger](images/Touchpad.png )                                                                                                                               | \+ ![Touchpad (Maus)-Zeiger](images/Touchpad.png )                                                                                                                                          | / **PgDown**                                                                                                                                                  |                                                                                                 |
++++++
| Gesture                  | ziehe ![Drücke rechte Maustaste](images/Pan-mouse-Ctrl.svg )                                                                                                                                     | ziehe ![Drücke linke Maustaste](images/Select-mouse.svg )                                                                                                                                   | ![Drehe Mausrad](images/Zoom-mouse.svg )                                                                                                                                | ![Drücke linke Maustaste](images/Select-mouse.svg )                            |
++++++
| OpenCascade              | ![Drücke mittlere Maustaste](images/Pan-mouse.svg )                                                                                                                                            | ![Halte mittlere, dann rechte Maustaste](images/Rotate-mouse-MMB+RMB.svg )                                                                                                   | ![Drehe Mausrad](images/Zoom-mouse.svg )                                                                                                                                | ![Drücke linke Maustaste](images/Select-mouse.svg )                            |
++++++

#### Tastaturnavigation

Alternativ sind einige Bedienelemente der Tastatur immer verfügbar, unabhängig vom Navigationsmodus:

-   Die Tasten **Strg**+{{ASCII|43}} und **Strg**+{{ASCII|22}} zum Vergrößern und Verkleinern

-   Die Pfeiltasten {{ASCII|17}}, {{ASCII|16}}, {{ASCII|30}} und {{ASCII|31}} zum Verschieben der Ansicht nach links/rechts und oben/unten

-   Die Tasten **Shift**+{{ASCII|17}} und **Shift**+{{ASCII|16}} um die Ansicht um 90 Grad zu drehen

-   Die Zifferntasten {{ASCII|48}}, {{ASCII|49}}, {{ASCII|50}}, {{ASCII|51}}{{ASCII|52}}, {{ASCII|53}} und {{ASCII|54}} für die sieben Standardansichten: <img alt="" src=images/Std_ViewIsometric.svg  style="width:24px;"> [Isometrisch](Std_ViewIsometric/de.md), <img alt="" src=images/Std_ViewFront.svg  style="width:24px;"> [Vorderansicht](Std_ViewFront/de.md), <img alt="" src=images/Std_ViewTop.svg  style="width:24px;"> [Draufsicht](Std_ViewTop/de.md), <img alt="" src=images/Std_ViewRight.svg  style="width:24px;"> [Ansicht von rechts](Std_ViewRight/de.md), <img alt="" src=images/Std_ViewRear.svg  style="width:24px;"> [Rückansicht](Std_ViewRear/de.md), <img alt="" src=images/Std_ViewBottom.svg  style="width:24px;"> [Boden](Std_ViewBottom/de.md) und <img alt="" src=images/Std_ViewLeft.svg  style="width:24px;"> [Ansicht von links](Std_ViewLeft/de.md)

-    **V**
    **O**setzt die Kamera in die <img alt="" src=images/View-isometric.svg  style="width:24px;"> [Orthographische Ansicht](Std_OrthographicCamera.md).

-    **V**
    **P**setzt sie in die <img alt="" src=images/View-perspective.svg  style="width:24px;"> [Perspectivische Ansicht](Std_PerspectiveCamera/de.md).

-    **Strg**erlaubt, mehr als ein Objekt oder Element auszuwählen.

Diese Steuerelemente sind auch über das [Menü Ansicht](Std_View_Menu/de.md) und einige über die Symbolleiste Ansicht verfügbar.

##### Verwendung des Navigationsclusters 

In der Standardeinstellung befindet sich ein [Navigationscluster](Navigation_Cube/de.md) in der oberen rechten Ecke der 3D Anzeige. Dieser kann dazu verwendet werden, das angezeigte Objekt um einen festen Betrag zu drehen, die Anzeige auf eine von mehreren Standardansichten zurücksetzen, und den Anzeigemodus zu ändern.

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

Bei Verwendung des Navigationsclusters wird ein Kontrollpunkt hellblau, wenn der Zeiger über einen empfindlichen Bereich schwebt. Wenn der Bereich unter dem Zeiger seine Farbe nicht ändert, hat ein Klick darauf keinen Einfluss. Vom Zeitpunkt des Schreibens an (v0.18) gibt es einige Registrierungsprobleme, die verhindern, dass alle Teile einiger Kontrollpunkte aktiv sind.

Klicken auf eine Seite wird die Ansicht auf dieser Seite umschalten; Ein Klick auf eine Ecke wechselt zu einer Ansicht, bei der die Ecke auf dich zeigt.

Klicken auf eines der vier Dreiecke dreht die Ansicht um 45 Grad in die angegebene Richtung. Klicken auf einen der beiden gekrümmten Pfeile oben dreht die Ansicht um 45 Grad in der angegebenen Richtung um eine Linie, die auf dich zeigt.

Das Navigationscluster kann durch Ziehen an jede Stelle der 3D Anzeige verschoben werden. Die linke Maustaste muss innerhalb des Würfels selbst gedrückt werden, um das Ziehen zu initiieren. Die Struktur beginnt sich erst dann zu bewegen, wenn der Mauszeiger aus dem Würfel gezogen wird.

Unten rechts im Cluster befindet sich ein kleinerer Mini Würfel, der ein Aufklappmenü aktiviert, mit dem du den Ansichtsmodus wechseln kannst.

### Objekte anwählen 

Objekte in der 3D Ansicht können je nach Navigationsmodus (oben beschrieben) durch Anklicken mit der entsprechenden Maustaste ausgewählt werden. Mit einem einzigen Klick werden das Objekt und eine seiner Unterkomponenten (Kante, Fläche, Knoten) ausgewählt. Ein Doppelklick wählt das Objekt und alle seine Unterkomponenten aus. Du kannst mehr als eine Unterkomponente oder sogar verschiedene Unterkomponenten von verschiedenen Objekten auswählen, indem du die STRG Taste drückst. Wenn Sie mit dem Auswahlknopf auf einen leeren Bereich der 3D Ansicht klicken, wird alles abgewählt.

Ein Paneel namens \"Auswahlansicht\", das im Menü \"Ansicht\" verfügbar ist, kann ebenfalls eingeschaltet werden, die dir zeigt, was gerade ausgewählt ist:

![](images/Selection_view.jpg )

Du kannst auch die Auswahlansicht verwenden, um Objekte durch die Suche nach einem bestimmten Objekt auszuwählen.

**Weiterlesen**

-   [Die FreeCAD Navigationsmodi](Mouse_navigation/de.md)
-   [Navigationscluster](Navigation_Cube/de.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > Manual:Navigating in the 3D view/de
