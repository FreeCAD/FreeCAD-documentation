---
- GuiCommand:
   Name: Arch CurtainWall
   MenuLocation: Arch -> Curtain Wall
   Workbenches: Arch_Workbench
   Shortcut: **C** **W**
   Version: 0.19
   SeeAlso: Arch_Wall, Arch_Grid
---

# Arch CurtainWall/en

## Description

This tool creates a [curtain wall](https://en.wikipedia.org/wiki/Curtain_wall_(architecture)) by subdividing a base face into quadrangular faces, then creating vertical mullion on the vertical edges, horizontal mullions on the horizontal edges, and filling the spaces between mullions with panels.

<img alt="" src=images/Arch_CurtainWall_example.png  style="width:780px;">

Curtain Walls can be created from any type of existing object, in which case all the faces of the object will be subdivided. It works therefore best if used with an object that has only one face. Typically, you would first create a face, preferably bound by exactly 4 edges, that represents the area you want to fill with a curtain wall, then apply the tool.

Curtain walls can also be built from a linear object, such as a line, arc or polyline, like the normal [wall](Arch_Wall.md) tool.

Faces that have double curvature, or faces with more than 4 edges will work too, but the result is less predictable.

Faces will be divided in quadrangular facets. If the 4 points of the facet are coplanar, a square facet is created. If not, it is divided into two triangles and a diagonal mullion is added.

In case you need a non-regular subdivision, it is also possible to build your own subdivided object, for example using [Arch Grid](Arch_Grid.md), and set the vertical and horizontal subdivisions of the curtain wall to 1.

You can also use the curtain wall tool without any selected object, in which case you will be able to draw a baseline, which will the be extruded vertically to form the face on which the curtain wall will be built.

## Usage

### Drawing a curtain wall from scratch 

1.  Make sure nothing is selected
2.  Press the **<img src="images/Arch_CurtainWall.svg" width=16px> [CurtainWall](Arch_CurtainWall.md)** button, or press **C** then **W** keys.
3.  Click a first point on the 3D view, or type coordinates.
4.  Click a second point on the 3D view, or type coordinates.
5.  Adjust needed properties.

### Creating a curtain wall from a selected object 

1.  Select one or more base geometry objects (Draft object, sketch, etc).
2.  Press the **<img src="images/Arch_CurtainWall.svg" width=16px> [CurtainWall](Arch_CurtainWall.md)** button, or press the **C** then **W** keys.
3.  Adjust needed properties.

## Options

-   Curtain walls share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   Curtain wall mullions can be made from an automatic square profile (set their **Mullion Size** properties) or from a custom profile (set their **Mullion Profile** property). The mullions can be centered over each edge, or placed relatively to the (0,0,0) point by turning off the **Center Profile** property. For example, if you want a profile to be placed slightly behind the panels, you would draw that profile slightly below the (0,0,0) origin point
-   Curtain walls support [Multi-materials](Arch_MultiMaterial.md). Inside the multi-material, the **Frame** layer will be used for the mullions, and the **Glass panel** layer for panels, or **Solid panel** if no Glass panel layer exists in the multi-material.
-   Curtain walls can be based on a linear object such as a line, arc or polyline. In that case, internally, a base surface will be built by extruding the linear object along the direction given by the **Vertical Direction** property, by the length given by the **Height** property.

## Properties

Curtain wall objects inherit the properties of [Arch Components](Arch_Component.md) objects, and also have the following extra properties:

-    **Vertical Mullion Number**:The number of vertical mullions

-    **Vertical Mullion Alignment**: If the profile of the vertical mullions get aligned with the surface or not

-    **Vertical Sections**: The number of vertical sections of this curtain wall

-    **Vertical Mullion Height**: The height of the vertical mullions profile, if no profile is used

-    **Vertical Mullion Width**: The width of the vertical mullions profile, if no profile is used

-    **Vertical Mullion Profile**: A profile for vertical mullions (disables vertical mullion size)

-    **Horizontal Mullion Number**: The number of horizontal mullions

-    **Horizontal Mullion Alignment**: If the profile of the horizontal mullions gets aligned with the surface or not

-    **Horizontal Sections**: The number of horizontal sections of this curtain wall

-    **Horizontal Mullion Height**: The height of the horizontal mullions profile, if no profile is used

-    **Horizontal Mullion Width**: The width of the horizontal mullions profile, if no profile is used

-    **Horizontal Mullion Profile**: A profile for horizontal mullions (disables horizontal mullion size)

-    **Diagonal Mullion Number**: The number of diagonal mullions

-    **Diagonal Mullion Size**: The size of the diagonal mullions, if any, if no profile is used

-    **Diagonal Mullion Profile**: A profile for diagonal mullions, if any (disables horizontal mullion size)

-    **Panel Number**: The number of panels

-    **Panel Thickness**: The thickness of the panels

-    **Swap Horizontal Vertical**: Swaps horizontal and vertical lines

-    **Refine**: Perform subtractions between components so none overlap

-    **Center Profiles**: Centers the profile over the edges or not

-    **Vertical Direction**: The vertical direction reference to be used by this object to deduce vertical/horizontal directions. Keep it close to the actual vertical direction of your curtain wall

-    **Height**: The height of this curtain wall, in case it is based on a linear object

-    **Host**: The host of this curtain wall. The curtain wall will appear embedded in its host object in the tree view (no other action is performed)

## Making frame walls 

Curtain walls are convenient to use in conjunction with [walls](Arch_Wall.md) to create frame walls (walls where an inner, structural layer is made of frames, usually wooden or metal, instead of an homogeneous material such as concrete or brick).

<img alt="" src=images/Frame_wall_example.png  style="width:780px;">

The procedure described below creates a wall and a curtain wall based on a same baseline, then gives the wall a multi-material which leaves an empty space, where the curtain wall is placed:

1.  Create a normal [Arch Wall](Arch_Wall.md), either by clicking two points of from an existing linear object
2.  Select the base object of the newly created arch wall
3.  Press the **<img src="images/Arch_CurtainWall.svg" width=16px> [CurtainWall](Arch_CurtainWall.md)** button, or press the **C** then **W** keys to create a curtain wall from the same baseline as the wall
4.  Make sure both the wall and curtain wall have the same **Height**
5.  Set the number of **horizontal sections** of the curtain wall to zero if you wish only vertical frames
6.  Set the desired **horizontal mullion width** and **horizontal mullion height** (or use a mullion profile)
7.  Prepare two (or more) [materials](Arch_SetMaterial.md), one for the panels, one for the void where the frame will be
8.  Make one [multi-material](Arch_MultiMaterial.md), using one layer of the panel material, one layer of the void material with a negative width value (which will make it not drawn) corresponding to the vertical mullion height of the curtain wall, and another layer of panel material
9.  Attribute the multi-material to the wall
10. Set the **Host** property of the curtain wall to the wall we created in first point

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Curtain wall tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
MyCurtainWall = makeCurtainWall(baseobj)
```

Example:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseface = FreeCAD.ActiveDocument.addObject('Part::Extrusion','Extrusion')
baseface.Base = baseline
baseface.DirMode = "Normal"
baseface.LengthFwd = 2000
curtainwall = Arch.makeCurtainWall(baseface)
curtainWall.VerticalSections = 6
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CurtainWall/en
