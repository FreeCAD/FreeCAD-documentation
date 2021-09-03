---
- GuiCommand:/cs   Name:Draft Upgrade   Name/cs:Kreslení Vylepšení   Workbenches:[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation:Kreslení → Aktualizace   Shortcut:U P   SeeAlso:[Kreslení Degradace](Draft_Downgrade/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj vylepší vybrané objekty jiným způsobem. Není-li vybrán žádný objekt budete vyzváni k jeho výběru.


</div>

<img alt="" src=images/Draft_Upgrade_example.jpg  style="width:400px;"> 
*An open non-editable wire is upgraded to a closed wire, and then to a face. A closed non-editable square wire is also upgraded to a face. The two faces are then upgraded to create a compound, which is finally upgraded to a single editable Draft Wire.*

## Použití


<div class="mw-translate-fuzzy">

1.  Vyberte jeden nebo více objektů, které chcete vylepšit
2.  Stiskněte tlačítko **<img src="images/Draft_Upgrade.png" width=16px> [Kreslení Vylepšení](Draft_Upgrade/cs.md)
** nebo stiskněte klávesy **U** a potom **P**


</div>

## Notes

-   [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md) can be joined with this command, but also with the [Draft Join](Draft_Join.md) command or the [Draft Wire](Draft_Wire.md) command.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Vylepšení může být použit ze skriptů Pythonu a z [maker](macros/cs.md) takto:


</div>


```python
upgrade_list = upgrade(objects, delete=False, force=None)
```


<div class="mw-translate-fuzzy">

-   Vylepší daný objekt(y) (může to být objekt nebo seznam objektů).
-   Je-li delete True, jsou staré objekty smazány.
-   Atribut force může být využit pro určení požadovaného způsobu vylepšení. Může to být: makeCompound, closeGroupWires, makeSolid, closeWire, turnToParts, makeFusion, makeShell, makeFaces, draftify, joinFaces, makeSketchFace, makeWires
-   Vrací adresář obsahující dva seznamy, seznam nových objektů a seznam objektů ke smazání


</div>

Příklad:


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





 
