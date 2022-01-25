---
- GuiCommand:
   Name:Mesh PolyTrim
   MenuLocation:Meshes → Cutting → Trim mesh
   Workbenches:[Mesh](Mesh_Workbench.md)
   SeeAlso:[Mesh PolyCut](Mesh_PolyCut.md), [Mesh TrimByPlane](Mesh_TrimByPlane.md)
---

# Mesh PolyTrim/pl

## Description

The **Mesh PolyTrim** command trims faces and parts of faces from mesh objects.

## Usage

1.  During the command the [3D view](3D_view.md) cannot be changed. It is advisable to properly line up the 3d view first.
2.  Select one or more mesh objects.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_PolyTrim.svg" width=16px> [Mesh PolyTrim](Mesh_PolyTrim.md)** button.
    -   Select the **Meshes → Cutting → <img src="images/Mesh_PolyTrim.svg" width=16px> Trim mesh** option from the menu.
4.  Define a polygon by picking points in the 3D view.
5.  Select an option from the 3D view context menu:
    -   
        **Inner**
        
        : removes the faces and parts of faces that are inside the polygon.

    -   
        **Outer**
        
        : removes the faces and parts of faces that are outside the polygon.

    -   
        **Split**
        
        : removes the faces and parts of faces that are outside the polygon, and creates a new mesh object containing them.

    -   
        **Cancel**
        
        : cancels the command.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyTrim/pl
