# Import from STL or OBJ/en
{{TutorialInfo
|Topic= Import from STL or OBJ
|Level= Beginner
|Time= 30 minutes
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}

## Introduction

In this tutorial we will cover how to import STL/OBJ files in FreeCAD. Since the mesh-format STL/OBJ is dimensionless, FreeCAD will assume on import that the units used in the model are mm. If this is not the case you have to scale your model either in the application it was created with (before exporting it) or you have to scale your model in FreeCAD after import and conversion to a solid.

## Sample part 

For this tutorial you can use your own STL file or create a demo file by doing this   *

-   Open FreeCAD
-   Create a new document
-   Switch to the mesh workbench
-   Insert a torus by clicking on **Meshes** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Regular solid...**, choosing settings like   *
    -   Radius1   * 10 mm
    -   Radius2   * 2 mm
    -   Sampling   * 50
-   Click on **Create** and then on **Close**
-   Save your file with **File** → **Save** to get a FreeCAD-File containing a mesh object

For importing a STL or OBJ file into FreeCAD, create a new FreeCAD document und choose **File** → **Import** from the top menu.

## Cleaning and repairing the STL/OBJ-File for preparing import 

Basically, FreeCAD would import any STL/OBJ-File. But our goal is to have a solid which can be measured and changed (adding pads/pockets ..). For a successful conversion from mesh to solid we need to make sure that the mesh is "water-tight" (has no holes) or doesn't have any other errors.
FreeCAD's aim is not to be a good mesh modeler, it is designed to be a solid modeler. FreeCAD has some capabilities for mesh operation in mesh workbench and OpenSCAD workbench (some operations need OpenSCAD to be installed and configured in the FreeCAD-preferences).
Some users like to use third-party software for cleaning and repairing meshes, for example

-   [Netfabb Basic](http   *//www.netfabb.com/downloadcenter.php?basic=1) (Windows/Linux/Mac) - free for personal use (automatic mesh repair available)
-   [Meshlab](http   *//meshlab.sourceforge.net/) (Windows/Linux/Mac) - Open Source

In this tutorial we will use the mesh workbench within FreeCAD to clean/repair/verify the mesh of our sample file.

### Automatic testing and repairing 

-   Open FreeCAD and the sample FreeCAD file containing the mesh object
-   Switch to mesh workbench
-   Make sure that your mesh object is selected in the tree view
-   Choose **Meshes** → **Analyze** → **Evaluate & Repair mesh...** from the top menu
-   Make sure the pull down menu on the top right corner displays the name of your mesh object
-   With the last point in the list reading \"All above tests together\" click on **Analyze**
-   The texts beside the tick boxes will change to reflect results of the different tests
-   If errors had been detected the corresponding check-boxes will be ticked and you will be able to select **Repair**
-   Choose **Close** to close the menu

### Harmonizing normals 

Harmonizing normals of a mesh object can be done by

-   Selecting your mesh object in the tree view
-   Choose **Meshes** → **<img src="images/Mesh_HarmonizeNormals.svg" width=32px> Harmonize normals** from the top menu.

Tip   * By choosing the mesh object in the tree view, going to the view tab in the property view and changing \"Lighting\" from \"Two Side\" to \"One Side\" you can identify triangles with flipped normals. If the normals point into the mesh the triangle will be shown in black.

### Closing holes 

You can also manually close holes in your mesh object by

-   Selecting your mesh object in the tree view
-   Choose **Meshes** → **Fill holes...** from the top menu
-   Specify maximum number of edges to be filled (3 is default)
-   Since STL and OBJ are meshes consisting of triangles the default number of edges should be sufficient

Another method of manually closing holes in your mesh object would be

-   Selecting your mesh object in the tree view
-   Choose **Meshes** → **<img src="images/Mesh_FillInteractiveHole.svg" width=32px> Close hole** from the top menu
-   Select one of the edges of the hole in the mesh object in the 3D view
-   Right-Click in 3D view and choose **Leave hole-filling mode** to exit the command

## Conversion mesh to solid 

-   Switch to <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part Workbench](Part_Workbench.md)
-   Make sure your mesh object is selected in the tree view, otherwise select it
-   Choose **Part** → **<img src="images/Part_ShapeFromMesh.svg" width=32px> Create shape from mesh ...** from top menu
-   Specify tolerance for sewing shape (0,1 is default)
-   A new object will be created in the tree view (with blue shape icon, instead of green mesh icon)
-   Select the newly created object in the tree view
-   Choose **Part** → **Create a copy** → **<img src="images/Part_RefineShape.svg" width=32px> Refine shape** from the top menu
-   A new object will be created in the tree view and the previous one will be made invisible
-   Select the newly created object in the tree view
-   Choose **Part** → **Convert to solid** from the top menu
-   A new object will be created in the tree view, bearing \"(Solid)\" in its name, to indicate it is a solid

Since the created solid has no history and no editable features (like a simple copy in FreeCAD) you could delete all previous objects from the tree view. This would keep your file size small \...

## Links

-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md)
-   [Import Export](Import_Export.md)


 

[Category   *File\_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Import](Import_Workbench.md) > Import from STL or OBJ/en
