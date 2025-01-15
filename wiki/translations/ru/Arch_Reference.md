---
 GuiCommand:
   Name: Arch_Reference
   Name/ru: Ссылка
   MenuLocation: Arch , Ссылка
   Workbenches: Arch_Workbench/ru
   SeeAlso: Arch_BuildingPart/ru
---

# Arch Reference/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Инструмент «Reference» позволяет поместить объект в текущий документ, который копирует его форму и цвета из объекта [ Part](Part_Workbench.md) (включая [Arch BuildingPart](Arch_BuildingPart.md)), хранящегося в другом файле FreeCAD. Если этот файл FreeCAD изменяется, ссылочный объект отмечен для перезагрузки.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_reference_screenshot.png  style="width:800px;">


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **<img src="images/Arch_Reference.png" width=16px> '''Arch Reference'''
**
2.  Нажмите кнопку «Выбрать файл \...» и выберите существующий файл FreeCAD
3.  Выберите один из включенных объектов на основе частей из раскрывающегося списка
4.  Нажмите **OK**


</div>



## Опции

-   The reference object can be moved and rotated, the current position will be retained after reloading the object.
-   If the original object gets moved in containing file, this movement will reflect in the reference object.
-   By right-clicking a Reference object in the tree view, you have the options to reload the original object, or open the containing file.
-   To reference several objects at once, place them inside an [Arch BuildingPart](Arch_BuildingPart.md).
-   When turning off the **Update Colors** view property of the Reference, it won\'t reload the original colors anymore, so you can safely change them.



## Свойства

-    **File**: The base file this component is built upon

-    **Part**: The part to use from the base file

-    **Update Colors**: If true, the colors from the linked file will be kept updated



## Программирование

The Reference tool can by used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
reference = makeReference([filepath], [partname], [name])
```

Creates a `reference` object named `name` from the object `partname` in the file `filepath`. All arguments are optional.

Пример:


```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd", "myPart")
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Reference/ru
