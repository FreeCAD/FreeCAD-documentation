# Constraint/de
## Einleitung




In FreeCAD wird das Wort \"[Randbedingung](Constraint/de.md)\" (Beschränkung) normalerweise verwendet, um sich auf eine \"Regel\" zum Zeichnen geometrischer Formen innerhalb einer <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketch/de.md) (Klasse `Sketcher::SketchObject`) zu beziehen. Eine Randbedingung legt die Position eines bestimmten geometrischen Elements auf verschiedene Weisen fest; z.B. kann sie angeben, dass ein Element horizontal oder vertikal ist, tangential, parallel oder senkrecht zu einem anderen verläuft, mit einem Punkt deckungsgleich ist, konzentrisch zu einem anderen Objekt liegt usw.

Es gibt zwei Oberarten von Randbedingungen:

-    **Geometrische Randbedingungen**legen die Eigenschaften von Formen fest, ohne genaue Abmessungen anzugeben, z.B. Horizontalität, Vertikalität, Parallelität, Rechtwinkligkeit und Tangentialität.

-    **Bezugbasierte**oder **Maßliche Randbedingungen** legen Merkmale von Formen durch Angabe von Längen, Abständen oder Winkeln fest.

Siehe die Informationen des Arbeitsbereichs <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/de.md) für eine Liste aller Randbedingungen, die angewendet werden können. Einige von ihnen gelten für Linien, andere für Kurven und wieder andere für Knoten. Siehe auch [Grundlegendes Sketcher Tutorium](Basic_Sketcher_Tutorial/de.md).



## Anwendung

1.  Eine Skizze erstellen, entweder im Arbeitsbereich <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/de.md) oder über den Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md).
2.  Dementsprechend eine Möglichkeit wählen:
    -   Die Schaltfläche **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher Skizze erstellen](Sketcher_NewSketch/de.md)** drücken.
    -   Die Schaltflächen **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper erstellen](PartDesign_Body.md)** gefolgt von **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Skizze erstellen](PartDesign_NewSketch/de.md)** drücken.
3.  Die Skizze wird im Bearbeitungsmodus geöffnet.
4.  Eine Folge von Linien zeichnen mit **[<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Linienzug erstellen](Sketcher_CreatePolyline/de.md)**.
5.  Eine der Linien auswählen, und die Schaltfläche **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Vertikal festlegen](Sketcher_ConstrainVertical/de.md)** drücken.
6.  Eine der Linien auswählen, und die Schaltfläche **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md)** drücken.
7.  Die vertikale Linie auswählen und die Schaltfläche **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md)** drücken; anschließend eine Länge angeben.
8.  Die horizontale Linie auswählen und die Schaltfläche **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md)** drücken; anschließend eine Länge angeben.



## Hinweise

-   Randbedingungen sind nützlich, um sehr präzise Profile zu erstellen, die mit den Werkzeugen **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Block](PartDesign_Pad/de.md)** oder **[<img src=images/Part_Extrude.svg style="width:16px"> [Part Extrudieren](Part_Extrude/de.md)** zu Festkörpern extrudiert werden können.
-   Randbedingungen werden nur innerhalb von [Skizzen](Sketch/de.md) verwendet; andere 2D-Objekte, wie solche die mit dem Arbeitsbereich <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) erstellt werden, arbeiten nicht mit Randbedingungen; letztere werden einfach im 3D-Raum abgelegt, und ihre Form und Position über ihre Eigenschaften festgelegt.


{{Sketcher Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Sketcher](Category_Sketcher.md) > Constraint/de
