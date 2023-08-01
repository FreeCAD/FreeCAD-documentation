---
- GuiCommand:
   Name:Arch_Stairs   Name/cs:Arch Schody
   Workbenches:[Modul architektura](Arch_Workbench/cs.md)
   MenuLocation:Arch → Stairs
   Shortcut:**S** **R**
   SeeAlso:[[Arch Structure/cs]], [[Arch Equipment/cs]]
   Version:0.14
---

# Arch Stairs/cs


</div>

## Description


<div class="mw-translate-fuzzy">

## Description 

The stairs tool allows you to build automatically several types of stairs. At the moment, only straight stairs (with or without a central landing) are supported. Stairs can be built from scratch, or from a straight [line](Draft_Line.md), in which case the stairs follow the line. If the line is not horizontal but has a vertical inclination, the stairs will also follow its slope.

## Popis

Nástroj Schody pro vytváření a definování schodišť jakéhokoliv typu


</div>

See the [Stairs entry in wikipedia](https://en.wikipedia.org/wiki/Stairs) for a definition of the different terms used to describe parts of stairs.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*Na obrázku nahoře jsou vytvořena dvě schodiště, jedno s plnou strukturou a podestou a druhé s jednotlivými stupni.*


</div>

## Options

-   Stairs share the common properties and behaviors of all [Arch Components](Arch_Component.md)

## Usage


<div class="mw-translate-fuzzy">

## Použití

Stiskněte tlačítko **<img src="images/Arch_Stairs.png" width=32px> Schody
** nebo klávesy **S**, **R**

1.  Nastavte požadované vlastnosti. Některé z části schodiště, jako je struktura, se nemusí projevit okamžitě, pokud je to u některých vlastností nemožné, jako je třeba tloušťka struktury nastavená na nulu.


</div>

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;"> 
*Complex stairs based on a selection of lines and wired as shown on the left.<br>
In red the wires used for the landings at Z&equals;1500mm, Z&equals;3000mm and Z&equals;4500mm.<br>
In black the lines connecting them used for the flights.
*



## Vlastnosti

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

-    **Railing Left|LinkHidden**: The left railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: Offset of the left railing from the edge of the stairs or landing.

-    **Railing Offset Right|Length**: Offset of the right railing from the edge of the stairs or landing.

-    **Railing Right|LinkHidden**: The right railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.


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

-    **Number Of Steps|Integer**: The numbers of steps (risers). Must be at least 2 for a single flight, and at least 4 for a stairs with a central landing.

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

## Omezení

-   Nejsou dostupné před verzí FreeCAD 0.14
-   V současnosti jsou dostupné pouze přímé schody
-   Podívejte se na [forum zdroj](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) na kruhové schody.
-   Podívejte se na následující [forum oznámení](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).


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

Example: 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```


<div class="mw-translate-fuzzy">


{{docnav/cs|[Space/cs](Arch_Space/cs.md)|[Arch CompPanel/cs](Arch_CompPanel/cs.md)|[Arch](Arch_Workbench/cs.md)|IconL=Arch_Space.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompPanel.png}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Stairs/cs
