# Topological data scripting/pt



{{TOCright}}

## Introduction

Here we will explain to you how to control the [Part](Part_Workbench.md) module directly from the FreeCAD Python interpreter, or from any external script. Be sure to browse the [Scripting](Scripting.md) section and the [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) pages if you need more information about how Python scripting works in FreeCAD. If you are new to Python, it is a good idea to first read the [Introduction to Python](Introduction_to_Python.md).

### See also 

-   [Part scripting](Part_scripting.md)
-   [OpenCASCADE](OpenCASCADE.md)

## Class diagram 

This is a [Unified Modeling Language (UML)](http://en.wikipedia.org/wiki/Unified_Modeling_Language) overview of the most important classes of the Part module: ![Python classes of the Part module](images/Part_Classes.jpg ) {{Top}}

### Geometry

The geometric objects are the building blocks of all topological objects:

-   **Geom** Base class of the geometric objects.
-   **Line** A straight line in 3D, defined by starting point and end point.
-   **Circle** Circle or circle segment defined by a center point and start and end point.
-   Etc.


{{Top}}

### Topology

The following topological data types are available:

-   **Compound** A group of any type of topological objects.
-   **Compsolid** A composite solid is a set of solids connected by their faces. It expands the notions of WIRE and SHELL to solids.
-   **Solid** A part of space limited by shells. It is three dimensional.
-   **Shell** A set of faces connected by their edges. A shell can be open or closed.
-   **Face** In 2D it is part of a plane; in 3D it is part of a surface. Its geometry is constrained (trimmed) by contours. It is two dimensional.
-   **Wire** A set of edges connected by their vertices. It can be an open or closed contour depending on whether the edges are linked or not.
-   **Edge** A topological element corresponding to a restrained curve. An edge is generally limited by vertices. It has one dimension.
-   **Vertex** A topological element corresponding to a point. It has zero dimension.
-   **Shape** A generic term covering all of the above.


{{Top}}

## Example: Create simple topology 

![Wire](images/Wire.png )

We will now create a topology by constructing it out of simpler geometry. As a case study we will use a part as seen in the picture which consists of four vertices, two arcs and two lines. {{Top}}

### Create geometry 

First we create the distinct geometric parts of this wire. Making sure that parts that have to be connected later share the same vertices.

So we create the points first:


```python
import Part
from FreeCAD import Base
V1 = Base.Vector(0, 10, 0)
V2 = Base.Vector(30, 10, 0)
V3 = Base.Vector(30, -10, 0)
V4 = Base.Vector(0, -10, 0)
```


{{Top}}

### Arc

![Circle](images/Circel.png )

For each arc we need a helper point:


```python
VC1 = Base.Vector(-10, 0, 0)
C1 = Part.Arc(V1, VC1, V4)
VC2 = Base.Vector(40, 0, 0)
C2 = Part.Arc(V2, VC2, V3)
```


{{Top}}

### Line

![Line](images/Line.png )

The line segments can be created from two points:


```python
L1 = Part.LineSegment(V1, V2)
L2 = Part.LineSegment(V3, V4)
```


{{Top}}

### Put it all together 

The last step is to put the geometric base elements together and bake a topological shape:


```python
S1 = Part.Shape([C1, L1, C2, L2])
```


{{Top}}

### Make a prism 

Now extrude the wire in a direction and make an actual 3D shape:


```python
W = Part.Wire(S1.Edges)
P = W.extrude(Base.Vector(0, 0, 10))
```


{{Top}}

### Show it all 


```python
Part.show(P)
```


{{Top}}

## Create basic shapes 

You can easily create basic topological objects with the `make...()` methods from the Part module:


```python
b = Part.makeBox(100, 100, 100)
Part.show(b)
```

Some available `make...()` methods:

-    `makeBox(l, w, h, [p, d])`Makes a box located in p and pointing into the direction d with the dimensions (l,w,h).

-    `makeCircle(radius)`Makes a circle with a given radius.

-    `makeCone(radius1, radius2, height)`Makes a cone with the given radii and height.

-    `makeCylinder(radius, height)`Makes a cylinder with a given radius and height.

-    `makeLine((x1, y1, z1), (x2, y2, z2))`Makes a line from two points.

-    `makePlane(length, width)`Makes a plane with length and width.

-    `makePolygon(list)`Makes a polygon from a list of points.

-    `makeSphere(radius)`Makes a sphere with a given radius.

-    `makeTorus(radius1, radius2)`Makes a torus with the given radii.

See the [Part API](Part_API.md) page for a complete list of available methods of the Part module. {{Top}}

### Import modules 

First we need to import the Part module so we can use its contents in Python. We\'ll also import the Base module from inside the FreeCAD module:


```python
import Part
from FreeCAD import Base
```


{{Top}}

### Create a vector 

[Vectors](http://en.wikipedia.org/wiki/Euclidean_vector) are one of the most important pieces of information when building shapes. They usually contain three numbers (but not necessarily always): the X, Y and Z cartesian coordinates. You create a vector like this:


```python
myVector = Base.Vector(3, 2, 0)
```

We just created a vector at coordinates X = 3, Y = 2, Z = 0. In the Part module, vectors are used everywhere. Part shapes also use another kind of point representation called Vertex which is simply a container for a vector. You access the vector of a vertex like this:


```python
myVertex = myShape.Vertexes[0]
print(myVertex.Point)
> Vector (3, 2, 0)
```


{{Top}}

### Create an edge 

An edge is nothing but a line with two vertices:


```python
edge = Part.makeLine((0, 0, 0), (10, 0, 0))
edge.Vertexes
> [<Vertex object at 01877430>, <Vertex object at 014888E0>]
```

Note: You can also create an edge by passing two vectors:


```python
vec1 = Base.Vector(0, 0, 0)
vec2 = Base.Vector(10, 0, 0)
line = Part.LineSegment(vec1, vec2)
edge = line.toShape()
```

You can find the length and center of an edge like this:


```python
edge.Length
> 10.0
edge.CenterOfMass
> Vector (5, 0, 0)
```


{{Top}}

### Put the shape on screen 

So far we created an edge object, but it doesn\'t appear anywhere on the screen. This is because the FreeCAD 3D scene only displays what you tell it to display. To do that, we use this simple method:


```python
Part.show(edge)
```

The show function creates an object in our FreeCAD document and assigns our \"edge\" shape to it. Use this whenever it is time to display your creation on screen. {{Top}}

### Create a wire 

A wire is a multi-edge line and can be created from a list of edges or even a list of wires:


```python
edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
wire1 = Part.Wire([edge1, edge2]) 
edge3 = Part.makeLine((10, 10, 0), (0, 10, 0))
edge4 = Part.makeLine((0, 10, 0), (0, 0, 0))
wire2 = Part.Wire([edge3, edge4])
wire3 = Part.Wire([wire1, wire2])
wire3.Edges
> [<Edge object at 016695F8>, <Edge object at 0197AED8>, <Edge object at 01828B20>, <Edge object at 0190A788>]
Part.show(wire3)
```


`Part.show(wire3)`

will display the 4 edges that compose our wire. Other useful information can be easily retrieved:


```python
wire3.Length
> 40.0
wire3.CenterOfMass
> Vector (5, 5, 0)
wire3.isClosed()
> True
wire2.isClosed()
> False
```


{{Top}}

### Create a face 

Only faces created from closed wires will be valid. In this example, wire3 is a closed wire but wire2 is not (see above):


```python
face = Part.Face(wire3)
face.Area
> 99.99999999999999
face.CenterOfMass
> Vector (5, 5, 0)
face.Length
> 40.0
face.isValid()
> True
sface = Part.Face(wire2)
sface.isValid()
> False
```

Only faces will have an area, wires and edges do not. {{Top}}

### Create a circle 

A circle can be created like this:


```python
circle = Part.makeCircle(10)
circle.Curve
> Circle (Radius : 10, Position : (0, 0, 0), Direction : (0, 0, 1))
```

If you want to create it at a certain position and with a certain direction:


```python
ccircle = Part.makeCircle(10, Base.Vector(10, 0, 0), Base.Vector(1, 0, 0))
ccircle.Curve
> Circle (Radius : 10, Position : (10, 0, 0), Direction : (1, 0, 0))
```

ccircle will be created at distance 10 from the X origin and will be facing outwards along the X axis. Note: `makeCircle()` only accepts `Base.Vector()` for the position and normal parameters, not tuples. You can also create part of the circle by giving a start and an end angle:


```python
from math import pi
arc1 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
arc2 = Part.makeCircle(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 180, 360)
```

Angles should be provided in degrees. If you have radians simply convert them using the formula: `degrees <nowiki>=</nowiki> radians * 180/pi` or by using Python\'s `math` module:


```python
import math
degrees = math.degrees(radians)
```


{{Top}}

### Create an arc along points 

Unfortunately there is no `makeArc()` function, but we have the `Part.Arc()` function to create an arc through three points. It creates an arc object joining the start point to the end point through the middle point. The arc object\'s `toShape()` function must be called to get an edge object, the same as when using `Part.LineSegment` instead of `Part.makeLine`.


```python
arc = Part.Arc(Base.Vector(0, 0, 0), Base.Vector(0, 5, 0), Base.Vector(5, 5, 0))
arc
> <Arc object>
arc_edge = arc.toShape()
Part.show(arc_edge)
```


`Arc()`

only accepts `Base.Vector()` for points and not tuples. You can also obtain an arc by using a portion of a circle:


```python
from math import pi
circle = Part.Circle(Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 10)
arc = Part.Arc(circle,0,pi)
```

Arcs are valid edges like lines, so they can be used in wires also. {{Top}}

### Create a polygon 

A polygon is simply a wire with multiple straight edges. The `makePolygon()` function takes a list of points and creates a wire through those points:


```python
lshape_wire = Part.makePolygon([Base.Vector(0, 5, 0), Base.Vector(0, 0, 0), Base.Vector(5, 0, 0)])
```


{{Top}}

### Create a bézier curve 

Bézier curves are used to model smooth curves using a series of poles (points) and optional weights. The function below makes a `Part.BezierCurve()` from a series of `FreeCAD.Vector()` points. Note: when \"getting\" and \"setting\" a single pole or weight, indices start at 1, not 0.


```python
def makeBCurveEdge(Points):
   geomCurve = Part.BezierCurve()
   geomCurve.setPoles(Points)
   edge = Part.Edge(geomCurve)
   return(edge)
```


{{Top}}

### Create a plane 

A Plane is a flat rectangular surface. The method used to create one is `makePlane(length, width, [start_pnt, dir_normal])`. By default start\_pnt = Vector(0, 0, 0) and dir\_normal = Vector(0, 0, 1). Using dir\_normal = Vector(0, 0, 1) will create the plane facing in the positive Z axis direction, while dir\_normal = Vector(1, 0, 0) will create the plane facing in the positive X axis direction:


```python
plane = Part.makePlane(2, 2)
plane
> <Face object at 028AF990>
plane = Part.makePlane(2, 2, Base.Vector(3, 0, 0), Base.Vector(0, 1, 0))
plane.BoundBox
> BoundBox (3, 0, 0, 5, 0, 2)
```


`BoundBox`

is a cuboid enclosing the plane with a diagonal starting at (3, 0, 0) and ending at (5, 0, 2). Here the `BoundBox` thickness along the Y axis is zero, since our shape is totally flat.

Note: `makePlane()` only accepts `Base.Vector()` for start\_pnt and dir\_normal and not tuples. {{Top}}

### Create an ellipse 

There are several ways to create an ellipse:


```python
Part.Ellipse()
```

Creates an ellipse with major radius 2 and minor radius 1 with the center at (0, 0, 0).


```python
Part.Ellipse(Ellipse)
```

Creates a copy of the given ellipse.


```python
Part.Ellipse(S1, S2, Center)
```

Creates an ellipse centered on the point Center, where the plane of the ellipse is defined by Center, S1 and S2, its major axis is defined by Center and S1, its major radius is the distance between Center and S1, and its minor radius is the distance between S2 and the major axis.


```python
Part.Ellipse(Center, MajorRadius, MinorRadius)
```

Creates an ellipse with major and minor radii MajorRadius and MinorRadius, located in the plane defined by Center and the normal (0, 0, 1)


```python
eli = Part.Ellipse(Base.Vector(10, 0, 0), Base.Vector(0, 5, 0), Base.Vector(0, 0, 0))
Part.show(eli.toShape())
```

In the above code we have passed S1, S2 and center. Similar to `Arc`, `Ellipse` creates an ellipse object not an edge, so we need to convert it into an edge using `toShape()` for display.

Note: `Ellipse()` only accepts `Base.Vector()` for points and not tuples.


```python
eli = Part.Ellipse(Base.Vector(0, 0, 0), 10, 5)
Part.show(eli.toShape())
```

For the above Ellipse constructor we have passed center, MajorRadius and MinorRadius. {{Top}}

### Create a torus 

Using `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = 0, angle2 = 360 and angle = 360. Consider a torus as small circle sweeping along a big circle. Radius1 is the radius of the big circle, radius2 is the radius of the small circle, pnt is the center of the torus and dir is the normal direction. angle1 and angle2 are angles in degrees for the small circle; the last angle parameter is to make a section of the torus:


```python
torus = Part.makeTorus(10, 2)
```

The above code will create a torus with diameter 20 (radius 10) and thickness 4 (small circle radius 2)


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 180)
```

The above code will create a slice of the torus.


```python
tor=Part.makeTorus(10, 5, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), 0, 360, 180)
```

The above code will create a semi torus; only the last parameter is changed. i.e the remaining angles are defaults. Giving the angle 180 will create the torus from 0 to 180, that is, a half torus. {{Top}}

### Create a box or cuboid 

Using `makeBox(length, width, height, [pnt, dir])`. By default pnt = Vector(0, 0, 0) and dir = Vector(0, 0, 1).


```python
box = Part.makeBox(10, 10, 10)
len(box.Vertexes)
> 8
```


{{Top}}

### Create a sphere 

Using `makeSphere(radius, [pnt, dir, angle1, angle2, angle3])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1), angle1 = -90, angle2 = 90 and angle3 = 360. Angle1 and angle2 are the vertical minimum and maximum of the sphere, angle3 is the sphere diameter.


```python
sphere = Part.makeSphere(10)
hemisphere = Part.makeSphere(10, Base.Vector(0, 0, 0), Base.Vector(0, 0, 1), -90, 90, 180)
```


{{Top}}

### Create a cylinder 

Using `makeCylinder(radius, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360. 
```python
cylinder = Part.makeCylinder(5, 20)
partCylinder = Part.makeCylinder(5, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}

### Create a cone 

Using `makeCone(radius1, radius2, height, [pnt, dir, angle])`. By default pnt = Vector(0, 0, 0), dir = Vector(0, 0, 1) and angle = 360. 
```python
cone = Part.makeCone(10, 0, 20)
semicone = Part.makeCone(10, 0, 20, Base.Vector(20, 0, 0), Base.Vector(0, 0, 1), 180)
```{{Top}}

## Modify shapes 

There are several ways to modify shapes. Some are simple transformation operations such as moving or rotating shapes, others are more complex, such as unioning and subtracting one shape from another. {{Top}}

## Transform operations 

### Translate a shape 

Translating is the act of moving a shape from one place to another. Any shape (edge, face, cube, etc\...) can be translated the same way: 
```python
myShape = Part.makeBox(2, 2, 2)
myShape.translate(Base.Vector(2, 0, 0))
``` This will move our shape \"myShape\" 2 units in the X direction. {{Top}}

### Rotate a shape 

To rotate a shape, you need to specify the rotation center, the axis, and the rotation angle: 
```python
myShape.rotate(Base.Vector(0, 0, 0),Base.Vector(0, 0, 1), 180)
``` The above code will rotate the shape 180 degrees around the Z Axis. {{Top}}

### Matrix transformations 

A matrix is a very convenient way to store transformations in the 3D world. In a single matrix, you can set translation, rotation and scaling values to be applied to an object. For example: 
```python
myMat = Base.Matrix()
myMat.move(Base.Vector(2, 0, 0))
myMat.rotateZ(math.pi/2)
``` Note: FreeCAD matrixes work in radians. Also, almost all matrix operations that take a vector can also take three numbers, so these two lines do the same thing: 
```python
myMat.move(2, 0, 0)
myMat.move(Base.Vector(2, 0, 0))
``` Once our matrix is set, we can apply it to our shape. FreeCAD provides two methods for doing that: `transformShape()` and `transformGeometry()`. The difference is that with the first one, you are sure that no deformations will occur (see [Scaling a shape](#Scaling_a_shape.md) below). We can apply our transformation like this: 
```python
myShape.transformShape(myMat)
``` or 
```python
myShape.transformGeometry(myMat)
```{{Top}}

### Scale a shape 

Scaling a shape is a more dangerous operation because, unlike translation or rotation, scaling non-uniformly (with different values for X, Y and Z) can modify the structure of the shape. For example, scaling a circle with a higher value horizontally than vertically will transform it into an ellipse, which behaves mathematically very differently. For scaling, we cannot use the `transformShape()`, we must use `transformGeometry()`: 
```python
myMat = Base.Matrix()
myMat.scale(2, 1, 1)
myShape=myShape.transformGeometry(myMat)
```{{Top}}

## Boolean operations 

### Subtraction

Subtracting a shape from another one is called \"cut\" in FreeCAD and is done like this: 
```python
cylinder = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
sphere = Part.makeSphere(5, Base.Vector(5, 0, 0))
diff = cylinder.cut(sphere)
```{{Top}}

### Intersection

The same way, the intersection between two shapes is called \"common\" and is done this way: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
common = cylinder1.common(cylinder2)
```{{Top}}

### Union

Union is called \"fuse\" and works the same way: 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
fuse = cylinder1.fuse(cylinder2)
```{{Top}}

### Section

A \"section\" is the intersection between a solid shape and a plane shape. It will return an intersection curve, a compound curve composed of edges. 
```python
cylinder1 = Part.makeCylinder(3, 10, Base.Vector(0, 0, 0), Base.Vector(1, 0, 0))
cylinder2 = Part.makeCylinder(3, 10, Base.Vector(5, 0, -5), Base.Vector(0, 0, 1))
section = cylinder1.section(cylinder2)
section.Wires
> []
section.Edges
> [<Edge object at 0D87CFE8>, <Edge object at 019564F8>, <Edge object at 0D998458>, 
 <Edge  object at 0D86DE18>, <Edge object at 0D9B8E80>, <Edge object at 012A3640>, 
 <Edge object at 0D8F4BB0>]
```{{Top}}

### Extrusion

Extrusion is the act of \"pushing\" a flat shape in a certain direction, resulting in a solid body. Think of a circle becoming a tube by \"pushing it out\": 
```python
circle = Part.makeCircle(10)
tube = circle.extrude(Base.Vector(0, 0, 2))
``` If your circle is hollow, you will obtain a hollow tube. If your circle is actually a disc with a filled face, you will obtain a solid cylinder: 
```python
wire = Part.Wire(circle)
disc = Part.Face(wire)
cylinder = disc.extrude(Base.Vector(0, 0, 2))
```{{Top}}

## Explore shapes 

You can easily explore the topological data structure: 
```python
import Part
b = Part.makeBox(100, 100, 100)
b.Wires
w = b.Wires[0]
w
w.Wires
w.Vertexes
Part.show(w)
w.Edges
e = w.Edges[0]
e.Vertexes
v = e.Vertexes[0]
v.Point
``` By typing the lines above in the Python interpreter, you will gain a good understanding of the structure of Part objects. Here, our `makeBox()` command created a solid shape. This solid, like all Part solids, contains faces. Faces always contain wires, which are lists of edges that border the face. Each face has at least one closed wire (it can have more if the face has a hole). In the wire, we can look at each edge separately, and inside each edge, we can see the vertices. Straight edges have only two vertices, obviously. {{Top}}

### Edge analysis 

In case of an edge, which is an arbitrary curve, it\'s most likely you want to do a discretization. In FreeCAD the edges are parametrized by their lengths. That means you can walk an edge/curve by its length: 
```python
import Part
box = Part.makeBox(100, 100, 100)
anEdge = box.Edges[0]
print(anEdge.Length)
``` Now you can access a lot of properties of the edge by using the length as a position. That means if the edge is 100mm long the start position is 0 and the end position 100. 
```python
anEdge.tangentAt(0.0)          # tangent direction at the beginning
anEdge.valueAt(0.0)            # Point at the beginning
anEdge.valueAt(100.0)          # Point at the end of the edge
anEdge.derivative1At(50.0)     # first derivative of the curve in the middle
anEdge.derivative2At(50.0)     # second derivative of the curve in the middle
anEdge.derivative3At(50.0)     # third derivative of the curve in the middle
anEdge.centerOfCurvatureAt(50) # center of the curvature for that position
anEdge.curvatureAt(50.0)       # the curvature
anEdge.normalAt(50)            # normal vector at that position (if defined)
```{{Top}}

### Use a selection 

Here we see now how we can use a selection the user did in the viewer. First of all we create a box and show it in the viewer. 
```python
import Part
Part.show(Part.makeBox(100, 100, 100))
Gui.SendMsgToActiveView("ViewFit")
``` Now select some faces or edges. With this script you can iterate over all selected objects and their sub elements: 
```python
for o in Gui.Selection.getSelectionEx():
    print(o.ObjectName)
    for s in o.SubElementNames:
        print("name: ", s)
        for s in o.SubObjects:
            print("object: ", s)
``` Select some edges and this script will calculate the length: 
```python
length = 0.0
for o in Gui.Selection.getSelectionEx():
    for s in o.SubObjects:
        length += s.Length

print("Length of the selected edges: ", length)
```{{Top}}

## Example: The OCC bottle 

A typical example found on the [OpenCasCade Technology website](https://www.opencascade.com/doc/occt-6.9.0/overview/html/occt__tutorial.html) is how to build a bottle. This is a good exercise for FreeCAD too. In fact, if you follow our example below and the OCC page simultaneously, you will see how well OCC structures are implemented in FreeCAD. The script is included in the FreeCAD installation (inside the {{FileName|Mod/Part}} folder) and can be called from the Python interpreter by typing: 
```python
import Part
import MakeBottle
bottle = MakeBottle.makeBottle()
Part.show(bottle)
```{{Top}}

### The script 

For the purpose of this tutorial we will consider a reduced version of the script. In this version the bottle will not be hollowed out, and the neck of the bottle will not be threaded. 
```python
import Part, math
from FreeCAD import Base

def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])

    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])

    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)

    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    myBody = myBody.fuse(myNeck)

    return myBody

el = makeBottleTut()
Part.show(el)
```{{Top}}

### Detailed explanation 


```python
import Part, math
from FreeCAD import Base
```

We will need, of course, the `Part` module, but also the `FreeCAD.Base` module, which contains basic FreeCAD structures like vectors and matrices.


```python
def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=Base.Vector(-myWidth / 2., 0, 0)
    aPnt2=Base.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=Base.Vector(0, -myThickness / 2., 0)
    aPnt4=Base.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=Base.Vector(myWidth / 2., 0, 0)
```

Here we define our `makeBottleTut` function. This function can be called without arguments, like we did above, in which case default values for width, height, and thickness will be used. Then, we define a couple of points that will be used for building our base profile.


```python
    ...
    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)
```

Here we define the geometry: an arc, made of three points, and two line segments, made of two points.


```python
    ...
    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])
```

Remember the difference between geometry and shapes? Here we build shapes out of our construction geometry. Three edges (edges can be straight or curved), then a wire made of those three edges.


```python
    ...
    aTrsf=Base.Matrix()
    aTrsf.rotateZ(math.pi) # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])
```

So far we have built only a half profile. Instead of building the whole profile the same way, we can just mirror what we did and glue both halves together. We first create a matrix. A matrix is a very common way to apply transformations to objects in the 3D world, since it can contain in one structure all basic transformations that 3D objects can undergo (move, rotate and scale). After we create the matrix we mirror it, then we create a copy of our wire and apply the transformation matrix to it. We now have two wires, and we can make a third wire out of them, since wires are actually lists of edges.


```python
    ...
    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=Base.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)
```

Now that we have a closed wire, it can be turned into a face. Once we have a face, we can extrude it. In doing so, we make a solid. Then we apply a nice little fillet to our object because we care about good design, don\'t we? 
```python
    ...
    neckLocation=Base.Vector(0, 0, myHeight)
    neckNormal=Base.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 10.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
``` At this point, the body of our bottle is made, but we still need to create a neck. So we make a new solid, with a cylinder. 
```python
    ...
    myBody = myBody.fuse(myNeck)
``` The fuse operation is very powerful. It will take care of gluing what needs to be glued and remove parts that need to be removed. 
```python
    ...
    return myBody
``` Then, we return our Part solid as the result of our function. 
```python
el = makeBottleTut()
Part.show(el)
``` Finally, we call the function to actually create the part, then make it visible. {{Top}}

## Example: Pierced box 

Here is a complete example of building a pierced box.

The construction is done one side at a time. When the cube is finished, it is hollowed out by cutting a cylinder through it. 
```python
import Part, math
from FreeCAD import Base

size = 10
poly = Part.makePolygon([(0, 0, 0), (size, 0, 0), (size, 0, size), (0, 0, size), (0, 0, 0)])

face1 = Part.Face(poly)
face2 = Part.Face(poly)
face3 = Part.Face(poly)
face4 = Part.Face(poly)
face5 = Part.Face(poly)
face6 = Part.Face(poly)
     
myMat = Base.Matrix()

myMat.rotateZ(math.pi / 2)
face2.transformShape(myMat)
face2.translate(Base.Vector(size, 0, 0))

myMat.rotateZ(math.pi / 2)
face3.transformShape(myMat)
face3.translate(Base.Vector(size, size, 0))

myMat.rotateZ(math.pi / 2)
face4.transformShape(myMat)
face4.translate(Base.Vector(0, size, 0))

myMat = Base.Matrix()

myMat.rotateX(-math.pi / 2)
face5.transformShape(myMat)

face6.transformShape(myMat)               
face6.translate(Base.Vector(0, 0, size))

myShell = Part.makeShell([face1, face2, face3, face4, face5, face6])   
mySolid = Part.makeSolid(myShell)

myCyl = Part.makeCylinder(2, 20)
myCyl.translate(Base.Vector(size / 2, size / 2, 0))

cut_part = mySolid.cut(myCyl)

Part.show(cut_part)
```{{Top}}

## Loading and saving 

There are several ways to save your work. You can of course save your FreeCAD document, but you can also save [Part](Part_Workbench.md) objects directly to common CAD formats, such as BREP, IGS, STEP and STL.

Saving a shape to a file is easy. There are `exportBrep()`, `exportIges()`, `exportStep()` and `exportStl()` methods available for all shape objects. So, doing: 
```python
import Part
s = Part.makeBox(10, 10, 10)
s.exportStep("test.stp")
``` will save our box into a STEP file. To load a BREP, IGES or STEP file: 
```python
import Part
s = Part.Shape()
s.read("test.stp")
``` To convert a STEP file to an IGS file: 
```python
 import Part
 s = Part.Shape()
 s.read("file.stp")       # incoming file igs, stp, stl, brep
 s.exportIges("file.igs") # outbound file igs
```{{Top}} {{Powerdocnavi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
