# Datum/de
## Einführung

In FreeCAD wird das Wort \"[Bezugsebene](Datum/de.md)\" normalerweise verwendet, um sich auf Hilfsgeometrie im [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) zu beziehen. Diese geometrischen Elemente bilden kein Teil der endgültigen [Form](Shape/de.md) des [Körpers](Body/de.md), können aber als Referenzen und als Unterstützung für [Skizzen](Sketch/de.md) und andere Arten von [Formelementen](Feature/de.md) verwendet werden.

Die folgenden stimmen mit Elementen überein, die von der `Part::Datum` Klasse abgeleitet, selbst abgeleitet von [Part Formelemente](Part_Feature/de.md) abgeleitet sind:

-   [PartDesign Punkt](PartDesign_Point/de.md)
-   [PartDesign Linie](PartDesign_Line/de.md)
-   [PartDesign Ebene](PartDesign_Plane/de.md)
-   [PartDesign KoordinatenSystem](PartDesign_CoordinateSystem/de.md)

Die Folgenden sind direkt abgeleitet von [Part Formelement](Part_Feature/de.md):

-   [PartDesign FormBinder](PartDesign_ShapeBinder/de.md)
-   [PartDesign UnterFormBinder](PartDesign_SubShapeBinder/de.md)

## Anwendung

1.  Wechsle zum [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md).
2.  Drücke **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**.
3.  Wähle den Ursprung des Körpers und mache ihn durch Drücken der **Leertaste** Leiste deiner Tastatur sichtbar.
4.  Drücke **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Ebene](PartDesign_Plane/de.md)** um die Ebene [Audfgabenpaneel](task_panel/de.md) zu öffnen.
5.  In der [3D Ansicht](3D_view/de.md), klicke auf eine der Standardebenen, z.B. die XY Ebene. Drücke dann **OK** um das Aufgabenpaneel zu schließen.
6.  Wähle nun in der [Baumansicht](tree_view/de.md), die neu erstellte BezugsEbene aus, und drücke dann **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NeueSkizze](PartDesign_NewSketch/de.md)**.
7.  Erstelle einen geschlossenen Draht und verwende dann **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Polster](PartDesign_Pad/de.md)** um die Skizze zu extrudieren und einen ersten Volumenkörper zu erzeugen.

Jetzt kannst du die BezugsEbene beliebig verschieben und drehen, indem du ihre Eigenschaften im [Eigenschaftseditor](property_editor/de.md) änderst, und die Skizze und das Polster folgen deiner neuen [Platzierung](Placement/de.md).

Du kannst andere Arten von Bezugspunkten hinzufügen, die mit anderen Skizzen und Formelementen verwendet werden können.

## Hinweise

Seit ihrem Erscheinen in v0.17 waren Bezugsobjekte für die Verwendung innerhalb von [PartDesign Körper](PartDesign_Body/de.md) vorgesehen. Da es sich jedoch um nützliche \"Referenz\" Objekte mit verschiedenen [Anhangmethoden](Part_EditAttachment/de.md) handelt, wurde vorgeschlagen, dass sie außerhalb der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) verfügbar sein sollten. Auf diese Weise werden sie in allen Arbeitsbereichen als tragende Geometrie verwendbar sein, insbesondere im Zusammenhang mit der Erstellung von [Baugruppen](Assembly/de.md).

-   [Lokales Koordinatensystem erstellen und anzeigen](https://forum.freecadweb.org/viewtopic.php?f=10&t=2604)
-   [Datumsobjekte in App::Part](https://forum.freecadweb.org/viewtopic.php?f=22&t=33654)
-   [Struktur-Werkzeugleiste und Bezugspunkte](https://forum.freecadweb.org/viewtopic.php?t=42759)
-   [Lokale CS kann nicht im Part Arbeitsbereich verwendet werden?](https://forum.freecadweb.org/viewtopic.php?f=3&t=42960)


{{PartDesign Tools navi

}} {{Document objects navi}} 

[<img src="images/Property.png" style="width:16px"> Glossary](Category_Glossary.md)

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Datum/de
