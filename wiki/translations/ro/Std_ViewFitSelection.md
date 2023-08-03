# Std ViewFitSelection/ro
---
 GuiCommand:   Name: Std ViewFitSelection   MenuLocation: Std View Menu   View , Fit Selection|Workbenches: All   Shortcut:    SeeAlso: ---


</div>




<div class="mw-translate-fuzzy">

## Descriere

Faceți Zooms până toae obiectele selectate din arborescența vizualizătilro sunt vizibile în vizualizarea 3D.


</div>

The **Std ViewFitSelection** command zooms and pans the camera so that all selected objects fit inside the active [3D view](3D_view.md). This command is useful in cases where for some reason objects are beyond the boundaries of the current 3D View or can\'t be easily found using [3D navigation](Mouse_navigation.md).




<div class="mw-translate-fuzzy">

## Utilizare

Click pe <img alt="" src=images/Std_ViewFitSelection.png  style="width:32px;"> or choose ** View** → ** Standard views** → **<img src="images/Std_ViewFitSelection.png" width=32px> Fit selection** din meniul principal.
Comanda este de asemenea disponibilă făcând cilc drapta în vizualizarea 3D (și neavânde nimic preselectat).


</div>

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewFitSelection.svg" width=16px> [Std ViewFitSelection](Std_ViewFitSelection.md)** button.
    -   Select the **View → Standard views → <img src="images/Std_ViewFitSelection.svg" width=16px>Fit selection** option from the menu.
    -   Select the **<img src="images/Std_ViewFitSelection.svg" width=16px> Fit selection** option from the [3D view](3D_view.md) context menu.
    -   Use the keyboard shortcut: **V** then **S**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to \'fit selection\' the `SendMsgToActiveView` method of the FreeCADGui object can be used. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewSelection')
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFitSelection/ro
