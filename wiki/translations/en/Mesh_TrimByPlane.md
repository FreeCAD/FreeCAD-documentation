---
- GuiCommand   *
   Name   *Mesh TrimByPlane
   MenuLocation   *Meshes → Cutting → Trim mesh with a plane
   Workbenches   *[Mesh](Mesh_Workbench.md)
   SeeAlso   *[Mesh PolyCut](Mesh_PolyCut.md), [Mesh PolyTrim](Mesh_PolyTrim.md)
---

# Mesh TrimByPlane/en

## Description

The **Mesh TrimByPlane** command trims faces and parts of faces on one side of a plane from a mesh object.

## Usage

1.  Select a single mesh object and a single [Part plane](Part_Plane.md). The (extended) plane should intersect the mesh object.

2.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Mesh_TrimByPlane.svg" width=16px> [Mesh TrimByPlane](Mesh_TrimByPlane.md)** button.
    -   Select the **Meshes → Cutting → <img src="images/Mesh_TrimByPlane.svg" width=16px> Trim mesh with a plane** option from the menu.

3.  The **Trim by plane** dialog box opens.

4.  
    **Select the side you want to keep**by pressing one of the buttons   *

    -   
        {{button|Below}}
        

    -   
        {{button|Above}}
        

    -   
        {{button|Split}}
        
           * removes the faces and parts of faces above the plane, and creates a new mesh object containing them.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh TrimByPlane/en
