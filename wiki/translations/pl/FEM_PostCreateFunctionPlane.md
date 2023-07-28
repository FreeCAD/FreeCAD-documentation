---
- GuiCommand:
   Name:FEM PostCreateFunctionPlane
   MenuLocation:Results → Filter Functions → Plane
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM PostCreateFunctionPlane/pl



## Opis

Funkcja <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> **Utwórz płaszczyznę funkcji** określa sposób geometrycznego cięcia siatki. Jest ona wykorzystywana przez narzędzia <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtr funkcji odcięcia](FEM_PostFilterCutFunction/pl.md) oraz <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtr odcięcia obszaru](FEM_PostFilterClipRegion/pl.md).



## Użycie

### Create a plane function 

1.  Either press the **<img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> [Plane](FEM_PostCreateFunctionPlane.md)** button or select the **Results → Filter functions → <img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> Plane** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the origin and the direction of the section plane.
4.  Press the **OK** button to finish.

### Edit a plane function 

If the Plane object in the [3D view](3D_view.md) is hidden, select the <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> Plane object in the [tree view](Tree_view.md) and press **Space** to make it visible, like in this example:

<img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width:300px;">

#### Move the plane 

-   Click and drag the big white cuboid to move the plane along its normal vector.
-   Click and drag the white grid .

#### Rotate and tilt the plane 

-   Click and drag a line that connects the small cubes with the the big white cuboid to rotate and tilt the plane around its origin.

#### Scale the plane 

-   Click and drag one of the 6 small cubes to scale the plane. However, since the object is an infinite plane, the size does not matter.

## Notes

-   Existing functions can be used for different filters and even for different <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [result pipelines](FEM_PostPipelineFromResult.md). It is nevertheless recommended to use a separate set of functions for each pipeline to keep track of the elements in the [tree view](Tree_view.md).





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionPlane/pl
