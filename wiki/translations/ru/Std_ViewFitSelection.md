---
- GuiCommand:/ru
   Name:Std ViewFitSelection
   Name/ru:Std ViewFitSelection
   MenuLocation:Вид → Стандартные виды → Уместить выделенное
   Workbenches:All
   Shortcut:**V** **S**
   SeeAlso:[Std ViewFitAll](Std_ViewFitAll.md)
---

## Описание

The **Std ViewFitSelection** command zooms and pans the camera so that all selected objects fit inside the active [3D view](3D_view.md).

## Применение

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewFitSelection.svg" width=16px> [Std ViewFitSelection](Std_ViewFitSelection.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewFitSelection.svg" width=16px>Fit selection** option from the menu.
    -   Select the **<img src="images/Std_ViewFitSelection.svg" width=16px> Fit selection** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **V** then **S**.

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the view to \'fit selection\' the `SendMsgToActiveView` method of the FreeCADGui object can be used. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewSelection')
```





{{Std Base navi

}}  
