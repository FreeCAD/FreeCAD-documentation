---
 GuiCommand:
   Name: Arch MergeWalls
   Name/de: Arch WändeVerbinden
   MenuLocation: Utils , Wände Zusammenfügen
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_Wall/de
---

# Arch MergeWalls/de



## Beschreibung

Das Werkzeug [WändeVerbinden](Arch_MergeWalls/de.md) fügt [Arch-Wände](Arch_Wall/de.md) zusammen.



## Anwendung

1.  Eine der folgenden Möglichkeiten ausführen:
    -   Eine einzelne Wand mit einer oder mehreren [Komponenten](Arch_Add/de.md), die auch Wände sind, auswählen.
    -   Zwei oder mehr Wände auswählen.
2.  In beiden Fällen müssen die {{PropertyData/de|Height}}, {{PropertyData/de|Width}} und {{PropertyData/de|Align}} der Wände identisch sein.
3.  Den Menüeintrag **Utils → <img src="images/Arch_MergeWalls.svg" width=16px> Wände zusammenfügen** auswählen.



## Hinweise

-   [Arch Hinzufügen](Arch_Add/de.md) kann Wände zusammenführen, auch wenn sie unterschiedlich hoch, unterschiedlich breit und unterschiedlich ausgerichtet sind.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Dieses Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch folgende Funktion verwendet werden:


```python
base = joinWalls(walls, delete=False)
```

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

base = Arch.joinWalls([Wall1, Wall2])
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch MergeWalls/de
