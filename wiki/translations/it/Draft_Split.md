---
- GuiCommand   */it
   Name   *Draft Split
   Name/it   *Dividi
   MenuLocation   *Draft → Dividi
   Workbenches   *[Draft](Draft_Workbench/it.md)
   Shortcut   ***S** **P**
   Version   *0.18
   SeeAlso   *[Unisci](Draft_Join/it.md)
---

# Draft Split/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Split.svg  style="width   *16px;"> Dividi tenta di dividere un contorno esistente su uno spigolo o un punto specificato.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Split.svg" width=16px> [Dividi](Draft_Split/it.md)** o premere i tasti **S** e poi **P**.
2.  Cliccare su un contorno dove si vuole dividerlo.


</div>

## Notes


<div class="mw-translate-fuzzy">

La controparte di questo strumento è l\'operazione <img alt="" src=images/Draft_Join.svg  style="width   *16px;"> [Unisci](Draft_Join/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche   ***

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Dividi può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione   *


</div>


```python
split(wire, newPoint, edgeIndex)
```

-    `wire`the wire object to be split.

-    `newPoint`the point where the split should occur.

-    `edgeIndex`index of the edge where the split should occur (1-based).

Example   *


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(500, 0, 0)
p3 = App.Vector(250, 0, 0)

wire = Draft.make_wire([p1, p2])

Draft.split(wire, p3, 1)
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Split/it
