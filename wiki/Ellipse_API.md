# Ellipse API

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
			



#### <img src="images/Type_enum.svg" style="width:16px;"> AngleXU

The angle between the X axis and the major axis of the conic.



#### <img src="images/Type_enum.svg" style="width:16px;"> Axis

The axis direction of the circle



#### <img src="images/Type_enum.svg" style="width:16px;"> Center

Deprecated -- use Location.



#### <img src="images/Type_enum.svg" style="width:16px;"> Content

Content of the object in XML representation



#### <img src="images/Type_enum.svg" style="width:16px;"> Continuity


					Returns the global continuity of the curve.
				



#### <img src="images/Type_enum.svg" style="width:16px;"> Eccentricity


            returns the eccentricity value of the conic e.
            e = 0 for a circle
            0 < e < 1 for an ellipse  (e = 0 if MajorRadius = MinorRadius)
            e > 1 for a hyperbola
            e = 1 for a parabola
            



#### <img src="images/Type_enum.svg" style="width:16px;"> FirstParameter


					Returns the value of the first parameter.
				



#### <img src="images/Type_enum.svg" style="width:16px;"> Focal

The focal distance of the ellipse.



#### <img src="images/Type_enum.svg" style="width:16px;"> Focus1

The first focus is on the positive side of the major axis of the ellipse;
the second focus is on the negative side.



#### <img src="images/Type_enum.svg" style="width:16px;"> Focus2





#### <img src="images/Type_enum.svg" style="width:16px;"> LastParameter


					Returns the value of the last parameter.
				



#### <img src="images/Type_enum.svg" style="width:16px;"> Location

Location of the conic.



#### <img src="images/Type_enum.svg" style="width:16px;"> MajorRadius

The major radius of the ellipse.



#### <img src="images/Type_enum.svg" style="width:16px;"> MemSize

Memory size of the object in byte



#### <img src="images/Type_enum.svg" style="width:16px;"> MinorRadius

The minor radius of the ellipse.



#### <img src="images/Type_enum.svg" style="width:16px;"> Module

Module in which this class is defined



#### <img src="images/Type_enum.svg" style="width:16px;"> Rotation

Returns a rotation object to describe the orientation for curve that supports it



#### <img src="images/Type_enum.svg" style="width:16px;"> Tag

Gives the tag of the geometry as string.



#### <img src="images/Type_enum.svg" style="width:16px;"> TypeId

Is the type of the FreeCAD object with module domain



#### <img src="images/Type_enum.svg" style="width:16px;"> XAxis

The X axis direction of the circle



#### <img src="images/Type_enum.svg" style="width:16px;"> YAxis

The Y axis direction of the circle



#### <img src="images/Type_enum.svg" style="width:16px;"> approximateBSpline


					Approximates a curve of any type to a B-Spline curve
					approximateBSpline(Tolerance, MaxSegments, MaxDegree, [Order='C2']) -> B-Spline curve
				



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

Dumps the content of the object, both the XML representation as well as the additional datafiles  
required, into a byte representation. It will be returned as byte array.
dumpContent() -- returns a byte array with full content
dumpContent(Compression=1-9) -- Sets the data compression from 0 (no) to 9 (max)
                



#### <img src="images/Type_enum.svg" style="width:16px;"> getAllDerivedFrom

Returns all descendants



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



#### <img src="images/Type_enum.svg" style="width:16px;"> hasExtensionOfName

Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.



#### <img src="images/Type_enum.svg" style="width:16px;"> hasExtensionOfType

Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.



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


              Returns true if the curve is closed.
            



#### <img src="images/Type_enum.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/Type_enum.svg" style="width:16px;"> isPeriodic

Returns true if this curve is periodic.



#### <img src="images/Type_enum.svg" style="width:16px;"> length

Computes the length of a curve
length([uMin,uMax,Tol]) -> Float



#### <img src="images/Type_enum.svg" style="width:16px;"> makeRuledSurface

Make a ruled surface of this and the given curves



#### <img src="images/Type_enum.svg" style="width:16px;"> mirror

Performs the symmetrical transformation of this geometric object



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



#### <img src="images/Type_enum.svg" style="width:16px;"> restoreContent

Restore the content of the object from a byte representation as stored by "dumpContent".
It could be restored from any python object implementing the buffer protocol.
restoreContent(buffer) -- restores from the given byte array
                



#### <img src="images/Type_enum.svg" style="width:16px;"> reverse

Changes the direction of parametrization of the curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> reversedParameter

Returns the parameter on the reversed curve for
the point of parameter U on this curve.



#### <img src="images/Type_enum.svg" style="width:16px;"> rotate

Rotates this geometric object at angle Ang (in radians) about axis



#### <img src="images/Type_enum.svg" style="width:16px;"> scale

Applies a scaling transformation on this geometric object with a center and scaling factor



#### <img src="images/Type_enum.svg" style="width:16px;"> setExtension

Sets a geometry extension of the indicated type.



#### <img src="images/Type_enum.svg" style="width:16px;"> tangent

Computes the tangent of parameter u on this curve



#### <img src="images/Type_enum.svg" style="width:16px;"> toBSpline


					Converts a curve of any type (only part from First to Last)
					toBSpline([Float=First, Float=Last]) -> B-Spline curve
				



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
[documentation index](../README.md) > [API](Category_API.md) > Ellipse API
