---
- GuiCommand:
   Name:Part Offset
   MenuLocation:Part → 3D Offset
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Thickness](Part_Thickness.md), [Part 2D Offset](Part_Offset2D.md)
---

# Part Offset/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Offset Part 3D creează copii ale unei forme selectate la o anumită distanță față de forma de bază.


</div>

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

De completat


</div>

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as source objects. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

![](images/PartOffset1_it.png )  ![](images/PartOffset2_it.png ) 


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


<div class="mw-translate-fuzzy">

## Exemplu


</div>

-    **Offset**: Distance to offset the faces of the shape.

-    **Mode**: Mode of creation. Skin creates a new shape around the source shape. Pipe (todo). RectoVerso (todo).

-    **Join type**: How the new corners are build up. Intersection gives sharp corners by linear extension of the edges. Arc and Tangent give rounded corners.

1.  Option: Intersection: Allows offsets pointing inwards to \"overflow\" the gap by intersecting the resulting shape until opposite faces are reached.
2.  Option: Self Intersection: (todo).
3.  Option: Fill Offset: When the shape was 2 dimensional, the gap between the 2 shapes gets filled. The fill is now a solid, hence the source shape is not a solid. Thus boolean operations may lead to strange results. (see example below).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/ro
