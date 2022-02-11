---
- GuiCommand:
   Name:Part Circle
   MenuLocation:Part → [Create primitives](Part_Primitives.md) → Circle
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:
---

# Part Circle

## Description

This command will create a circular curved edge. With the default values, the circular curved edge will be closed and therefore will be a circle. If the properties Angle 0 or Angle 1 are changed from their default values (0 and 360) the edge will be an open curve, an arc.

Alternatively a Part Circle can be initially defined from three points. Once created the circle will only contain the standard Part Circle properties and will no longer contain a reference to the creation points.

## Usage

A Circle geometric primitive is available from the Create Primitives dialogue in the Part workbench.

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md)
2.  There are several ways to access the Create Primitives dialogue:
    -   Press the <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Primitives](Part_Primitives.md) button located in the Part toolbar
    -   Use the **Part → [Create primitives](Part_Primitives.md) → Circle**

## Properties

-    {{Parameter|Radius}}: the radius of the curved edge (arc or circle)

-    {{Parameter|Angle 0}}: start of the curved edge, (degrees anti-clockwise), the default value is 0

-    {{Parameter|Angle 1}}: end of the curved edge, (degrees anti-clockwise), the default value is 360

## Notes

## Properties 

## Limitations

## Scripting

A Part Circle can be created with the following function:

 
```python
circle = FreeCAD.ActiveDocument.addObject("Part::Circle", "myCircle")
```

-   Where {{Incode|"myCircle"}} is the name for the object.
-   The function returns the newly created object.

The name of the object can be easily changed by

 
```python
circle.Label = "new circleName"
```

You can access and modify attributes of the {{Incode|circle}} object. For example, you may wish to modify the radius, angle 0 and angle 1 parameters.

 
```python
circle.Radius = 10
circle.Angle0 = 45
circle.Angle1 = 225
```

The result will be a 45 degree rotated semicircle with a radius of 10.

You can change its placement and orientation with:

 
```python
circle.Placement = FreeCAD.Placement(FreeCAD.Vector(2, 4, 6), FreeCAD.Rotation(30, 45, 10))
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Circle
