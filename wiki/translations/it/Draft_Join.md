---
- GuiCommand:/it
   Name:Draft Join
   Name/it:Unisci
   MenuLocation:Draft → Unisci
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut:**J** **O**
   Version:0.18
   SeeAlso:[Dividi](Draft_Split/it.md)
---

# Draft Join/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Unisci tenta di unire tutti i contorni attualmente presenti nella selezione in un unico contorno.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare due o più contorni che si desidera unire.
2.  Premere il pulsante **<img src="images/Draft_Join.svg" width=16px> [Unisci](Draft_Join/it.md)** o premere i tasti **J** e poi **O**.


</div>

## Notes


<div class="mw-translate-fuzzy">

La controparte di questo strumento è l\'operazione <img alt="" src=images/Draft_Split.svg  style="width:16px;"> [Dividi](Draft_Split/it.md).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Unisci può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
join_wires(wires)
```

-    `wires`is a list of wire objects to be joined.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(500, 0, 0)
p3 = App.Vector(500, 500, 0)
p4 = App.Vector(0, 500, 0)

wire1 = Draft.make_wire([p1, p2])
wire2 = Draft.make_wire([p2, p3])
wire3 = Draft.make_wire([p3, p4])
wire4 = Draft.make_wire([p4, p1])

Draft.join_wires([wire1, wire3, wire2, wire4])
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Join/it
