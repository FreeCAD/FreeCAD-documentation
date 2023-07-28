---
- GuiCommand:
   Name:Sketcher Snap
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Version:0.21
   SeeAlso:[Sketcher Grid](Sketcher_Grid.md)
---

# Sketcher Snap/en

## Description

The **Sketcher Snap** command toggles snapping in all sketches. Individual snaps and settings can be changed in the related menu.

Snapping only works while creating geometry. Note that snapping is just a drawing aid, it does not produce additional constraints.

## Usage

1.  Press the **<img src="images/Sketcher_Snap.svg" width=16px> [Toggle snap](Sketcher_Snap.md)** button to toggle snapping.
2.  optionally click on the down arrow to the right of the button to open the menu. The settings in this menu can only be changed if snapping is switched on:
    ![](images/Sketcher_Snap_Menu.png )
    -   If the **Snap to grid** checkbox is checked, the cursor will snap to grid lines and grid intersections. Also works if the grid is invisible.

    -   If the **Snap to objects** checkbox is checked, the cursor will snap to edges of geometry and midpoints of lines and arcs.

    -   
        **Snap angle**
        
        specifies the angle for angular snap. Snapping will occur at multiples of this value starting from the direction of the positive X axis of the sketch. The **Ctrl** key must be held down for this snap. Only works when creating certain geometry, [lines](Sketcher_CreateLine.md) for example.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Snap/en
