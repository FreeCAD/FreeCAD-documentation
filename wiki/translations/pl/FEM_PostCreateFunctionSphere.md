---
- GuiCommand:
   Name: FEM PostCreateFunctionSphere
   MenuLocation: Results -> Filter Functions -> Sphere
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
---

# FEM PostCreateFunctionSphere/pl



## Opis

Funkcja <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:24px;"> **Utwórz sferę funkcji** określa sposób geometrycznego cięcia siatki. Jest ona wykorzystywana przez narzędzia <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtr funkcji odcięcia](FEM_PostFilterCutFunction/pl.md) oraz <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtr odcięcia obszaru](FEM_PostFilterClipRegion/pl.md).



## Użycie

### Create a sphere function 

1.  Either press the **<img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> [Sphere](FEM_PostCreateFunctionSphere.md)** button or select the **Results → Filter functions → <img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> Sphere** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the origin and the radius of the section sphere.
4.  Press the **OK** button to finish.

### Edit a sphere function 

If the Sphere object in the [tree view](Tree_view.md) is hidden, select the <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:24px;"> Sphere object in the [3D view](3D_view.md) and press **Space** to make it visible, like in this example:

<img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width:400px;">

#### Move the sphere 

-   Click and drag the spherical grid to move the sphere.

#### Scale the sphere 

-   Click and drag one of the 8 small cubes to scale the sphere.

## Notes

-   Existing functions can be used for different filters and even for different <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [result pipelines](FEM_PostPipelineFromResult.md). It is nevertheless recommended to use a separate set of functions for each pipeline to keep track of the elements in the [tree view](Tree_view.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionSphere/pl
