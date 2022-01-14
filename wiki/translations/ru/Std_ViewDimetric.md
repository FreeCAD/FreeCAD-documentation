---
- GuiCommand:/ru
   Name:Std_ViewDimetric
   Name/ru:Диметрическая
   MenuLocation:Вид → Стандартные виды → Axonometric → Диметрическая
   Workbenches:Все
   SeeAlso:[Изометрическая](Std_ViewIsometric/ru.md),<br> [Триметрическая](Std_ViewTrimetric/ru.md)
---

# Std ViewDimetric/ru

## Описание

The **Std ViewDimetric** command realigns the camera in the active [3D view](3D_view.md) to obtain a [dimetric](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types) view. For a truly dimetric view the 3D view must be in [orthographic mode](Std_OrthographicCamera.md), but the command also works if the view is in [perspective mode](Std_PerspectiveCamera.md).

![](images/Std_ViewDimetric_example.svg ) 
*The [axis cross](Std_AxisCross.md) and a cube in dimetric view*

## Применение

1.  Select the **View → Standard views → Axonometric → <img src="images/Std_ViewDimetric.svg" width=16px> Dimetric** option from the menu.

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Чтобы установить диметрический Вид используйте `viewDimetric` метод ActiveView объекта. Данный метод не доступен в консольном режиме FreeCAD.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewDimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewDimetric/ru
