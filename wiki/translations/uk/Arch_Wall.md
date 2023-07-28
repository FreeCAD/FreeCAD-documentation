# Arch Wall/uk
---
- GuiCommand:/uk   Name:Arch Wall   Name/uk:Arch Wall   Workbenches:[MenuLocation:Arch → Wall   Shortcut:W A   SeeAlso:[[Arch Structure/uk|Arch Structure](Arch_Workbench/uk___Arch]].md)---


</div>

## Description

This tool builds a Wall object from scratch or on top of any other [shape](Part_Workbench.md)-based or [mesh](Mesh_Workbench.md)-based object. A wall can be built without any base object, in which case it behaves as a cubic volume, using length, width and height properties. When built on top of an existing shape, a wall can be based on:

-   A **linear 2D object**, such as lines, wires, arcs or sketches, in which case you can change thickness, alignment (right, left or centered) and height. The length property has no effect.
-   A **flat face**, in which case you can only change the height. Length and width properties have no effect. If the base face is vertical, however, the wall will use the width property instead of height, allowing you to build walls from space-like objects or mass studies.
-   A **solid**, in which case length, width and height properties have no effect. The wall simply uses the underlying solid as its shape.
-   A **mesh**, in which case the underlying mesh must be a closed, manifold solid.

<img alt="" src=images/Arch_Wall_example.jpg  style="width:780px;"> 
*Walls built from a line, a wire, a face, a solid, and a sketch*

Walls can also have additions or subtractions. Additions are other objects whose shapes are joined in this Wall\'s shape, while subtractions are subtracted. Additions and subtractions can be added with the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools. Additions and subtractions have no influence over wall parameters such as height and width, which can still be changed. Walls can also have their height automatic, if they are included into a higher-level object such as [floors](Arch_Floor.md). The height must be kept at 0, then the wall will adopt the height specified in the parent object.

When several walls should intersect, you need to place them into a [floor](Arch_Floor.md) to have their geometry intersected.

## Usage

### Drawing a wall from scratch 

1.  Press the **<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall.md)** button, or press **W** then **A** keys.
2.  Click a first point on the 3D view, or type coordinates.
3.  Click a second point on the 3D view, or type coordinates.

### Drawing a wall on top of a selected object 

1.  Select one or more base geometry objects (Draft object, sketch, etc)
2.  Press the **<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall.md)** button, or press the **W** then **A** keys
3.  Adjust needed properties such as height or width.

## Options

-   Walls share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The height, width and alignment of a wall can be set during drawing, via the task panel
-   When snapping a wall to an existing wall, both walls will be joined into one. The way the two walls are joined depends on their properties: If they have the same width, height and alignment, and if the option \"join base sketches\" is enabled in the Arch preferences, the resulting wall will be one object based on a sketch made of several segments. Otherwise, the latter wall will be added to the first one as addition.
-   Press **X**, **Y** or **Z** after the first point to constrain the second point on the given axis.
-   To enter coordinates manually, simply enter the numbers, then press **Enter** between each X, Y and Z component.
-   Press **R** or click the checkbox to check/uncheck the **Relative** button. If relative mode is on, the coordinates of the second point are relative to the first one. If not, they are absolute, taken from the (0,0,0) origin point.
-   Press **Shift** while drawing to [constrain](Draft_Constrain.md) your second point horizontally or vertically in relation to the first one.
-   Press **Esc** or the **Cancel** button to abort the current command.
-   Double-clicking on the wall in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions
-   Multi-layer walls can be easily created by building several walls from the same baseline. By setting their Align property to either left or right, and specifying an Offset value, you can effectively construct several wall layers. Placing a window in such a wall layer will propagate the opening to the other wall layers based on the same baseline.
-   Walls can also make use of [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the wall will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Wall\'s Width value, after subtracting the other layers.
-   Walls can be made to display blocks, instead of one single solid, by turning their **Make Blocks** property on. The size and offset of blocks can be configured with different properties, and the amount of blocks is automatically calculated.

## Snapping

Snapping works a bit differently with Arch walls than other Arch and Draft objects. If a wall has a baseline object, snapping will anchor to the base object, instead of the wall geometry, allowing to easily align walls by their baseline. If, however, you specifically want to snap to the wall geometry, pressing **Ctrl** will switch snapping to the wall object.

<img alt="" src=images/Arch_wall_snap.jpg  style="width:780px;"> 
*Second wall snapping perpendicularly to the first one*

## Properties

Wall objects inherit the properties of [Part](Part_Workbench.md) objects, and also have the following extra properties:

### Data


{{TitleProperty|Blocks}}

-    **Block Height**: The height of each block

-    **Block Length**: The length of each block

-    **Count Broken**: The number of broken blocks (read-only)

-    **Count Entire**: The number of entire blocks (read-only)

-    **Joint**: The size of the joints between each block

-    **Make Blocks**: Enable this to make the wall generate blocks

-    **Offset First**: The horizontal offset of the first line of blocks

-    **Offset Second**: The horizontal offset of the second line of blocks


{{TitleProperty|Component}}

-    **Base**: The base object this wall is built on


{{TitleProperty|Wall}}

-    **Align**: The alignment of the wall on its baseline: Left, Right or Center

-    **Area**:

-    **Face**: The index of the face from the base object to use. If the value is not set or 0, the whole object is used

-    **Height**: The height of the wall (not used when the wall is based on a solid). If no height is given, and the wall is inside a [floor](Arch_Floor.md) object with its height defined, the wall will automatically take the value of the floor height.

-    **Length**: The length of the wall (not used when the wall is based on an object)

-    **Normal**: An extrusion direction for the wall. If set to (0,0,0), the extrusion direction is automatic.

-    **Offset**: This specifies the distance between the wall and its baseline. Works only if the Align property is set to Right or Left.

-    **Override Align**:

-    **Override Width**:

-    **Width**: The width of the wall (not used when the wall is based on a face)

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Wall tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```

-   Creates a `Wall` object from the given `baseobj`, which can be a [Draft object](Draft_Workbench.md), a [Sketch](Sketcher_Workbench.md), a face, or a solid.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width` (thickness), and `height`.
    -   If given, `face` can be used to give the index of a face from the underlying object, to build this wall on, instead of using the whole object.

-    `align`can be `"Center"`, `"Left"` or `"Right"`.

-   It returns `None` if the operation fails.

Example:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Wall/uk
