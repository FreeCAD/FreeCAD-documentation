---
 GuiCommand:
   Name: Std_Measure
   MenuLocation: View , Measure
   Workbenches: All
   Shortcut: 
   Version: 0.22
   SeeAlso: 
---

# Sandbox Measurement

## Description

The **Std_Measure** command opens a task panel to display information about selected objects. The command displays a measurement type that works with the given selection (distance for two points, area for a face, angle for two edges, etc). Measurement information can optionally be added to the 3d view.

The **Std_Measure** command is available in many (all?) workbenches.

## Usage

There are two ways to use the **Std_Measure** command:

1.  Select the geometry to be measured (vertices, edges or faces).
2.  Press the **<img src="images/UMF-Measurement.svg" width=16px> [Std_Measure](Measure_Std_Measure.md)
**
3.  A task panel opens showing the selected geometry and appropriate information.

\- or -

1.  Press the **<img src="images/UMF-Measurement.svg" width=16px> [Std_Measure](Measure_Std_Measure.md)** button.
2.  An empty task panel opens.
3.  Select geometry to be measure. The task panel is updated with information about the selection.

In either case, press the **Annotate** button to add the measurement information to the 3D view (and exit the command??)

To exit the **Std_Measure** command press **ESC** or the **Close** button.

## Scripting

The **Std_Measure** command is available to Python scripts as TBD

## Notes

-   This command is a product of the 2023 Google Summer of Code.




 {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Sandbox Measurement
