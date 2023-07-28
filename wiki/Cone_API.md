# Cone API

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
			



#### <img src="images/BIM_Column.svg" style="width:16px;"> Apex

Compute the apex of the cone.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Axis

The axis direction of the cone



#### <img src="images/BIM_Column.svg" style="width:16px;"> Center

Center of the cone.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Content

Content of the object in XML representation.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Continuity

Returns the global continuity of the surface.



#### <img src="images/BIM_Column.svg" style="width:16px;"> MemSize

Memory size of the object in bytes.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Module

Module in which this class is defined



#### <img src="images/BIM_Column.svg" style="width:16px;"> Radius

The radius of the cone.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Rotation

Returns a rotation object to describe the orientation for surface that supports it



#### <img src="images/BIM_Column.svg" style="width:16px;"> SemiAngle

The semi-angle of the cone.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Tag

Gives the tag of the geometry as string.



#### <img src="images/BIM_Column.svg" style="width:16px;"> TypeId

Is the type of the FreeCAD object with module domain



#### <img src="images/BIM_Column.svg" style="width:16px;"> UPeriod

Returns the period of this patch in the u parametric direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> VPeriod

Returns the period of this patch in the v parametric direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> bounds

Returns the parametric bounds (U1, U2, V1, V2) of this trimmed surface.



#### <img src="images/BIM_Column.svg" style="width:16px;"> clone

Create a clone of this geometry with the same Tag



#### <img src="images/BIM_Column.svg" style="width:16px;"> copy

Create a copy of this geometry



#### <img src="images/BIM_Column.svg" style="width:16px;"> curvature

curvature(u,v,type) -> float
The value of type must be one of this: Max, Min, Mean or Gauss
Computes the curvature of parameter (u,v) on this geometry



#### <img src="images/BIM_Column.svg" style="width:16px;"> curvatureDirections

curvatureDirections(u,v) -> (Vector,Vector)
Computes the directions of maximum and minimum curvature
of parameter (u,v) on this geometry.
The first vector corresponds to the maximum curvature,
the second vector corresponds to the minimum curvature.



#### <img src="images/BIM_Column.svg" style="width:16px;"> deleteExtensionOfName

Deletes all extensions of the indicated name.



#### <img src="images/BIM_Column.svg" style="width:16px;"> deleteExtensionOfType

Deletes all extensions of the indicated type.



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



#### <img src="images/BIM_Column.svg" style="width:16px;"> getDN

Returns the n-th derivative



#### <img src="images/BIM_Column.svg" style="width:16px;"> getExtensionOfName

Gets the first geometry extension of the name indicated by the string.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getExtensionOfType

Gets the first geometry extension of the type indicated by the string.



#### <img src="images/BIM_Column.svg" style="width:16px;"> getExtensions

Returns a list with information about the geometry extensions.



#### <img src="images/BIM_Column.svg" style="width:16px;"> hasExtensionOfName

Returns a boolean indicating whether a geometry extension with the name indicated as a string exists.



#### <img src="images/BIM_Column.svg" style="width:16px;"> hasExtensionOfType

Returns a boolean indicating whether a geometry extension of the type indicated as a string exists.



#### <img src="images/BIM_Column.svg" style="width:16px;"> intersect

Returns all intersection points/curves between the surface and the curve/surface.



#### <img src="images/BIM_Column.svg" style="width:16px;"> intersectSS

Returns all intersection curves of this surface and the given surface.
The required arguments are:
* Second surface
* precision code (optional, default=0)



#### <img src="images/BIM_Column.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/BIM_Column.svg" style="width:16px;"> isPlanar

isPlanar([float]) -> Bool
Checks if the surface is planar within a certain tolerance.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isUClosed

Checks if this surface is closed in the u parametric direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isUPeriodic

Returns true if this patch is periodic in the given parametric direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isUmbillic

isUmbillic(u,v) -> bool
Check if the geometry on parameter is an umbillic point,
i.e. maximum and minimum curvature are equal.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isVClosed

Checks if this surface is closed in the v parametric direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> isVPeriodic

Returns true if this patch is periodic in the given parametric direction.



#### <img src="images/BIM_Column.svg" style="width:16px;"> mirror

Performs the symmetrical transformation of this geometric object



#### <img src="images/BIM_Column.svg" style="width:16px;"> normal

normal(u,v) -> Vector
Computes the normal of parameter (u,v) on this geometry



#### <img src="images/BIM_Column.svg" style="width:16px;"> parameter

Returns the parameter on the curve
of the nearest orthogonal projection of the point.



#### <img src="images/BIM_Column.svg" style="width:16px;"> projectPoint

Computes the projection of a point on the surface

projectPoint(Point=Vector,[Method="NearestPoint"])
projectPoint(Vector,"NearestPoint") -> Vector
projectPoint(Vector,"LowerDistance") -> float
projectPoint(Vector,"LowerDistanceParameters") -> tuple of floats (u,v)
projectPoint(Vector,"Distance") -> list of floats
projectPoint(Vector,"Parameters") -> list of tuples of floats
projectPoint(Vector,"Point") -> list of points



#### <img src="images/BIM_Column.svg" style="width:16px;"> restoreContent

restoreContent(obj) -> None

Restore the content of the object from a byte representation as stored by `dumpContent`.
It could be restored from any Python object implementing the buffer protocol.

obj : buffer
    Object with buffer protocol support.



#### <img src="images/BIM_Column.svg" style="width:16px;"> rotate

Rotates this geometric object at angle Ang (in radians) about axis



#### <img src="images/BIM_Column.svg" style="width:16px;"> scale

Applies a scaling transformation on this geometric object with a center and scaling factor



#### <img src="images/BIM_Column.svg" style="width:16px;"> setExtension

Sets a geometry extension of the indicated type.



#### <img src="images/BIM_Column.svg" style="width:16px;"> tangent

tangent(u,v) -> (Vector,Vector)
Computes the tangent of parameter (u,v) on this geometry



#### <img src="images/BIM_Column.svg" style="width:16px;"> toBSpline

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



#### <img src="images/BIM_Column.svg" style="width:16px;"> toShape

Return the shape for the geometry.



#### <img src="images/BIM_Column.svg" style="width:16px;"> toShell

Make a shell of the surface.



#### <img src="images/BIM_Column.svg" style="width:16px;"> transform

Applies a transformation to this geometric object



#### <img src="images/BIM_Column.svg" style="width:16px;"> translate

Translates this geometric object



#### <img src="images/BIM_Column.svg" style="width:16px;"> uIso

Builds the U isoparametric curve



#### <img src="images/BIM_Column.svg" style="width:16px;"> vIso

Builds the V isoparametric curve



#### <img src="images/BIM_Column.svg" style="width:16px;"> value

value(u,v) -> Point
Computes the point of parameter (u,v) on this surface









---
![](images/Button_right.png) [documentation index](../README.md) > [API](Category_API.md) > Cone API
