---
 GuiCommand:
   Name: Arch PipeConnector
   Name/de: Arch Rohrverbinder
   MenuLocation: 3D/BIM , Verbinder
   Workbenches: BIM_Workbench/de
   Shortcut: **P** **C**
   Version: 0.17
   SeeAlso: 
---

# Arch PipeConnector/de



## Beschreibung

Das Werkzeug **Arch Rohrverbinder** ermöglicht eine Eck- oder T-Stück-Verbindung zwischen zwei oder drei ausgewählten [Arch Rohren](Arch_Pipe/de.md) zu erstellen.



## Anwendung

1.  2 oder 3 [Arch Rohre](Arch_Pipe/de.md) auswählen. Werden 3 Rohre ausgewählt, müssen zwei davon kollinear ausgerichtet sein.
2.  Die Schaltfläche **<img src="images/Arch_PipeConnector.svg" width=16px> [Verbinder](Arch_PipeConnector/de.md)** drücken oder das Tastaturkürzel **P** dann **C**.



## Eigenschaften

-    **Radius**: Der Krümmungsradius dieses Verbinders



## Typischer Arbeitsablauf 

Siehe die Information auf [Arch Rohr](Arch_Pipe/de.md) für den Arbeitsablauf zur Verwendung von Rohren und der Erstellung von Verbindungen.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Rohrverbinder kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit folgender Funktion verwendet werden:


```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```

-   Erstellt ein `Connector`-Objekt aus den gegebenen `pipes`, eine Liste von [Arch Rohren](Arch_Pipe/de.md), und wahlweise einen Krümmungsradius `radius`.
    -   Die Basisobjekte ([Draft Linienzüge](Draft_Wire/de.md)) der [Arch Rohre](Arch_Pipe/de.md) sollten einen gemeinsamen Endpunkt haben, so dass sie einen sauberen, glatten Verbinder ergeben.

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(-1000, 0, 0)
p2 = FreeCAD.Vector(-2000, 0, 0)
p3 = FreeCAD.Vector(-2000, 0, 0)
p4 = FreeCAD.Vector(-2000, -1000, 0)
p5 = FreeCAD.Vector(-2000, -1000, 0)
p6 = FreeCAD.Vector(-4000, -1000, 0)
Line1 = Draft.makeWire([p1, p2])
Line2 = Draft.makeWire([p3, p4])
Line3 = Draft.makeWire([p5, p6])

Pipe1 = Arch.makePipe(Line1, 150)
Pipe2 = Arch.makePipe(Line2, 150)
Pipe3 = Arch.makePipe(Line3, 150)
FreeCAD.ActiveDocument.recompute()

Conn = Arch.makePipeConnector([Pipe1, Pipe2])
Conn2 = Arch.makePipeConnector([Pipe2, Pipe3])
FreeCAD.ActiveDocument.recompute()

Line4 = Draft.move(Line1, FreeCAD.Vector(-500, 1000, 0), copy=True)
Line5 = Draft.move(Line2, FreeCAD.Vector(-500, 1000, 0), copy=True)
Pipe4 = Arch.makePipe(Line4, 100)
Pipe5 = Arch.makePipe(Line5, 100)
FreeCAD.ActiveDocument.recompute()

Conn3 = Arch.makePipeConnector([Pipe4, Pipe5], radius=400)
FreeCAD.ActiveDocument.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch PipeConnector/de
