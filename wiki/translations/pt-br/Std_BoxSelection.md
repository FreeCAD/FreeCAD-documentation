---
- GuiCommand:
   Name:Std BoxSelection
   MenuLocation:Edit - Box selection
   Workbenches:All
   Shortcut:**Shift**+**B**
   SeeAlso:[Std BoxElementSelection](Std_BoxElementSelection.md), [Std SelectAll](Std_SelectAll.md)
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
-   This command cannot be used to select elements in a [sketch](sketch.md). To \'box select\' when the [Sketcher Dialog](Sketcher_Dialog.md) is open:
    1.  Make sure that no command is active.
    2.  Do one of the following:
        -   Click in an empty area and drag a rectangle from left to right to select objects that lie completely inside the rectangle.
        -   Click in an empty area and drag a rectangle from right to left to also select objects that touch or cross the rectangle.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std BoxSelection/pt-br
