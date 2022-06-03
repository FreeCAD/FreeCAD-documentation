# Draft Downgrade/cs
---
- GuiCommand   */cs   Name   *Draft_Downgrade   Name/cs   *Kreslení Degradace   Workbenches   *[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation   *Draft → Downgrade   Shortcut   *D N   SeeAlso   *[Draft Upgrade](Draft_Upgrade/cs.md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj degraduje vybrané objekty různými způsoby. Není-li vybrán žádný objekt, budete vyzvání k výběru objektu.


</div>

<img alt="" src=images/Draft_Downgrade_example.jpg  style="width   *400px;"> 
*Two overlapping faces are downgraded to a Part Cut object, which is downgraded to a face. That face is then downgraded to a closed wire, which is finally downgraded to separate edges.*


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte jeden nebo více objektů, které chcete degradovat
2.  Stiskněte tlačítko **<img src="images/Draft_Downgrade.png" width=16px> [Degradace](Draft_Downgrade/cs.md)
** nebo klávesy **D** a **N**


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Degradace může být použit ve skriptech Pythonu a v [makrech](macros/cs.md) použitím následující funkce   *


</div>


```python
downgrade_list = downgrade(objects, delete=False, force=None)
```


<div class="mw-translate-fuzzy">

-   Degraduje zadaný objekt(y) (může to být objekt nebo seznam objektů).
-   Je-li delete True, staré objekty budou smazány.
-   Atribut force může být využit pro určení požadovaného způsobu degradace. Může to být   * explode (oddělení), shapify, subtr(odebrání), splitFaces(rozděl plochy), cut2, getWire, splitWires(rozděl drát).
-   Vrací katalog obsahující dva seznamy, seznam nových objektů a seznam objektů ke smazání


</div>

Příklad   *


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

box = doc.addObject("Part   *   *Box", "Box")
box.Length = 2300
box.Width = 800
box.Height = 1000

add_list4, delete_list4 = Draft.downgrade(box, delete=True)

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Downgrade/cs
