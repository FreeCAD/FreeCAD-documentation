---
 GuiCommand:
   Name: Arch CutPlane
   MenuLocation: Arch , Cut Plane
   Workbenches: Arch_Workbench
   SeeAlso: Arch_CutLine, Arch_Remove
---

# Arch CutPlane/pl

## Description

The Cut Plane tool allows you to cut an Arch object according to a plane:

-   You can cut an Arch object with the selected face, normal or opposite of the face plane.
-   This add a subtraction component CutVolume to the Arch object

<img alt="" src=images/Arch_CutPlane_example.jpg  style="width:640px;">



*Left: Before applying the CutPlane tool. Middle: resulting wall after the cut is done. Right: yet another optional result*

## Usage

1.  Select the object to be cut, then the face (the face must be the last one you selected, and must be selected in the [3D View](3D_View.md)).
2.  Press the **<img src="images/Arch_CutPlane.svg" width=24px> [Cut Plane](Arch_CutPlane.md)** button.
3.  Choose if the object is cut **behind** the normal face or in**front** of the normal face.
4.  Click the **OK** button.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The CutPlane tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
cutObj = cutComponentwithPlane(archObject, cutPlane, sideFace)
```

-   Creates a `cutObj` object from the given `archObject`, which is cut by `cutPlane`, which is the face of another object.
    -   
        `archObject`
        
        should be a `SelectionObject` obtained from `FreeCADGui.Selection.SelectionEx()[0]`.

    -   
        `cutPlane`
        
        should be a `FaceObject` obtained from `FreeCADGui.Selection.SelectionEx()[0].SubObjects[0]`.

-    `sideFace`specifies on which side of the `FaceObject` a volume will be created; this volume will then be used to subtract from the `archObject`. If `sideFace` is `0` it will create a volume in the rear of the face, otherwise it create it in front of the face.

Example: 
```python
import FreeCAD, FreeCADGui, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select the Wall
main_object = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall2
selection = FreeCADGui.Selection.getSelectionEx()[0]
cut_face = selection.SubObjects[0]

cutObj = Arch.cutComponentwithPlane(main_object, cut_face, 0)
FreeCAD.ActiveDocument.recompute()

Wall3 = Draft.move(Wall, FreeCAD.Vector(-4000, 0, 0), copy=True)
Wall4 = Draft.move(Wall2, FreeCAD.Vector(-4000, 0, 0), copy=True)
FreeCAD.ActiveDocument.recompute()

# Select the Wall3
main_object2 = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall4
selection2 = FreeCADGui.Selection.getSelectionEx()[0]
cut_face2 = selection2.SubObjects[0]

cutObj2 = Arch.cutComponentwithPlane(main_object2, cut_face2, 1)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CutPlane/pl
