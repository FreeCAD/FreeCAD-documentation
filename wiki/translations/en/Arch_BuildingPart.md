---
- GuiCommand   *
   Name   *Arch BuildingPart
   MenuLocation   *Arch → BuildingPart
   Workbenches   *[Arch](Arch_Workbench.md)
   Version   *0.18
   SeeAlso   *[Arch Building](Arch_Building.md), [Arch Site](Arch_Site.md)
---

# Arch BuildingPart/en

## Description

The BuildingPart replaces the old [Arch Floor](Arch_Floor.md) and [Arch Building](Arch_Building.md) with a more capable version that can be used not only to create Floor/Storey/Levels but also all kinds of situations where different Arch/BIM objects need to be grouped and that group might need to be handled as one object or replicated.

## Usage

1.  Optionally, select one or more objects to be included in your new Building Part.
2.  Press the **<img src="images/Arch_BuildingPart.svg" width=16px> [Arch BuildingPart](Arch_BuildingPart.md)** button.

### Notes

BuildingParts have a built-in, implicit [Arch SectionPlane](Arch_SectionPlane.md). <small>(v0.19)</small> 

This plane is always parallel to the BuildingPart\'s base plane, but you can specify the offset between them. So all tools that work with a section plane, such as [Draft Shape2DView](Draft_Shape2DView.md) and [TechDraw ArchView](TechDraw_ArchView.md) also work with BuildingParts.

## Options

-   After creating a BuildingPart, you can add more objects to it by dragging and dropping them in the Tree View or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.
-   You can remove objects from a BuildingPart by dragging and dropping them out of the Tree View or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.
-   By double-clicking the BuildingPart object in the tree view, the [Working Plane](Draft_SelectPlane.md) will be set to its location, and the BuildingPart will become active, which means that new objects will be added automatically to it. Double-clicking the BuildingPart again will deactivate it and set the working plane back to its previous position (in version 0.19, to be available this option needs to be set up as true, in View Property panel - Interaction - Double Click Activates).
-   The BuildingPart can display a mark in the 3D view with a label and level indication.
-   When a BuildingPart is moved/rotated, all its children that either have no **Move With Host** property, or have it turned on, will move/rotate together.
-   Building Parts can be [Draft Cloned](Draft_Clone.md).
-   Building Parts can take any IFC type. Its **IFC Type** property determines its use. If you set it to **Building Storey** it will behave as a level. If you set it to **Building** it behaves as a building, and if you set it to **Element Assembly** it behaves as an assembly. Its icon will change to reflect this setting, but other than that it has no other impact in FreeCAD. However, being exported to IFC as one or another type can have an impact in other BIM applications.
-   Building Parts allow to define an **Auto-group capture box**. Subsequent Draft and Arch objects, or anything else that uses Draft.autogroup(), will be automatically added to that Building Part if they are fully inside the capture box. <small>(v0.20)</small> 

## Properties

See also   * [Property editor](Property_editor.md).

An Arch BuildingPart is derived from an [App GeoFeature](App_GeoFeature.md) object and inherits all its properties. It also has the following additional properties   *

### Data


{{TitleProperty|Base}}

-    **Group|LinkList**   * List of referenced objects.

-    **_ Group Touched|Bool|Hidden**
    


{{TitleProperty|Building Part}}

-    **Area|Area**   * The computed floor area of this floor.

-    **Height|Length**   * The height of this object, and of its children objects. The children objects could be, for example, [Arch Walls](Arch_Wall.md). Each wall\'s height must be set to `0` (zero), so the height property of the BuildingPart propagates to the objects inside of it.

-    **Level Offset|Length**   * The level of the (0,0,0) point of this level. This value is added to the `Placement.Base.z` attribute of the BuildingPart, to indicate a vertical offset without actually moving the object. The resulting offset is displayed if **Show Level** is `True`.

-    **Materials Table|Map|Hidden**   * A MaterialName   *SolidIndexesList map that relates material names with solid indexes to be used when referencing this object from other files.

-    **Only Solids|Bool**   * If true, only solids will be collected by this object when referenced from other files.

-    **Saved Inventor|FileIncluded|Hidden**   * This property stores an inventor representation for this object.

-    **Shape|PartShape|Hidden**   * The shape of this object.


{{TitleProperty|Children}}

-    **Height Propagate|Bool**   * If true, the height value propagates to contained objects.


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**   * IFC data.

-    **Ifc Properties|Map|Hidden**   * IFC properties of this object.

-    **Ifc Type|Enumeration**   * The IFC type of this object.


{{TitleProperty|IFC Attributes}}

-    **Description|String**   * An optional description for this component

-    **Global Id|String**
    

-    **Object Type|String**
    

-    **Overall Height|Length**
    

-    **Overall Width|Length**
    

-    **Partitioning Type|Enumeration**
    

-    **Predefined Type|Enumeration**
    

-    **Tag|String**   * An optional tag for this component.

-    **User Defined Partitioning Type|String**
    

### View


{{TitleProperty|Auto Group}}

-    **Autogroup Autosize|Bool**   * Automatically set the capture box size from the Building Part contents. <small>(v0.20)</small> 

-    **Autogroup Box|Bool**   * Turns auto grouping (and the display of the capture box) on/off. <small>(v0.20)</small> 

-    **Autogroup Margin|Length**   * A margin to use when autosize is turned on. <small>(v0.20)</small> 

-    **Autogroup Size|IntegerList**   * The capture box for newly created objects expressed as \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. <small>(v0.20)</small> 


{{TitleProperty|Building Part}}

-    **Diffuse Color|ColorList|Hidden**   * The individual face colors.

-    **Display Offset|Placement**   * A transformation to apply to the level mark.

-    **Font Name|Font**   * The font to be used for texts.

-    **Font Size|Length**   * The font size of texts.

-    **Line Width|Float**   * The line width of this object.

-    **Origin Offset|Bool**   * If true, when activated, Display offset will affect the origin mark too.

-    **Override Unit|String**   * An optional unit to express levels.

-    **Show Label|Bool**   * If true, when activated, the object\'s label is displayed.

-    **Show Level|Bool**   * If true, show the level.

-    **Show Unit|Bool**   * If true, show the unit on the level tag.


{{TitleProperty|Children}}

-    **Children Line Color|Color**   * The line color to apply to the children of this Building Part.

-    **Children Line Width|Float**   * The line width to apply to the children of this Building Part.

-    **Children Override|Bool**   * If true, the objects contained in this Building Part will adopt these line, color and transparency settings.

-    **Children Shape Color|Color**   * The shape color to apply to the children of this Building Part.

-    **Children Transparency|Percent**   * The transparency to apply to the children of this Building Part.


{{TitleProperty|Clip}}

-    **Auto Cut View|Bool**   * Turn cutting on when activating this level.

-    **Cut Margin|Length**   * The distance between the level plane and the cut line.

-    **Cut View|Bool**   * Cut the view above this level.


{{TitleProperty|Interactions}}

-    **Auto Working Plane|Bool**   * If set to True, the working plane will be kept on Auto mode.

-    **Double Click Activates|Bool**   * If True, double-clicking this object in the tree activates it.

-    **Restore View|Bool**   * If set, the view stored in this object will be restored on double-click.

-    **Save Inventor|Bool**   * If this is enabled, the inventor representation of this object will be saved in the FreeCAD file, allowing to reference it in other files in lightweight mode.

-    **Saved Inventor|FileIncluded|Hidden**   * A slot to save the inventor representation of this object, if enabled.

-    **Set Working Plane|Bool**   * If true, when activated, the working plane will automatically adapt to this Building Part.

-    **View Data|FloatList|Hidden**   * Camera position data associated with this object.

## Scripting


**See also   ***

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The BuildingPart tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function   *


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Creates a `BuildingPart` object from `objectslist`, which is a list of objects.

Example   * 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/en
