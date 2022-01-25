# Part scripting/es
{{TOCright}}

## Introducción

The main data structure used in the Part module is the [BRep](http://en.wikipedia.org/wiki/Boundary_representation) data type from OpenCascade. Almost all contents and object types of the Part module are available by [Python](Python.md) scripting. This includes geometric primitives, such as Line and Circle (or Arc), and the whole range of TopoShapes, like Vertexes, Edges, Wires, Faces, Solids and Compounds. For each of those objects, several creation methods exist, and for some of them, especially the TopoShapes, advanced operations like boolean union/difference/intersection are also available. Explore the contents of the Part module, as described in the [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) page, to know more.

The most basic object that can be created is a [Part Feature](Part_Feature.md), which has a simple **Placement** property, and basic properties to define its color and appearance.

Another simple object used in 2D geometrical objects is [Part Part2DObject](Part_Part2DObject.md), which is the base of [Sketcher SketchObject](Sketcher_SketchObject.md) ([Sketcher](Sketcher_Workbench.md)), and most [Draft elements](Draft_Workbench.md).

### Ver también 

-   [Guiones de datos topológicos](Topological_data_scripting/es.md)
-   [OpenCASCADE](OpenCASCADE/es.md)

## Guión de prueba 

Test the creation of [Part Primitives](Part_Primitives.md) with a script. <small>(v0.19)</small> 


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

This script is located in the installation directory of the program, and can be examined to see how the basic primitives are built. 
```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

## Ejemplos

To create a line element switch to the Python console and type in:


```python
import Part,PartGui 
doc=App.newDocument()  
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
doc.addObject("Part::Feature","Line").Shape=l.toShape() 
doc.recompute()
```

Let\'s go through the above python example step by step:


```python
import Part,PartGui
doc=App.newDocument()
```

loads the Part module and creates a new document


```python
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
```

Line is actually a line segment, hence the start and endpoint.


```python
doc.addObject("Part::Feature","Line").Shape=l.toShape()
```

This adds a Part object type to the document and assigns the shape representation of the line segment to the \'Shape\' property of the added object. It is important to understand here that we used a geometric primitive (the Part.LineSegment) to create a TopoShape out of it (the toShape() method). Only Shapes can be added to the document. In FreeCAD, geometry primitives are used as \"building structures\" for Shapes.


```python
doc.recompute()
```

Updates the document. This also prepares the visual representation of the new part object.

Note that a Line Segment can be created by specifying its start and endpoint directly in the constructor, for example Part.LineSegment(point1,point2), or we can create a default line and set its properties afterwards, as we did here.

A Line can be created also using:


```python
import FreeCAD
import Part
DOC = FreeCAD.newDocument()

def mycreateLine(pt1, pt2, objName):
    obj = DOC.addObject("Part::Line", objName)
    obj.X1 = pt1[0]
    obj.Y1 = pt1[1]
    obj.Z1 = pt1[2]

    obj.X2 = pt2[0]
    obj.Y2 = pt2[1]
    obj.Z2 = pt2[2]

    DOC.recompute()
    return obj

line = mycreateLine((0,0,0), (0,10,0), "LineName")
```

A circle can be created in a similar way:


```python
import Part
doc = App.activeDocument()
c = Part.Circle() 
c.Radius=10.0  
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()
```

or using:


```python
import FreeCAD
import Part
DOC = FreeCAD.newDocument()

def mycreateCircle(rad, objName):
    obj = DOC.addObject("Part::Circle", objName)
    obj.Radius = rad

    DOC.recompute()
    return obj

circle = mycreateCircle(5.0, "CircleName")
```

or create a circle defined by it\'s center, axis and radius using:


```python
import Part
doc = App.activeDocument()
center = App.Vector(1,2,3)
axis = App.Vector(1,1,1)
radius = 10
c=Part.Circle(center,axis,radius)
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()
```

or create a circle defined by three points using:


```python
import Part
doc = App.activeDocument()
p1 = App.Vector(10,0,0)
p2 = App.Vector(0,10,0)
p3 = App.Vector(0,0,10)
c = Part.Circle(p1,p2,p3)
f = doc.addObject("Part::Feature", "Circle")
f.Shape = c.toShape()
doc.recompute()
```

Note again, we used the circle (geometry primitive) to construct a shape out of it. We can of course still access our construction geometry afterwards, by doing:


```python
s = f.Shape
e = s.Edges[0]
c = e.Curve
```

Here we take the shape of our object f, then we take its list of edges. In this case there will be only one because we made the whole shape out of a single circle, so we take only the first item of the Edges list, and we takes its curve. Every Edge has a Curve, which is the geometry primitive it is based on.

Head to the [Topological data scripting](Topological_data_scripting.md) page if you would like to know more.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Part](Part_Workbench.md) > Part scripting/es
