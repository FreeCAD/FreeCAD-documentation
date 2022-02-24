---
- GuiCommand:
   Name:Part Point
   MenuLocation:Part → [Create primitives](Part_Primitives.md) → Point
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Primitives](Part_Primitives.md)
---

# Part Point

## Description

The <img alt="" src=images/Part_Point.svg  style="width:24px;"> [Part Point](Part_Point.md) command creates a point.

FreeCAD creates a point (vertex) geometric primitive, that is positioned at the origin (0,0,0).

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Primitives.svg" width=16px> [Create Primitives...](Part_Primitives.md)** button.
    -   Select the **Part → Create Primitives → <img src="images/Part_Primitives.svg" width=16px> Create Primitives...** option from the menu.
    -   Select the **<img src="images/Part_Point.svg" width=16px> Point** option from the menu.
2.  Set options and press **Create**.
3.  To close the dialog press **Close**.

## Properties

See also: [Property editor](Property_editor.md).

A Part Point object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties.

## Scripting

A Part Point is created with the {{Incode|addObject()}} method of the document.

 
```python
point = App.ActiveDocument.addObject("Part::Vertex", "myPoint")
```

-   Where {{Incode|myPoint}} is the name for the object. The name must be unique for the entire document.
-   The function returns the newly created object.

The {{Incode|Label}} is the user editable name for the object. It can be easily changed by

 
```python
point.Label = "new myPointName"
```

You can access and modify attributes of the {{Incode|point}} object. For example, you may wish to modify the x, y or z-coordinate.

 
```python
point.X = 1
point.Y = 2
point.Z = 3
```

The result will be a new location of the point with the given coordinates.

You can change its placement and orientation with:

 
```python
point.Placement= App.Placement(App.Vector(1,2,3), App.Rotation())
```




 {{Part_Tools_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Point
