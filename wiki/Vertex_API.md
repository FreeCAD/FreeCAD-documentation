# Vertex API

TopoShapeVertex is the OpenCasCade topological vertex wrapper



#### <img src="images/BIM_Column.svg" style="width:16px;"> Area

Total area of the faces of the shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> BoundBox

Get the BoundBox of the object



#### <img src="images/BIM_Column.svg" style="width:16px;"> CenterOfGravity

Get the center of gravity



#### <img src="images/BIM_Column.svg" style="width:16px;"> CompSolids

List of subsequent shapes in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Compounds

List of compounds in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Content

Content of the object in XML representation.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Edges

List of Edges in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Faces

List of faces in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Length

Total length of the edges of the shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> MemSize

Memory size of the object in bytes.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Module

Module in which this class is defined



#### <img src="images/BIM_Column.svg" style="width:16px;"> Orientation

Returns the orientation of the shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Placement](Placement_API.md)

Get the current transformation of the object as placement



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Point](Point_API.md)

Position of this Vertex as a Vector



#### <img src="images/BIM_Column.svg" style="width:16px;"> ShapeType

Returns the type of the shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Shells

List of subsequent shapes in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Solids

List of subsequent shapes in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> SubShapes

List of sub-shapes in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Tag

Geometry Tag



#### <img src="images/BIM_Column.svg" style="width:16px;"> Tolerance

Set or get the tolerance of the vertex



#### <img src="images/BIM_Column.svg" style="width:16px;"> TypeId

Is the type of the FreeCAD object with module domain



#### <img src="images/BIM_Column.svg" style="width:16px;"> Vertexes

List of vertexes in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Volume

Total volume of the solids of the shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Wires

List of wires in this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> X

X component of this Vertex.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Y

Y component of this Vertex.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Z

Z component of this Vertex.



#### <img src="images/BIM_Column.svg" style="width:16px;"> ancestorsOfType

For a sub-shape of this shape get its ancestors of a type.
ancestorsOfType(shape, shape type) -> list



#### <img src="images/BIM_Column.svg" style="width:16px;"> applyRotation

Apply an additional rotation to the placement



#### <img src="images/BIM_Column.svg" style="width:16px;"> applyTranslation

Apply an additional translation to the placement



#### <img src="images/BIM_Column.svg" style="width:16px;"> check

Checks the shape and report errors in the shape structure.
check([runBopCheck = False])
--
This is a more detailed check as done in isValid().
if runBopCheck is True, a BOPCheck analysis is also performed.



#### <img src="images/BIM_Column.svg" style="width:16px;"> childShapes

Return a list of sub-shapes that are direct children of this shape.
childShapes([cumOri=True, cumLoc=True]) -> list
--
 * If cumOri is true, the function composes all
   sub-shapes with the orientation of this shape.
 * If cumLoc is true, the function multiplies all
   sub-shapes by the location of this shape, i.e. it applies to
   each sub-shape the transformation that is associated with this shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> cleaned

This creates a cleaned copy of the shape with the triangulation removed.
clean()
--
This can be useful to reduce file size when exporting as a BREP file.
Warning: Use the cleaned shape with care because certain algorithms may work incorrectly
if the shape has no internal triangulation any more.



#### <img src="images/BIM_Column.svg" style="width:16px;"> common

Intersection of this and a given (list of) topo shape.
common(tool) -> Shape
  or
common((tool1,tool2,...),[tolerance=0.0]) -> Shape
--
Supports:
- Fuzzy Boolean operations (global tolerance for a Boolean operation)
- Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
- Parallelization of Boolean Operations algorithm

OCC 6.9.0 or later is required.



#### <img src="images/BIM_Column.svg" style="width:16px;"> complement

Computes the complement of the orientation of this shape,
i.e. reverses the interior/exterior status of boundaries of this shape.
complement()



#### <img src="images/BIM_Column.svg" style="width:16px;"> copy

Create a copy of this shape
copy(copyGeom=True, copyMesh=False) -> Shape
--
If copyMesh is True, triangulation contained in original shape will be
copied along with geometry.
If copyGeom is False, only topological objects will be copied, while
geometry and triangulation will be shared with original shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> countElement

Returns the count of a type of element
countElement(type) -> int



#### <img src="images/BIM_Column.svg" style="width:16px;"> countSubElements

Return the number of elements of a type



#### <img src="images/BIM_Column.svg" style="width:16px;"> cut

Difference of this and a given (list of) topo shape
cut(tool) -> Shape
  or
cut((tool1,tool2,...),[tolerance=0.0]) -> Shape
--
Supports:
- Fuzzy Boolean operations (global tolerance for a Boolean operation)
- Support of multiple arguments for a single Boolean operation
- Parallelization of Boolean Operations algorithm

OCC 6.9.0 or later is required.



#### <img src="images/BIM_Column.svg" style="width:16px;"> defeaturing

Remove a feature defined by supplied faces and return a new shape.
defeaturing(shapeList) -> Shape
--
The parameter is a list of faces.



#### <img src="images/BIM_Column.svg" style="width:16px;"> distToShape

Find the minimum distance to another shape.
distToShape(shape) -> (dist, vectors, infos)
--
dist is the minimum distance, in mm (float value).

vectors is a list of pairs of App.Vector. Each pair corresponds to solution.
Example: [(App.Vector(2.0, -1.0, 2.0), App.Vector(2.0, 0.0, 2.0)),
(App.Vector(2.0, -1.0, 2.0), App.Vector(2.0, -1.0, 3.0))]
First vector is a point on self, second vector is a point on s.

infos contains additional info on the solutions. It is a list of tuples:
(topo1, index1, params1, topo2, index2, params2)

    topo1, topo2 are strings identifying type of BREP element: 'Vertex',
    'Edge', or 'Face'.

    index1, index2 are indexes of the elements (zero-based).

    params1, params2 are parameters of internal space of the elements. For
    vertices, params is None. For edges, params is one float, u. For faces,
    params is a tuple (u,v).



#### <img src="images/BIM_Column.svg" style="width:16px;"> dumpContent

dumpContent(Compression=3) -> bytearray

Dumps the content of the object, both the XML representation and the additional
data files required, into a byte representation.

Compression : int
    Set the data compression level in the range [0,9]. Set to 0 for no compression.



#### <img src="images/BIM_Column.svg" style="width:16px;"> dumpToString

Dump information about the shape to a string.
dumpToString() -> string



#### <img src="images/BIM_Column.svg" style="width:16px;"> exportBinary

Export the content of this shape in binary format to a file.
exportBinary(filename)



#### <img src="images/BIM_Column.svg" style="width:16px;"> exportBrep

Export the content of this shape to an BREP file.
exportBrep(filename)
--
BREP is an OpenCasCade native format.



#### <img src="images/BIM_Column.svg" style="width:16px;"> exportBrepToString

Export the content of this shape to a string in BREP format.
exportBrepToString() -> string
--
BREP is an OpenCasCade native format.



#### <img src="images/BIM_Column.svg" style="width:16px;"> exportIges

Export the content of this shape to an IGES file.
exportIges(filename)



#### <img src="images/BIM_Column.svg" style="width:16px;"> exportStep

Export the content of this shape to an STEP file.
exportStep(filename)



#### <img src="images/BIM_Column.svg" style="width:16px;"> exportStl

Export the content of this shape to an STL mesh file.
exportStl(filename)



#### <img src="images/BIM_Column.svg" style="width:16px;"> extrude

Extrude the shape along a vector.
extrude(vector) -> Shape
--
Shp2 = Shp1.extrude(App.Vector(0,0,10)) - extrude the shape 10 mm in the +Z direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> findPlane

return a plane if the shape is planar
findPlane(tol=None) -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> fix

Tries to fix a broken shape.
fix(working precision, minimum precision, maximum precision) -> bool
--
True is returned if the operation succeeded, False otherwise.



#### <img src="images/BIM_Column.svg" style="width:16px;"> fixTolerance

Sets (enforces) tolerances in a shape to the given value
fixTolerance(value, [ShapeType=Shape])
--
ShapeType = Vertex : only vertices are set
ShapeType = Edge   : only edges are set
ShapeType = Face   : only faces are set
ShapeType = Wire   : to have edges and their vertices set
ShapeType = other value : all (vertices,edges,faces) are set



#### <img src="images/BIM_Column.svg" style="width:16px;"> fuse

Union of this and a given (list of) topo shape.
fuse(tool) -> Shape
  or
fuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
--
Union of this and a given list of topo shapes.

Supports (OCCT 6.9.0 and above):
- Fuzzy Boolean operations (global tolerance for a Boolean operation)
- Support of multiple arguments for a single Boolean operation
- Parallelization of Boolean Operations algorithm

Beginning from OCCT 6.8.1 a tolerance value can be specified.



#### <img src="images/BIM_Column.svg" style="width:16px;"> generalFuse

Run general fuse algorithm (GFA) between this and given shapes.
generalFuse(list_of_other_shapes, [fuzzy_value = 0.0]) -> (result, map)
--
list_of_other_shapes: shapes to run the algorithm against (the list is
effectively prepended by 'self').

fuzzy_value: extra tolerance to apply when searching for interferences, in
addition to tolerances of the input shapes.

Returns a tuple of 2: (result, map).

result is a compound containing all the pieces generated by the algorithm
(e.g., for two spheres, the pieces are three touching solids). Pieces that
touch share elements.

map is a list of lists of shapes, providing the info on which children of
result came from which argument. The length of list is equal to length of
list_of_other_shapes + 1. First element is a list of pieces that came from
shape of this, and the rest are those that come from corresponding shapes in
list_of_other_shapes.
hint: use isSame method to test shape equality

Parallelization of Boolean Operations algorithm

OCC 6.9.0 or later is required.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getAllDerivedFrom

Returns all descendants



#### <img src="images/BIM_Column.svg" style="width:16px;"> getElement

Returns a SubElement
getElement(elementName) -> Face | Edge | Vertex



#### <img src="images/BIM_Column.svg" style="width:16px;"> getElementTypes

Return a list of element types



#### <img src="images/BIM_Column.svg" style="width:16px;"> getFaces

Return a tuple of points and triangles with a given accuracy



#### <img src="images/BIM_Column.svg" style="width:16px;"> getFacesFromSubElement

Return vertexes and faces from a sub-element



#### <img src="images/BIM_Column.svg" style="width:16px;"> getLines

Return a tuple of points and lines with a given accuracy



#### <img src="images/BIM_Column.svg" style="width:16px;"> getLinesFromSubElement

Return vertexes and lines from a sub-element



#### <img src="images/BIM_Column.svg" style="width:16px;"> getPoints

Return a tuple of points and normals with a given accuracy



#### <img src="images/BIM_Column.svg" style="width:16px;"> getTolerance

Determines a tolerance from the ones stored in a shape
getTolerance(mode, ShapeType=Shape) -> float
--
mode = 0 : returns the average value between sub-shapes,
mode > 0 : returns the maximal found,
mode < 0 : returns the minimal found.
ShapeType defines what kinds of sub-shapes to consider:
Shape (default) : all : Vertex, Edge, Face,
Vertex : only vertices,
Edge   : only edges,
Face   : only faces,
Shell  : combined Shell + Face, for each face (and containing
         shell), also checks edge and Vertex



#### <img src="images/BIM_Column.svg" style="width:16px;"> globalTolerance

Returns the computed tolerance according to the mode
globalTolerance(mode) -> float
--
mode = 0 : average
mode > 0 : maximal
mode < 0 : minimal



#### <img src="images/BIM_Column.svg" style="width:16px;"> hashCode

This value is computed from the value of the underlying shape reference and the location.
hashCode() -> int
--
Orientation is not taken into account.



#### <img src="images/BIM_Column.svg" style="width:16px;"> importBinary

Import the content to this shape of a string in BREP format.
importBinary(filename)



#### <img src="images/BIM_Column.svg" style="width:16px;"> importBrep

Load the shape from a file in BREP format.
importBrep(filename)



#### <img src="images/BIM_Column.svg" style="width:16px;"> importBrepFromString

Load the shape from a string that keeps the content in BREP format.
importBrepFromString(string, [displayProgressBar=True])
--
importBrepFromString(str,False) to not display a progress bar.



#### <img src="images/BIM_Column.svg" style="width:16px;"> inTolerance

Determines which shapes have a tolerance within a given interval
inTolerance(value, [ShapeType=Shape]) -> ShapeList
--
ShapeType is interpreted as in the method getTolerance



#### <img src="images/BIM_Column.svg" style="width:16px;"> isClosed

Checks if the shape is closed.
isClosed() -> bool
--
If the shape is a shell it returns True if it has no free boundaries (edges).
If the shape is a wire it returns True if it has no free ends (vertices).
(Internal and External sub-shepes are ignored in these checks)
If the shape is an edge it returns True if its vertices are the same.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isCoplanar

Checks if this shape is coplanar with the given shape.
isCoplanar(shape,tol=None) -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/BIM_Column.svg" style="width:16px;"> isEqual

Checks if both shapes are equal.
        This means geometry, placement and orientation are equal.
isEqual(shape) -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> isInfinite

Checks if this shape has an infinite expansion.
isInfinite() -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> isInside

Checks whether a point is inside or outside the shape.
isInside(point, tolerance, checkFace) => Boolean
--
checkFace indicates if the point lying directly on a face is considered to be inside or not



#### <img src="images/BIM_Column.svg" style="width:16px;"> isNull

Checks if the shape is null.
isNull() -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> isPartner

Checks if both shapes share the same geometry.
Placement and orientation may differ.
isPartner(shape) -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> isSame

Checks if both shapes share the same geometry
        and placement. Orientation may differ.
isSame(shape) -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> isValid

Checks if the shape is valid, i.e. neither null, nor empty nor corrupted.
isValid() -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> limitTolerance

Limits tolerances in a shape
limitTolerance(tmin, [tmax=0, ShapeType=Shape]) -> bool
--
tmin = tmax -> as fixTolerance (forces)
tmin = 0   -> maximum tolerance will be tmax
tmax = 0 or not given (more generally, tmax < tmin) ->
tmax ignored, minimum will be tmin
else, maximum will be max and minimum will be min
ShapeType = Vertex : only vertices are set
ShapeType = Edge   : only edges are set
ShapeType = Face   : only faces are set
ShapeType = Wire   : to have edges and their vertices set
ShapeType = other value : all (vertices,edges,faces) are set
Returns True if at least one tolerance of the sub-shape has been modified



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeChamfer

Make chamfer.
makeChamfer(radius,edgeList) -> Shape
or
makeChamfer(radius1,radius2,edgeList) -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeFillet

Make fillet.
makeFillet(radius,edgeList) -> Shape
or
makeFillet(radius1,radius2,edgeList) -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeOffset2D

makes an offset shape (2d offsetting).
makeOffset2D(offset, [join = 0, fill = False, openResult = false, intersection =
false]) -> Shape
--
The function supports keyword
arguments. Input shape (self) can be edge, wire, face, or a compound of those.

* offset: distance to expand the shape by. Negative value will shrink the
shape.

* join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
intersection

* fill: if true, the output is a face filling the space covered by offset. If
false, the output is a wire.

* openResult: affects the way open wires are processed. If False, an open wire
is made. If True, a closed wire is made from a double-sided offset, with rounds
around open vertices.

* intersection: affects the way compounds are processed. If False, all children
are offset independently. If True, and children are edges/wires, the children
are offset in a collective manner. If compounding is nested, collectiveness
does not spread across compounds (only direct children of a compound are taken
collectively).

Returns: result of offsetting (wire or face or compound of those). Compounding
structure follows that of source shape.



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeOffsetShape

makes an offset shape (3d offsetting).
makeOffsetShape(offset, tolerance, [inter = False, self_inter = False,
offsetMode = 0, join = 0, fill = False]) -> Shape
--
The function supports keyword arguments.

* offset: distance to expand the shape by. Negative value will shrink the
shape.

* tolerance: precision of approximation.

* inter: (parameter to OCC routine; not implemented)

* self_inter: (parameter to OCC routine; not implemented)

* offsetMode: 0 = skin; 1 = pipe; 2 = recto-verso

* join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
intersection

* fill: if true, offsetting a shell is to yield a solid

Returns: result of offsetting.



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeParallelProjection

Parallel projection of an edge or wire on this shape
makeParallelProjection(shape, dir) -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> makePerspectiveProjection

Perspective projection of an edge or wire on this shape
makePerspectiveProjection(shape, pnt) -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeShapeFromMesh

Make a compound shape out of mesh data.
makeShapeFromMesh((vertex,facets),tolerance) -> Shape
--
Note: This should be used for rather small meshes only.



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeThickness

Hollow a solid according to given thickness and faces.
makeThickness(List of faces, Offset (Float), Tolerance (Float)) -> Shape
--
A hollowed solid is built from an initial solid and a set of faces on this solid,
which are to be removed. The remaining faces of the solid become the walls of
the hollowed solid, their thickness defined at the time of construction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeWires

make wire(s) using the edges of this shape
makeWires([op=None])
--
The function will sort any edges inside the current shape, and connect them
into wire. If more than one wire is found, then it will make a compound out of
all found wires.

This function is element mapping aware. If the input shape has non-zero Tag,
it will map any edge and vertex element name inside the input shape into the
itself.

op: an optional string to be appended when auto generates element mapping.



#### <img src="images/BIM_Column.svg" style="width:16px;"> mirror

Mirror this shape on a given plane.
mirror(base, norm) -> Shape
--
The plane is given with its base point and its normal direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> multiFuse

Union of this and a given list of topo shapes.
multiFuse((tool1,tool2,...),[tolerance=0.0]) -> Shape
--
Supports (OCCT 6.9.0 and above):
- Fuzzy Boolean operations (global tolerance for a Boolean operation)
- Support of multiple arguments for a single Boolean operation
- Parallelization of Boolean Operations algorithm

Beginning from OCCT 6.8.1 a tolerance value can be specified.
Deprecated: use fuse() instead.



#### <img src="images/BIM_Column.svg" style="width:16px;"> nullify

Destroys the reference to the underlying shape stored in this shape.
As a result, this shape becomes null.
nullify()



#### <img src="images/BIM_Column.svg" style="width:16px;"> oldFuse

Union of this and a given topo shape (old algorithm).
oldFuse(tool) -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> optimalBoundingBox

Get the optimal bounding box
optimalBoundingBox([useTriangulation = True, useShapeTolerance = False]) -> bound box



#### <img src="images/BIM_Column.svg" style="width:16px;"> overTolerance

Determines which shapes have a tolerance over the given value
overTolerance(value, [ShapeType=Shape]) -> ShapeList
--
ShapeType is interpreted as in the method getTolerance



#### <img src="images/BIM_Column.svg" style="width:16px;"> project

Project a list of shapes on this shape
project(shapeList) -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> proximity

Returns two lists of Face indexes for the Faces involved in the intersection.
proximity(shape,[tolerance]) -> (selfFaces, shapeFaces)



#### <img src="images/BIM_Column.svg" style="width:16px;"> read

Read in an IGES, STEP or BREP file.
read(filename)



#### <img src="images/BIM_Column.svg" style="width:16px;"> reflectLines

Build projection or reflect lines of a shape according to a view direction.
reflectLines(ViewDir, [ViewPos, UpDir, EdgeType, Visible, OnShape]) -> Shape (Compound of edges)
--
This algorithm computes the projection of the shape in the ViewDir direction.
If OnShape is False(default), the returned edges are flat on the XY plane defined by
ViewPos(origin) and UpDir(up direction).
If OnShape is True, the returned edges are the corresponding 3D reflect lines located on the shape.
EdgeType is a string defining the type of result edges :
- IsoLine : isoparametric line
- OutLine : outline (silhouette) edge
- Rg1Line : smooth edge of G1-continuity between two surfaces
- RgNLine : sewn edge of CN-continuity on one surface
- Sharp : sharp edge (of C0-continuity)
If Visible is True (default), only visible edges are returned.
If Visible is False, only invisible edges are returned.



#### <img src="images/BIM_Column.svg" style="width:16px;"> removeInternalWires

Removes internal wires (also holes) from the shape.
removeInternalWires(minimalArea) -> bool



#### <img src="images/BIM_Column.svg" style="width:16px;"> removeShape

Remove a sub-shape and return a new shape.
removeShape(shapeList) -> Shape
--
The parameter is a list of shapes.



#### <img src="images/BIM_Column.svg" style="width:16px;"> removeSplitter

Removes redundant edges from the B-REP model
removeSplitter() -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> replaceShape

Replace a sub-shape with a new shape and return a new shape.
replaceShape(tupleList) -> Shape
--
The parameter is in the form list of tuples with the two shapes.



#### <img src="images/BIM_Column.svg" style="width:16px;"> restoreContent

restoreContent(obj) -> None

Restore the content of the object from a byte representation as stored by `dumpContent`.
It could be restored from any Python object implementing the buffer protocol.

obj : buffer
    Object with buffer protocol support.



#### <img src="images/BIM_Column.svg" style="width:16px;"> reverse

Reverses the orientation of this shape.
reverse()



#### <img src="images/BIM_Column.svg" style="width:16px;"> reversed

Reverses the orientation of a copy of this shape.
reversed() -> Shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> revolve

Revolve the shape around an Axis to a given degree.
revolve(base, direction, angle)
--
Part.revolve(App.Vector(0,0,0),App.Vector(0,0,1),360) - revolves the shape around the Z Axis 360 degree.

Hints: Sometimes you want to create a rotation body out of a closed edge or wire.
Example:
from FreeCAD import Base
import Part
V=Base.Vector

e=Part.Ellipse()
s=e.toShape()
r=s.revolve(V(0,0,0),V(0,1,0), 360)
Part.show(r)

However, you may possibly realize some rendering artifacts or that the mesh
creation seems to hang. This is because this way the surface is created twice.
Since the curve is a full ellipse it is sufficient to do a rotation of 180 degree
only, i.e. r=s.revolve(V(0,0,0),V(0,1,0), 180)

Now when rendering this object you may still see some artifacts at the poles. Now the
problem seems to be that the meshing algorithm doesn't like to rotate around a point
where there is no vertex.

The idea to fix this issue is that you create only half of the ellipse so that its shape
representation has vertexes at its start and end point.

from FreeCAD import Base
import Part
V=Base.Vector

e=Part.Ellipse()
s=e.toShape(e.LastParameter/4,3*e.LastParameter/4)
r=s.revolve(V(0,0,0),V(0,1,0), 360)
Part.show(r)



#### <img src="images/BIM_Column.svg" style="width:16px;"> rotate

Apply the rotation (base,dir,degree) to the current location of this shape
rotate(base,dir,degree)
--
Shp.rotate(App.Vector(0,0,0),App.Vector(0,0,1),180) - rotate the shape around the Z Axis 180 degrees.



#### <img src="images/BIM_Column.svg" style="width:16px;"> rotated

Create a new shape with rotation.
rotated(base,dir,degree) -> shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> scale

Apply scaling with point and factor to this shape.
scale(factor,[base=App.Vector(0,0,0)])



#### <img src="images/BIM_Column.svg" style="width:16px;"> scaled

Create a new shape with scale.
scaled(factor,[base=App.Vector(0,0,0)]) -> shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> section

Section of this with a given (list of) topo shape.
section(tool,[approximation=False]) -> Shape
  or
section((tool1,tool2,...),[tolerance=0.0, approximation=False]) -> Shape
--
If approximation is True, section edges are approximated to a C1-continuous BSpline curve.

Supports:
- Fuzzy Boolean operations (global tolerance for a Boolean operation)
- Support of multiple arguments for a single Boolean operation (s1 AND (s2 OR s3))
- Parallelization of Boolean Operations algorithm

OCC 6.9.0 or later is required.



#### <img src="images/BIM_Column.svg" style="width:16px;"> sewShape

Sew the shape if there is a gap.
sewShape()



#### <img src="images/BIM_Column.svg" style="width:16px;"> slice

Make single slice of this shape.
slice(direction, distance) --> Wires



#### <img src="images/BIM_Column.svg" style="width:16px;"> slices

Make slices of this shape.
slices(direction, distancesList) --> Wires



#### <img src="images/BIM_Column.svg" style="width:16px;"> tessellate

Tessellate the shape and return a list of vertices and face indices
tessellate() -> (vertex,facets)



#### <img src="images/BIM_Column.svg" style="width:16px;"> toNurbs

Conversion of the complete geometry of a shape into NURBS geometry.
toNurbs() -> Shape
--
For example, all curves supporting edges of the basis shape are converted
into B-spline curves, and all surfaces supporting its faces are converted
into B-spline surfaces.



#### <img src="images/BIM_Column.svg" style="width:16px;"> transformGeometry

Apply geometric transformation on this or a copy the shape.
transformGeometry(matrix) -> Shape
--
This method returns a new shape.
The transformation to be applied is defined as a 4x4 matrix.
The underlying geometry of the following shapes may change:
- a curve which supports an edge of the shape, or
- a surface which supports a face of the shape;

For example, a circle may be transformed into an ellipse when
applying an affinity transformation. It may also happen that
the circle then is represented as a B-spline curve.

The transformation is applied to:
- all the curves which support edges of the shape, and
- all the surfaces which support faces of the shape.

Note: If you want to transform a shape without changing the
underlying geometry then use the methods translate or rotate.



#### <img src="images/BIM_Column.svg" style="width:16px;"> transformShape

Apply transformation on a shape without changing the underlying geometry.
transformShape(Matrix,[boolean copy=False, checkScale=False]) -> None
--
If checkScale is True, it will use transformGeometry if non-uniform
scaling is detected.



#### <img src="images/BIM_Column.svg" style="width:16px;"> transformed

Create a new transformed shape
transformed(Matrix,copy=False,checkScale=False,op=None) -> shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> translate

Apply the translation to the current location of this shape.
translate(vector)



#### <img src="images/BIM_Column.svg" style="width:16px;"> translated

Create a new shape with translation
translated(vector) -> shape



#### <img src="images/BIM_Column.svg" style="width:16px;"> writeInventor

Write the mesh in OpenInventor format to a string.
writeInventor() -> string









---
![](images/Button_right.png) [documentation index](../README.md) > [API](Category_API.md) > Vertex API
