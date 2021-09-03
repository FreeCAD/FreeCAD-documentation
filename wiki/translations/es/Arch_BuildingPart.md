---
- GuiCommand:/es
   Name:Arch BuildingPart
   Name/es:Arquitectura EdificioPieza
   MenuLocation:Arquitectura → EdificioPieza
   Workbenches:[Arquitectura](Arch_Module/es.md)
   Version:0.18
   SeeAlso:[Arquitectura Edificio](Arch_Building/es.md), [Arquitectura Sitio](Arch_Site/es.md)
---


</div>

## Descripción

La EdificioPieza reemplaza a las antiguas [Arquitectura Planta](Arch_Floor/es.md) y [Arquitectura Edificio](Arch_Building/es.md) con una versión más capaz que puede ser usada no sólo para crear Suelo/Piso/Niveles sino también todo tipo de situaciones donde diferentes objetos de Arquitectura/BIM necesitan ser agrupados y ese grupo puede necesitar ser manejado como un solo objeto o replicado.

## Utilización

1.  Optionally, select one or more objects to be included in your new Building Part.
2.  Press the **<img src="images/Arch_BuildingPart.svg" width=16px> [Arch BuildingPart](Arch_BuildingPart.md)** button.

### Notas

BuildingParts have a built-in, implicit [Arch SectionPlane](Arch_SectionPlane.md). <small>(v0.19)</small> 

This plane is always parallel to the BuildingPart\'s base plane, but you can specify the offset between them. So all tools that work with a section plane, such as [Draft Shape2DView](Draft_Shape2DView.md) and [TechDraw ArchView](TechDraw_ArchView.md) also work with BuildingParts.

## Opciones

-   After creating a BuildingPart, you can add more objects to it by dragging and dropping them in the Tree View or by using the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.
-   You can remove objects from a BuildingPart by dragging and dropping them out of the Tree View or by using the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.
-   By double-clicking the BuildingPart object in the tree view, the [Working Plane](Draft_SelectPlane.md) will be set to its location, and the BuildingPart will become active, which means that new objects will be added automatically to it. Double-clicking the BuildingPart again will deactivate it and set the working plane back to its previous position (in version 0.19, to be available this option needs to be set up as true, in View Property panel - Interaction - Double Click Activates).
-   The BuildingPart can display a mark in the 3D view with a label and level indication.
-   When a BuildingPart is moved/rotated, all its children that either have no **Move With Host** property, or have it turned on, will move/rotate together.
-   Building Parts can be [Draft Cloned](Draft_Clone.md).
-   Building Parts can take any IFC type. Its **IFC Type** property determines its use. If you set it to **Building Storey** it will behave as a level. If you set it to **Building** it behaves as a building, and if you set it to **Element Assembly** it behaves as an assembly. Its icon will change to reflect this setting, but other than that it has no other impact in FreeCAD. However, being exported to IFC as one or another type can have an impact in other BIM applications.

## Propiedades

### Data

-    **Height**: The height of this object, and of its children objects. The children objects could be, for example, [Arch Walls](Arch_Wall.md). Each wall\'s height must be set to `0` (zero), so the height property of the BuildingPart propagates to the objects inside of it.

-    **LevelOffset**: The level of the (0,0,0) point of this level. This value is added to the `Placement.Base.z` attribute of the BuildingPart, to indicate a vertical offset without actually moving the object. The resulting offset is displayed if **Show Level** is `True`.

-    **Area**: The computed floor area of this floor

-    **IfcType**: The IFC type of this object

-    **Description**: An optional description for this component

-    **Tag**: An optional tag for this component

-    **IfcAttributes**: Custom IFC properties and attributes

### View

-    **LineWidth**: The line width of this object

-    **OverrideUnit**: An optional unit to express levels

-    **DisplayOffset**: A transformation to apply to the level mark

-    **ShowLevel**: If true, show the level

-    **ShowUnit**: If true, show the unit on the level tag

-    **SetWorkingPlane**: If true, when activated, the working plane will automatically adapt to this Building Part

-    **OriginOffset**: If true, when activated, Display offset will affect the origin mark too

-    **ShowLabel**: If true, when activated, the object\'s label is displayed

-    **FontName**: The font to be used for texts

-    **FontSize**: The font size of texts

-    **RestoreView**: If set, the view stored in this object will be restored on double-click

-    **DiffuseColor**: The individual face colors


<small>(v0.19)</small> 

-    **ChildrenOverride**: If set, the settings below will affect the children of this Building Part

-    **ChildrenLineWidth**: The line width to apply to the children of this Building Part

-    **ChildrenLineColor**: The line color to apply to the children of this Building Part

-    **ChildrenShapeColor**: The shape color to apply to the children of this Building Part

-    **ChildrenTransparency**: The transparency to apply to the children of this Building Part

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The BuildingPart tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Creates a `BuildingPart` object from `objectslist`, which is a list of objects.

Ejemplo: 
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


<div class="mw-translate-fuzzy">





</div>


 
