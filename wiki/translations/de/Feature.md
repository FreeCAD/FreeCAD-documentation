

## Einleitung

In FreeCAD wird das Wort \"[Formelement](Feature/de.md)\" normalerweise verwendet, um sich auf eine [PartDesign Formelement](PartDesign_Feature/de.md) Objekt (`PartDesign::Feature` Klasse) zu beziehen, die von der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) definiert wird. Dies ist eine Operation oder ein Modellierungsschritt ausgeführt zum Erstellen oder Ändern eines Volumenkörpers [Form](Shape/de.md) nach dem [Formelementbearbeitungs](feature_editing/de.md) Paradigma.

Siehe [PartDesign Formelement](PartDesign_Feature/de.md) für weitere Informationen über diesen Objekttyp.

## Anwendung

1.  Wechsle zum <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesignArbeitsbereich](PartDesign_Workbench/de.md).
2.  Drücke **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**.
3.  Drücke **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NeueSkizze](PartDesign_NewSketch.md)**, um eine neue [Skizze](Sketch/de.md) zu erstellen.
4.  Erstelle einen geschlossenen Draht und verwende dann **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Polster](PartDesign_Pad/de.md)** um die Skizze zu extrudieren und einen ersten Volumenkörper zu erzeugen. Dieser Anfangs Volumenkörper ist das anfängliche Formelement.
5.  Füge weitere Skizzen und Polster hinzu, und verwende andere Werkzeuge des [PartDesign Arbeitsbereichs](PartDesign_Workbench/de.md), um den ursprünglichen Volumenkörper zu ändern und umzuwandeln. Jeder dieser Schritte entspricht den Formelementen der [Körper](Body/de.md).
6.  Alternativ können primitive Objekte wie **<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> <img src=images/PartDesign_SubtractiveCylinder.svg style="width:PartDesign Hinzuzufügender Quader](PartDesign_AdditiveBox/de.md)** und **[16px"> [PartDesign Abzuziehender Zylinder](PartDesign_SubtractiveCylinder/de.md)**. Jede Anzahl von hinzuzufügenden und abzuziehenden Schritten sind Formelemente, die zur Erzeugung eines Endvolumens verwendet werden.

## Hinweise

Im allgemeinen Verständnis kann ein \"Formelement\" jeder Modellierungsschritt sein, der zur Erstellung einer endgültigen [Form](Shape/de.md) mit einem beliebigen Werkzeug eines beliebigen [Arbeitsbereichs](Workbenches/de.md) verwendet werden.

-   Zum Beispiel im <img src=images/Part_Fuse.svg style="width:Part Arbeitsbereich](Part_Workbench/de.md), im [konstruktive Volumenkörpergeometrie](constructive_solid_geometry/de.md) Arbeitsablauf kann ein \"Formelement\" eine beliebige boolesche Operation sein, wie {{Button[16px"> <img src=images/Part_Cut.svg style="width:Part Verschmelzung](Part_Fuse/de.md)}}, **[16px"> <img src=images/Part_Common.svg style="width:Part Schnitt](Part_Cut.md)**, oder **[16px"> [Part Schnittmenge](Part_Common/de.md)**.

In einem genaueren Verständnis ist ein \"Formelement\" ein Modellierungsschritt, der innerhalb eines [PartDesign Körper](PartDesign_Body/de.md) verwendet wird.

-   Zum Beispiel: **<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> <img src=images/PartDesign_AdditiveLoft.svg style="width:PartDesign Hinzuzufügender Zylinder](PartDesign_AdditiveCylinder/de.md)**, **[16px"> <img src=images/PartDesign_Pocket.svg style="width:PartDesign Hinzuzufügende Ausformung](PartDesign_AdditiveLoft/de.md)**, **[16px"> <img src=images/PartDesign_SubtractiveCone.svg style="width:PartDesign Tasche](PartDesign_Pocket/de.md)**, **[16px"> [PartDesign Abzuziehender Kegel](PartDesign_SubtractiveCone.md)**, usw., sind alles \"Formelemente\".


{{PartDesign Tools navi

}}  {{Document objects navi}} 

[Category:Glossary{{\#translation:}}](Category:Glossary.md)
