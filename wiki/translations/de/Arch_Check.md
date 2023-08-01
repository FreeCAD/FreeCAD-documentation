---
- GuiCommand:/de
   Name:Arch Check
   Name/de:Arch Überprüfen
   Workbenches:[Arch](Arch_Workbench/de.md)
   MenuLocation:Arch → Dienstprogramme → Überprüfen
   SeeAlso:[Arch SchließeLöcher](Arch_CloseHoles/de.md)
---

# Arch Check/de



## Beschreibung

Dieses Werkzeug prüft das aktuelle Dokument oder die ausgewählten Objekte auf Nicht-Volumenkörper **<img src="images/_Workbench_Part.svg" width=16px> [Part](Part_Workbench/de.md)**- oder **<img src="images/_Workbench_Arch.svg" width=16px> [Arch](Arch_Workbench.md)**-Objekte, die Probleme bereiten könnten, da die meisten Operationen des Arch-Arbeitsbereichs Volumenkörper erfordern.



## Anwendung

1.  Drücke die **<img src="images/Arch_Check.svg" width=16px>[Überprüfung](Arch_Check/de.md)** Schaltfläche oder **Arch** → **Dienstprogramme** → **<img src="images/Arch_Check.svg" width=16px> [Überprüfung](Arch_Check/de.md)** im oberen Menü.




<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Dieses Werkzeug kann in [Makros](macros/de.md) und von der [Python](Python/de.md) Konsole aus mit der folgenden Funktion verwendet werden:


</div>


```python
list_bad = check(objectslist, includehidden=False)
```

-   Prüft, ob es sich bei allen angegebenen Objekten in `objectslist` um Volumenkörper (solids) handelt.
-   Wenn `includehidden` den Wert `True` hat, werden auch alle versteckten Objekte berücksichtigt, anderenfalls von der Suche ausgenommen.
-   Liefert in `list_bad` eine Liste mit Objekten zurück, die nicht von einem `Part::Feature` abgeleitet sind oder Komponenten, die nicht geschlossen, nicht valide sind, keine Volumenkörper sind oder die Flächen enthalten, die nicht Teil irgendeines Volumenkörpers sind. Diese Liste wird im [Arch](Arch_Workbench/de.md)- oder [Draft](Draft_Workbench/de.md)-Arbeitsbereich genutzt, um Linienzüge und Profile zu erkennen, die keine Volumenkörper sind.
    -   Jedes Element in `list_bad` ist eine weitere Liste `object, message`, wobei `object` der erkannte nicht-Volumenkörper ist und `message` den Grund angibt, warum er in dieser Liste enthalten ist.

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
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Check/de
