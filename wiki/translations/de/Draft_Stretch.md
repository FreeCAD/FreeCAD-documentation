---
 GuiCommand:
   Name: Draft Stretch
   Name/de: Draft Strecken
   MenuLocation: Änderung , Strecken<br>Bearbeiten , Strecken
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: **S** **H**
   Version: 0.17
---

# Draft Stretch/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Stretch.svg  style="width:24px;"> **Draft Strecken** dehnt Objekte, indem es ausgewählte Punkte bewegt.

<img alt="" src=images/Draft_Stretch_Example.jpg  style="width:400px;"> 
*Strecken von drei Draft-Drähten*



## Anwendung

Siehe auch: [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).

1.  Wahlweise einen oder mehrere Objekte auswählen. Die objekte müssen [Draft Linien](Draft_Line/de.md), [Draft Linienzüge](Draft_Wire/de.md) (Polylinien), [Draft Rechtecke](Draft_Rectangle/de.md), [Draft B-Splines](Draft_BSpline/de.md) oder [Draft Bézierkurve](Draft_BezCurve/de.md) sein. Andere Objekte werden ignoriert.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Stretch.svg" width=16px> [Strecken](Draft_Stretch/de.md)** drücken.
    -   [Draft](Draft_Workbench.md): Den Menüeintrag **Änderung → <img src="images/Draft_Stretch.svg" width=16px> Strecken** auswählen.
    -   [BIM](BIM_Workbench.md): Den Menüeintrag **Bearbeiten → <img src="images/Draft_Stretch.svg" width=16px> Strecken** auswählen.
    -   Das Tastaturkürzel **S** dann **H**.
3.  Wurde noch kein Objekt ausgewählt: Ein Objekt in der [3D-Ansicht](3D_view/de.md) auswählen.
4.  Der Aufgaben-Bereich **Strecken** wird geöffnet. Siehe [Optionen](#Optionen.md) Für weitere Informationen.
5.  Den ersten Punkt, eine Ecke eines rechteckigen Auswahlbereichs, in der [3D-Ansicht](3D_view/de.md) auswählen oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
6.  Den zweiten Punkt, die gegenüberliegende Ecke des Auswahlbereichs, in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
7.  Die Punkte des ausgewählten Objekts, die innerhalb des Auswahlbereiches liegen, werden markiert.
8.  Den dritten Punkt, den Basispunkt, in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
9.  Den vierten Punkt, den Zielpunkt, in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.



## Optionen

Die im Aufgaben-Bereich verfügbaren Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft-Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.

-   Zum manuellen Eingeben der Koordinaten werden die X-, Y- und Z-Komponenten eingegeben und jeweils anschließend **Enter** gedrückt oder es wird die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** gedrückt, sobald die gewünschten Werte erreicht sind. Es ist ratsam, den Mauszeiger aus dem [3D-Ansicht](3D_view/de.md) heraus zu bewegen, bevor Koordinaten eingegeben werden.

-    **R**drücken oder die Checkbox **Relativ** aktivieren, um den Relativ-Modus umzuschalten. Ist der Relativ-Modus eingeschaltet, werden die Koordinaten des zweiten Punktes des Versatzes relativ zum ersten Punkt angegeben, andernfalls zum Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den Global-Modus umzuschalten. Ist der Global-Modus eingeschaltet, werden Koordinaten relativ zum globalen Koordinatensystem angegeben, andernfalls zum Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md).

-    **S**drücken, um [Draft Einrasten](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**drücken oder die Schaltfläche **Schließen** drücken, um den Befehl abzubrechen.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Es gibt keine Python-Methode, um Objekte zu strecken. Um die Ergebnisse des Befehls Draft Strecken zu emulieren, müssen die geometrische Eigenschaften der Objekte geändert werden.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Stretch/de
