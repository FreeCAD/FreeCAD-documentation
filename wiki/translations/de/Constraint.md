# Constraint/de
## Einführung


{{TOCright}}

In FreeCAD wird das Wort \"[Beschränkung](Constraint/de.md)\" normalerweise verwendet, um sich auf eine \"Regel\" zum Zeichnen geometrischer Formen innerhalb einer <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Skizze](Sketch/de.md) (`Sketcher::SketchObject` Klasse) zu beziehen. Eine Beschränkung begrenzt die Position eines bestimmten geometrischen Elements auf verschiedene Weise, z.B. kann sie angeben, ob das Element horizontal, vertikal, tangential, parallel, senkrecht, mit einem Punkt deckungsgleich, konzentrisch zu einem anderen Objekt usw. ist.

Es gibt zwei große Typen von Beschränkungen:

-    **Geometrische Beschränkungen**definieren Eigenschaften der Formen, ohne genaue Abmessungen anzugeben, z.B. Horizontalität, Vertikalität, Parallelität, Rechtwinkligkeit und Tangentialität.

-    **Bezugsbeschränkungen**oder **Maßliche Beschränkungen** definieren Merkmale der Formen durch Angabe von Abmessungen, z.B. eine numerische Länge oder einen Winkel.

Siehe die Informationen in der <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md) für eine Liste aller Beschränkungen, die angewendet werden können. Einige von ihnen gelten für Linien, andere für Kurven und wieder andere für Knoten. Siehe auch [Basis Skizzierer Tutorium](Basic_Sketcher_Tutorial/de.md).

## Anwendung

1.  Erstelle eine Skizze entweder aus der <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Arbeitsbereich Skizzierer](Sketcher_Workbench/de.md) oder über die <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md).
2.  Drücke
    -   
        **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Skizzierer NeueSkizze](Sketcher_NewSketch/de.md)**
        
        , oder

    -   
        **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body.md)**
        
        gefolgt von **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NeueSkizze](PartDesign_NewSketch/de.md)**.
3.  Doppelklicke auf die erstellte Skizze, um den Bearbeitungsmodus aufzurufen.
4.  Zeichne eine Reihe von Linien mit **<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Polylinie erstellen](Sketcher_CreatePolyline/de.md)**.
5.  Wähle eine der Linien aus, und verwende **<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Beschränke vertikal](Sketcher_ConstrainVertical/de.md)**.
6.  Wähle eine der Linien aus, und verwende **<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Beschränke horizontal](Sketcher_ConstrainHorizontal.md)**.
7.  Wähle die vertikale Linie und verwende **<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Beschränke Abstand Y](Sketcher_ConstrainDistanceY.md)**; weise einen Abstand zu.
8.  Wähle die horizontale Linie, und verwende **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Beschränke Abstand X](Sketcher_ConstrainDistanceX.md)**; weise einen Abstand zu.

## Hinweise

-   Beschränkungen sind nützlich, um sehr präzise Profile zu erstellen, die in feste Extrusionen umgewandelt werden können durch verwenden von **<img src=images/PartDesign_Pad.svg style="width:16px"> <img src=images/Part_Extrude.svg style="width:PartDesign Polster](PartDesign_Pad/de.md)** oder **[16px"> [Part Extrudieren](Part_Extrude/de.md)** Arbeitsgänge.
-   Beschränkungen werden nur innerhalb von [Skizzen](Sketch/de.md) verwendet; andere 2D Objekte, wie die mit <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereich](Draft_Workbench/de.md) erzeugten verstehen nichts von Beschränkungen; letztere werden einfach im 3D-Raum platziert, und ihre Eigenschaften definieren ihre Form und Position.


{{Sketcher Tools navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)

---
[documentation index](../README.md) > [Glossary](Category:Glossary.md) > Constraint/de
