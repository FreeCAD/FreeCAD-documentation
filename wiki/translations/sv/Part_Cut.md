# Part Cut/sv
---
- GuiCommand:/sv   Name:Part_Cut   Name/sv:Part Cut   MenuLocation:Part → Cut   Workbenches:[Komplett](Part_Workbench/sv___Del]],[[Complete_Workbench/sv.md)|SeeAlso:[Union](Part_Union/sv.md), [Common](Part_Common/sv.md)---


</div>




<div class="mw-translate-fuzzy">

Klipper (subtraherar) valda Del objekt, där den sista subtraheras från den första. Denna operation är helt parametrisk, så de ingående komponenterna kan förändras och resultatet beräknas om.


</div>

Cuts (subtracts) selected Part objects, the last one being subtracted from the first one. This operation is fully parametric and the components can be modified and the result recomputed.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

[480px\|left\|Cut](IMAGE:Part_Cut_01.png.md)

## Usage

1.  Select two shapes
2.  Invoke the Part Cut command several ways:
    -   Press the **![](images/) '''Cut'''** button in the Part toolbar
    -   Use the **Part → Boolean → Cut** entry from the Part menu

## Supported inputs 

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. For example objects made with the Part, PartDesign or Sketcher workbenches. For meshes there are dedicated Boolean tools in [Mesh Workbench](Mesh_Workbench.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/sv
