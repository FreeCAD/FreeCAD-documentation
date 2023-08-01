---
- GuiCommand:
   Name: Part Measure Linear
   MenuLocation: Measure - Measure Linear
   Workbenches: [Part](Part_Workbench.md)
   SeeAlso: [Std MeasureDistance](Std_MeasureDistance.md), [Draft Dimension](Draft_Dimension.md)
---

# Part Measure Linear

## Description

This command measures the distance between two selected topological elements (vertex, edge, face) and displays measurements in the [3D view](3D_view.md). The shortest distance between the two elements and the delta measurements (distances parallel to the global X, Y, Z axes) are shown.

The appearance of the measurements can be changed in the [preferences](PartDesign_Preferences#Measure.md).

 <img alt="" src=images/MeasureLinear3D1.png  style="width:400px;"> <img alt="" src=images/MeasureLinearDelta1.PNG  style="width:400px;"> 

## Usage

1.  Select any combination of two elements: vertices, edges, faces
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Measure_Linear.svg" width=16px> [Measure Linear](Part_Measure_Linear.md)** button.
    -   Select the **Measure → <img src="images/Part_Measure_Linear.svg" width=16px> Measure Linear** option from the menu.
3.  Alternatively the command can be launched without prior selection. A selection dialog then opens in the [Task panel](Task_panel.md). A Control widget also provides buttons to reset the selection, toggle the measurement display in the [3D view](3D_view.md), and clear all measurements.
4.  Measurements are automatically discarded when closing the document.

## Notes

-   You cannot use the [Draft](Draft_Workbench.md) snap tools with this command.
-   To add dimensions to drawings use the dimension tools from the [TechDraw Workbench](TechDraw_Workbench.md).
-   For more comprehensive measuring tools, install the <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator Workbench](Manipulator_Workbench.md) (an [external workbench](External_workbenches.md)).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Measure Linear
