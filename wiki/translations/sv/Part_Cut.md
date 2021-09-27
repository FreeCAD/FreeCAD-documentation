# Part Cut/sv
---
- GuiCommand:/sv   Name:Part_Cut   Name/sv:Part Cut   MenuLocation:Part → Cut   Workbenches:_, [Common](Part_Common/sv.md)---


</div>


<div class="mw-translate-fuzzy">

Klipper (subtraherar) valda Del objekt, där den sista subtraheras från den första. Denna operation är helt parametrisk, så de ingående komponenterna kan förändras och resultatet beräknas om.


</div>

Cuts (subtracts) selected Part objects, the last one being subtracted from the first one. This operation is fully parametric and the components can be modified and the result recomputed.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

_

## Usage

1.  Select two shapes
2.  Invoke the Part Cut command several ways:
    -   Press the **![](images/) '''Cut'''** button in the Part toolbar
    -   Use the **Part → Boolean → Cut** entry from the Part menu

## Supported inputs 

Input objects must be [OpenCascade](OpenCascade.md) shapes. Examples: stuff made with Part, PartDesign, Sketcher workbenches. Not meshes (unless those were converted to shapes) - for meshes, there are specific Boolean tools in MeshDesign workbench.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/sv
