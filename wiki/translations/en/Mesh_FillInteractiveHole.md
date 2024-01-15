---
 GuiCommand:
   Name: Mesh FillInteractiveHole
   MenuLocation: Meshes , Close hole
   Workbenches: Mesh_Workbench
   SeeAlso: Mesh_FillupHoles, Mesh_AddFacet
---

# Mesh FillInteractiveHole/en

## Description

The **Mesh FillInteractiveHole** command fills selected holes in mesh objects.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_FillInteractiveHole.svg" width=16px> [Close hole](Mesh_FillInteractiveHole.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_FillInteractiveHole.svg" width=16px> Close hole** option from the menu.
2.  The cursor changes to a triangle icon.
3.  Select a face that shares an edge with the hole you wish to close.
4.  The hole is closed.
5.  Optionally repeat this to close additional holes.
6.  If required you can use [Std Undo](Std_Undo.md) to undo the last action of the command.
7.  Select the **Leave hole-filling mode** option from the [3D view](3D_view.md) context menu to finish the command.

## Notes

-   If the edges of a hole do not lie in the same plane, the result of the command can depend on the selected face.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh FillInteractiveHole/en
