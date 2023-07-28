# Object API

This is the father of all Feature classes



### Attributes

#### <img src="images/type_class.svg" style="width:16px;"> Proxy





#### <img src="images/type_class.svg" style="width:16px;"> [ViewObject](ViewObject_API.md)





### Functions

#### <img src="images/type_method.svg" style="width:16px;"> addExtension

Adds an extension to the object. Requires the string identifier for the python extension as argument



#### <img src="images/type_method.svg" style="width:16px;"> addProperty

addProperty(string, string) -- Add a generic property.
                    The first argument specifies the type, the second the
                    name of the property.



#### <img src="images/type_method.svg" style="width:16px;"> adjustRelativeLinks

adjustRelativeLinks(parent,recursive=True) -- auto correct potential cyclic dependencies



#### <img src="images/type_method.svg" style="width:16px;"> clearExpression

Clear the expression for a property



#### <img src="images/type_method.svg" style="width:16px;"> dumpContent

dumpContent(Compression=3) -> bytearray

Dumps the content of the object, both the XML representation and the additional
data files required, into a byte representation.

Compression : int
    Set the data compression level in the range [0,9]. Set to 0 for no compression.



#### <img src="images/type_method.svg" style="width:16px;"> dumpPropertyContent

dumpPropertyContent(Property, Compression=3) -> bytearray

Dumps the content of the property, both the XML representation and the additional
data files required, into a byte representation.

Property : str
    Property Name.
Compression : int
    Set the data compression level in the range [0, 9]. Set to 0 for no compression.



#### <img src="images/type_method.svg" style="width:16px;"> enforceRecompute

Mark the object for recompute



#### <img src="images/type_method.svg" style="width:16px;"> evalExpression

Evaluate an expression



#### <img src="images/type_method.svg" style="width:16px;"> getAllDerivedFrom

Returns all descendants



#### <img src="images/type_method.svg" style="width:16px;"> getDocumentationOfProperty

getDocumentationOfProperty(name) -> str

Returns the documentation string of the property of this class.

name : str
    Property name.



#### <img src="images/type_method.svg" style="width:16px;"> getEditorMode

getEditorMode(name) -> list

Get the behaviour of the property in the property editor.
It returns a list of strings with the current mode. If the list is empty there are no
special restrictions.
If the list contains 'ReadOnly' then the item appears in the property editor but is
disabled.
If the list contains 'Hidden' then the item even doesn't appear in the property editor.

name : str
    Property name.



#### <img src="images/type_method.svg" style="width:16px;"> getEnumerationsOfProperty

getEnumerationsOfProperty(name) -> list or  None

Return all enumeration strings of the property of this class or None if not a
PropertyEnumeration.

name : str
    Property name.



#### <img src="images/type_method.svg" style="width:16px;"> getGroupOfProperty

getGroupOfProperty(name) -> str

Returns the name of the group which the property belongs to in this class.
The properties are sorted in different named groups for convenience.

name : str
    Property name.



#### <img src="images/type_method.svg" style="width:16px;"> getLinkedObject

getLinkedObject(recursive=True, matrix=None, transform=True, depth=0)
Returns the linked object if there is one, or else return itself

* recursive: whether to recursively resolve the links

* transform: whether to transform the sub object using this object's placement

* matrix: If not none, this specifies the initial transformation to be applied
to the sub object. And cause the method to return a tuple (object, matrix)
containing the accumulated transformation matrix

* depth: current recursive depth



#### <img src="images/type_method.svg" style="width:16px;"> getParent

Returns the group the object is in or None if it is not part of a group.
                          Note that an object can only be in a single group, hence only a single return
                          value.
                          The parent can be a simple group as with getParentGroup() or a
                          GeoFeature group as with getParentGeoFeatureGroup().



#### <img src="images/type_method.svg" style="width:16px;"> getParentGeoFeatureGroup

Returns the GeoFeatureGroup, and hence the local coordinate system, the object 
                          is in or None if it is not part of a group. Note that an object can only be 
                          in a single group, hence only a single return value.



#### <img src="images/type_method.svg" style="width:16px;"> getParentGroup

Returns the group the object is in or None if it is not part of a group. 
                          Note that an object can only be in a single group, hence only a single return 
                          value.



#### <img src="images/type_method.svg" style="width:16px;"> getPathsByOutList

Get all paths from this object to another object following the OutList.



#### <img src="images/type_method.svg" style="width:16px;"> getPropertyByName

getPropertyByName(name, checkOwner=0) -> object or Tuple

Returns the value of a named property. Note that the returned property may not
always belong to this container (e.g. from a linked object).

name : str
     Name of the property.
checkOwner : int
    0: just return the property.
    1: raise exception if not found or the property does not belong to this container.
    2: return a tuple (owner, propertyValue).



#### <img src="images/type_method.svg" style="width:16px;"> getPropertyStatus

getPropertyStatus(name='') -> list

Get property status.

name : str
    Property name. If empty, returns a list of supported text names of the status.



#### <img src="images/type_method.svg" style="width:16px;"> getPropertyTouchList

getPropertyTouchList(name) -> tuple

Returns a list of index of touched values for list type properties.

name : str
    Property name.



#### <img src="images/type_method.svg" style="width:16px;"> getStatusString

Returns the status of the object as string.
If the object is invalid its error description will be returned.
If the object is valid but touched then 'Touched' will be returned,
'Valid' otherwise.



#### <img src="images/type_method.svg" style="width:16px;"> getSubObject

getSubObject(subname, retType=0, matrix=None, transform=True, depth=0)

* subname(string|list|tuple): dot separated string or sequence of strings
referencing subobject.

* retType: return type, 0=PyObject, 1=DocObject, 2=DocAndPyObject, 3=Placement

    PyObject: return a python binding object for the (sub)object referenced in
    each 'subname' The actual type of 'PyObject' is implementation dependent.
    For Part::Feature compatible objects, this will be of type TopoShapePy and
    pre-transformed by accumulated transformation matrix along the object path.  

    DocObject:  return the document object referenced in subname, if 'matrix' is
    None. Or, return a tuple (object, matrix) for each 'subname' and 'matrix' is
    the accumulated transformation matrix for the sub object.

    DocAndPyObject: return a tuple (object, matrix, pyobj) for each subname

    Placement: return a transformed placement of the sub-object

* matrix: the initial transformation to be applied to the sub object.

* transform: whether to transform the sub object using this object's placement

* depth: current recursive depth



#### <img src="images/type_method.svg" style="width:16px;"> getSubObjectList

getSubObjectList(subname)

Return a list of objects referenced by a given subname including this object



#### <img src="images/type_method.svg" style="width:16px;"> getSubObjects

Return subname reference of all sub-objects



#### <img src="images/type_method.svg" style="width:16px;"> getTypeIdOfProperty

getTypeIdOfProperty(name) -> str

Returns the C++ class name of a named property.

name : str
    Property name.



#### <img src="images/type_method.svg" style="width:16px;"> getTypeOfProperty

getTypeOfProperty(name) -> list

Returns the type of a named property. This can be a list conformed by elements in
(Hidden, NoRecompute, NoPersist, Output, ReadOnly, Transient).

name : str
    Property name.



#### <img src="images/type_method.svg" style="width:16px;"> hasChildElement

Return true to indicate the object having child elements



#### <img src="images/type_method.svg" style="width:16px;"> hasExtension

Returns if this object has the specified extension



#### <img src="images/type_method.svg" style="width:16px;"> isDerivedFrom

Returns true if given type is a father



#### <img src="images/type_method.svg" style="width:16px;"> isElementVisible

Check if a child element is visible
Return -1 if element visibility is not supported or element not found, 0 if invisible, or else 1



#### <img src="images/type_method.svg" style="width:16px;"> isValid

Returns True if the object is valid, False otherwise



#### <img src="images/type_method.svg" style="width:16px;"> purgeTouched

Mark the object as unchanged



#### <img src="images/type_method.svg" style="width:16px;"> recompute

Recomputes this object



#### <img src="images/type_method.svg" style="width:16px;"> removeProperty

removeProperty(string) -- Remove a generic property.
                    Note, you can only remove user-defined properties but not built-in ones.



#### <img src="images/type_method.svg" style="width:16px;"> resolve

resolve(subname) -- resolve the sub object

Returns a tuple (subobj,parent,elementName,subElement), where 'subobj' is the
last object referenced in 'subname', and 'parent' is the direct parent of
'subobj', and 'elementName' is the name of the subobj, which can be used
to call parent.isElementVisible/setElementVisible(). 'subElement' is the
non-object sub-element name if any.



#### <img src="images/type_method.svg" style="width:16px;"> resolveSubElement

resolveSubElement(subname,append,type) -- resolve both new and old style sub element

subname: subname reference containing object hierarchy
append: Whether to append object hierarchy prefix inside subname to returned element name
type: 0: normal, 1: for import, 2: for export

Return tuple(obj,newElementName,oldElementName)



#### <img src="images/type_method.svg" style="width:16px;"> restoreContent

restoreContent(obj) -> None

Restore the content of the object from a byte representation as stored by `dumpContent`.
It could be restored from any Python object implementing the buffer protocol.

obj : buffer
    Object with buffer protocol support.



#### <img src="images/type_method.svg" style="width:16px;"> restorePropertyContent

restorePropertyContent(name, obj) -> None

Restore the content of the object from a byte representation as stored by `dumpPropertyContent`.
It could be restored from any Python object implementing the buffer protocol.

name : str
    Property name.
obj : buffer
    Object with buffer protocol support.



#### <img src="images/type_method.svg" style="width:16px;"> setDocumentationOfProperty

setDocumentationOfProperty(name, docstring) -> None

Set the documentation string of a dynamic property of this class.

name : str
    Property name.
docstring : str
    Documentation string.



#### <img src="images/type_method.svg" style="width:16px;"> setEditorMode

setEditorMode(name, type) -> None

Set the behaviour of the property in the property editor.

name : str
    Property name.
type : int, sequence of str
    Property type.
    0: default behaviour. 1: item is ready-only. 2: item is hidden. 3: item is hidden and read-only.
    If sequence, the available items are 'ReadOnly' and 'Hidden'.



#### <img src="images/type_method.svg" style="width:16px;"> setElementVisible

Set the visibility of a child element
Return -1 if element visibility is not supported, 0 if element not found, 1 if success



#### <img src="images/type_method.svg" style="width:16px;"> setExpression

Register an expression for a property



#### <img src="images/type_method.svg" style="width:16px;"> setGroupOfProperty

setGroupOfProperty(name, group) -> None

Set the name of the group of a dynamic property.

name : str
    Property name.
group : str
    Group name.



#### <img src="images/type_method.svg" style="width:16px;"> setPropertyStatus

setPropertyStatus(name, val) -> None

Set property status.

name : str
    Property name.
val : int, str, sequence of str or int
    Call getPropertyStatus() to get a list of supported text value.
    If the text start with '-' or the integer value is negative, then the status is cleared.



#### <img src="images/type_method.svg" style="width:16px;"> supportedProperties

A list of supported property types



#### <img src="images/type_method.svg" style="width:16px;"> touch

Mark the object as changed (touched)



#### <img src="images/Type_enum.svg" style="width:16px;"> Content

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> Document

This is a Document class



#### <img src="images/Type_enum.svg" style="width:16px;"> ExpressionEngine

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> FullName

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> ID

int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4



#### <img src="images/Type_enum.svg" style="width:16px;"> InList

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> InListRecursive

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> Label

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> Label2

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> MemSize

int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4



#### <img src="images/Type_enum.svg" style="width:16px;"> Module

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> MustExecute

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.



#### <img src="images/Type_enum.svg" style="width:16px;"> Name

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> NoTouch

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.



#### <img src="images/Type_enum.svg" style="width:16px;"> OldLabel

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> OutList

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> OutListRecursive

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> Parents

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> PropertiesList

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> Removing

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.



#### <img src="images/Type_enum.svg" style="width:16px;"> State

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> TypeId

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> Visibility

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Object API
