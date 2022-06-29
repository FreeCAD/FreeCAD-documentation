# Point API

Describes a point
To create a point there are several ways:
Part.Point()
    Creates a default point

Part.Point(Point)
    Creates a copy of the given point

Part.Point(Vector)
    Creates a line for the given coordinates



#### <img src="images/Type_enum.svg" style="width:16px;"> Content

Content of the object in XML representation.



#### <img src="images/Type_enum.svg" style="width:16px;"> MemSize

Memory size of the object in bytes.



#### <img src="images/Type_enum.svg" style="width:16px;"> Module

Module in which this class is defined



#### <img src="images/Type_enum.svg" style="width:16px;"> Tag

Gives the tag of the geometry as string.



#### <img src="images/Type_enum.svg" style="width:16px;"> TypeId

Is the type of the FreeCAD object with module domain



#### <img src="images/Type_enum.svg" style="width:16px;"> X

X component of this point.



#### <img src="images/Type_enum.svg" style="width:16px;"> Y

Y component of this point.



#### <img src="images/Type_enum.svg" style="width:16px;"> Z

Z component of this point.



#### <img src="images/Type_enum.svg" style="width:16px;"> clone

Create a clone of this geometry with the same Tag



#### <img src="images/Type_enum.svg" style="width:16px;"> copy

Create a copy of this geometry



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



#### <img src="images/Type_enum.svg" style="width:16px;"> getAllDerivedFrom

Returns all descendants



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



#### <img src="images/Type_enum.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/Type_enum.svg" style="width:16px;"> mirror

Performs the symmetrical transformation of this geometric object



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



#### <img src="images/Type_enum.svg" style="width:16px;"> setExtension

Sets a geometry extension of the indicated type.



#### <img src="images/Type_enum.svg" style="width:16px;"> toShape

Create a vertex from this point.



#### <img src="images/Type_enum.svg" style="width:16px;"> transform

Applies a transformation to this geometric object



#### <img src="images/Type_enum.svg" style="width:16px;"> translate

Translates this geometric object









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > Point API
