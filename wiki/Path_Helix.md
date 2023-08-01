---
- GuiCommand:
   Name:Path Helix
   MenuLocation:Path - Helix
   Workbenches:[Path](Path_Workbench.md)
---

# Path Helix

## Description

The <img alt="" src=images/Path_Helix.svg  style="width:24px;"> [Path Helix](Path_Helix.md) tool appends a helical clearing operation to the Job. Clockwise Helix outputs (G2) G-Code commands. Counterclockwise outputs (G3) G-Code commands. Step Over percentage specifies the concentric step-over as a percentage of the Tool diameter. One or more helical paths will be created at progressively different diameters, to clear the hole.

## Usage

-   Select the **[<img src=images/Workbench_Path.svg style="width:16px"> [Path Workbench](Path_Workbench.md)**.
-   Select the **<img src="images/Path_Helix.svg" width=24px>** icon or **Path** → **<img src="images/Path_Helix.svg" width=24px> Helix** from the top menu. This opens the **<img src="images/Path_Helix.svg" width=24px>** Helix configuration panel.
-   You will be prompted with a \"Choose a Tool Controller\" pop-up window to select a Tool Controller. In older versions, in the **<img src="images/Path_Helix.svg" width=24px>** Operation tab, choose a Tool controller and confirm by pressing **Apply**.
-   Open the Base Geometry tab. All available holes compatible with the Helix tool in the Job Model will be selectable for processing. In the [3D view](3D_view.md) select the holes by their edge or wall face and add them with the **Add** button. Check that they appear in the list. Confirm that the list matches the holes that are intended for processing.
-   To remove holes select them in the list and press the **Remove** button.
-   Ensure Start Depth, Final Depth and Step Down (the pitch of the helix) are correct, and adjust if not.
-   Ensure Safe and Clearance Heights are correct, and adjust if not.
-   In the Operation tab, specify the helix Starting surface (outside/inside), Direction (CW/CCW), and Step Over percentage.
-   Click **Apply** to create or update the path, **OK** to apply and close the panel, or **Cancel** to abort and close the panel.

## Options

Extra Offset adds a margin of material to be left unmachined. This is typically to allow a light finishing pass as a separate operation.

## Comments

-   Step Down is not respected exactly. It is always rounded to give a complete number of turns from Start Depth to Final Depth.
-   Similarly Step Over is not respected exactly. It is always rounded to give a number of equal steps.

The feedrate parameter is constant across all cuts and is based on the position of the tool\'s axis, thus actual feedrate of the cutting edge of the tool can vary considerably between the inner most cut and the outside surface. If the job dimensions produce a path diameter smaller than the tool diameter, this can lead to much faster cutting speeds than the feedrate given for the tool in the tool controller. This may need to considered when selecting \"feed and speeds\" for the job.

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
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Helix
