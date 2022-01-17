# FreeCAD API

The functions in the FreeCAD module allow working with documents.
The FreeCAD instance provides a list of references of documents which
can be addressed by a string. Hence the document name must be unique.

The document has the read-only attribute FileName which points to the
file the document should be stored to.




#### <img src="images/Type_enum.svg" style="max-width:24px;">ActiveDocument

This is a Document class



#### <img src="images/Type_enum.svg" style="max-width:24px;">Axis

Axis
An defines a direction and a position (base) in 3D space.

The following constructors are supported:
Axis() -- empty constructor
Axis(Axis) -- copy constructor
Axis(Base, Direction) -- define position and direction
		



#### <img src="images/type_module.svg" style="max-width:24px;">Base

The Base module contains the classes for the geometric basics
like vector, matrix, bounding box, placement, rotation, axis, ...




#### <img src="images/Type_enum.svg" style="max-width:24px;">BoundBox

Bound box class
A bounding box is an orthographic cube which is a way to describe outer boundaries.
You get a bounding box from a lot of 3D types. It is often used to check if a 3D
entity lies in the range of another object. Checking for bounding interference first
can save a lot of computing time!

Constructor:
App.BoundBox([Xmin,Ymin,Zmin,Xmax,Ymax,Zmax])
App.BoundBox(Tuple, Tuple)
App.BoundBox(Vector, Vector)
App.BoundBox(BoundBox)
	  



#### <img src="images/type_method.svg" style="max-width:24px;">ConfigDump

Dump the configuration to the output.



#### <img src="images/type_method.svg" style="max-width:24px;">ConfigGet

ConfigGet(string) -- Get the value for the given key.



#### <img src="images/type_method.svg" style="max-width:24px;">ConfigSet

ConfigSet(string, string) -- Set the given key to the given value.



#### <img src="images/type_module.svg" style="max-width:24px;">Console

FreeCAD Console




#### <img src="images/Type_enum.svg" style="max-width:24px;">Document

This is a Document class



#### <img src="images/Type_enum.svg" style="max-width:24px;">DocumentObject

This is the father of all classes handled by the document



#### <img src="images/Type_enum.svg" style="max-width:24px;">DocumentObjectExtension

Base class for all document object extensions



#### <img src="images/Type_enum.svg" style="max-width:24px;">DocumentObjectGroup

This class handles document objects in group



#### <img src="images/type_method.svg" style="max-width:24px;">EndingAdd

deprecated -- use addImportType



#### <img src="images/type_method.svg" style="max-width:24px;">EndingGet

deprecated -- use getImportType



#### <img src="images/Type_enum.svg" style="max-width:24px;">Extension

Base class for all extensions



#### <img src="images/Type_enum.svg" style="max-width:24px;">ExtensionContainer

Base class for all objects which can be extended



#### <img src="images/Type_enum.svg" style="max-width:24px;">GeoFeature

This class does the whole placement and position handling



#### <img src="images/Type_enum.svg" style="max-width:24px;">GeoFeatureGroupExtension

This class handles placeable group of document objects



#### <img src="images/Type_enum.svg" style="max-width:24px;">GroupExtension

Extension class which allows grouping of document objects



#### <img src="images/Type_enum.svg" style="max-width:24px;">GuiUp

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



#### <img src="images/Type_enum.svg" style="max-width:24px;">LinkBaseExtension

Link extension base class



#### <img src="images/Type_enum.svg" style="max-width:24px;">Logger <small>(tag, **kargs)</small>

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
    



#### <img src="images/Type_enum.svg" style="max-width:24px;">Material

This is the Material class



#### <img src="images/Type_enum.svg" style="max-width:24px;">Matrix

A 4x4 Matrix



#### <img src="images/Type_enum.svg" style="max-width:24px;">Metadata


        Metadata
        A Metadata object reads an XML-formatted package metadata file and provides read-only access to its contents.

        A single constructor is supported:
        Metadata(file) -- Reads the XML file and provides access to the metadata it specifies.
      



#### <img src="images/Type_enum.svg" style="max-width:24px;">OriginGroupExtension

This class handles placable group of document objects with an Origin



#### <img src="images/type_method.svg" style="max-width:24px;">ParamGet

Get parameters by path



#### <img src="images/Type_enum.svg" style="max-width:24px;">Part

This class handles document objects in Part



#### <img src="images/Type_enum.svg" style="max-width:24px;">Placement

Placement
A placement defines an orientation (rotation) and a position (base) in 3D space.
It is used when no scaling or other distortion is needed.

The following constructors are supported:
Placement() -- empty constructor
Placement(Placement) -- copy constructor
Placement(Matrix) -- 4D matrix consisting of rotation and translation
Placement(Base, Rotation) -- define position and rotation
Placement(Base, Rotation,Center) -- define position and rotation with center
Placement(Base, Axis, Angle) -- define position and rotation
		



#### <img src="images/Type_enum.svg" style="max-width:24px;">PropertyContainer

This is a Persistence class



#### <img src="images/type_module.svg" style="max-width:24px;">Qt

This module is the Translate module



#### <img src="images/Type_enum.svg" style="max-width:24px;">Rotation


				A Rotation using a quaternion.
				The Rotation object can be created by:
				-- an empty parameter list
				-- a Rotation object
				-- a Vector (axis) and a float (angle)
				-- two Vectors (rotation from/to vector)
				-- three floats (Euler angles) as yaw-pitch-roll in XY'Z'' convention
                -- one string and three floats (Euler angles) as euler rotation 
                   of a given type. Call toEulerSequence() for supported sequence types.
				-- four floats (Quaternion) where the quaternion is specified as:
				   q=xi+yj+zk+w, i.e. the last parameter is the real part
				-- three vectors that define rotated axes directions + an optional
				   3-characher string of capital letters 'X', 'Y', 'Z' that sets the
				   order of importance of the axes (e.g., 'ZXY' means z direction is
				   followed strictly, x is used but corrected if necessary, y is ignored).
			



#### <img src="images/type_module.svg" style="max-width:24px;">Units

The Unit API



#### <img src="images/Type_enum.svg" style="max-width:24px;">Vector

This class represents a 3D float vector



#### <img src="images/type_method.svg" style="max-width:24px;">Version

Print the version to the output.



#### <img src="images/type_method.svg" style="max-width:24px;">activeDocument

activeDocument() -> object or None

Return the active document or None if there is no one.



#### <img src="images/type_method.svg" style="max-width:24px;">addDocumentObserver

addDocumentObserver() -> None

Add an observer to get notified about changes on documents.



#### <img src="images/type_method.svg" style="max-width:24px;">addExportType

Register filetype for export



#### <img src="images/type_method.svg" style="max-width:24px;">addImportType

Register filetype for import



#### <img src="images/type_method.svg" style="max-width:24px;">changeExportModule

Change the export module name of a registered filetype



#### <img src="images/type_method.svg" style="max-width:24px;">changeImportModule

Change the import module name of a registered filetype



#### <img src="images/type_method.svg" style="max-width:24px;">checkAbort

checkAbort() -- check for user abort in length operation.

This only works if there is an active sequencer (or ProgressIndicator in Python).
There is an active sequencer during document restore and recomputation. User may
abort the operation by pressing the ESC key. Once detected, this function will
trigger a BaseExceptionFreeCADAbort exception.



#### <img src="images/type_method.svg" style="max-width:24px;">checkLinkDepth

checkLinkDepth(depth) -- check link recursion depth



#### <img src="images/type_method.svg" style="max-width:24px;">closeActiveTransaction

closeActiveTransaction(abort=False) -- commit or abort current active transaction



#### <img src="images/type_method.svg" style="max-width:24px;">closeDocument

closeDocument(string) -> None

Close the document with a given name.



#### <img src="images/type_method.svg" style="max-width:24px;">getActiveTransaction

getActiveTransaction() -> (name,id) return the current active transaction name and ID



#### <img src="images/type_method.svg" style="max-width:24px;">getDependentObjects

getDependentObjects(obj|[obj,...], options=0)
Return a list of dependent objects including the given objects.

options: can have the following bit flags,
         1: to sort the list in topological order.
         2: to exclude dependency of Link type object.



#### <img src="images/type_method.svg" style="max-width:24px;">getDocument

getDocument(string) -> object

Get a document by its name or raise an exception
if there is no document with the given name.



#### <img src="images/type_method.svg" style="max-width:24px;">getExportType

Get the name of the module that can export the filetype



#### <img src="images/type_method.svg" style="max-width:24px;">getHelpDir

Get the directory of the documentation



#### <img src="images/type_method.svg" style="max-width:24px;">getHomePath

Get the home path, i.e. the parent directory of the executable



#### <img src="images/type_method.svg" style="max-width:24px;">getImportType

Get the name of the module that can import the filetype



#### <img src="images/type_method.svg" style="max-width:24px;">getLinksTo

getLinksTo(obj,options=0,maxCount=0) -- return the objects linked to 'obj'

options: 1: recursive, 2: check link array. Options can combine.
maxCount: to limit the number of links returned




#### <img src="images/type_method.svg" style="max-width:24px;">getLogLevel

getLogLevel(tag) -- Get the log level of a string tag



#### <img src="images/type_method.svg" style="max-width:24px;">getResourceDir

Get the root directory of all resources



#### <img src="images/type_method.svg" style="max-width:24px;">getTempPath

Get the root directory of cached files



#### <img src="images/type_method.svg" style="max-width:24px;">getUserAppDataDir

Get the root directory of application data



#### <img src="images/type_method.svg" style="max-width:24px;">getUserCachePath

Get the root path of cached files



#### <img src="images/type_method.svg" style="max-width:24px;">getUserConfigDir

Get the root path of user config files



#### <img src="images/type_method.svg" style="max-width:24px;">getUserMacroDir

getUserMacroDir(bool=False) -> stringGet the directory of the user's macro directory
If parameter is False (the default) it returns the standard path in theuser's home directory, otherwise it returns the user-defined path.



#### <img src="images/type_method.svg" style="max-width:24px;">isRestoring

isRestoring() -> Bool -- Test if the application is opening some document



#### <img src="images/type_method.svg" style="max-width:24px;">listDocuments

listDocuments(sort=False) -> list

Return a list of names of all documents, optionally sort in dependency order.



#### <img src="images/type_method.svg" style="max-width:24px;">loadFile

loadFile(string=filename,[string=module]) -> None

Loads an arbitrary file by delegating to the given Python module:
* If no module is given it will be determined by the file extension.
* If more than one module can load a file the first one will be taken.
* If no module exists to load the file an exception will be raised.



#### <img src="images/type_method.svg" style="max-width:24px;">newDocument

newDocument(name, label=None, hidden=False, temp=False) -> object
Create a new document with a given name.

name: unique document name which is checked automatically.
label: optional user changeable label for the document.
hidden: whether to hide document 3D view.
temp: mark the document as temporary so that it will not be saved



#### <img src="images/type_method.svg" style="max-width:24px;">open

See openDocument(string)



#### <img src="images/type_method.svg" style="max-width:24px;">openDocument

openDocument(filepath,hidden=False) -> object
Create a document and load the project file into the document.

filepath: file path to an existing file. If the file doesn't exist
          or the file cannot be loaded an I/O exception is thrown.
          In this case the document is kept alive.
hidden: whether to hide document 3D view.



#### <img src="images/type_method.svg" style="max-width:24px;">removeDocumentObserver

removeDocumentObserver() -> None

Remove an added document observer.



#### <img src="images/type_method.svg" style="max-width:24px;">saveParameter

saveParameter(config='User parameter') -> None
Save parameter set to file. The default set is 'User parameter'



#### <img src="images/type_method.svg" style="max-width:24px;">setActiveDocument

setActiveDocement(string) -> None

Set the active document by its name.



#### <img src="images/type_method.svg" style="max-width:24px;">setActiveTransaction

setActiveTransaction(name, persist=False) -- setup active transaction with the given name

name: the transaction name
persist(False): by default, if the calling code is inside any invocation of a command, it
                will be auto closed once all commands within the current stack exists. To
                disable auto closing, set persist=True
Returns the transaction ID for the active transaction. An application-wide
active transaction causes any document changes to open a transaction with
the given name and ID.



#### <img src="images/type_method.svg" style="max-width:24px;">setLogLevel

setLogLevel(tag, level) -- Set the log level for a string tag.
'level' can either be string 'Log', 'Msg', 'Wrn', 'Error', or an integer value







---
[documentation index](../README.md) > [API](Category_API.md) > FreeCAD API
