---
- GuiCommand:/ru
   Name:Arch Stairs
   Name/ru:Arch Stairs
   MenuLocation:Архитектура → Лестницы
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:**S** **R**
   Version:0.14
   SeeAlso:[[Arch Structure/ru]], [[Arch Equipment/ru]]
---

# Arch Stairs/ru


</div>

## Description


<div class="mw-translate-fuzzy">

## Описание

Инструмент лестницы позволяет автоматически создавать несколько типов лестниц. В настоящий момент поддерживаются только прямые лестницы (с или без центральной посадки). Лестница может быть построена с нуля или с прямой [ line](Draft_Line.md), и в этом случае лестница следует за строкой. Если линия не горизонтальна, а имеет вертикальный наклон, лестница также будет следовать ее наклону.


</div>


<div class="mw-translate-fuzzy">

См. [Stairs entry in wikipedia](Http://en.wikipedia.org/wiki/Stairs) для определения различных терминов, используемых для описания частей лестницы.


</div>

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

«На вышеупомянутом изображении были созданы две лестницы, одна с массивной структурой и посадкой, а другая с одним стрингером».


</div>

## Опции


<div class="mw-translate-fuzzy">

-   Лестницы разделяют общие свойства и поведение всех [ Arch Components](Arch_Component.md)


</div>

## Usage


<div class="mw-translate-fuzzy">

## Использование

1.  Нажмите кнопку {{KEY | <img src="images/_Arch_Stairs.png_" width= 16px> [[Arch Stairs]]}} или нажмите клавиши {{KEY | S}}, {{KEY | R}}
2.  Adjust the desired properties. Some parts of the stairs, such as the structure, might not appear immediately, if any of the properties makes it impossible, such as a structure thickness of 0.


</div>

## Свойства

### Data


{{TitleProperty|Segment and Parts}}

-    **Abs Top|Vector**: (read-only) The absolute top level the stairs lead to.

-    **Last Segment|Link**: Last segment (flight or landing) of an Arch Stairs connecting to this segment. The start level of the stairs will be the end level of this last segment.

-    **Outline Left|VectorList**: The left outline of the stairs.

-    **Outline Left All|VectorList**: The left outline of all segments of the stairs.

-    **Outline Right|VectorList**: The right outline of the stairs.

-    **Outline Right All|VectorList**: The right outline of all segments of the stairs.

-    **Railing Height Left|Length**: Height of the left railing of the stairs or landing.

-    **Railing Height Right|Length**: Height of the right railing of the stairs or landing.

-    **Railing Left|String**: Name of the left railing object.

-    **Railing Offset Left|Length**: Offset of the left railing from the edge of the stairs or landing.

-    **Railing Offset Right|Length**: Offset of the right railing from the edge of the stairs or landing.

-    **Railing Right|String**: Name of the right railing object.


{{TitleProperty|Stairs}}

-    **Align|Enumeration**: The alignment of the stairs on the baseline. Only used if a baseline is defined. Can be {{value|Left}}, {{value|Right}} or {{value|Center}}.

-    **Height|Length**: The total height of the stairs. Only used if no baseline is defined, or if the baseline is horizontal. Ignored if **Riser Height Enforce** is non-zero.

-    **Length|Length**: The total length of the stairs if no baseline is defined. Ignored if **Tread Depth Enforce** is non-zero.

-    **Width|Length**: The width of the stairs.

-    **Width of Landing|FloatList**: If the **Number Of Steps** is 1, the stairs object acts as a landing. When this is the case and the baseline is multi-segment, the width of first segment of the landing follows the **Width**, the widths of subsequent segments follow the list set here.


{{TitleProperty|Steps}}

-    **Blondel Ratio|Float**: (read-only) The calculated Blondel ratio. This ratio indicates comfortable stairs and should be between 62 and 64cm or 24.5 and 25.5in.

-    **Landing Depth|Length**: The depth of the landing of the flight, if enabled in **Landings**. Defaults to the **Width** if 0.

-    **Nosing|Length**: The size of the nosing.

-    **Number Of Steps|Integer**: The numbers of steps (risers).

-    **Riser Height|Length**: (read-only) The height of the risers. If **Riser Height Enforce** is 0 it is calculated (**Height** / **Number of Steps**). Else it is the same as **Riser Height Enforce**.

-    **Riser Height Enforce|Length**: The enforced height of the risers.

-    **Riser Thickness|Length**: The thickness of the risers.

-    **Tread Depth|Length**: (read-only) The depth of the treads. If **Tread Depth Enforce** is 0 it is calculated (**Length** / **Number of Steps**). Else it is the same as **Tread Depth Enforce**.

-    **Tread Depth Enforce|Length**: The enforced depth of the treads.

-    **Tread Thickness|Length**: The thickness of the treads.


{{TitleProperty|Structure}}

-    **Connection Down Start Stairs|Enumeration**: The type of connection between the lower floor slab and the start of the stairs. Can be {{value|HorizontalCut}}, {{value|VerticalCut}} or {{value|HorizontalVerticalCut}}.

-    **Connection End Stairs Up|Enumeration**: The type of connection between the end of the stairs and the upper floor slab. Can be {{value|toFlightThickness}} or {{value|toSlabThickness}}.

-    **Down Slab Thickness|Length**: The thickness of the lower floor slab.

-    **Flight|Enumeration**: The direction of the flight after the landing. Can be {{value|Straight}}, {{value|HalfTurnLeft}} or {{value|HalfTurnRight}}.

-    **Landings|Enumeration**: The type of landings. Can be {{value|None}} or {{value|At center}} ({{value|At each corner}} not implemented yet).

-    **Stringer Overlap|Length**: The overlap of the stringers above the bottom of the treads.

-    **Stringer Width|Length**: The width of the stringers.

-    **Structure|Enumeration**: The structure type of the stairs. Can be {{value|None}}, {{value|Massive}}, {{value|One stringer}} or {{value|Two stringers}}.

-    **Structure Offset|Length**: The offset between the border of the stairs and the structure.

-    **Structure Thickness|Length**: The thickness of the structure.

-    **Up Slab Thickness|Length**: The thickness of the upper floor slab.

-    **Winders|Enumeration**: The type of winders. Not implemented.

## Limitations


<div class="mw-translate-fuzzy">

## Ограничения

-   Недоступно до версии 0.14 FreeCAD
-   Only straight stairs are available at the moment
-   See the [forum entry](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) for circle stairs.
-   See the [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).


</div>

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Stairs tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```

-   Creates a `Stairs` object from the given `baseobj`.
-   If `baseobj` is not given, it will use `length`, `width`, `height`, and `steps`, to build a solid object.

Пример: 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Stairs/ru
