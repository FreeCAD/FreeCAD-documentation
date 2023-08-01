---
- GuiCommand:
   Name:Sketcher RectangularArray
   MenuLocation:Sketch → Sketcher tools → Rectangular array
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**Z** **A**
   Version:0.16
---

# Sketcher RectangularArray/en

## Description

Creates an array of selected sketcher elements.

## Usage

1.  Select sketcher elements in [task panel](Task_panel.md) or in [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/Sketcher_RectangularArray.svg style="width:16px"> [Rectangular array](Sketcher_RectangularArray.md)** button.
    -   Select the **Sketch → Sketcher tools → [<img src=images/Sketcher_RectangularArray.svg style="width:16px"> Rectangular array** option from the menu.
3.  Specify the options for the array in the dialog that opens.
4.  Press the **OK** button.
5.  Move the mouse in the [3D view](3D_view.md) towards the desired reference point.By keeping **Ctrl** pressed, the angle to the reference point can be fixed in steps of 5°. <small>(v0.20)</small> 
6.  Left-click in the 3D view to create the array.
7.  To set the distances between the array elements, edit the dimensional constraints of the array.

## Options

![](images/Sketcher_RectangularArray_Options.jpg )

**Rectangular array** has the following options:

-   **Colums**: The number of columns for the array.
-   **Rows**: The number of rows for the array.
-   **Equal vertical/horizontal spacing**: If the vertical distance between the array elements should be the same as the horizontal distance.
-   **Constrain inter-element separation**: When this is checked, the distance between the array elements will be constrained.If you for example only know that you need a 23 x 15 mm array, use this option to later be able to change these constraints to the dimensions you need.
-   **Clone**: If selected, dimensional constraints are replaced by geometric constraints in the copies, so that any change in the original element is also reflected in the copies.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RectangularArray/en
