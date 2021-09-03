




<img alt="Part workbench icon" src=images/Workbench_Part.svg  style="width:128px;">


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

## Introducere

Capacitățile de modelare a solidelor ale FreeCAD se bazează pe kernelul [Open Cascade Technology](http://en.wikipedia.org/wiki/Open_Cascade_Technology) (OCCT), un sistem CAD de calitate profesionistă, care oferă crearea și manipularea geometriei avansate 3D.


</div>

A more detailed discussion of Part workbench versus Part Design workbench can be found here: [Part and Part Design](Part_and_PartDesign.md).


<div class="mw-translate-fuzzy">

[Atelierul Piese](Part_Workbench/ro.md) permite utilizatorului să acceseze și să utilizeze obiectele și funcțiile OCCT. Obiectele piese, spre deosebire de [Mesh objects](Mesh_Workbench/ro.md), sunt mai complexe și, prin urmare, permit operații mai avansate cum ar fi operațiile booleene coerente, istoricul modificărilor și comportamentul parametric.


</div>

Part objects are more complex than mesh objects created with the [Mesh Workbench](Mesh_Workbench.md), as they permit more advanced operations like coherent boolean operations, modifications history, and parametric behaviour.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">


*The Part Workbench is the basic layer that exposes the OCCT drawing functions to all workbenches in FreeCAD.*

## Instrumente


<div class="mw-translate-fuzzy">

Instrumentele sunt toate amplasate în meniul {{MenuCommand|Part}}


</div>


<div class="mw-translate-fuzzy">

### Primitive


</div>

Acestea sunt instrumente pentru crearea de obiecte primitive grafice.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Box.png  style="width:32px;"> [Caseta](Part_Box/ro.md): Deseneaza o caseta prin specificarea dimensiunile sale
-   <img alt="" src=images/Part_Cylinder.png  style="width:32px;"> [Cilindru](Part_Cylinder/ro.md): Deseneaza un cilindru prin specificarea dimensiunile sale
-   <img alt="" src=images/Part_Sphere.png  style="width:32px;"> [Sfera](Part_Sphere/ro.md): Deseneaza o sfera prin specificarea dimensiunile sale
-   <img alt="" src=images/Part_Cone.png  style="width:32px;"> [Con](Part_Cone/ro.md): Deseneaza un con prin specificarea dimensiunile sale
-   <img alt="" src=images/Part_Torus.png  style="width:32px;"> [Tor](Part_Torus/ro.md): Deseneaza un tor (inel) prin specificarea dimensiunile sale
-   <img alt="" src=images/Part_CreatePrimitives.png  style="width:32px;"> [Creaza primitive](Part_CreatePrimitives/ro.md): Unealta pentru crearea primitivelor geometrice bazate pe parametrii
-   <img alt="" src=images/Part_Shapebuilder.png  style="width:32px;"> [Creaza forme](Part_Shapebuilder/ro.md): Unealta pentru crearea formelor complexe din primitive geometrice bazate pe parametrii


</div>

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylinder](Part_Cylinder.md): Creates a cylinder.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphere](Part_Sphere.md): Creates a sphere.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cone](Part_Cone.md): Creates a cone.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Torus](Part_Torus.md): Creates a torus (ring).

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube.md): Creates a tube. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Primitives](Part_Primitives.md): A tool to create one of the following primitives:
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
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Circle](Part_Circle.md): Creates a circular edge.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse.md): Creates an elliptical edge.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point.md): Creates a point (vertex).
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Line](Part_Line.md): Creates a line (edge).
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Regular Polygon](Part_RegularPolygon.md): Creates a regular polygon.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Builder](Part_Builder.md): Creates shapes from various primitives.


<div class="mw-translate-fuzzy">

### Modificarea obiectelor {#modificarea_obiectelor}


</div>


<div class="mw-translate-fuzzy">

Acestea sunt unelte pentru modificarea obiectelor existente. Ele permit alegerea obiectelor cu care se lucrează.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Extrude.png  style="width:32px;"> [Extrudare](Part_Extrude/ro.md): Extrudeaza fetele plane ale unui obiect
-   <img alt="" src=images/Part_Revolve.png  style="width:32px;"> [Rotatie](Part_Revolve/ro.md): Creaza un obiect prin rotirea altui obiect in jurul unei axe
-   <img alt="" src=images/Part_Mirror.png  style="width:32px;"> [Simetrizare](Part_Mirror/ro.md): Simetrizează obiectul selectat fata de un plan
-   <img alt="" src=images/Part_Fillet.png  style="width:32px;"> [Panglica](Part_Fillet/ro.md): Rotunjeste marginile unui obiect
-   <img alt="" src=images/Part_Chamfer.png  style="width:32px;"> [Tesire](Part_Chamfer/ro.md): Teseste marginile unui obiect
-   <img alt="" src=images/Part_RuledSurface.png  style="width:32px;"> [Ruled Surface](Part_RuledSurface/ro.md):
-   <img alt="" src=images/Part_Loft.png  style="width:32px;"> [Mansardare](Part_Loft/ro.md): Uneste un profil de altul
-   <img alt="" src=images/Part_Sweep.png  style="width:32px;"> [Baleiere](Part_Sweep/ro.md): Baleiază unul sau mai multe profile de-a lungul unei cai


</div>

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Revolve](Part_Revolve.md): Creates a solid by revolving an object (not a solid) around an axis.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Mirror](Part_Mirror.md): Mirrors the selected object across a mirror plane.

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Fillet](Part_Fillet.md): Fillets (rounds) edges of an object.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chamfer](Part_Chamfer.md): Chamfers edges of an object.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Make face from wires](Part_MakeFace.md): Makes a face from a set of wires (contours). <small>(v0.19)</small> 

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Ruled Surface](Part_RuledSurface.md): Creates a ruled surface.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Loft](Part_Loft.md): Lofts from one profile to another.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Sweep](Part_Sweep.md): Sweeps one or more profiles along a path.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section.md): Creates a section by intersecting an object with a section plane.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Cross sections\...](Part_CrossSections.md): Creates one or more cross-sections through an object.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Offset tools](Part_CompOffsetTools/ro.md):
    -   <img alt="" src=images/Part_Offset.png  style="width:32px;"> [3D Offset](Part_Offset/ro.md): Construiește o formă paralelă la o anumită distanță față de original.
    -   <img alt="" src=images/Part_Offset2D.png  style="width:32px;"> [2D Offset](Part_Offset2D/ro.md): Construiește o polilinie paralelă la o anumită distanță față de original, sau enlarges/shrinks o fațetă plană. (v0.17)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Thickness.png  style="width:32px;"> [Thickness](Part_Thickness/ro.md): Golește un solid, lăsând deschideri lângă fațetele selectate.


</div>

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projection on surface](Part_ProjectionOnSurface.md): Projects a logo, text or any face, wire or edge onto a surface. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_Attachment.svg  style="width:32px;"> [Attachment](Part_Attachment.md): Attaches an object to another object.

### Boolean

These tools perform boolean operations.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width:48px;"> [Compound Tools](Part_CompCompoundTools/ro.md):
    -   <img alt="" src=images/Part_MakeCompound.png  style="width:32px;"> [Make compound](Part_MakeCompound/ro.md): Creează un compus din obiectele selectate.
    -   <img alt="" src=images/Part_ExplodeCompound.svg  style="width:32px;"> [Explode Compound](Part_ExplodeCompound/ro.md): Instrumente pentru separarea unui compus din forme
    -   <img alt="" src=images/Part_Compound‏‎Filter.png  style="width:32px;"> [Compound Filter](Part_Compound‏‎Filter/ro.md): The CompoundFilter poate fi utilizat pentru a extrage piesele individuale.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Booleans.png  style="width:32px;"> [Logice](Part_Booleans/ro.md): Efectueaza operatii logice asupra obiectelor
-   <img alt="" src=images/Part_Union.png  style="width:32px;"> [Fuziune](Part_Union/ro.md): Uneste doua obiecte
-   <img alt="" src=images/Part_Common.png  style="width:32px;"> [Comun](Part_Common/ro.md): Extrage partea comuna a doua obiecte
-   <img alt="" src=images/Part_Cut.png  style="width:32px;"> [Decupare](Part_Cut/ro.md): Substrage on obiect din celalalt


</div>

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Cut](Part_Cut.md): Cuts (subtracts) one object from another.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Fuse](Part_Fuse.md): Fuses (unions) two objects.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Common](Part_Common.md): Extracts the common (intersection) part of two objects.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Join features](Part_CompJoinFeatures/ro.md): funcții booleene inteligente pentru obiecte de pus în perete (de ex țevi) (v0.16)
    -   <img alt="" src=images/Part_JoinConnect.png  style="width:32px;"> [Connect](Part_JoinConnect/ro.md): Conectează interiorul obiectelor (v0.16)
    -   <img alt="" src=images/Part_JoinEmbed.png  style="width:32px;"> [Embed](Part_JoinEmbed/ro.md): Include un obiect din perete într-un alt obiect din perete(v0.16)
    -   <img alt="" src=images/Part_JoinCutout.png  style="width:32px;"> [Cutout](Part_JoinCutout/ro.md): Crează o tăietură într-un peretele unui obiect pentru un alt obiect de pus în perete (v0.16)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Splitting tools](Part_CompSplittingTools/ro.md): (v0.17)
    -   <img alt="" src=images/Part_BooleanFragments.png  style="width:32px;"> [Boolean fragments](Part_BooleanFragments/ro.md): face toate piesele care pot fi obținute prin operații booleene între obiecte (v0.17)
    -   <img alt="" src=images/Part_SliceApart.svg  style="width:32px;"> [Slice a part](Part_SliceApart/ro.md): instrument pentru a separa forme prin intersecția cu alte forme
    -   <img alt="" src=images/Part_Slice.png  style="width:32px;"> [Slice](Part_Slice/ro.md): Separă un obiect în piese prin intersecții cu un alt obiect(v0.17)
    -   <img alt="" src=images/Part_XOR.png  style="width:32px;"> [XOR](Part_XOR/ro.md):

elimină spațiul partajat de un număr par de obiecte (versiunea simetrică a [Cut](Part_Cut/ro.md)) (v0.17)


</div>

### Measure

<img alt="" src=images/Part_Measure_Menu.png  style="width:64px;"> [Measure](Part_Measure_Menu.md): Tools for linear and angular measurements.

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Measure Linear](Part_Measure_Linear.md): Creates a linear measurement.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Measure Angular](Part_Measure_Angular.md): Creates an angular measurement.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Measure Refresh](Part_Measure_Refresh.md): Updates all measurements.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Clear All](Part_Measure_Clear_All.md): Clears all measurements.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Toggle All](Part_Measure_Toggle_All.md): Shows or hides all measurements.

-   <img alt="" src=images/Part_Measure_Toggle_3d.svg  style="width:32px;"> [Toggle 3D](Part_Measure_Toggle_3d.md): Shows or hides 3D measurements.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Toggle Delta](Part_Measure_Toggle_Delta.md): Shows or hides delta measurements.


<div class="mw-translate-fuzzy">

### Alte Instrumente {#alte_instrumente}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_ImportCAD.png  style="width:32px;"> [Import CAD](Part_ImportCAD/ro.md): Acest insrument vă permite să adăugați un fișier tip \*.IGES, \*.STEP, \*.BREP în documentul curent.
-   <img alt="" src=images/Part_ExportCAD.png  style="width:32px;"> [Export CAD](Part_ExportCAD/ro.md): Acest instrument vă permite să ecportați un obiect piesă într-un fișier tip \*.IGES, \*.STEP, \*.BREP .
-   <img alt="" src=images/Part_ShapeFromMesh.png  style="width:32px;"> [Shape from Mesh](Part_ShapeFromMesh/ro.md): Crează un obiect formă dintr-un obiect tip plasă.
-   [Convert to solid](Part_ConvertToSolid/ro.md): Convertește un obeict formă într-un obeict tip solid.
-   [Reverse shapes](Part_ReverseShapes/ro.md): Îndepărtează normalele tuturor fețelor obiectului selectat.
-   <img alt="" src=images/Part_CreateSimpleCopy‎.svg  style="width:32px;"> [Create simple copy](Part_CreateSimpleCopy/ro.md): Creează o simplă copie a obeictului selectat.
-   <img alt="" src=images/Part_RefineShape.png  style="width:32px;"> [Refine shape](Part_RefineShape/ro.md): Curăță fațetele prin ștergerea liniilor nenecesare.
-   <img alt="" src=images/Part_CheckGeometry.png  style="width:32px;"> [Check geometry](Part_CheckGeometry/ro.md): Verifică de erori geometria obiectelor selectate.
-   [Measure](Std_Measure_Menu/ro.md): Permite măsurări liniare și unghiulare între points/edges/faces.
-   <img alt="" src=images/Part_Attachment.svg  style="width:32px;"> [Attachment](Part_Attachment/ro.md): Atașamentul este o utilitatea de atașare a unui obiect la un altul .


</div>

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Export](Part_Export.md): Exports to \*.IGES, \*.STEP, or \*.BREP files.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [BoxSelection](Part_BoxSelection.md): Selects faces from a rectangular area.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Shape from Mesh](Part_ShapeFromMesh.md): Creates a shape object from a mesh object.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Points from mesh](Part_PointsFromMesh.md): Creates a shape object made of points from a mesh object. <small>(v0.19)</small> 

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convert to solid](Part_MakeSolid.md): Converts a shape object to a solid object.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width:32px;"> [Reverse shapes](Part_ReverseShapes.md): Flips the normals of all faces of selected objects.

-   Create a copy:
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Create simple copy](Part_SimpleCopy.md): Creates a simple copy of a selected object.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Create transformed copy](Part_TransformedCopy.md): Creates a transformed copy of a selected object. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Create shape element copy](Part_ElementCopy.md): Creates a copy from an element (vertex, edge, face) of a selected object. <small>(v0.19)</small> 
    -   <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Refine shape](Part_RefineShape.md): Cleans faces by removing unnecessary lines.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Check geometry](Part_CheckGeometry.md): Checks the geometry of selected objects for errors.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Defeaturing](Part_Defeaturing/ro.md): (v0.18)
-   <img alt="" src=images/Part_Section.png  style="width:32px;"> [Sectiune](Part_Section/ro.md): Creaza o sectiune prin intersectarea unui obiect cu planul de sectionare
-   <img alt="" src=images/Part_SectionCross.png  style="width:32px;"> [Cross sections\...](Part_SectionCross/ro.md):


</div>

### Context menu items {#context_menu_items}

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): Determines the appearance of a whole object (color, transparency etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors](Part_FaceColors.md): Assigns colors to individual faces of objects.

## Preferințe


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Preference \...](Import_Export_Preference/ro.md) Import Export


</div>

## Scripting

See [Part scripting](Part_scripting.md).


<div class="mw-translate-fuzzy">

## Tutorials

-   [Import from STL or OBJ](Import_from_STL_or_OBJ/ro.md) : How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ/ro.md) : How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial/ro.md) : How to use the Part Module


</div>

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md) : How to import STL/OBJ files in FreeCAD
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md) : How to export STL/OBJ files from FreeCAD
-   [Whiffle Ball tutorial](Whiffle_Ball_tutorial.md) : How to use the Part Module


<div class="mw-translate-fuzzy">


{{docnav/ro|[Mesh Workbench](Mesh_Workbench/ro.md)|[Drawing Workbench](Drawing_Workbench/ro.md)}}


{{Userdocnavi/ro}}


</div>


 

[Category:Part/ro](Category:Part/ro.md) [Category:Workbenches/ro](Category:Workbenches/ro.md) [Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
