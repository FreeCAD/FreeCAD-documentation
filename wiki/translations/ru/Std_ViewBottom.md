---
- GuiCommand   */ru
   Name   *Std ViewBottom
   Name/ru   *Std ViewBottom
   MenuLocation   *Виды → Стандартные виды → Снизу
   Workbenches   *All
   Shortcut   ***5**
   SeeAlso   *[Std ViewRear](Std_ViewRear/ru.md), [Std ViewLeft](Std_ViewLeft/ru.md)
---

# Std ViewBottom/ru

## Описание

The **Std ViewBottom** command points the camera in the active [3D view](3D_view.md) in the direction of the positive Z axis.

![](images/FreeCAD_views_rear.svg ) 
*Arrow 5 points in the direction of the bottom view*

## Применение

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Std_ViewBottom.svg" width=16px> [Std ViewBottom](Std_ViewBottom.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewBottom.svg" width=16px> Bottom** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewBottom.svg" width=16px> Bottom** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut   * **5**.

## Scripting


**Смотрите так же   ***

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change to bottom view use the `viewBottom` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewBottom()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewBottom/ru
