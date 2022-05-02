# Workarounds
## Introduction

The goal of this article is to list the most important currently missing features in FreeCAD and provide workarounds for them. It can be helpful for new users who can\'t find a particular functionality in FreeCAD.

## Missing features in the Sketcher 

++++
| No. | Missing feature                                                                                                                    | Workarounds                                                                                                                                                                                                                                                                                                              |
+=====+====================================================================================================================================+==========================================================================================================================================================================================================================================================================================================================+
| 1   | Auto snapping to objects (midpoints, center points, quadrants, extensions, intersections)                                          | -   manually applying [constraints](Sketcher_Workbench#Sketcher_constraints.md) and using [construction lines](Sketcher_ToggleConstruction.md)                                                                                                                                                           |
|     |                                                                                                                                    | -   drawing in [Draft Workbench](Draft_Workbench.md) where snapping to objects is available, then converting with [Draft2Sketch](Draft_Draft2Sketch.md) tool                                                                                                                                             |
++++
| 2   | Chamfer tool                                                                                                                       | -   making chamfers on part level (after the sketch is turned into a volume) - [PartDesign Chamfer](PartDesign_Chamfer.md) tool                                                                                                                                                                                  |
|     |                                                                                                                                    | -   adding [fillet](Sketcher_CreateFillet.md), turning it to [construction geometry](Sketcher_ToggleConstruction.md) and then connecting the points with [line](Sketcher_CreateLine.md) to create a chamfer                                                                                      |
++++
| 3   | Circular pattern                                                                                                                   | -   creating circular patterns on part level (after the sketch is turned into a volume)                                                                                                                                                                                                                                  |
|     |                                                                                                                                    |     -   for a [PartDesign Workbench](PartDesign_Workbench.md) Feature use [PartDesign PolarPattern](PartDesign_PolarPattern.md)                                                                                                                                                                          |
|     |                                                                                                                                    |     -   for a [Part Workbench](Part_Workbench.md) shape, or a complete PartDesign Body, use [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md)                                                                                                             |
++++
| 4   | Offset tool                                                                                                                        | -   SketcherOffset macro                                                                                                                                                                                                                                                                                                 |
|     |                                                                                                                                    | -   [Part Offset2D](Part_Offset2D.md) tool ([SubShapeBinder](PartDesign_SubShapeBinder.md) necessary to [pad](PartDesign_Pad.md))                                                                                                                                                                |
|     |                                                                                                                                    | -   [Draft Offset](Draft_Offset.md) tool ([SubShapeBinder](PartDesign_SubShapeBinder.md) necessary to [pad](PartDesign_Pad.md))                                                                                                                                                                  |
++++
| 5   | Rotate tool                                                                                                                        | -   to rotate the whole sketch: change its Placement property                                                                                                                                                                                                                                                            |
|     |                                                                                                                                    | -   to rotate a selection inside the active sketch:                                                                                                                                                                                                                                                                      |
|     |                                                                                                                                    |     1.  remove constraints that prevent the rotation, e.g. with [Sketcher RemoveAxesAlignment](Sketcher_RemoveAxesAlignment.md)                                                                                                                                                                                  |
|     |                                                                                                                                    |     2.  optionally add constraints between the objects to be rotated                                                                                                                                                                                                                                                     |
|     |                                                                                                                                    |     3.  apply an appropriate [Sketcher ConstrainAngle](Sketcher_ConstrainAngle.md) constraint or drag a vertex of one of the objects                                                                                                                                                                             |
++++
| 6   | Scale tool                                                                                                                         | -   [Draft Scale](Draft_Scale.md), then [Draft2Sketch](Draft_Draft2Sketch.md)                                                                                                                                                                                                                            |
++++
| 7   | Adaptive dimension constraint                                                                                                      | -   using a range of [dimensional constraints](Sketcher_Workbench#Dimensional_constraints.md) -- 3 for lines, 1 for angles and 3 for arcs/circles                                                                                                                                                                |
++++
| 8   | Inputting coordinates and dimensions on go (when drawing an object)                                                                | -   dimensioning afterwards                                                                                                                                                                                                                                                                                              |
++++
| 9   | [Tangency](Sketcher_ConstrainTangent.md) to [B-spline](B-Splines.md) edge                                          | -   [tangency](Sketcher_ConstrainTangent.md) applied to endpoints instead of edges                                                                                                                                                                                                                               |
++++
| 10  | Checking geometric and mass properties of the sketch (area, center of mass, second moments of area and so on)                      | -   create a face from the sketch with [Part MakeFace](Part_MakeFace.md), then analyze that face with [Part CheckGeometry](Part_CheckGeometry.md)                                                                                                                                                        |
++++
| 11  | Possibility to use the results of the [External Geometry](Sketcher_External.md) tool directly for operations on the sketch | -   manually outlining the geometry created by this tool                                                                                                                                                                                                                                                                 |
++++
| 12  | Projecting multiple edges at once with the [External Geometry](Sketcher_External.md) tool when a face is selected          | -   projecting edges individually                                                                                                                                                                                                                                                                                        |
++++
| 13  | 3D sketches                                                                                                                        | -   [Draft Workbench](Draft_Workbench.md) but 3D drafts can't be converted to sketches (however, they can be used for spatial frame analyses done [internally](FEM_Workbench.md) or externally and for [Additive Pipe](PartDesign_AdditivePipe.md) or [Part Sweep](Part_Sweep.md) paths) |
++++
| 14  | Projection of cut edges when making a sketch on a plane cutting through an object                                                  | -   create a [Link](Std_LinkMake.md) from the object, and [slice](Part_SliceApart.md) that object to get actual cut edges.                                                                                                                                                                               |
++++
| 15  | [View section](Sketcher_ViewSection.md) tool showing filled cuts                                                           | -   if the sketch is plane-parallel to one of the main planes of the global coordinate system: use [Part SectionCut](Part_SectionCut.md)                                                                                                                                                                         |
++++

## Missing features in the Part and Part Design workbenches 

++++
| No. | Missing feature                                                                                                                                                                                     | Workarounds                                                                                                                                                                                      |
+=====+=====================================================================================================================================================================================================+==================================================================================================================================================================================================+
| 1   | Checking geometric and mass properties of the model                                                                                                                                                 | -   [FCInfo macro](Macro_FCInfo.md)                                                                                                                                                      |
|     |                                                                                                                                                                                                     | -   [Part CheckGeometry](Part_CheckGeometry.md) tool -- area, volume, mass, length, COM, moments of inertia, radius of gyration                                                          |
++++
| 2   | Displaying center of mass of the model (part or assembly)                                                                                                                                           | -   [Macro CenterOfMass](Macro_CenterOfMass.md)                                                                                                                                          |
++++
| 3   | [Clipping plane](Std_ToggleClipPlane.md) that doesn\'t make the model look like it\'s hollow                                                                                                | -   changing lighting in part's view settings to one side (very rough equivalent, problem with multicolored parts)                                                                               |
|     |                                                                                                                                                                                                     | -   [Persistent section cut](Part_SectionCut.md) tool - deselect all planes before pressing Close, doesn't work for intersecting parts in assemblies                                     |
++++
| 4   | Creation of an axis on the intersection of 2 planes and a plane midway between two faces/points, possibly more variants for [datum](Datum.md) creation                                      | -   more manual [datum](Datum.md) creation                                                                                                                                               |
++++
| 5   | Automated midsurface extraction (for thin-walled parts)                                                                                                                                             | -   [Draft Facebinder](Draft_Facebinder.md) and then [Draft Scale](Draft_Scale.md) or [Part Offset](Part_Offset.md) to make it actual midsurface                         |
++++
| 6   | Projecting (mapping/wrapping) sketches on non-planar (e.g. cylindrical) faces                                                                                                                       | -   [Sketch on Surface](Curves_SketchOnSurface.md) tool in add-on [Curves Workbench](Curves_Workbench.md)                                                                        |
|     |                                                                                                                                                                                                     | -   [Part ProjectionOnSurface](Part_ProjectionOnSurface.md) tool                                                                                                                         |
++++
| 7   | Support for multiple solids within a [body](PartDesign_Body.md)                                                                                                                             | -   creating a separate [body](PartDesign_Body.md) for each solid                                                                                                                        |
++++
| 8   | Selecting which part of the sketch to [pad](PartDesign_Pad.md)                                                                                                                              | -   select the edges from the sketch and create a [SubLink](Std_LinkMakeRelative.md) or a [SubShapeBinder](PartDesign_SubShapeBinder.md) and pad that new object                 |
++++
| 9   | [Fillets](PartDesign_Fillet.md) and [chamfers](PartDesign_Chamfer.md) that can consume adjacent faces/edges                                                                         | -   making [fillets](PartDesign_Fillet.md) with a slightly smaller radius (e.g. 6.4999 instead of 6.5 mm)                                                                                |
++++
| 10  | Variable radius for the [PartDesign Fillet](PartDesign_Fillet.md) tool                                                                                                                      | -   using [Part Fillet](Part_Fillet.md) tool which supports variable radius                                                                                                              |
++++
| 11  | Parametric curves                                                                                                                                                                                   | -   [Macro 3D Parametric Curve](Macro_3D_Parametric_Curve.md)                                                                                                                            |
++++
| 12  | Cosmetic threads                                                                                                                                                                                    | -   modeling true threads, for holes those can be generated automatically using [Hole](PartDesign_Hole.md) tool                                                                          |
++++
| 13  | Partitions (splitting surfaces and volumes with sketches and datum planes while keeping the number of parts unchanged)                                                                              | -   [Boolean Fragments](Part_BooleanFragments.md) tool -- only splitting surfaces with sketches                                                                                          |
++++
| 14  | Guide rails for [Additive Pipe](PartDesign_AdditivePipe.md) and [Additive Loft](PartDesign_AdditiveLoft.md) or their equivalents in the [Part Workbench](Part_Workbench.md) | -   add-on [CurvedShapes Workbench](CurvedShapes_Workbench.md) - [CurvedArray](CurvedShapes_CurvedArray.md)                                                                      |
++++
| 15  | Twist for [Additive Pipe](PartDesign_AdditivePipe.md) or [Part Sweep](Part_Sweep.md)                                                                                                | -   [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md) (pitch=height\*360/twist angle)                                                                                              |
|     |                                                                                                                                                                                                     | -   add-on [CurvedShapes Workbench](CurvedShapes_Workbench.md) - [CurvedArray](CurvedShapes_CurvedArray.md)                                                                      |
|     |                                                                                                                                                                                                     | -   Multisection mode in [Additive Pipe](PartDesign_AdditivePipe.md)                                                                                                                     |
++++
| 16  | Bending existing parts                                                                                                                                                                              | -   for sheet metal objects: add-on [SheetMetal Workbench](SheetMetal_Workbench.md) - [SheetMetal AddFoldWall](SheetMetal_AddFoldWall.md)                                        |
++++
| 17  | Pattern along a curve                                                                                                                                                                               | -   [Draft PathArray](Draft_PathArray.md) tool                                                                                                                                           |
++++
| 18  | Cut scope - cut tools affecting only selected part of the model                                                                                                                                     | -   different order of operations and using [boolean cut](Part_Cut.md) on [padded](PartDesign_Pad.md) bodies                                                                     |
++++
| 19  | Merging adjacent faces                                                                                                                                                                              | -   for faces of a PartDesign Body: change the Refine property of the last Feature to {{True}}.                                                                                    |
|     |                                                                                                                                                                                                     | -   for co-planar faces: use [Draft Upgrade](Draft_Upgrade.md) twice to get a [Draft Wire](Draft_Wire.md), [Draft Downgrade](Draft_Downgrade.md) the wire to get a face. |
++++
| 20  | [Hole](PartDesign_Hole.md) tool using points from sketches                                                                                                                                  | -   drawing circles for the [Hole](PartDesign_Hole.md) tool                                                                                                                              |
++++
| 21  | [Datum points](PartDesign_Point.md) from coordinates                                                                                                                                        | -   basing [datum points](PartDesign_Point.md) on existing geometry                                                                                                                      |
++++

## Missing features in the TechDraw workbench 

++++
| No. | Missing feature                                                        | Workarounds                                                                                                                                                                                                                                                                   |
+=====+========================================================================+===============================================================================================================================================================================================================================================================================+
| 1   | Advanced section views (half, broken out, offset and aligned sections) | -   using the [Slice apart](Part_SliceApart.md) tool to physically cut the model and then creating its view                                                                                                                                                           |
++++
| 2   | Surface quality annotations                                            | -   importing symbols created in external software (e.g. Inkscape) and saved to svg format - [Insert SVG Symbol](TechDraw_Symbol.md) tool                                                                                                                             |
++++
| 3   | Auto diameter dimension on side views                                  | -   manual addition of the diameter symbol                                                                                                                                                                                                                                    |
++++
| 4   | Sketching in drawings                                                  | -   cosmetic line tools in [Annotations](TechDraw_Workbench#Annotations.md), limited                                                                                                                                                                                  |
|     |                                                                        | -   creating [regular views](TechDraw_View.md) and [Draft views](TechDraw_DraftView.md) of sketches and [Draft](Draft_Workbench.md) objects                                                                                                           |
++++
| 5   | Shaded views in drawings                                               | -   no known workaround                                                                                                                                                                                                                                                       |
++++
| 6   | Ordinate dimensions                                                    | -   no known workaround                                                                                                                                                                                                                                                       |
++++
| 7   | Broken (interrupted) views                                             | -   creating broken views manually:                                                                                                                                                                                                                                           |
|     |                                                                        |     1.  sketch two wavy or zig-zag lines close to the ends of a long part and [extrude](Part_Extrude.md) them towards the model creating surfaces for the cut                                                                                                         |
|     |                                                                        |     2.  use the [Part Slice](Part_Slice.md) tool to cut the model with these surfaces                                                                                                                                                                                 |
|     |                                                                        |     3.  hide the middle piece and [move](Std_TransformManip.md) one of the remaining pieces towards the other                                                                                                                                                         |
|     |                                                                        |     4.  create a [view](TechDraw_View.md) of these objects                                                                                                                                                                                                            |
|     |                                                                        |     5.  if needed, make the lines of the cut dashed (using the [TechDraw DecorateLine](TechDraw_DecorateLine.md) tool)                                                                                                                                                |
|     |                                                                        |     6.  if lines of the cut have to be extended, create a [view](TechDraw_View.md) of the sketch used in the first step and align it with the cut                                                                                                                     |
|     |                                                                        |     7.  to obtain a proper value of the length of the cut part, you can either change the dimension value manually (after enabling the *Arbitrary Text* option) or [link](TechDraw_LinkDimension.md) it to the distance between the end vertices of the original part |
++++

## Missing features in the FEM workbench 

++++
| No. | Missing feature                                                                                                                               | Workarounds                                                                                 |
+=====+===============================================================================================================================================+=============================================================================================+
| 1   | Beams with arbitrary [cross-section](FEM_ElementGeometry1D.md)                                                                        | -   no known workaround                                                                     |
++++
| 2   | [Pressure load](FEM_ConstraintPressure.md) on shells, distributed load on beams                                                       | -   [force load](FEM_ConstraintForce.md)                                            |
++++
| 3   | Support for multiple meshes and thus possibility to define [contact](FEM_ConstraintContact.md) between touching (not separated) faces | -   no known workaround                                                                     |
++++
| 4   | Applying torque to any surface                                                                                                                | -   [Transform constraint](FEM_ConstraintTransform.md) (only for cylindrical faces) |
++++
| 5   | Defining rigid bodies and virtual elements                                                                                                    | -   no known workaround                                                                     |
++++
| 6   | Advanced material models (hyperelasticity, creep and so on)                                                                                   | -   no known workaround                                                                     |
++++
| 7   | Composite shells                                                                                                                              | -   no known workaround                                                                     |
++++
| 8   | Simple creation of node and element sets                                                                                                      | -   no known workaround                                                                     |
++++
| 9   | CalculiX keyword editor                                                                                                                       | -   no known workaround                                                                     |
++++

## General missing features 

++++
| No. | Missing feature                                                                                                                                                                                             | Workarounds                                                                                                                                        |
+=====+=============================================================================================================================================================================================================+====================================================================================================================================================+
| 1   | Official [assembly](Assembly.md) workbench                                                                                                                                                          | -   three different add-on [assembly](Assembly.md) workbenches                                                                             |
++++
| 2   | Improved appearance/rendering of 3D models                                                                                                                                                                  | -   no known workaround                                                                                                                            |
++++
| 3   | [Status bar](Status_bar.md) instructions ("Now pick this ...") for many tools that would benefit from having them (e.g. [Sketcher constraints](Sketcher_Workbench#Sketcher_constraints.md)) | -   no known workaround                                                                                                                            |
++++
| 4   | Consistent selection order - some tools require the user to pick the geometric entity first while others allow selection after enabling the tool                                                            | -   no known workaround                                                                                                                            |
++++
| 5   | More GUI customization options - pie menus, different icon styles and themes and so on                                                                                                                      | -   various customization packages created by the community                                                                                        |
++++
| 6   | Selection filter (picking only faces, edges, points and so on)                                                                                                                                              | -   manual selection of proper geometric entities                                                                                                  |
|     |                                                                                                                                                                                                             | -   [Wireframe mode](Std_DrawStyle#Wireframe.md) to facilitate edge selection                                                              |
++++
| 7   | [Assembly](Assembly.md) workbench with an option to constrain parts to the origin and to [datums](Datum.md)                                                                                 | -   no known workaround                                                                                                                            |
++++
| 8   | [Transform](Std_TransformManip.md) tool with an option to move and rotate with respect to edges and global coordinates                                                                              | -   add-on [Manipulator Workbench](Manipulator_Workbench.md)                                                                               |
++++
| 9   | More texturing options                                                                                                                                                                                      | -   no known workaround                                                                                                                            |
++++
| 10  | View normal to a face                                                                                                                                                                                       | -   [Macro Align View to Face](Macro_Align_View_to_Face.md)                                                                                |
++++
| 11  | Highlighting only individual PartDesign feature of the model when the corresponding operation in the [Tree view](Tree_view.md) is selected                                                          | -   no known workaround                                                                                                                            |
++++
| 12  | Selecting individual PartDesign feature in the [Tree view](Tree_view.md) upon clicking on the corresponding face                                                                                    | -   no known workaround                                                                                                                            |
++++
| 13  | Freeform modeling                                                                                                                                                                                           | -   no known workaround                                                                                                                            |
++++
| 14  | Assembly component generators and calculators for: bolted and riveted connections, shafts, splines, keys, cams, gears (spur, bevel, worm), bearings, springs, belts and chains, pins, o-rings               | -   [Fasteners Workbench](Fasteners_Workbench.md) and [FCGear Workbench](FCGear_Workbench.md) but no design calculations available |
++++



---
![](images/Right_arrow.png) [documentation index](../README.md) > Workarounds
