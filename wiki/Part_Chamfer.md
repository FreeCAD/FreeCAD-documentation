---
- GuiCommand:
   Name: Part Chamfer
   MenuLocation: Part -> Chamfer...
   Workbenches: Part_Workbench
   SeeAlso: Part_Fillet
---

# Part Chamfer

## Description

**Part Chamfer** chamfers the selected edge(s) of an object. A dialog allows you to choose which edge(s) to work on as well as modify various chamfer parameters.

![Chamfer example](images/Chamfer-example.png )

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Chamfer.svg" width=16px> Chamfer...** button.
    -   Select the **Part → Chamfer...** option from the menu.
2.  Select the shape to chamfer from the dialog.
3.  Select edges to chamfer by checking the corresponding box in the chamfer dialog or by selecting them on the model directly.
4.  Edit chamfer parameters.
5.  Press **OK** to close the chamfer dialog and apply the chamfer.

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
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Chamfer
