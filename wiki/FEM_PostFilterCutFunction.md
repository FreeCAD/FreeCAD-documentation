---
- GuiCommand   *
   Name   *FEM PostFilterCutFunction
   MenuLocation   *Results → Function cut filter
   Workbenches   *[FEM](FEM_Workbench.md)
   SeeAlso   *[FEM Result pipeline](FEM_PostPipelineFromResult.md), [FEM Filter functions](FEM_PostCreateFunctions.md), [FEM tutorial](FEM_tutorial.md)
---

# FEM PostFilterCutFunction

## Description

Displays the results on a sphere or a plane cutting through the model.

 <img alt="" src=images/FEM_Function-Cut-Filter-Example.png  style="width   *400px;"> 

*A function cut filter with a sphere as cut function.The original pipeline is the semi-transparent object.*

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md).
2.  Invoke the command either by   *
    -   Pressing the button **<img src="images/FEM_PostFilterCutFunction.svg" width=16px> '''Function cut filter'''**.
    -   Using the menu **Results → <img src="images/FEM_PostFilterCutFunction.svg" width=16px> Function cut filter**.
3.  Adjust the **Result display options** like for the [result pipeline](FEM_PostPipelineFromResult.md). You might need to hide the pipeline to see the effect of the filter in the preview.
4.  Either
    -   If there is no [filter function](FEM_PostCreateFunctions.md) defined yet, press the **<img src="images/List-add.svg" width=16px> Create
** button and select **<img src="images/Fem-post-geo-plane.svg" width=16px> Plane** or **<img src="images/Fem-post-geo-sphere.svg" width=16px> Sphere**
    -   Choose an existing filter function from the list. If needed, adjust the cut parameters to make sure that it intersects the model. Note that changed cut parameters will also change the parameters of the used filter function.
5.  The results will be displayed on the surface of the filter function.
6.  Click the **OK** button to finish the command.




 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterCutFunction
