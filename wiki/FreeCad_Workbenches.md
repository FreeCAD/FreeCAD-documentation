# FreeCad Workbenches
# Introduction

This is a fairly **Early Draft**, more for discussion than use. See discussion tab.

One of the ( many ) organizing principals of FreeCad is the WorkBench. So if you are new to FreeCad you need to acquire at least a basic understanding of them. On this page we will list many of the workbenches and some basic understanding of what they do. This is meant to be a 10,000 meter overview, just to help you get oriented.

In the FreeCad GUI you can move between different workbenches by using a drop down list, normally near the top of the FreeCad document window.

FreeCad typically makes complicated objects by building up from simple objects. The tools are broken down into groups called workbenches.

A workbench is a set of tools that can create or modify objects in your model. The sorts of objects each workbench can create is usually limited to a fairly small number ( see discussion below ). Most models are base on creating some ( relatively simple ) objects then modifying them again and again into something complex. Think about taking a block of wood: modify with a saw, then a drill press\.... to a finished object.

The topic of WorkBenches may be a bit confused because some tools occur in multiple workbenches and you can configure the benches by adding or deleting tools. This document is for version number .19, but is based on a moving target, so will not be fully defined now. It should be close enough so you can adapt.

On this page we sometime used a convention of combining the workbench formal name ( as in the dropdown list in FreeCad ) with the word WorkBench thus the PartWorkBench. We have also used shorthand like:

   Sketcher sketches --> Part objects, extrusions and pockets....

to mean that a workbench ( in this case the PartWorkbench, see below ) can take a Sketcher sketch object and transform it into a Part object, an extrusion, pocket or more.

Links to example files will attempt to show very simple examples of how each WorkBench works. Files that show more complicated models using multiple workbenches will be linked to at the end of this page.

Documentation links are in English, other languages may be available from the top of each page.

# PartWorkbench

-   Overview

The PartWorkbench makes geometric objects in a couple of ways: from basic named 3D objects like spheres, cones, blocks, or from manipulation of 2D sketches into a third dimension.

-   Can Make/Modify:
    -   0 \--\> Part Part Objects ( the zero, 0, indicates the part starts from nothing, it is created from scratch out of quantum fluctuation bits )
    -   Sketcher sketches \--\> Part Objects, extrusions and pockets \....
    -   PartDesign objects -\> Part Objects
    -   Part objects -\> Part Objects ( fusions, unions\..... )

-   Documentation and Links:
    -   [Part Workbench](Part_Workbench.md)
    -   **[FreeCAD Tutorial Part 1: The Part Workbench - YouTube](https://www.youtube.com/watch?v=izAB2ax3Mis)**

-   Example Files:
    -   **[workbench\_examples/Part\_primitive.txt · master · Russell Hensel / FreeCadTest · GitLab](https://gitlab.com/russhensel/freecadtest/-/blob/master/workbench_examples/Part_primitive.txt)** This is a link to the documentation \*.txt file ( which can be read directly on gitlab ), the FreeCad file has the same name, in the same directory, with the FCStd extension.
    -   **[workbench\_examples/Part\_part\_by\_extruding\_sketch.txt · master · Russell Hensel / FreeCadTest · GitLab](https://gitlab.com/russhensel/freecadtest/-/blob/master/workbench_examples/Part_part_by_extruding_sketch.txt)** This is a link to the documentation \*.txt file ( which can be read directly on gitlab ), the FreeCad file has the same name, in the same directory, with the FCStd extension.

# PartDesign

-   Overview

The PartDesignWorkbench typically makes 3D objects from 2D sketches, but can also make \"primitive features\". The basic PartDesign object is the body, an object with its own 3D space, axis, planes\... and other features that the PartDesign workbench may add to it. There is quiet a bit of functional overlap between the PartDesignWorkbench and the PartWorkbench; the PartDesignWorkbench is often preferred and is more modern.

-   Can Make/Modify:
    -   0 \--\> PartDesign Bodies: 3D objects which are also containers for other PartDesign Objects.
    -   PartDesign body \--\> PartDesign Primitives: either negative space ( subtractive ) or positive space ( additive, an object ) somewhat like Part Workbench. Must be created inside a body.
    -   0 \--\> Sketcher sketches ( but actually jumps over to the sketcher workbench, then back ) Sketches are often attached to objects inside a PartDesign Body.
    -   Sketch sketches \--\> PartDesign pads and pockets
    -   Part Objects \--\> PartDesign base feature \.... drag into body to create an object PartDesign can manage

-   Documents and Links:
    -   [PartDesign Workbench](PartDesign_Workbench.md)
    -   **[FreeCAD Tutorial Part 1: The Part Workbench - YouTube](https://www.youtube.com/watch?v=izAB2ax3Mis)**

-   Example Files:
    -   **[workbench\_examples/PartDesign\_pad.txt · master · Russell Hensel / FreeCadTest · GitLab](https://gitlab.com/russhensel/freecadtest/-/blob/master/workbench_examples/PartDesign_pad.txt)** This is a link to the documentation \*.txt file ( which can be read directly on gitlab ), the FreeCad file has the same name, in the same directory, with the FCStd extension.

# Sketcher

-   Overview

The Sketcher primarily makes 2D objects in a plane that are typically used by other workbenches to create 3D objects. The plane used is chosen when the sketch is created. Sketches can make \"positive space\" by being \"padded\" or \"extruded\", or \"negative space\" by being \"pocketed\". More complicated operations like \"sweeps\", and \"lofts\" are also supported. These other operations take place in other workbenches including PartWorkBench and PartDesignWorkbench.

-   Can Make/Modify:
    -   0 -\> Sketches \-\-\-- Make a sketch from nothing.

-   Documents and Links:
    -   [Sketcher Workbench](Sketcher_Workbench.md)

-   Example Files:
    -   **[workbench\_examples/Sketcher\_sketch.txt · master · Russell Hensel / FreeCadTest · GitLab](https://gitlab.com/russhensel/freecadtest/-/blob/master/workbench_examples/Sketcher_sketch.txt)** This is the link to the documentation \*.txt file ( which can be read directly on gitlab ), the FreeCad file has the same name, in the same directory, with the FCStd extension.

# Spreadsheet

-   Overview:

The Spreadsheet workbench makes spreadsheets, think OpenOffice, Excel\.... Compared to dedicated spreadsheet programs it is quite limited. But it has a magic ability: It can link its calculated or entered values into expression throughout objects in the rest of FreeCad. All the important variables and calculations can be kept in one place, and the model dynamically ( parametrically ) modified from there.

-   Can Make/Modify:
    -   0 \--\> Spreadsheets
    -   CSV file -\> Spreadsheets data ( and interface to Excel in this way )
    -   Most parts with numerical values -\> same part with values controlled by the spreadsheet. ( this is not in this WorkBench, but in an expression elsewhere in FreeCad )

-   Documents and Links:
    -   [Spreadsheet Workbench](Spreadsheet_Workbench.md)
    -   [Manual:Using spreadsheets](Manual_Using_spreadsheets.md)

-   Example Files:
    -   **[workbench\_examples/SpreadSheet\_part.txt · master · Russell Hensel / FreeCadTest · GitLab](https://gitlab.com/russhensel/freecadtest/-/blob/master/workbench_examples/SpreadSheet_part.txt)** This is the link to the documentation \*.txt file ( which can be read directly on gitlab ), the FreeCad file has the same name, in the same directory, with the FCStd extension.

# MeshDesign Workbench 

-   Overview:

This workbench can transform other FreeCad parts into meshes ( the sort of part in a \*.stl file often used in 3D printing ). It also can perform a number of operations on meshes. Beware in documentation may be called simply the Mesh Workbench.

-   Can Make/Modify:
    -   Part part \--\> Mesh mesh object
    -   PartDesign body \--\> Mesh

-   Documents and Links:
    -   [Mesh Workbench](Mesh_Workbench.md)
    -   [Mesh](Mesh.md)

-   Example Files:
    -   **[Edit · FWE Mesh from Part · Wiki · Russell Hensel / FreeCadTest · GitLab](https://gitlab.com/russhensel/freecadtest/-/wikis/FWE-Mesh-from-Part/edit)** This is the link to the documentation \*.txt file ( which can be read directly on gitlab ), the FreeCad file has the same name, in the same directory, with the FCStd extension.

# ManyMore WorkBenches to Go 

-   This is a nontrivial effort, is there community interest to continue.

# More General Links 

-   [Workbenches](Workbenches.md)

[<img src="images/Property.png" style="width:16px"> Sandbox](Category_Sandbox.md) [<img src="images/Property.png" style="width:16px"> User Documentation](Category_User_Documentation.md) [<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Sandbox]]  ](Category_Sandbox]]  .md) > FreeCad Workbenches
