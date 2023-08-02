---
- GuiCommand:
   Name/ru: Сзади
   Name: Std_ViewRear
   MenuLocation: Вид -> Стандартные виды‏‎ -> Сзади
   Workbenches: Все
   Shortcut: **4**
   SeeAlso: Std_ViewBottom/ru, Std_ViewLeft/ru
---

# Std ViewRear/ru

## Описание

The **Std ViewRear** command points the camera in the active [3D view](3D_view.md) in the direction of the negative Y axis.

![](images/FreeCAD_views_rear.svg ) 
*Arrow 4 points in the direction of the rear view*

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewRear.svg" width=16px> [Std ViewRear](Std_ViewRear.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewRear.svg" width=16px> Rear** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewRear.svg" width=16px> Rear** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **4**.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change to rear view use the `viewRear` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRear()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewRear/ru
