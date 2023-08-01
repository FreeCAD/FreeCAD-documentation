---
- GuiCommand:
   Name:Arch Axis
   MenuLocation:Arch - Axis tools - Axis
   Workbenches:[Arch](Arch_Workbench.md)
   Shortcut:**A** **X**
   SeeAlso:[Arch AxisSystem](Arch_AxisSystem.md), [Arch Grid](Arch_Grid.md)
---

# Arch Axis/en

## Description

The **<img src="images/Arch_Axis.svg" width=16px> [Arch Axis](Arch_Axis.md)** tool allows you to place a series of axes in the current document. The distance and the angle between axes is customizable, as well as the numbering style. The axes serve mainly as references to snap objects onto, but can also be used together with **<img src="images/Arch_AxisSystem.svg" width=16px> [Arch AxisSystems](Arch_AxisSystem.md)**. They can also be referenced by other Arch objects to create parametric arrays, for example of beams or columns. **<img src="images/Arch_Grid.svg" width=16px> [Arch Grids](Arch_Grid.md)** can also be used in places of axes.

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Two axes objects positioned perpendicularly to each other to create a grid*

## Usage

1.  Press the **<img src="images/Arch_Axis.svg" width=16px> [Arch Axis](Arch_Axis.md)** button, or press **A** then **X** keys.
2.  [Move](Draft_Move.md)/[rotate](Draft_Rotate.md) the axes system to the desired position.
3.  Enter edit mode by double-clicking the axes system in the tree view to adjust its settings like number of axes, distances and angles between axes.

## Options

-   Each axis in the series has its own distance and angle in relation to the previous axis. This allows to do very complex systems such as non-orthogonal systems, polar systems or any kind of non-uniform system.
-   Double-clicking the axis in the tree view allows to edit the distances, angles and labels of each axis.
-   Axes length, size of the bubbles and numbering styles are customizable directly via the axes system\'s properties.
-   Each axis can also display a label, which is editable via the task panel dialog.

## Properties

-    **Length**: The length of the axes

-    **Limit**: If greater than zero, each axis will be represented as two lines of the given length instead of one continuous line <small>(v0.20)</small> 

-    **Bubble Size**: The size of the axis bubbles

-    **Numeration style**: How the axes are numbered: 1,2,3, A,B,C, etc\...

-    **Bubble Position**: Where the bubble is placed on the axis: At start point, endpoint, both or none.

-    **Font Name**: A font to draw the bubble number and/or labels

-    **Font Size**: The size of the label text only (bubble text is controlled by the bubble size)

-    **Show Labels**: Turns the display of the label texts on/off

## Use as section mark 

By setting the **Bubble Position** property to **Arrow left/right** or **Bar left/right**, the axis will display a filled arrow or bar instead of the bubble, so it can be used as a section mark. <small>(v0.20)</small> 

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Axis tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```

-   Creates an `Axes` object from the given number (`num`) of axes, and `size`, the interval between each axis.

Example:


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Axis/en
