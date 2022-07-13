# BSplineCurve API

Describes a B-Spline curve in 3D space



#### <img src="images/Type_enum.svg" style="width:16px;"> Content

Content of the object in XML representation.



#### <img src="images/Type_enum.svg" style="width:16px;"> Continuity

Returns the global continuity of the curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> Degree

Returns the polynomial degree of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> EndPoint

Returns the end point of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> FirstParameter

Returns the value of the first parameter.



#### <img src="images/Type_enum.svg" style="width:16px;"> FirstUKnotIndex

Returns the index in the knot array of the knot
corresponding to the first or last parameter
of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> KnotSequence

Returns the knots sequence of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> LastParameter

Returns the value of the last parameter.



#### <img src="images/Type_enum.svg" style="width:16px;"> LastUKnotIndex

Returns the index in the knot array of the knot
corresponding to the first or last parameter
of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> MaxDegree

Returns the value of the maximum polynomial degree of any
B-Spline curve curve. This value is 25.



#### <img src="images/Type_enum.svg" style="width:16px;"> MemSize

Memory size of the object in bytes.



#### <img src="images/Type_enum.svg" style="width:16px;"> Module

Module in which this class is defined



#### <img src="images/Type_enum.svg" style="width:16px;"> NbKnots

Returns the number of knots of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> NbPoles

Returns the number of poles of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> Rotation

Returns a rotation object to describe the orientation for curve that supports it



#### <img src="images/Type_enum.svg" style="width:16px;"> StartPoint

Returns the start point of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> Tag

Gives the tag of the geometry as string.



#### <img src="images/Type_enum.svg" style="width:16px;"> TypeId

Is the type of the FreeCAD object with module domain



#### <img src="images/Type_enum.svg" style="width:16px;"> approximate

Replaces this B-Spline curve by approximating a set of points.
					The function accepts keywords as arguments.

					approximate(Points = list_of_points)

					Optional arguments :

					DegMin = integer (3) : Minimum degree of the curve.
					DegMax = integer (8) : Maximum degree of the curve.
					Tolerance = float (1e-3) : approximating tolerance.
					Continuity = string ('C2') : Desired continuity of the curve.
					Possible values : 'C0','G1','C1','G2','C2','C3','CN'

					LengthWeight = float, CurvatureWeight = float, TorsionWeight = float
					If one of these arguments is not null, the functions approximates the
					points using variational smoothing algorithm, which tries to minimize
					additional criterium:
					LengthWeight*CurveLength + CurvatureWeight*Curvature + TorsionWeight*Torsion
                                        Continuity must be C0, C1(with DegMax >= 3) or C2(with DegMax >= 5).

					Parameters = list of floats : knot sequence of the approximated points.
					This argument is only used if the weights above are all null.

					ParamType = string ('Uniform','Centripetal' or 'ChordLength')
					Parameterization type. Only used if weights and Parameters above aren't specified.

					Note : Continuity of the spline defaults to C2. However, it may not be applied if
					it conflicts with other parameters ( especially DegMax ).



#### <img src="images/Type_enum.svg" style="width:16px;"> approximateBSpline

Approximates a curve of any type to a B-Spline curve
					approximateBSpline(Tolerance, MaxSegments, MaxDegree, [Order='C2']) -> B-Spline curve



#### <img src="images/Type_enum.svg" style="width:16px;"> buildFromPoles

Builds a B-Spline by a list of poles.
					arguments: poles (sequence of Base.Vector), [periodic (default is False), degree (default is 3), interpolate (default is False)]

					Examples:
					from FreeCAD import Base
					import Part
					V = Base.Vector
					poles = [V(-2, 2, 0),V(0, 2, 1),V(2, 2, 0),V(2, -2, 0),V(0, -2, 1),V(-2, -2, 0)]

					# non-periodic spline
					n=Part.BSplineCurve()
					n.buildFromPoles(poles)
					Part.show(n.toShape())

					# periodic spline
					n=Part.BSplineCurve()
					n.buildFromPoles(poles, True)
					Part.show(n.toShape())



#### <img src="images/Type_enum.svg" style="width:16px;"> buildFromPolesMultsKnots

Builds a B-Spline by a lists of Poles, Mults, Knots.
				arguments: poles (sequence of Base.Vector), [mults , knots, periodic, degree, weights (sequence of float), CheckRational]

				Examples:
				from FreeCAD import Base
				import Part
				V=Base.Vector
				poles=[V(-10,-10),V(10,-10),V(10,10),V(-10,10)]

				# non-periodic spline
				n=Part.BSplineCurve()
				n.buildFromPolesMultsKnots(poles,(3,1,3),(0,0.5,1),False,2)
				Part.show(n.toShape())

				# periodic spline
				p=Part.BSplineCurve()
				p.buildFromPolesMultsKnots(poles,(1,1,1,1,1),(0,0.25,0.5,0.75,1),True,2)
				Part.show(p.toShape())

				# periodic and rational spline
				r=Part.BSplineCurve()
				r.buildFromPolesMultsKnots(poles,(1,1,1,1,1),(0,0.25,0.5,0.75,1),True,2,(1,0.8,0.7,0.2))
				Part.show(r.toShape())



#### <img src="images/Type_enum.svg" style="width:16px;"> centerOfCurvature

Vector = centerOfCurvature(float pos) - Get the center of curvature at the given parameter [First|Last] if defined



#### <img src="images/Type_enum.svg" style="width:16px;"> clone

Create a clone of this geometry with the same Tag



#### <img src="images/Type_enum.svg" style="width:16px;"> continuityWith

Computes the continuity of two curves



#### <img src="images/Type_enum.svg" style="width:16px;"> copy

Create a copy of this geometry



#### <img src="images/Type_enum.svg" style="width:16px;"> curvature

Float = curvature(pos) - Get the curvature at the given parameter [First|Last] if defined



#### <img src="images/Type_enum.svg" style="width:16px;"> deleteExtensionOfName

Deletes all extensions of the indicated name.



#### <img src="images/Type_enum.svg" style="width:16px;"> deleteExtensionOfType

Deletes all extensions of the indicated type.



#### <img src="images/Type_enum.svg" style="width:16px;"> discretize

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



#### <img src="images/Type_enum.svg" style="width:16px;"> dumpContent

dumpContent(Compression=3) -> bytearray

Dumps the content of the object, both the XML representation and the additional
data files required, into a byte representation.

Compression : int
    Set the data compression level in the range [0,9]. Set to 0 for no compression.



#### <img src="images/Type_enum.svg" style="width:16px;"> getAllDerivedFrom

Returns all descendants



#### <img src="images/Type_enum.svg" style="width:16px;"> getCardinalSplineTangents

Compute the tangents for a Cardinal spline



#### <img src="images/Type_enum.svg" style="width:16px;"> getD0

Returns the point of given parameter



#### <img src="images/Type_enum.svg" style="width:16px;"> getD1

Returns the point and first derivative of given parameter



#### <img src="images/Type_enum.svg" style="width:16px;"> getD2

Returns the point, first and second derivatives



#### <img src="images/Type_enum.svg" style="width:16px;"> getD3

Returns the point, first, second and third derivatives



#### <img src="images/Type_enum.svg" style="width:16px;"> getDN

Returns the n-th derivative



#### <img src="images/Type_enum.svg" style="width:16px;"> getExtensionOfName

Gets the first geometry extension of the name indicated by the string.



#### <img src="images/Type_enum.svg" style="width:16px;"> getExtensionOfType

Gets the first geometry extension of the type indicated by the string.



#### <img src="images/Type_enum.svg" style="width:16px;"> getExtensions

Returns a list with information about the geometry extensions.



#### <img src="images/Type_enum.svg" style="width:16px;"> getKnot

Get a knot of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> getKnots

Get all knots of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> getMultiplicities

Returns the multiplicities table M of the knots of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> getMultiplicity

Returns the multiplicity of the knot of index
from the knots table of this B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> getPole

Get a pole of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> getPoles

Get all poles of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> getPolesAndWeights

Returns the table of poles and weights in homogeneous coordinates.



#### <img src="images/Type_enum.svg" style="width:16px;"> getResolution

Computes for this B-Spline curve the parametric tolerance (UTolerance)
for a given 3D tolerance (Tolerance3D).
If f(t) is the equation of this B-Spline curve, the parametric tolerance
ensures that:
|t1-t0| < UTolerance ===> |f(t1)-f(t0)| < Tolerance3D



#### <img src="images/Type_enum.svg" style="width:16px;"> getWeight

Get a weight of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> getWeights

Get all weights of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> hasExtensionOfName

Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.



#### <img src="images/Type_enum.svg" style="width:16px;"> hasExtensionOfType

Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.



#### <img src="images/Type_enum.svg" style="width:16px;"> increaseDegree

increase(Int=Degree)
Increases the degree of this B-Spline curve to Degree.
As a result, the poles, weights and multiplicities tables
are modified; the knots table is not changed. Nothing is
done if Degree is less than or equal to the current degree.



#### <img src="images/Type_enum.svg" style="width:16px;"> increaseMultiplicity

increaseMultiplicity(int index, int mult)
				increaseMultiplicity(int start, int end, int mult)
				Increases multiplicity of knots up to mult.

				index: the index of a knot to modify (1-based)
				start, end: index range of knots to modify.
				If mult is lower or equal to the current multiplicity nothing is done. If mult is higher than the degree the degree is used.



#### <img src="images/Type_enum.svg" style="width:16px;"> incrementMultiplicity

incrementMultiplicity(int start, int end, int mult)
				Raises multiplicity of knots by mult.

				start, end: index range of knots to modify.



#### <img src="images/Type_enum.svg" style="width:16px;"> insertKnot

insertKnot(u, mult = 1, tol = 0.0)
				Inserts a knot value in the sequence of knots. If u is an existing knot the
				multiplicity is increased by mult.



#### <img src="images/Type_enum.svg" style="width:16px;"> insertKnots

insertKnots(list_of_floats, list_of_ints, tol = 0.0, bool_add = True)
				Inserts a set of knots values in the sequence of knots.

				For each u = list_of_floats[i], mult = list_of_ints[i]

				If u is an existing knot the multiplicity is increased by mult if bool_add is
				True, otherwise increased to mult.

				If u is not on the parameter range nothing is done.

				If the multiplicity is negative or null nothing is done. The new multiplicity
				is limited to the degree.

				The tolerance criterion for knots equality is the max of Epsilon(U) and ParametricTolerance.



#### <img src="images/Type_enum.svg" style="width:16px;"> interpolate

Replaces this B-Spline curve by interpolating a set of points.
					The function accepts keywords as arguments.

					interpolate(Points = list_of_points)

					Optional arguments :

					PeriodicFlag = bool (False) : Sets the curve closed or opened.
					Tolerance = float (1e-6) : interpolating tolerance

					Parameters : knot sequence of the interpolated points.
					If not supplied, the function defaults to chord-length parameterization.
					If PeriodicFlag == True, one extra parameter must be appended.

					EndPoint Tangent constraints :

					InitialTangent = vector, FinalTangent = vector
					specify tangent vectors for starting and ending points
					of the BSpline. Either none, or both must be specified.

					Full Tangent constraints :

					Tangents = list_of_vectors, TangentFlags = list_of_bools
					Both lists must have the same length as Points list.
					Tangents specifies the tangent vector of each point in Points list.
					TangentFlags (bool) activates or deactivates the corresponding tangent.
					These arguments will be ignored if EndPoint Tangents (above) are also defined.

					Note : Continuity of the spline defaults to C2. However, if periodic, or tangents
					are supplied, the continuity will drop to C1.



#### <img src="images/Type_enum.svg" style="width:16px;"> intersect

Returns all intersection points and curve segments between the curve and the curve/surface.

				  arguments: curve/surface (for the intersection), precision (float)



#### <img src="images/Type_enum.svg" style="width:16px;"> intersect2d

Get intersection points with another curve lying on a plane.



#### <img src="images/Type_enum.svg" style="width:16px;"> intersectCC

Returns all intersection points between this curve and the given curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> intersectCS

Returns all intersection points and curve segments between the curve and the surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> isClosed

Returns true if the distance between the start point and end point of
					this B-Spline curve is less than or equal to gp::Resolution().



#### <img src="images/Type_enum.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/Type_enum.svg" style="width:16px;"> isPeriodic

Returns true if this BSpline curve is periodic.



#### <img src="images/Type_enum.svg" style="width:16px;"> isRational

Returns true if this B-Spline curve is rational.
					A B-Spline curve is rational if, at the time of construction,
					the weight table has been initialized.



#### <img src="images/Type_enum.svg" style="width:16px;"> join

Build a new spline by joining this and a second spline.



#### <img src="images/Type_enum.svg" style="width:16px;"> length

Computes the length of a curve
length([uMin,uMax,Tol]) -> Float



#### <img src="images/Type_enum.svg" style="width:16px;"> makeC1Continuous

makeC1Continuous(tol = 1e-6, ang_tol = 1e-7)
					Reduces as far as possible the multiplicities of the knots of this BSpline
					(keeping the geometry). It returns a new BSpline, which could still be C0.
					tol is a geometrical tolerance.
					The tol_ang is angular tolerance, in radians. It sets tolerable angle mismatch
					of the tangents on the left and on the right to decide if the curve is G1 or
					not at a given point.



#### <img src="images/Type_enum.svg" style="width:16px;"> makeRuledSurface

Make a ruled surface of this and the given curves



#### <img src="images/Type_enum.svg" style="width:16px;"> mirror

Performs the symmetrical transformation of this geometric object



#### <img src="images/Type_enum.svg" style="width:16px;"> movePoint

movePoint(U, P, Index1, Index2)
				Moves the point of parameter U of this B-Spline curve to P.
Index1 and Index2 are the indexes in the table of poles of this B-Spline curve
of the first and last poles designated to be moved.

Returns: (FirstModifiedPole, LastModifiedPole). They are the indexes of the
first and last poles which are effectively modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> normal

Vector = normal(pos) - Get the normal vector at the given parameter [First|Last] if defined



#### <img src="images/Type_enum.svg" style="width:16px;"> parameter

Returns the parameter on the curve
of the nearest orthogonal projection of the point.



#### <img src="images/Type_enum.svg" style="width:16px;"> parameterAtDistance

Returns the parameter on the curve of a point at the given distance from a starting parameter.
parameterAtDistance([abscissa, startingParameter]) -> Float the



#### <img src="images/Type_enum.svg" style="width:16px;"> period

Returns the period of this curve
or raises an exception if it is not periodic.



#### <img src="images/Type_enum.svg" style="width:16px;"> projectPoint

Computes the projection of a point on the curve

projectPoint(Point=Vector,[Method="NearestPoint"])
projectPoint(Vector,"NearestPoint") -> Vector
projectPoint(Vector,"LowerDistance") -> float
projectPoint(Vector,"LowerDistanceParameter") -> float
projectPoint(Vector,"Distance") -> list of floats
projectPoint(Vector,"Parameter") -> list of floats
projectPoint(Vector,"Point") -> list of points



#### <img src="images/Type_enum.svg" style="width:16px;"> removeKnot

removeKnot(Index, M, tol)

					Reduces the multiplicity of the knot of index Index to M.
					If M is equal to 0, the knot is removed.
					With a modification of this type, the array of poles is also modified.
					Two different algorithms are systematically used to compute the new
					poles of the curve. If, for each pole, the distance between the pole
					calculated using the first algorithm and the same pole calculated using
					the second algorithm, is less than Tolerance, this ensures that the curve
					is not modified by more than Tolerance. Under these conditions, true is
					returned; otherwise, false is returned.

					A low tolerance is used to prevent modification of the curve.
					A high tolerance is used to 'smooth' the curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> restoreContent

restoreContent(obj) -> None

Restore the content of the object from a byte representation as stored by `dumpContent`.
It could be restored from any Python object implementing the buffer protocol.

obj : buffer
    Object with buffer protocol support.



#### <img src="images/Type_enum.svg" style="width:16px;"> reverse

Changes the direction of parametrization of the curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> reversedParameter

Returns the parameter on the reversed curve for
the point of parameter U on this curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> rotate

Rotates this geometric object at angle Ang (in radians) about axis



#### <img src="images/Type_enum.svg" style="width:16px;"> scale

Applies a scaling transformation on this geometric object with a center and scaling factor



#### <img src="images/Type_enum.svg" style="width:16px;"> segment

segment(u1,u2)
					Modifies this B-Spline curve by segmenting it.



#### <img src="images/Type_enum.svg" style="width:16px;"> setExtension

Sets a geometry extension of the indicated type.



#### <img src="images/Type_enum.svg" style="width:16px;"> setKnot

Set a knot of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> setKnots

Set knots of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> setNotPeriodic

Changes this B-Spline curve into a non-periodic curve.
If this curve is already non-periodic, it is not modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setOrigin

Assigns the knot of index Index in the knots table
as the origin of this periodic B-Spline curve. As a consequence,
the knots and poles tables are modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setPeriodic

Changes this B-Spline curve into a periodic curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> setPole

Modifies this B-Spline curve by assigning P
to the pole of index Index in the poles table.



#### <img src="images/Type_enum.svg" style="width:16px;"> setWeight

Set a weight of the B-Spline curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> tangent

Computes the tangent of parameter u on this curve



#### <img src="images/Type_enum.svg" style="width:16px;"> toBSpline

Converts a curve of any type (only part from First to Last)
					toBSpline([Float=First, Float=Last]) -> B-Spline curve



#### <img src="images/Type_enum.svg" style="width:16px;"> toBezier

Build a list of Bezier splines.



#### <img src="images/Type_enum.svg" style="width:16px;"> toBiArcs

Build a list of arcs and lines to approximate the B-spline.
					toBiArcs(tolerance) -> list.



#### <img src="images/Type_enum.svg" style="width:16px;"> toNurbs

Converts a curve of any type (only part from First to Last)
                    toNurbs([Float=First, Float=Last]) -> NURBS curve



#### <img src="images/Type_enum.svg" style="width:16px;"> toShape

Return the shape for the geometry.



#### <img src="images/Type_enum.svg" style="width:16px;"> transform

Applies a transformation to this geometric object



#### <img src="images/Type_enum.svg" style="width:16px;"> translate

Translates this geometric object



#### <img src="images/Type_enum.svg" style="width:16px;"> trim

Returns a trimmed curve defined in the given parameter range
                    trim([Float=First, Float=Last]) -> trimmed curve



#### <img src="images/Type_enum.svg" style="width:16px;"> value

Computes the point of parameter u on this curve









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > BSplineCurve API
