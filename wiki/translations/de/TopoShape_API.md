# TopoShape API/de
**(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation].**

The TopoShape is the mother object of the Part Module. All shape types (wire, face, solid, etc\...) of the Part module are TopoShapes, and share the following attributes and methods. Example: 
```python
import Part
sh = Part.makeBox(10,10,10)
print sh.Faces
for f in sh.Faces:
   print f.Edges
```


{{APIProperty|Area|The total area of the faces of the shape.}}


{{APIProperty|BoundBox|The BoundBox of the object}}


{{APIProperty|CenterOfMass|The center of mass of the current system. If the gravitational field is uniform, it is the center of gravity. The coordinates returned for the center of mass are expressed in the absolute Cartesian coordinate system.}}


{{APIProperty|CompSolids|Lists the subsequent shapes in this shape.}}


{{APIProperty|Compounds|Lists the coumpounds in this shape.}}


{{APIProperty|Edges|Lists the Edges in this shape.}}


{{APIProperty|Faces|Lists the faces in this shape.}}


{{APIProperty|Length|Total length of the edges of the shape.}}


{{APIProperty|Matrix|The current transformation of the object as matrix}}


{{APIProperty|Orientation|the orientation of the shape.}}


{{APIProperty|Placement|The current transformation of the object as placement}}


{{APIProperty|ShapeType|The type of the shape.}}


{{APIProperty|Shells|Lists the subsequent shapes in this shape.}}


{{APIProperty|Solids|List of subsequent shapes in this shape.}}


{{APIProperty|Vertexes|List of vertexes in this shape.}}


{{APIProperty|Volume|Total volume of the solids of the shape.}}


{{APIProperty|Wires|List of wires in this shape.}}


{{APIFunction|approximate| |Approximates a B-Spline-curve from this wire|a BSplineCurve object}}


{{APIFunction|check| |Checks the shape and report errors in the shape structure. This is a more detailed check as done in isValid().| }}


{{APIFunction|common|TopoShape|Intersection of this and a given topo shape.|a TopoShape}}


{{APIFunction|complement| |Computes the complement of the orientation of this shape, i.e. reverses the interior/exterior status of boundaries of this shape.|a TopoShape}}


{{APIFunction|copy| |Creates a copy of this shape|a TopoShape}}


{{APIFunction|cut|TopoShape|Difference of this and a given topo shape.|a TopoShape}}


{{APIFunction|distToShape| TopoShape |Calculates the minimum distance between this and a given TopoShape.|float<minimum distance>,list<nearest points>,list<nearest subshapes & parameters> }}


{{APIFunction|exportBrep| string |Exports the content of this shape to an BREP file. BREP is a CasCade native format.| }}


{{APIFunction|exportIges| string |Exports the content of this shape to an IGES file.| }}


{{APIFunction|exportStep| string |Exports the content of this shape to an STEP file.| }}


{{APIFunction|exportStl| string |Exports the content of this shape to an STL mesh file.| }}


{{APIFunction|extrude|Vector|Extrudes the shape along a direction.|a TopoShape}}


{{APIFunction|fuse|TopoShape|Union of this and a given topo shape.|a TopoShape}}


{{APIFunction|getAllDerivedFrom| |Returns all descentences of this object type|a list}}


{{APIFunction|hashCode| |This value is computed from the value of the underlying shape reference and the location. Orientation is not taken into account.|a string}}


{{APIFunction|isClosed| |Checks if the shape is closed.|a boolean}}


{{APIFunction|isDerivedFrom|string|Returns true if given type is a father|boolean}}


{{APIFunction|isEqual|TopoShape|Returns true if both shapes share the same TShape, have the same Location and have the same Orientation.|a boolean}}


{{APIFunction|isInside|Vector,float,Boolean|Checks if a point is inside a solid with a certain tolerance. If the 3rd parameter is True a point on a face is considered as inside|a boolean}}


{{APIFunction|isNull| |Checks if the shape is null.|a boolean}}


{{APIFunction|isPartner|TopoShape|Returns true if both shapes share the same TShape, but may have a different Location and may have a different Orientation.|a boolean}}


{{APIFunction|isSame|TopoShape|Checks if both shapes share the same geometry, true if both shapes share the same TShape, have the same Location but may have a different Orientation.|a boolean}}


{{APIFunction|isValid| |Checks if the shape is valid, i.e. neither null, nor empty nor corrupted.|a boolean}}


{{APIFunction|makeFillet|float,TopoShape|Returns a new object based on TopoShape, but with a fillet of radius 'float' applied to each edge.|a TopoShape}}


{{APIFunction|makeHomogenousWires|wire|Makes this and the given wire homogenous to have the same number of edges| a wire}}


{{APIFunction|makeOffset|float|Offsets the shape by a given ammount|a TopoShape}}


{{APIFunction|makePipe|wire|Makes a pipe by sweeping along a wire.|a TopoShape}}


{{APIFunction|makePipeShell|wire|Makes a loft defined by profiles along a wire.|a TopoShape}}


{{APIFunction|makeShapeFromMesh|mesh|Makes a compound shape out of mesh data. Note: This should be used for rather small meshes only.|a TopoShape}}


{{APIFunction|makeThickness|list,float,float|A hollowed solid is built from an initial solid and a set of faces on this solid, which are to be removed. The remaining faces of the solid become the walls of the hollowed solid, their thickness defined at the time of construction. The arguments to be passed are a list of faces to be skipped, the thickness of the walls and a tolerance value.|a TopoShape}}


{{APIFunction|nullify| |Destroys the reference to the underlying shape stored in this shape. As a result, this shape becomes null.|}}


{{APIFunction|project|TopoShape|Project a shape on this shape|a TopoShape}}


{{APIFunction|read|string|Reads in an IGES, STEP or BREP file.|a TopoShape}}


{{APIFunction|reverse| |Reverses the orientation of this shape.| }}


{{APIFunction|revolve|Vector, Vector, float|Revolves the shape around a Axis to a given degree. ex: Part.revolve(Vector(0,0,0),Vector(0,0,1),360) revolves the shape around the Z Axis 360 degree.|a TopoShape}}


{{APIFunction|rotate|Vector<position>, Vector<direction>, float<angle>|Rotates this shape by angle degrees around an axis specified by position and direction. ex: Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) rotate the shape around the Z Axis 180 degrees.| }}


{{APIFunction|scale|float<factor>, [Vector<centre>]|Uniformly scales this shape by factor. Optionally specify centre of scaling transformation.| }}


{{APIFunction|section|TopoShape|Section of this with a given topo shape.|a TopoShape}}


{{APIFunction|sewShape| |Sews the shape if there is a gap.| }}


{{APIFunction|tessellate|float|Tessellate the the shape and return a list of vertices and face indices. The given float is the tolerance.|a list}}


{{APIFunction|toNurbs| |Conversion of the complete geometry of a shape into NURBS geometry. For example, all curves supporting edges of the basis shape are converted into BSpline curves, and all surfaces supporting its faces are converted into BSpline surfaces.|a NURBS curve}}


{{APIFunction|transformGeometry|matrix|Applies geometric transformation on a copy of the shape. The transformation to be applied is defined as a 4x4 matrix. The underlying geometry of the following shapes may change to a curve which supports an edge of the shape, or a surface which supports a face of the shape. For example, a circle may be transformed into an ellipse when applying an affinity transformation. It may also happen that the circle then is represented as a b-spline curve. The transformation is applied to all the curves which support edges of the shape, and all the surfaces which support faces of the shape. Note: If you want to transform a shape without changing the underlying geometry then use the methods translate or rotate.|a TopoShape}}


{{APIFunction|transformShape|matrix|Applies transformation on a shape without changing the underlying geometry.| }}


{{APIFunction|translate|Vector|Applies the translation to the current location of this shape.| }}


{{APIFunction|writeInventor| |Writes the mesh in OpenInventor format to a string.|a string}}

Some attributes and methods apply only to certain TopoShapes. These items apply to Edges (TopoShapeEdge).


{{APIProperty|FirstParameter|The parameter value at one end of the Edge. Not necessarily at Vertex[0]. [http://en.wikipedia.org/wiki/Parametric_equations See Parametric Equations]}}


{{APIProperty|LastParameter|The parameter value at the other end of the Edge. Not necessarily at Vertex[1].}}


{{APIFunction|getParameterByLength|Float|Maps the interval [0,Length] to the interval [FirstParameter,LastParameter]|Float }}


{{APIFunction|valueAt|Float|Returns the 3D vector corresponding to a parameter value.|Vector}}


{{APIFunction|parameterAt|Vertex,[Face]|Returns the parameter value corresponding to a Vertex (3D point).|Float}}


{{APIFunction|tangentAt|Float|Returns the direction vector of the tangent to the edge at a parameter value (if it exists).|Vector}}


{{APIFunction|normalAt|Float|Returns the direction vector of the normal to the edge at a parameter value (if it exists uniquely).|Vector}}


{{APIFunction|curvatureAt|Float|Returns the curvature of the edge at a parameter value.|Float}}


{{APIFunction|centerOfCurvatureAt|Float|Returns the center (3D point) of the osculating circle at a parameter value.|Vector}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > TopoShape API/de
