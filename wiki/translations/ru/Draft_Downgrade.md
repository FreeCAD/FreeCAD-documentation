---
- GuiCommand:/ru
   Name:Draft Downgrade
   Name/ru:Draft Downgrade
   MenuLocation:Черчение -> Перестроить
   Workbenches:[Draft](Draft_Workbench/ru.md), [Arch](Arch_Workbench/ru.md)
   Shortcut:**D** **N**
   SeeAlso:[Обновить](Draft_Upgrade/ru.md)
---

# Draft Downgrade/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Этот инструмент разбивает выбранные объекты (преобразует объект в несколько объектов нижнего уровня). Если объекты не выбраны, попросите их выбрать.


</div>

<img alt="" src=images/Draft_Downgrade_example.jpg  style="width:400px;"> 
*Two overlapping faces are downgraded to a Part Cut object, which is downgraded to a face. That face is then downgraded to a closed wire, which is finally downgraded to separate edges.*


<div class="mw-translate-fuzzy">

## Использование


</div>


<div class="mw-translate-fuzzy">

1.  Выберите один или несколько объектов, которые вы хотите понизить
2.  Нажмите кнопку **<img src="images/Draft_Downgrade.png" width=16px> [[Draft Downgrade]]** или нажмите {{KEY | D}}, затем клавиши {{KEY | N}}


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Скриптование


</div>


<div class="mw-translate-fuzzy">

Инструмент Даунгрейд можно использовать в сценариях python и [макросы](макросы.md), используя следующую функцию:


</div>


```python
downgrade_list = downgrade(objects, delete=False, force=None)
```

-    `objects`contains the objects to be downgraded. It is either a single object or a list of objects.

-   If `delete` is `True` the source objects are deleted.

-    `force`forces a certain way of downgrading by calling a specific internal function. It can be: `"explode"`, `"shapify"`, `"subtr"`, `"splitFaces"`, `"cut2"`, `"getWire"`, `"splitWires"` or `"splitCompounds"`.

-    `downgrade_list`is returned. It is a list containing two lists: a list of new objects and a list of objects to be deleted. If `delete` is `True` the second list is empty.

Пример:


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Downgrade/ru
