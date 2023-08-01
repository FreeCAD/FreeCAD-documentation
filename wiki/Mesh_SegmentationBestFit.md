---
- GuiCommand:
   Name:Mesh SegmentationBestFit
   MenuLocation:Meshes - Create mesh segments from best-fit surfaces...
   Workbenches:[Mesh](Mesh_Workbench.md)
   SeeAlso:[Mesh Segmentation](Mesh_Segmentation.md)
---

# Mesh SegmentationBestFit

## Description

The **Mesh SegmentationBestFit** command creates separate mesh segments for specified surface types of a mesh object. The command can also identify their parameters which can be useful when re-engineering a mesh object.

## Usage

1.  If you plan to identify the parameters of a surface type, note that the command uses the color red to mark the faces selected for this option. To see them properly:
    -   The **Display Mode** of the mesh object ideally should be {{Value|Flat lines}}, but should at least show faces. If necessary use the [Std DrawStyle](Std_DrawStyle.md) command to override this property.
    -   The **Shape Color** of the mesh object should not be red.
2.  Select a single mesh object.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_SegmentationBestFit.svg" width=16px> [Mesh SegmentationBestFit](Mesh_SegmentationBestFit.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_SegmentationBestFit.svg" width=16px> Create mesh segments from best-fit surfaces...** option from the menu.
4.  The **Mesh segmentation** task panel opens.
5.  Optionally press one of the **Parameters...** buttons to identify the parameters of a surface:
    -   The **Surface fit** dialog box opens.
    -   Select one or more faces belonging to the surface:
        -   Press the **Region** button and while holding down the left mouse button draw a region, a closed spline, in the [3D view](3D_view.md). Faces that (partially) fall inside the region will be selected.
        -   Press the **Triangle** button to select individual faces.
        -   Optionally press the **Clear** button to clear the selection.
    -   Press the **Compute** button to calculate the parameters.
    -   Press the **OK** or **Cancel** button to close the dialog box.
6.  Select the surface type(s) you wish to create mesh segments for:
    -   
        **Plane**
        

    -   
        **Cylinder**
        

    -   
        **Sphere**
        
7.  Specify the **Tolerance** values.
8.  Specify the **Minimum number of faces** values.
9.  Press the **OK** button.
10. The command will create a [group](Std_Group.md) containing separate mesh objects, each a segment of the original mesh object.
11. If the created group is empty try using the command again with modified settings.




 {{Mesh Tools navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SegmentationBestFit
