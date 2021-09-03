---
- GuiCommand:
   Name:OpenSCAD ExplodeGroup
   MenuLocation:OpenSCAD → Explode Group‏‎
   Workbenches:[OpenSCAD](OpenSCAD_Workbench.md)
---

## Description

This feature explodes a fusion or a compound back to single parts applying random colours to these parts.

## Usage

1.  Select fusion/compound to be exploded
2.  Click on <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> or choose **OpenSCAD** → **<img src="images/OpenSCAD_ExplodeGroup.svg" width=32px> Explode Group** from the top menu.

## Limitations

The feature works only on fusions/compounds consisting of

-   part primitives from part workbench
-   extruded parts from part workbench
-   revolved parts from part workbench

The feature will **NOT** work on

-   pads/revolution-parts from part design workbench
-   arrays from draft workbench

## Notes

For dissolving arrays from draft workbench use the [Draft Downgrade](Draft_Downgrade.md) - tool from draft workbench.




 {{OpenSCAD_Tools_navi}} 
