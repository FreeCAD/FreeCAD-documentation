---
 TutorialInfo:
   Topic: Export to STL or OBJ
   Level: Beginner
   Time: 20 minutes
   Author: r-frank
   FCVersion: 0.16.6703
---

# Export to STL or OBJ/en





## Introduction

In this tutorial we will cover how to export STL/OBJ-files from FreeCAD. The mesh-format STL/OBJ is dimensionless; FreeCAD will assume on export that the units used in the model are in mm. If this is not the case you have to scale your model. One way to do this is using <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> [Draft Scale](Draft_Scale.md).

## Sample part 

You can use your own FreeCAD file, but you can also create a quick test file:

1.  Open FreeCAD.
2.  Create a new document.
3.  Switch to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md).
4.  Insert a cube by clicking on <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Box/Cube](Part_Box.md).
5.  Insert a cone by clicking on <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cone](Part_Cone.md).
6.  Select both objects in the [tree view](Tree_view.md).
7.  Apply a fusion by clicking on <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Part Fuse](Part_Fuse.md).
8.  Save your file.

## Export Method 1: Using \"File → Export\" 

1.  With the default settings, this method creates a mesh with noticeably jagged curves. To get a smoother finish when e.g. 3D printing, the mesh resolution should be configured:
    1.  Make sure the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md) has been loaded (it is not loaded by default).
    2.  Go to **Edit → Preferences... → Import-Export → Mesh Formats**.
    3.  Change **Maximum mesh deviation**. A lower value will produce a mesh with a higher resolution.
2.  Select the solid to be exported in the tree view.
3.  Choose **File → Export...** and set the file type to **STL mesh (*.stl *.ast)**.
4.  Enter your file name. The default extension is **.stl**. You must include the extension **.ast** to produce an **.ast** file.
5.  Choose **Save**.

## Export Method 2: Using the Mesh Workbench in FreeCAD 

1.  Switch to the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md).
2.  Select the solid to be meshed in the tree view.
3.  Choose **Meshes  →  <img src="images/Mesh_FromPartShape.svg" width=24px> Create Mesh from shape...** from the main (top) menu.
4.  Select one of the available meshers and specify the available options. For more information refer to [Mesh from Shape](Mesh_FromPartShape.md).
5.  Choose **OK**. The mesh object will be created in the tree view (with a green mesh icon <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">).
6.  Right click the mesh object in the tree view and choose **<img src="images/Mesh_Export.svg" width=24px> Export mesh...**.
7.  Fill in the file name, the extension is not necessary. The extension will be set based on the file type. If you include an extension which does not match the selected file type, an extension for the selected type will be added when the file is saved.
8.  The default file type is **Binary STL (*.stl)**. Change the type if you wish.
9.  Choose **Save**.

## Which Method to choose ? 

-   Method 1 can be used for most situations where a mesh file is needed.
-   With method 2 you can verify the mesh in FreeCAD. And if you have more than one solid to convert you can use Tools from the [Mesh Workbench](Mesh_Workbench.md). For example, you can fuse meshes before exporting.

## Links

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Import Export](Import_Export.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Export to STL or OBJ/en
