---
- GuiCommand:/ru
   Name/ru:Arch_PipeConnector
   Name:Arch_PipeConnector
   MenuLocation:Arch → Pipe Tools → Pipe Connector
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:**P** **C**
   Version:0.17
   SeeAlso:[Arch Pipe](Arch_Pipe/ru.md), [Оборудование](Arch_Equipment/ru.md)
---

# Arch PipeConnector/ru

## Описание


<div class="mw-translate-fuzzy">


<small>(v0.17)</small> 

Этот инструмент позволяет создавать углы или тройные соединения между двумя или тремя выбранными трубами/[Arch Pipes](Arch_Pipe.md).


</div>

## Применение


<div class="mw-translate-fuzzy">

Выберите 2 или 3 [Arch Pipes](Arch_Pipe.md). Если вы выбираете 3 трубы, два из них должны быть точно выровнены.

1.  Нажмите кнопку **<img src="images/Arch_PipeConnector.png" width=16px> [[Arch PipeConnector]]
** или нажмите **P**, затем **C**


</div>

## Свойства

-    **Radius**: Радиус кривизны этого соединителя

## Типичный рабочий процесс 


<div class="mw-translate-fuzzy">

См. [Arch Pipe#Typical_workflow](Arch_Pipe#Typical_workflow.md)


</div>

## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


<div class="mw-translate-fuzzy">

Инструмент «Коннектор труб» может использоваться в [макросах](Macros/ru.md) и на консоли python с помощью следующей функции:


</div>


```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```

-   Creates a `Connector` object from the given `pipes`, which is a list of [Arch Pipes](Arch_Pipe.md), and optionally a `radius` of curvature.
    -   The base objects ([Draft Wires](Draft_Wire.md)) of the [Arch Pipes](Arch_Pipe.md) should share an endpoint so they create a proper, smooth connector.

Пример: 
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



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch PipeConnector/ru
