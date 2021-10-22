---
- GuiCommand:
   Name:Std Placement
   MenuLocation:Edit → Placement...
   Workbenches:All
   SeeAlso:[Std Alignment](Std_Alignment.md), [Placement](Placement.md)
---

# Std Placement

## Description

The **Std Placement** command displays the Placement [task panel](Task_panel.md) for a selected object.

 ![](images/Std_Placement_taskpanel.png )  
*The Placement task panel*

## Usage

1.  Select a single object that has a **Placement** property in the [property editor](Property_editor.md).
2.  Select the **Edit → Placement...** option from the menu.
3.  Change one or more of the translation and rotation parameters.
4.  Do one of the following:
    -   Press the **OK** button to apply the changes and close the task panel.
    -   Press the **Apply** button to apply the changes, but keep the task panel open for further changes.
5.  Press **Esc** or the **Cancel** button to abort the operation. This will undo any changes that have not been applied.

The dialog can also be launched by clicking on the ellipsis button **...** that appears in the [property editor](Property_editor.md) when you click on the **Placement** property.

## Notes

-   For more information about the placement parameters see the [Placement](Placement.md) page, and the [Aeroplane](Aeroplane.md) tutorial.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

See the [Python scripting tutorial](Python_scripting_tutorial#Vectors_and_placements.md).

A placement is internally defined by a matrix; in many cases it is simpler to represent it by means of two components, a `Base` point (vector), and a `Rotation` value. The `Rotation` itself has different representations; it can be entirely defined by the value of a \"[quaternion](https://en.wikipedia.org/wiki/Quaternion)\" `(xi + yj + zk + w)`, but it can also be described by a rotation `Axis` (unit vector) and a rotation `Angle` (radians).

 
```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Cylinder", "Cylinder")

print(obj.Placement)
# Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
print(obj.Placement.Base)
# Vector (0.0, 0.0, 0.0)
print(obj.Placement.Rotation)
# Rotation (0.0, 0.0, 0.0, 1.0)

print(obj.Placement.Rotation.Angle)
# 0.0
print(obj.Placement.Rotation.Axis)
# Vector (0.0, 0.0, 1.0)
print(obj.Placement.Rotation.Q)
# (0.0, 0.0, 0.0, 1.0)
```

Move the base point of the object, then rotate the object 45 degrees around the X axis.  
```python
import math

obj.Placement.Base = App.Vector(5, 3, 1)
obj.Placement.Rotation.Axis = App.Vector(1, 0, 0)
obj.Placement.Rotation.Angle = math.radians(45)

print(obj.Placement)
# Placement [Pos=(5,3,1), Yaw-Pitch-Roll=(0,0,45)]
print(obj.Placement.Rotation.Q)
# (0.3826834323650898, 0.0, 0.0, 0.9238795325112867)
print(obj.Placement.Matrix)
# Matrix ((1,0,0,5),(0,0.707107,-0.707107,3),(0,0.707107,0.707107,1),(0,0,0,1))
```




 {{Std Base navi}}

---
[documentation index](../README.md) > Std Placement
