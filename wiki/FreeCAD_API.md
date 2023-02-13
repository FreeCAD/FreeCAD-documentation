# FreeCAD API

The functions in the FreeCAD module allow working with documents.
The FreeCAD instance provides a list of references of documents which
can be addressed by a string. Hence the document name must be unique.

The document has the read-only attribute FileName which points to the
file the document should be stored to.




### Attributes

#### <img src="images/type_class.svg" style="width:16px;"> PropertyType <small>(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)</small>





#### <img src="images/type_class.svg" style="width:16px;"> ScaleType <small>(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)</small>





### Functions

#### <img src="images/type_method.svg" style="width:16px;"> ConfigDump

Dump the configuration to the output.



#### <img src="images/type_method.svg" style="width:16px;"> ConfigGet

ConfigGet(string) -- Get the value for the given key.



#### <img src="images/type_method.svg" style="width:16px;"> ConfigSet

ConfigSet(string, string) -- Set the given key to the given value.



#### <img src="images/type_method.svg" style="width:16px;"> ParamGet

Get parameters by path



#### <img src="images/type_method.svg" style="width:16px;"> Version

Print the version to the output.



#### <img src="images/type_method.svg" style="width:16px;"> activeDocument

activeDocument() -> object or None

Return the active document or None if there is no one.



#### <img src="images/type_method.svg" style="width:16px;"> addDocumentObserver

addDocumentObserver() -> None

Add an observer to get notified about changes on documents.



#### <img src="images/type_method.svg" style="width:16px;"> addExportType

Register filetype for export



#### <img src="images/type_method.svg" style="width:16px;"> addImportType

Register filetype for import



#### <img src="images/type_method.svg" style="width:16px;"> changeExportModule

Change the export module name of a registered filetype



#### <img src="images/type_method.svg" style="width:16px;"> changeImportModule

Change the import module name of a registered filetype



#### <img src="images/type_method.svg" style="width:16px;"> checkAbort

checkAbort() -- check for user abort in length operation.

This only works if there is an active sequencer (or ProgressIndicator in Python).
There is an active sequencer during document restore and recomputation. User may
abort the operation by pressing the ESC key. Once detected, this function will
trigger a Base.FreeCADAbort exception.



#### <img src="images/type_method.svg" style="width:16px;"> checkLinkDepth

checkLinkDepth(depth) -- check link recursion depth



#### <img src="images/type_method.svg" style="width:16px;"> closeActiveTransaction

closeActiveTransaction(abort=False) -- commit or abort current active transaction



#### <img src="images/type_method.svg" style="width:16px;"> closeDocument

closeDocument(string) -> None

Close the document with a given name.



#### <img src="images/type_method.svg" style="width:16px;"> getActiveTransaction

getActiveTransaction() -> (name,id) return the current active transaction name and ID



#### <img src="images/type_method.svg" style="width:16px;"> getDependentObjects

getDependentObjects(obj|[obj,...], options=0)
Return a list of dependent objects including the given objects.

options: can have the following bit flags,
         1: to sort the list in topological order.
         2: to exclude dependency of Link type object.



#### <img src="images/type_method.svg" style="width:16px;"> getDocument

getDocument(string) -> object

Get a document by its name or raise an exception
if there is no document with the given name.



#### <img src="images/type_method.svg" style="width:16px;"> getExportType

Get the name of the module that can export the filetype



#### <img src="images/type_method.svg" style="width:16px;"> getHelpDir

Get the directory of the documentation



#### <img src="images/type_method.svg" style="width:16px;"> getHomePath

Get the home path, i.e. the parent directory of the executable



#### <img src="images/type_method.svg" style="width:16px;"> getImportType

Get the name of the module that can import the filetype



#### <img src="images/type_method.svg" style="width:16px;"> getLibraryDir

Get the directory of all extension modules



#### <img src="images/type_method.svg" style="width:16px;"> getLinksTo

getLinksTo(obj,options=0,maxCount=0) -- return the objects linked to 'obj'

options: 1: recursive, 2: check link array. Options can combine.
maxCount: to limit the number of links returned



#### <img src="images/type_method.svg" style="width:16px;"> getLogLevel

getLogLevel(tag) -- Get the log level of a string tag



#### <img src="images/type_method.svg" style="width:16px;"> getResourceDir

Get the root directory of all resources



#### <img src="images/type_method.svg" style="width:16px;"> getTempPath

Get the root directory of cached files



#### <img src="images/type_method.svg" style="width:16px;"> getUserAppDataDir

Get the root directory of application data



#### <img src="images/type_method.svg" style="width:16px;"> getUserCachePath

Get the root path of cached files



#### <img src="images/type_method.svg" style="width:16px;"> getUserConfigDir

Get the root path of user config files



#### <img src="images/type_method.svg" style="width:16px;"> getUserMacroDir

getUserMacroDir(bool=False) -> stringGet the directory of the user's macro directory
If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path.



#### <img src="images/type_method.svg" style="width:16px;"> isRestoring

isRestoring() -> Bool -- Test if the application is opening some document



#### <img src="images/type_method.svg" style="width:16px;"> listDocuments

listDocuments(sort=False) -> list

Return a list of names of all documents, optionally sort in dependency order.



#### <img src="images/type_method.svg" style="width:16px;"> loadFile

loadFile(string=filename,[string=module]) -> None

Loads an arbitrary file by delegating to the given Python module:
* If no module is given it will be determined by the file extension.
* If more than one module can load a file the first one will be taken.
* If no module exists to load the file an exception will be raised.



#### <img src="images/type_method.svg" style="width:16px;"> newDocument

newDocument(name, label=None, hidden=False, temp=False) -> object
Create a new document with a given name.

name: unique document name which is checked automatically.
label: optional user changeable label for the document.
hidden: whether to hide document 3D view.
temp: mark the document as temporary so that it will not be saved



#### <img src="images/type_method.svg" style="width:16px;"> open

See openDocument(string)



#### <img src="images/type_method.svg" style="width:16px;"> openDocument

openDocument(filepath,hidden=False) -> object
Create a document and load the project file into the document.

filepath: file path to an existing file. If the file doesn't exist
          or the file cannot be loaded an I/O exception is thrown.
          In this case the document is kept alive.
hidden: whether to hide document 3D view.



#### <img src="images/type_method.svg" style="width:16px;"> removeDocumentObserver

removeDocumentObserver() -> None

Remove an added document observer.



#### <img src="images/type_method.svg" style="width:16px;"> saveParameter

saveParameter(config='User parameter') -> None
Save parameter set to file. The default set is 'User parameter'



#### <img src="images/type_method.svg" style="width:16px;"> setActiveDocument

setActiveDocement(string) -> None

Set the active document by its name.



#### <img src="images/type_method.svg" style="width:16px;"> setActiveTransaction

setActiveTransaction(name, persist=False) -- setup active transaction with the given name

name: the transaction name
persist(False): by default, if the calling code is inside any invocation of a command, it
                will be auto closed once all commands within the current stack exists. To
                disable auto closing, set persist=True
Returns the transaction ID for the active transaction. An application-wide
active transaction causes any document changes to open a transaction with
the given name and ID.



#### <img src="images/type_method.svg" style="width:16px;"> setLogLevel

setLogLevel(tag, level) -- Set the log level for a string tag.
'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value



#### <img src="images/Type_enum.svg" style="width:16px;"> ActiveDocument

This is a Document class



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



#### <img src="images/Type_enum.svg" style="width:16px;"> Document

This is a Document class



#### <img src="images/Type_enum.svg" style="width:16px;"> DocumentObject

This is the father of all classes handled by the document



#### <img src="images/Type_enum.svg" style="width:16px;"> DocumentObjectExtension

Base class for all document object extensions



#### <img src="images/Type_enum.svg" style="width:16px;"> DocumentObjectGroup

This class handles document objects in group



#### <img src="images/Type_enum.svg" style="width:16px;"> Extension

Base class for all extensions



#### <img src="images/Type_enum.svg" style="width:16px;"> ExtensionContainer

Base class for all objects which can be extended



#### <img src="images/Type_enum.svg" style="width:16px;"> GeoFeature

App.GeoFeature class.

Base class of all geometric document objects.
This class does the whole placement and position handling.
With the method `getPropertyOfGeometry` is possible to obtain
the main geometric property in general form, without reference
to any particular property name.



#### <img src="images/Type_enum.svg" style="width:16px;"> GeoFeatureGroupExtension

This class handles placeable group of document objects



#### <img src="images/Type_enum.svg" style="width:16px;"> GroupExtension

Extension class which allows grouping of document objects



#### <img src="images/Type_enum.svg" style="width:16px;"> GuiUp

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



#### <img src="images/Type_enum.svg" style="width:16px;"> LinkBaseExtension

Link extension base class



#### <img src="images/Type_enum.svg" style="width:16px;"> Logger <small>(tag, **kargs)</small>

Convenient class for tagged logging.

       Example usage:
           >>> logger = FreeCAD.Logger('MyModule')
           >>> logger.info('log test {}',1)
           24.36053 <MyModule> <input>(1): test log 1

       The default output format is:
           <timestamp> <tag> <source file>(line number): message

       The message is formatted using new style Python string formatting, e.g.
       'test {}'.format(1). It is strongly recommended to not directly use
       Python string formatting, but pass additional argument indirectly through
       various logger print function, because the logger can skip string
       evaluation in case the logging level is disabled. For more options,
       please consult the docstring of __init__(), catch() and report().

       To set/get logger level:
           >>> FreeCAD.setLogLevel('MyModule','Trace')
           >>> FreeCAD.getLogLevel('MyModule')
           4

        There are five predefined logger level, each corresponding to an integer
        value, as shown below together with the corresponding logger print
        method,
            0: Error, Logger.error()
            1: Warning, Logger.warn()
            2: Message, Logger.msg() or info()
            3: Log, Logger.log() or debug()
            4: Trace, Logger.trace()

        FreeCAD.setLogLevel() supports both text and integer value, which allows
        you to define your own levels. The level set is persisted to user
        configuration file.

        By default any tag has a log level of 2 for release, and 3 for debug
        build.



#### <img src="images/Type_enum.svg" style="width:16px;"> Material

This is the Material class



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



#### <img src="images/Type_enum.svg" style="width:16px;"> Metadata

App.Metadata class.

A Metadata object reads an XML-formatted package metadata file and provides
read and write access to its contents.

The following constructors are supported:

Metadata()
Empty constructor.

Metadata(metadata)
Copy constructor.
metadata : App.Metadata

Metadata(file)
Reads the XML file and provides access to the metadata it specifies.
file : str
    XML file name.



#### <img src="images/Type_enum.svg" style="width:16px;"> OriginGroupExtension

This class handles placable group of document objects with an Origin



#### <img src="images/Type_enum.svg" style="width:16px;"> [Part](Part_API.md)

This class handles document objects in Part



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



#### <img src="images/Type_enum.svg" style="width:16px;"> PropertyContainer

App.PropertyContainer class.



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



### Modules

#### <img src="images/type_module.svg" style="width:16px;"> [Base](Base_API.md)

The Base module contains the classes for the geometric basics
like vector, matrix, bounding box, placement, rotation, axis, ...



#### <img src="images/type_module.svg" style="width:16px;"> [Console](Console_API.md)

FreeCAD Console module.

The Console module contains functions to manage log entries, messages,
warnings and errors.
There are also functions to get/set the status of the observers used as
logging interfaces.



#### <img src="images/type_module.svg" style="width:16px;"> Qt

This module is the Translate module



#### <img src="images/type_module.svg" style="width:16px;"> Units

The Unit API









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > FreeCAD API
