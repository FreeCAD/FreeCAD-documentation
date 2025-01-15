---
 GuiCommand:
   Name: Sketcher Clone
   MenuLocation: Sketch , Sketcher tools , Clone
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **L**
   Version: 0.16
   SeeAlso: Sketcher_Copy, Sketcher_Move
---

# Sketcher Clone/hr



## Opis

The <img alt="" src=images/Sketcher_Clone.svg  style="width:16px;"> [Sketcher Clone](Sketcher_Clone.md) command clones the selected sketch elements from one point to another, using the last selected point as reference. If any constraints are part of the source elements, then the new constraints are linked to the source constraints; if the constraints in the source are changed, the constraints in the clone are also changed. To avoid this linking see **[<img src=images/Sketcher_Copy.svg style="width:16px"> [Sketcher Copy](Sketcher_Copy.md)**.

Note that a clone of a clone becomes a Sketcher Copy. If you wish to create linked constraints, clone the original source elements again.




<div class="mw-translate-fuzzy">

## Kako koristiti 


</div>

1.  Select the sketch elements to clone.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Sketcher_Clone.svg" width=16px> [Clone](Sketcher_Clone.md)** button.
    -   Select the **Sketch → Sketcher tools → <img src="images/Sketcher_Clone.svg" width=16px> Clone** option from the menu.
    -   The keyboard shortcut: **Z** then **L**.
3.  Move the mouse in the [3D view](3D_view.md) to the desired location for the clone.By keeping **Shift** pressed, the angle to the location point can be fixed in steps of 5°. <small>(v0.20)</small> 
4.  Left-click in the 3D view to create the clone.

No extra constraints are added for the clone.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Clone/hr
