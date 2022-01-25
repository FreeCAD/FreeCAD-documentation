---
- GuiCommand:
   Name:Mesh HarmonizeNormals
   MenuLocation:Meshes → Harmonize normals
   Workbenches:[Mesh](Mesh_Workbench.md)
   SeeAlso:[Mesh FlipNormals](Mesh_FlipNormals.md)
---

# Mesh HarmonizeNormals/pl

## Description

The **Mesh HarmonizeNormals** command harmonizes the normals of mesh objects.

## Usage

1.  Select one or more mesh objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_HarmonizeNormals.svg" width=16px> [Mesh HarmonizeNormals](Mesh_HarmonizeNormals.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_HarmonizeNormals.svg" width=16px> Harmonize normals** option from the menu.

## Notes

-   This command can produce a mesh with flipped normals. The [Mesh FlipNormals](Mesh_FlipNormals.md) command can be used to correct this.
-   For a clear indication of the orientation of the faces of mesh objects make sure the **Lighting** property of the mesh objects is set to {{Value|One side}}. The color of the back side of their faces will then depend on the backlight settings: **Edit → Preferences... → Display → 3D View → Backlight color - Intensity**. See: [Preferences Editor](Preferences_Editor#3D_View.md).





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh HarmonizeNormals/pl
