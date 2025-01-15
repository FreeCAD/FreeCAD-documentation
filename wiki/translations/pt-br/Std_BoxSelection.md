---
 GuiCommand:
   Name: Std BoxSelection
   MenuLocation: Edit , Box selection
   Workbenches: All
   Shortcut: **Shift**+**B**
   SeeAlso: Std_BoxElementSelection, Std_SelectAll
---

# Std BoxSelection/pt-br

## Description

The **Std BoxSelection** command selects objects from a user defined rectangular area, a box, in the [3D view](3D_view.md).

## Usage

1.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_BoxSelection.svg" width=16px> Box selection** option from the menu.
    -   Use the keyboard shortcut: **Shift**+**B**.
2.  Do one of the following:
    -   Drag a rectangle from left to right to select objects whose geometric center lies inside the rectangle.
    -   Drag a rectangle from right to left to select objects whose bounding box is (partially) inside the rectangle, or touches it.

## Notes

-   Use the [Std BoxElementSelection](Std_BoxElementSelection.md) command to box select faces instead of objects.
-   This command cannot be used to select elements in a sketch. See [Sketcher Workbench](Sketcher_Workbench#Selection_methods.md).



---
⏵ [documentation index](../README.md) > Std BoxSelection/pt-br
