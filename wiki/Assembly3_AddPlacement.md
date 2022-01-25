---
- GuiCommand:
   Name:Assembly3 AddPlacement
   Icon:Assembly_Add_Placement.svg‎‎
   MenuLocation:Assembly3 → Workplane and origin → Add placement
   Workbenches:[Assembly3](Assembly3_Workbench.md)
---

# Assembly3 AddPlacement

## Description

The <img alt="" src=images/Assembly_Add_Placement.svg  style="width:24px;"> [Add placement](Assembly3_AddPlacement.md) command adds a Placement to an active assembly.

A Placement object will be created inside the Parts container of the assembly tree and a related placement item will be placed in the 3D view. It is placed at the assembly\'s origin and oriented according to the assembly\'s YZ plane, if the Assembly object was selected directly.

 <img alt="" src=images/Assembly3_AddPlacement-01.png  style="width:250px;"> <img alt="" src=images/Assembly3_AddPlacement-02.png  style="width:350px;"> 



*Left: Tree view. Right: A placement near the assembly origin (shown as file origin here)*

The assembly could be selected indirectly by some other item belonging to the assembly. Then the placement is placed at the item\'s origin and oriented according to this item\'s local coordinate system.

Valid items are e.g. Elements, bodies, vertexes, edges, faces, origins, workplanes, and other placements from either the tree view or the 3D view.

## Usage

1.  Activate the <img alt="" src=images/Assembly_Add_Placement.svg  style="width:16px;"> **Add placement** command using one of the following:
    -   The **<img src="images/Assembly_Add_Placement.svg_" width=16px> [Add placement](Assembly3_AddPlacement.md)** button.
    -   The **Assembly3 → Workplane and origin → <img src="images/Assembly_Add_Placement.svg_" width=16px> Add placement** menu option.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 AddPlacement
