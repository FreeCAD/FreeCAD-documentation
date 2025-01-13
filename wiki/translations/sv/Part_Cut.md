# Part Cut/sv
---
 GuiCommand:   Name: Part_Cut   Name/sv: Part Cut   MenuLocation: Part , Cut   Workbenches: Part_Workbench/sv   Del, Part Common/sv---


</div>




<div class="mw-translate-fuzzy">

Klipper (subtraherar) valda Del objekt, där den sista subtraheras från den första. Denna operation är helt parametrisk, så de ingående komponenterna kan förändras och resultatet beräknas om.


</div>

The <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **Part Cut** tool cuts (subtracts) selected Part objects, the last one being subtracted from the first one. This operation is fully parametric and the components can be modified and the result recomputed.

This tool is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

<img alt="" src=images/Part_Cut_01.png  style="width:480px;">

## Usage

1.  Select two shapes.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Part_Cut.svg" width=16px> [Cut](Part_Cut.md)** button.
    -   Select the **Part → Boolean → <img src="images/Part_Cut.svg" width=16px> Cut** option from the menu.

## Supported inputs 

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. For example objects made with the Part, PartDesign or Sketcher workbenches. For meshes there are dedicated Boolean tools in [Mesh Workbench](Mesh_Workbench.md).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/sv
