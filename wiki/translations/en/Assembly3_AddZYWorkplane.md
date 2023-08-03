---
 GuiCommand:
   Name: Assembly3 AddZYWorkplane
   Icon: Assembly_Add_WorkplaneZY.svg‎‎
   MenuLocation: Assembly3 , Workplane and origin , Add ZY workplane
   Workbenches: Assembly3_Workbench
---

# Assembly3 AddZYWorkplane/en

## Description

The <img alt="" src=images/Assembly_Add_WorkplaneZY.svg  style="width:24px;"> [Add ZY workplane](Assembly3_AddZYWorkplane.md) command adds a ZY Workplane to an active assembly.

A Workplane object will be created inside the Parts container of the assembly tree and a related workplane item will be placed in the 3D view. It is placed at the assembly\'s origin and oriented according to the assembly\'s YZ plane, if the Assembly object was selected directly.

<img alt="" src=images/Assembly_Add_Workplane-01.png  style="width:250px;"> <img alt="" src=images/Assembly_AddZYWorkplane-04.png  style="width:350px;">

The assembly can also be selected indirectly by some item belonging to the assembly. Then the workplane is placed at the item\'s origin but it is still oriented according to the assembly\'s YZ plane.

Valid items are e.g. elements, bodies, vertexes, edges, faces, origins, and other workplanes from either the [Tree view](Tree_view.md) or the [3D view](3D_view.md).

## Usage

1.  Activate the <img alt="" src=images/Assembly_Add_WorkplaneZY.svg  style="width:16px;"> **Add ZY workplane** command using one of the following:
    -   The **<img src="images/Assembly_Add_WorkplaneZY.svg" width=16px> [Add ZY workplane](Assembly3_AddZYWorkplane.md)** button.
    -   The **Assembly3 → Workplane and origin → <img src="images/Assembly_Add_WorkplaneZY.svg" width=16px> Add ZY workplane** menu option.



---
⏵ [documentation index](../README.md) > Assembly3 AddZYWorkplane/en
