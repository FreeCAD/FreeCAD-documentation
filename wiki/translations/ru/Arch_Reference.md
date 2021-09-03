---
- GuiCommand:/ru   Name:Arch Reference   Name/ru:Arch Reference   Workbenches:[MenuLocation:Arch → Reference   Shortcut:   SeeAlso:[[Arch BuildingPart](Arch_Module/ru___Arch]].md)---


</div>

## Описание

<img alt="" src=images/Arch_reference_screenshot.png  style="width:800px;">


<div class="mw-translate-fuzzy">

Инструмент «Reference» позволяет поместить объект в текущий документ, который копирует его форму и цвета из объекта [ Part](Part_Workbench.md) (включая [Arch BuildingPart](Arch_BuildingPart.md)), хранящегося в другом файле FreeCAD. Если этот файл FreeCAD изменяется, ссылочный объект отмечен для перезагрузки.


</div>


<div class="mw-translate-fuzzy">

## Использование


</div>


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **<img src="images/Arch_Reference.png" width=16px> '''Arch Reference'''
**
2.  Нажмите кнопку «Выбрать файл \...» и выберите существующий файл FreeCAD
3.  Выберите один из включенных объектов на основе частей из раскрывающегося списка
4.  Нажмите **OK**


</div>

## Options

-   The reference object can be moved and rotated, the current position will be retained after reloading the object.
-   If the original object gets moved in containing file, this movement will reflect in the reference object.
-   By right-clicking a Reference object in the tree view, you have the options to reload the original object, or open the containing file.
-   To reference several objects at once, place them inside an [Arch BuildingPart](Arch_BuildingPart.md).
-   When turning off the **Update Colors** view property of the Reference, it won\'t reload the original colors anymore, so you can safely change them.

## Properties

-    **File**: The base file this component is built upon

-    **Part**: The part to use from the base file

-    **Update Colors**: If true, the colors from the linked file will be kept updated

## Scripting

The Reference tool can by used in [macros](macros.md) and from the python console by using the following function: 
```python
makeReference ([file_path,object_name])
```

creates a Reference object from the given object in the given file.

Example: 
```python
import Arch
Arch.makeReference("/path/to/some/file.FSCtd","myPart")
```





 
