---
 GuiCommand:
   Name: Mesh Export
   MenuLocation: Meshes , Export mesh...
   Workbenches: Mesh_Workbench
   SeeAlso: Std_Export, Import_Export
---

# Mesh Export/hu

## Description

The **Mesh Export** command exports a mesh object to a mesh file format. Several file formats are supported.

## Usage

1.  Select a single mesh object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Export.svg" width=16px> [Mesh Export](Mesh_Export.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_Export.svg" width=16px> Export mesh...** option from the menu.
    -   Select the **<img src="images/Mesh_Export.svg" width=16px> Export mesh...** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.
3.  Select the correct file format in the dialog box.
4.  Enter a filename. If you have selected the {{Value|All files (*.*)}} option in the previous step, and do not specify a file extension here, the **.stl** extension will be used.
5.  Press the **Save** button.

## Notes

-   There are some [export preferences related to Mesh Formats](Import_Export_Preferences#Mesh_Formats.md) but these do not apply to this command. They are used by the [Std Export](Std_Export.md) command.

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To export objects (including mesh objects) to a mesh file format use the `export` method of the Mesh module.


```python
import FreeCAD
import Mesh

doc = FreeCAD.ActiveDocument

Mesh.export([doc.Cone, doc.Cylinder], 'D:/testfiles/mymodel.stl')
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Export/hu
