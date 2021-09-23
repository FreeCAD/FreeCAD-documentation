# Path scripting/pl






{{TOCright}}

## Introduction

The Path workbench offers tools to import, create, manipulate and export [machine toolpaths](http://en.wikipedia.org/wiki/G-code) in FreeCAD. With it, the user is able to import, visualize and modify existing gcode programs, generate toolpaths from 3D shapes, and export these toolpaths to gcode.

The Path workbench is currently in early development, and does not offer all the advanced functions found in some commercial alternatives. However, the python scripting interface makes it easy to modify or develop more powerful tools.

## Quickstart

FreeCAD\'s Path objects are made of a sequence of motion commands. A typical use is this:


```python
>>> import Path
>>> c1 = Path.Command("g1x1")
>>> c2 = Path.Command("g1y4")
>>> c3 = Path.Command("g1 x2 y2") # spaces end newlines are not considered
>>> p = Path.Path([c1,c2,c3])
>>> o = App.ActiveDocument.addObject("Path::Feature","mypath")
>>> o.Path = p
>>> print p.toGCode()
```

## The FreeCAD Internal GCode Format 

A preliminary concept is important to grasp. Most of the implementation below relies heavily on motion commands that have the same names as GCode commands, but aren\'t meant to be close to a particular controller\'s implementation. We chose names such as \'G0\' to represent \'rapid\' move or \'G1\' to represent \'feed\' move for performance (efficient file saving) and to minimize the work needed to translate to/from other GCode formats. Since the CNC world speaks thousands of GCode dialects, we chose to stick with a very simplified subset of it. You could describe FreeCAD\'s GCode format as a \"machine-agnostic\" form of GCode.

Inside .FCStd files, Path data is saved directly into that GCode form.

All translations to/from dialects to FreeCAD GCode are done through pre and post scripts. That means that if you want to work with a machine that uses a specific LinuxCNC, Fanuc, Mitusubishi, or HAAS controller etc, you will have to use (or write if inexistant) a post processor for that particular control (see the \"Importing and exporting GCode\" section below).

### GCode Reference 

The following rules and guidelines define the GCode subset used internally in FreeCAD:

-   GCode data, inside FreeCAD Path objects, is separated into \"Commands\". A Command is defined by a command name, which must begin with G or M, and (optionally) arguments, which are in the form Letter = Float, for example X 0.02 or Y 3.5 or F 300. These are examples of typical GCode commands in FreeCAD:




    G0 X2.5 Y0 (The command name is G0, the arguments are X=2.5 and Y=0)

    G1 X30 (The command name is G1, the only argument is X=30)

    G90 (The command name is G90, there are no arguments)

-   For the numeric part of a G or M command, both \"G1\" or \"G01\" forms are supported.
-   Only commands starting with G or M are supported at the moment.
-   Only millimeters are accepted at the moment. G20/G21 are not considered.
-   Arguments are always sorted alphabetically. This means that if you create a command with \"G1 X2 Y4 F300\", it will be stored as \"G1 F300 X2 Y4\"
-   Arguments cannot be repeated inside a same command. For example, \"G1 X1 Y2 X2 Y3\" will not work. You will need to split it into two commands, for example: \"G1 X1 Y2, G1 X2 Y3\"
-   X, Y, Z, A, B, C arguments are absolute or relative, depending on the current G90/G91 mode. Default (if not specified) is absolute.
-   I, J, K are always relative to the last point. K can be omitted.
-   X, Y, or Z (and A, B, C) can be omitted. In this case, the previous X, Y or Z coordinates are maintained.
-   Gcode commands other than the ones listed in the table below are supported, that is, they are saved inside the path data (as long as they comply to the rules above, of course), but they simply won\'t produce any visible result on screen. For example, you could add a G81 command, it will be stored, but not displayed.

### List of currently supported GCode commands 

  Command         Description                                     Supported Arguments   Displayed
  --------------- ----------------------------------------------- --------------------- -----------
  G0              rapid move                                      X,Y,Z,A,B,C           Red
  G1              normal move                                     X,Y,Z,A,B,C           Green
  G2              clockwise arc                                   X,Y,Z,A,B,C,I,J,K     Green
  G3              counterclockwise arc                            X,Y,Z,A,B,C,I,J,K     Green
  G81, G82, G83   drill                                           X,Y,Z,R,Q             Red/Green
  G38.2           Straight probe move (used in probe operation)   Z,F                   Yellow
  G90             absolute coordinates                                                  
  G91             relative coordinates                                                  
  (Message)       comment                                                               

## The Command object 

The Command object represents a gcode command. It has three attributes: Name, Parameters and Placement, and two methods: toGCode() and setFromGCode(). Internally, it contains only a name and a dictionary of parameters. The rest (placement and gcode) is computed to/from this data.


```python
>>> import Path
>>> c=Path.Command()
>>> c
Command  ( )
>>> c.Name = "G1"
>>> c
Command G1 ( )
>>> c.Parameters= {"X":1,"Y":0}
>>> c
Command G1 ( X:1 Y:0 )
>>> c.Parameters
{'Y': 0.0, 'X': 1.0}
>>> c.Parameters= {"X":1,"Y":0.5}
>>> c
Command G1 ( X:1 Y:0.5 )
>>> c.toGCode()
'G1X1Y0.5'
>>> c2=Path.Command("G2")
>>> c2
Command G2 ( )
>>> c3=Path.Command("G1",{"X":34,"Y":1.2})
>>> c3
Command G1 ( X:34 Y:1.2 )
>>> c3.Placement
Placement [Pos=(34,1.2,0), Yaw-Pitch-Roll=(0,0,0)]
>>> c3.toGCode()
'G1X34Y1.2'
>>> c3.setFromGCode("G1X1Y0")
>>> c3
Command G1 [ X:1 Y:0 ]
>>> c4 = Path.Command("G1X4Y5")
>>> c4
Command G1 [ X:4 Y:5 ]
>>> p1 = App.Placement()
>>> p1.Base = App.Vector(3,2,1)
>>> p1
Placement [Pos=(3,2,1), Yaw-Pitch-Roll=(0,0,0)]
>>> c5=Path.Command("g1",p1)
>>> c5
Command G1 [ X:3 Y:2 Z:1 ]
>>> p2=App.Placement()
>>> p2.Base = App.Vector(5,0,0)
>>> c5
Command G1 [ X:3 Y:2 Z:1 ]
>>> c5.Placement=p2
>>> c5
Command G1 [ X:5 ]
>>> c5.x
5.0
>>> c5.x=10
>>> c5
Command G1 [ X:10 ]
>>> c5.y=2
>>> c5
Command G1 [ X:10 Y:2 ]
```

## The Path object 

The Path object holds a list of commands


```python
>>> import Path
>>> c1=Path.Command("g1",{"x":1,"y":0})
>>> c2=Path.Command("g1",{"x":0,"y":2})
>>> p=Path.Path([c1,c2])
>>> p
Path [ size:2 length:3 ]
>>> p.Commands
[Command G1 [ X:1 Y:0 ], Command G1 [ X:0 Y:2 ]]
>>> p.Length
3.0
>>> p.addCommands(c1)
Path [ size:3 length:4 ]
>>> p.toGCode()
'G1X1G1Y2G1X1'

lines = """
G0X-0.5905Y-0.3937S3000M03
G0Z0.125
G1Z-0.004F3
G1X0.9842Y-0.3937F14.17
G1X0.9842Y0.433
G1X-0.5905Y0.433
G1X-0.5905Y-0.3937
G0Z0.5
"""

slines = lines.split('\n')
p = Path.Path()
for line in slines:
    p.addCommands(Path.Command(line))

o = App.ActiveDocument.addObject("Path::Feature","mypath")
o.Path = p

# but you can also create a path directly form a piece of gcode.
# The commands will be created automatically:

p = Path.Path()
p.setFromGCode(lines)
```

As a shortcut, a Path object can also be created directly from a full GCode sequence. It will be divided into a sequence of commands automatically.


```python
>>> p = Path.Path("G0 X2 Y2 G1 X0 Y2")
>>> p
Path [ size:2 length:2 ]
```

## The Path feature 

The Path feature is a FreeCAD document object, that holds a path, and represents it in the 3D view.


```python
>>> pf = App.ActiveDocument.addObject("Path::Feature","mypath")
>>> pf
<Document object>
>>> pf.Path = p
>>> pf.Path
Path [ size:2 length:2 ]
```

The Path feature also holds a Placement property. Changing the value of that placement will change the position of the Feature in the 3D view, although the Path information itself won\'t be modified. The transformation is purely visual. This allows you, for example, to create a Path around a face that has a particular orientation on your model, that is not the same orientation as your cutting material will have on the CNC machine.

However, Path Compounds can make use of the Placement of their children (see below).

## The Tool and Tooltable objects 

**NOTE:** This type of tool usage is depreciated as of the 0.19 official release. In 0.19 the new ToolBit tool system was implemented to supersede this older, Legacy, system. Therefore, coding has changed from what is represented below. Please visit [Path Tools](Path_Tools.md) page for more information.

===Scripting \<= 0.18===

The Tool object contains the definitions of a CNC tool. The Tooltable object contains an ordered list of tools. Tooltables are attached as a property to Path Project features, and can also be edited via the GUI, by double-clicking a project in the tree view, and clicking the \"Edit tooltable\" button in the task views that opens.

From that dialog, tooltables can be imported from FreeCAD\'s .xml and HeeksCad\'s .tooltable formats, and exported to FreeCAD\'s .xml format.


```python
>>> import Path
>>> t1=Path.Tool()
>>> t1
Tool Default tool
>>> t1.Name = "12.7mm Drill Bit"
>>> t1
Tool 12.7mm Drill Bit
>>> t1.ToolType
'Undefined'
>>> t1.ToolType = "Drill"
>>> t1.Diameter= 12.7
>>> t1.LengthOffset = 127
>>> t1.CuttingEdgeAngle = 59
>>> t1.CuttingEdgeHeight = 50.8
>>> t2 = Path.Tool("my other tool",tooltype="EndMill",diameter=10)
>>> t2
Tool my other tool
>>> t2.Diameter
10.0
>>> table = Path.Tooltable()
>>> table
Tooltable containing 0 tools
>>> table.addTools(t1)
Tooltable containing 1 tools
>>> table.addTools(t2)
Tooltable containing 2 tools
>>> table.Tools
{1: Tool 12.7mm Drill Bit, 2: Tool my other tool}
>>> 
```

## Features

### The Path Compound feature 

The aim of this feature is to gather one or more toolpaths and associate it (them) with a tooltable. The Compound feature also behaves like a standard FreeCAD group, so you can add or remove objects to/from it directly from the tree view. You can also reorder items by double-clicking the Compound object in the Tree view, and reorder its elements in the Task view that opens.


```python
>>> import Path
>>> p1 = Path.Path("G1X1")
>>> o1 = App.ActiveDocument.addObject("Path::Feature","path1")
>>> o1.Path=p1
>>> p2 = Path.Path("G1Y1")
>>> o2 = App.ActiveDocument.addObject("Path::Feature","path2")
>>> o2.Path=p2
>>> o3 = App.ActiveDocument.addObject("Path::FeatureCompound","compound")
>>> o3.Group=[o1,o2]
```

An important feature of Path Compounds is the possibility to take into account the Placement of their child paths or not, by setting their UsePlacements property to True or False. If not, the Path data of their children will simply be added sequentially. If True, each command of the child paths, if containing position information (G0, G1, etc..) will first be transformed by the Placement before being added.

Creating a compound with just one child path allows you therefore to turn the child path\'s Placement \"real\" (it affects the Path data).

### The Path Project feature 

The Path project is an extended kind of Compound, that has a couple of additional machine-related properties such as a tooltable. It is made mainly to be the main object type you\'ll want to export to gcode once your whole path setup is ready. The Project object is now coded in python, so its creation mechanism is a bit different:


```python
>>> from PathScripts import PathProject
>>> o4 = App.ActiveDocument.addObject("Path::FeatureCompoundPython","prj")
>>> PathProject.ObjectPathProject(o4)
>>> o4.Group = [o3]
>>> o4.Tooltable
Tooltable containing 0 tools
```

The Path module also features a GUI tooltable editor that can be called from python, giving it an object that has a ToolTable property:


```python
>>> from PathScripts import TooltableEditor
>>> TooltableEditor.edit(o4)
```

### Getting Path from Shape 

Assign the shape of wire Part to a normal Path object, using Path.fronShape() script function (or more powerful Path.fronShapes()). By giving as parameter a wire Part object, its path will be automatically calculated from the shape. Note that in this case the placement is automatically set to the first point of the wire, and the object is therefore not movable anymore by changing its placement. To move it, the underlying shape itself must be moved.


```python
>>> import Part
>>> import Path
>>> v1 = FreeCAD.Vector(0,0,0)
>>> v2 = FreeCAD.Vector(0,2,0)
>>> v3 = FreeCAD.Vector(2,2,0)
>>> v4 = FreeCAD.Vector(3,3,0)
>>> wire = Part.makePolygon([v1,v2,v3,v4])
>>> o = FreeCAD.ActiveDocument.addObject("Path::Feature","myPath2")
>>> o.Path = Path.fromShape(wire)
>>> FreeCAD.ActiveDocument.recompute()
>>> p =  o.Path
>>> print(p.toGCode())
```

### Python features 

Both Path::Feature and Path::FeatureShape features have a python version, respectively named Path::FeaturePython and Path::FeatureShapePython, that can be used in python code to create more advanced parametric objects derived from them.

## Importing and exporting GCode 

### Native format 

GCode files can be directly imported and exported via the GUI, by using the \"open\", \"insert\" or \"export\" menu items. After the file name is acquired, a dialog pops up to ask which processing script must be used. It can also be done from python:

Path information is stored into Path objects using a subset of gcode described in the \"FreeCAD\'s internal GCode format\"section above. This subset can be imported or exported \"as is\", or converted to/from a particular version of GCode suited for your machine.

If you have a very simple and standard GCode program, that complies to the rules described in the \"FreeCAD\'s internal GCode format\" section above, for example the boomerang from <http://www.cnccookbook.com/GWESampleFiles.html> , it can be imported directly into a Path object, without translation (this is equivalent to using the \"None\" option of the GUI dialog):


```python
import Path
f = open("/path/to/boomerangv4.ncc")
s = f.read()
p = Path.Path(s)
o = App.ActiveDocument.addObject("Path::Feature","boomerang")
o.Path = p
```

In the same manner, you can obtain the path information as \"agnostic\" gcode, and store it manually in a file:


```python
text = o.Path.toGCode()
print text
myfile = open("/path/to/newfile.ngc")
myfile.write(text)
myfile.close()
```

If you need a different output, though, you will need to convert this agnostic GCode into a format suited for your machine. That is the job of post-processing scripts.

### Using pre- and post-processing scripts 

If you have a gcode file written for a particular machine, which doesn\'t comply to the internal rules used by FreeCAD, described in the \"FreeCAD\'s internal GCode format\" section above, it might fail to import and/or render properly in the 3D view. To remedy to this, you must use a pre-processing script, which will convert from your machine-specific format to the FreeCAD format.

If you know the name of the pre-processing script to use, you can import your file using it, from the python console like this:


```python
import example_pre
example_pre.insert("/path/to/myfile.ncc","DocumentName")
```

In the same manner, you can output a path object to GCode, using a post\_processor script like this:


```python
import example_post
example_post.export (myObjectName,"/path/to/outputFile.ncc")
```

### Writing processing scripts 

Pre- and post-processing scripts behave like other common FreeCAD imports/exporters. When choosing a pre/post processing script from the dialog, the import/export process will be redirected to the specified given script. Preprocessing scripts must contain at least the following methods open(filename) and insert(filename,docname). Postprocessing scripts need to implement export(objectslist,filename).

Scripts are placed into either the Mod/Path/PathScripts folder or the user\'s macro path directory. You can give them any name you like but by convention, and to be picked by the GUI dialog, pre-processing scripts names must end with \"\_pre\", post-processing scripts with \"\_post\" (make sure to use the underscore, not the hyphen, otherwise python cannot import it). This is an example of a very, very simple preprocessor. More complex examples are found in the Mod/Path/PathScripts folder:


```python
def open(filename):
    gfile = __builtins__.open(filename)
    inputstring = gfile.read()
    # the whole gcode program will come in as one string,
    # for example: "G0 X1 Y1\nG1 X2 Y2"
    output = ""
    # we add a comment
    output += "(This is my first parsed output!)\n"
    # we split the input string by lines
    lines = inputstring.split("\n")
    for line in lines:
        output += line
        # we must insert the "end of line" character again
        # because the split removed it
        output += "\n"
    # another comment
    output += "(End of program)"
    import Path
    p = Path.Path(output)
    myPath = FreeCAD.ActiveDocument.addObject("Path::Feature","Import")
    myPath.Path = p
    FreeCAD.ActiveDocument.recompute()
```

Pre- and post-processors work exactly the same way. They just do the contrary: The pre scripts convert from specific GCode to FreeCAD\'s \"agnostic\" GCode, while post scripts convert from FreeCAD\'s \"agnostic\" GCode to machine-specific GCode.

## Adding all faces of a ShapeString to the BaseFeature\'s list of a ProfileFromFaces operation 

This example is based on a [discussion in the german forum](https://forum.freecadweb.org/viewtopic.php?f=13&t=33310&p=279991#p279959).

### Prerequisites

-   Create a solid with ShapeString as Cutout
-   Create a Job using this solid as its BaseObject
-   Create a ProfileFromFaces operation named \"Profile\_Faces\" with empty BaseGeometry.

### The code 

The following code will then add all faces from ShapeString and create the paths:


```python
doc = App.ActiveDocument
list_of_all_element_faces = []
for i, face in enumerate(doc.ShapeString.Shape.Faces):
    list_of_all_element_faces.append('Face' + str(i + 1))


doc.Profile_Faces.Base = [(doc.ShapeString, tuple(list_of_all_element_faces))]
doc.recompute()
```





{{Path_Tools_navi

}} {{Powerdocnavi}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
