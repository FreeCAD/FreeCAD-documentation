# Std ViewFitAll/ro
---
- GuiCommand:   Name:Std ViewFitAll   MenuLocation:[|Workbenches:All   Shortcut:   SeeAlso:[[Std_ViewFitSelection|Fit Selection](Std_View_Menu___View]]_→_Standard_views‏‎_→_FitAll.md)---


</div>




<div class="mw-translate-fuzzy">

## Descriere

Efectuarea unui zoom/se micșorează până când toate obiectele vizibile sunt afișate în vizualizarea 3D.


</div>

The **Std ViewFitAll** command zooms and pans the camera so that all visible objects fit inside the active [3D view](3D_view.md).




<div class="mw-translate-fuzzy">

## Utilizare

Click pe <img alt="" src=images/Std_ViewFitAll.png  style="width:32px;"> sau alegeți ** View** → ** Standard views** → **<img src="images/Std_ViewFitAll.png" width=32px> Fit all** din meniul de sus/top.
Comanda este de asemenea disponibilă în vizualizarea 3D (și nu are nimic pre-selectat).


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewFitAll.svg" width=16px> [Std ViewFitAll](Std_ViewFitAll.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewFitAll.svg" width=16px> Fit all** option from the menu.
    -   Select the **<img src="images/Std_ViewFitAll.svg" width=16px> Fit all** option from the [3D view](3D_view.md) context menu.
    -   Select the **<img src="images/Std_ViewFitAll.svg" width=16px> Fit all** option from the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).
    -   Use the keyboard shortcut: **V** then **F**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

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



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewFitAll/ro
