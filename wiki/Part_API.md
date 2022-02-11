# Part API

This is a module working with shapes.



#### <img src="images/Type_enum.svg" style="width:16px;"> [Arc](Arc_API.md)

Describes a portion of a curve



#### <img src="images/Type_enum.svg" style="width:16px;"> ArcOfCircle

Describes a portion of a circle



#### <img src="images/Type_enum.svg" style="width:16px;"> ArcOfConic

Describes a portion of a conic



#### <img src="images/Type_enum.svg" style="width:16px;"> ArcOfEllipse

Describes a portion of an ellipse



#### <img src="images/Type_enum.svg" style="width:16px;"> ArcOfHyperbola

Describes a portion of an hyperbola



#### <img src="images/Type_enum.svg" style="width:16px;"> ArcOfParabola

Describes a portion of an parabola



#### <img src="images/Type_enum.svg" style="width:16px;"> AttachEngine

AttachEngine abstract class - the functionality of AttachableObject, but outside of DocumentObject



#### <img src="images/type_module.svg" style="width:16px;"> BRepFeat

This is a module working with the BRepFeat package.



#### <img src="images/type_module.svg" style="width:16px;"> BRepOffsetAPI

This is a module working with the BRepOffsetAPI package.



#### <img src="images/Type_enum.svg" style="width:16px;"> [BSplineCurve](BSplineCurve_API.md)

Describes a B-Spline curve in 3D space



#### <img src="images/Type_enum.svg" style="width:16px;"> [BSplineSurface](BSplineSurface_API.md)

Describes a B-Spline surface in 3D space



#### <img src="images/Type_enum.svg" style="width:16px;"> [BezierCurve](BezierCurve_API.md)


				Describes a rational or non-rational Bezier curve:
				-- a non-rational Bezier curve is defined by a table of poles (also called control points)
				-- a rational Bezier curve is defined by a table of poles with varying weights

				Constructor takes no arguments.

				Example usage:
					p1 = Base.Vector(-1, 0, 0)
					p2 = Base.Vector(0, 1, 0.2)
					p3 = Base.Vector(1, 0, 0.4)
					p4 = Base.Vector(0, -1, 1)

					bc = BezierCurve()
					bc.setPoles([p1, p2, p3, p4])
					curveShape = bc.toShape()
			



#### <img src="images/Type_enum.svg" style="width:16px;"> BezierSurface

Describes a rational or non-rational Bezier surface
				-- A non-rational Bezier surface is defined by a table of poles (also known as control points).
				-- A rational Bezier surface is defined by a table of poles with varying associated weights.
			



#### <img src="images/Type_enum.svg" style="width:16px;"> BodyBase

Base class of all Body objects



#### <img src="images/Type_enum.svg" style="width:16px;"> [Circle](Circle_API.md)

Describes a circle in 3D space
To create a circle there are several ways:
Part.Circle()
    Creates a default circle with center (0,0,0) and radius 1

Part.Circle(Circle)
    Creates a copy of the given circle

Part.Circle(Circle, Distance)
    Creates a circle parallel to given circle at a certain distance

Part.Circle(Center,Normal,Radius)
    Creates a circle defined by center, normal direction and radius

Part.Circle(Point1,Point2,Point3)
    Creates a circle defined by three non-linear points
   



#### <img src="images/Type_enum.svg" style="width:16px;"> [CompSolid](CompSolid_API.md)

TopoShapeCompSolid is the OpenCasCade topological compound solid wrapper



#### <img src="images/Type_enum.svg" style="width:16px;"> [Compound](Compound_API.md)

Create a compound out of a list of shapes



#### <img src="images/Type_enum.svg" style="width:16px;"> [Cone](Cone_API.md)

Describes a cone in 3D space
				To create a cone there are several ways:
				Part.Cone()
				    Creates a default cone with radius 1

				Part.Cone(Cone)
				    Creates a copy of the given cone

				Part.Cone(Cone, Distance)
				    Creates a cone parallel to given cone at a certain distance

				Part.Cone(Point1,Point2,Radius1,Radius2)
				    Creates a cone defined by two points and two radii
				    The axis of the cone is the line passing through
				    Point1 and Poin2.
				    Radius1 is the radius of the section passing through
				    Point1 and Radius2 the radius of the section passing
				    through Point2.

				Part.Cone(Point1,Point2,Point3,Point4)
				    Creates a cone passing through three points Point1,
				    Point2 and Point3.
				    Its axis is defined by Point1 and Point2 and the radius of
				    its base is the distance between Point3 and its axis.
				    The distance between Point and the axis is the radius of
				    the section passing through Point4.
			



#### <img src="images/Type_enum.svg" style="width:16px;"> Conic

Describes an abstract conic in 3d space



#### <img src="images/Type_enum.svg" style="width:16px;"> [Cylinder](Cylinder_API.md)

Describes a cylinder in 3D space
				To create a cylinder there are several ways:
				Part.Cylinder()
					Creates a default cylinder with center (0,0,0) and radius 1

				Part.Cylinder(Cylinder)
					Creates a copy of the given cylinder

				Part.Cylinder(Cylinder, Distance)
					Creates a cylinder parallel to given cylinder at a certain distance

				Part.Cylinder(Point1,Point2,Point2)
					Creates a cylinder defined by three non-linear points

				Part.Cylinder(Circle)
					Creates a cylinder by a circular base
			



#### <img src="images/Type_enum.svg" style="width:16px;"> [Edge](Edge_API.md)

TopoShapeEdge is the OpenCasCade topological edge wrapper



#### <img src="images/Type_enum.svg" style="width:16px;"> [Ellipse](Ellipse_API.md)

Describes an ellipse in 3D space
				To create an ellipse there are several ways:
				Part.Ellipse()
					Creates an ellipse with major radius 2 and minor radius 1 with the
					center in (0,0,0)

				Part.Ellipse(Ellipse)
					Create a copy of the given ellipse

				Part.Ellipse(S1,S2,Center)
					Creates an ellipse centered on the point Center, where
					the plane of the ellipse is defined by Center, S1 and S2,
					its major axis is defined by Center and S1,
					its major radius is the distance between Center and S1, and
					its minor radius is the distance between S2 and the major axis.

				Part.Ellipse(Center,MajorRadius,MinorRadius)
					Creates an ellipse with major and minor radii MajorRadius and
					MinorRadius, and located in the plane defined by Center and
					the normal (0,0,1)
			



#### <img src="images/Type_enum.svg" style="width:16px;"> [Face](Face_API.md)

TopoShapeFace is the OpenCasCade topological face wrapper



#### <img src="images/Type_enum.svg" style="width:16px;"> Feature

This is the father of all shape object classes



#### <img src="images/type_module.svg" style="width:16px;"> Geom2d

This is a module working with 2d geometries.



#### <img src="images/type_module.svg" style="width:16px;"> GeomPlate

This is a module working with the GeomPlate framework.



#### <img src="images/Type_enum.svg" style="width:16px;"> GeometryBoolExtension

A GeometryExtension extending geometry objects with a boolean.



#### <img src="images/Type_enum.svg" style="width:16px;"> GeometryDoubleExtension

A GeometryExtension extending geometry objects with a double.



#### <img src="images/Type_enum.svg" style="width:16px;"> GeometryIntExtension

A GeometryExtension extending geometry objects with an int.



#### <img src="images/Type_enum.svg" style="width:16px;"> GeometryStringExtension

A GeometryExtension extending geometry objects with a string.



#### <img src="images/type_module.svg" style="width:16px;"> HLRBRep

This is a module working with the HLRBRep framework.



#### <img src="images/Type_enum.svg" style="width:16px;"> Hyperbola

Describes an hyperbola in 3D space
				To create a hyperbola there are several ways:
				Part.Hyperbola()
					Creates an hyperbola with major radius 2 and minor radius 1 with the
					center in (0,0,0)

				Part.Hyperbola(Hyperbola)
					Create a copy of the given hyperbola

				Part.Hyperbola(S1,S2,Center)
					Creates an hyperbola centered on the point Center, where
					the plane of the hyperbola is defined by Center, S1 and S2,
					its major axis is defined by Center and S1,
					its major radius is the distance between Center and S1, and
					its minor radius is the distance between S2 and the major axis.

				Part.Hyperbola(Center,MajorRadius,MinorRadius)
					Creates an hyperbola with major and minor radii MajorRadius and
					MinorRadius, and located in the plane defined by Center and
					the normal (0,0,1)
			



#### <img src="images/Type_enum.svg" style="width:16px;"> [Line](Line_API.md)

Describes an infinite line
To create a line there are several ways:
Part.Line()
    Creates a default line

Part.Line(Line)
    Creates a copy of the given line

Part.Line(Point1,Point2)
    Creates a line that goes through two given points



#### <img src="images/Type_enum.svg" style="width:16px;"> LineSegment

Describes a line segment
To create a line segment there are several ways:
Part.LineSegment()
    Creates a default line segment

Part.LineSegment(LineSegment)
    Creates a copy of the given line segment

Part.LineSegment(Point1,Point2)
    Creates a line segment that goes through two given points



#### <img src="images/Type_enum.svg" style="width:16px;"> OCCConstructionError





#### <img src="images/Type_enum.svg" style="width:16px;"> OCCDimensionError





#### <img src="images/Type_enum.svg" style="width:16px;"> OCCDomainError





#### <img src="images/Type_enum.svg" style="width:16px;"> OCCError





#### <img src="images/Type_enum.svg" style="width:16px;"> OCCRangeError





#### <img src="images/Type_enum.svg" style="width:16px;"> OCC_VERSION

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> OffsetCurve





#### <img src="images/Type_enum.svg" style="width:16px;"> OffsetSurface





#### <img src="images/Type_enum.svg" style="width:16px;"> Parabola

Describes a parabola in 3D space



#### <img src="images/Type_enum.svg" style="width:16px;"> Part2DObject

This object represents a 2D Shape in a 3D World



#### <img src="images/Type_enum.svg" style="width:16px;"> Plane

Describes an infinite plane
To create a plane there are several ways:
Part.Plane()
    Creates a default plane with base (0,0,0) and normal (0,0,1)

Part.Plane(Plane)
    Creates a copy of the given plane

Part.Plane(Plane, Distance)
    Creates a plane parallel to given plane at a certain distance

Part.Plane(Location,Normal)
    Creates a plane with a given location and normal

Part.Plane(Point1,Point2,Point3)
    Creates a plane defined by three non-linear points

Part.Plane(A,B,C,D)
    Creates a plane from its cartesian equation
    Ax+By+Cz+D=0




#### <img src="images/Type_enum.svg" style="width:16px;"> PlateSurface





#### <img src="images/Type_enum.svg" style="width:16px;"> [Point](Point_API.md)

Describes a point
To create a point there are several ways:
Part.Point()
    Creates a default point

Part.Point(Point)
    Creates a copy of the given point

Part.Point(Vector)
    Creates a line for the given coordinates



#### <img src="images/Type_enum.svg" style="width:16px;"> Precision

This is the Type class



#### <img src="images/Type_enum.svg" style="width:16px;"> RectangularTrimmedSurface

Describes a portion of a surface (a patch) limited by two values of the
u parameter in the u parametric direction, and two values of the v parameter in the v parametric
direction. The domain of the trimmed surface must be within the domain of the surface being trimmed.

The trimmed surface is defined by:
- the basis surface, and
- the values (umin, umax) and (vmin, vmax) which limit it in the u and v parametric directions.

The trimmed surface is built from a copy of the basis surface. Therefore, when the basis surface
is modified the trimmed surface is not changed. Consequently, the trimmed surface does not
necessarily have the same orientation as the basis surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> [Shape](Shape_API.md)

TopoShape is the OpenCasCade topological shape wrapper.
Sub-elements such as vertices, edges or faces are accessible as:
* Vertex#, where # is in range(1, number of vertices)
* Edge#, where # is in range(1, number of edges)
* Face#, where # is in range(1, number of faces)



#### <img src="images/type_module.svg" style="width:16px;"> ShapeUpgrade

This is a module working with the ShapeUpgrade framework.



#### <img src="images/Type_enum.svg" style="width:16px;"> [Shell](Shell_API.md)

Create a shell out of a list of faces



#### <img src="images/Type_enum.svg" style="width:16px;"> [Solid](Solid_API.md)

Part.Solid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created.



#### <img src="images/Type_enum.svg" style="width:16px;"> [Sphere](Sphere_API.md)

Describes a sphere in 3D space



#### <img src="images/Type_enum.svg" style="width:16px;"> SurfaceOfExtrusion

Describes a surface of linear extrusion



#### <img src="images/Type_enum.svg" style="width:16px;"> SurfaceOfRevolution

Describes a surface of revolution



#### <img src="images/Type_enum.svg" style="width:16px;"> Toroid

Describes a toroid in 3D space



#### <img src="images/Type_enum.svg" style="width:16px;"> [Vertex](Vertex_API.md)

TopoShapeVertex is the OpenCasCade topological vertex wrapper



#### <img src="images/Type_enum.svg" style="width:16px;"> [Wire](Wire_API.md)

TopoShapeWire is the OpenCasCade topological wire wrapper



#### <img src="images/type_method.svg" style="width:16px;"> cast_to_shape

cast_to_shape(shape) -- Cast to the actual shape type



#### <img src="images/type_method.svg" style="width:16px;"> clearShapeCache

clearShapeCache() -- Clears internal shape cache



#### <img src="images/type_method.svg" style="width:16px;"> export

export(list,string) -- Export a list of objects into a single file.



#### <img src="images/type_method.svg" style="width:16px;"> exportUnits

exportUnits([string=MM|M|INCH|FT|MI|KM|MIL|UM|CM|UIN]) -- Set units for exporting STEP/IGES files and returns the units.



#### <img src="images/type_method.svg" style="width:16px;"> getFacets

getFacets(shape): simplified mesh generation



#### <img src="images/type_method.svg" style="width:16px;"> getShape

getShape(obj,subname=None,mat=None,needSubElement=False,transform=True,retType=0):
Obtain the the TopoShape of a given object with SubName reference

* obj: the input object
* subname: dot separated sub-object reference
* mat: the current transformation matrix
* needSubElement: if False, ignore the sub-element (e.g. Face1, Edge1) reference in 'subname'
* transform: if False, then skip obj's transformation. Use this if mat already include obj's
             transformation matrix
* retType: 0: return TopoShape,
           1: return (shape,subObj,mat), where subObj is the object referenced in 'subname',
              and 'mat' is the accumulated transformation matrix of that sub-object.
           2: same as 1, but make sure 'subObj' is resolved if it is a link.
* refine: refine the returned shape



#### <img src="images/type_method.svg" style="width:16px;"> getSortedClusters

getSortedClusters(list of edges) -- Helper method to sort and cluster a variety of edges



#### <img src="images/type_method.svg" style="width:16px;"> insert

insert(string,string) -- Insert the file into the given document.



#### <img src="images/type_method.svg" style="width:16px;"> joinSubname

joinSubname(sub,mapped,subElement) -> subname




#### <img src="images/type_method.svg" style="width:16px;"> makeBox

makeBox(length,width,height,[pnt,dir]) -- Make a box located
in pnt with the dimensions (length,width,height)
By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)



#### <img src="images/type_method.svg" style="width:16px;"> makeCircle

makeCircle(radius,[pnt,dir,angle1,angle2]) -- Make a circle with a given radius
By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0 and angle2=360



#### <img src="images/type_method.svg" style="width:16px;"> makeCompound

makeCompound(list) -- Create a compound out of a list of shapes.



#### <img src="images/type_method.svg" style="width:16px;"> makeCone

makeCone(radius1,radius2,height,[pnt,dir,angle]) -- Make a cone with given radii and height
By default pnt=Vector(0,0,0), dir=Vector(0,0,1) and angle=360



#### <img src="images/type_method.svg" style="width:16px;"> makeCylinder

makeCylinder(radius,height,[pnt,dir,angle]) -- Make a cylinder with a given radius and height
By default pnt=Vector(0,0,0),dir=Vector(0,0,1) and angle=360



#### <img src="images/type_method.svg" style="width:16px;"> makeFace

makeFace(list_of_shapes_or_compound, maker_class_name) -- Create a face (faces) using facemaker class.
maker_class_name is a string like 'Part::FaceMakerSimple'.



#### <img src="images/type_method.svg" style="width:16px;"> makeFilledFace

makeFilledFace(list) -- Create a face out of a list of edges.



#### <img src="images/type_method.svg" style="width:16px;"> makeHelix

makeHelix(pitch,height,radius,[angle]) -- Make a helix with a given pitch, height and radius
By default a cylindrical surface is used to create the helix. If the fourth parameter is set
(the apex given in degree) a conical surface is used instead



#### <img src="images/type_method.svg" style="width:16px;"> makeLine

makeLine(startpnt,endpnt) -- Make a line between two points

Args:
    startpnt (Vector or tuple): Vector or 3 element tuple 
        containing the x,y and z coordinates of the start point,
        i.e. (x1,y1,z1).
    endpnt (Vector or tuple): Vector or 3 element tuple 
        containing the x,y and z coordinates of the start point,
        i.e. (x1,y1,z1).

Returns:
    Edge: Part.Edge object




#### <img src="images/type_method.svg" style="width:16px;"> makeLoft

makeLoft(list of wires,[solid=False,ruled=False,closed=False,maxDegree=5]) -- Create a loft shape.



#### <img src="images/type_method.svg" style="width:16px;"> makeLongHelix

makeLongHelix(pitch,height,radius,[angle],[hand]) -- Make a (multi-edge) helix with a given pitch, height and radius
By default a cylindrical surface is used to create the helix. If the fourth parameter is set
(the apex given in degree) a conical surface is used instead.



#### <img src="images/type_method.svg" style="width:16px;"> makePlane

makePlane(length,width,[pnt,dirZ,dirX]) -- Make a plane
By default pnt=Vector(0,0,0) and dirZ=Vector(0,0,1), dirX is ignored in this case



#### <img src="images/type_method.svg" style="width:16px;"> makePolygon

makePolygon(pntslist) -- Make a polygon from a list of points

Args:
    pntslist (list(Vector)): list of Vectors representing the 
        points of the polygon.

Returns:
    Wire: Part.Wire object. If the last point in the list is 
        not the same as the first point, the Wire will not be 
        closed and cannot be used to create a face.




#### <img src="images/type_method.svg" style="width:16px;"> makeRevolution

makeRevolution(Curve or Edge,[vmin,vmax,angle,pnt,dir,shapetype]) -- Make a revolved shape
by rotating the curve or a portion of it around an axis given by (pnt,dir).
By default vmin/vmax=bounds of the curve, angle=360, pnt=Vector(0,0,0),
dir=Vector(0,0,1) and shapetype=Part.Solid



#### <img src="images/type_method.svg" style="width:16px;"> makeRuledSurface

makeRuledSurface(Edge|Wire,Edge|Wire) -- Make a ruled surface
Create a ruled surface out of two edges or wires. If wires are used thenthese must have the same number of edges.



#### <img src="images/type_method.svg" style="width:16px;"> makeShell

makeShell(list) -- Create a shell out of a list of faces.



#### <img src="images/type_method.svg" style="width:16px;"> makeShellFromWires

makeShellFromWires(Wires) -- Make a shell from wires.
The wires must have the same number of edges.



#### <img src="images/type_method.svg" style="width:16px;"> makeSolid

makeSolid(shape): Create a solid out of shells of shape. If shape is a compsolid, the overall volume solid is created.



#### <img src="images/type_method.svg" style="width:16px;"> makeSphere

makeSphere(radius,[pnt, dir, angle1,angle2,angle3]) -- Make a sphere with a given radius
By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=90 and angle3=360



#### <img src="images/type_method.svg" style="width:16px;"> makeSplitShape

makeSplitShape(shape, list of shape pairs,[check Interior=True]) -> two lists of shapes.
The following shape pairs are supported:
* Wire, Face
* Edge, Face
* Compound, Face
* Edge, Edge
* The face must be part of the specified shape and the edge, wire or compound must
lie on the face.
Output:
The first list contains the faces that are the left of the projected wires.
The second list contains the left part on the shape.

Example:
face = ...
edges = ...
split = [(edges[0],face),(edges[1],face)]
r = Part.makeSplitShape(face, split)
Part.show(r[0][0])
Part.show(r[1][0])




#### <img src="images/type_method.svg" style="width:16px;"> makeSweepSurface

makeSweepSurface(edge(path),edge(profile),[float]) -- Create a profile along a path.



#### <img src="images/type_method.svg" style="width:16px;"> makeThread

makeThread(pitch,depth,height,radius) -- Make a thread with a given pitch, depth, height and radius



#### <img src="images/type_method.svg" style="width:16px;"> makeTorus

makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) -- Make a torus with a given radii and angles
By default pnt=Vector(0,0,0),dir=Vector(0,0,1),angle1=0,angle1=360 and angle=360



#### <img src="images/type_method.svg" style="width:16px;"> makeTube

makeTube(edge,radius,[continuity,max degree,max segments]) -- Create a tube.
continuity is a string which must be 'C0','C1','C2','C3','CN','G1' or 'G1',



#### <img src="images/type_method.svg" style="width:16px;"> makeWedge

makeWedge(xmin, ymin, zmin, z2min, x2min,
xmax, ymax, zmax, z2max, x2max,[pnt,dir])
 -- Make a wedge located in pnt
By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)



#### <img src="images/type_method.svg" style="width:16px;"> makeWireString

makeWireString(string,fontdir,fontfile,height,[track]) -- Make list of wires in the form of a string's characters.



#### <img src="images/type_method.svg" style="width:16px;"> open

open(string) -- Create a new document and load the file into the document.



#### <img src="images/type_method.svg" style="width:16px;"> read

read(string) -- Load the file and return the shape.



#### <img src="images/type_method.svg" style="width:16px;"> setStaticValue

setStaticValue(string,string|int|float) -- Set a name to a value The value can be a string, int or float.



#### <img src="images/type_method.svg" style="width:16px;"> show

show(shape,[string]) -- Add the shape to the active document or create one if no document exists.



#### <img src="images/type_method.svg" style="width:16px;"> sortEdges

sortEdges(list of edges) -- list of lists of edges
It does basically the same as __sortEdges__ but sorts all input edges and thus returns
a list of lists of edges



#### <img src="images/type_method.svg" style="width:16px;"> splitSubname

splitSubname(subname) -> list(sub,mapped,subElement)
Split the given subname into a list

sub: subname without any sub-element reference
mapped: mapped element name, or '' if none
subElement: old style element name, or '' if none









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Part](Part_Workbench.md) > Part API
