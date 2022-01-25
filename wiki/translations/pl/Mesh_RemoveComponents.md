---
- GuiCommand:
   Name:Mesh_RemoveComponents
   MenuLocation:Meshes → Remove components...
   Workbenches:[Mesh](Mesh_Workbench.md)
   SeeAlso:[Mesh RemoveCompByHand](Mesh_RemoveCompByHand.md), [Arch SplitMesh](Arch_SplitMesh.md)
---

# Mesh RemoveComponents/pl

## Description

The **Mesh RemoveComponents** command removes faces from mesh objects.

![](images/Meshes_RemoveComponents.jpg ) 
*The Remove components task panel*

## Usage

1.  The command uses the color red to mark selected faces. To see them properly:
    -   The **Display Mode** of the mesh objects ideally should be {{Value|Flat lines}}, but should at least show faces. If necessary use the [Std DrawStyle](Std_DrawStyle.md) command to override this property.
    -   The **Shape Color** of the mesh objects should not be red.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_RemoveComponents.svg" width=16px> [Mesh RemoveComponents](Mesh_RemoveComponents.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_RemoveComponents.svg" width=16px> Remove components...** option from the menu.
3.  The **Remove components** task panel opens.
4.  Use one or more of the **Select** options to select faces:
    -   Press the **Region** button and while holding down the left mouse button draw a region, a closed spline, in the [3D view](3D_view.md). Faces that match the **Region options** and (partially) fall inside the region will be selected.
    -   Press the **All** button to select all faces.
    -   Press the **Components** button to select all components with fewer than the specified maximum number of faces. Here a component refers to a complete group of connected faces. Usually a mesh object contains a single component. But, for example after using the [Mesh Merge](Mesh_Merge.md) command, a mesh object can contain multiple components.
    -   Press the **Pick triangle** button to select a single face in the 3D view. If the **Select whole component** option is checked, selecting a face will result in selecting the entire component the face belongs to.
5.  Optionally use one or more of the **Deselect** options to deselect faces. These options are identical to the **Select** options, except that the number of faces for the **Components** button is a minimum number.
6.  Optionally press the **Invert** button to invert the selection.
7.  Press the **Delete** button to delete the selected faces.
8.  Press the **Close** button to close the task panel and finish the command.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveComponents/pl
