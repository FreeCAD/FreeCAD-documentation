---
- GuiCommand:/de
   Name:Arch Project
   Name/de:Architektur Projekt
   MenuLocation:Architektur → Projekt
   Workbenches:[Arch-Arbeitsbereich](Arch_Workbecnch.md)
   Shortcut:**P** **O**/de
   SeeAlso:[Architektur Grundstück](Arch_Site/de.md), [Architektur Gebäude](Arch_Building/de.md)
---

# Arch Project/de

## Beschreibung

Das Arch Projekt ist ein spezielles Objekt, das geeignet ist, eine bessere Kompatibilität mit [IFC](Arch_IFC/de.md) Dateien hinzuzufügen. Jede IFC Datei muss eine [IfcProject](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/schema/ifckernel/lexical/ifcproject.htm) Einheit enthalten. Das IfcProjekt wird meist verwendet, um allgemeine Projekteinstellungen wie Projektionssysteme, für GIS Kompatibilität oder Einheitensysteme zu definieren.

Wenn ein FreeCAD Modell in das IFC Dateiformat exportiert wird und dein Modell kein Projekt Objekt enthält, wird automatisch ein Standardobjekt erstellt, was in den meisten Fällen ausreichend ist. Möglicherweise möchtest du jedoch in der Lage sein, die Projekteinstellungen fein abzustimmen, in diesem Fall kann das Hinzufügen eines Projekt Objektes nützlich sein. Wenn eine IFC Datei importiert wird, wird immer ein Projekt Objekt erstellt. Wenn es jedoch nicht ausdrücklich verwendet wird, kannst du es nach dem Import einfach löschen.

Beachte, dass zwar jedes andere BIM Objekt zu einem Projekt hinzugefügt werden kann, was der IFC Standard nicht verbietet, die übliche Vorgehensweise jedoch immer darin besteht, nur [Standorte](Arch_Site/de.md) oder [Gebäude](Arch_Building/de.md) als direkte Kinder eines Projekts zu haben. Alle anderen BIM Objekte sollten sich innerhalb dieser Standorte oder Gebäude befinden. Das Projekt selbst sollte immer an der Spitze Ihrer Modellstruktur stehen, d.h. es sollte in keinem anderen Objekt enthalten sein.

## Anwendung

1.  Drücke die **<img src="images/Arch_Project.svg" width=16px> [Arch Projekt](Arch_Project/de.md)** Taste oder drücke die Tasten**P** und dann **O**.
2.  Füge deinem Projekt ein beliebiges Objekt hinzu, indem du es per Ziehen & Ablegen auf das Projekt in der [Baumansicht](Tree_view/de.md) ziehst.

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Project/de
