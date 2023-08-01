---
- GuiCommand:
   Name:Arch Grid
   MenuLocation:Arch → Axis tools → Grid
   Workbenches:[Arch](Arch_Workbench.md)
   SeeAlso:[Arch Axis](Arch_Axis.md), [Arch AxisSystem](Arch_AxisSystem.md)
---

# Arch Grid/en

## Description

The **<img src="images/Arch_Grid.svg" width=16px> [Arch Grid](Arch_Grid.md)** tool allows you to place a grid-like object in the document. This object is meant to serve as a base to build Arch objects that need a regular but complex frame, such as windows, curtain walls, column grids, railings, etc. The Grid object is editable like a spreadsheet, where you can add or remove columns and rows, define their size, and merge cells.

The Grid is a 2D object, and can therefore be used anywhere a 2D shape such as a [Draft](Draft_Workbench.md) or [Sketch](Sketcher_Workbench.md) is needed, but it can also behave as a [Arch AxisSystem](Arch_AxisSystem.md), and be used to propagate the placement of other Arch objects.

<img alt="" src=images/Arch_Grid_example.jpg  style="width:600px;"> 
*An array of columns, a railing system, and a window, each based on an [Arch Grid](Arch_Grid.md) object.*

## Usage

1.  Press the **<img src="images/Arch_Grid.svg" width=16px> [Arch Grid](Arch_Grid.md)** button.
2.  Set the **Width** and **Height** of the grid in the properties.
3.  Enter edit mode by double-clicking the grid object in the tree view.
4.  Add rows and columns.
5.  Set the desired width and height of rows and columns by double-clicking the row or column headers.

## Options

-   A column width or row height of 0 means its size will be adapted automatically to fit the total width/height of the grid.
-   Cells can be merged and unmerged by selecting them and clicking the appropriate button.
-   When used as the **Axis** property of other Arch objects, the grid will drive the positioning of these objects. The **Points Output** property defines how the other objects are placed on the grid: At vertices, edge midpoints or face centers.
-   By setting the **Auto Height** or **Auto Width** properties to a non-zero value, the total number of rows/columns and their individual heights/widths is ignored. Instead, the maximum number of columns or rows of the given auto width/height get automatically created.

## Properties

-    **Rows**: The number of rows

-    **Columns**: The number of columns

-    **Row Size**: The sizes for rows

-    **Column Size**: The sizes of columns

-    **Points Output**: The type of 3D points produced by this grid object

-    **Width**: The total width of this grid

-    **Height**: The total height of this grid

-    **Auto Width**: Creates automatic column divisions (set to 0 to disable)

-    **Auto Height**: Creates automatic row divisions (set to 0 to disable)

-    **Reorient**: When in edge midpoint mode, if this grid must reorient its children along edge normals or not

-    **Hidden Faces**: The indices of faces to hide

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Grid tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Grid = makeGrid(name="Grid")
```

-   Creates a `Grid` object.

Its `Width`, `Height`, `Rows`, and `Columns` attributes can be changed directly to define the appearance of the grid.


```python
import FreeCAD, Draft, Arch
Grid = Arch.makeGrid()

Grid.Width = 5000
Grid.Height = 5000
Grid.Rows = 4
Grid.Columns = 6
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = Grid
FreeCAD.ActiveDocument.recompute() 
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Grid/en
