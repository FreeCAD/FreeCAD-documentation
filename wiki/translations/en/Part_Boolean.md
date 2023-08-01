---
- GuiCommand:
   Name:Part Boolean
   MenuLocation:Part - Boolean - Boolean...
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Cut](Part_Cut.md), [Part Fuse](Part_Fuse.md), [Part Common](Part_Common.md), [Part Section](Part_Section.md)
---

# Part Boolean/en

## Description


**[<img src=images/Part_Boolean.svg style="width:16px"> [Part Boolean](Part_Boolean.md)**

is a generic all-in-one boolean tool. It allows you to specify the objects and operation to perform via a single dialog.

For quicker access to these operations, use **[<img src=images/Part_Cut.svg style="width:16px"> [Part Cut](Part_Cut.md)**, **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Fuse](Part_Fuse.md)**, **[<img src=images/Part_Common.svg style="width:16px"> [Part Common](Part_Common.md)** and **[<img src=images/Part_Section.svg style="width:16px"> [Part Section](Part_Section.md)**.

![](images/PartBooleansDialog.png )



*Dialog to select objects and perform boolean operations with them.*

## Usage

See the individual commands:

-    **<img src="images/Part_Cut.svg" width=16px> [Part Cut](Part_Cut.md)
**
    

-    **<img src="images/Part_Fuse.svg" width=16px> [Part Fuse](Part_Fuse.md)
**
    

-    **<img src="images/Part_Common.svg" width=16px> [Part Common](Part_Common.md)
**
    

-    **<img src="images/Part_Section.svg" width=16px> [Part Section](Part_Section.md)
**
    

Also see the **Part → Create a copy → [Refine Shape](Part_RefineShape.md)** menu.

## Coplanar problems 

The boolean operations are performed by the internal geometry kernel, [OpenCASCADE Technology](OpenCASCADE.md) (OCCT). This library sometimes has problems producing boolean results when the input objects share an edge or a face. To be sure the boolean operation is successful the recommendation is that the shapes intersect each other clearly; this means that in most cases, one shape should protrude or be larger in size than the other shape.

In cases of coplanarity, even if the first boolean operation succeeds, subsequent boolean operations may fail. In this case, the problem may not be in the last operation done, but in the older ones, that is, in the nested operations as indicated in the [tree view](Tree_view.md). To troubleshoot these issues, it is recommended to use the **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part CheckGeometry](Part_CheckGeometry.md)** tool to inspect all objects for problems.

<img alt="" src=images/Part_Boolean_cut_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_cut_coplanar_2.png  style="width:500px;">



*Left: shapes that share a face, a boolean cut may produce incorrect results. Right: shapes that intersect each other clearly, the boolean cut will be successful in most cases.*

<img alt="" src=images/Part_Boolean_fusion_coplanar_1.png  style="width:500px;">

<img alt="" src=images/Part_Boolean_fusion_coplanar_2.png  style="width:500px;">



*Left: shapes that share a face, a boolean union may produce incorrect results. Right: shapes that intersect each other clearly, the boolean union will be successful in most cases.*



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Boolean/en
