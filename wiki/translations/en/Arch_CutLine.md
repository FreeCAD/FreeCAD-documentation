---
 GuiCommand:
   Name: Arch CutLine
   MenuLocation: Arch , Cut with line
   Workbenches: Arch_Workbench
   Version: 0.19
   SeeAlso: Arch_CutPlane
---

# Arch CutLine/en

## Description

The **Arch CutLine** tool cuts a solid Arch object like an [Arch Wall](Arch_Wall.md) or [Arch Structure](Arch_Structure.md) with a straight edge. Based on that edge and the normal of the [Draft working plane](Draft_SelectPlane.md) a cutting face is generated.

<img alt="" src=images/Arch_CutLine_example_1.png  style="width:" height="300px;"> <img alt="" src=images/Arch_CutLine_example_2.png  style="width:" height="300px;">



*[Arch Wall](Arch_Wall.md) cut by a line. Left: subtractive box that appears when using the tool. Right: resulting wall after the cut is done.*

## Usage

1.  If required align the working plane:
    -   The selected edge may not be parallel to the normal of the working plane.
    -   The generated cutting face will be perpendicular to the working plane.
2.  Select the object to be cut in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
3.  Select a straight edge. This must be selected in the [3D view](3D_view.md).
4.  Press the **<img src="images/Arch_CutLine.svg" width=16px> [Cut with line](Arch_CutLine.md)** button.
5.  Choose **Behind** or **Front** to indicate on which side of the cutting face material should be removed.
6.  Press the **OK** button.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch CutLine/en
