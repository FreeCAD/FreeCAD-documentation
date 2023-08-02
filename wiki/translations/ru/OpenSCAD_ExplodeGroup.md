---
- GuiCommand:
   Name: OpenSCAD ExplodeGroup
   Name/ru: OpenSCAD ExplodeGroup
   MenuLocation: OpenSCAD -> Расчленить Группу
   Workbenches: OpenSCAD_Workbench/ru
   Shortcut: нет
   SeeAlso: ---
---

# OpenSCAD ExplodeGroup/ru


</div>

## Description

Эта функция разрывает соединение на составляющие, применяя к этим частям случайные цвета.

## Usage

1.  Select fusion/compound to be exploded
2.  Click on <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> or choose **OpenSCAD** → **<img src="images/OpenSCAD_ExplodeGroup.svg" width=32px> Explode Group** from the top menu.

## Limitations

The feature works only on fusions/compounds consisting of:

-   Part primitives from Part Workbench
-   Extruded parts from Part Workbench
-   Revolved parts from Part Workbench

The feature will **NOT** work on:

-   Pads/Revolution-parts from Part Design Workbench
-   Arrays from Draft Workbench

## Notes

For dissolving arrays from Draft Workbench use [Draft Downgrade](Draft_Downgrade.md).





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ExplodeGroup/ru
