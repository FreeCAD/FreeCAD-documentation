# Body/de


## Einleitung

In FreeCAD wird das Wort \"[Körper](Body/de.md)\" normalerweise verwendet, um sich auf ein [PartDesign Körper](PartDesign_Body/de.md) Objekt (`PartDesign::Body` Klasse ) zu beziehen, das vom [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) definiert wird. Dies ist ein Behälterobjekt, das [2D Skizzen](Sketch/de.md) und [3D geometrische Formelemente](PartDesign_Feature/de.md) aufnehmen kann, um eine Volumenkörperform zu erstellen.

Siehe [PartDesign Körper](PartDesign_Body/de.md) für weitere Informationen über diesen Objekttyp.

## Verwendung

1.  Wechsle zum [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md).
2.  Drücke **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**.
3.  Drücke **<img src=images/PartDesign_NewSketch.svg style="width:16px">. [PartDesign NeueSkizze](PartDesign_NewSketch/de.md)**, um eine neue [ Skizze](Sketch/de.md) zu erstellen.
4.  Erstelle einen geschlossenen Draht und verwende dann **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Polster](PartDesign_Pad/de.md)**, um die Skizze zu extrudieren und einen ersten Volumenkörper zu erstellen.
5.  Füge weitere Skizzen und Polster hinzu, und verwende andere Werkzeuge des [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md), um den ersten Volumenkörper zu ändern und umzuwandeln.

Alternativ kannst Du statt <img src=images/PartDesign_AdditiveBox.svg style="width:Skizzen](Sketch/de.md) auch primitive [PartDesign Formelemente](PartDesign_Feature/de.md) hinzufügen, zum Beispiel eine **[16px"> [PartDesign HinzuzufügenderQuader](PartDesign_AdditiveBox/de.md)**. Eine beliebige Anzahl hinzuzufügender und abzuziehender Funktionselemente kann zur Erstellung eines Endvolumens verwendet werden.

## Hinweise

Ein Körper ist erforderlich, wenn der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) in einer [Funktionselementbearbeitungs](feature_editing/de.md) Methodik verwendet wird.

Ein Körper ist nicht erforderlich, wenn der [Part Arbeitsbereich](Part_Workbench/de.md) verwendet wird, da dieser Arbeitsbereich einen [Konstructive Voumenkörpergeometrie](constructive_solid_geometry/de.md) Arbeitsablauf verwendet, der auf [Primitivformen](Part_Primitives/de.md) und booleschen Operationen basiert.


{{PartDesign Tools navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
