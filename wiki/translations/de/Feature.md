# Feature/de
## Einleitung

In FreeCAD wird das Wort \"[Formelement](Feature/de.md)\" normalerweise verwendet, um sich auf ein [PartDesign-Formelement](PartDesign_Feature/de.md)-Objekt (Klasse `PartDesign::Feature`) zu beziehen, das im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) definiert ist. Dies ist eine Operation oder ein Modellierungsschritt zum Erstellen oder Ändern einer Festkörper-[Form](Shape/de.md) nach dem Prinzip [Formelemente bearbeiten](feature_editing/de.md).

Siehe [PartDesign Formelement](PartDesign_Feature/de.md) für weitere Informationen über diese Objektart.



## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) wechseln.
2.  Die Schaltfläche **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper erstellen](PartDesign_Body/de.md)** drücken.
3.  Die Schaltfläche **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Skizze erstellen](PartDesign_NewSketch.md)** drücken, um eine neue [Skizze](Sketch/de.md) zu erstellen.
4.  Einen geschlossenen Linienzug erstellen und dann die Schaltfläche **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad/de.md)** drücken, um die Skizze zu extrudieren und einen ersten Festkörper zu erstellen. Dieser erste Festkörper ist das Anfangsformelement.
5.  Weitere Skizzen hinzufügen und mit anderen Werkzeuge des Arbeitsbereichs [PartDesign](PartDesign_Workbench/de.md) verwenden, um den ursprünglichen Festkörper zu ändern und in Mustern anzuordnen. Alle diese Schritte entsprechen Formelementen des [Körpers](Body/de.md).
6.  Alternativ können Grundkörper-Objekte hinzugefügt werden, wie **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [PartDesign Quader](PartDesign_AdditiveBox/de.md)** und abzuziehende **[<img src=images/PartDesign_SubtractiveCylinder.svg style="width:16px"> [PartDesign Zylinder](PartDesign_SubtractiveCylinder/de.md)**. Jeder Schritt zum Hinzufügen und Abziehen entspricht einem Formelement, das zum Erstellen eines endgültigen Volumens verwendet wird.



## Hinweise

Nach allgemeinem Verständnis kann ein \"Formelement\" jeder Modellierungsschritt sein, der zum Erstellen einer endgültigen [Form](Shape/de.md) mit einem beliebigen Werkzeug eines beliebigen [Arbeitsbereichs](Workbenches/de.md) erfolgt.

-   Zum Beispiel kann im Arbeitsbereich [Part](Part_Workbench/de.md) im Arbeitsablauf nach dem Prinzip [Konstruktive Festkörpergeometrie](constructive_solid_geometry/de.md) ein \"Formelement\" eine beliebige boolesche Verknüpfung sein, wie **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Vereinigung](Part_Fuse/de.md)**, **[<img src=images/Part_Cut.svg style="width:16px"> [Part Differenz](Part_Cut.md)**, oder **[<img src=images/Part_Common.svg style="width:16px"> [Part Schnitt](Part_Common/de.md)**.

Im engeren Sinn ist ein \"Formelement\" ein Modellierungsschritt, der innerhalb eines [PartDesign Körpers](PartDesign_Body/de.md) verwendet wird.

-   Zum Beispiel: **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Zylinder](PartDesign_AdditiveCylinder/de.md)**, **[<img src=images/PartDesign_AdditiveLoft.svg style="width:16px"> [PartDesign Ausformung](PartDesign_AdditiveLoft/de.md)**, **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [PartDesign Vertiefung](PartDesign_Pocket/de.md)**, **[<img src=images/PartDesign_SubtractiveCone.svg style="width:16px"> abzuziehender [PartDesign Kegel](PartDesign_SubtractiveCone.md)** usw. sind alle \"Formelemente\".


{{PartDesign Tools navi

}}  {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Feature/de
