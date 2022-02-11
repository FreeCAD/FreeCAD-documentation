---
- GuiCommand:
   Name:Part Ellipse
   MenuLocation:Part → [Create primitives](Part_Primitives.md) → Ellipse
   Workbenches:[Part](Part_Workbench.md), [OpenSCAD](OpenSCAD_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Ellipse

## Description

This command will create a elliptical curved edge. With the default values, the elliptical curved edge will be closed and therefore will be an ellipse. If the properties Angle 1 or Angle 2 are changed from their default values (0 and 360) the edge will be an open curve.

## Usage

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md)
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Primitives.svg" width=16px> [Primitives](Part_Primitives.md)** button.
    -   Select the **Part → [Create primitives...](Part_Primitives.md) → Ellipse** from the menu bar.

## Properties

-   **Major radius:** the major radius of the ellipse, the default value is 4
-   **Minor radius:** the minor radius of the ellipse, the default value is 2
-   **Angle0:** start of the edge of the ellipse or elliptical curved edge, (degrees anti-clockwise), the default value is 0
-   **Angle1:** end of the edge of the ellipse or elliptical curved edge, (degrees anti-clockwise), the default value is 360

## Notes

## Properties 

## Limitations

## Scripting

A Part Ellipse can be created with the following function:

 
```python
ellipse = FreeCAD.ActiveDocument.addObject("Part::Ellipse", "myEllipse")
```

-   Where {{Incode|"myEllipse"}} is the name for the object.
-   The function returns the newly created object.

You can access and modify attributes of the {{Incode|ellipse}} object.

The name of the object can be easily changed by

 
```python
ellipse.label = "new ellipseName"
```

For example, you may wish to modify the two radii and angles of the ellipse.

 
```python
ellipse.MajorRadius = 20
ellipse.MinorRadius = 10
ellipse.Angle0 = 45
ellipse.Angle1 = 135
```

The result will be a part of an ellipse.

You can change its placement and orientation with:

 
```python
ellipse.Placement = FreeCAD.Placement(FreeCAD.Vector(2, 4, 6), FreeCAD.Rotation(30, 45, 10))
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Ellipse
