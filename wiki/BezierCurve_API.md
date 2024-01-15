# BezierCurve API

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



#### <img src="images/BIM_Column.svg" style="width:16px;"> Content

Content of the object in XML representation.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Continuity

Returns the global continuity of the curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Degree

Returns the polynomial degree of this Bezier curve,
which is equal to the number of poles minus 1.



#### <img src="images/BIM_Column.svg" style="width:16px;"> EndPoint

Returns the end point of this Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> FirstParameter

Returns the value of the first parameter.



#### <img src="images/BIM_Column.svg" style="width:16px;"> LastParameter

Returns the value of the last parameter.



#### <img src="images/BIM_Column.svg" style="width:16px;"> MaxDegree

Returns the value of the maximum polynomial degree of any
Bezier curve curve. This value is 25.



#### <img src="images/BIM_Column.svg" style="width:16px;"> MemSize

Memory size of the object in bytes.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Module

Module in which this class is defined



#### <img src="images/BIM_Column.svg" style="width:16px;"> NbPoles

Returns the number of poles of this Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Rotation

Returns a rotation object to describe the orientation for curve that supports it



#### <img src="images/BIM_Column.svg" style="width:16px;"> StartPoint

Returns the start point of this Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Tag

Gives the tag of the geometry as string.



#### <img src="images/BIM_Column.svg" style="width:16px;"> TypeId

Is the type of the FreeCAD object with module domain



#### <img src="images/BIM_Column.svg" style="width:16px;"> approximateBSpline

Approximates a curve of any type to a B-Spline curve
                    approximateBSpline(Tolerance, MaxSegments, MaxDegree, [Order='C2']) -> B-Spline curve



#### <img src="images/BIM_Column.svg" style="width:16px;"> centerOfCurvature

Vector = centerOfCurvature(float pos) - Get the center of curvature at the given parameter [First|Last] if defined



#### <img src="images/BIM_Column.svg" style="width:16px;"> clone

Create a clone of this geometry with the same Tag



#### <img src="images/BIM_Column.svg" style="width:16px;"> continuityWith

Computes the continuity of two curves



#### <img src="images/BIM_Column.svg" style="width:16px;"> copy

Create a copy of this geometry



#### <img src="images/BIM_Column.svg" style="width:16px;"> curvature

Float = curvature(pos) - Get the curvature at the given parameter [First|Last] if defined



#### <img src="images/BIM_Column.svg" style="width:16px;"> deleteExtensionOfName

Deletes all extensions of the indicated name.



#### <img src="images/BIM_Column.svg" style="width:16px;"> deleteExtensionOfType

Deletes all extensions of the indicated type.



#### <img src="images/BIM_Column.svg" style="width:16px;"> discretize

Discretizes the curve and returns a list of points.
The function accepts keywords as argument:
discretize(Number=n) => gives a list of 'n' equidistant points
discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
discretize(Distance=d) => gives a list of equidistant points with distance 'd'
discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the curve
discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the curve (faster)
discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
                                    and a curvature deflection of 'c'. Optionally a minimum number of points
                                    can be set which by default is set to 2.

Optionally you can set the keywords 'First' and 'Last' to define a sub-range of the parameter range
of the curve.

If no keyword is given then it depends on whether the argument is an int or float.
If it's an int then the behaviour is as if using the keyword 'Number', if it's float
then the behaviour is as if using the keyword 'Distance'.

Example:

import Part
c=Part.Circle()
c.Radius=5
p=c.discretize(Number=50,First=3.14)
s=Part.Compound([Part.Vertex(i) for i in p])
Part.show(s)


p=c.discretize(Angular=0.09,Curvature=0.01,Last=3.14,Minimum=100)
s=Part.Compound([Part.Vertex(i) for i in p])
Part.show(s)



#### <img src="images/BIM_Column.svg" style="width:16px;"> dumpContent

dumpContent(Compression=3) -> bytearray

Dumps the content of the object, both the XML representation and the additional
data files required, into a byte representation.

Compression : int
    Set the data compression level in the range [0,9]. Set to 0 for no compression.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getAllDerivedFrom

Returns all descendants



#### <img src="images/BIM_Column.svg" style="width:16px;"> getD0

Returns the point of given parameter



#### <img src="images/BIM_Column.svg" style="width:16px;"> getD1

Returns the point and first derivative of given parameter



#### <img src="images/BIM_Column.svg" style="width:16px;"> getD2

Returns the point, first and second derivatives



#### <img src="images/BIM_Column.svg" style="width:16px;"> getD3

Returns the point, first, second and third derivatives



#### <img src="images/BIM_Column.svg" style="width:16px;"> getDN

Returns the n-th derivative



#### <img src="images/BIM_Column.svg" style="width:16px;"> getExtensionOfName

Gets the first geometry extension of the name indicated by the string.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getExtensionOfType

Gets the first geometry extension of the type indicated by the string.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getExtensions

Returns a list with information about the geometry extensions.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getPole

Get a pole of the Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getPoles

Get all poles of the Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getResolution

Computes for this Bezier curve the parametric tolerance (UTolerance)
for a given 3D tolerance (Tolerance3D).
If f(t) is the equation of this Bezier curve, the parametric tolerance
ensures that:
|t1-t0| < UTolerance =""==> |f(t1)-f(t0)| < Tolerance3D



#### <img src="images/BIM_Column.svg" style="width:16px;"> getWeight

Get a weight of the Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getWeights

Get all weights of the Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> hasExtensionOfName

Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.



#### <img src="images/BIM_Column.svg" style="width:16px;"> hasExtensionOfType

Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.



#### <img src="images/BIM_Column.svg" style="width:16px;"> increase

increase(Int=Degree)
Increases the degree of this Bezier curve to Degree.
As a result, the poles and weights tables are modified.



#### <img src="images/BIM_Column.svg" style="width:16px;"> insertPoleAfter

Inserts after the pole of index.



#### <img src="images/BIM_Column.svg" style="width:16px;"> insertPoleBefore

Inserts before the pole of index.



#### <img src="images/BIM_Column.svg" style="width:16px;"> interpolate

Interpolates a list of constraints.
                Each constraint is a list of a point and some optional derivatives
                An optional list of parameters can be passed. It must be of same size as constraint list.
                Otherwise, a simple uniform parametrization is used.
                Example :
                bezier.interpolate([[pt1, deriv11, deriv12], [pt2,], [pt3, deriv31]], [0, 0.4, 1.0])



#### <img src="images/BIM_Column.svg" style="width:16px;"> intersect

Returns all intersection points and curve segments between the curve and the curve/surface.

                  arguments: curve/surface (for the intersection), precision (float)



#### <img src="images/BIM_Column.svg" style="width:16px;"> intersect2d

Get intersection points with another curve lying on a plane.



#### <img src="images/BIM_Column.svg" style="width:16px;"> intersectCC

Returns all intersection points between this curve and the given curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> intersectCS

Returns all intersection points and curve segments between the curve and the surface.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isClosed

Returns true if the distance between the start point and end point of
                    this Bezier curve is less than or equal to gp::Resolution().



#### <img src="images/BIM_Column.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/BIM_Column.svg" style="width:16px;"> isPeriodic

Returns false.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isRational

Returns false if the weights of all the poles of this Bezier curve are equal.



#### <img src="images/BIM_Column.svg" style="width:16px;"> length

Computes the length of a curve
length([uMin,uMax,Tol]) -> Float



#### <img src="images/BIM_Column.svg" style="width:16px;"> makeRuledSurface

Make a ruled surface of this and the given curves



#### <img src="images/BIM_Column.svg" style="width:16px;"> mirror

Performs the symmetrical transformation of this geometric object



#### <img src="images/BIM_Column.svg" style="width:16px;"> normal

Vector = normal(pos) - Get the normal vector at the given parameter [First|Last] if defined



#### <img src="images/BIM_Column.svg" style="width:16px;"> parameter

Returns the parameter on the curve
of the nearest orthogonal projection of the point.



#### <img src="images/BIM_Column.svg" style="width:16px;"> parameterAtDistance

Returns the parameter on the curve of a point at the given distance from a starting parameter.
parameterAtDistance([abscissa, startingParameter]) -> Float the



#### <img src="images/BIM_Column.svg" style="width:16px;"> period

Returns the period of this curve
or raises an exception if it is not periodic.



#### <img src="images/BIM_Column.svg" style="width:16px;"> projectPoint

Computes the projection of a point on the curve

projectPoint(Point=Vector,[Method="NearestPoint"])
projectPoint(Vector,"NearestPoint") -> Vector
projectPoint(Vector,"LowerDistance") -> float
projectPoint(Vector,"LowerDistanceParameter") -> float
projectPoint(Vector,"Distance") -> list of floats
projectPoint(Vector,"Parameter") -> list of floats
projectPoint(Vector,"Point") -> list of points



#### <img src="images/BIM_Column.svg" style="width:16px;"> removePole

Removes the pole of index Index from the table of poles of this Bezier curve.
If this Bezier curve is rational, it can become non-rational.



#### <img src="images/BIM_Column.svg" style="width:16px;"> restoreContent

restoreContent(obj) -> None

Restore the content of the object from a byte representation as stored by `dumpContent`.
It could be restored from any Python object implementing the buffer protocol.

obj : buffer
    Object with buffer protocol support.



#### <img src="images/BIM_Column.svg" style="width:16px;"> reverse

Changes the direction of parametrization of the curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> reversedParameter

Returns the parameter on the reversed curve for
the point of parameter U on this curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> rotate

Rotates this geometric object at angle Ang (in radians) about axis



#### <img src="images/BIM_Column.svg" style="width:16px;"> scale

Applies a scaling transformation on this geometric object with a center and scaling factor



#### <img src="images/BIM_Column.svg" style="width:16px;"> segment

Modifies this Bezier curve by segmenting it.



#### <img src="images/BIM_Column.svg" style="width:16px;"> setExtension

Sets a geometry extension of the indicated type.



#### <img src="images/BIM_Column.svg" style="width:16px;"> setPole

Set a pole of the Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> setPoles

Set the poles of the Bezier curve.

                Takes a list of 3D Base.Vector objects.



#### <img src="images/BIM_Column.svg" style="width:16px;"> setWeight

(id, weight) Set a weight of the Bezier curve.



#### <img src="images/BIM_Column.svg" style="width:16px;"> tangent

Computes the tangent of parameter u on this curve



#### <img src="images/BIM_Column.svg" style="width:16px;"> toBSpline

Converts a curve of any type (only part from First to Last)
                    toBSpline([Float=First, Float=Last]) -> B-Spline curve



#### <img src="images/BIM_Column.svg" style="width:16px;"> toNurbs

Converts a curve of any type (only part from First to Last)
                    toNurbs([Float=First, Float=Last]) -> NURBS curve



#### <img src="images/BIM_Column.svg" style="width:16px;"> toShape

Return the shape for the geometry.



#### <img src="images/BIM_Column.svg" style="width:16px;"> transform

Applies a transformation to this geometric object



#### <img src="images/BIM_Column.svg" style="width:16px;"> translate

Translates this geometric object



#### <img src="images/BIM_Column.svg" style="width:16px;"> trim

Returns a trimmed curve defined in the given parameter range
                    trim([Float=First, Float=Last]) -> trimmed curve



#### <img src="images/BIM_Column.svg" style="width:16px;"> value

Computes the point of parameter u on this curve









---
⏵ [documentation index](../README.md) > [API](Category_API.md) > BezierCurve API
