---
 GuiCommand:
   Name: Arch PipeConnector
   Name/de: Arch RohrVerbinder
   MenuLocation: Arch , Pipe tools , Rohr Verbinder
   Workbenches: Arch_Workbench/de
   Shortcut: **P** **C**
   Version: 0.17
   SeeAlso: Arch_Pipe/de, Arch_Equipment/de
---

# Arch PipeConnector/de

## Beschreibung


<div class="mw-translate-fuzzy">

Dieses Werkzeug ermöglicht eine Eck- oder T-Stück Verbindung zwischen zwei oder drei ausgewählten [Arch Rohre](Arch_Pipe/de.md) erstellen.


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle 2 oder 3 [Arch Rohre](Arch_Pipe/de.md). Wenn du 3 Rohre auswählst, müssen zwei davon exakt ausgerichtet sein.
2.  Drücke die **<img src="images/Arch_PipeConnector.svg" width=16px> [Arch RohrVerbinder](Arch_PipeConnector/de.md)** Schaltfläche oder drücke die **P** und dann **C** Tasten.


</div>

## Eigenschaften

-    **Radius**: Der Krümmungsradius dieses Verbinders

## Typischer Arbeitsablauf 


<div class="mw-translate-fuzzy">

Siehe die Information auf [Arch Rohr](Arch_Pipe/de.md) für den Arbeitsablauf zur Verwendung von Rohren und der Erstellung von Verbindungen.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Werkzeug Rohrverbinder kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole verwendet werden, durch anwenden der folgende Funktion:


</div>


```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```


<div class="mw-translate-fuzzy">

-   Erstellt ein `Verbinder` Objekt aus den gegebenen `Rohren`, die eine Liste von [Arch Rohren](Arch_Pipe/de.md) ist, und wahlweise einen `radius` der Krümmung.
    -   Die Basisobjekte ([Entwurf Drahte](Draft_Wire/de.md)) der [Arch Rohre](Arch_Pipe/de.md) sollten einen gemeinsamen Endpunkt haben, so dass sie einen sauberen, glatten Verbinder bilden.


</div>

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


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/de
