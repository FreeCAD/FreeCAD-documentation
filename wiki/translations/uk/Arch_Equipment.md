---
 GuiCommand:
   Name: Arch Equipment
   Name/uk: Arch Equipment
   MenuLocation: Arch , Equipment
   Workbenches: Arch_Workbench/uk
   Shortcut: E Q
   SeeAlso: Arch_3Views
---

# Arch Equipment/uk


</div>

## Description

The **Arch Equipment** tool offers you a simple and convenient way to insert non-structural, standalone elements such as pieces of furniture, hydro-sanitary equipments or electrical appliances to your projects. Equipments are based on [Part shapes](Part_Workbench.md), which allow them to benefit from the solidity and possibilities of BRep geometry, and generate nice views when rendered to plan and section views.

<img alt="" src=images/Arch_equipment_example.jpg  style="width:600px;"> 
*Furniture objects enclosed in an [Arch Equipment](Arch_Equipment.md) object. The flat projections can be obtained by the [Draft Shape2DView](Draft_Shape2DView.md) tool*

As of version 0.17, equipment objects also have a **HiRes** property where a [Mesh](Mesh_Workbench.md) object can be attached. Equipment objects can then be made to display that mesh in the 3D view instead of their shape, which allows to use any high-resolution mesh objects such as detailed pieces of furniture commonly found on websites.

<img alt="" src=images/Arch_equipment_mesh.jpg  style="width:600px;"> 
*Furniture objects enclosed in an [Arch Equipment](Arch_Equipment.md) object, with a high resolution mesh attached*

When using the Arch OBJ exporter, all equipment objects that are in mesh display mode will be exported as their mesh instead of their shape.

## Usage

1.  Select a [Part](Part_Workbench.md) shape, and optionally a [Mesh](Mesh_Workbench.md) object.
2.  Press the **<img src="images/Arch_Equipment.svg" width=16px> [Equipment](Arch_Equipment.md)** button, or press **E** then **Q** keys.

## Options

-   Equipments share the common properties and behaviours of all [Arch Components](Arch_Component.md)

## Properties

-    **Model**: A description of the model of this equipment.

-    **Url**: An URL of the product page where more information about this equipment can be found.

-    **Mesh**: A [Mesh](Mesh_Workbench.md) representation to use for this equipment. When set, the **Mesh** display mode becomes available.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Equipment tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Equipment = makeEquipment(baseobj=None, placement=None, name="Equipment")
```

-   Creates an `Equipment` object from the given `baseobj`, which can be a `Part` or a `Mesh`.
-   If a `placement` is given, it is used.
-   It returns `None` if the operation fails.

Example: 
```python
import FreeCAD, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 500
Box.Width = 2000
Box.Height = 600

Equip = Arch.makeEquipment(Box)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/uk|[Fence](Arch_Fence/uk.md)|[Arch CompPipe](Arch_CompPipe/uk.md)|[Arch](Arch_Workbench/uk.md)|IconL=Arch_Fence.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompPipe.png}}


</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Equipment/uk
