---
- GuiCommand:/sv
   Name:Arch Stairs   Name/sv:Arch Stairs
   MenuLocation:Arch → Stairs
   Workbenches:[Arch](Arch_Workbench/sv.md)
   Shortcut:**S** **R**
   SeeAlso:[[Arch Structure/sv]], [[Arch Equipment/sv]]
   Version:0.14
---

# Arch Stairs/sv


</div>

## Description

The [Arch Stairs](Arch_Stairs.md) tool allows you to build automatically several types of stairs. At the moment, only straight stairs (with or without a central landing) are supported. Stairs can be built from scratch, or from a straight [line](Draft_Line.md), in which case the stairs follow the line. If the line is not horizontal but has a vertical inclination, the stairs will also follow its slope.

See the [Stairs entry in wikipedia](http://en.wikipedia.org/wiki/Stairs) for a definition of the different terms used to describe parts of stairs.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;"> 
*Two constructed stairs, one with a massive structure and a landing, and another one with a single stringer.*

## Options

-   Stairs share the common properties and behaviours of all [Arch Components](Arch_Component.md)

## Usage

1.  Press the **<img src="images/Arch_Stairs.svg" width=16px> [[Arch Stairs]]** button, or press **S**, **R** keys.
2.  Adjust the desired properties. Some parts of the stairs, such as the structure, might not appear immediately, if any of the properties makes it impossible, such as a structure thickness of 0.

## Properties

Base

-    **Align**: The alignment of these stairs on their baseline, if applicable.

-    **Base**: The baseline of these stairs, if any.

-    **Height**: The total height of these stairs, if not based on a baseline, or the baseline is horizontal.

-    **Length**: The total length of these stairs if no baseline is defined.

-    **Width**: The width of these stairs.

Steps

-    **Nosing**: The size of the nosing.

-    **Number of Steps**: The numbers of steps (risers) in these stairs.

-    **Riser Height**: The height of the risers.

-    **Tread Depth**: The depth of the treads.

-    **Tread Thickness**: The thickness of the treads.

Structure

-    **Landings**: The type of landings.

-    **Stringer Offset**: The offset between the border of the stairs and the structure.

-    **Stringer Width**: The width of the stringers.

-    **Structure**: The type of structure of these stairs.

-    **Structure Thickness**: The thickness of the structure.

-    **Winders**: The type of winders.

## Limitations

-   Only straight stairs are available at the moment
-   See the [forum entry](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) for circle stairs.
-   See the [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).


<div class="mw-translate-fuzzy">

## Skript


</div>

The Stairs tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
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


{{docnav/sv|[Space/sv](Arch_Space/sv.md)|[Arch CompPanel/sv](Arch_CompPanel/sv.md)|[Arch](Arch_Workbench/sv.md)|IconL=Arch_Space.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompPanel.png}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Stairs/sv
