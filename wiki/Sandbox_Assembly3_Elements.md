# Sandbox:Assembly3 Elements
Still not finished :-)




{{TOCright}}



Don't mark for translation yet!

## Introduction

-   **Elements** are the key objects in the **Assembly3** workbench. They provide **element coordinate systems** (ECSs) that are used to constrain elements to one another. (Referred to as implicit coordinate systems - ICSs - on the constraint pages)
-   Two part objects are linked by one or several pairs of constrained elements to determine position and orientation to one another.
-   Several linked part objects can add up to a link chain.
    -   A rigid assembly consists of a fully constrained link chain.
    -   A kinematic assembly has to be fully constrained, too, but some constraints can be used as actuators to change the shape of the link chain. The actuator values can be changed by hand in the properties editor or by an external macro.
-   To choose the combination of elements and constraints for a link chain properly, it is necessary to know how ECSs are placed.

## Elements

Elements (Assembly3 element objects) are mainly 3D representations of an object\'s boundary representation such as:

-   Face elements
-   Line elements
-   Point elements

Further elements are used to create 2D skeleton sketches:

-   Workplanes
-   2D lines
-   2D points

To get a few examples some elements have to be extracted from a sample body. The <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width:16px;"> [Create element](Assembly3_CreateElement.md) command is used for this task.

### Face elements 

Face elements can be extracted from planar faces, cylindrical faces, or 3D bent faces.

 <img alt="" src=images/Assembly3_CreateElement-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-04.png  style="width:200px;"> , <img alt="" src=images/Assembly3_CreateElement-05.png  style="width:200px;"> , <img alt="" src=images/Assembly3_CreateElement-06.png  style="width:200px;"> 



*Sample body -> planar face elements, cylindrical face elements, 3D bent face elements*

### Line elements 

Line elements can be extracted from straight lines, arcs, or circles.

 <img alt="" src=images/Assembly3_CreateElement-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-07.png  style="width:200px;"> , <img alt="" src=images/Assembly3_CreateElement-08.png  style="width:200px;"> 



*Sample body -> straight line elements, curved line elements*

### Point elements 

Point elements can be extracted from any vertex e.g. line ends.

 <img alt="" src=images/Assembly3_CreateElement-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-09.png  style="width:200px;"> 



*Sample body -> point elements*

### Workplanes

### 2D line elements 

### 2D point elements 

## Main Coordinate System (MCS) 

Each FreeCAD document has its own coordinate system to provide an origin and the three axes that are use to position all geometry contained in the document.

The <img alt="" src=images/Std_AxisCross.svg  style="width:16px;"> [AxisCross](Std_AxisCross.md) command toggles its visibility.

It is the main coordinate system (MCS) of the document and it is represented by 3 arrows which meet at the documents origin:

-   a red arrow for the X axis
-   a green arrow for the Y axis
-   a blue arrow for the Z axis

 <img alt="" src=images/Assembly3_CreateElement-10.png  style="width:200px;"> 

## Element Coordinate System (ECS) 

Geometry doesn\'t have to be positioned on or near the **MCS** and so it can be quite useless when objects need to be assembled.

In automotive design a MCS represents the global coordinate system (GCS) of a specific model (usually the center of a virtual front axle) and a local coordinate system (LCS) provides the basis to create model specific parts in situ. A standard part like e.g. a fastener in contrast doesn\'t have a GCS and its MCS presents its LCS.

To assemble two objects Assembly3 tools use the **element coordinate systems** (ECSs) of elements extracted from the objects\' boundary representations.

Sometimes linked objects don\'t behave as expected and this can be due to the placement of the ECSs.  To have a look at the ECSs they have to be visible:

### ECS Visibility 

Activate the <img alt="" src=images/Assembly_ShowElementCS.svg  style="width:16px;"> **Show element coordinate system** function (toggle) and deactivate the <img alt="" src=images/Assembly_AutoElementVis.svg  style="width:16px;"> **Auto element visibility** function (toggle) to have several ECSs permanently visible.

 <img alt="" src=images/Assembly3_CreateElement-02.png  style="width:400px;"> 



*Toggled as described*

### Point element ECS 

An ECS of a **point element** i.e. its origin is located at the same position as the point itself and its axes are parallel to the axes of the MCS.

 <img alt="" src=images/Assembly3_CreateElement-11.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-12.png  style="width:300px;"> 



*Part as created -> part turned 30° around the Z axis*

To get a better view:

 <img alt="" src=images/Assembly3_CreateElement-13.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-14.png  style="width:300px;"> 



*Only point elements -> situation turned 30° around the Z axis*

Even if the part is turned the ECSs stay oriented parallel to the MCS.

### Line element ECS 

An ECS of a **straight line element** i.e. its origin is located in the middle of the line and its z axis is colinear to the line.

 <img alt="" src=images/Assembly3_CreateElement-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-16.png  style="width:300px;"> 



*Only straight line elements -> situation turned 30° around the Z axis*

When the part is turned the ECSs\' z axes stay colinear to their lines, but the direction of the other axes is almost not predictable.

The solver seems to try to align the remaining axes as good as possible to the main axes and so the ECS of the short line parallel to the main z axis keeps its orientation in this case.

An ECS of a **curved line element** (arc or circle) i.e. its origin is located in the center of the curve and its xy plane is coplanar to the curve.

 <img alt="" src=images/Assembly3_CreateElement-17.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-18.png  style="width:300px;"> 



*Only curved line element -> situation turned 30° around the Z axis*

When the part is turned the ECSs turn with the part and it seems like its x axis goes through the starting point of the curve i.e. it keeps its orientation according to the curve. That is only true for edges not created from sketches like the hole fillet. The other ECSs are oriented like the sketches which are the bases of their curved line elements.

### Face element ECS 

An ECS of a **planar face element** i.e. its origin is located at the face\'s center of area and its xy plane is coplanar to the face; and so the z axis is parallel to the face normal but it does not necessarily point to the part\'s outside.

 <img alt="" src=images/Assembly3_CreateElement-19.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-20.png  style="width:300px;"> 



*Only planar face elements -> situation turned 30° around the Z axis*

When the part is turned the ECSs turn the same way. Their orientations depend fully on their associated faces and not a bit on the MCS.

An ECS of a **cylindrical face element** i.e. its origin is located at the center of one circular edge and its z axis is colinear to the face\'s axis; but the z axis it does not necessarily point to the part\'s outside.

 <img alt="" src=images/Assembly3_CreateElement-21.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-22.png  style="width:300px;"> 



*Only cylindrical face elements -> situation turned 30° around the Z axis*

When the part is turned the ECSs turn the same way. Their orientations depend fully on their associated faces and not a bit on the MCS.

The circular edge that defines the position of the ECs\'s origin does not necessarily belong to the selected face. In case of the upper cut-out cylinder the sketch is defining the origin.

 <img alt="" src=images/Assembly3_CreateElement-23.png  style="width:300px;"> 

An ECS of a **90° fillet face element** i.e. its origin is located at the center of one circular edge and its xy plane is coplanar to the edge with its x axis going through the edge\'s starting point.

 <img alt="" src=images/Assembly3_CreateElement-24.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/Assembly3_CreateElement-25.png  style="width:300px;"> 



*Only cylindrical face elements -> situation turned 30° around the Z axis*

When the part is turned the ECSs turn the same way. Their orientations depend fully on their associated edges and not on the MCS.

This applies to circular edges like those of a cylinder or a cuboid fillet.

### Workplane ECS 

### 2D line element ECS 

### 2D point element ECS 

## Notes

1.  An element extracted from a sketch based boundary representation feature is likely to have an ECS oriented according to the sketche\'s x and y axes.
2.  A section



Dies ist eine Sandbox



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Assembly3](Category_Assembly3.md) > [Addons](Category_Addons.md) > Sandbox:Assembly3 Elements
