# <img alt="Part workbench icon" src=images/Workbench_Part.svg  style="width:64px;"> Part Workbench/en




## Introduction

The <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> **Part Workbench** provides a traditional [constructive solid geometry](Constructive_solid_geometry.md) (CSG) workflow. In this workflow each object is an independent solid. The Part Workbench can create them from parametrically defined [sketches](Sketcher_Workbench.md) using tools like [Extrude](Part_Extrude.md), [Revolve](Part_Revolve.md), [Loft](Part_Loft.md), etc. In addition, basic primitive solids like [Cube](Part_Box.md), [Cylinder](Part_Cylinder.md), etc. can be created as well. These objects can be combined, through [Boolean operations](Part_Boolean.md), to create more complex solids.

The Part Workbench can also create objects that are not solids, such as faces, shells, and objects with only edges or vertices. It also provides a variety of general purpose tools for geometry manipulation, geometry validation, and making copies.

The <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) uses an alternative workflow for creating solids. For a detailed discussion of the Part Workbench versus the Part Design Workbench see [Part and Part Design](Part_and_PartDesign.md).

![](images/Part_Workbench_Example.jpg )

## Tools

### Solids toolbar 

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md): Creates a box.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube.md): Creates a tube.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Create primitives\...](Part_Primitives.md): A tool to create one of the following primitives:

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plane](Part_Plane.md): Creates a plane.

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md): Creates a box. This object can also be created with the [Box](Part_Box.md) tool.

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder. This object can also be created with the [Cylinder](Part_Cylinder.md) tool.

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone. This object can also be created with the [Cone](Part_Cone.md) tool.

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere. This object can also be created with the [Sphere](Part_Sphere.md) tool.

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid.md): Creates a ellipsoid.

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus. This object can also be created with the [Torus](Part_Torus.md) tool.

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prism](Part_Prism.md): Creates a prism.

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Wedge](Part_Wedge.md): Creates a wedge.

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix.md): Creates a helix.

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spiral](Part_Spiral.md): Creates a spiral.

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Circle](Part_Circle.md): Creates a circular arc.

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse.md): Creates an elliptical arc.

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Creates a point.

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line.md): Creates a line.

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regular polygon](Part_RegularPolygon.md): Creates a regular polygon.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shape builder\...](Part_Builder.md): Creates shapes from various primitives.

### Part tools toolbar 

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrude](Part_Extrude.md): Extrudes planar faces.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolve](Part_Revolve.md): Creates a solid by revolving an object (not a solid) around an axis.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Mirror](Part_Mirror.md): Mirrors the selected object across a mirror plane.

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scale](Part_Scale.md): Scales one or more shapes. <small>(v1.0)</small> 

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Fillet](Part_Fillet.md): Fillets (rounds) edges of an object.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chamfer](Part_Chamfer.md): Chamfers edges of an object.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Make face from wires](Part_MakeFace.md): Makes a face from a set of wires (contours).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Ruled Surface](Part_RuledSurface.md): Creates a ruled surface.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft.md): Lofts from one profile to another.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep.md): Sweeps one or more profiles along a path.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section.md): Creates a section by intersecting an object with a section plane.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cross sections\...](Part_CrossSections.md): Creates one or more cross-sections through an object.

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Offset:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Offset](Part_Offset.md): Constructs a parallel shape at a certain distance from an original.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Offset](Part_Offset2D.md): Constructs a parallel wire at certain distance from an original, or enlarges/shrinks a planar face.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Thickness](Part_Thickness.md): Hollows out a solid.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projection on surface](Part_ProjectionOnSurface.md): Projects a logo, text or any face, wire or edge onto a surface.

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Color per face](Part_ColorPerFace.md): Assigns colors to individual faces of objects.

### Boolean toolbar 

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Compound:

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Make compound](Part_Compound.md): Creates a compound from the selected objects.

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explode compound](Part_ExplodeCompound.md): Splits up compounds.

  - <img alt="" src=images/Part_CompoundFilter.svg  style="width:32px;"> [Compound Filter](Part_CompoundFilter.md): Extracts the individual pieces from compounds.

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolean](Part_Boolean.md): Performs boolean operations on two objects.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts one object from another.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse.md): Fuses two or more objects.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Intersection](Part_Common.md): Extracts the common part of two objects.

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Join:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connect objects](Part_JoinConnect.md): Connects interiors of walled objects.

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embed object](Part_JoinEmbed.md): Embeds a walled object into another walled object.

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Cutout for object](Part_JoinCutout.md): Creates a cutout in a wall of an object for another walled object.

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Split:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Boolean fragments](Part_BooleanFragments.md): Creates all pieces obtained from Boolean operations.

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Slice apart](Part_SliceApart.md): Slices and splits an object by intersecting it with other objects.

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Slice to compound](Part_Slice.md): Slices an object by intersecting it with other objects.

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [Boolean XOR](Part_XOR.md): Removes space shared by an even number of objects.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Check geometry](Part_CheckGeometry.md): Checks the geometry of selected objects for errors.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing.md): Removes features from an object.

### Other tools 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Import CAD file\...](Part_Import.md): Imports from \*.IGES, \*.STEP, or \*.BREP files.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Export CAD file\...](Part_Export.md): Exports to \*.IGES, \*.STEP, or \*.BREP files.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Box selection](Part_BoxSelection.md): Selects faces from a rectangular area.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Create shape from mesh](Part_ShapeFromMesh.md): Creates shapes from mesh objects.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Create points object from geometry](Part_PointsFromMesh.md): Creates points objects from geometric objects.

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convert to solid](Part_MakeSolid.md): Creates solids from shape objects.

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Reverse shapes](Part_ReverseShape.md): Creates parametric copies with reversed face normals from selected objects.

-   Create a copy:

  - <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Create simple copy](Part_SimpleCopy.md): Creates non-parametric copies of objects.

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Create transformed copy](Part_TransformedCopy.md): Creates non-parametric copies of objects. It is intended for objects nested in containers.

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Create shape element copy](Part_ElementCopy.md): Creates non-parametric copies of subelements: vertices, edges and faces.

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refine shape](Part_RefineShape.md): Creates parametric copies with a refined shape from selected objects. It removes unnecessary edges from planar and cylindrical faces.

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Attachment\...](Part_EditAttachment.md): Attaches an object to one or more other objects.

## Obsolete tools 

### Measure

The <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Std Measure](Std_Measure.md) tool replaces the tools listed below. <small>(v1.0)</small> 

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Measure Linear](Part_Measure_Linear.md): Creates a linear measurement. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Measure Angular](Part_Measure_Angular.md): Creates an angular measurement. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Measure Refresh](Part_Measure_Refresh.md): Updates all measurements. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Clear All](Part_Measure_Clear_All.md) and [View Measure Clear All](View_Measure_Clear_All.md): Clears all measurements. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Toggle All](Part_Measure_Toggle_All.md) and [View Measure Toggle All](View_Measure_Toggle_All.md): Shows or hides all measurements. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Toggle 3D](Part_Measure_Toggle_3D.md): Shows or hides 3D measurements. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Toggle Delta](Part_Measure_Toggle_Delta.md): Shows or hides delta measurements. Not available in <small>(v1.0)</small> .

## Preferences

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferences](PartDesign_Preferences.md): Preferences for the Part Workbench.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): Preferences for importing from and exporting to different file formats.
-   [Fine-tuning](Fine-tuning#Part_Workbench.md): Some extra parameters to fine-tune Part behavior.

## Scripting

See [Part scripting](Part_scripting.md).

## Tutorials

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md): How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md): How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md): How to use the Part Workbench



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/en
