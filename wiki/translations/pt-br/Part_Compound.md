---
- GuiCommand   *
   Name   *Part Compound‏‎
   MenuLocation   *Part → Make compound
   Workbenches   *[Part](Part_Workbench.md)
   Version   *0.14
   SeeAlso   *[Part Fuse](Part_Fuse.md), [Part CompoundFilter](Part_CompoundFilter.md), [Part ExplodeCompound](Part_ExplodeCompound.md)
---

# Part Compound/pt-br

## Description

This command creates a compound of objects with a topological shape such as solid objects and other objects with faces and/or edges. It cannot handle meshes as they do not have a topological shape.

## Usage

1.  Mark the topological shapes to be added to the compound in the [tree view](Tree_view.md)
2.  Choose **Part → Compound → Make Compound** entry in the Part menu or click on the <img alt="" src=images/Part_Compound.svg  style="width   *24px;"> button.

## Notes

A compound containing pieces that intersect or touch is **invalid** for Boolean operations. Because of performance issues, checking if the pieces intersect is not done by default. Automatic geometry check (available for Boolean operations) is disabled for part compound as well.

To turn this check on go to **Tools → Edit Parameters → Preferences... → Mod → Part → CheckGeometry → RunBOPCheck** and set the parameter to `true`.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/pt-br
