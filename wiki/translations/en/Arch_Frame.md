---
 GuiCommand:
   Name: Arch Frame
   MenuLocation: 3D/BIM , Frame
   Workbenches: BIM_Workbench
   Shortcut: **F** **R**
   SeeAlso: 
---

# Arch Frame/en

## Description

The **Arch Frame** tool is used to build all kinds of frame objects based on a profile and a layout. The profile is extruded along the edges of the layout, which can be any 2D object such as a [sketch](Sketcher_Workbench.md), or a [Draft object](Draft_Workbench.md). It is especially useful to create railings, or frame walls. Frame objects can then easily be turned into [wall](Arch_Wall.md) or [structure](Arch_Structure.md) objects.

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;"> 
*Frame object created from a [Draft OrthoArray](Draft_OrthoArray.md) of a [Draft Line](Draft_Line.md), using a [Draft Circle](Draft_Circle.md) as profile*

## Usage

1.  Create a layout object and a profile object, for example with the [Draft Workbench](Draft_Workbench.md) or the [Sketcher Workbench](Sketcher_Workbench.md).
2.  Select the layout object first, then, with **Ctrl** pressed, select the profile object.
3.  Press the **<img src="images/Arch_Frame.svg" width=16px> [Frame](Arch_Frame.md)** button, or press **F** then **R** keys.

## Options

-   Frames share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The frame object can be placed at a certain distance from the layout object, by setting its Offset property
-   The profile will be copied at the base of each edge of the layout object, then extruded along it. You can control how the profile is placed at the base of each edge with the Align and Rotation properties.

## Properties

### Data


{{TitleProperty|Component}}

-    **Base|Link**: The layout this frame is based on.

For the other properties in the group see [Arch Component](Arch_Component#Properties.md).


{{TitleProperty|Frame}}

-    **Align|Bool**: Specifies if the profile must be rotated to have its normal axis aligned with each edge.

-    **Base Point|Integer**: Zero-based index indicating the crossing point of the path on the profile:

    -   
        {{Value|0}}
        
        : The **Base** of the **Placement** of the profile. This point is also used in case of an invalid index.

    -   
        {{Value|1}}
        
        : The midpoint of the 1st edge of the profile.

    -   
        {{Value|2}}
        
        : The endpoint of the 1st edge of the profile.

    -   
        {{Value|3}}
        
        : The midpoint of the 2nd edge of the profile.

    -   
        {{Value|4}}
        
        : The endpoint of the 2nd edge of the profile.

    -   \...

    -   
        {{Value|n*2-1}}
        
        : The midpoint of the nth edge of the profile.

    -   
        {{Value|n*2}}
        
        : The endpoint of the nth edge of the profile.

-    **Edges|Enumeration**: The type of edges to consider. The options are:

    -   
        {{Value|All edges}}
        

    -   
        {{Value|Vertical edges}}
        

    -   
        {{Value|Horizontal edges}}
        

    -   
        {{Value|Bottom horizontal edges}}
        
        : Based of the global Z coordinate of the center of mass of the edge.

    -   
        {{Value|Top horizontal edges}}
        
        : Idem.

-    **Fuse|Bool**: If true, overlapping solids are fused.

-    **Offset|VectorDistance**: An optional distance between the layout object and the frame object.

-    **Profile|Link**: The profile this frame is based on.

-    **Profile Placement|Placement**: An optional additional placement to add to the profile before extruding it. Only the **Rotation** of the **Placement** is used. Ignored if **Align** is `True`.

-    **Rotation|Angle**: The rotation of the profile around its extrusion axis.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Frame tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Frame = makeFrame(baseobj, profile)
```

-   Creates a `Frame` object from the given `baseobj` and `profile`.
    -   
        `baseobj`
        
        is any object containing wires, like a [Draft Wire](Draft_Wire.md), or a [Draft OrthoArray](Draft_OrthoArray.md) with a collection of them.

    -   
        `profile`
        
        is an extrudable 2D object containing faces or closed wires.

Example:


```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Frame/en
