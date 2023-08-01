---
- GuiCommand:/ru
   Name:Std ViewLeft
   Name/ru:Std ViewLeft
   MenuLocation:Виды → Стандартные виды → Слева
   Workbenches:All
   Shortcut:**6**
   SeeAlso:[Std ViewRear](Std_ViewRear/ru.md), [Std ViewBottom](Std_ViewBottom/ru.md)
---

# Std ViewLeft/ru

## Описание

The **Std ViewLeft** command points the camera in the active [3D view](3D_view.md) in the direction of the positive X axis.

![](images/FreeCAD_views_rear.svg ) 
*Arrow 6 points in the direction of the left view*

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewLeft.svg" width=16px> [Std ViewLeft](Std_ViewLeft.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewLeft.svg" width=16px> Left** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewLeft.svg" width=16px> Left** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **6**.

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change to left view use the `viewLeft` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewLeft()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewLeft/ru
