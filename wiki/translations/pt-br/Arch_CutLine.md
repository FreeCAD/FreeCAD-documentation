---
- GuiCommand:
   Name:Arch CutLine
   MenuLocation:Arch → Cut with a line
   Workbenches:[Arch](Arch_Workbench.md)
   Version:0.19
   SeeAlso:[Arch CutPlane](Arch_CutPlane.md)
---

# Arch CutLine/pt-br

## Descrição

The [Arch CutLine](Arch_CutLine.md) tool allows you to cut a solid Arch object like an [Arch Wall](Arch_Wall.md) or [Arch Structure](Arch_Structure.md) using a line that is crossing the object.

<img alt="" src=images/Arch_CutLine_example_1.png  style="width:" height="300px;"> <img alt="" src=images/Arch_CutLine_example_2.png  style="width:" height="300px;">


*[Arch Wall](Arch_Wall.md) cut by a line. Left: subtractive box that appears when using the tool. Right: resulting wall after the cut is done.*

## Utilização

1.  Select the object to be cut in the [tree view](Tree_view.md) or the [3D view](3D_view.md).
2.  Then select the edge to be used to cut the object, for example, a [Draft Wire](Draft_Wire.md). This object should be selected in the [3D view](3D_view.md) only.
3.  Press the **<img src="images/Arch_CutLine.svg" width=16px> [Cut Line](Arch_CutLine.md)** button.
4.  Choose **Behind** or **Front** to indicate what part of the solid will be removed.
5.  Click the **OK** button.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CutLine/pt-br
