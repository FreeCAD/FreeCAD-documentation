---
- GuiCommand:   Name:Draft Upgrade   Name:Draft Upgrade   Workbenches:[Arch](Draft_Workbench___Draft]],_[[Arch_Workbench.md)|MenuLocation:Draft -> Upgrade   Shortcut:U P   SeeAlso:[Draft Downgrade](Draft_Downgrade.md)---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument upgradează obiectele selectate în moduri diferite. Dacă nu este selectat niciun obiect, veți fi invitați să selectați unul.


</div>

<img alt="" src=images/Draft_Upgrade_example.jpg  style="width:400px;"> 
*An open non-editable wire is upgraded to a closed wire, and then to a face. A closed non-editable square wire is also upgraded to a face. The two faces are then upgraded to create a compound, which is finally upgraded to a single editable Draft Wire.*

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați unul sau mi multe obiecte pe care doriți să le upgradați
2.  apăsați pe butonul **<img src="images/Draft_Upgrade.png" width=16px> [[Draft Upgrade]]
** sau apăsați pe tasta **U** și apoi pe **P**


</div>

## Notes

-   [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md) can be joined with this command, but also with the [Draft Join](Draft_Join.md) command or the [Draft Wire](Draft_Wire.md) command.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul upgrade poate fi utilizaqt de la consola Python și prin [macros](macros.md), ca de exemplu:


</div>


```python
upgrade_list = upgrade(objects, delete=False, force=None)
```


<div class="mw-translate-fuzzy">

-   Actualizează obiectul/e dat/e, acesta (poate fi un obiect sau o listă de obiecte).
-   Dacă ștergerea este True, obiectele vechi sunt șterse.
-   Atributul de forță poate fi folosit pentru a forța un anumit mod de modernizare. Poate fi: makeCompound, closeGroupWires, makeSolid, closeWire, turnToParts, makeFusion, makeShell, makeFaces, draftify, joinFaces, makeSketchFace, makeWires
-   Returnează un dicționar care conține două liste, o listă de obiecte noi și o listă de obiecte care trebuie șterse


</div>

Exempluː


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





 
