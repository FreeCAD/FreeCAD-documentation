---
- GuiCommand:/ru
   Name:Std_Delete
   Name/ru:Удалить
   MenuLocation:Правка → Удалить
   Workbenches:Все
   Shortcut:**Del**
---

## Описание

The **Std Delete** command deletes selected objects.

## Применение

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_Delete.svg" width=16px> Delete** option from the menu.
    -   Select the **<img src="images/Std_Delete.svg" width=16px> Delete** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **Del**.

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To delete an object use the `removeObject` method of the document object.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std Base navi

}}  
