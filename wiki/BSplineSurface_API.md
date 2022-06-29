# BSplineSurface API

Describes a B-Spline surface in 3D space



#### <img src="images/Type_enum.svg" style="width:16px;"> Content

Content of the object in XML representation.



#### <img src="images/Type_enum.svg" style="width:16px;"> Continuity

Returns the global continuity of the surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> FirstUKnotIndex

Returns the index in the knot array associated with the u parametric direction,
					which corresponds to the first parameter of this B-Spline surface in the specified
					parametric direction.

					The isoparametric curves corresponding to these values are the boundary curves of
					this surface.

					Note: The index does not correspond to the first knot of the surface in the specified
					parametric direction unless the multiplicity of the first knot is equal to Degree + 1,
					where Degree is the degree of this surface in the corresponding parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> FirstVKnotIndex

Returns the index in the knot array associated with the v parametric direction,
					which corresponds to the first parameter of this B-Spline surface in the specified
					parametric direction.

					The isoparametric curves corresponding to these values are the boundary curves of
					this surface.

					Note: The index does not correspond to the first knot of the surface in the specified
					parametric direction unless the multiplicity of the first knot is equal to Degree + 1,
					where Degree is the degree of this surface in the corresponding parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> LastUKnotIndex

Returns the index in the knot array associated with the u parametric direction,
					which corresponds to the last parameter of this B-Spline surface in the specified
					parametric direction.

					The isoparametric curves corresponding to these values are the boundary curves of
					this surface.

					Note: The index does not correspond to the first knot of the surface in the specified
					parametric direction unless the multiplicity of the last knot is equal to Degree + 1,
					where Degree is the degree of this surface in the corresponding parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> LastVKnotIndex

Returns the index in the knot array associated with the v parametric direction,
					which corresponds to the last parameter of this B-Spline surface in the specified
					parametric direction.

					The isoparametric curves corresponding to these values are the boundary curves of
					this surface.

					Note: The index does not correspond to the first knot of the surface in the specified
					parametric direction unless the multiplicity of the last knot is equal to Degree + 1,
					where Degree is the degree of this surface in the corresponding parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> MaxDegree

Returns the value of the maximum polynomial degree of any
					B-Spline surface surface in either parametric directions.
					This value is 25.



#### <img src="images/Type_enum.svg" style="width:16px;"> MemSize

Memory size of the object in bytes.



#### <img src="images/Type_enum.svg" style="width:16px;"> Module

Module in which this class is defined



#### <img src="images/Type_enum.svg" style="width:16px;"> NbUKnots

Returns the number of knots of this B-Spline surface in the u parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> NbUPoles

Returns the number of poles of this B-Spline surface in the u parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> NbVKnots

Returns the number of knots of this B-Spline surface in the v parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> NbVPoles

Returns the number of poles of this B-Spline surface in the v parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> Rotation

Returns a rotation object to describe the orientation for surface that supports it



#### <img src="images/Type_enum.svg" style="width:16px;"> Tag

Gives the tag of the geometry as string.



#### <img src="images/Type_enum.svg" style="width:16px;"> TypeId

Is the type of the FreeCAD object with module domain



#### <img src="images/Type_enum.svg" style="width:16px;"> UDegree

Returns the degree of this B-Spline surface in the u parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> UKnotSequence

Returns the knots sequence of this B-Spline surface in
						the u direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> UPeriod

Returns the period of this patch in the u parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> VDegree

Returns the degree of this B-Spline surface in the v parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> VKnotSequence

Returns the knots sequence of this B-Spline surface in
					the v direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> VPeriod

Returns the period of this patch in the v parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> approximate

Replaces this B-Spline surface by approximating a set of points.
					This method uses keywords :
					- Points = 2Darray of points (or floats, in combination with X0, dX, Y0, dY)
					- DegMin (int), DegMax (int)
					- Continuity = 0,1 or 2 (for C0, C1, C2)
					- Tolerance (float)
					- X0, dX, Y0, dY (floats) with Points = 2Darray of floats
					- ParamType = 'Uniform','Centripetal' or 'ChordLength'
					- LengthWeight, CurvatureWeight, TorsionWeight (floats)
					(with this smoothing algorithm, continuity C1 requires DegMax >= 3 and C2, DegMax >=5)

					Possible combinations :
					- approximate(Points, DegMin, DegMax, Continuity, Tolerance)
					- approximate(Points, DegMin, DegMax, Continuity, Tolerance, X0, dX, Y0, dY)
					With explicit keywords :
					- approximate(Points, DegMin, DegMax, Continuity, Tolerance, ParamType)
					- approximate(Points, DegMax, Continuity, Tolerance, LengthWeight, CurvatureWeight, TorsionWeight)



#### <img src="images/Type_enum.svg" style="width:16px;"> bounds

Returns the parametric bounds (U1, U2, V1, V2) of this B-Spline surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> buildFromNSections

Builds a B-Spline from a list of control curves



#### <img src="images/Type_enum.svg" style="width:16px;"> buildFromPolesMultsKnots

Builds a B-Spline by a lists of Poles, Mults and Knots
					arguments: poles (sequence of sequence of Base.Vector), umults, vmults, [uknots, vknots, uperiodic, vperiodic, udegree, vdegree, weights (sequence of sequence of float)]



#### <img src="images/Type_enum.svg" style="width:16px;"> clone

Create a clone of this geometry with the same Tag



#### <img src="images/Type_enum.svg" style="width:16px;"> copy

Create a copy of this geometry



#### <img src="images/Type_enum.svg" style="width:16px;"> curvature

curvature(u,v,type) -> float
The value of type must be one of this: Max, Min, Mean or Gauss
Computes the curvature of parameter (u,v) on this geometry



#### <img src="images/Type_enum.svg" style="width:16px;"> curvatureDirections

curvatureDirections(u,v) -> (Vector,Vector)
Computes the directions of maximum and minimum curvature
of parameter (u,v) on this geometry.
The first vector corresponds to the maximum curvature,
the second vector corresponds to the minimum curvature.



#### <img src="images/Type_enum.svg" style="width:16px;"> deleteExtensionOfName

Deletes all extensions of the indicated name.



#### <img src="images/Type_enum.svg" style="width:16px;"> deleteExtensionOfType

Deletes all extensions of the indicated type.



#### <img src="images/Type_enum.svg" style="width:16px;"> dumpContent

dumpContent(Compression=3) -> bytearray

Dumps the content of the object, both the XML representation and the additional
data files required, into a byte representation.

Compression : int
    Set the data compression level in the range [0,9]. Set to 0 for no compression.



#### <img src="images/Type_enum.svg" style="width:16px;"> exchangeUV

Exchanges the u and v parametric directions on this B-Spline surface.
					As a consequence:
					-- the poles and weights tables are transposed,
					-- the knots and multiplicities tables are exchanged,
					-- degrees of continuity and rational, periodic and uniform
					   characteristics are exchanged and
					-- the orientation of the surface is reversed.



#### <img src="images/Type_enum.svg" style="width:16px;"> getAllDerivedFrom

Returns all descendants



#### <img src="images/Type_enum.svg" style="width:16px;"> getD0

Returns the point of given parameter



#### <img src="images/Type_enum.svg" style="width:16px;"> getDN

Returns the n-th derivative



#### <img src="images/Type_enum.svg" style="width:16px;"> getExtensionOfName

Gets the first geometry extension of the name indicated by the string.



#### <img src="images/Type_enum.svg" style="width:16px;"> getExtensionOfType

Gets the first geometry extension of the type indicated by the string.



#### <img src="images/Type_enum.svg" style="width:16px;"> getExtensions

Returns a list with information about the geometry extensions.



#### <img src="images/Type_enum.svg" style="width:16px;"> getPole

Returns the pole of index (UIndex,VIndex) of this B-Spline surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> getPoles

Returns the table of poles of this B-Spline surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> getPolesAndWeights

Returns the table of poles and weights in homogeneous coordinates.



#### <img src="images/Type_enum.svg" style="width:16px;"> getResolution

Computes two tolerance values for this B-Spline surface, based on the
					given tolerance in 3D space Tolerance3D. The tolerances computed are:
					-- UTolerance in the u parametric direction and
					-- VTolerance in the v parametric direction.

					If f(u,v) is the equation of this B-Spline surface, UTolerance and
					VTolerance guarantee that:
					|u1 - u0| < UTolerance
					|v1 - v0| < VTolerance
					====> ||f(u1, v1) - f(u2, v2)|| < Tolerance3D



#### <img src="images/Type_enum.svg" style="width:16px;"> getUKnot

Returns, for this B-Spline surface, in the u parametric direction
					the knot of index UIndex of the knots table.



#### <img src="images/Type_enum.svg" style="width:16px;"> getUKnots

Returns, for this B-Spline surface, the knots table
					in the u parametric direction



#### <img src="images/Type_enum.svg" style="width:16px;"> getUMultiplicities

Returns, for this B-Spline surface, the table of
					multiplicities in the u parametric direction



#### <img src="images/Type_enum.svg" style="width:16px;"> getUMultiplicity

Returns, for this B-Spline surface, the multiplicity of
					the knot of index UIndex in the u parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> getVKnot

Returns, for this B-Spline surface, in the v parametric direction
					the knot of index VIndex of the knots table.



#### <img src="images/Type_enum.svg" style="width:16px;"> getVKnots

Returns, for this B-Spline surface, the knots table
					in the v parametric direction



#### <img src="images/Type_enum.svg" style="width:16px;"> getVMultiplicities

Returns, for this B-Spline surface, the table of
					multiplicities in the v parametric direction



#### <img src="images/Type_enum.svg" style="width:16px;"> getVMultiplicity

Returns, for this B-Spline surface, the multiplicity of
					the knot of index VIndex in the v parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> getWeight

Return the weight of the pole of index (UIndex,VIndex)
					in the poles table for this B-Spline surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> getWeights

Returns the table of weights of the poles for this B-Spline surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> hasExtensionOfName

Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.



#### <img src="images/Type_enum.svg" style="width:16px;"> hasExtensionOfType

Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.



#### <img src="images/Type_enum.svg" style="width:16px;"> increaseDegree

increase(Int=UDegree, int=VDegree)
					Increases the degrees of this B-Spline surface to UDegree and VDegree
					in the u and v parametric directions respectively.
					As a result, the tables of poles, weights and multiplicities are modified.
					The tables of knots is not changed.

					Note: Nothing is done if the given degree is less than or equal to the
					current degree in the corresponding parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> increaseUMultiplicity

Increases the multiplicity in the u direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> increaseVMultiplicity

Increases the multiplicity in the v direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> incrementUMultiplicity

Increment the multiplicity in the u direction



#### <img src="images/Type_enum.svg" style="width:16px;"> incrementVMultiplicity

Increment the multiplicity in the v direction



#### <img src="images/Type_enum.svg" style="width:16px;"> insertUKnot

insertUKnote(float U, int Index, float Tolerance) - Insert or override a knot



#### <img src="images/Type_enum.svg" style="width:16px;"> insertUKnots

insertUKnote(List of float U, List of float Mult, float Tolerance) - Inserts knots.



#### <img src="images/Type_enum.svg" style="width:16px;"> insertVKnot

insertUKnote(float V, int Index, float Tolerance) - Insert or override a knot.



#### <img src="images/Type_enum.svg" style="width:16px;"> insertVKnots

insertUKnote(List of float V, List of float Mult, float Tolerance) - Inserts knots.



#### <img src="images/Type_enum.svg" style="width:16px;"> interpolate

interpolate(points)
					interpolate(zpoints, X0, dX, Y0, dY)

					Replaces this B-Spline surface by interpolating a set of points.
					The resulting surface is of degree 3 and continuity C2.
					Arguments:
					a 2 dimensional array of vectors, that the surface passes through
					or
					a 2 dimensional array of floats with the z values,
					the x starting point X0 (float),
					the x increment dX (float),
					the y starting point Y0 and increment dY



#### <img src="images/Type_enum.svg" style="width:16px;"> intersect

Returns all intersection points/curves between the surface and the curve/surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> intersectSS

Returns all intersection curves of this surface and the given surface.
The required arguments are:
* Second surface
* precision code (optional, default=0)



#### <img src="images/Type_enum.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/Type_enum.svg" style="width:16px;"> isPlanar

isPlanar([float]) -> Bool
Checks if the surface is planar within a certain tolerance.



#### <img src="images/Type_enum.svg" style="width:16px;"> isUClosed

Checks if this surface is closed in the u parametric direction.
					Returns true if, in the table of poles the first row and the last
					row are identical.



#### <img src="images/Type_enum.svg" style="width:16px;"> isUPeriodic

Returns true if this surface is periodic in the u parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> isURational

Returns false if the equation of this B-Spline surface is polynomial
					(e.g. non-rational) in the u or v parametric direction.
					In other words, returns false if for each row of poles, the associated
					weights are identical



#### <img src="images/Type_enum.svg" style="width:16px;"> isUmbillic

isUmbillic(u,v) -> bool
Check if the geometry on parameter is an umbillic point,
i.e. maximum and minimum curvature are equal.



#### <img src="images/Type_enum.svg" style="width:16px;"> isVClosed

Checks if this surface is closed in the v parametric direction.
					Returns true if, in the table of poles the first column and the
					last column are identical.



#### <img src="images/Type_enum.svg" style="width:16px;"> isVPeriodic

Returns true if this surface is periodic in the v parametric direction.



#### <img src="images/Type_enum.svg" style="width:16px;"> isVRational

Returns false if the equation of this B-Spline surface is polynomial
					(e.g. non-rational) in the u or v parametric direction.
					In other words, returns false if for each column of poles, the associated
					weights are identical



#### <img src="images/Type_enum.svg" style="width:16px;"> mirror

Performs the symmetrical transformation of this geometric object



#### <img src="images/Type_enum.svg" style="width:16px;"> movePoint

Moves the point of parameters (U, V) of this B-Spline surface to P.
					UIndex1, UIndex2, VIndex1 and VIndex2 are the indexes in the poles
					table of this B-Spline surface, of the first and last poles which
					can be moved in each parametric direction.
					The returned indexes UFirstIndex, ULastIndex, VFirstIndex and
					VLastIndex are the indexes of the first and last poles effectively
					modified in each parametric direction.
					In the event of incompatibility between UIndex1, UIndex2, VIndex1,
					VIndex2 and the values U and V:
					-- no change is made to this B-Spline surface, and
					-- UFirstIndex, ULastIndex, VFirstIndex and VLastIndex are set to
					   null.



#### <img src="images/Type_enum.svg" style="width:16px;"> normal

normal(u,v) -> Vector
Computes the normal of parameter (u,v) on this geometry



#### <img src="images/Type_enum.svg" style="width:16px;"> parameter

Returns the parameter on the curve
of the nearest orthogonal projection of the point.



#### <img src="images/Type_enum.svg" style="width:16px;"> projectPoint

Computes the projection of a point on the surface

projectPoint(Point=Vector,[Method="NearestPoint"])
projectPoint(Vector,"NearestPoint") -> Vector
projectPoint(Vector,"LowerDistance") -> float
projectPoint(Vector,"LowerDistanceParameters") -> tuple of floats (u,v)
projectPoint(Vector,"Distance") -> list of floats
projectPoint(Vector,"Parameters") -> list of tuples of floats
projectPoint(Vector,"Point") -> list of points



#### <img src="images/Type_enum.svg" style="width:16px;"> removeUKnot

Reduces to M the multiplicity of the knot of index Index in the given
				parametric direction. If M is 0, the knot is removed.
				With a modification of this type, the table of poles is also modified.
				Two different algorithms are used systematically to compute the new
				poles of the surface. For each pole, the distance between the pole
				calculated using the first algorithm and the same pole calculated using
				the second algorithm, is checked. If this distance is less than Tolerance
				it ensures that the surface is not modified by more than Tolerance.
				Under these conditions, the function returns true; otherwise, it returns
				false.

				A low tolerance prevents modification of the surface. A high tolerance
				'smoothes' the surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> removeVKnot

Reduces to M the multiplicity of the knot of index Index in the given
				parametric direction. If M is 0, the knot is removed.
				With a modification of this type, the table of poles is also modified.
				Two different algorithms are used systematically to compute the new
				poles of the surface. For each pole, the distance between the pole
				calculated using the first algorithm and the same pole calculated using
				the second algorithm, is checked. If this distance is less than Tolerance
				it ensures that the surface is not modified by more than Tolerance.
				Under these conditions, the function returns true; otherwise, it returns
				false.

				A low tolerance prevents modification of the surface. A high tolerance
				'smoothes' the surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> reparametrize

Returns a reparametrized copy of this surface



#### <img src="images/Type_enum.svg" style="width:16px;"> restoreContent

restoreContent(obj) -> None

Restore the content of the object from a byte representation as stored by `dumpContent`.
It could be restored from any Python object implementing the buffer protocol.

obj : buffer
    Object with buffer protocol support.



#### <img src="images/Type_enum.svg" style="width:16px;"> rotate

Rotates this geometric object at angle Ang (in radians) about axis



#### <img src="images/Type_enum.svg" style="width:16px;"> scale

Applies a scaling transformation on this geometric object with a center and scaling factor



#### <img src="images/Type_enum.svg" style="width:16px;"> segment

Modifies this B-Spline surface by segmenting it between U1 and U2 in the
					u parametric direction and between V1 and V2 in the v parametric direction.
					Any of these values can be outside the bounds of this surface, but U2 must
					be greater than U1 and V2 must be greater than V1.

					All the data structure tables of this B-Spline surface are modified but the
					knots located between U1 and U2 in the u parametric direction, and between
					V1 and V2 in the v parametric direction are retained.
					The degree of the surface in each parametric direction is not modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setExtension

Sets a geometry extension of the indicated type.



#### <img src="images/Type_enum.svg" style="width:16px;"> setPole

Modifies this B-Spline surface by assigning P to the pole of
					index (UIndex, VIndex) in the poles table.
					The second syntax allows you also to change the weight of the
					modified pole. The weight is set to Weight. This syntax must
					only be used for rational surfaces.
					Modifies this B-Spline curve by assigning P to the pole of
					index Index in the poles table.



#### <img src="images/Type_enum.svg" style="width:16px;"> setPoleCol

Modifies this B-Spline surface by assigning values to all or part
					of the column of poles of index VIndex, of this B-Spline surface.
					You can also change the weights of the modified poles. The weights
					are set to the corresponding values of CPoleWeights.
					These syntaxes must only be used for rational surfaces.



#### <img src="images/Type_enum.svg" style="width:16px;"> setPoleRow

Modifies this B-Spline surface by assigning values to all or part
					of the row of poles of index VIndex, of this B-Spline surface.
					You can also change the weights of the modified poles. The weights
					are set to the corresponding values of CPoleWeights.
					These syntaxes must only be used for rational surfaces.



#### <img src="images/Type_enum.svg" style="width:16px;"> setUKnot

Modifies this B-Spline surface by assigning the value K to the knot of index
					UIndex of the knots table corresponding to the u parametric direction.
					This modification remains relatively local, since K must lie between the values
					of the knots which frame the modified knot.

					You can also increase the multiplicity of the modified knot to M. Note however
					that it is not possible to decrease the multiplicity of a knot with this function.



#### <img src="images/Type_enum.svg" style="width:16px;"> setUKnots

Changes all knots of this B-Spline surface in the u parametric
					direction. The multiplicity of the knots is not modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setUNotPeriodic

Changes this B-Spline surface into a non-periodic one in the u parametric direction.
					If this B-Spline surface is already non-periodic in the given parametric direction,
					it is not modified.
					If this B-Spline surface is periodic in the given parametric direction, the boundaries
					of the surface are not given by the first and last rows (or columns) of poles (because
					the multiplicity of the first knot and of the last knot in the given parametric direction
					are not modified, nor are they equal to Degree+1, where Degree is the degree of this
					B-Spline surface in the given parametric direction). Only the function Segment ensures
					this property.

					Note: the poles and knots tables are modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setUOrigin

Assigns the knot of index Index in the knots table
					in the u parametric direction to be the origin of
					this periodic B-Spline surface. As a consequence,
					the knots and poles tables are modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setUPeriodic

Modifies this surface to be periodic in the u parametric direction.
					To become periodic in a given parametric direction a surface must
					be closed in that parametric direction, and the knot sequence relative
					to that direction must be periodic.
					To generate this periodic sequence of knots, the functions FirstUKnotIndex
					and LastUKnotIndex are used to compute I1 and I2. These are the indexes,
					in the knot array associated with the given parametric direction, of the
					knots that correspond to the first and last parameters of this B-Spline
					surface in the given parametric direction. Hence the period is:

					Knots(I1) - Knots(I2)

					As a result, the knots and poles tables are modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setVKnot

Modifies this B-Spline surface by assigning the value K to the knot of index
					VIndex of the knots table corresponding to the v parametric direction.
					This modification remains relatively local, since K must lie between the values
					of the knots which frame the modified knot.

					You can also increase the multiplicity of the modified knot to M. Note however
					that it is not possible to decrease the multiplicity of a knot with this function.



#### <img src="images/Type_enum.svg" style="width:16px;"> setVKnots

Changes all knots of this B-Spline surface in the v parametric
					direction. The multiplicity of the knots is not modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setVNotPeriodic

Changes this B-Spline surface into a non-periodic one in the v parametric direction.
					If this B-Spline surface is already non-periodic in the given parametric direction,
					it is not modified.
					If this B-Spline surface is periodic in the given parametric direction, the boundaries
					of the surface are not given by the first and last rows (or columns) of poles (because
					the multiplicity of the first knot and of the last knot in the given parametric direction
					are not modified, nor are they equal to Degree+1, where Degree is the degree of this
					B-Spline surface in the given parametric direction). Only the function Segment ensures
					this property.

					Note: the poles and knots tables are modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setVOrigin

Assigns the knot of index Index in the knots table
					in the v parametric direction to be the origin of
					this periodic B-Spline surface. As a consequence,
					the knots and poles tables are modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setVPeriodic

Modifies this surface to be periodic in the v parametric direction.
					To become periodic in a given parametric direction a surface must
					be closed in that parametric direction, and the knot sequence relative
					to that direction must be periodic.
					To generate this periodic sequence of knots, the functions FirstUKnotIndex
					and LastUKnotIndex are used to compute I1 and I2. These are the indexes,
					in the knot array associated with the given parametric direction, of the
					knots that correspond to the first and last parameters of this B-Spline
					surface in the given parametric direction. Hence the period is:

					Knots(I1) - Knots(I2)

					As a result, the knots and poles tables are modified.



#### <img src="images/Type_enum.svg" style="width:16px;"> setWeight

Modifies this B-Spline surface by assigning the value Weight to the weight
					of the pole of index (UIndex, VIndex) in the poles tables of this B-Spline
					surface.

					This function must only be used for rational surfaces.



#### <img src="images/Type_enum.svg" style="width:16px;"> setWeightCol

Modifies this B-Spline surface by assigning values to all or part of the
					weights of the column of poles of index VIndex of this B-Spline surface.

					The modified part of the column of weights is defined by the bounds
					of the array CPoleWeights.

					This function must only be used for rational surfaces.



#### <img src="images/Type_enum.svg" style="width:16px;"> setWeightRow

Modifies this B-Spline surface by assigning values to all or part of the
					weights of the row of poles of index UIndex of this B-Spline surface.

					The modified part of the row of weights is defined by the bounds of the
					array CPoleWeights.

					This function must only be used for rational surfaces.



#### <img src="images/Type_enum.svg" style="width:16px;"> tangent

tangent(u,v) -> (Vector,Vector)
Computes the tangent of parameter (u,v) on this geometry



#### <img src="images/Type_enum.svg" style="width:16px;"> toBSpline

Returns a B-Spline representation of this surface. 
					The optional arguments are:
					* tolerance (default=1e-7)
					* continuity in u (as string e.g. C0, G0, G1, C1, G2, C3, CN) (default='C1')
					* continuity in v (as string e.g. C0, G0, G1, C1, G2, C3, CN) (default='C1')
					* maximum degree in u (default=25)
					* maximum degree in v (default=25)
					* maximum number of segments (default=1000)
					* precision code (default=0)
					Will raise an exception if surface is infinite in U or V (like planes, cones or cylinders)



#### <img src="images/Type_enum.svg" style="width:16px;"> toShape

Return the shape for the geometry.



#### <img src="images/Type_enum.svg" style="width:16px;"> toShell

Make a shell of the surface.



#### <img src="images/Type_enum.svg" style="width:16px;"> transform

Applies a transformation to this geometric object



#### <img src="images/Type_enum.svg" style="width:16px;"> translate

Translates this geometric object



#### <img src="images/Type_enum.svg" style="width:16px;"> uIso

Builds the U isoparametric curve



#### <img src="images/Type_enum.svg" style="width:16px;"> vIso

Builds the V isoparametric curve



#### <img src="images/Type_enum.svg" style="width:16px;"> value

value(u,v) -> Point
Computes the point of parameter (u,v) on this surface









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > BSplineSurface API
