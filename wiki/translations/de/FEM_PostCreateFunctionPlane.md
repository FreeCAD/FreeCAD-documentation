---
- GuiCommand   */de
   Name   *FEM PostCreateFunctionPlane
   Name/de   *FEM NachbearbeitungFunktionEbene
   Icon   *Fem-post-geo-plane.svg
   MenuLocation   *Ergebnisse → Filterfunktionen → Ebene
   Workbenches   *[FEM](FEM_Workbench/de.md)
   SeeAlso   *[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM PostCreateFunctionPlane/de

## Beschreibung

The <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *24px;"> **FEM PostCreateFunctionPlane** function defines how a mesh is cut geometrically. It is used by <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width   *16px;"> [Function cut filter](FEM_PostFilterCutFunction.md) and <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width   *16px;"> [Region clip filter](FEM_PostFilterClipRegion.md).

## Anwendung

### Ebenenfunktion erstellen 

1.  There are several ways to create a function   *
    -   Press the **<img src="images/Fem-post-geo-plane.svg" width=16px> [Plane](FEM_PostCreateFunctionPlane.md)** button.
    -   Select the **Results → Filter functions → <img src="images/Fem-post-geo-plane.svg" width=16px> Plane** option from the menu.
2.  The Implicit function [task panel](Task_panel.md) is opened.
3.  Optionally set the values for the origin and the direction of the section plane.
4.  Press the **OK** button to finish.

### Ebenenfunktion bearbeiten 

If the Plane object in the [3D view](3D_view.md) is hidden, select the <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *24px;"> Plane object in the [tree view](Tree_view.md) and press **Space** to make it visible, like in this example   *

<img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width   *300px;">

#### Die Ebene bewegen 

-   Click and drag the big white cuboid to move the plane along its normal vector.
-   Click and drag the white grid .

#### Die Ebene drehen und neigen 

-   Click and drag a line that connects the small cubes with the the big white cuboid to rotate and tilt the plane around its origin.

#### Die Ebenengröße anpassen 

-   Click and drag one of the 6 small cubes are handles to adjust the size to scale the plane. However, since the object is an infinite plane, the size does not matter.

## Hinweise

-   Existing functions can be used for different filters and even for different <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width   *16px;"> [result pipelines](FEM_PostPipelineFromResult.md). It is nevertheless recommended to use a separate set of functions for each pipeline to keep track of the elements in the [tree view](Tree_view.md).





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionPlane/de
