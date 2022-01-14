# Part TopoShape
## Introduction

A [Part TopoShape](Part_TopoShape.md), or formally a `Part::TopoShape`, is a class that defines a parametric **topological shape** in the software. Objects in the document that show something in the [3D view](3D_view.md) normally have a TopoShape.

The topological shapes, as well as their methods, are defined by the [OpenCASCADE Technology](OpenCASCADE.md) kernel (OCCT). FreeCAD uses these shapes, and builds [App DocumentObjects](App_DocumentObject.md) around them.

Another type of class is that of [meshes](Mesh.md); this class is not very parametric because it can\'t be redefined easily except by specifying individual vertices and triangular surfaces.

![](images/Shape_and_mesh.svg )



*Left: parametric [Part TopoShape](Part_TopoShape.md) defined by properties. Right: non-parametric [mesh](Mesh.md), defined by vertices and triangular surfaces.*

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `Part::TopoShape* class is embedded in the {{incode|Part::Feature` object and from there it is propagated to all objects that are derived from it.}}

## Usage

The Part TopoShape is an object that is assigned to some [App DocumentObjects](App_DocumentObject.md).

In particular, the basic object that handles these types of attributes is the [Part Feature](Part_Feature.md) (`Part::Feature` class). All objects derived from this class will have access to a Part TopoShape.

Some of the most important objects with Part TopoShape are the following:

-   Any primitive solid created with the [Part Workbench](Part_Workbench.md).
-   Any [PartDesign Body](PartDesign_Body.md) and [PartDesign Feature](PartDesign_Feature.md) created with the [PartDesign Workbench](PartDesign_Workbench.md).
-   Any object derived from [Part Part2DObject](Part_Part2DObject.md), like most objects created with the [Draft Workbench](Draft_Workbench.md).
-   Any [sketch](Sketch.md), that is, [Sketcher SketchObject](Sketcher_SketchObject.md), created with the [Sketcher Workbench](Sketcher_Workbench.md).
-   Any object created by importing a STEP, BREP, and similar solid format files.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

All objects derived from  
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Box", "Box")
print(obj.Shape)
```

A TopoShape has many attributes (variables) and methods that contain information about it, and which allow doing operations with it. These variables and methods can be tested in the [Python console](Python_console.md).  
```python
print(obj.Shape.Area)
print(obj.Shape.BoundBox)
print(obj.Shape.CenterOfMass)
print(obj.Shape.ShapeType)

obj.Shape.check()
obj.Shape.copy()
obj.Shape.exportStep("my_file.step")
obj.Shape.exportStl("my_file.stl")
```

For a full list of attributes and methods, consult the [source documentation](Source_documentation.md), and the **[<img src=images/Std_PythonHelp.svg style="width:16px"> [Std PythonHelp](Std_PythonHelp.md)** tool.

You can obtain a quick summary of all methods using Python\'s built-in  
```python
help(obj.Shape)
```

  {{Document objects navi}}

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part TopoShape
