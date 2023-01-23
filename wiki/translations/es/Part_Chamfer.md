# Part Chamfer/es
---
- GuiCommand:/es   Name:Part_Chamfer   MenuLocation:Pieza → Chaflán   Workbenches:Pieza,Completo---


</div>

## Description


<div class="mw-translate-fuzzy">

Crea chaflanes en las aristas de un objeto. Un letrero de diálogo te permite seleccionar que objetos y en que aristas trabajar.


</div>

![Chamfer example](images/Chamfer-example.png )

## Usage


<div class="mw-translate-fuzzy">

![](images/Dialog-chamfer.jpg )


</div>

## Options

![Dialog-chamfer](images/Dialog-chamfer.png )

-   When selecting edges on the model, you have the option to select by edge or by face. Selecting by face will select all bordering edges of that face.
-   Constant length chamfer or variable length chamfer.
    -   A constant length chamfer will create a chamfer with edges equidistant to the original edge at the distance specified.
    -   A variable length chamfer will have edges that may be set to different distances from the original edge, allowing you to create a chamfer at a variable angle.

## Properties

![Part Chamfer Properties](images/Part_Chamfer-Properties.png ) 


{{Properties_Title|Base}}

-    **Base**: The shape onto which the chamfer is to be applied.

-    **Placement**: Specifies the orientation and position of the shape in the 3D space.

-    **Label**: Label given to the object. Change to suit your needs.




## Limitations

Chamfer might do nothing if the result would touch or cross the next adjacent edge. So if you do not get the expected result, try with a smaller value. This is the same for <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Fillet](Part_Fillet.md).

Also note that the Chamfer feature is affected by the [Topological naming problem](Topological_naming_problem.md) when the any change is done to a modeling step earlier in the chain that affects the number of facets or vertices. This could cause unpredictable result. Until that is resolved it is advised to apply Chamfer and <img alt="" src=images/Part_Fillet.svg  style="width:24px;"> [Part Fillet](Part_Fillet.md) operations at the last steps in the chain.

## Scripting

The Chamfer tool can by used in [macros](Macros.md) and from the [Python](Python.md) console by adding a Chamfer object to the document.

**Example Script:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
chmfr.Base = FreeCAD.ActiveDocument.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
FreeCADGui.ActiveDocument.myCube.Visibility = False
FreeCAD.ActiveDocument.recompute()
```

**Example Script Explanation:**


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part::Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
```

-   Creates a 5 mm cube for us to apply chamfered edges to. See [Part_API](Part_API.md) for an explanation of the makeBox method.


```python
chmfr = FreeCAD.ActiveDocument.addObject("Part::Chamfer", "myChamfer")
```

-   Adds a new object to the document of type Chamfer (from the Part module) with label \"myChamfer\".


```python
chmfr.Base = FreeCAD.ActiveDocument.myCube
```

-   Specifies that the base shape of the chamfer object should be \"myCube\".


```python
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
```

-   Creates an empty array \"myEdges\" and then appends the array with each edge\'s chamfer parameters.
-   Syntax for each item should be (edge#, chamfer start length, chamfer end length)


```python
chmfr.Edges = myEdges
```

-   Sets the Edges attribute of our Chamfer object equal to the array we just created.


```python
FreeCADGui.ActiveDocument.myCube.Visibility = False
```

-   This line simply hides \"myCube\" so that our newly created \"myChamfer\" object is the only one visible.


```python
FreeCAD.ActiveDocument.recompute()
```

-   Recomputes all altered components on the screen and refreshes the display.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Chamfer/es
