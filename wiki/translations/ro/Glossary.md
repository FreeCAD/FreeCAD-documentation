# Glossary/ro
Această pagină este un glosar de termeni și definiții comune ale FreeCAD.

Salt la literă: {{CompactTOC|center=yes}}

## 0-9


{{gloss}}


{{term|3D view|content=[3D view](3D_view.md)}}


{{defn|defn=The 3D view is a component of the FreeCAD [interface](Interface.md). It shows a 3D representation of the model.}}


{{glossend}}

## A


<div class="mw-translate-fuzzy">

## A 


{{gloss}}


{{term|Arc}}


{{defn|defn=O porțiune sau un segment de cerc.}}


{{term|Arch|content=[Arch](Arch_Workbench.md)}}


{{defn|defn=O abreviere pentru Arhitectură [workbench](#Workbench.md) care este folosită în principal pentru modelarea clădirilor și a structurilor. În strânsă legătură cu [Draft Workbench](#Draft.md).}}


{{term|Assembly|content=[Assembly](Assembly.md)}}


{{defn|no=1|defn=Un set de [parts](#Part.md) care au definite pozițiile în relația fiecare cu celaltă.}}


{{defn|no=2|defn=A [workbench](#Workbench.md) care urmărește să faciliteze crearea de ansambluri. Acest Atelier este în curs de dezvoltare și încă nu face parte din FreeCAD.}}


{{term|Axis}}


{{defn|defn= O linie imaginară care trece prin originea spațiului de lucru. Există 3 axe normale. Ele au numele clasic de X, Y și Z. X este în parte stângă sau dreapta. Y este în parte de sus sau în partea de jos. Z este în interiorul sau în afara ecranului/paginii(cea de-a treia dimensiune) .}}


{{glossend}}


</div>

## B


<div class="mw-translate-fuzzy">

## B 


{{gloss}}


{{term|Backtrace}}


{{defn|defn=Ieșire dintr-un program de depanare care afișează seria de instrucțiuni pe care FreeCAD le-a urmat înainte de apariția unei probleme.}}


{{term|Bezier Curve|content=[http://en.wikipedia.org/wiki/B%C3%A9zier_curve Bezier Curve]}}


{{defn|defn=Un tip de curbă parametrică}}


{{term|Blueprint}}


{{defn|defn=Vechi termen utilizat pentru [drawing](#Drawing.md), și formulat prntru originalul său [http://en.wikipedia.org/wiki/Blueprint reproduction process].}}


{{term|Body}}


{{defn|defn=Un tip de container utilizat în Atelierul [PartDesign](PartDesign_Workbench.md) [workbench](#Workbench.md) care grupează o secvență de operații ([sketches](#Sketch.md), de construcție geometrică și[features](#Feature.md)) pentru a crea un solid invecinat. (Introduced in FreeCAD V0.17.)}}


{{term|Boolean Logic}}


{{defn|defn=O metodă de manipularea datelor utilizând operanzii: And, Or, Not.}}


{{term|Boolean Operation}}


{{defn|defn=O metodă de maipulare a aobiectelor folosind logica Boolean. În FreeCAD, operațiile Boolean sunt: Union ([Fuse](#Fuse.md)), Difference ([Cut](#Cut.md)), Intersection, and Section.}}


{{term|Boolean OPerations check}}


{{defn|defn=See [BOPcheck](#BOPcheck.md).}}


{{term|BOPcheck}}


{{defn|defn= O setare care permite instrumentului de verificare a geometriei din partea WB(Atelierului) și OpenSCAD WB să verifice și geometria făcută din [Boolean logic](#Boolean_Logic.md). Setarea implicită este "false" (sau off) dar utilizatorul îi poate permite să furnizeze mai multă precizie atunci când execută o Check Geometry, dar acest lucru este în detrimentul timpilor de procesare a  unei Check Geometry . Setarea este activată prin navigarea pe traseul Tools > Edit Parameters > Preferences folder > Mod folder > Part folder > Check geometry folder, apoi dublu click "false" în tab-ul drept, schimbarea valorii la "True", click pe butonul "OK", click pe butonul"Save to disk", apoi click pe butonul "Close". O captură de ecran și o descriere a procedurii de activare BOPCheck este la adresa [http://forum.freecadweb.org/viewtopic.php?t=8031#p65914 in post[rile de pe acest forum].}}


{{term|brep}}


{{defn|defn=Format nativ de fișier pentru [Open CASCADE](#Open_CASCADE.md) și este partajat de câteva aplicații. FreeCAD poate salva în format *.brep .}}


{{term|B-rep}}


{{defn|defn=Stands for [http://en.wikipedia.org/wiki/B-rep boundary representation],care este unul dintre cele două tipuri de modele 3D pe care FreeCAD le suportă (cealaltă fiind[mesh](#Mesh.md)).}}


{{term|B-spline}}


{{defn|defn=Un tip de curbă parametrică. Vezi [http://en.wikipedia.org/wiki/B-spline B-spline]}}


{{glossend}}


</div>

## C


<div class="mw-translate-fuzzy">

## C 


{{gloss}}


{{term|Callout}}


{{defn|defn=String of text connected to a line pointing to an object in a [drawing](#Drawing.md).}}


{{term|Chamfer}}


{{defn|defn=The cutting off of an edge, at an angle, to get rid of its sharpness; a beveled edge.}}


{{term|1=Clipping Plane}}


{{defn|1=The clipping plane is used to cut away at the model in the 3D view. It is just a visual aid and does not actually cut the model.}}


{{term|Clone}}


{{defn|defn=A copy of an object whereby the copy remains parametric.  When the original object is changed the Clone(s) also change to show modifications made to the original object.}}


{{term|Coin}}


{{defn|defn=Also called Coin3D. Third-party software library used for 3D representation by FreeCAD.}}


{{term|COLLADA}}


{{defn|defn=An interchange file format for [mesh](#Mesh.md) models. File extension is *.dae.}}


{{term|Command|content=[Command](Command.md)}}


{{defn|defn=An action invoked from the [Gui](#GUI.md) when you press a toolbar button or type a keyboard shortcut or type into the python console. }}


{{term|Compound}}


{{defn|defn=Groups objects together without fusing them like a [boolean union](#Boolean_Operation.md) would.}}


{{term|CompSolid}}


{{defn|defn=Set of [solids](#Solid.md) connected by their [faces](#Face.md). CompSolids are needed in [FEM](#FEM.md), where more than one material is used in one FEM-mesh.}}


{{term|1=Constraint}}


{{defn|1=A restriction on the geometric relationship between primitives in a [Sketch](#Sketch.md). If a constraint has a numerical value, it is referred to as Datum (e.g., a distance constraint has a numerical value - the length of an imaginary line connecting the two points). A constraint that has no numerical value (e.g., a Horizontal constraint) is sometimes referred to as Geometric Constraint.}}


{{term|Constructive Solid Geometry|content=[http://en.wikipedia.org/wiki/Constructive_solid_geometry Constructive Solid Geometry]}}


{{defn|defn=A solid modeling method for creating shapes by using [boolean operations](#Boolean_Operation.md) on [primitives](#Primitive.md).}}


{{term|Coordinate}}


{{defn|defn=A number which defines the position of an object in space in reference to a [http://en.wikipedia.org/wiki/Cartesian_coordinate_system coordinate system].}}


{{term|Coplanar}}


{{defn|defn=Existing on the same plane.}}


{{term|CSG}}


{{defn|defn=Short for [Constructive Solid Geometry](#Constructive_Solid_Geometry.md).}}


{{term|Cut}}


{{defn|defn=Applying a [boolean difference](#Boolean_Operation.md) between shapes.}}


{{glossend}}


</div>

## D


<div class="mw-translate-fuzzy">

## D 


{{gloss}}


{{term|DAG}}


{{defn|defn=See [Directed Acyclic Graph.](#Directed_Acyclic_Graph.md)}}


{{term|Degrees Of Freedom}}


{{defn|defn=The number of ways geometry in a [Sketch](#Sketch.md) may vary.  For example, if we have a Sketch consisting of only one point, and the point has no [Constraints](#Constraint.md) applied to it, the point has two [DOF](#DOF.md) because it is free to move both vertically and horizontally.  Similarly, a Sketch consisting of only a single unconstrained circle has three [DOF](#DOF.md) because the circle can move vertically and horizontally and, additionally, the radius is not defined.  It is good practice to constrain a Sketch until it has no [DOF](#DOF.md) remaining, in which case it is said to be [Fully Constrained](#Fully_Constrained.md).}}


{{term|Dependency Graph}}


{{defn|defn=A third-party graphing tool used to show how objects in a FreeCAD model use or are related to one another.  For more information, refer to the [Dependency Graph Wiki page](Std_DependencyGraph.md)|.}}


{{term|Difference}}


{{defn|no=1|defn=The result of, or remainder of, a subtraction.}}


{{defn|no=2|defn=A [Boolean Operation](#Boolean_operation.md) in the [Part](Part_Workbench.md) [workbench](#Workbench.md) which is used to subtract one geometry from another; it results in a [Cut](#Cut.md).}}


{{term|Directed Acyclic Graph}}

(abbreviated as \"DAG\") {{defn|defn=A type of [Dependency Graph](#Dependency_Graph.md) where the relationship of objects flows in a generally linear direction from start to end with no circular dependencies.  When following a DAG there is no flow from one object A to any other objects and then back to that same object A again.  In FreeCAD, a graph of the model must always be a DAG.}} {{term|DOF}} {{defn|[Degrees Of Freedom](#Degrees_Of_Freedom.md)}} {{term|Draft|content=[Draft](Draft_Workbench.md)}} {{defn|no=1|defn=A FreeCAD [workbench](#Workbench.md) used primarily for 2 dimensional work.}} {{defn|no=2|defn=A relief angle on a mold to allow removal of the finished product. See [Drawing|content=[[Drawing_Workbench|Drawing](PartDesign_Draft]].}} {{term.md)}} {{defn|no=1|defn=A FreeCAD [workbench](#Workbench.md) used to generate 2D representations of a model, also called drawings.}} {{defn|no=2|defn=Describes a representation of geometry through the use of two-dimensional views. Also called plan or [blueprint](#Blueprint.md).}} {{glossend}}


</div>

## E


<div class="mw-translate-fuzzy">

## E 


{{gloss}}


{{term|Edge}}


{{defn|no=1|defn=A segment joining two [vertices](#Vertex.md). This segment can be a straight line or a curve. The CAD kernel defines it as: One-dimensional shape corresponding to a curve and bounded by a vertex at each extremity. A closed circle has therefore only one vertex, where it starts and ends. [ see Profile: Defining the Topology](https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3.md).}}


{{defn|no=2|defn=The joining line between two faces. It can be curved or straight.}}


{{term|Element}}


{{defn|An item of Sketcher geometry such as a point, a line segment, an arc, a circle, etc.}}


{{term|1=Extrude}}


{{defn|1=A general term for extending a 2D object into 3D along 1 direction. See also [Pad](#Pad.md).}}


{{glossend}}


</div>

## F


<div class="mw-translate-fuzzy">

## F 


{{gloss}}


{{term|1=Face}}


{{defn|1=A 2 dimensional topological construct.  For example, a cube has 6 Faces. A face can be curved, like in case of a sphere, which has one face in FreeCAD. The CAD kernel defines it as: Part of a surface bounded by a closed [wire(s)](#Wire.md). See [Profile: Defining the Topology](https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3.md).}}


{{term|Facet}}


{{defn|defn=Often used to describe planar faces on a [mesh](#Mesh.md).}}


{{term|FC}}


{{defn|defn=Short for FreeCAD.}}


{{term|FCStd}}


{{defn|defn=FreeCAD native file format. File extension *.fcstd, *.FCStd}}


{{term|1=Feature}}


{{defn|1=A step in a 3d part's evolution in the [Part Design](PartDesign_Workbench.md) [workbench](#Workbench.md) workflow.  Examples are [Pad](#Pad.md), [Pocket](#Pocket.md), [Groove](#Groove.md), [Fillet](#Fillet.md), etc.  As we create a model in the [Part Design](PartDesign_Workbench.md) [workbench](#Workbench.md), each feature takes the shape of the last one and adds or removes something.  Hence a "Pocket" feature is not only the pocketed hole itself, but the whole part with the pocket feature.}}


{{term|FEM|content=[FEM](FEM_Workbench.md)}}


{{defn|defn=[https://en.wikipedia.org/wiki/Finite_element_method Finite Element Method], a [workbench](#Workbench.md) used to solve engineering and mathematical physics problems associated with parts, assemblies and structures.}}


{{term|Fillet}}


{{defn|defn=A rounded relief or cut at an edge added for a finished appearance and to break sharp edges. See [[Part Fillet]] and [[PartDesign Fillet]].}}


{{term|Fork}}


{{defn|defn=See [Forked Model](#Forked_Model.md).}}


{{term|Forked Model}}


{{defn|defn=A modeling method, usually accidental and incorrect in FreeCAD, that creates two or more versions of a model from a previous item. (Not to be confused with intentional operations like Array, Clone, PolarPattern, etc.)}}


{{term|Frenet}}


{{defn|defn=When Sweeping a profile along a 3D path, the Frenet parameter controls the orientation of the profile as it travels along the path. If Frenet is true, the profiles are oriented using the Frenet Frame (tangent, binormal, normal) of the path. If Frenet is false the profile's rotation is not restricted. [http://en.wikipedia.org/wiki/Frenet_Frame]}}


{{term|Freetype|content=[http://www.freetype.org FreeType]}}


{{defn|defn=A freely available software library used to extract information from font definition files.}}


{{term|Frustum|content=[http://en.wikipedia.org/wiki/Frustum Frustum]}}


{{defn|defn=The portion of a solid that lies between two parallel planes cutting it. Used in computer graphics to describe the three-dimensional region which is visible on the screen, the [http://en.wikipedia.org/wiki/Viewing_frustum "viewing frustum"]}}


{{term|Fully Constrained}}


{{defn|defn=In [Sketcher](#Sketcher.md), when a [Sketch](#Sketch.md) has no [Degrees Of Freedom](#Degrees_Of_Freedom.md), the Sketch is said to be "fully constrained" by the applied [Constraints](#Constraint.md).}}


{{term|Fuse}}


{{defn|defn=Term commonly used in FreeCAD to refer to a [boolean union](#Boolean_Operation.md) of shapes.}}


{{glossend}}


</div>

## G


<div class="mw-translate-fuzzy">

## G 


{{gloss}}


{{term|GDB or gdb}}


{{defn|defn=[https://www.gnu.org/software/gdb/ '''G'''NU Project '''D'''e'''B'''ugger], a debugging program used on Unix and other 'nix operating systems in order to get a [backtrace](#Backtrace.md). "gdb" (without the quotation marks) is also the first part of the command used to start the GDB program itself.  An example of how to use GDB with FreeCAD is in [http://forum.freecadweb.org/viewtopic.php?t=7052#p56918 this forum post]}}


{{term|Geometric modeling kernel}}


{{defn|defn=Also called CAD kernel. A set of complex software libraries responsible for the creation of 3D shapes. All operations on objects (extrude, boolean operations, chamfer, fillet) rely on the geometric modeling kernel.}}


{{term|Git}}


{{defn|defn=[http://en.wikipedia.org/wiki/Distributed_revision_control Distributed revision control system] used by FreeCAD to host and manage its code base.}}


{{term|[Group](Std_Group.md)}}


{{defn|defn=Used to organize elements in the Model tree.}}


{{term|GUI}}


{{defn|defn='''G'''raphical '''U'''ser '''I'''nterface. Allows users to interact with FreeCAD through graphical icons and the mouse pointer.}}


{{glossend}}


</div>

## H


<div class="mw-translate-fuzzy">

## H 


{{gloss}}


{{term|Half_Space|content=[http://en.wikipedia.org/wiki/Half-space_%28geometry%29 Half Space]}}


{{defn|defn=When a plane completely divides a 3D Euclidian space, the plane forms two half spaces.}}


{{glossend}}


</div>

## I


<div class="mw-translate-fuzzy">

## I 


{{gloss}}


{{term|IGES}}


{{defn|defn=A file format for the exchange of product data models. Files extensions are *.iges, *.igs. See also [STEP](#STEP.md).}}


{{term|Intersection|content=[http://en.wikipedia.org/wiki/Intersection Intersection]}}


{{defn|defn=That portion of two or more geometric entities that is common to all.  For example, the intersection of two lines is a point.}}


{{glossend}}


</div>

## J


<div class="mw-translate-fuzzy">

## J 


{{gloss}}


{{term|JT}}


{{defn|defn=A proprietary 3D data format developed by Siemens PLM Software.  FreeCAD has no support for JT at this time.}}


{{glossend}}


</div>

## K


<div class="mw-translate-fuzzy">

## K 


{{gloss}}


{{term|Kernel}}


{{defn|defn=See [Geometric modeling kernel](#Geometric_modeling_kernel.md).}}


{{term|KML}}


{{defn|defn=Keyhole Markup Language -  an XML-based geospatial 3D data definition file used by Google Earth.  FreeCAD has no support for KML at this time.}}


{{glossend}}


</div>

## L


<div class="mw-translate-fuzzy">

## L 


{{gloss}}


{{term|Label}}


{{defn|no=1|defn=A user defined property of an object; used to make the model tree easier to understand by humans.}}


{{defn|no=2|defn=A string of descriptive text added to a drawing (see [Draft Label](Draft_Label.md)).}}


{{defn|defn=Contrast with [Name](#Name.md).}}


{{term|Line}}


{{defn|defn=Most often this is used as a synonym for a line segment (see below). In sketcher it is used sometimes with its exact meaning of an infinite straight path.}}


{{term|Line Segment}}


{{defn|defn=A straight path between two [points](#Point.md).}}


{{term|Lock}}


{{defn|defn=[Constraint Lock](Sketcher_ConstrainLock.md)}}


{{term|Loft|content=[http://en.wikipedia.org/wiki/Loft_%283D%29 Loft]}}


{{defn|defn=A topological form created by linking consecutive profiles with a surface.  Similar to the process used to make fabric covered aeroplanes or boats. Also the FreeCAD function for creating such a form.}}


{{glossend}}


</div>

## M


<div class="mw-translate-fuzzy">

## M 


{{gloss}}


{{term|Macro}}


{{defn|defn=A saved sequence of FreeCAD instructions, often written by end users.}}


{{term|Manifold}}


{{defn|defn=Said of a [shape](#Shape.md) that forms a perfectly enclosed volume. A familiar synonym that gives a good description is "watertight". To generate a solid, a [shell](#Shell.md) must be manifold.}}


{{term|Mantis}}


{{defn|defn=[Bug tracking system](#Tracker.md) used by the FreeCAD project.}}


{{term|Mesh}}


{{defn|defn=Type of object that can be imported or created by FreeCAD. See [http://en.wikipedia.org/wiki/Polygon_mesh Polygon mesh] for more details.}}


{{term|Model}}


{{defn|defn=Also called 3D model. Computer representation of a three-dimensional [part](#Part.md) or [assembly](#Assembly.md).}}


{{term|MultiTransform|content=[MultiTransform](PartDesign_MultiTransform.md)}}


{{defn|defn=Stands for multiple transformation. A [feature](#Feature.md) from the [PartDesign](PartDesign_Workbench.md) [workbench](#Workbench.md) that applies a series of chained transformations (linear and circular pattern, mirrored) to selected features.}}


{{glossend}}


</div>

## N


<div class="mw-translate-fuzzy">

## N 


{{gloss}}


{{term|Name}}


{{defn|defn=An unique identifier for a FreeCAD document object. Once assigned by the program, the Name can not be easily changed.  Contrast with [Label](#Label.md).}}


{{term|Non-manifold}}


{{defn|defn=Non-manifold topology, also called zero-thickness, is two distinct solid bodies connected at a theoretical vertex or edge. It is an unsupported type of shape (not always detected by FreeCAD) that should be avoided, as it can cause trouble with further steps and export.}}


{{term|Null Shape}}


{{defn|defn=A [Shape](#Shape.md) property that has not been initialized by a program/macro.  Usually an error condition.}}


{{glossend}}


</div>

## O


<div class="mw-translate-fuzzy">

## O 


{{gloss}}


{{term|OCC}}


{{defn|defn=Acronym for [Open CASCADE](#Open_CASCADE.md). Prior to being open sourced, it used to be named CAS.CADE (abbreviated from Computer Aided Software for Computer Aided Design and Engineering).}}


{{term|OCE}}


{{defn|defn='''O'''pen CASCADE '''C'''ommunity '''E'''dition. It provides patches, improvements and experiments contributed by users over the official [Open CASCADE](#Open_CASCADE.md) library. FreeCAD is known to work on either OCC or OCE.}}


{{term|OCCT}}


{{defn|Open CASCADE Technology. See [OCC](#OCC.md).}}


{{term|Open CASCADE|content=[http://www.opencascade.org Open CASCADE]}}


{{defn|The [geometric modeling kernel](#Geometric_modeling_kernel.md) (software library) underlying FreeCAD. Also called [OCC](#OCC.md) or [OCCT](#OCCT.md) (for Open CASCADE Technology). See also [OCE](#OCE.md).}}


{{term|OpenSCAD|content=[http://www.openscad.org/ OpenSCAD]}}


{{defn|no=1|Name of a script-only based CAD program.}}


{{defn|no=2|A [workbench](#Workbench.md) in FreeCAD. The [OpenSCAD](OpenSCAD_Workbench.md) [workbench](#Workbench.md) provides an interface for import/export of *.scad and *.csg models, as well as a some utility tools.}}


{{term|Origin}}


{{defn|defn=The center of the coordinate system. Everything goes out from here in either the positive or negative directions. As is our view of the universe with Earth being the “origin”.}}


{{term|Orthographic}}


{{defn|defn=See [http://en.wikipedia.org/wiki/Orthographic_projection Orthographic projection] and [http://en.wikipedia.org/wiki/Multiview_orthographic_projection Multiview orthographic projection].}}


{{glossend}}


</div>

## P


<div class="mw-translate-fuzzy">

## P 


{{gloss}}


{{term|1=Pad}}


{{defn|1=An extension of a [Sketch](#Sketch.md) in a direction perpendicular to the plane of the Sketch. See also [Extrude](#Extrude.md).}}


{{term|Part|content=[Part](Part_Workbench.md)}}


{{defn|no=1|A FreeCAD [workbench](#Workbench.md) primarily used for a [http://en.wikipedia.org/wiki/Constructive_solid_geometry Constructive Solid Geometry] workflow.}}


{{defn|no=2|A unibody solid. The lowest level component in an assembly.}}


{{defn|no=3|A container which groups any type of FreeCAD object and has a [placement](#Placement.md). (Introduced in FreeCAD V0.17.)}}


{{term|PartDesignNext}}


{{defn|defn=Nickname used over the forums to distinguish the [PartDesign](PartDesign_Workbench.md) [workbench](#Workbench.md) in the FreeCAD 0.17 release version from the one in v0.16 and earlier, because of the vast changes introduced.}}


{{term|PD}}


{{defn|defn=Abbreviation of [PartDesign](PartDesign_Workbench.md), a FreeCAD [workbench](#Workbench.md).}}


{{term|PDN}}


{{defn|defn=Abbreviation of [PartDesignNext](#PartDesignNext.md).}}


{{term|Perspective}}


{{defn|defn=[http://en.wikipedia.org/wiki/Graphical_projection#Perspective Perspective projection]}}


{{term|Pivy|content=[http://pypi.python.org/pypi/Pivy Pivy]}}


{{defn|defn=A software library that allows Python to use Coin.}}


{{term|Placement}}


{{defn|defn=Set of properties of an object that defines its coordinates and orientation in space. See [[Placement]].}}


{{term|Planar}}


{{defn|defn=Said of geometry of which elements all lie on a same plane.}}


{{term|Plane}}


{{defn|no=1|A flat, two-dimensional surface that extends infinitely far.}}


{{defn|no=2|A primitive two-dimensional object created in the [Part](Part_Workbench.md) [workbench](#Workbench.md).}}


{{term|Plot}}


{{defn|defn=<To be added.>}}


{{term|1=Pocket}}


{{defn|1=A [feature](#Feature.md) that removes material from a solid based on a [Sketch](#Sketch.md).}}


{{term|1=Point}}


{{defn|1=An item used to reference a single area in the 3D workspace. A “point” is dimensionless. It has a dimension on the screen, usually represented by a “dot” only so we can see where it is. See also [Vertex](#Vertex.md).}}


{{term|Polygon mesh}}


{{defn|defn=See [http://en.wikipedia.org/wiki/Polygonal_mesh Polygonal_mesh]}}


{{term|Polyline}}


{{defn|defn=A series of connected line or arc segments.}}


{{term|POV-Ray}}


{{defn|defn=[http://en.wikipedia.org/wiki/POV-Ray POV-Ray]}}


{{term|PPA}}


{{defn|defn=An acronym that stands for '''P'''ersonal '''P'''ackage '''A'''rchive. It's a type of software repository exclusive to the Ubuntu Linux operating system. The FreeCAD project offers the latest release as well as development versions through two PPA repositories. Updates are managed by the host system's update manager.}}


{{term|Primitive}}


{{defn|defn=A basic shape used in the construction of models. Some 2D primitives are: point, line, polygon, circle, ellipse, spiral, helix. 3D primitives are: box, cylinder, cone, torus, sphere, ellipsoid, prism.}}


{{term|PySide|content=[https://wiki.qt.io/PySide PySide]}}


{{defn|defn=A freely available software library that allows Python to use QT.}}


{{term|Python|content=[http://www.python.org Python]}}


{{defn|defn=A programming language used in the development of FreeCAD as well as in user-written [macros](#Macro.md) or scripts.}}


{{glossend}}


</div>

## Q


<div class="mw-translate-fuzzy">

## Q 


{{gloss}}


{{term|Qt|content=[https://www.qt.io/developers/ Qt]}}


{{defn|1=A cross-platform application and user interface framework. Also Qt4.}}


{{glossend}}


</div>

## R


<div class="mw-translate-fuzzy">

## R 


{{gloss}}


{{term|Raytracing}}


{{defn|defn=[http://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29 Ray tracing]}}


{{term|Revolve}}


{{defn|defn=A tool in the [Part](Part_Workbench.md) [workbench](#Workbench.md). See [[Part Revolve]].}}


{{term|Robot}}


{{defn|defn=[http://en.wikipedia.org/wiki/Industrial_robot Industrial robot]}}


{{term|Rotate}}


{{defn|defn=Action to spin an object unto an axis to change its orientation in space.}}


{{glossend}}


</div>

## S


<div class="mw-translate-fuzzy">

## S 


{{gloss}}


{{term|Section}}


{{defn|defn=[http://en.wikipedia.org/wiki/Cross_section_%28geometry%29 Cross section (geometry)]}}


{{term|Self Intersection}}


{{defn|defn=A condition where a curve crosses over itself (ex.'8','&'). This confuses geometric kernel algorithms and generally produces an error condition.}}


{{term|Shape}}


{{defn|defn=Generic term used in FreeCAD to describe most elements (except for [meshes](#Mesh.md)).}}


{{term|Shell}}


{{defn|defn=Shape made of two or more contiguous [faces](#Face.md). A [manifold](#Manifold.md) (enclosed) shell can be converted into a [solid](#Solid.md).}}


{{term|1=Sketch}}


{{defn|1=A constrained 2D depiction of an object fixed to a plane or a [Face](#Face.md).  In FreeCAD a Sketch is always a 2-dimensional object somewhere in the 3D space.}}


{{term|Sketcher|content=[Sketcher](Sketcher_Workbench.md)}}


{{defn|A [workbench](#Workbench.md) used to create 2D geometry by use of [elements](#Element.md) and [constraints](#Constraint.md).}}


{{term|Sketcher Solver}}


{{defn|defn=The internal FreeCAD mechanism that calculates inter-dependencies and effects of adding, deleting, and modifying geometry and associated constraints in each Sketch.  Sketcher Solver also calculates the arrangement of all geometry in each Sketch so it can be displayed correctly.}}


{{term|Smooth Line}}


{{defn|defn=In a Drawing, a line indicating a change between tangent surfaces, as in the transition from a flat surface to a fillet. Also "tangent edge". See [http://www.freecadweb.org/wiki/index.php?title=Drawing_View#Modify_an_existing_view Drawing View]}}


{{term|Solid}}


{{defn|defn=Part of 3D space bounded by [Shells](#Shell.md). A solid has a volume and other properties related to objects with a mass.}}


{{term|Solver}}


{{defn|defn=See [Sketcher Solver](#Sketcher_Solver.md).}}


{{term|1=Stable}}


{{defn|1=A nickname for the last general release version of the FreeCAD software.  This is typically the version available from sources other than the FreeCAD project.  Compare with [Unstable](#Unstable.md).}}


{{term|STL}}


{{defn|''STereoLithography'', also known as ''Standard Tessellation Language.'' A [mesh](#Mesh.md) file format defining only the surface of a 3D object. File extensions is *.stl}}


{{term|STEP}}


{{defn|defn=An ISO standard (ISO 10303) for the exchange of 3D data and product manufacturing information. It replaces [IGES](#IGES.md). File extensions are *.step, *.stp.}}


{{term|SVG}}


{{defn|[https://en.wikipedia.org/wiki/Scalable_Vector_Graphics '''S'''calable '''V'''ector '''G'''raphics]. A vector graphics file format.}}


{{term|Sweep}}


{{defn|defn=A 3D shape generated from at least one 2D cross-section that traces along a trajectory (path). Commonly used to define the tool as well as the created shape. See [http://en.wikipedia.org/wiki/Solid_modeling#Sweeping Solid modeling]}}


{{glossend}}


</div>

## T


<div class="mw-translate-fuzzy">

## T 


{{gloss}}


{{term|Task panel}}


{{defn|defn=See [Tasks tab](#Tasks_tab.md).}}


{{term|Tasks tab}}


{{defn|defn=A [https://en.wikipedia.org/wiki/Panel_(computer_software) control panel] in FreeCAD that displays content specific to the task at hand. It can show available tools in the active [workbench](#Workbench.md) or prompt for values and options while a [command](#Command.md) is active.}}


{{term|Tessellation}}


{{defn|defn=A tessellation of a surface is the tiling of the surface using one or more geometric shapes, called tiles, with no overlaps and no gaps. In FreeCAD it is needed to display the geometric shapes in the 3D-view. The tessellation relative to the dimensions of a shape can be set in the preferences to get a smoother view of round surfaces at the cost of computation time. See [Preferences Editor](Preferences_Editor.md).}}


{{term|Thickness}}


{{defn|no=1|defn=A measure of how thick a shape is.}}


{{defn|no=2|A [Part](Part_Workbench.md) [workbench](#Workbench.md) tool to hollow out a solid and leave a defined uniform thickness.}}


{{term|Toggle}}


{{defn|defn=A setting that can be changed between two options, for example between True or False or between Off and On.}}


{{term|Topological Naming}}


{{defn|A scheme whereby an edge or face, once created, is assigned a permanent name.  Internally, FreeCAD identifies edges and faces on a solid by numbering them such as: Edge1, Edge2, Face1, Face2, etc. The problem is that these IDs are somewhat randomly applied, and they will change after something is done to the model that changes the amount of edges and faces.  For example, if the model is revised an item linked to a Face2 could later erroneously become linked to a different face (which was renamed to become the new Face2), causing the user unwanted results.  As of the FreeCAD 0.17 release Topological Naming has not yet been implemented, and so if an object is modified such that the number of edges or faces changes, the names of the edges or faces of that object might change too.}}


{{term|Torus}}


{{defn|A primitive shape.}}


{{term|Tracker}}


{{defn|defn=Short for bug tracker, the online software application used to keep track of reported bugs or feature requests. See also [Mantis](#Mantis.md).}}


{{glossend}}


</div>

## U


<div class="mw-translate-fuzzy">

## U 


{{gloss}}


{{term|Union}}


{{defn|defn=A [Part](Part_Workbench.md) [workbench](#Workbench.md) tool that performs a [Boolean operation](#Boolean_Operation.md) on selected shapes.}}


{{term|1=Unstable}}


{{defn|1=A nickname for a very recent version of the FreeCAD software. This version will contain many changes recently implemented by the developers.  It does not typically fail or produce wrong results, but it has not completed testing.}}


{{term|Upgrade|content=[Upgrade](Draft_Upgrade.md)}}


{{defn|defn=A [Draft](Draft_Workbench.md) [workbench](#Workbench.md) tool.}}


{{glossend}}


</div>

## V


<div class="mw-translate-fuzzy">

## V 


{{gloss}}


{{term|Vector}}


{{defn|defn=O mărime cu direcție. Adesea reprezentat grafic ca o săgeată în 2 sau 3 dimensiuni. De exemplu, "fifty paces north", "9.8 m/s^2 down", și "(3,5,6) unități în direcția x, respectiv y, z" susnt toți vectori. În FreeCAD,ele sunt cele mai des desemnate ca perechi ordonate (x, y) sau triplete ordonate (x, y, z).}}


{{term|Vertex}}


{{defn|defn=A lone [point](#Point.md) în spațiu, sau colțul unei [shape](#shape.md) unde se întâlnesc [edges](#Edge.md). Tehnologia Open Cascade definește asta ca având cu dimensiunea zero [shape](#shape.md) corespunzător punctului din geometrie. [ vezi OCCT Profile: Defining the topology](https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3.md)}}


{{glossend}}


</div>

## W


<div class="mw-translate-fuzzy">

## W 


{{gloss}}


{{term|WB}}


{{defn|defn=Prescurtare pentru [workbench](#Workbench.md).}}


{{term|Wire}}


{{defn|no=1|O secvență conectată la [edges](#Edge.md) prin [vertices](#Vertex.md). Termenul fir(polilinie) este utilizat în acest sens, în principal prin tehnologia Open Cascade [[https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3]]and therefore also inside of FreeCAD.}}


{{defn|no=2|A [Draft](Draft_Workbench.md) [workbench](#Workbench.md) comandă pentru a crea un fir parametric.}}


{{term|Workbench}}


{{defn|defn=Numit și modul, fiecare Atelier [workbench](Workbenches.md) grupează un set de instrumente dedicate rezolvării unei sarcini specifice.}}


{{glossend}}


</div>

## X


<div class="mw-translate-fuzzy">

## X 


{{gloss}}


{{term|X}}


{{defn|De obicei se referă la axa cu același nume din spațiul 2D sau 3D X [axis](#Axis.md).}}


{{glossend}}


</div>

## Y


<div class="mw-translate-fuzzy">

## Y 


{{gloss}}


{{term|Y}}


{{defn|De obicei se referă la axa cu același nume din spațiul 2D sau 3D Y [axis](#Axis.md).}}


{{glossend}}


</div>

## Z


<div class="mw-translate-fuzzy">

## Z 


{{gloss}}


{{term|term=Z}}


{{defn|Se referă de obicei la axa Z [axis](#Axis.md).}}


{{glossend}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Wiki](Category_Wiki.md) > [Glossary](Category_Glossary.md) > Glossary/ro
