---
- GuiCommand:
   Name:Path Helix
   MenuLocation:Path → Helix
   Workbenches:[Path](Path_Workbench.md)
---

# Path Helix

## Description

The <img alt="" src=images/Path_Helix.svg  style="width:24px;"> [Path Helix](Path_Helix.md) command appends a helical interpolation Operation to the Job. Clockwise Helix interpolation outputs (G2) G-Code commands. Counterclockwise outputs (G3) G-Code commands. Step Over percentage specifies the concentric step-over as a percentage of the Tool diameter.

## Usage

-   Select the **[<img src=images/Workbench_Path.svg style="width:16px"> [Path Workbench](Path_Workbench.md)**
-   Select the **<img src="images/Path_Helix.svg" width=24px>** icon or **Path** → **<img src="images/Path_Helix.svg" width=24px> Helix** from the top menu. This opens the configuration panel.
-   Choose a Tool controller and confirm by pressing **Apply**
-   All available holes compatible to the Helix tool in the Job Model will be selectable for processing. Upon acknowledging, the tool will create a path for those listed in the Base Geometry tab. Confirm that the list matches the holes that are intended for processing. Adjust using add, enable, or disable, as necessary. Note that holes can also be selected by their edge as well as by their wall faces.
-   Ensure Start Depth, Final Depth and step down are correct, and adjust if not.
-   Ensure Safe and Clearance Heights are correct, and adjust if not.
-   In the Operation tab, specify the Helix Starting point, Direction, and Step Over percentage.
-   Click **Apply** to create or update the path, **OK** to apply and close the panel, or **Cancel** to abort and close the panel.

## Options

Empty

## Properties

### Data

Empty

### View

Empty

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Example:

 
```python
#Place code example here.
```




 {{Path_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Helix
