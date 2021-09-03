 {{Macro
|Name=Macro MeasureCircle
|Icon=Macro_MeasureCircle.png
|Description=This macro will report the computed radius and center of a circle given 3 vertices or a circular edge.
A line is drawn from the center of the circle to the first vertex, which may be used for future measurements.
|Author=galou_breizh
|Version=1.0
|Date=2016-04-08
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/b/bd/Macro_MeasureCircle.png ToolBar Icon]
}}

## Description

This macro will report the computed radius and center of a circle given 3 vertices or a circular edge. A line is drawn from the center of the circle to the first vertex, which may be used for future measurements.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro}}

## How To Use {#how_to_use}

Copy the macro in your macros\' folder and run (see [How to install macros](How_to_install_macros.md) for further details).

Just select the vertices and the result will be shown in the Report View. Edges may also be selected and count as two vertices. A circular edge can also be selected. If two edges are selected the end vertex of the second edge is not used in the calculation.

You can either select elements and then launch the macro or launch the macro without selection and select elements after launch. If not enough elements are selected before launching the macro, you must select the missing elements.

## Code

The latest version of the macro is to be found at [MeasureCircle.FCMacro](https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/MeasureCircle.FCMacro) but the easiest way to install this macro is through the [Addon Manager](Addon_Manager.md).

ToolBar Icon ![](images/Macro_MeasureCircle.png )

**Macro\_MeasureCircle.FCMacro**




