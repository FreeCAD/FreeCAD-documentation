---
- GuiCommand:
   Name:Mesh Import
   MenuLocation:Meshes → Import mesh...
   Workbenches:[Mesh](Mesh_Workbench.md)
   SeeAlso:[Std Import](Std_Import.md), [Std Open](Std_Open.md), [Import Export](Import_Export.md)
---

# Mesh Import

## Description

The **Mesh Import** command imports geometry from a mesh file format into the active document. Several file formats are supported. The command creates a non-parametric mesh object, a [Mesh Feature](Mesh_Feature.md).

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Import.svg" width=16px> [Mesh Import](Mesh_Import.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_Import.svg" width=16px> Import mesh...** option from the menu.
    -   Select the **<img src="images/Mesh_Import.svg" width=16px> Import mesh...** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu. This option is only available if an existing mesh object has been selected. Note that the selected object is actually not used or modified by the command.
2.  Optionally select the correct file format in the dialog box.
3.  Select a file.
4.  Press the **Open** button.

## Supported file types 

The **Mesh Import** supports: bms, stl, ast, iv, nas, bdf, obj, smf, off and ply files. For NASTRAN nas/bdf file, only GRID, CTRIA3 and CQUAD4 cards are supported. In each data line, a space must exist between two variables.

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Properties

See: [Mesh Feature](Mesh_Feature.md).

## Scripting

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To import a mesh file use the `insert` method of the Mesh module.

 
```python
import Mesh
Mesh.insert('D:/testfiles/cylinder.stl')
```




 {{Mesh Tools navi}}

---
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Import
