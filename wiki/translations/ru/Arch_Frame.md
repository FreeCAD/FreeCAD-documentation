---
- GuiCommand:/ru
   Name:Arch Frame
   Name/ru:Arch Frame
   MenuLocation:Архитектура -> Каркас
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:**F** **R**
   SeeAlso:[[Arch Wall/ru]], [[Arch Structure/ru]]
---


</div>

## Описание


<div class="mw-translate-fuzzy">

Инструмент «Рамка» используется для создания всех видов объектов фрейма на основе профиля и макета. Профиль экструдируется по краям макета, который может быть любым 2D-объектом, таким как [sketch](Sketcher_Workbench.md) или [draft object](Draft_Workbench.md). Особенно полезно создавать перила или стены рамы. Объекты кадра затем могут быть легко превращены в объекты [wall](Arch_Wall.md) или [structure](Arch_Structure.md) .


</div>

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*На приведенном выше рисунке [line](Draft_Line.md) была преобразована в [Массив массива](Массив_массива.md), а объект фрейма был создан с использованием массива как макета, а [circle](Draft_Circle.md) как профиль.*


</div>

## Usage

1.  Create a layout object and a profile object, for example with the [Draft Workbench](Draft_Workbench.md) or the [Sketcher Workbench](Sketcher_Workbench.md).
2.  Select the layout object first, then, with **Ctrl** pressed, select the profile object.
3.  Press the **<img src="images/Arch_Frame.svg" width=16px> [Arch Frame](Arch_Frame.md)** button, or press **F** then **R** keys.

## Options

-   Frames share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The frame object can be placed at a certain distance from the layout object, by setting its Offset property
-   The profile will be copied at the base of each edge of the layout object, then extruded along it. You can control how the profile is placed at the base of each edge with the Align and Rotation properties.

## Properties

-    **Base**: The layout this frame is based on.

-    **Profile**: The profile this frame is based on.

-    **Align**: Specifies if the profile must be rotated to have its normal axis aligned with each edge.

-    **Offset**: An optional distance between the layout object and the frame object.

-    **Rotation**: The rotation of the profile around its extrusion axis.

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

Пример: 
```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/ru|[Nest](Arch_Nest.md)|[Fence](Arch_Fence.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Nest.svg |IconC=Workbench_Arch.svg |IconR=Arch_Fence.svg}}


</div>






