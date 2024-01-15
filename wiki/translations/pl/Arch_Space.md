---
 GuiCommand:
   Name: Arch Space
   MenuLocation: Arch , Space
   Workbenches: Arch_Workbench
   Shortcut: **S** **P**
   Version: 0.14
   SeeAlso: Arch_Wall, Arch_Structure
---

# Arch Space/pl

## Description

The Space tool allows you to define an empty volume, either by basing it on a solid shape, or by defining its boundaries, or a mix of both. If it is based solely on boundaries, the volume is calculated by starting from the bounding box of all the given boundaries, and subtracting the spaces behind each boundary. The Space object always defines a solid volume. The floor area of a space object, calculated by intersecting a horizontal plane at the center of mass of the space volume, can also be displayed.

<img alt="" src=images/Arch_Space_example.jpg  style="width:640px;">



*Space object created from an existing solid object, then two wall faces are added as boundaries.*

## Usage

1.  Select an existing solid object, or faces on boundary objects.
2.  Invoke the Arch Space command using several methods:
    -   Pressing the **<img src="images/Arch_Space.svg" width=16px> [Arch Space](Arch_Space.md)** button in the toolbar.
    -   Using the **S** then **P** keyboard keys
    -   Using the **Arch → Space** entry from the top menu

### Limitations

-   The boundaries properties is currently not editable via GUI.
-   See the [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4275).

## Properties

-    **Base**: The base object, if any (must be a solid)

-    **Boundaries**: A list of optional boundary elements

-    **Area**: The computed floor area of this space

-    **FinishFloor**: The finishing of the floor of this space

-    **FinishWalls**: The finishing of the walls of this space

-    **FinishCeiling**: The finishing of the ceiling of this space

-    **Group**: Objects that are included inside this space, such as furniture

-    **SpaceType**: The type of this space

-    **FloorThickness**: The thickness of the floor finish

-    **NumberOfPeople**: The number of people who typically occupy this space

-    **LightingPower**: The electric power needed to light this space in Watts

-    **EquipmentPower**: The electric power needed by the equipment of this space in Watts

-    **AutoPower**: If True, Equipment Power will be automatically filled by the equipment included in this space

-    **Conditioning**: The type of air conditioning of this space

-    **Internal**: Specifies if this space is internal or external

-    **Text**: The text to show. Use \$area, \$label, \$tag, \$floor, \$walls, \$ceiling to insert the respective data

-    **FontName**: The name of the font

-    **TextColor**: The color of the text

-    **FontSize**: The size of the text

-    **FirstLine**: The size of the first line of text (multiplies the font size. 1 = same size, 2 = double size, etc..)

-    **LineSpacing**: The space between the lines of text

-    **TextPosition**: The position of the text. Leave (0,0,0) for automatic position

-    **TextAlign**: The justification of the text

-    **Decimals**: The number of decimals to use for calculated texts

-    **ShowUnit**: Show the unit suffix or not

## Options

-   To create zones that group several spaces, use an [Arch BuildingPart](Arch_BuildingPart.md) and set its IFC type to \"Spatial Zone\".
-   The Space object has the same display modes as other Arch and Part objects, with one more, called **Footprint**, that displays only the bottom face of the space.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Space tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Space = makeSpace(objects=None, baseobj=None, name="Space")
```

-   Creates a `Space` object from the given `objects` or `baseobj`, which can be
    -   one document object, in which case it becomes the base shape of the Space object, or
    -   a list of selection objects as returned by `FreeCADGui.Selection.getSelectionEx()`, or
    -   a list of tuples `(object, subobjectname)`

Example:


```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 1000
Box.Height = 1000

Space = Arch.makeSpace(Box)
Space.ViewObject.LineWidth = 2
FreeCAD.ActiveDocument.recompute()
```

After a space object is created, selected faces can be added to it with the following code:


```python
import FreeCAD, FreeCADGui, Draft, Arch

points = [FreeCAD.Vector(-500, 0, 0), FreeCAD.Vector(1000, 1000, 0)]
Line = Draft.makeWire(points)
Wall = Arch.makeWall(Line, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select a face of the wall
selection = FreeCADGui.Selection.getSelectionEx()
Arch.addSpaceBoundaries(Space, selection)
```

Boundaries can also be removed, again by selecting the indicated faces:


```python
selection = FreeCADGui.Selection.getSelectionEx()
Arch.removeSpaceBoundaries(Space, selection)
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Space/pl
