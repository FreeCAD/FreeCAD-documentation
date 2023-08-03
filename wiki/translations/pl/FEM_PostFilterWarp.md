---
 GuiCommand:
   Name: FEM PostFilterWarp
   MenuLocation: Results , Wrap filter
   Workbenches: FEM_Workbench
   SeeAlso: FEM_PostPipelineFromResult, FEM_tutorial
---

# FEM PostFilterWarp/pl

## Description

Displays the deformed shape of the model using a specified scale factor. Therefore a warp filter only has an effect for result vectors that deform the shape.

The result will be the same like with the *Displacement* slider of the [result show](FEM_ResultShow.md) dialog with the difference that the displacement is for the Warp filter in the SI unit meter. For example if you use a [unit system](Preferences_Editor#Units.md) where the length unit is mm and set a displacement factor of 100 in the [result show](FEM_ResultShow.md) dialog, you need to set for the Warp filter a factor of 100.000 to get the same result.

![](images/FEM_Warp-Filter-Example.gif )

*A warp filter of the displacement of a beam clamped on one side.*

## Usage

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md).
2.  Invoke the command either by:
    -   Pressing the button **<img src="images/FEM_PostFilterWarp.svg" width=16px> '''Warp filter'''** button.
    -   Using the menu **Results → <img src="images/FEM_PostFilterWarp.svg" width=16px> Warp filter**.
3.  Adjust the **Result display options** like for the [result pipeline](FEM_PostPipelineFromResult.md). Hide that pipeline to see the effect of a Warp Filter.
4.  Specify the **Warp factor** directly or use the slider to set it. The **Min warp** and **Max warp** fields allow you to adjust the range of the slider.
5.  Click the **OK** button to finish the command.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterWarp/pl
