---
 GuiCommand:
   Name: Arch Check
   Name/de: Arch Überprüfen
   MenuLocation: Utils , Check
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_CloseHoles/de
---

# Arch Check/de



## Beschreibung

Dieses Werkzeug prüft das aktuelle Dokument oder die ausgewählten Objekte auf [Part](Part_Workbench/de.md)- oder [BIM](BIM_Workbench/de.md)-Objekte, die keine Festkörper sind und Probleme bereiten könnten, da die meisten Operationen des Arbeitsbereichs BIM Festkörper erfordern.



## Anwendung

1.  Den Menüeintrag **Utils → <img src="images/Arch_Check.svg" width=16px> Check** auswählen.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden: 
```python
list_bad = check(objectslist, includehidden=False)
```

-   Prüft, ob alle in `objectslist` enthaltenen Objekte Festkörper (solids) sind.
-   Hat `includehidden` den Wert `True`, werden auch alle ausgeblendeten Objekte berücksichtigt, anderenfalls werden sie von der Suche ausgenommen.
-   Gibt `list_bad` zurück, eine Liste mit Objekten, die nicht von einem `Part::Feature` abgeleitet sind oder Komponenten, die nicht geschlossen, nicht gültig oder keine Festkörper sind oder die Flächen enthalten, die nicht Teil irgendeines Festkörpers sind. Diese Liste wird eingesetzt, um Linienzüge sowie Profile der Arbeitsbereiche [BIM](BIM_Workbench/de.md) oder [Draft](Draft_Workbench/de.md) zu erkennen, die keine Festkörper sind.
    -   Jedes Element in `list_bad` ist eine weitere Liste `[object, message]`, wobei `object` der erkannte nicht-Festkörper ist und `message` den Grund angibt, warum er in dieser Liste enthalten ist.

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```



---
⏵ [documentation index](../README.md) > Arch Check/de
