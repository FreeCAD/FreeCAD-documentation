---
 GuiCommand:
   Name: FEM MeshRegion
   Name/ru: Область сетки МКЭ
   MenuLocation:  Mesh , Область сетки МКЭ
   Workbenches: FEM_Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM MeshRegion/ru


</div>



## Описание

Enables the user to set a localized set of meshing parameters by selecting a set of elements (vertex, edge, face) and applying the parameters to it. It is especially useful for refining meshes in areas of interest or areas where the solver will generate a stronger gradient of a variable. For example, it can be used to refine the mesh around stress-risers (sharp edges, holes, notches, \...) in mechanical analysis, or at areas of contraction in a fluid flow.

Refining the mesh has the advantage of enabling accurate simulation where needed, while allowing coarser mesh in the wider domain, thus drastically optimizing the computation time while maintaining meaningful solutions output.



## Применение

1.  To enable the function a <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:16px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md) or (<small>(v1.1)</small> ) <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:16px;"> [FEM mesh from shape by Netgen](FEM_MeshNetgenFromShape.md) must be first provided. Select the Mesh object in the Model Tree and either press the **<img src="images/FEM_MeshRegion.svg" width=16px> [FEM mesh refinement](FEM_MeshRegion.md)** button or use the **Mesh → <img src="images/FEM_MeshRegion.svg" width=16px> FEM mesh refinement** menu option.
2.  Press the **Add** button and select one or more of either *faces*, *edges* or *vertices* in the [3D view](3D_view.md) to apply the mesh refinement to. The selected items will appear in the list of geometrical objects. The selection mode can be also set to *Solid*.
3.  Enter the maximum element size for the region.
4.  Click the **OK** button.
5.  Close the task.

    :   Result: You now should see a new `FEMMeshRegion` object under the `FEMMeshGmsh` or (<small>(v1.1)</small> ) `FEMMeshNetgen` object (see example #3 below) in your active analysis container.
6.  Double-click on the `FEMMeshGmsh` or (<small>(v1.1)</small> ) `FEMMeshNetgen` parent object in your Model Tree and press **Apply** to force a mesh recalculation.
7.  Close the task.

After the mesh has been created, you can change its properties using the [property editor](Property_editor.md). After you change a property, you must reopen the mesh dialog again and click the **Apply** button (you can leave the dialog open while changing properties).

You can create as many different mesh regions as needed.

## Visual examples 

<img alt="" src=images/FEMMeshRegion_Example1.png style="width:300px;"> 
*Example 1: The initial coarse FEM Mesh by GMSH*

<img alt="" src=images/FEMMeshRegion_Example2.png  style="width:300px;"> 
*Example 2: After applying a Mesh refinement using two FEM Mesh Region objects, the large hole is refined to a maximum element size of 3 mm, the smaller hole is refined to 1 mm*

<img alt="" src=images/FEMMeshRegion_Example3.png  style="width:300px;"> 
*Example 3: A simple example of the resulting Model Tree*



## Примечания


<div class="mw-translate-fuzzy">

Порядок, в котором области отображаются в [Древе проекта](Tree_view/ru.md), может изменить результат сетки. См. Эту [ветку форума](https://forum.freecadweb.org/viewtopic.php?f=18&t=41955).


</div>

## Related

-   \"Mesh Regions for a Better Analysis\" - Video Tutorial by Joko Engineering ([link](https://www.youtube.com/watch?v=X5RVe2SDPvw))


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshRegion/ru
