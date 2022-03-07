---
- GuiCommand:/ru
   Name:Part Offset2D
   Name/ru:Part Offset2D
   MenuLocation:Деталь → 2D смещение
   Workbenches:[Part](Part_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Part Offset 3D](Part_Offset/ru.md), [Part Thickness](Part_Thickness/ru.md), [Draft Offset](Draft_Offset/ru.md)
---

# Part Offset2D/ru


</div>

## Description

Part 2D Offset constructs a wire, parallel to the original wire, at a certain distance from it. Or enlarges/shrinks a planar face, similarly.

The wire/face must be planar. There can be multiple wires in one object, not necessarily coplanar.

![600px](images/Part_Offset2D_Demo.png)

## Usage

1.  Select an object to offset
2.  Press the **[<img src=images/Part_Offset2D.svg style="width:24px">** **Offset2D** button.
3.  Set up the offset in the [Task Panel](Task_panel.md).
4.  Press **OK**.

A 2D Offset parametric object is created. Original objects are switched to wireframe display mode.

## Свойства

-    **Source**: Link to original shape

-    **Value**: The distance to enlarge the wire/face by. If negative, the wire/face is shrunk instead.

-    **Mode**(\"Pipe\" or \"Skin\"): sets how non-closed wires are processed. If \"Pipe\", the wire is outlined as if it was an extremely thin closed contour. If \"Skin\", an open wire is created.

:   ![600px](images/Part_Offset2D_Mode.png)

-    **Join**(\"Arc\", \"Tangent\", \"Intersection\"): sets the behavior around kinks. If \"Arc\", offset segments are connected with an arc of circle, centered at the vertex. \"Tangent\" is unsupported on OCC7.0.0. \"Intersection\": offset segments are extended till they intersect.

:   ![600px](images/Part_Offset2D_Join.png)

-    **Intersection**(\"false\", \"true\"): sets if multiple wires are treated collectively or independently. If \"false\", wires are offset independently, intersections between resulting wires are ignored. If \"true\", the wires are offset in collective manner.

:   ![600px](images/Part_Offset2D_Intersection.png)





:   Only wires within a compound are coupled. For example, if the structure is like compound(wire1, wire2, compound(wire3, wire4)), wire1 and wire2 will be treated collectively, but independently from wire3 and wire4. Likewise, wire3 and wire4 are treated collectively, but independently of wire1+wire2.





:   Also, in collective mode, directions of wires are important, and influence direction of offset. This is in tight relationship with how holes in faces are treated.





:   Wires being treated collectively must be coplanar. Wires being offset independently don\'t have to be coplanar.

-    **Fill**(\"false\", \"true\"): if \"true\", the space between original wire/face and the offset is filled with a face.

:   ![600px](images/Part_Offset2D_Fill.png)

## Known issues 

-   Most of non-default modes will only work with OCC 7.0.0 or later.

-   Using the tool can crash FreeCAD (see next point). On Windows, these crashes are converted to exceptions and don\'t generally cause FreeCAD to close; on other OS\'es it is not the case, so it is advisable to save project before attempting to use the tool. Ellipses are not handled either.

-   Enlarging faces with circular holes by an amount large enough to cause holes to close up, a crash occurs (OCC 7.0.0). The problem seems to be specific to circles; other shapes seem to close out properly.

-   When offsetting circles that have non-zero Placement, the result is placed wrongly. (OCC 7.0.0)

-   When offsetting circles, sometimes they are offset in unexpected direction (e.g. inward instead of outward). (OCC 7.0.0)

-   Fill=\"true\" doesn\'t work when collectively offsetting open wires in \"Skin\" mode

-   \"Tangent\" join mode doesn\'t work (OCC 7.0.0)

-   Offsetting wires made of single line segment is not supported (because line segment doesn\'t define a plane). Single line segments cannot participate in collective offset either.

## Программирование

The tool can by used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: {{code|code=
f = App.ActiveDocument.addObject("Part::Offset2D", "Offset2D")
f.Source =  #some object
f.Value = 10.0
}}

2D offset is also available as a method of Part.Shape. Example: {{code|code=
import Part
circle = Part.Circle().toShape()
enlarged_circle = circle.makeOffset2D(10.0)
Part.show(circle)
Part.show(enlarged_circle)
# makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection = false)
# 
# * offset: distance to expand the shape by. 
# 
# * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
# intersection
# 
# * fill: if true, the output is a face filling the space covered by offset. If
# false, the output is a wire/face.
# 
# * openResult: True for "Skin" mode; False for Pipe mode. 
# 
# * intersection: collective offset
# 
# Returns: result of offsetting (wire or face or compound of those). Compounding
# structure follows that of source shape.
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset2D/ru
