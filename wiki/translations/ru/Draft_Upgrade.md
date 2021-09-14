---
- GuiCommand:/ru
   Name:Draft Upgrade
   Name/ru:Draft Upgrade
   MenuLocation:Черчение → Обновить
   Workbenches:[Draft](Draft_Workbench/ru.md), [Arch](Arch_Workbench/ru.md)
   Shortcut:**U** **P**
   SeeAlso:[Draft Downgrade](Draft_Downgrade/ru.md), [Part Fuse](Part_Fuse/ru.md)
---


</div>

## Описание


<div class="mw-translate-fuzzy">

Этот инструмент изменяет выбранные объекты по-разному. Если ни один объект не выбран, вам будет предложено выбрать его.


</div>

<img alt="" src=images/Draft_Upgrade_example.jpg  style="width:400px;"> 
*An open non-editable wire is upgraded to a closed wire, and then to a face. A closed non-editable square wire is also upgraded to a face. The two faces are then upgraded to create a compound, which is finally upgraded to a single editable Draft Wire.*

## Использование


<div class="mw-translate-fuzzy">

1.  Выберите один или несколько объектов, которые вы хотите обновить.
2.  Нажмите кнопку {{KEY | <img src="images/_Draft_Upgrade.png_" width= 16px> [[Draft Upgrade]]}} или нажмите {{KEY | U}}, затем {{KEY | P}}


</div>

## Notes

-   [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md) can be joined with this command, but also with the [Draft Join](Draft_Join.md) command or the [Draft Wire](Draft_Wire.md) command.

## Scripting


<div class="mw-translate-fuzzy">

## Скриптование


</div>


<div class="mw-translate-fuzzy">

Инструмент Апгрейд можно использовать из скриптов python и [макросов](макросов.md) следующим образом:


</div>


```python
upgrade_list = upgrade(objects, delete=False, force=None)
```

-    `objects`contains the objects to be upgraded. It is either a single object or a list of objects.

-   If `delete` is `True` the source objects are deleted.

-    `force`forces a certain way of upgrading by calling a specific internal function. It can be: `"makeCompound"`, `"closeGroupWires"`, `"makeSolid"`, `"closeWire"`, `"turnToParts"`, `"makeFusion"`, `"makeShell"`, `"makeFaces"`, `"draftify"`, `"joinFaces"`, `"makeSketchFace"`, `"makeWires"` or `"turnToLine"`.

-    `upgrade_list`is returned. It is a list containing two lists: a list of new objects and a list of objects to be deleted. If `delete` is `True` the second list is empty.

Пример:


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





 
