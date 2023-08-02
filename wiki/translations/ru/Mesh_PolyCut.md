---
- GuiCommand:
   Name: Mesh PolyCut
   MenuLocation: Meshes -> Cutting -> Cut mesh
   Workbenches: Mesh_Workbench
   SeeAlso: Mesh_PolyTrim, Mesh_TrimByPlane
---

# Mesh PolyCut/ru

## Description

The **Mesh PolyCut** command cuts whole faces from mesh objects.

## Usage

1.  During the command the [3D view](3D_view.md) cannot be changed. It is advisable to properly line up the 3d view first.
2.  Select one or more mesh objects.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_PolyCut.svg" width=16px> [Mesh PolyCut](Mesh_PolyCut.md)** button.
    -   Select the **Meshes → Cutting → <img src="images/Mesh_PolyCut.svg" width=16px> Cut mesh** option from the menu.
4.  Define a polygon by picking points in the 3D view.
5.  Select an option from the 3D view context menu:
    -   
        **Inner**
        
        : removes the faces that are (partially) inside the polygon.

    -   
        **Outer**
        
        : removes the faces that are completely outside the polygon.

    -   
        **Split**
        
        : removes the faces that are completely outside the polygon, and creates a new mesh object containing them.

    -   
        **Cancel**
        
        : cancels the command.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyCut/ru
