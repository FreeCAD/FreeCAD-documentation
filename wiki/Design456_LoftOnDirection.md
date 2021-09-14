---
- GuiCommand:
   Name:Design456 LoftOnDirection
   MenuLocation:Design456_Tools → 3DTools → LoftOnDirection
   Workbenches:[Design456](Design456_Workbench.md)
   Shortcut:None
   SeeAlso:
---

## Description

The <img alt="" src=images/Design456_LoftOnDirection.svg  style="width:24px;"> **Design456 Loft on Direction** lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur at felis ut urna auctor pharetra id at nulla. This tool is part of the [external workbench](external_workbenches.md) called [Design456](Design456_Workbench.md).

## Usage

1.  Switch to the <img alt="" src=images/Design456_workbench_icon.svg  style="width:24px;"> [Design456](Design456_Workbench.md) workbench (install from <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) is necessary, if not previously installed)
2.  Select any face
3.  Press the <img alt="" src=images/Design456_LoftOnDirection.svg  style="width:24px;"> LoftOnDirection button. It will ask you to give some data (length, the x -scale, y-scale, z-scale). If you chose 1 for the x,y,z scales, the command will make a normal extrusion. But choosing bigger number will results in scaling the face to a bigger size, or if you chose numbers that is smaller than 1, the produced shape will be smaller than the original face.

The produced object is 3D and solid. Play with the command to find out what you can do with it. Negative numbers result in different object shapes. Depending on the face\'s form, it can create different kind of 3D objects.

## Limitations

Works on 3D objects and might fail sometimes. To be more tested and find out the weaknesses. Giving zero as a scale could cause a failure to the command.

## Properties


{{Properties_Title|Base}}

## Scripting





{{Design456 Tools navi

}} 

[Category:External Command Reference](Category:External_Command_Reference.md)
