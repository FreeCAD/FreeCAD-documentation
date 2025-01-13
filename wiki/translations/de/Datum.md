# Datum/de
## Einleitung

In FreeCAD wird das Wort \"[Bezugselement](Datum/de.md)\" normalerweise verwendet, um sich auf Hilfsgeometrie im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) zu beziehen. Diese geometrischen Elemente sind kein Bestandteil der endgültigen [Form](Shape/de.md) eines [Körpers](Body/de.md), können aber als Referenzen und als Befestigungsmöglichkeiten für [Skizzen](Sketch/de.md) und andere Arten von [Formelementen](Feature/de.md) verwendet werden.

Die folgenden entsprechen Elementen, die von der Klasse `Part::Datum` abgeleitet sind, die wiederum selbst von [Part Formelement](Part_Feature/de.md) abgeleitet ist:

-   [PartDesign Punkt](PartDesign_Point/de.md)
-   [PartDesign Linie](PartDesign_Line/de.md)
-   [PartDesign Ebene](PartDesign_Plane/de.md)
-   [PartDesign Koordinatensystem](PartDesign_CoordinateSystem/de.md)

Die folgenden sind direkt von [Part Formelement](Part_Feature/de.md) abgeleitet:

-   [PartDesign Formbinder](PartDesign_ShapeBinder/de.md)
-   [PartDesign Teilformbinder](PartDesign_SubShapeBinder/de.md)



## Anwendung

1.  Zum Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) wechseln.
2.  Die Schaltfläche **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper erstellen](PartDesign_Body/de.md)** drücken.
3.  Den Ursprung des Körpers auswählen und durch Drücken der **Leertaste** sichtbar schalten.
4.  Die Schaltfläche **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Ebene](PartDesign_Plane/de.md)** drücken, um das [Aufgaben-Fenster](task_panel/de.md) Parameter der Bezugsebene zu öffnen.
5.  In der [3D-Ansicht](3D_view/de.md) eine der Standardebenen anklicken, z.B. die XY-Ebene. Dann **OK** drücken, um das Aufgaben-Fenster zu schließen.
6.  Jetzt in der [Baumansicht](tree_view/de.md) die neu erstellte Bezugsebene auswählen und dann **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Skizze erstellen](PartDesign_NewSketch/de.md)** drücken.
7.  Einen geschlossenen Linienzug erstellen und dann **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Block](PartDesign_Pad/de.md)** um die Skizze zu extrudieren und einen ersten Festkörper zu erzeugen.

Jetzt kann die Bezugsebene beliebig verschoben und gedreht werden, indem ihre Eigenschaften im [Eigenschafteneditor](property_editor/de.md) angepasst werden; die Skizze und der Festkörper folgen der neuen [Positionierung](Placement/de.md).

Es können andere Arten von Bezugselementen hinzugefügt werden, die mit anderen Skizzen und Formelementen verwendet werden.



## Hinweise

Seit ihrem Erscheinen in v0.17 waren Bezugsobjekte für die Verwendung innerhalb von [PartDesign Körpern](PartDesign_Body/de.md) vorgesehen. Da es sich jedoch um nützliche \"Referenz\"-Objekte mit unterschiedlichen [Befestigungsmethoden](Part_EditAttachment/de.md) handelt, wurde vorgeschlagen, dass sie außerhalb der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) zur Verfügung stehen sollten. Auf diese Weise wären sie in allen Arbeitsbereichen als Geometrie zum Befestigen verwendbar, insbesondere im Zusammenhang mit der Erstellung von [Baugruppen](Assembly/de.md).

-   [Create and display local coordinate system](https://forum.freecadweb.org/viewtopic.php?f=10&t=2604)
-   [Datum objects in App::Part](https://forum.freecadweb.org/viewtopic.php?f=22&t=33654)
-   [Structure toolbar and datums](https://forum.freecadweb.org/viewtopic.php?t=42759)
-   [Local CS cannot be used in Part Wb?](https://forum.freecadweb.org/viewtopic.php?f=3&t=42960)


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Datum/de
