---
- GuiCommand:/ru
   Name:Std_Delete
   Name/ru:Удалить
   MenuLocation:Правка → Удалить
   Workbenches:Все
   Shortcut:**Del**
---

# Std Delete/ru

## Описание

Команда **Удалить**, удаляет выбранные объекты.

## Применение

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_Delete.svg" width=16px> Delete** option from the menu.
    -   Select the **<img src="images/Std_Delete.svg" width=16px> Delete** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Del**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Для удаления объекта используйте метод `removeObject` объекта document.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Delete/ru
