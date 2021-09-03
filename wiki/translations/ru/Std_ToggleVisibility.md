---
- GuiCommand:/ru
   Name:Std ToggleVisibility
   Name/ru:Std ToggleVisibility
   Empty:1
   MenuLocation:Вид → Видимость
   Workbenches:All
   Shortcut:**пробел**
   SeeAlso:[Std ShowSelection](Std_ShowSelection/ru.md), [Std HideSelection](Std_HideSelection/ru.md), [Std ToggleObjects](Std_ToggleObjects/ru.md), [Std ShowObjects](Std_ShowObjects/ru.md), [Std HideObjects](Std_HideObjects/ru.md)
---


</div>

## Описание

Команда **Std ToggleVisibility** переключает видимость выделенных объектов в окне [трёхмерного вида](3D_view/ru.md).

## Применение

1.  Выберите один или более чем один объект.
    -   Невидимые объекты могут быть выбраны в [древе проекта](Tree_view/ru.md).
    -   Будьте осторожны при использовании **Ctrl**+**A** для выделения всех объектов в древе проекта. Так как эта комбинация выделяет подэлементы [тел PartDesign](PartDesign_Body/ru.md) и объекты, используемые для [булевых операций в Part](Part_Boolean/ru.md). В большинстве случаев их надо оставлять невидимыми.
    -   Объекты, используемые для [булевых операций в Part](Part_Boolean/ru.md) так же выделяются при использовании **Ctrl**+**A** в окне трёхмерного вида.
2.  Есть несколько способов вызвать команду:
    -   Выбрать {{MenuCommand|Вид → <img src="images/Std_ToggleVisibility.svg" width=16px> Видимость}} из меню.
    -   Выбрать {{MenuCommand|Вид → Видимость → <img src="images/Std_ToggleVisibility.svg" width=16px> Видимость}} из меню.
    -   Выбрать {{MenuCommand|<img src="images/Std_ToggleVisibility.svg" width=16px> Видимость}} из контекстного меню в древе проекта. Эта опция не доступна в [верстаке PartDesign](PartDesign_Workbench/ru.md).
    -   Выбрать {{MenuCommand|<img src="images/Std_ToggleVisibility.svg" width=16px> Видимость}} из контекстного меню окна трёхмерного вида.
    -   Используя **пробел** на клавиатуре.

## Примечания


<div class="mw-translate-fuzzy">

-   Действие этих команд не может быть отменено через [Std Undo](Std_Undo/ru.md).
-   Видимость объекта может быть изменена через соответствующее свойство **Visibility** в [Property editor](Property_editor/ru.md) или [Combo view](Combo_view/ru.md).


</div>

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Используйте методы `show` и `hide` объектов для изменения их видимости.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Visibility == True:
  obj.hide()
else:
  obj.show()
```





{{Std Base navi

}}  
