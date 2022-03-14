# Missing features
## Introduction

The goal of this article is to list the most important currently missing features in FreeCAD and provide workarounds for them. It can be helpful for new users who can\'t find a particular functionality in FreeCAD.

## Missing features in the Sketcher 

++++
| No. | Missing feature                                                                                                                                                                  | Workarounds                                                                                                                                                                                                                                                                                                              |
+=====+==================================================================================================================================================================================+==========================================================================================================================================================================================================================================================================================================================+
| 1   | Auto snapping to objects (midpoints, center points, quadrants, extensions, intersections)                                                                                        | -   manually applying [constraints](Sketcher_Workbench#Sketcher_constraints.md) and using [construction lines](Sketcher_ToggleConstruction.md)                                                                                                                                                           |
|     |                                                                                                                                                                                  | -   drawing in [Draft Workbench](Draft_Workbench.md) where snapping to objects is available, then converting with [Draft2Sketch](Draft_Draft2Sketch.md) tool                                                                                                                                             |
++++
| 2   | Chamfer tool                                                                                                                                                                     | -   making chamfers on part level (after the sketch is turned into a volume) - [PartDesign Chamfer](PartDesign_Chamfer.md) tool                                                                                                                                                                                  |
|     |                                                                                                                                                                                  | -   adding [fillet](Sketcher_CreateFillet.md), turning it to [construction geometry](Sketcher_ToggleConstruction.md) and then connecting the points with [line](Sketcher_CreateLine.md) to create a chamfer                                                                                      |
++++
| 3   | Circular pattern                                                                                                                                                                 | -   creating circular patterns on part level (after the sketch is turned into a volume) - [PartDesign PolarPattern](PartDesign_PolarPattern.md) tool                                                                                                                                                             |
++++
| 4   | Offset tool                                                                                                                                                                      | -   SketcherOffset macro                                                                                                                                                                                                                                                                                                 |
|     |                                                                                                                                                                                  | -   [Part Offset2D](Part_Offset2D.md) tool ([SubShapeBinder](PartDesign_SubShapeBinder.md) necessary to [pad](PartDesign_Pad.md))                                                                                                                                                                |
|     |                                                                                                                                                                                  | -   [Draft Offset](Draft_Offset.md) tool ([SubShapeBinder](PartDesign_SubShapeBinder.md) necessary to [pad](PartDesign_Pad.md))                                                                                                                                                                  |
++++
| 5   | Rotate tool                                                                                                                                                                      | -   no known workaround                                                                                                                                                                                                                                                                                                  |
++++
| 6   | Scale tool                                                                                                                                                                       | -   [Draft Scale](Draft_Scale.md), then [Draft2Sketch](Draft_Draft2Sketch.md)                                                                                                                                                                                                                            |
++++
| 7   | Adaptive dimension constraint                                                                                                                                                    | -   using a range of [dimensional constraints](Sketcher_Workbench#Dimensional_constraints.md) -- 3 for lines, 1 for angles and 3 for arcs/circles                                                                                                                                                                |
++++
| 8   | Inputting coordinates and dimensions on go (when drawing an object)                                                                                                              | -   dimensioning afterwards                                                                                                                                                                                                                                                                                              |
++++
| 9   | Tangency to [B-spline](B-Splines.md) edge                                                                                                                                | -   no known workaround                                                                                                                                                                                                                                                                                                  |
++++
| 10  | Checking geometric and mass properties of the sketch (area, center of mass, second moments of area and so on)                                                                    | -   no known workaround                                                                                                                                                                                                                                                                                                  |
++++
| 11  | Possibility to use the results of the [External Geometry](Sketcher_External.md) tool directly for operations on the sketch                                               | -   manually outlining the geometry created by this tool                                                                                                                                                                                                                                                                 |
++++
| 12  | Projecting multiple edges at once with the [External Geometry](Sketcher_External.md) tool when a face is selected                                                        | -   projecting edges individually                                                                                                                                                                                                                                                                                        |
++++
| 13  | 3D sketches                                                                                                                                                                      | -   [Draft Workbench](Draft_Workbench.md) but 3D drafts can't be converted to sketches (however, they can be used for spatial frame analyses done [internally](FEM_Workbench.md) or externally and for [Additive Pipe](PartDesign_AdditivePipe.md) or [Part Sweep](Part_Sweep.md) paths) |
++++
| 14  | Projection of cut edges when making a sketch on a plane cutting through the model                                                                                                | -   no known workaround                                                                                                                                                                                                                                                                                                  |
++++
| 15  | [View section](Sketcher_ViewSection.md) tool showing filled cuts (not hollow ones) - directly related to the [Clipping plane](Std_ToggleClipPlane.md) tool issue | -   no known workaround                                                                                                                                                                                                                                                                                                  |
++++

## Missing features in the Part and Part Design workbenches 

++++
| No. | Missing feature                                                                                                                                                                                  | Workarounds                                                                                                                                                  |
+=====+==================================================================================================================================================================================================+==============================================================================================================================================================+
| 1   | Checking geometric and mass properties of the model                                                                                                                                              | -   [FCInfo macro](Macro_FCInfo.md)                                                                                                                  |
|     |                                                                                                                                                                                                  | -   [Part CheckGeometry](Part_CheckGeometry.md) tool -- area, volume, mass, length, COM, moments of inertia, radius of gyration                      |
++++
| 2   | [Clipping plane](Std_ToggleClipPlane.md) that doesn\'t make the model look like it\'s hollow                                                                                             | -   changing lighting in part's view settings to one side (very rough equivalent, problem with multicolored parts)                                           |
|     |                                                                                                                                                                                                  | -   [Persistent section cut](Part_SectionCut.md) tool - deselect all planes before pressing Close, doesn't work for intersecting parts in assemblies |
++++
| 3   | Creation of an axis on the intersection of 2 planes and a plane midway between two faces/points, possibly more variants for [datum](Datum.md) creation                                   | -   more manual [datum](Datum.md) creation                                                                                                           |
++++
| 4   | Automated midsurface extraction (for thin-walled parts)                                                                                                                                          | -   [Draft Facebinder](Draft_Facebinder.md) and then [Draft Scale](Draft_Scale.md) to make it actual midsurface                              |
++++
| 5   | Projecting (mapping/wrapping) sketches on non-planar (e.g. cylindrical) faces                                                                                                                    | -   [Sketch on Surface](Curves_SketchOnSurface.md) tool in add-on [Curves Workbench](Curves_Workbench.md)                                    |
++++
| 6   | Support for multiple solids within a [body](PartDesign_Body.md)                                                                                                                          | -   creating a separate [body](PartDesign_Body.md) for each solid                                                                                    |
++++
| 7   | Selecting which part of the sketch to [pad](PartDesign_Pad.md)                                                                                                                           | -   no known workarounds                                                                                                                                     |
++++
| 8   | [Fillets](PartDesign_Fillet.md) and [chamfers](PartDesign_Chamfer.md) that can consume adjacent faces/edges                                                                      | -   making [fillets](PartDesign_Fillet.md) with a slightly smaller radius (e.g. 6.4999 instead of 6.5 mm)                                            |
++++
| 9   | Variable radius for the [PartDesign Fillet](PartDesign_Fillet.md) tool                                                                                                                   | -   using [Part Fillet](Part_Fillet.md) tool which supports variable radius                                                                          |
++++
| 10  | Parametric curves                                                                                                                                                                                | -   [Macro 3D Parametric Curve](Macro_3D_Parametric_Curve.md)                                                                                        |
++++
| 11  | Cosmetic threads                                                                                                                                                                                 | -   modeling true threads, for holes those can be generated automatically using [Hole](PartDesign_Hole.md) tool                                      |
++++
| 12  | Partitions (splitting surfaces and volumes with sketches and datum planes while keeping the number of parts unchanged)                                                                           | -   [Boolean Fragments](Part_BooleanFragments.md) tool -- only splitting surfaces with sketches                                                      |
++++
| 13  | Guide rails for [Additive Pipe](PartDesign_AdditivePipe.md) and [Additive Loft](PartDesign_AdditiveLoft.md) or their equivalents in the [Part Workbench](Part_Module.md) | -   [CurvedShapes](CurvedShapes_Workbench.md) add-on workbench - [CurvedArray](CurvedShapes_CurvedArray.md)                                  |
++++
| 14  | Twist for [Additive Pipe](PartDesign_AdditivePipe.md) or [Part Sweep](Part_Sweep.md)                                                                                             | -   [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md) (pitch=height\*360/twist angle)                                                          |
|     |                                                                                                                                                                                                  | -   [CurvedShapes](CurvedShapes_Workbench.md) add-on workbench - [CurvedArray](CurvedShapes_CurvedArray.md)                                  |
++++
| 15  | Bending existing parts                                                                                                                                                                           | -   no known workaround                                                                                                                                      |
++++
| 16  | Pattern along a curve                                                                                                                                                                            | -   [Draft PathArray](Draft_PathArray.md) tool                                                                                                       |
++++
| 17  | Cut scope - cut tools affecting only selected part of the model                                                                                                                                  | -   different order of operations and using [boolean cut](Part_Cut.md) on [padded](PartDesign_Pad.md) bodies                                 |
++++
| 18  | Merging adjacent faces                                                                                                                                                                           | -   no known workaround                                                                                                                                      |
++++
| 19  | [Hole](PartDesign_Hole.md) tool using points from sketches                                                                                                                               | -   drawing circles for the [Hole](PartDesign_Hole.md) tool                                                                                          |
++++
| 20  | [Datum points](PartDesign_Point.md) from coordinates                                                                                                                                     | -   basing [datum points](PartDesign_Point.md) on existing geometry                                                                                  |
++++

## Missing features in the TechDraw workbench 

++++
| No. | Missing feature                                                        | Workarounds                                                                                                                                       |
+=====+========================================================================+===================================================================================================================================================+
| 1   | Advanced section views (half, broken out, offset and aligned sections) | -   using the [Slice apart](Part_SliceApart.md) tool to physically cut the model and then creating its view                               |
++++
| 2   | Surface quality annotations                                            | -   importing symbols created in external software (e.g. Inkscape) and saved to svg format - [Insert SVG Symbol](TechDraw_Symbol.md) tool |
++++
| 3   | Auto diameter dimension on side views                                  | -   manual addition of the diameter symbol                                                                                                        |
++++
| 4   | Sketching in drawings                                                  | -   cosmetic line tools in [Annotations](TechDraw_Workbench#Annotations.md), limited                                                      |
++++
| 5   | Shaded views in drawings                                               | -   no known workaround                                                                                                                           |
++++

## Missing features in the FEM workbench 

++++
| No. | Missing feature                                                                                                                               | Workarounds                                                                              |
+=====+===============================================================================================================================================+==========================================================================================+
| 1   | Beams with arbitrary [cross-section](FEM_ElementGeometry1D.md)                                                                        | -   no known workaround                                                                  |
++++
| 2   | [Pressure load](FEM_ConstraintPressure.md) on shells, distributed load on beams                                                       | -   [force load](FEM_ConstraintForce.md)                                         |
++++
| 3   | Support for multiple meshes and thus possibility to define [contact](FEM_ConstraintContact.md) between touching (not separated) faces | -   no known workaround                                                                  |
++++
| 4   | Applying torque to any surface                                                                                                                | -   [Transform constraint](FEM_ConstraintTransform.md) (only for circular faces) |
++++
| 5   | Defining rigid bodies and virtual elements                                                                                                    | -   no known workaround                                                                  |
++++
| 6   | Advanced material models (hyperelasticity, creep and so on)                                                                                   | -   no known workaround                                                                  |
++++
| 7   | Composite shells                                                                                                                              | -   no known workaround                                                                  |
++++
| 8   | Simple creation of node and element sets                                                                                                      | -   no known workaround                                                                  |
++++
| 9   | CalculiX keyword editor                                                                                                                       | -   no known workaround                                                                  |
++++

## General missing features 

++++
| No. | Missing feature                                                                                                                                                                                             | Workarounds                                                          |
+=====+=============================================================================================================================================================================================================+======================================================================+
| 1   | Official [assembly](Assembly.md) module                                                                                                                                                             | -   three different addon [assembly](Assembly.md) modules    |
++++
| 2   | Improved appearance/rendering of 3D models                                                                                                                                                                  | -   no known workaround                                              |
++++
| 3   | [Status bar](Status_bar.md) instructions ("Now pick this ...") for many tools that would benefit from having them (e.g. [Sketcher constraints](Sketcher_Workbench#Sketcher_constraints.md)) | -   no known workaround                                              |
++++
| 4   | Consistent selection order - some tools require the user to pick the geometric entity first while others allow selection after enabling the tool                                                            | -   no known workaround                                              |
++++
| 5   | More GUI customization options - pie menus, different icon styles and themes and so on                                                                                                                      | -   various customization packages created by the community          |
++++
| 6   | Selection filter (picking only faces, edges, points and so on)                                                                                                                                              | -   manual selection of proper geometric entities                    |
++++
| 7   | [Assembly](Assembly.md) module with an option to constrain parts to the origin and to [datums](Datum.md)                                                                                    | -   no known workaround                                              |
++++
| 8   | [Transform](Std_TransformManip.md) tool with an option to move and rotate with respect to edges and global coordinates                                                                              | -   Add-on [Manipulator Workbench](Manipulator_Workbench.md) |
++++
| 9   | More texturing options                                                                                                                                                                                      | -   no known workaround                                              |
++++



---
![](images/Right_arrow.png) [documentation index](../README.md) > Missing features
