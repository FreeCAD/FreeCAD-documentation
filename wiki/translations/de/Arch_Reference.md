---
 GuiCommand:
   Name: Arch Reference
   Name/de: Arch Referenz
   MenuLocation: 3D/BIM , Generic 3D tools , Externe Referenz
   Workbenches: BIM_Workbench/de
   Shortcut: 
   SeeAlso: 
---

# Arch Reference/de



## Beschreibung

Das Werkzeug **Arch Referenz** ermöglicht im aktuellen Dokument ein Objekt zu platzieren, das die Form und Farben eines in einer anderen Datei gespeicherten [Part](Part_Workbench/de.md)-basierten Objekts (einschließlich [Arch Gebäudeteil](Arch_BuildingPart/de.md)) kopiert. Wenn sich die FreeCAD-Datei ändert, wird das Objekt für eine Aktualisierung vorgemerkt.

<img alt="" src=images/Arch_reference_screenshot.png  style="width:600px;">



## Anwendung

1.  Die Schaltfläche **<img src="images/Arch_Reference.svg" width=16px> [ExterneReferenz](Arch_Reference/de.md)** drücken.

2.  Die Schaltfläche **Datei auswählen...** drücken und eine vorhandene FreeCAD-Datei auswählen.

3.  Eins der enthaltenen auf Part basierenden Objekte in der Aufklappliste auswählen.

4.  
    **OK**drücken.



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



## Skripten

Das Werkzeug Referenz kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch Verwendung der folgenden Funktion verwendet werden:


```python
reference = makeReference([filepath], [partname], [name])
```

erstellt ein Objekt `reference` mit dem Namen `name` vom Objekt `partname` in der Datei `filepath`. Alle Argumente sind optional.

Beispiel:


```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd", "myPart")
```



---
⏵ [documentation index](../README.md) > Arch Reference/de
