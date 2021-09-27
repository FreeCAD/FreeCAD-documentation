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


<div class="mw-translate-fuzzy">

## Описание

Инструмент лестницы позволяет автоматически создавать несколько типов лестниц. В настоящий момент поддерживаются только прямые лестницы (с или без центральной посадки). Лестница может быть построена с нуля или с прямой [ line](Draft_Line.md), и в этом случае лестница следует за строкой. Если линия не горизонтальна, а имеет вертикальный наклон, лестница также будет следовать ее наклону.


</div>

См. [Stairs entry in wikipedia](Http://en.wikipedia.org/wiki/Stairs) для определения различных терминов, используемых для описания частей лестницы.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

«На вышеупомянутом изображении были созданы две лестницы, одна с массивной структурой и посадкой, а другая с одним стрингером».


</div>

## Опции

-   Лестницы разделяют общие свойства и поведение всех [ Arch Components](Arch_Component.md)


<div class="mw-translate-fuzzy">

## Использование

1.  Нажмите кнопку {{KEY | <img src="images/_Arch_Stairs.png_" width= 16px> [[Arch Stairs]]}} или нажмите клавиши {{KEY | S}}, {{KEY | R}}
2.  Adjust the desired properties. Some parts of the stairs, such as the structure, might not appear immediately, if any of the properties makes it impossible, such as a structure thickness of 0.


</div>

## Свойства

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

The Stairs tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
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
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Stairs/ru
