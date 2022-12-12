# Placement API

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



#### <img src="images/Type_enum.svg" style="width:16px;"> [Base](Base_API.md)

Vector to the Base Position of the Placement.



#### <img src="images/Type_enum.svg" style="width:16px;"> [Matrix](Matrix_API.md)

Set/get matrix representation of the placement.



#### <img src="images/Type_enum.svg" style="width:16px;"> Rotation

Orientation of the placement expressed as rotation.



#### <img src="images/Type_enum.svg" style="width:16px;"> copy

copy() -> Base.Placement

Returns a copy of this placement.



#### <img src="images/Type_enum.svg" style="width:16px;"> inverse

inverse() -> Base.Placement

Compute the inverse placement.



#### <img src="images/Type_enum.svg" style="width:16px;"> isIdentity

isIdentity() -> bool

Returns True if the placement has no displacement and no rotation.
Matrix representation is the 4D identity matrix.



#### <img src="images/Type_enum.svg" style="width:16px;"> isSame

isSame(Base.Placement, [tol=0.0]) -> bool

Checks whether this and the given placement are the same.
The default tolerance is set to 0.0



#### <img src="images/Type_enum.svg" style="width:16px;"> move

move(vector) -> None

Move the placement along a vector.

vector : Base.Vector
    Vector by which to move the placement.



#### <img src="images/Type_enum.svg" style="width:16px;"> multVec

multVec(vector) -> Base.Vector

Compute the transformed vector using the placement.

vector : Base.Vector
    Vector to be transformed.



#### <img src="images/Type_enum.svg" style="width:16px;"> multiply

multiply(placement) -> Base.Placement

Right multiply this placement with another placement.
Also available as `*` operator.

placement : Base.Placement
    Placement by which to multiply this placement.



#### <img src="images/Type_enum.svg" style="width:16px;"> pow

pow(t, shorten=True) -> Base.Placement

Raise this placement to real power using ScLERP interpolation.
Also available as `**` operator.

t : float
    Real power.
shorten : bool
    If True, ensures rotation quaternion is net positive to make
    the path shorter.



#### <img src="images/Type_enum.svg" style="width:16px;"> rotate

rotate(center, axis, angle, comp) -> None

Rotate the current placement around center and axis with the given angle.
This method is compatible with TopoShape.rotate() if the (optional) keyword
argument comp is True (default=False).

center : Base.Vector, sequence of float
    Rotation center.
axis : Base.Vector, sequence of float
    Rotation axis.
angle : float
    Rotation angle in degrees.
comp : bool
    optional keyword only argument, if True (default=False),
behave like TopoShape.rotate() (i.e. the resulting placements are interchangeable).



#### <img src="images/Type_enum.svg" style="width:16px;"> sclerp

sclerp(placement2, t, shorten=True) -> Base.Placement

Screw Linear Interpolation (ScLERP) between this placement and `placement2`.
Interpolation is a continuous motion along a helical path parametrized by `t`
made of equal transforms if discretized.
If quaternions of rotations of the two placements differ in sign, the interpolation
will take a long path.

placement2 : Base.Placement
t : float
    Parameter of helical path. t=0 returns this placement, t=1 returns
    `placement2`. t can also be outside of [0, 1] range for extrapolation.
shorten : bool
    If True, the signs are harmonized before interpolation and the interpolation
    takes the shorter path.



#### <img src="images/Type_enum.svg" style="width:16px;"> slerp

slerp(placement2, t) -> Base.Placement

Spherical Linear Interpolation (SLERP) between this placement and `placement2`.
This function performs independent interpolation of rotation and movement.
Result of such interpolation might be not what application expects, thus this tool
might be considered for simple cases or for interpolating between small intervals.
For more complex cases you better use the advanced sclerp() function.

placement2 : Base.Placement
t : float
    Parameter of the path. t=0 returns this placement, t=1 returns `placement2`.



#### <img src="images/Type_enum.svg" style="width:16px;"> toMatrix

toMatrix() -> Base.Matrix

Compute the matrix representation of the placement.



#### <img src="images/Type_enum.svg" style="width:16px;"> translate

translate(vector) -> None

Alias to move(), to be compatible with TopoShape.translate().

vector : Base.Vector
    Vector by which to move the placement.









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Placement API
