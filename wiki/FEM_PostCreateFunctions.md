---
- GuiCommand   *
   Name   *FEM CompPostCreateFunctions
   MenuLocation   *Results → Filter Functions
   Workbenches   *[FEM](FEM_Workbench.md)
   SeeAlso   *[FEM tutorial](FEM_tutorial.md)
---

# FEM PostCreateFunctions

## Description

For the result filters [Funtion cut filter](FEM_PostFilterCutFunction.md) and [Region cut filter](FEM_PostFilterClipRegion.md) it is necessary how the mesh is cut geometrically. At the moment you can choose between the geometric functions <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *32px;"> Plane and <img alt="" src=images/Fem-post-geo-sphere.svg  style="width   *32px;"> Sphere.

## Usage

To create a function, use the toolbar button <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *32px;"> or <img alt="" src=images/Fem-post-geo-sphere.svg  style="width   *32px;"> (whatever is currently visible). Note the small triangle besides it allowing you to choose the function type. Alternatively use the menu **Results → Filter functions → <img src="images/Fem-post-geo-plane.svg" width=16px> Plane / <img src="images/Fem-post-geo-sphere.svg" width=16px> Sphere**.

To edit a function see the section [Types](#Types.md) below.

Existing functions can be used for different filters and even for different [result pipelines](FEM_PostPipelineFromResult.md). It is nevertheless recommended to use for every pipeline on own set of functions to keep the overview in the [document tree](Tree_view.md).

## Types

### Plane

Planes appear in the document tree with the icon <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *32px;">. When they are made visible in the tree, they look like this   *

 <img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width   *400px;"> 

To move the plane, Click on the big white cuboid that is perpendicular to the plane and keep the mouse button pressed while the mouse is moved. Or click on white grid and keep the mouse button pressed while the mouse is moved

To rotate and tilt the plane, click on a line that connects the small cubes with the the big white cuboid and keep the mouse button pressed while the mouse is moved.

The 6 small cubes are handles to adjust the size. However, since the object is an infinite plane, the size does not matter.

### Sphere

Spheres appear in the document tree with the icon <img alt="" src=images/Fem-post-geo-sphere.svg  style="width   *32px;">. When they are made visible in the tree, they look like this   *

 <img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width   *400px;"> 

The 8 small cubes around the spherical grid are handles to adjust the sphere size. To use them, click a cube and keep the mouse button pressed while the mouse is moved.

To move the sphere position, click the spherical grid and keep the mouse button pressed while the mouse is moved.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctions
