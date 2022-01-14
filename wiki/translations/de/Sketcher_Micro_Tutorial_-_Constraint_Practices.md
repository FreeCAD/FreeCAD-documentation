# Sketcher Micro Tutorial - Constraint Practices/de
{{TutorialInfo/de
|Topic=Skizzierer
|Level=Anfänger
|Time=30 Minuten
|Author=Mark Stephen ([Quick61](User_Quick61.md)) und vocx
|FCVersion 0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&p=371659#p371659 Skizzierer Beschränkungspraktiken]
}}

## Einführung

Dieses Tutorial wurde ursprünglich von Quick61 geschrieben, und es wurde von vocx neu geschrieben und neu illustriert.

Dieses Tutorium ist so gestaltet um dem neuen Anwender zu helfen, sich mit den bewährten Verfahren zur Beschränkung einer [Skizze](Sketch/de.md) im Arbeitsablauf des <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Skizzierer Arbeitsbereichs](Sketcher_Workbench/de.md) vertraut zu machen.

Es gibt eine allgemeine Regel mit Beschränkungen: je weniger **Bezugsbeschränkungen** (Dimensionen), desto besser.

Vorzuziehen ist, wenn möglich, eine **geometrische Beschränkung** anstelle einer dimensionalen zu verwenden. Dies hat mit der internen Funktionsweise des Beschränkungslösers des Skizzierers zu tun.

## Einrichtung

1\. Öffne FreeCAD, erstelle ein neues leeres Dokument mit **Datei → [<img src=images/Std_New.svg style="width:16px"> [Neu](Std_New/de.md)**.

:   1.1. Wechsle zum [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) über den [Arbeitsbereich Wähler](Std_Workbench/de.md) oder das Menü **[Ansicht](Std_View_Menu/de.md) → Arbeitsbereich → Skizzierer**.

Einige Aktivitäten zum Erinnern:

-   Drücke die rechte Maustaste, oder drücke **Esc** einmal auf der Tastatur, um das aktive Werkzeug im Bearbeitungsmodus abzuwählen.
-   Um den Skizzenbearbeitungsmodus zu verlassen, drücke die **Schließen** Schaltfläche im [Aufgabenpaneel](task_panel/de.md) oder drücke **Esc** zweimal auf der Tastatur.
-   Um den Bearbeitungsmodus erneut aufzurufen, doppelklicke auf die Skizze in der [Baumansicht](tree_view/de.md) oder wähle sie aus und klicke dann auf **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [Skizze bearbeiten](Sketcher_EditSketch/de.md)**.

## Erstellen einer Skizze 

2\. Klicke auf **<img src="images/Sketcher_NewSketch.svg‎‎" width=16px> [Neue Skizze](Sketcher_NewSketch/de.md)**.

:   2.1. Wähle die Skizzenausrichtung, d.h. eine der Basisebenen XY, XZ oder YZ. Wir werden die Standardebene und -optionen verwenden.
:   2.2. Klicke **OK**, um mit der Konstruktion der Skizze zu beginnen.


**Hinweis:**

im [Augabenpaneel](task_panel/de.md) erweitere den **Bedienelemente bearbeiten** Abschnitt und stelle sicher, dass die Option **Auto Beschränkungen** deaktiviert ist. Schalte auch den Rasterfang aus und blende das Raster aus.

## Erster Näherung: Bezugsbeschränkungen 

3\. Wir werden ein vollständig beschränktes Quadrat zeichnen, das am Ursprung zentriert ist.

:   3.1. Klicke auf **<img src="images/Sketcher_CreatePolyline.svg‎‎" width=16px> [Erstelle Polylinie](Sketcher_CreatePolyline/de.md)** und zeichne dann vier Linien in der allgemeinen Form eines Rechtecks um den Ursprung.

<img alt="" src=images/01a_Sk02_Sketcher_Rectangle_unconstrained.png  style="width:" height="400px;"> 
*Unbeschränkte rechteckige Skizze.*

:   3.2. Wähle eine horizontale Linie, und drücke **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md)**, gib dann {{Value|20 mm}} ein.
:   3.3. Wähle die andere horizontale Linie und wiederhole die Beschränkung mit dem gleichen Abstand.
:   3.4. Wähle eine vertikale Linie und drücke **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md)**, gib dann {{Value|20 mm}} ein.
:   3.5. Wähle die andere vertikale Linie und wiederhole die Beschränkung mit dem gleichen Abstand.
:   3.6. Wähle einen unteren Eckpunkt (a) und den Ursprung der Skizze aus und drücke **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md)**, gib dann {{Value|10 mm}} ein.
:   3.7. Wähle den oberen Eckpunkt (b) über dem vorherigen Eckpunkt (a) und den Ursprung der Skizze und wiederhole die horizontale Beschränkung mit dem gleichen Abstand.
:   3.8. Wähle den anderen unteren Eckpunkt (c) und den Ursprung der Skizze, und drücke **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md)**, gib dann {{Value|10 mm}} ein.
:   3.9. Wähle erneut den oberen Eckpunkt (b) und den Ursprung der Skizze und wiederhole die vertikale Beschränkung mit dem gleichen Abstand.

<img alt="" src=images/01b_Sk02_Sketcher_Rectangle_constrained_lengths_1.png  style="width:" height="400px;"> <img alt="" src=images/01c_Sk02_Sketcher_Rectangle_constrained_lengths_2.png  style="width:" height="400px;"> 
*Links: Bezugsbeschränkungen für die Seiten. Rechts: zusätzliche Bezugsbeschränkungen für die Innenabstände.*

Mit Blick auf die **Beschränkungen** Abschnitt im [Aufgabenpaneel](task_panel/de.md), sehen wir, dass die Beschränkungen zu zahlreich sind; sie erschweren auch den Blick auf die Skizze. Diese Beschränkungen sind auch für den Löser rechenintensiv; obwohl dies bei einer einfachen Form kein Problem darstellt, kann es bei komplexeren Formen zu einem Problem werden.

## Ein besserer Weg: Bezugs und geometrische Beschränkungen 

4\. Wir werden dasselbe Quadrat vollständig beschränkt und am Ursprung zentriert zeichnen. Wenn du die neue Skizze erstellst, vergewissere dich, dass die Option **Auto Beschränkungen** deaktiviert ist.

:   4.1. Klicke auf **<img src="images/Sketcher_CreatePolyline.svg‎‎" width=16px> [Erstelle Polylinie](Sketcher_CreatePolyline/de.md)**, dann zeichne vier Linien in der allgemeinen Form eines Rechtecks um den Ursprung.
:   4.2. Wähle eine horizontale Linie aus, und drücke **[<img src=images/Constraint_Horizontal.svg style="width:16px"> [Horizontal](‎Sketcher_ConstrainHorizontal/de.md)**.
:   4.3. Wähle die andere horizontale Linie, und wiederhole die Beschränkung.
:   4.4. Wähle eine vertikale Linie, und drücke **[<img src=images/Constraint_Vertical.svg style="width:16px"> [Vertikal](‎Sketcher_ConstrainVertical/de.md)**.
:   4.5. Wähle die andere vertikale Linie aus, und wiederhole die Beschränkung.

<img alt="" src=images/02a_Sk02_Sketcher_Rectangle_constrained_horizontal-vertical.png  style="width:" height="400px;"> 
*Geometrische horizontale und vertikale Beschränkungen.*

:   4.6. Wähle eine horizontale Linie und drücke **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md)**, gib dann {{Value|20 mm}}. Wir sehen, dass die andere horizontale Linie gleichzeitig ihre Größe ändert.
:   4.7. Wähle eine vertikale Linie aus, und drücke **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md)**, gib dann {{Value|20 mm}} ein. Wir sehen, dass die andere vertikale Linie gleichzeitig ihre Größe ändert.
:   4.8. Wähle einen unteren Eckpunkt (a) und den Ursprung der Skizze aus und drücke **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md)**, gib dann {{Value|10 mm}} ein.
:   4.9. Wähle den oberen Eckpunkt (b) über dem vorherigen Eckpunkt (a) und den Ursprung der Skizze und drücke **[<img src=images/Constraint_VerticalDistance.svg style="width:16px"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md)**, gib dann {{Value|10 mm}} ein.

<img alt="" src=images/02b_Sk02_Sketcher_Rectangle_constrained_lengths_1.png  style="width:" height="400px;"> <img alt="" src=images/02c_Sk02_Sketcher_Rectangle_constrained_lengths_2.png  style="width:" height="400px;"> 
*Links: Bezugsbeschränkungen für nur zwei Seiten. Rechts: zusätzliche Bezugsbeschränkungen für nur zwei Innenabstände.*

Dies ist eine besser beschränkte Skizze als die erste. Die horizontalen und vertikalen geometrischen Beschränkungen erlauben es uns, weniger Bezugsbeschränkungen zu verwenden, so dass unsere Skizze weniger überladen aussieht.

## Optimales Schema: meist geometrische Beschränkungen 

5\. Wir werden dasselbe Quadrat vollständig beschränkt und am Ursprung zentriert zeichnen. Wenn du die neue Skizze erstellst, vergewissere dich, dass die Option **Auto Beschränkungen** deaktiviert ist.

:   5.1. Klicke auf **<img src="images/Sketcher_CreatePolyline.svg‎‎" width=16px> [Erstelle Polylinie](Sketcher_CreatePolyline/de.md)**, dann zeichne vier Linien in der allgemeinen Form eines Rechtecks um den Ursprung.
:   5.2. Wähle eine horizontale Linie aus, und drücke **[<img src=images/Constraint_Horizontal.svg style="width:16px"> [Horizontal](‎Sketcher_ConstrainHorizontal/de.md)**.
:   5.3. Wähle die andere horizontale Linie, und wiederhole die Beschränkung.
:   5.4. Wähle eine vertikale Linie, und drücke **[<img src=images/Constraint_Vertical.svg style="width:16px"> [Vertikal](‎Sketcher_ConstrainVertical/de.md)**.
:   5.5. Wähle die andere vertikale Linie aus, und wiederhole die Beschränkung.

<img alt="" src=images/03a_Sk02_Sketcher_Rectangle_constrained_horizontal-vertical.png  style="width:" height="400px;"> 
*Geometrische horizontale und vertikale Beschränkungen.*

:   5.6. Wähle einen unteren Eckpunkt (a), dann den oberen Eckpunkt, der diagonal gegenüber liegt, und dann den Ursprung der Skizze; drücke dann **[<img src=images/Constraint_Symmetric.svg style="width:16px"> [Symmetrisch](Sketcher_ConstrainSymmetric/de.md)**. Die beiden ausgewählten Punkte sind gleich weit vom Ursprung entfernt.
:   5.7. Wähle zwei benachbarte Seiten des Rechtecks (verbunden an einer Ecke), und drücke **[<img src=images/Constraint_EqualLength.svg style="width:16px"> [Gleiche Länge](Sketcher_ConstrainEqual/de.md)**. Beachte, dass aufgrund der Symmetrie der Eckpunkte nun alle Seiten gleich groß sind.

<img alt="" src=images/03b_Sk02_Sketcher_Rectangle_constrained_symmetric.png  style="width:" height="400px;"> <img alt="" src=images/03c_Sk02_Sketcher_Rectangle_constrained_equal_length.png  style="width:" height="400px;"> 
*Links: symmetrische Beschränkung für nur zwei Eckpunkte. Rechts: zusätzliche gleiche Längenabstände für nur zwei benachbarte Seiten.*

:   5.8. Wähle eine horizontale Linie und drücke **[<img src=images/Constraint_HorizontalDistance.svg style="width:16px"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md)**, gib dann {{Value|20 mm}}. ein. Aufgrund der zuvor hinzugefügten Beschränkungen für Symmetrie und Längengleichheit sehen wir, dass alle Seiten gleichzeitig gleich werden.

<img alt="" src=images/03d_Sk02_Sketcher_Rectangle_constrained_length.png  style="width:" height="400px;"> 
*Alle angewandten geometrischen Beschränkungen und eine einzige Bezugsbeschränkung für eine Seite.*

Dies ist der beste Weg, diese Skizze zu beschränken, da wir nur eine Bezugs- (Bemaßungs-) Beschränkung verwendet haben.

## Zusätzliche Quellen 

-   [Grundlegendes Skizzierer Tutorium](Basic_Sketcher_Tutorial/de.md)
-   [Skizzierer Referenz](Sketcher_reference/de.md)
-   [Skizzierer Tutorium](Sketcher_Tutorial/de.md)


{{Tutorials navi

}} {{Sketcher Tools navi}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Micro Tutorial - Constraint Practices/de
