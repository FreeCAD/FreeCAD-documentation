# Vector API

This class represents a 3D float vector



#### <img src="images/Type_enum.svg" style="width:16px;"> Length

Length([Float]) -> Float
						  gets or sets the length of this vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> add

add(Vector)
					      returns the sum of this and another vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> cross

cross(Vector)
					      returns the cross product between this and another vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> distanceToLine

distanceToLine(Vector,Vector)
						  returns the distance between this vector and a line defined by
						  a base point and a direction
				



#### <img src="images/Type_enum.svg" style="width:16px;"> distanceToLineSegment

distanceToLineSegment(Vector,Vector)
						  returns the distance between this vector and a line segment defined by
						  a base point and a direction
				



#### <img src="images/Type_enum.svg" style="width:16px;"> distanceToPlane

distanceToPlane(Vector,Vector)
						  returns the distance between this vector and a plane defined by
						  a base point and a normal
				



#### <img src="images/Type_enum.svg" style="width:16px;"> distanceToPoint


					distanceToPoint(Vector)
					returns the distance to another point
				



#### <img src="images/Type_enum.svg" style="width:16px;"> dot

dot(Vector)
						  returns the dot product of the this vector with another one
				



#### <img src="images/Type_enum.svg" style="width:16px;"> getAngle

getAngle(Vector)
					      returns the angle in radians between this and another vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> isEqual

isEqual(Vector, tolerance) -> Boolean
                          If the distance to the given point is less or equal to the tolerance
                          bith points are considered equal.
                



#### <img src="images/Type_enum.svg" style="width:16px;"> isOnLineSegment

isOnLineSegment(Vector, Vector)
					      checks if Vector is on a line segment
				



#### <img src="images/Type_enum.svg" style="width:16px;"> multiply

multiply(Float)
					      multiplies (scales) this vector by a single factor
				



#### <img src="images/Type_enum.svg" style="width:16px;"> negative

negative()
					      returns the negative (opposite) of this vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> normalize

normalize()
						  normalizes the vector to the length of 1.0
				



#### <img src="images/Type_enum.svg" style="width:16px;"> projectToLine

projectToLine(Vector pnt,Vector vec)
						  Projects the point 'pnt' on a line that goes through the origin with the direction vector 'vec'.
						  The result is the vector from point 'pnt' to the projected point.
						  NOTE: The result does not depend on the vector instance 'self'.
						  NOTE: This method modifies the vector instance 'self'.
				



#### <img src="images/Type_enum.svg" style="width:16px;"> projectToPlane

projectToPlane(Vector,Vector)
						  projects the vector on a plane defined by a base point and a normal
				



#### <img src="images/Type_enum.svg" style="width:16px;"> scale

scale(Float,Float,Float)
					      scales (multiplies) this vector by a factor
			    



#### <img src="images/Type_enum.svg" style="width:16px;"> sub

sub(Vector)
					      returns the difference of this and another vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> x

x([Float]) -> Float
						  gets or sets the X component of this vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> y

y([Float]) -> Float
						  gets or sets the Y component of this vector
				



#### <img src="images/Type_enum.svg" style="width:16px;"> z

z([Float]) -> Float
						  gets or sets the Z component of this vector
				







---
[documentation index](../README.md) > [API](Category_API.md) > Vector API
