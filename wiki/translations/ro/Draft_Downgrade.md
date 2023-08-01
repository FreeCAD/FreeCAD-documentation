---
- GuiCommand:
   Name:Draft Downgrade
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   MenuLocation:Draft - Downgrade
   Shortcut:D N
   SeeAlso:[Draft Upgrade](Draft_Upgrade.md)
---

# Draft Downgrade/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument downgradează/ retrogradează/ descompune/ explodează obiectele selectate în moduri diferite. Dacă nu este selectat niciun obiect, veți putea selecta unul.


</div>

<img alt="" src=images/Draft_Downgrade_example.jpg  style="width:400px;"> 
*Two overlapping faces are downgraded to a Part Cut object, which is downgraded to a face. That face is then downgraded to a closed wire, which is finally downgraded to separate edges.*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați unul sau mi multe obiecte pe caer vreți să le downgradați
2.  apăsați pe butonul **<img src="images/Draft_Downgrade.png" width=16px> [[Draft Downgrade]]
** sau apăsați pe tasta **D** și apoi pe **N**


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

Instrumentul Downgrade poate fi folosit în scripturile python și [macros](macros.md) utilizând următoarea funcție:


</div>


```python
downgrade_list = downgrade(objects, delete=False, force=None)
```


<div class="mw-translate-fuzzy">

-   Downgradează obiectul/e dat/e (poate fi un obiect sau o listă de obiecte).
-   Dacă ștergerea este True, obiectele vechi sunt șterse.
-   Atributul de forță poate fi folosit pentru a forța un anumit mod de dezasambalre. Acesta poate fi: explode, shapify, subtr, splitFaces, cut2, getWire, splitWires.
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

add_list1, delete_list1 = Draft.upgrade([circle, rectangle], delete=True)

compound = add_list1[0]
add_list2, delete_list2 = Draft.downgrade(compound, delete=False)
face = add_list2[0]
add_list3, delete_list3 = Draft.downgrade(face, delete=False)

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

add_list4, delete_list4 = Draft.downgrade(box, delete=True)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Downgrade/ro
