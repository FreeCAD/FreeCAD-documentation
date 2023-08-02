---
- GuiCommand:
   Name: FEM PostFilterContours
   MenuLocation: Results -> Contours filter
   Workbenches: FEM_Workbench
   Version: 0.21
   SeeAlso: FEM_PostPipelineFromResult, FEM_PostCreateFunctions, FEM_tutorial
---

# FEM PostFilterContours/de


</div>



## Beschreibung


<div lang="en" dir="ltr" class="mw-content-ltr">

Creates iso-contours and iso-lines in the results mesh.


</div>

<img alt="" src=images/FEM_PostFilterContours_Example.png  style="width:400px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Iso-contours, depicting the y-component of the absolute magnetic<br>
flux density in and around a copper wire that is flown through by<br>
an electric current at a frequency of 100 kHz.<br>
For more info about this model, see section 14 of the [https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf Elmer Tutorials].*


</div>



## Anwendung


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select a previously created [result pipeline](FEM_PostPipelineFromResult.md).
2.  Create the filter either by pressing the button **<img src="images/FEM_PostFilterContours.svg" width=16px> '''Contours filter'''** or by using the menu **Results → <img src="images/FEM_PostFilterContours.svg" width=16px> Contours filter**.
3.  Adjust the **Result display options** like for the [result pipeline](FEM_PostPipelineFromResult.md). You might need to hide the pipeline to see the effect of the filter in the preview.
4.  In the dialog that appears set the result field and the number of contours.
5.  Click the **OK** button to finish the command.


</div>



## Optionen


<div lang="en" dir="ltr" class="mw-content-ltr">

The dialog offers the following settings:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   **Field**: The results field to be drawn.
-   **Vector**: If the **Field** is a vector, the vector components.
-   **Number of contours**: The number of contours to be created. **Note:** depending on the geometry the created number of contours can be higher than specified. This is caused by the creation algorithm. However, for 2D and simple 3D geometries, the number should be correct.
-   **No color**: Don\'t apply a color to the contours.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

**Note**: A **Field** can only be set if a filter function exists and has been applied with <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:16px;"> [Apply Changes](FEM_PostApplyChanges.md). Alternatively you can reopen the filter dialog.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## File Size Information 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Setting a Contours filter can increase the file size significantly. The reason is that the algorithm needs to copy the [Post result pipeline](FEM_PostPipelineFromResult.md). A single contour does not need the whole mesh and the algorithm only requires half the pipeline storage size to create a contour. But this will be the size increase for every contour. Take for example the case where the pipeline storage size is 1 MB, adding a Contours filter with 10 contours will then lead to a 5 MB larger file size.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The storage size of the pipeline depends on the used mesh. The finer the mesh, the larger the pipeline size. Therefore be careful if you have large meshes and a large number of contours.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If you use contours only on a part of the mesh, for example when you have a clip filter, then create the Contours filter on the filter and not on the pipeline. If you do need the whole pipeline, start with a few contours and then step by step go up until the file size is still acceptable while the visualization is as you like it.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterContours/de
