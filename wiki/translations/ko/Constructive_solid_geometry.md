# Constructive solid geometry/ko
## 소 개 

[Constructive solid geometry](https://en.wikipedia.org/wiki/Constructive_solid_geometry) (**CSG**) is a modelling paradigm that is used in many traditional CAD systems. It essentially consists of using primitive solid objects and doing boolean operations with them, such as fusion, subtraction and intersection, in order to create a final shape.

In FreeCAD, this method is mostly utilized with the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md), which has the ability of creating primitive objects like <img alt="" src=images/Part_Box.svg  style="width:24px;"> [boxes](Part_Box.md), <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> [cylinders](Part_Cylinder.md), and <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> [spheres](Part_Sphere.md) and fuse them together, or use them to cut other objects with tools like **<img src="images/Part_Cut.svg" width=24px> [Part Cut](Part_Cut.md)**.

<img alt="" src=images/Part_Constructive_Solid_Geometry_workflow.svg  style="width:800px;">



*Constructive solid geometry (CSG) workflow; any number of operations can be done on solid primitives to create other solid objects, and then fuse or cut them until the final shape is produced.*

Alternatively, the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md) uses a more modern approach than simple CSG; this method is called [feature editing](feature_editing.md), which means creating a base solid, and then adding sequential parametric transformations to obtain a final body.


**Note:**

A [PartDesign Body](PartDesign_Body.md) created with the [PartDesign Workbench](PartDesign_Workbench.md) can also be used in a boolean operation with other objects.

## Example

<img alt="" src=images/Part_CGS_workflow_example.svg  style="width:600px;">



*Example of constructive solid geometry (CSG) workflow: primitive parts are fused (union); the intersection of two other primitive parts is calculated (common); the difference (cut) of the two previous shapes is obtained.*

## Tutorials

The [tutorials](tutorials.md) page provides some examples on creating solids with the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) that use the **CSG** method.

-   [Traditional modeling, the CSG way](Manual:Traditional_modeling,_the_CSG_way.md)
-   [Wiffle ball tutorial](Whiffle_Ball_tutorial.md)
-   [Basic modeling tutorial](Basic_modeling_tutorial.md)



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [Part](Category_Part.md) > Constructive solid geometry/ko
