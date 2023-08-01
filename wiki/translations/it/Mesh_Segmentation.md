---
- GuiCommand:
   Name: Mesh_Segmentation
   Name/it: Crea segmenti di mesh
   MenuLocation: Mesh - Crea segmenti di mesh...
   Workbenches: [Mesh](Mesh_Workbench/it.md)
   SeeAlso: [Adatta i segmenti](Mesh_SegmentationBestFit/it.md)
---

# Mesh Segmentation/it

## Descrizione

Il comando **Crea segmenti di mesh** crea segmenti di mesh separati per i tipi di superficie specificati di un oggetto mesh.

## Utilizzo

1.  Select a single mesh object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Segmentation.svg" width=16px> [Mesh Segmentation](Mesh_Segmentation.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_Segmentation.svg" width=16px> Create mesh segments...** option from the menu.
3.  The **Mesh segmentation** task panel opens.
4.  Optionally check the **Smooth mesh** option and specify a value for the smoothness of the mesh. The higher the value the smoother the mesh is assumed to be. Specifying {{Value|0}} has the same effect as unchecking this option. Do not select this option if you want to create planar segments.
5.  Select the surface type you wish to create mesh segments for. You can select more than one type, but this can lead to poorer results. The available surface types are:
    -   
        **Plane**
        

    -   
        **Cylinder**
        

    -   
        **Sphere**
        

    -   
        **Freeform**
        
6.  Specify the required settings. Make sure the **Tolerance** values are not too low, and the **Minimum number of faces** values not too high.
7.  Press the **OK** button.
8.  The command will create a [group](Std_Group.md) containing separate mesh objects, each a segment of the original mesh object.
9.  If the created group is empty try using the command again with modified settings.

## Note

-   The current version of the command has trouble identifying faces at the edges of surface types.
-   In some cases the [Mesh SegmentationBestFit](Mesh_SegmentationBestFit.md) command will produce better results.


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Segmentation/it
