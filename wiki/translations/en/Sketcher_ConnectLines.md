---
- GuiCommand:
   Name:Sketcher ConnectLines
   MenuLocation:Sketch → Sketcher tools → Connect Edges
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**Ctrl**+**Shift**+**K**
   Version:0.15
   SeeAlso:[Sketcher ConstrainCoincident](Sketcher_ConstrainCoincident.md)
---

# Sketcher ConnectLines/en

## Description

Applies [Coincident constraints](Sketcher_ConstrainCoincident.md) to endpoints with the same coordinates of the selected elements.

## Usage

1.  Select the elements in the [3D view](3D_view.md) or in the [Task panel](Task_panel.md) on the left side of the screen
2.  Invoke the command using several methods:
    -   Press the **<img src=images/Sketcher_ConnectLines.svg style="width:16px"> [Connect lines](Sketcher_ConnectLines.md)** button.
    -   Use the **Ctrl** + **Shift** + **K** keyboard shortcut.
    -   Use the **Sketch → Sketcher tools → <img src=images/Sketcher_ConnectLines.svg style="width:16px"> Connect Edges** entry from the top menu.

## Notes

Before using this command make sure that obvious constraints (horizontal, vertical, tangential) are already applied to the elements. Selecting the elements in a counter-clock-wise order seems to produce better results.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConnectLines/en
