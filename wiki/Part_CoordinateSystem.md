---
 GuiCommand:
   Name: Part CoordinateSystem
   Workbenches: All
   Version: 1.1
   SeeAlso: Part_DatumPlane, Part_DatumLine, Part_DatumPoint
---

# Part CoordinateSystem

## Description

The **Part CoordinateSystem** command creates a coordinate system object that can be attached to other objects. A coordinate system is one of several [datum objects](Std_Base#Part_Datums.md). A datum object is typically used to attach multiple other objects to. If the position or orientation of a datum object changes, all objects attached to it will follow.

## Usage

1.  Optionally activate the correct container, for example a <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Body](PartDesign_Body.md), a <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Std Part](Std_Part.md) or an <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:16px;"> [Assembly](Assembly_CreateAssembly.md). The datum object is added to the first active container if multiple containers are active.
2.  Optionally select the geometry the datum object should be attached to. If there is an active container the geometry should belong to that container.
3.  Press the **<img src="images/Part_CoordinateSystem.svg" width=16px> [Create coordinate system](Part_CoordinateSystem.md)** button.
4.  The **Attachment** task panel opens.
5.  If no geometry has been selected: optionally press the **OK** button to not attach the datum object and finish the command.
6.  For further steps see [Part EditAttachment](Part_EditAttachment#Usage.md). Continue from step 7 on that page if geometry has been preselected.

## Notes

-   A datum object can also be put into a container by dropping it on the container in the [Tree view](Tree_view.md).
-   The attachment of a datum object can be changed by editing its **Map Mode** property. See [Part EditAttachment](Part_EditAttachment#Usage.md).
-   The axes of a coordinate system are [datum lines](Part_DatumLine.md), its planes are [datum planes](Part_DatumPlane.md), and its origin point is a [datum point](Part_DatumPoint.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CoordinateSystem
