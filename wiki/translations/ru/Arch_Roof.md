---
 GuiCommand:
   Name: Arch_Roof
   Name/ru: Крыша
   MenuLocation: Архитектура , Крыша
   Workbenches: Arch_Workbench/ru
   Shortcut: **R** **F**
   SeeAlso: Arch_Structure/ru, Arch_Wall/ru
---

# Arch Roof/ru


</div>



## Описание

The **Arch Roof** tool allows for the creation of a sloped roof from a selected wire. The created roof object is parametric, keeping its relationship with the base object. The principle is that each edge is seen allotting a profile of roof (slope, width, overhang, thickness).

**Note:** This tool is still in development, and might fail with very complex shapes.

<img alt="" src=images/RoofExample.png  style="width:600px;"> 
*View from above a building model showing the roof with certain transparency*




<div class="mw-translate-fuzzy">

## Применение


</div>


<div class="mw-translate-fuzzy">

1.  Создайте замкнутый контур с помощью инструмента **Wire** с направлением построения против часовой стрелки и выберите его.

    :   <img alt="" src=images/CounterclockwiseWire.png  style="width:600px;">

2.  Нажмите кнопку **<img src="images/Arch_Roof.svg" width=16px> [Крыша](Arch_Roof/ru.md)
**, или клавишу клавиатуры **R** затем **F**

3.  Крыша созданная изначально может иметь странную форму, это связанно с тем, что параметры граней созданной крыши, пока что ещё не настроены.

4.  После создания крыши по умолчанию дважды щелкните по объекту в [древе проекта](tree_view/ru.md) для доступа к редактированию свойств. Угол крыши должен быть между 0 и 90.

    :   ![](images/RoofTable.png )

5.  Каждая строка соответствует одной из панелей крыши. Таким образом, вы можете установить нужные свойства для каждой панели крыши.

6.  Чтобы помочь себе, вы можете установить `Angle (Угол)` или `Run` в `0` и определить `Relative Id`, что приведет к автоматическому расчету, чтобы найти данные относительно `Relative Id`.

7.  Это работает следующим образом:
    1.  Если `Angle (Угол) &#61; 0` и `Run &#61; 0` тогда профиль идентичен относительному профилю.
    2.  Если `Angle (Угол) &#61; 0` тогда `Angle (Угол)` рассчитывается таким образом, чтобы высота была такой же, как и относительный профиль.
    3.  Если `Run &#61; 0` тогда `Run` рассчитывается таким образом, чтобы высота была такой же, как и относительный профиль.

8.  Наконец, установите Angle (Угол) на 90°, чтобы сделать фронтон.

    :   <img alt="" src=images/RoofProfil.png  style="width:600px;">

9.  
    **Примечание**: для лучшего понимания, пожалуйста, посмотрите это [youtube видеоролик](https://www.youtube.com/watch?v=4Urwru71dVk).


</div>

## Usage (solid base) 

If your roof has a complex shape (e.g. contains pitched windows or other non-standard features) you can create a custom solid object using various other FreeCAD workbenches ([Part](Part_Workbench.md), [Sketcher](Sketcher_Workbench.md) etc.). And then use this solid as the **Base** object of your roof:

1.  Select the solid base object.
2.  Press the **<img src="images/Arch_Roof.svg" width=16px> [Arch Roof](Arch_Roof.md)** button, or press **R** then **F** keys.

## Subtracting a roof 

Roofs have an automatically generated subtraction volume (<small>(v1.0)</small>  for roofs with a solid base). When a roof is [removed](Arch_Remove.md) from the walls of a building, both the roof itself as well as everything above it is subtracted from the walls.


<small>(v1.0)</small> 

: It is possible to override the automatic subtraction volume by setting the **Subvolume** property of the roof to a custom solid object.

<img alt="" src=images/Arch_Roof_Subtract_Default.png  style="width:" height="150px;"> <img alt="" src=images/Arch_Roof_Subtract_Subvolume.png  style="width:" height="150px;"> <img alt="" src=images/Arch_Roof_Subvolume_Example.png  style="width:" height="150px;"> 
*Solid-based roof before (1st image) and after (2nd image) [removing](Arch_Remove.md) it from walls.<br>
The 3rd image shows the generated subtraction volume.*



## Опции


<div class="mw-translate-fuzzy">

-   Крыши обладают таким же свойствами и моделью поведения, как и все остальные [компоненты верстака Arch](Arch_Component/ru.md)


</div>



## Свойства

### Data


{{TitleProperty|Roof}}


<div class="mw-translate-fuzzy">

-    **Angles (Углы)**: Список содержащий углы наклона крыши, для каждой её грани.

-    **Runs ()**: Список содержащий расстояние от центра крыши до свеса, для каждой грани крыши.

-    **IdRel**: Список содержащий идентификаторы, для каждой грани крыши.

-    **Thickness (Толщины)**: Список содержащий толщины крыши, для каждой её грани.

-    **Overhang (Свесы)**: Список содержащий длины свесов крыши, для каждой её грани.

-    **Face (Грань)**: Индекс грани базового объекта (не используется).


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

The Roof tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```

-   Creates a `Roof` object from the given `baseobj`, which can be a closed wire or a solid object.
    -   If `baseobj` is a wire, you can provide lists for `angles`, `run`, `idrel`, `thickness`, and `overhang`, for each edge in the wire to define the shape of the roof.
    -   The lists are automatically completed to match the number of edges in the wire.

Пример:


```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Roof/ru
