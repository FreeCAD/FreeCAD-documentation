---
- GuiCommand:/ru
   Name/ru:Уместить всё
   Name:Std_ViewFitAll
   MenuLocation:Вид → Стандартные виды‏‎ → Уместить всё
   Workbenches:Все
   Shortcut:**V** **F**
   SeeAlso:[Уместить выделенное](Std_ViewFitSelection/ru.md)
---

## Описание

The **Std ViewFitAll** command zooms and pans the camera so that all visible objects fit inside the active [3D view](3D_view.md).

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewFitAll.svg" width=16px> [Std ViewFitAll](Std_ViewFitAll.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewFitAll.svg" width=16px> Fit all** option from the menu.
    -   Select the **<img src="images/Std_ViewFitAll.svg" width=16px> Fit all** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **V** then **F**.

## Примечания

-   It is also possible to zoom to \'fit all\' via the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the view to \'fit all\' use the `fitAll` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

Alternatively the `SendMsgToActiveView` method of the FreeCADGui object can be used. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```





{{Std Base navi

}}  
