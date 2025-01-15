---
 GuiCommand:
   Name: Arch PipeConnector
   Name/pl: Architektura: Kształtka
   MenuLocation: 3D / BIM , Kształtka
   Workbenches: BIM_Workbench/pl
   Shortcut: **P** **C**
   Version: 0.17
   SeeAlso: 
---

# Arch PipeConnector/pl



## Opis

Narzędzie **Kształtka** pozwala na tworzenie połączeń kątowych lub trójnikowych pomiędzy dwoma lub trzema wybranymi [rurami](Arch_Pipe/pl.md).



## Użycie

1.  Wybierz 2 lub 3 [rury](Arch_Pipe/pl.md). Jeśli wybierasz 3 rury, dwie z nich muszą być dokładnie wyrównane.
2.  Naciśnij przycisk **<img src="images/Arch_PipeConnector.svg" width=16px> '''Kształtka'''** lub naciśnij **P**, a następnie **C**.



## Właściwości

-    **Promień**: Promień krzywizny tego złącza.



## Typowy przepływ pracy 

Zobacz informacje na temat [rura](Arch_Pipe/pl.md) w celu zapoznania się z przepływem pracy dotyczącym używania rur i tworzenia połączeń.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Kształtka** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Connector = makePipeConnector(pipes, radius=0, name="Connector")
```

-   Tworzy obiekt `Connector` z podanego `pipes`, który jest listą [rur](Arch_Pipe/pl.md) i opcjonalnie `radius` krzywizny.
    -   Obiekty bazowe ([polilinii](Draft_Wire/pl.md)) [rur](Arch_Pipe/pl.md) powinny mieć wspólny punkt końcowy, aby utworzyć odpowiednie, gładkie połączenie.

Przykład:


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
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch PipeConnector/pl
