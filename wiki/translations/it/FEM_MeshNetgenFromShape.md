---
 GuiCommand:
   Name: FEM_MeshNetgenFromShape
   Name/it: Mesh FEM da forma con Netgen
   MenuLocation: FEM , Mesh FEM da forma con Netgen
   Workbenches: FEM_Workbench/it
   Shortcut: 
   SeeAlso: FEM_tutorial/it
---

# FEM MeshNetgenFromShape/it


</div>



## Descrizione

For a finite element analysis, the geometry needs to be discretized into a [FEM Mesh](FEM_Mesh.md). This command uses [Netgen](https://www.ngsolve.org/) (which needs to be installed on the system) to generate the mesh. Netgen meshes are not supported by [Elmer](FEM_SolverElmer.md).

Depending on your operating system and installation package, Netgen might be bundled with FreeCAD or not. For further information see [FEM Install](FEM_Install.md).



## Utilizzo

1.  Select the shape you want to analyze. For a volume, this needs to be solid or compsolid. A compsolid is necessary if your part is made from multiple materials (a compsolid can be created with the [Part BooleanFragments](Part_BooleanFragments.md) command).
2.  Activate the tool in one of the following ways:
    -   Press the **<img src="images/FEM_MeshNetgenFromShape.svg" width=16px> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape.md)** button.
    -   Select the **Mesh → <img src="images/FEM_MeshGmshFromShape.svg" width=16px> FEM mesh from shape by Netgen** option from the menu.
3.  Optionally, set the max/min element size (the default setting usually creates meshes that are too coarse) and element order (using the *Second Order* checkbox).
4.  Optionally, change the *Fineness* to one of the predefined choices or choose *UserDefined* and manually edit the parameters.
5.  Click the **Apply** button to generate the mesh. <small>(v1.0)</small> : Optionally, use the **Cancel** button to abort meshing if using the new Netgen implementation.
6.  Click the **OK** button to generate the mesh and close the dialogue. You can also click the **Cancel** button to cancel the changes or creation of the mesh object.

## Properties

-    **Max. Size**: Maximum size of the element in mm.

-    **Min. Size**: <small>(v1.0)</small> : Minimum size of the element in mm.

-    **Second order**: Second order elements contain more nodes per element. Usually, it is enough to use rougher mesh to obtain same solution precision as with the first order elements,

    -   true (default); second order elements,
    -   false; first order elements.

-    **Fineness**: Offers predefined levels of mesh density.

-    **Growth Rate**: Defines how much adjacent elements can differ in size.

-    **Nb. Segs per Edge**: Defines the minimum number of mesh segments per edge.

-    **Nb. Segs per Radius**: Defines the minimum number of mesh segments per radius.

-    **Optimize**:

    -   true (default): applies optimization algorithm to improve mesh quality
    -   false


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshNetgenFromShape/it
