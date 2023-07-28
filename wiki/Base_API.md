# Base API

The Base module contains the classes for the geometric basics
like vector, matrix, bounding box, placement, rotation, axis, ...




#### <img src="images/Type_enum.svg" style="width:16px;"> Axis

Base.Axis class.

An Axis defines a direction and a position (base) in 3D space.

The following constructors are supported:

Axis()
Empty constructor.

Axis(axis)
Copy constructor.
axis : Base.Axis

Axis(base, direction)
Define from a position and a direction.
base : Base.Vector
direction : Base.Vector



#### <img src="images/Type_enum.svg" style="width:16px;"> BadFormatError





#### <img src="images/Type_enum.svg" style="width:16px;"> BadGraphError





#### <img src="images/Type_enum.svg" style="width:16px;"> BoundBox

Base.BoundBox class.

This class represents a bounding box.
A bounding box is a rectangular cuboid which is a way to describe outer
boundaries and is obtained from a lot of 3D types.
It is often used to check if a 3D entity lies in the range of another object.
Checking for bounding interference first can save a lot of computing time!
An invalid BoundBox is represented by inconsistent values at each direction:
The maximum float value of the system at the minimum coordinates, and the
opposite value at the maximum coordinates.

The following constructors are supported:

BoundBox()
Empty constructor. Returns an invalid BoundBox.

BoundBox(boundBox)
Copy constructor.
boundBox : Base.BoundBox

BoundBox(xMin, yMin=0, zMin=0, xMax=0, yMax=0, zMax=0)
Define from the minimum and maximum values at each direction.
xMin : float
    Minimum value at x-coordinate.
yMin : float
    Minimum value at y-coordinate.
zMin : float
    Minimum value at z-coordinate.
xMax : float
    Maximum value at x-coordinate.
yMax : float
    Maximum value at y-coordinate.
zMax : float
    Maximum value at z-coordinate.

App.BoundBox(min, max)
Define from two containers representing the minimum and maximum values of the
coordinates in each direction.
min : Base.Vector, tuple
    Minimum values of the coordinates.
max : Base.Vector, tuple
    Maximum values of the coordinates.



#### <img src="images/Type_enum.svg" style="width:16px;"> CADKernelError





#### <img src="images/Type_enum.svg" style="width:16px;"> CoordinateSystem

Base.CoordinateSystem class.

An orthonormal right-handed coordinate system in 3D space.

CoordinateSystem()
Empty constructor.



#### <img src="images/Type_enum.svg" style="width:16px;"> ExpressionError





#### <img src="images/Type_enum.svg" style="width:16px;"> FreeCADAbort





#### <img src="images/Type_enum.svg" style="width:16px;"> FreeCADError





#### <img src="images/Type_enum.svg" style="width:16px;"> [Matrix](Matrix_API.md)

Base.Matrix class.

A 4x4 Matrix.
In particular, this matrix can represent an affine transformation, that is,
given a 3D vector `x`, apply the transformation y = M*x + b, where the matrix
`M` is a linear map and the vector `b` is a translation.
`y` can be obtained using a linear transformation represented by the 4x4 matrix
`A` conformed by the augmented 3x4 matrix (M|b), augmented by row with
(0,0,0,1), therefore: (y, 1) = A*(x, 1).

The following constructors are supported:

Matrix()
Empty constructor.

Matrix(matrix)
Copy constructor.
matrix : Base.Matrix.

Matrix(*coef)
Define from 16 coefficients of the 4x4 matrix.
coef : sequence of float
    The sequence can have up to 16 elements which complete the matrix by rows.

Matrix(vector1, vector2, vector3, vector4)
Define from four 3D vectors which represent the columns of the 3x4 submatrix,
useful to represent an affine transformation. The fourth row is made up by
(0,0,0,1).
vector1 : Base.Vector
vector2 : Base.Vector
vector3 : Base.Vector
vector4 : Base.Vector
    Default to (0,0,0). Optional.



#### <img src="images/Type_enum.svg" style="width:16px;"> ParserError





#### <img src="images/Type_enum.svg" style="width:16px;"> [Placement](Placement_API.md)

Base.Placement class.

A Placement defines an orientation (rotation) and a position (base) in 3D space.
It is used when no scaling or other distortion is needed.

The following constructors are supported:

Placement()
Empty constructor.

Placement(placement)
Copy constructor.
placement : Base.Placement

Placement(matrix)
Define from a 4D matrix consisting of rotation and translation.
matrix : Base.Matrix

Placement(base, rotation)
Define from position and rotation.
base : Base.Vector
rotation : Base.Rotation

Placement(base, rotation, center)
Define from position and rotation with center.
base : Base.Vector
rotation : Base.Rotation
center : Base.Vector

Placement(base, axis, angle)
define position and rotation.
base : Base.Vector
axis : Base.Vector
angle : float



#### <img src="images/Type_enum.svg" style="width:16px;"> Precision

This is the Precision class



#### <img src="images/Type_enum.svg" style="width:16px;"> ProgressIndicator

Progress indicator



#### <img src="images/Type_enum.svg" style="width:16px;"> Rotation

Base.Rotation class.

A Rotation using a quaternion.

The following constructors are supported:

Rotation()
Empty constructor.

Rotation(rotation)
Copy constructor.

Rotation(Axis, Radian)
Rotation(Axis, Degree)
Define from an axis and an angle (in radians or degrees according to the keyword).
Axis : Base.Vector
Radian : float
Degree : float

Rotation(vector_start, vector_end)
Define from two vectors (rotation from/to vector).
vector_start : Base.Vector
vector_end : Base.Vector

Rotation(angle1, angle2, angle3)
Define from three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention.
angle1 : float
angle2 : float
angle3 : float

Rotation(seq, angle1, angle2, angle3)
Define from one string and three floats (Euler angles) as Euler rotation
of a given type. Call toEulerAngles() for supported sequence types.
seq : str
angle1 : float
angle2 : float
angle3 : float

Rotation(x, y, z, w)
Define from four floats (quaternion) where the quaternion is specified as:
q = xi+yj+zk+w, i.e. the last parameter is the real part.
x : float
y : float
z : float
w : float

Rotation(dir1, dir2, dir3, seq)
Define from three vectors that define rotated axes directions plus an optional
3-characher string of capital letters 'X', 'Y', 'Z' that sets the order of
importance of the axes (e.g., 'ZXY' means z direction is followed strictly,
x is used but corrected if necessary, y is ignored).
dir1 : Base.Vector
dir2 : Base.Vector
dir3 : Base.Vector
seq : str

Rotation(matrix)
Define from a matrix rotation in the 4D representation.
matrix : Base.Matrix

Rotation(*coef)
Define from 16 or 9 elements which represent the rotation in the 4D matrix
representation or in the 3D matrix representation, respectively.
coef : sequence of float



#### <img src="images/Type_enum.svg" style="width:16px;"> TypeId

Base.BaseType class.

This class is not intended to create instances of itself, but to get information
from the different types and create instances of them.
Regarding instantiation, this is possible in cases that inherit from the
Base::BaseClass class and are not abstract classes.



#### <img src="images/Type_enum.svg" style="width:16px;"> UnknownProgramOption





#### <img src="images/Type_enum.svg" style="width:16px;"> [Vector](Vector_API.md)

Base.Vector class.

This class represents a 3D float vector.
Useful to represent points in the 3D space.

The following constructors are supported:

Vector(x=0, y=0, z=0)
x : float
y : float
z : float

Vector(vector)
Copy constructor.
vector : Base.Vector

Vector(seq)
Define from a sequence of float.
seq : sequence of float.



#### <img src="images/Type_enum.svg" style="width:16px;"> Vector2d

Vector2d class



#### <img src="images/Type_enum.svg" style="width:16px;"> XMLAttributeError





#### <img src="images/Type_enum.svg" style="width:16px;"> XMLBaseException





#### <img src="images/Type_enum.svg" style="width:16px;"> XMLParseException











---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Base API
