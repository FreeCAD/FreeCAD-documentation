---
- GuiCommand   *
   Name   *Mesh RemoveCompByHand
   MenuLocation   *Meshes → Remove components by hand...
   Workbenches   *[Mesh](Mesh_Workbench.md)
   SeeAlso   *[Mesh RemoveComponents](Mesh_RemoveComponents.md), [Arch SplitMesh](Arch_SplitMesh.md)
---

# Mesh RemoveCompByHand

## Description

The **Mesh RemoveCompByHand** command removes components from mesh objects.

## Usage

1.  A component refers to a complete group of connected faces. Usually a mesh object contains a single component. But, for example after using the [Mesh Merge](Mesh_Merge.md) command, a mesh object can contain multiple components.
2.  The command uses the color red to mark selected components. To see them properly   *
    -   The **Display Mode** of the mesh objects should show faces. If necessary use the [Std DrawStyle](Std_DrawStyle.md) command to override this property.
    -   The **Shape Color** of the mesh objects should not be red.
3.  Select the **Meshes → <img src="images/Mesh_RemoveCompByHand.svg" width=16px> Remove components by hand...** option from the menu.
4.  The cursor changes to a hand icon.
5.  Select the components you wish to delete in the [3D view](3D_view.md).
6.  Optionally select **Clear selected faces** from the 3D view context menu to deselect all components.
7.  Select **Delete selected faces** from the 3D view context menu to delete the selected components.
8.  Select **Leave removal mode** from the 3D view context menu to finish the command.




 {{Mesh Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemoveCompByHand
