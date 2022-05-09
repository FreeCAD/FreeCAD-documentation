# <img alt="OpenSCAD workbench icon" src=images/Workbench_OpenSCAD.svg  style="width   *64px;"> OpenSCAD Workbench/zh-cn

## Introduction

The <img alt="" src=images/Workbench_OpenSCAD.svg  style="width   *24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md) is intended to offer interoperability with the open source software [OpenSCAD](http   *//www.openscad.org/). This program is not distributed as part of FreeCAD, but should be installed to make full use of this workbench. OpenSCAD should not be confused with [OpenCASCADE](OpenCASCADE.md), which is the geometrical kernel that FreeCAD uses to build geometry on screen. The OpenCASCADE libraries are always needed to use FreeCAD, while the OpenSCAD executable is entirely optional.

It contains a [CSG](OpenSCAD_CSG.md) importer to open the CSG files from OpenSCAD, and an exporter to output a CSG based tree. Geometry which is not based on CSG operations will be exported as a mesh.

This workbench contains functions to modify the CSG feature tree and repair models. It also contains general purpose tools that do not require installation of OpenSCAD; they can be used in conjunction with other workbenches. For example, the [Mesh Workbench](Mesh_Workbench.md) internally uses the OpenSCAD functions to perform operations with [meshes](mesh.md), as they are quite robust.


{{TOCright}}

![](images/OpenSCADexamaple1.png )

## Dependencies

In FreeCAD 0.19, the Ply (Python-Lex-Yacc) module, which is used to import CSG files, was removed from the FreeCAD source code, as it is a third party library not developed by FreeCAD. As a result, you now need to install Ply before using the OpenSCAD Workbench. When using a pre-packaged, stable version of FreeCAD this dependency should be installed automatically in all platforms; in other cases, for example, when [compiling](Compiling.md) from source, you may have to install it from an online repository.

In openSUSE this is done by   *


```python
sudo zypper install python3-ply
```

In Debian/Ubuntu based systems this is done like the following   *


```python
sudo apt install python3-ply
```

The general installation in all platforms can be done from the Python package index.


```python
pip3 install --user ply
```

## OpenSCAD language and file format 

The OpenSCAD language allows the use of variables and loops. It allows you to specify sub-modules to reuse geometry and code. This high degree of flexibility makes parsing very complex. Currently the OpenSCAD Workbench cannot handle the OpenSCAD language natively. Instead, if OpenSCAD is installed, it can be used to convert the input to the CSG format, which is a subset of the OpenSCAD language, and can be used as the input to OpenSCAD for further processing. During conversion all parametric behavior is lost, meaning that all variable names are discarded, loops expanded, and mathematical expressions evaluated.

## Tools

-   <img alt="" src=images/OpenSCAD_ColorCodeShape.png  style="width   *32px;"> [Color Code Shape](OpenSCAD_ColorCodeShape.md)   * Change the color of selected or all shapes based on their validity.
-   <img alt="" src=images/OpenSCAD_ReplaceObject.png  style="width   *32px;"> [Replace Object](OpenSCAD_ReplaceObject.md)   * Replace an object in the feature tree.
-   <img alt="" src=images/OpenSCAD_RemoveSubtree.png  style="width   *32px;"> [Remove Subtree](OpenSCAD_RemoveSubtree.md)   * Removes the selected objects and all children that are not referenced from other objects.
-   <img alt="" src=images/OpenSCAD_RefineShapeFeature.png  style="width   *32px;"> [Refine Shape Feature](OpenSCAD_RefineShapeFeature.md)   * Create Refine Shape Feature.
-   <img alt="" src=images/OpenSCAD_IncreaseTolerance.png  style="width   *32px;"> [Increase Tolerance Feature](OpenSCAD_IncreaseTolerance.md)   * Increases tolerance of edges/faces/vertex of selected object(s).
-   <img alt="" src=images/OpenSCAD_Edgestofaces.png  style="width   *32px;"> [Convert Edges To Faces](OpenSCAD_Edgestofaces.md)   * Convert edges to faces. Useful to prepare imported DXF geometry for extrusion.
-   <img alt="" src=images/OpenSCAD_ExpandPlacements.png  style="width   *32px;"> [Expand Placements](OpenSCAD_ExpandPlacements.md)   * Expand all placements downwards the FeatureTree.
-   <img alt="" src=images/OpenSCAD_ExplodeGroup.png  style="width   *32px;"> [Explode Group](OpenSCAD_ExplodeGroup.md)   * Explodes fused part primitives.
-   <img alt="" src=images/OpenSCAD_AddOpenSCADElement.png  style="width   *32px;"> [Add OpenSCAD Element](OpenSCAD_AddOpenSCADElement.md)   * Add an OpenSCAD element by entering OpenSCAD code into the task panel.
-   <img alt="" src=images/OpenSCAD_MeshBoolean.png  style="width   *32px;"> [Mesh Boolean](OpenSCAD_MeshBoolean.md)   * Creates new mesh object by boolean operation from shapes.
-   <img alt="" src=images/OpenSCAD_Hull.png  style="width   *32px;"> [Hull](OpenSCAD_Hull.md)   * Apllies a hull to selected shapes.
-   <img alt="" src=images/OpenSCAD_Minkowski.png  style="width   *32px;"> [Minkowski](OpenSCAD_Minkowski.md)   * Applies a minkowski sum to selected shapes.

-   <img alt="" src=images/OpenSCAD_ColorCodeShape.svg  style="width   *32px;"> [Color Code Shape](OpenSCAD_ColorCodeShape.md)   * Change the color of selected or all shapes based on their validity.
-   <img alt="" src=images/OpenSCAD_ReplaceObject.svg  style="width   *32px;"> [Replace Object](OpenSCAD_ReplaceObject.md)   * Replace an object in the feature tree.
-   <img alt="" src=images/OpenSCAD_RemoveSubtree.svg  style="width   *32px;"> [Remove Subtree](OpenSCAD_RemoveSubtree.md)   * Removes the selected objects and all children that are not referenced from other objects.
-   <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width   *32px;"> [Refine Shape Feature](OpenSCAD_RefineShapeFeature.md)   * Create Refine Shape Feature.
-   <img alt="" src=images/OpenSCAD_MirrorMeshFeature.svg  style="width   *32px;"> [Mirror Mesh Feature](OpenSCAD_MirrorMeshFeature.md)   * Create Mirror Mesh Feature.
-   <img alt="" src=images/OpenSCAD_ScaleMeshFeature.svg  style="width   *32px;"> [Scale Mesh Feature](OpenSCAD_ScaleMeshFeature.md)   * Scale a Mesh Feature.
-   <img alt="" src=images/OpenSCAD_ResizeMeshFeature.svg  style="width   *32px;"> [Resize Mesh Feature](OpenSCAD_ResizeMeshFeature.md)   * Resize a Mesh Feature.
-   <img alt="" src=images/OpenSCAD_IncreaseToleranceFeature.svg  style="width   *32px;"> [Increase Tolerance Feature](OpenSCAD_IncreaseToleranceFeature.md)   * Increases tolerance of edges/faces/vertex of selected object(s).
-   <img alt="" src=images/OpenSCAD_Edgestofaces.svg  style="width   *32px;"> [Convert Edges To Faces](OpenSCAD_Edgestofaces.md)   * Convert edges to faces. Useful to prepare imported DXF geometry for extrusion.
-   <img alt="" src=images/OpenSCAD_ExpandPlacements.svg  style="width   *32px;"> [Expand Placements](OpenSCAD_ExpandPlacements.md)   * Expand all placements downwards the FeatureTree.
-   <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width   *32px;"> [Explode Group](OpenSCAD_ExplodeGroup.md)   * Explodes fused part primitives.
-   <img alt="" src=images/OpenSCAD_AddOpenSCADElement.svg  style="width   *32px;"> [Add OpenSCAD Element](OpenSCAD_AddOpenSCADElement.md)   * Add an OpenSCAD element by entering OpenSCAD code into the task panel.
-   <img alt="" src=images/OpenSCAD_MeshBoolean.svg  style="width   *32px;"> [Mesh Boolean](OpenSCAD_MeshBoolean.md)   * Creates new mesh object by boolean operation from shapes.
-   <img alt="" src=images/OpenSCAD_Hull.svg  style="width   *32px;"> [Hull](OpenSCAD_Hull.md)   * Applies a hull to selected shapes.
-   <img alt="" src=images/OpenSCAD_Minkowski.svg  style="width   *32px;"> [Minkowski](OpenSCAD_Minkowski.md)   * Applies a minkowski sum to selected shapes.

## Preferences

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width   *32px;"> [Preferences](OpenSCAD_Preferences.md)   * preferences available for the OpenSCAD tools.

## Limitations

OpenSCAD creates constructive solid geometry, as well as imports mesh files and extrudes 2D geometry from [DXF](DXF.md) files. FreeCAD allows you to create CSG with primitives as well. The FreeCAD geometry kernel (OCCT) works using a boundary representation. Therefore conversion from CSG to BREP should, in theory, be possible whereas conversion from BREP to CSG is, in general, not.

OpenSCAD works internally on meshes. Some operations which are useful on meshes are not meaningful on a BREP model and can not be fully supported. Among these are convex hull, minkowski sum, glide and subdiv. Currently we run the OpenSCAD binary in order to perform hull and minkwoski operations and import the result. This means that the involved geometry will be triangulated. In OpenSCAD non-uniform scaling is often used, which does not impose any problems when using meshes. In our geometry kernel geometric primitives (lines, circular sections, etc) are converted to BSpline prior to performing such deformations. Those BSplines are known to cause trouble in later boolean operations. An automatic solution is not available at the moment. Please feel free to post to the forum if you encounter such problems. Often such problems can be solved be remodeling small parts. A deformation of a cylinder can substituted by an extrusion of an ellipses.

## Importing text 

Importing OpenSCAD code with texts requires that the fonts that are used are properly installed on your system. You can verify this by opening OpenSCAD as a standalone tool and checking the list in **Help → Font List**. The list will also give you the correct font names. If a font does not appear in the list after installing, you may have to manually copy the font file to the appropriate system directory.

Importing texts is relatively slow. Behind the scenes FreeCAD uses a DXF file created by OpenSCAD. The more contours there are the slower the import.

It can be a good idea to first import a simple test case (replace {{Incode|NameOfFont}} with the correct font name)   *

    TESTFONT="NameOfFont";
    linear_extrude(0.001) {
      text("A", size=5, font=TESTFONT, script="Latn");
    };

The {{Incode|<nowiki>script="Latn"</nowiki>}} parameter can be left out here, but is required if the text string does not contain any letters, but only punctuation and/or numbers.

Please note that {{Incode|<nowiki>use <FONT>;</nowiki>}} statements in your source files are ignored when importing in FreeCAD. Under OpenSCAD the effect of a {{Incode|use}} statement is that the provided font file is temporarily added to the list of known fonts (although even there the statement does not work when a script is modified interactively).

## Hints

When importing [DXF](DXF.md) set the Draft precision to a sensible amount as this will affect the detection of connected edges.

If FreeCAD crashes when importing CSG, it is strongly recommended that you enable \"automatically check model after boolean operation\" in **Menu → Edit → Preferences → Part Design → Model setting**.

## Tutorials

-   [Import OpenSCAD code](Import_OpenSCAD_code.md)

## Links

-   The official OpenSCAD project source code repository hosted on [GitHub](https   *//github.com/openscad/openscad)
-   Open tickets tagged \"OpenSCAD\" on the [FreeCAD Github issue tracker](https   *//github.com/FreeCAD/FreeCAD/labels/WB%20OpenSCAD). There are also tickets on the now archived [mantis bugtracker](https   *//freecadweb.org/tracker/search.php?tag_string=OpenSCAD).
-   Models tagged with \"OpenSCAD\" on [Thingiverse](http   *//www.thingiverse.com/tag   *openscad)





{{OpenSCAD Tools navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [OpenSCAD](Category_OpenSCAD.md) > OpenSCAD Workbench/zh-cn
