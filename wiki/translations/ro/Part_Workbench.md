# Part Workbench/ro
<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="Part workbench icon" src=images/Workbench_Part.svg  style="width:128px;">


</div>





<div lang="en" dir="ltr" class="mw-content-ltr">

## Introduction


</div>


<div class="mw-translate-fuzzy">

## Introducere

Capacitățile de modelare a solidelor ale FreeCAD se bazează pe kernelul [Open Cascade Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT), un sistem CAD de calitate profesionistă, care oferă crearea și manipularea geometriei avansate 3D.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The Part Workbench can also create objects that are not solids, such as faces, shells, and objects with only edges or vertices. It also provides a variety of general purpose tools for geometry manipulation, geometry validation, and making copies.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) uses an alternative workflow for creating solids. For a detailed discussion of the Part Workbench versus the Part Design Workbench see [Part and Part Design](Part_and_PartDesign.md).


</div>

![](images/Part_Workbench_Example.jpg )



## Instrumente


<div lang="en" dir="ltr" class="mw-content-ltr">

### Solids toolbar 


</div>

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Caseta](Part_Box/ro.md): Deseneaza o caseta prin specificarea dimensiunile sale

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cilindru](Part_Cylinder/ro.md): Deseneaza un cilindru prin specificarea dimensiunile sale

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sfera](Part_Sphere/ro.md): Deseneaza o sfera prin specificarea dimensiunile sale

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Con](Part_Cone/ro.md): Deseneaza un con prin specificarea dimensiunile sale

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Tor](Part_Torus/ro.md): Deseneaza un tor (inel) prin specificarea dimensiunile sale

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube.md): Creates a tube.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Creaza primitive](Part_CreatePrimitives/ro.md): Unealta pentru crearea primitivelor geometrice bazate pe parametrii:


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plane](Part_Plane.md): Creates a plane.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Box](Part_Box.md): Creates a box. This object can also be created with the [Box](Part_Box.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder. This object can also be created with the [Cylinder](Part_Cylinder.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone. This object can also be created with the [Cone](Part_Cone.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere. This object can also be created with the [Sphere](Part_Sphere.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoid](Part_Ellipsoid.md): Creates a ellipsoid.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus. This object can also be created with the [Torus](Part_Torus.md) tool.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prism](Part_Prism.md): Creates a prism.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Wedge](Part_Wedge.md): Creates a wedge.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Helix](Part_Helix.md): Creates a helix.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spiral](Part_Spiral.md): Creates a spiral.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Circle](Part_Circle.md): Creates a circular arc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse.md): Creates an elliptical arc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Creates a point.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line.md): Creates a line.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regular polygon](Part_RegularPolygon.md): Creates a regular polygon.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Shape builder\...](Part_Builder.md): Creates shapes from various primitives.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Part tools toolbar 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](Sketcher_NewSketch.md): Creates a new sketch and opens the [Sketcher Dialog](Sketcher_Dialog.md) to edit it.


</div>

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrudare](Part_Extrude/ro.md): Extrudeaza fetele plane ale unui obiect

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Rotatie](Part_Revolve/ro.md): Creaza un obiect prin rotirea altui obiect in jurul unei axe

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Simetrizare](Part_Mirror/ro.md): Simetrizează obiectul selectat fata de un plan


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Scale](Part_Scale.md): Scales one or more shapes. <small>(v1.0)</small> 


</div>

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Panglica](Part_Fillet/ro.md): Rotunjeste marginile unui obiect

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Tesire](Part_Chamfer/ro.md): Teseste marginile unui obiect


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Make face from wires](Part_MakeFace.md): Makes a face from a set of wires (contours).


</div>

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Ruled Surface](Part_RuledSurface/ro.md):

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Mansardare](Part_Loft/ro.md): Uneste un profil de altul

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Baleiere](Part_Sweep/ro.md): Baleiază unul sau mai multe profile de-a lungul unei cai

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Sectiune](Part_Section/ro.md): Creaza o sectiune prin intersectarea unui obiect cu planul de sectionare

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cross sections\...](Part_SectionCross/ro.md):

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Offset:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [3D Offset](Part_Offset/ro.md): Construiește o formă paralelă la o anumită distanță față de original.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [2D Offset](Part_Offset2D/ro.md): Construiește o polilinie paralelă la o anumită distanță față de original, sau enlarges/shrinks o fațetă plană.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Thickness](Part_Thickness/ro.md): Golește un solid, lăsând deschideri lângă fațetele selectate.


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projection on surface](Part_ProjectionOnSurface.md): Projects a logo, text or any face, wire or edge onto a surface.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Color per face](Part_ColorPerFace.md): Assigns colors to individual faces of objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Boolean toolbar 


</div>

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Compound:

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Make compound](Part_Compound/ro.md): Creează un compus din obiectele selectate.


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explode Compound](Part_ExplodeCompound/ro.md): Instrumente pentru separarea unui compus din forme


</div>

  - <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Compound Filter](Part_Compound‏‎Filter/ro.md): The CompoundFilter poate fi utilizat pentru a extrage piesele individuale.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Boolean.svg  style="width:32px;"> [Boolean](Part_Boolean.md): Efectueaza operatii logice asupra obiectelor.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts one object from another.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse.md): Fuses two or more objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Intersection](Part_Common.md): Extracts the common part of two objects.


</div>

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Join:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connect](Part_JoinConnect/ro.md): Conectează interiorul obiectelor

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Embed](Part_JoinEmbed/ro.md): Include un obiect din perete într-un alt obiect din perete

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Cutout](Part_JoinCutout/ro.md): Crează o tăietură într-un peretele unui obiect pentru un alt obiect de pus în perete

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Split:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Boolean fragments](Part_BooleanFragments/ro.md): face toate piesele care pot fi obținute prin operații booleene între obiecte

  - <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Slice a part](Part_SliceApart/ro.md): instrument pentru a separa forme prin intersecția cu alte forme

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Slice](Part_Slice/ro.md): Separă un obiect în piese prin intersecții cu un alt obiect

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [XOR](Part_XOR/ro.md): elimină spațiul partajat de un număr par de obiecte (versiunea simetrică a [Cut](Part_Cut/ro.md))


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Check geometry](Part_CheckGeometry.md): Checks the geometry of selected objects for errors.


</div>

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing/ro.md)




<div class="mw-translate-fuzzy">

### Alte Instrumente 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Import](Part_Import.md): Imports from \*.IGES, \*.STEP, or \*.BREP files.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Export CAD file\...](Part_Export.md): Exports to \*.IGES, \*.STEP, or \*.BREP files.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Box selection](Part_BoxSelection.md): Selects faces from a rectangular area.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Create shape from mesh](Part_ShapeFromMesh.md): Creates shapes from mesh objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Create points object from geometry](Part_PointsFromMesh.md): Creates points objects from geometric objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convert to solid](Part_MakeSolid.md): Creates solids from shape objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Reverse shapes](Part_ReverseShape.md): Creates parametric copies with reversed face normals from selected objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Create a copy:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Create simple copy](Part_SimpleCopy.md): Creates non-parametric copies of objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Create transformed copy](Part_TransformedCopy.md): Creates non-parametric copies of objects. It is intended for objects nested in containers.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Create shape element copy](Part_ElementCopy.md): Creates non-parametric copies of subelements: vertices, edges and faces.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refine shape](Part_RefineShape.md): Creates parametric copies with a refined shape from selected objects. It removes unnecessary edges from planar and cylindrical faces.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Attachment\...](Part_EditAttachment.md): Attaches an object to one or more other objects.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Obsolete tools 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Measure


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Std Measure](Std_Measure.md) tool replaces the tools listed below. <small>(v1.0)</small> 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Measure Linear](Part_Measure_Linear.md): Creates a linear measurement. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Measure Angular](Part_Measure_Angular.md): Creates an angular measurement. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Measure Refresh](Part_Measure_Refresh.md): Updates all measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Clear All](Part_Measure_Clear_All.md) and [View Measure Clear All](View_Measure_Clear_All.md): Clears all measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Toggle All](Part_Measure_Toggle_All.md) and [View Measure Toggle All](View_Measure_Toggle_All.md): Shows or hides all measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Toggle 3D](Part_Measure_Toggle_3D.md): Shows or hides 3D measurements. Not available in <small>(v1.0)</small> .


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Toggle Delta](Part_Measure_Toggle_Delta.md): Shows or hides delta measurements. Not available in <small>(v1.0)</small> .


</div>



## Preferințe


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preference \...](Import_Export_Preferences/ro.md) Import Export


</div>

## Scripting


<div lang="en" dir="ltr" class="mw-content-ltr">

See [Part scripting](Part_scripting.md).


</div>

## Tutorials

-   [Import from STL or OBJ](Import_from_STL_or_OBJ/ro.md) : How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ/ro.md) : How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial/ro.md) : How to use the Part Workbench


<div class="mw-translate-fuzzy">


{{docnav/ro|[Mesh Workbench](Mesh_Workbench/ro.md)|[Drawing Workbench](Drawing_Workbench/ro.md)}}


{{Userdocnavi/ro}}


</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/ro
