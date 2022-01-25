---
- GuiCommand:/ru
   Name:Part_Offset
   Name/ru:Смещение 3D
   MenuLocation:Деталь → Смещение 3D
   Workbenches:[Верстак Part](Part_Workbench/ru.md)
   SeeAlso:[Толщина](Part_Thickness/ru.md)
---

# Part Offset/ru

## Описание

The Part 3D Offset tool creates parallel copies of a selected shape at a certain distance from the base shape, giving a new object.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">

## Применение

1.  Select the Object you want to create the offset from.
2.  Press the **<img src="images/Part_Offset.svg" width=16px> '''3D Offset'''** button
3.  Adjust distance and parameters depending on the original object and the resulting objects validity.

## Свойства

-    **Offset**: Distance to offset the faces of the shape

-    **Mode**: Mode of creation . Skin creates a new shape around the source shape. Pipe ( todo ) . RectoVerso ( todo )

-    **Join type**: How the new corners are build up. Intersection gives sharp corners by linear extension of the edges. Arc and Tangent give rounded corners.

1.  Option ː Intersection ː Allows offsets pointing inwards to \"overflood\" the gap by intersecting the resulting shape until opposite faces are reached.
2.  Option ː Self Intersection ː ( todo )
3.  Option ː Fill Offset ː When the shape was 2 dimensional , the gap inbetween the 2 shapes gets filled. The fill is now a solid, hence the source shape is not a solid . Thus boolean operations may lead to strange results. (see example below) .


<div class="mw-translate-fuzzy">

## Пример


</div>

Object with small offset and rounded ( arc ) corners.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;"> 

Same object with sharp ( intersection ) corners.

<img alt="" src=images/PartOffset3.png  style="width:400" height="200px;"> 

Same object with thick distance overfilling the front left gap and allowed intersections.

<img alt="" src=images/PartOffset2.png  style="width:400" height="200px;"> 

Arbitrary shape ( draft poly as wire ) with a 3D Offset ( ignores MODE param )

<img alt="" src=images/PartOffset4.png  style="width:400" height="200px;"> 

same shape with a 3D Offset as SKIN and *filled* offset

<img alt="" src=images/PartOffset5.png  style="width:400" height="200px;"> 

*filled* offset with 2 Cylinders creating boolean cuts. Cylinder A goes through the FILL whilst Cylinder B only goes thru the FILL and NOT through the source 2D shape.

<img alt="" src=images/PartOffset6.png  style="width:400" height="200px;">



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/ru
