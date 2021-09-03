---
- GuiCommand:   Name:Part CreatePrimitives   Workbenches:[OpenSCAD](Part_Workbench___Part]],_[[OpenSCAD_Workbench.md)|MenuLocation:[Part](Part_Workbench.md) → [Create Primitives](Part_CreatePrimitives.md) → Plane|
SeeAlso=[Create Primitives](Part_CreatePrimitives.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Create a simple parametric plane 10 x 10 mm, with the parameters of position, length, and width. By default, the plane is positioned at the origin (0,0,0).


</div>

![](images/PartPlane.png )


<div class="mw-translate-fuzzy">

## Cum se utilizează 

The standard plane is created with its lower left corner at the origin point 0,0,0. To change these parameters, open the Location section and enter the desired values ​​in the respective input fields, or click on the 3D view and select a point, the point coordinates are taken from the fields. In the Direction menu you can also define a standard vector (X, Y or Z) normal to the plane, or click User Defined \... to open the dialog box that allows you to set a different carrier (eg direction 1.0 , -1 creates a plane inclined 45 ° with respect to X and Z).


</div>

The standard plane is created with its lower left corner at the origin point `0,0,0`. To change these parameters, open the Location section and enter the desired values ​​in the respective input fields, or click on the [3D view](3D_view.md) and select a point, the point coordinates are taken from the fields. In the Direction menu you can also define a standard vector (X, Y or Z) normal to the plane, or click User Defined \... to open the dialog box that allows you to set a different carrier (eg. direction 1.0 , -1 creates a plane inclined 45° with respect to X and Z).


<div class="mw-translate-fuzzy">

The properties can be changed later in the **Combined View → Data**, after selecting the item.


</div>

## Properties

### Data


{{TitleProperty|Base}}

-    **Label**: String name of the object, defaults to \'Plane\'. User may rename it.

-    **Placement**: Placement of feature is defined by below angle, axis and position.

-    **Angle**: Angle of rotation relative to the below axis.

-    **Axis**: Defines the axis of rotation plane: X, Y, or Z. Defaults to Z axis, Z = 1

-    **Position**: Position X, Y, Z, relative to the origin 0, 0, 0.


{{TitleProperty|Plane}}

-    **Length**: Length is the dimension along the X axis The default value is 10 mm

-    **Width**: Width is the size of the Y-axis The default value is 10 mm

### View

You have the standard properties view.





 
