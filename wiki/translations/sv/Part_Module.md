# <img alt="Part workbench icon" src=images/Workbench_Part.svg  style="width:64px;"> Part Module/sv




## Introduction


<div class="mw-translate-fuzzy">

FreeCAD\'s CAD kapabilitet är baserad på [OpenCasCade](http://en.wikipedia.org/wiki/Open_CASCADE) kärnan. Del modulen tillåter FreeCAD att komma åt och använda OpenCasCade objekt och funktioner. OpenCascade är en professionell CAD kärna, som erbjuder avancerad 3D geometrimanipulation och objekt. Del objekten, till skillnad från [Nätmodul](Mesh_Workbench/sv.md) objekten, är mycket komplexare, och tillåter därför mycket mer avancerade operationer, som koherenta booleska operationer, ändringshistorik och parametriskt beteende.


</div>

A more detailed discussion of Part workbench versus Part Design workbench can be found here: [Part and Part Design](Part_and_PartDesign.md).

The objects created with the Part Workbench are relatively simple; they are intended to be used with boolean operations (unions and cuts) in order to build more complex shapes. **This modeling paradigm is known as the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) workflow, and it was the traditional methodology used in early CAD systems.** On the other hand, the [PartDesign Workbench](PartDesign_Workbench.md) provides a more modern workflow to constructing shapes: it uses a parametrically defined sketch, that is extruded to form a basic solid body, which is then modified by parametric transformations ([feature editing](feature_editing.md)), until the final object is obtained.

Part objects are more complex than mesh objects created with the [Mesh Workbench](Mesh_Workbench.md), as they permit more advanced operations like coherent boolean operations, modifications history, and parametric behaviour.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*The Part Workbench is the basic layer that exposes the OCCT drawing functions to all workbenches in FreeCAD.*




<div class="mw-translate-fuzzy">

### Verktygen


</div>


<div class="mw-translate-fuzzy">

Alla Del modul verktygen finns i **Del** menyn som kommer fram när du laddar Del modulen.


</div>




<div class="mw-translate-fuzzy">

### Primitiver


</div>

Detta är verktyg för att skapa primitivobjekt.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Box.png  style="width:32px;"> [Låda](Part_Box/sv.md): Ritar en låda genom att ge dess dimensioner
-   <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> [Cylinder](Part_Cylinder/sv.md): Ritar en cylinder genom att ge dess dimensioner
-   <img alt="" src=images/Part_Sphere.png  style="width:32px;"> [Sfär](Part_Sphere/sv.md): Ritar en sfär genom att ge dess dimensioner
-   <img alt="" src=images/Part_Cone.png  style="width:32px;"> [Kon](Part_Cone/sv.md): Ritar en kon genom att ge dess dimensioner
-   <img alt="" src=images/Part_Torus.png  style="width:32px;"> [Torus](Part_Torus/sv.md): Ritar en torus (ring) genom att ge dess dimensioner
-   <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> [CreatePrimitives](Part_CreatePrimitives/sv.md): Ett verktyg för att skapa olika parametriska geometriska primitiver
-   <img alt="" src=images/Part_Shapebuilder.png  style="width:32px;"> [Shapebuilder](Part_Shapebuilder/sv.md): Ett verktyg för att skapa mer komplexa former från olika parametriska geometriska primitiver


</div>

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube.md): Creates a tube.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Create primitives\...](Part_Primitives.md): A tool to create one of the following primitives:
    -   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plane](Part_Plane.md): Creates a plane.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Box](Part_Box.md): Creates a box. This object can also be created with the <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md) tool.
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder. This object can also be created with the <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md) tool.
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone. This object can also be created with the <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md) tool.
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere. This object can also be created with the <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md) tool.
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid.md): Creates a ellipsoid.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus. This object can also be created with the <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md) tool.
    -   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prism](Part_Prism.md): Creates a prism.
    -   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Wedge](Part_Wedge.md): Creates a wedge.
    -   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix.md): Creates a helix.
    -   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spiral](Part_Spiral.md): Creates a spiral.
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Circle](Part_Circle.md): Creates a circular arc.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse.md): Creates an elliptical arc.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Creates a point.
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line.md): Creates a line.
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regular polygon](Part_RegularPolygon.md): Creates a regular polygon.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shape builder\...](Part_Builder.md): Creates shapes from various primitives.




<div class="mw-translate-fuzzy">

### Förändra objekt 


</div>


<div class="mw-translate-fuzzy">

Detta är verktyg för att förändra existerande objekt. De kommer att låta dig välja vilka objekt som du vill förändra.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Extrude.png  style="width:32px;"> [Extrudera](Part_Extrude/sv.md): Extruderar plana ytor på ett objekt
-   <img alt="" src=images/Part_Revolve.png  style="width:32px;"> [Rotera](Part_Revolve/sv.md): Skapar ett objekt genom att rotera ett annat objekt runt en axel
-   <img alt="" src=images/Part_Mirror.png  style="width:32px;"> [Spegling](Part_Mirror/sv.md): Speglar de valda objekten runt en given axel
-   <img alt="" src=images/Part_Fillet.png  style="width:32px;"> [Fasning](Part_Fillet/sv.md): Fasar (rundar) kanterna på ett objekt
-   <img alt="" src=images/Part_Chamfer.png  style="width:32px;"> [Fasning](Part_Chamfer/sv.md): Fasar (klipper) kanter på ett objekt
-   <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> [Ruled Surface](Part_RuledSurface/sv.md):
-   <img alt="" src=images/Part_Loft.png  style="width:32px;"> [Loft](Part_Loft/sv.md): Lofts från en profil till en annan
-   <img alt="" src=images/Part_Sweep.png  style="width:32px;"> [Sweep](Part_Sweep/sv.md): Sopa en eller flera profiler längs en bana


</div>

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolve](Part_Revolve.md): Creates a solid by revolving an object (not a solid) around an axis.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Mirror](Part_Mirror.md): Mirrors the selected object across a mirror plane.

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scale](Part_Scale.md): Scales one or more shapes. <small>(v0.22)</small> 

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Fillet](Part_Fillet.md): Fillets (rounds) edges of an object.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chamfer](Part_Chamfer.md): Chamfers edges of an object.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Make face from wires](Part_MakeFace.md): Makes a face from a set of wires (contours).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Ruled Surface](Part_RuledSurface.md): Creates a ruled surface.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft.md): Lofts from one profile to another.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep.md): Sweeps one or more profiles along a path.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section.md): Creates a section by intersecting an object with a section plane.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cross sections\...](Part_CrossSections.md): Creates one or more cross-sections through an object.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Offset tools](Part_CompOffsetTools.md):
    -   <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Offset](Part_Offset.md): Constructs a parallel shape at a certain distance from an original.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Offset](Part_Offset2D.md): Constructs a parallel wire at certain distance from an original, or enlarges/shrinks a planar face.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Thickness](Part_Thickness.md): Hollows out a solid.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projection on surface](Part_ProjectionOnSurface.md): Projects a logo, text or any face, wire or edge onto a surface.

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Attachment](Part_EditAttachment.md): Attaches an object to another object.

### Boolean

These tools perform boolean operations.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width:48px;"> [Compound Tools](Part_CompCompoundTools.md):
    -   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Make compound](Part_Compound.md): Creates a compound from the selected objects.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explode Compound](Part_ExplodeCompound.md): Splits up compounds.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Compound Filter](Part_Compound‏‎Filter.md): Extracts the individual pieces from compounds.

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolean](Part_Boolean.md): Utför booleska operationer på objekt.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts (subtracts) one object from another.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Fuse](Part_Fuse.md): Fuses (unions) two or more objects.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Common](Part_Common.md): Extracts the common (intersection) part of two objects.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Join features](Part_CompJoinFeatures.md):
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connect](Part_JoinConnect.md): Connects interiors of walled objects.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embed](Part_JoinEmbed.md): Embeds a walled object into another walled object.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Cutout](Part_JoinCutout.md): Creates a cutout in a wall of an object for another walled object.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Splitting tools](Part_CompSplittingTools.md):
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Boolean fragments](Part_BooleanFragments.md): Creates all pieces obtained from Boolean operations.
    -   <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Slice apart](Part_SliceApart.md): Slices and splits an object by intersecting it with other objects.
    -   <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Slice](Part_Slice.md): Slices an object by intersecting it with other objects.
    -   <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [XOR](Part_XOR.md): Removes space shared by an even number of objects.

### Measure

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Measure Linear](Part_Measure_Linear.md): Creates a linear measurement.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Measure Angular](Part_Measure_Angular.md): Creates an angular measurement.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Measure Refresh](Part_Measure_Refresh.md): Updates all measurements.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Clear All](Part_Measure_Clear_All.md): Clears all measurements.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Toggle All](Part_Measure_Toggle_All.md): Shows or hides all measurements.

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Toggle 3D](Part_Measure_Toggle_3D.md): Shows or hides 3D measurements.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Toggle Delta](Part_Measure_Toggle_Delta.md): Shows or hides delta measurements.

### Other tools 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Import](Part_Import.md): Imports from \*.IGES, \*.STEP, or \*.BREP files.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Export](Part_Export.md): Exports to \*.IGES, \*.STEP, or \*.BREP files.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Box selection](Part_BoxSelection.md): Selects faces from a rectangular area.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Create shape from mesh](Part_ShapeFromMesh.md): Creates a shape object from a mesh object.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Create points object from geometry](Part_PointsFromMesh.md): Creates a points object from a geometric object.

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convert to solid](Part_MakeSolid.md): Converts a shape object to a solid object.

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Reverse shapes](Part_ReverseShape.md): Flips the normals of all faces of selected objects.

-   Create a copy:
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Create simple copy](Part_SimpleCopy.md): Creates a simple copy of a selected object.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Create transformed copy](Part_TransformedCopy.md): Creates a transformed copy of a selected object.
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Create shape element copy](Part_ElementCopy.md): Creates a copy from an element (vertex, edge, face) of a selected object.
    -   <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refine shape](Part_RefineShape.md): Cleans faces by removing unnecessary lines.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Check geometry](Part_CheckGeometry.md): Checks the geometry of selected objects for errors.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing/sv.md):


</div>

### Context menu items 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): Determines the appearance of a whole object (color, transparency etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors](Part_FaceColors.md): Assigns colors to individual faces of objects.

## Preferences

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferences](PartDesign_Preferences.md): Preferences available for Part Tools (the Part workbench also uses the PartDesign Preferences).
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import Export Preferences](Import_Export_Preferences.md): Preferences available for importing from and exporting to different file formats.
-   [Fine-tuning](Fine-tuning.md): Some extra parameters to fine-tune Part behavior.




<div class="mw-translate-fuzzy">

### Skript


</div>

See [Part scripting](Part_scripting.md).

## Tutorials

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md) : How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md) : How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md) : How to use the Part Module


<div class="mw-translate-fuzzy">


{{docnav/sv|Mesh Workbench/sv|Drawing Workbench/sv}}


</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Part_Workbench.md) > Part Module/sv
