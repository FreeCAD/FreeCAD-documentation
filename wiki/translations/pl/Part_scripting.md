# Part scripting/pl
{{TOCright}}

## Wprowadzenie

The main data structure used in the Part module is the [BRep](http   *//en.wikipedia.org/wiki/Boundary_representation) data type from [OpenCASCADE](OpenCASCADE.md). Almost all contents and object types of the Part module are available in [Python](Python.md) scripting. This includes geometric primitives, such as Lines, Circles and Arcs, and the whole range of TopoShapes, like Vertexes, Edges, Wires, Faces, Solids and Compounds. For each of those objects, several creation methods exist, and for some of them, especially the TopoShapes, advanced operations like boolean union/difference/intersection are also available. Explore the contents of the Part module, as described in the [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) page, to know more.

The most basic object that can be created is a [Part Feature](Part_Feature.md), which has a simple **Placement** property, and basic properties to define its color and appearance.

Another simple object used in 2D geometrical objects is the [Part Part2DObject](Part_Part2DObject.md), which is the base of the [Sketcher SketchObject](Sketcher_SketchObject.md) and most [Draft elements](Draft_Workbench.md).

### See also 

-   [Topological data scripting](Topological_data_scripting.md)
-   [OpenCASCADE](OpenCASCADE.md)

## Test script 

Test the creation of [Part Primitives](Part_Primitives.md) with a script. <small>(v0.19)</small> 


```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

This script is located in the installation directory of the program, and can be examined to see how the basic primitives are built.


```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

## Examples

### Line

To create a line element switch to the [Python console](Python_console.md) and enter   *


```python
import FreeCAD as App
import Part

doc = App.newDocument()

line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
obj = doc.addObject("Part   *   *Feature", "Line")
obj.Shape= line.toShape()

doc.recompute()
```

Let\'s go through the above Python example step by step   *


```python
import FreeCAD as App
import Part
doc = App.newDocument()
```

This loads the FreeCAD and Part modules and creates a new document.


```python
line = Part.LineSegment()
line.StartPoint = (0.0, 0.0, 0.0)
line.EndPoint = (1.0, 1.0, 1.0)
```

Line is actually a line segment, hence the start and endpoint.


```python
obj = doc.addObject("Part   *   *Feature", "Line")
obj.Shape= line.toShape()
```

This adds a Part object type to the document and assigns the shape representation of the line segment to the {{Incode|Shape}} property of the added object. It is important to understand here that we use a geometric primitive (the {{Incode|Part.LineSegment}}) to create a TopoShape out of it (with the {{Incode|toShape()}} method). Only shapes can be added to the document. In FreeCAD geometric primitives are used as \"building structures\" for shapes.


```python
doc.recompute()
```

Updates the document. This also prepares the visual representation of the new Part object.

Note that a line segment can also be created by specifying its start and endpoint directly in the constructor, for example {{Incode|Part.LineSegment(point1, point2)}}, or we can create a default line and set its properties afterwards, as we did here.

A Line can also be created using   *


```python
import FreeCAD as App
import Part

def my_create_line(pt1, pt2, obj_name)   *
    obj = App.ActiveDocument.addObject("Part   *   *Line", obj_name)
    obj.X1 = pt1[0]
    obj.Y1 = pt1[1]
    obj.Z1 = pt1[2]

    obj.X2 = pt2[0]
    obj.Y2 = pt2[1]
    obj.Z2 = pt2[2]

    App.ActiveDocument.recompute()
    return obj

line = my_create_line((0, 0, 0), (0, 10, 0), "LineName")
```

### Circle

A circle can be created in a similar way   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

circle = Part.Circle() 
circle.Radius = 10.0  
obj = doc.addObject("Part   *   *Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Or using   *


```python
import FreeCAD as App
import Part

def my_create_circle(rad, obj_name)   *
    obj = App.ActiveDocument.addObject("Part   *   *Circle", obj_name)
    obj.Radius = rad

    App.ActiveDocument.recompute()
    return obj

circle = my_create_circle(5.0, "CircleName")
```

Alternatively we can create a circle by defining its center, axis and radius   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

center = App.Vector(1, 2, 3)
axis = App.Vector(1, 1, 1)
radius = 10
circle = Part.Circle(center, axis, radius)
obj = doc.addObject("Part   *   *Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Or by defining three points on its circumference   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(0, 0, 10)
circle = Part.Circle(p1, p2, p3)
obj = doc.addObject("Part   *   *Feature", "Circle")
obj.Shape = circle.toShape()

doc.recompute()
```

Note again, we used the circle (geometric primitive) to construct a shape. We can of course still access our construction geometry afterwards, by doing   *


```python
shape = obj.Shape
edge = shape.Edges[0]
curve = edge.Curve
```

Here we take the {{Incode|Shape}} of our object {{Incode|obj}} and then its list of {{Incode|Edges}}. In this case there will be only one edge because we made the shape out of a single circle. So we take only the first item in the {{Incode|Edges}} list, and then take its curve. Every edge has a {{Incode|Curve}}, which is the geometric primitive it is based on.

### Arc

An arc can be created like this   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
arc = Part.Arc(p1, p2, p3)
obj = doc.addObject("Part   *   *Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

This draws a half circle. The center is at (0, 0, 0). The radius is 10. P1 is the start point on +X axis. P2 is the middle point on +Y axis and P3 is the end point on -X axis.

We can also create an arc from a circle   *


```python
import FreeCAD as App
import Part

doc = App.activeDocument()

p1 = App.Vector(10, 0, 0)
p2 = App.Vector(0, 10, 0)
p3 = App.Vector(-10, 0, 0)
circle = Part.Circle(p1, p2, p3)
arc = Part.ArcOfCircle(circle, 0.0, 0.7854)
obj = doc.addObject("Part   *   *Feature", "Arc")
obj.Shape = arc.toShape()

doc.recompute()
```

It needs a circle, and a start angle and end angle in radians.





 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Part](Part_Workbench.md) > Part scripting/pl
