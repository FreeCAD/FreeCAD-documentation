---
- GuiCommand:
   Name:Std MeasureDistance
   MenuLocation:Tools - Measure distance
   Workbenches:All
   SeeAlso:[Part Measure Linear](Part_Measure_Linear.md), [Draft Dimension](Draft_Dimension.md)
---

# Std MeasureDistance/en

## Description

The **Std MeasureDistance** command creates a distance object that measures and displays the distance between two points.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_MeasureDistance.svg" width=16px> [Std MeasureDistance](Std_MeasureDistance.md)** button.
    -   Select the **Tools → <img src="images/Std_MeasureDistance.svg" width=16px> Measure distance** option from the menu.
2.  Select the first dimension point anywhere on an object in the [3D view](3D_view.md).
3.  Select the second dimension point anywhere on an object in the 3D view.
4.  The selection order of the points can have an impact on the position of the dimension line.
5.  Optionally flip the position of the dimension line by changing the **Mirror** property of the distance object.

## Notes

-   You cannot use the [Draft](Draft_Workbench.md) snap tools with this command.
-   To add dimensions to drawings use the dimension tools from the [TechDraw Workbench](TechDraw_Workbench.md).
-   For more comprehensive measuring tools, install the <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator Workbench](Manipulator_Workbench.md) (an [external workbench](External_workbenches.md)).

## Properties

### Data


{{TitleProperty|Base}}

-    **Label**: by default the label contains the measured distance, but this distance is not updated when P1 or P2 are later changed.


{{TitleProperty|Measurement}}

-    **P1**: the first dimension point.

-    **P2**: the second dimension point.

-    **Distance**: (read-only) the measured distance between P1 and P2.

### View


{{TitleProperty|Base}}

-    **Dist Factor**: this factor, multiplied by the measured distance, determines the dimension line offset.

-    **Font Size**: the height of the letters (line height in pixels).

-    **Mirror**: if set to `True` the position of the dimension line relative to P1 and P2 is flipped.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std MeasureDistance/en
