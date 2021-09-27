---
- GuiCommand:/cs
   Name:Arch_Stairs   Name/cs:Arch Schody
   Workbenches:[Modul architektura](Arch_Workbench/cs.md)
   MenuLocation:Arch → Stairs
   Shortcut:**S** **R**
   SeeAlso:[[Arch Structure/cs]], [[Arch Equipment/cs]]
   Version:0.14
---

# Arch Stairs/cs


</div>


<div class="mw-translate-fuzzy">

## Description

The stairs tool allows you to build automatically several types of stairs. At the moment, only straight stairs (with or without a central landing) are supported. Stairs can be built from scratch, or from a straight [line](Draft_Line.md), in which case the stairs follow the line. If the line is not horizontal but has a vertical inclination, the stairs will also follow its slope.

## Popis

Nástroj Schody pro vytváření a definování schodišť jakéhokoliv typu


</div>

See the [Stairs entry in wikipedia](http://en.wikipedia.org/wiki/Stairs) for a definition of the different terms used to describe parts of stairs.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*Na obrázku nahoře jsou vytvořena dvě schodiště, jedno s plnou strukturou a podestou a druhé s jednotlivými stupni.*


</div>

## Options

-   Stairs share the common properties and behaviours of all [Arch Components](Arch_Component.md)


<div class="mw-translate-fuzzy">

## Použití

Stiskněte tlačítko **<img src="images/Arch_Stairs.png" width=32px> Schody
** nebo klávesy **S**, **R**

1.  Nastavte požadované vlastnosti. Některé z části schodiště, jako je struktura, se nemusí projevit okamžitě, pokud je to u některých vlastností nemožné, jako je třeba tloušťka struktury nastavená na nulu.


</div>

## Vlastnosti

Základ

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


{{docnav/cs|[Space/cs](Arch_Space/cs.md)|[Arch CompPanel/cs](Arch_CompPanel/cs.md)|[Arch](Arch_Workbench/cs.md)|IconL=Arch_Space.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompPanel.png}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Stairs/cs
