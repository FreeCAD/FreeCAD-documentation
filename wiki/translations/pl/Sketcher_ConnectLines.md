---
- GuiCommand:
   Name:Sketcher ConnectLines
   MenuLocation:Sketch → Sketcher tools → Connect edges
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**Z** **J**
   Version:0.15
   SeeAlso:[Sketcher ConstrainCoincident](Sketcher_ConstrainCoincident.md)
---

# Sketcher ConnectLines/pl

## Description

Applies [Coincident constraints](Sketcher_ConstrainCoincident.md) to endpoints with the same coordinates of the selected elements.

## Usage

1.  Select the unconnected elements in the [3D view](3D_view.md) or in the [Task panel](Task_panel.md) on the left side of the screen
2.  Invoke the command using several methods:
    -   Press the **[<img src=images/Sketcher_ConnectLines.svg style="width:16px"> [Connect edges](Sketcher_ConnectLines.md)** button.
    -   Use the **Z** then **J** keyboard shortcut.
    -   Use the **Sketch → Sketcher tools → [<img src=images/Sketcher_ConnectLines.svg style="width:16px"> Connect edges** entry from the top menu.

## Notes

Before using this command make sure that obvious constraints (horizontal, vertical, tangential) are already applied to the elements. Selecting the elements in a counter-clock-wise order seems to produce better results.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConnectLines/pl
