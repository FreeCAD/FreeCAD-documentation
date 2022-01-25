---
- GuiCommand:
   Name:Part Measure Linear
   MenuLocation:Measure → Measure Linear
   Workbenches:[Part](Part_Workbench.md)
---

# Part Measure Linear

## Description

This tool measures the distance between two selected topology elements (vertex, edge, face) and displays the measurement in the [3D view](3D_view.md). The shortest distance between the two elements is shown in red, and delta measurements (distances parallel to standard X, Y, Z axes) are shown in green.

 <img alt="" src=images/MeasureLinear3D1.png  style="width:400px;"> <img alt="" src=images/MeasureLinearDelta1.PNG  style="width:400px;"> 

## Usage

1.  Select any combination of two elements: vertices, edges, faces
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/Part_Measure_Linear.svg style="width:16px"> '''Measure Linear'''** button.
    -   Use the **Measure → Measure Linear** entry in the top menu
3.  Alternatively the command can be launched without prior selection. A selection dialog then opens in the [Task panel](Task_panel.md). A Control widget also provides buttons to reset the selection, toggle the measurement display in the [3D view](3D_view.md), and clear all measurements.
4.  Measurements are automatically discarded when closing the document.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Measure Linear
