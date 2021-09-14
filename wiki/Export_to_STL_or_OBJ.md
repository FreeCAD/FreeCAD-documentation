# Export to STL or OBJ

 


{{TutorialInfo
|Topic=Export to STL or OBJ
|Level=Beginner
|Time=20 minutes
|Author=r-frank
|FCVersion=0.16.6703
}}

## Introduction

In this tutorial we will cover how to export STL/OBJ-files from FreeCAD. The mesh-format STL/OBJ is dimensionless; FreeCAD will assume on export that the units used in the model are in mm. If this is not the case you have to scale your model. One way to do this is using <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> [Draft Scale](Draft_Scale.md).

## Sample part 

You can use your own FreeCAD file, but you could also create a quick test file by

-   Opening FreeCAD
-   Create a new document
-   Switch to <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md)
-   Insert a cube by clicking on <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Part Box/Cube](Part_Box.md)
-   Insert a cone by clicking on <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Part Cone](Part_Cone.md)
-   Select both objects in the [tree view](Tree_view.md)
-   Apply a fusion by clicking on <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Part Fuse](Part_Fuse.md)
-   Save your file

## Export Method 1: Using \"File → Export\" 

-   Select the solid to be exported in the tree view.
-   Choose **File** → **Export...** and set file type to \"STL mesh (\*.stl \*.ast)\".
-   Enter your file name. The default extension is \".stl\". You must include the extension \".ast\" in the file name to produce a .ast file. Choose **Save**.

## Export Method 2: Using the Mesh Workbench in FreeCAD 

-   Switch to the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md)
-   Select the solid to be meshed in the tree view.
-   Choose **Meshes** → **<img src="images/Mesh_FromPartShape.svg" width=32px> Create Mesh from shape...** from the main (top) menu.
-   Select one of the available meshers and specify the available options. For more information refer to [Mesh from Shape](Mesh_FromPartShape.md).
-   Choose **OK**. The mesh object will be created in the tree view (with green mesh icon <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">).
-   Right click the mesh object in the tree view and choose **<img src="images/Mesh_Export.svg" width=32px> Export mesh...**.
-   Fill in the file name; the extension is not necessary. The extension will be set based on the file type. If you include an extension which does not match the selected file type, an extension for the selected type will be added when the file is saved. If you include an extension which matches the file type, no additional extension will be added.
-   The default file type is \"Binary STL (\*.stl)\". Change the type if you wish.
-   Choose **Save**.

## Which Method to choose ? 

Method 2 is to be preferred. Among the reasons:

-   When you have more than one Body to convert you can use Tools from <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md). For example, you can fuse meshes before exporting.
-   Curved surfaces are represented in STL as a series of straight-line segments, generated via tessellation. This results in slightly under-sized inside dimensions for curved surfaces. If you are exporting to use in 3D-printing, this may result in an under-sized hole, for example. In such cases you may need a finer tessellation value. When exporting from another workbench using **File** → **Export...**, the tessellation is controlled by the overall display tessellation set in **Edit** → **Preferences...** → Part Design → Shape view. However, because those parameters control the tessellation used to render shapes on the display, decreasing them will slow down display rendering, often significantly. In addition, exporting immediately after changing the display tessellation preference value will not have the desired effect because display tessellation is not updated immediately. One must force a change in the underlying model to cause the tessellation to be recomputed \-- for example, by editing a sketch parameter (Setting it to its original value will suffice).

## Links

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Import Export](Import_Export.md)

 

[Category:File\_Formats](Category:File_Formats.md)
