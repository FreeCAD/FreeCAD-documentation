---
- GuiCommand:/it
   Name:Draft Upgrade
   Name/it:Promuovi
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Promuovi
   Shortcut:**U** **P**
   SeeAlso:[Declassa](Draft_Downgrade/it.md), [Unione di Part](Part_Union/it.md)
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Upgrade.svg  style="width:16px;"> Promuovi converte più oggetti in un unico oggetto di livello superiore in diversi modi.


</div>

<img alt="" src=images/Draft_Upgrade_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">


*Contorno aperto promosso in contorno chiuso, e quindi in una faccia; un quadrato chiuso promosso in faccia e quindi fuso con la faccia precedente*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti che si desidera declassare.
2.  Premere il pulsante **<img src="images/Draft_Upgrade.svg" width=16px> [Promuovi](Draft_Upgrade/it.md)** o premere i tasti **U** e **P**. Se nessun oggetto è selezionato, si viene invitati a selezionarne uno.


</div>

## Notes

-   [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md) can be joined with this command, but also with the [Draft Join](Draft_Join.md) command or the [Draft Wire](Draft_Wire.md) command.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Promuovi può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
upgrade_list = upgrade(objects, delete=False, force=None)
```


<div class="mw-translate-fuzzy">

-   Eleva di grado il dato `objects`, che può essere un oggetto o un elenco di oggetti.
-   Se `delete` è `True`, i vecchi oggetti vengono eliminati.
-   Se `force` è dato, viene usato per forzare un certo tipo di promozione. Esso può essere: `"makeCompound"`, `"closeGroupWires"`, `"makeSolid"`, `"closeWire"`, `"turnToParts"`, `"makeFusion"`, `"makeShell"`, `"makeFaces"`, `"draftify"`, `"joinFaces"`, `"makeSketchFace"`, `"makeWires"`, o `"turnToLine"`.
-   Restituisce una `upgrade_list`, che è una lista contenente due liste: una lista di nuovi oggetti (`addList`) e una lista di oggetti da eliminare (`deleteList`).


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle = Draft.make_circle(1000)
rectangle = Draft.make_rectangle(2000, 800)
doc.recompute()

add_list1, delete_list1 = Draft.upgrade([circle, rectangle], delete=False)

line1 = Draft.make_line(App.Vector(2000, 0, 0), App.Vector(2500, 1500, 0))
line2 = Draft.make_line(App.Vector(2500, 1500, 0), App.Vector(3000, -1000, 0))
doc.recompute()

add_list2, delete_list2 = Draft.upgrade([line1, line2], delete=False)

simple_wire = add_list2[0]
add_list3, delete_list3 = Draft.upgrade(simple_wire, delete=False)

closed_wire = add_list3[0]
add_list4, delete_list4 = Draft.upgrade(closed_wire, delete=False)

face = add_list4[0]
add_list5, delete_list5 = Draft.upgrade(face, delete=False)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
