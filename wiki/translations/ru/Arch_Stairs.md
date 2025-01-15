---
 GuiCommand:
   Name/ru: Лестница
   Name: Arch_Stairs
   MenuLocation: Arch , Лестница
   Workbenches: Arch_Workbench/ru
   Shortcut: **S** **R**
   Version: 0.14
   SeeAlso: Arch_Structure/ru, Arch_Equipment/ru
---

# Arch Stairs/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Инструмент [Лестница](Arch_Stairs/ru.md) позволяет автоматически создавать несколько типов лестниц. инструмент позволяет автоматически создавать несколько типов лестниц. На данный момент поддерживаются только прямые лестницы (лестничной площадкой или без нее). Лестница может быть построена с нуля или вдоль [Линии (верстак Draft)](Draft_Line/ru.md). Если линия не горизонтальна, а имеет наклон по вертикали, лестница также будет иметь наклон.


</div>

Смотрите [статью о лестницах на википедии](https://en.wikipedia.org/wiki/Stairs) для определения значения различных терминов, используемых при описании частей лестницы.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">



*Изображение двух сконструированных лестниц, одна с массивной конструкцией и лестничной площадкой, а другая с одним косоуром.*


</div>



## Опции

-   Лестницы обладают таким же свойствами и моделью поведения, как и все остальные [компоненты верстака Arch](Arch_Component/ru.md)



## Применение


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку **<img src="images/Arch_Stairs.svg" width=16px> [Лестница](Arch_Stairs.md)** или нажмите клавиши **S**, **R**.
2.  Настройте нужные свойства. Некоторые части лестницы, такие как конструкция, могут изначально отсутствовать, если какое-либо из свойств делает это невозможным, например, толщина конструкции равна 0.


</div>

<img alt="" src=images/Stairs_and_Landing_02.png  style="width:600px;">

<img alt="" src=images/Stairs_and_Landing_01.png  style="width:600px;">

<img alt="" src=images/Arch_Stairs_Complex_Example.png  style="width:600px;">



*Complex stairs based on a selection of lines and wired as shown on the left.<br>
In red the wires used for the landings at Z&equals;1500mm, Z&equals;3000mm and Z&equals;4500mm.<br>
In black the lines connecting them used for the flights.
*



## Свойства



### Данные


{{TitleProperty|Segment and Parts}}

-    **Abs Top|Vector**: (read-only) The absolute top level the stairs lead to.

-    **Last Segment|Link**: Last segment (flight or landing) of an Arch Stairs connecting to this segment. The start level of the stairs will be the end level of this last segment.

-    **Outline Left|VectorList**: The left outline of the stairs (read-only).

-    **Outline Left All|VectorList**: The left outline of all segments of the stairs (read-only).

-    **Outline Right|VectorList**: The right outline of the stairs (read-only).

-    **Outline Right All|VectorList**: The right outline of all segments of the stairs (read-only).

-    **Railing Height Left|Length**: Height of the left railing of the stairs or landing.

-    **Railing Height Right|Length**: Height of the right railing of the stairs or landing.

-    **Railing Left|LinkHidden**: The left railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.

-    **Railing Offset Left|Length**: Offset of the left railing from the edge of the stairs or landing.

-    **Railing Offset Right|Length**: Offset of the right railing from the edge of the stairs or landing.

-    **Railing Right|LinkHidden**: The right railing object. <small>(v0.20)</small> : Property type updated from {{Incode|String}} to {{Incode|LinkHidden}}.


{{TitleProperty|Stairs}}

(Лестница)

-    **Align|Enumeration**: The alignment of the stairs on the baseline. Only used if a baseline is defined. Can be {{value|Left}}, {{value|Right}} or {{value|Center}}.

-    **Height|Length**: The total height of the stairs. Only used if no baseline is defined, or if the baseline is horizontal. Ignored if **Riser Height Enforce** is non-zero.

-    **Length|Length**: The total length of the stairs if no baseline is defined. Ignored if **Tread Depth Enforce** is non-zero.

-    **Width|Length**: The width of the stairs.

-    **Width of Landing|FloatList**: If the **Number Of Steps** is 1, the stairs object acts as a landing. When this is the case and the baseline is multi-segment, the width of first segment of the landing follows the **Width**, the widths of subsequent segments follow the list set here.


{{TitleProperty|Steps}}

(Ступени)


<div class="mw-translate-fuzzy">

-    **Blondel Ratio|Float**: (только для чтения) Рассчитанный коэффициент Блонделя. Это соотношение позволяет определить наиболее удобную для человека лестницу и должно составлять от 62 до 64 см или от 24,5 до 25,5 дюйма.

-    **Landing Depth|Length**: Длина лестничной площадки находящейся по ходу лестницы, указывается только если площадка **Landings** добавлена. По умолчанию значение **Width** равно 0.

-    **Nosing|Length**: Размер выступа ступени.

-    **Number Of Steps|Integer**: Количество ступеней (подступенников).

-    **Riser Height|Length**: (только для чтения) Высота подступенников лестницы. Если высота ступеней **Riser Height Enforce** равна нулю, тогда она вычисляется как (**Height** / **Number of Steps**). В других случаях это значение эквивалентно **Riser Height Enforce**.

-    **Riser Height Enforce|Length**: Принудительная высота подступенников лестницы.

-    **Riser Thickness|Length**: Толщина подступенников лестницы.

-    **Tread Depth|Length**: (только для чтения) Длина ступеней. Если **Tread Depth Enforce** равно 0, то вычисляется как (**Length** / **Number of Steps**). В других случаях это значение эквивалентно **Tread Depth Enforce**.

-    **Tread Depth Enforce|Length**: Принудительная длина ступеней

-    **Tread Thickness|Length**: Толщина ступеней.


</div>


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



## Ограничения


<div class="mw-translate-fuzzy">

-   На данный момент доступны только прямые лестницы
-   См. [тему на форуме](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) про круговые лестницы.
-   См. [уведомления](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564) о данном инструменте на форуме.


</div>



## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

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
⏵ [documentation index](../README.md) > Arch Stairs/ru
