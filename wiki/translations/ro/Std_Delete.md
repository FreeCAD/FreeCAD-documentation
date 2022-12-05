# Std Delete/ro
---
- GuiCommand:   Name:Std Delete   Workbenches:All   MenuLocation:[Edit](Std_Edit_Menu.md) → Delete---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Această comandaă șterge obiect(ul)ele selectate. Dacă nu este selectat nici un obiect, nimic nu se întâmplă.


</div>


<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

Obiect(ul)ele selectatea pot fi șterse din document apăsând **DEL**, din meniul Edit → Delete, sau din vizualizarea arborescentă meniul contextual. Toate operațiunile de ștergere pot anulate(undone) și reluate(redone).


</div>

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To delete an object use the `removeObject` method of the document object.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Delete/ro
