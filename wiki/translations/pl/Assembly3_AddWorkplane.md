---
 GuiCommand:
   Name: Assembly3 AddWorkplane
   Icon: Assembly_Add_Workplane.svg‎‎
   MenuLocation: Assembly3 , Workplane and origin , Add workplane
   Workbenches: Assembly3_Workbench
---

# Assembly3 AddWorkplane/pl

## Description

The <img alt="" src=images/Assembly_Add_Workplane.svg  style="width:24px;"> [Add workplane](Assembly3_AddWorkplane.md) command adds a Workplane to an active assembly.

A Workplane object will be created inside the Parts container of the assembly tree and a related workplane item will be placed in the 3D view. It is placed at the assembly\'s origin and oriented according to the assembly\'s XY plane, if the Assembly object was selected directly.

<img alt="" src=images/Assembly_Add_Workplane-01.png  style="width:250px;"> <img alt="" src=images/Assembly_Add_Workplane-02.png  style="width:350px;">

The assembly can also be selected indirectly by some item belonging to the assembly. Then the workplane is placed at the item\'s origin and oriented according to this item\'s local XY plane.

Valid items are e.g. elements, bodies, vertexes, edges, faces, origins, and other workplanes from either the [Tree view](Tree_view.md) or the [3D view](3D_view.md).

## Usage

1.  Activate the <img alt="" src=images/Assembly_Add_Workplane.svg  style="width:16px;"> **Add workplane** command using one of the following:
    -   The **<img src="images/Assembly_Add_Workplane.svg_" width=16px> [Add workplane](Assembly3_AddWorkplane.md)** button.
    -   The **Assembly3 → Workplane and origin → <img src="images/Assembly_Add_Workplane.svg_" width=16px> Add workplane** menu option.



---
⏵ [documentation index](../README.md) > Assembly3 AddWorkplane/pl
