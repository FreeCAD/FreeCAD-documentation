---
- GuiCommand:
   Name:Arch Reference
   Name/de:Arch Referenz
   MenuLocation:Arch → Referenz
   Workbenches:[Arch Arbeitsbereich](Arch_Workbench/de.md)
   Shortcut:
   SeeAlso:[Arch GebäudeTeil](Arch_BuildingPart/de.md)
---

# Arch Reference/de

## Beschreibung

<img alt="" src=images/Arch_reference_screenshot.png  style="width:800px;">

Das Referenz Werkzeug erlaubt es, im aktuellen Dokument ein Objekt zu platzieren, das die Form und Farben eines in einer anderen Datei gespeicherten [Part](Part_Workbench/de.md) basierten Objekts (einschließlich [Arch Gebäudeteil](Arch_BuildingPart/de.md)) kopiert. Wenn sich die FreeCAD Datei ändert, wird das Objekt für eine Aktualisierung vorgemerkt.

## Anwendung

1.  Drücke die Schaltfläche **<img src="images/Arch_Reference.svg" width=16px> Arch Referenz
**
2.  Drücke die Schaltfläche **Wähle Datei...** und wähle eine vorhandene FreeCAD-Datei
3.  Wähle eins der enthaltenen Part-basierten Objekte aus der Aufklappliste
4.  Drücke **OK**

## Optionen

-   Das Referenz-Objekt kann bewegt und gedreht werden, die aktuelle Position wird bei einem Neuladen des Objekts beibehalten.
-   Falls das Original-Objekt in der externen Datei bewegt wird, wird sich diese Bewegung auf das Referenz-Objekt auswirken.
-   Bei Rechtsklick eines Referenz-Objekts in der Baumansicht hast du die Optionen, das Original-Objekt neuzuladen oder die externe Datei zu öffnen.
-   Um mehrere Objekte auf einmal zu referenzieren, platziere sie in einem [Arch Gebäudeteil](Arch_BuildingPart/de.md).
-   Beim Ausschalten der **Update Colors**-Eigenschaft der Referenz werden die Originalfarben nicht mehr neugeladen, so dass du sie gefahrlos ändern kannst.

## Eigenschaften

-    {{PropertyData/de|File}}: Die zugrunde liegende Datei, auf der diese Komponente basiert

-    {{PropertyData/de|Part}}: Das zu verwendende Teil aus der zugrunde liegenden Datei

-    {{PropertyView/de|Update Colors}}: Falls `True`, werden die Farben auf Basis der verbundenen Datei aktualisiert

## Programmierung

Das Referenz-Werkzeug kann in [Makros](macros/de.md) ebenso wie aus der Python-Konsole heraus mit folgender Funktion angesprochen werden: 
```python
makeReference ([file_path,object_name])
```

erstellt ein Referenz-Objekt aus dem angegebenen Objekt der angegebenen Datei.

Beispiel: 
```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd","myPart")
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Reference/de
