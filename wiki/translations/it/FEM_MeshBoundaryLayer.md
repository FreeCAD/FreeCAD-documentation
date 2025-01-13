# FEM MeshBoundaryLayer/it
---
 GuiCommand:   Name: FEM_MeshBoundaryLayer   Name/it: FEM MeshBoundaryLayer   Icon: Fem-femmesh-boundary-layer.svg   MenuLocation:  Mesh , FEM Mesh boundary layer   ---


</div>



## Descrizione

The **FEM MeshBoundaryLayer** command enables the user to set a localized set of meshing parameters by selecting a set of elements (Vertex, Edge, Face) and applying the parameters to it.

It is especially useful for refining meshes close to edges or surfaces in flow simulations. For example, it can be used to refine the mesh in the vicinity of an air foil or obstacle in a flow.

The boundary layer has the advantage of creating highly defined, anisotropic meshes. As the name implies it supports accurate calculations near boundaries, e.g. a wall where friction occurs, generating a velocity gradient.



## Utilizzo

1.  To enable the function a mesh must be first provided <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:16px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md).
    -   Select the Mesh object in the Model Tree and press the **<img src="images/FEM_MeshBoundaryLayer.svg" width=16px> [FEM mesh boundary layer](FEM_MeshBoundaryLayer.md)** button.
    -   Select the Mesh object in the Model Tree and select the **Mesh → <img src="images/FEM_MeshBoundaryLayer.svg" width=16px> FEM mesh boundary layer** option from the menu.
2.  Edit the start element size, the growth rate and the number of growth layers.
3.  Select a vertex, edge, face.
4.  Click the **OK** button.
5.  Close the task.

    :   Result: You now should see a new `FEMMeshBoundaryLayer` object under the `FEMMeshGMSH` object (see example #3 below) in your active analysis container.
6.  Double-click on the `FEMMeshGMSH` parent object in your Model Tree and press **Apply** to force a mesh recalculation.
7.  Close the task.

After the mesh has been created you can change its properties using the [property editor](Property_editor.md). After you changed a property, you must reopen the Gmsh dialog again and click the **Apply** button. (You can leave the dialog open while changing properties.)

You can create as many different mesh boundary layers as needed.

## Visual examples 

<img alt="" src=images/FEMMeshBoundaryLayer_Example1.png.png  style="width:300px;"> 
*Example 1: The initial coarse FEMMeshGMSH on a 2D case*

<img alt="" src=images/FEMMeshBoundaryLayer_Example2.png.png  style="width:300px;"> 
*Example 2: After applying a Mesh boundary layer*

<img alt="" src=images/FEMMeshBoundaryLayer_Example3.png.png  style="width:300px;"> 
*Example 3: A simple example of the resulting Model Tree*

## Notes

## Related





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshBoundaryLayer/it
