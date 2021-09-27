---
- GuiCommand:/ru
   Name:Arch Panel   Name/ru:Arch Panel
   MenuLocation:Архитектура → Панель
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:**P** **A**
   Version:0.15
   SeeAlso:[Структура](Arch_Structure/ru.md), [Arch Panel Cut](Arch_Panel_Cut/ru.md), [Arch Panel Sheet](Arch_Panel_Sheet/ru.md)
---

# Arch Panel/ru


</div>

## Описание

Этот инструмент позволяет создавать все виды панельных элементов, как правило, для панельных конструкций, таких как проект [WikiHouse](http://www.wikihouse.cc/), но также для всех видов объектов, которые основаны на плоском профиле.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*На приведенном выше рисунке показана серия объектов панели, просто сделанных из импортированных 2D-контуров из файла DXF. Затем они могут быть повернуты и собраны для создания структур.*


<div class="mw-translate-fuzzy">

Начиная с версии 0.17, панель Arch также может использоваться для создания гофрированных или трапециевидных профилей:


</div>

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">

## Использование

1.  Select a 2D shape (draft object, face or sketch) - optional.
2.  Press the **<img src="images/Arch_Panel.svg" width=16px> [Arch Panel](Arch_Panel.md)** button, or press **P** then **A** keys.
3.  Adjust the desired properties.


<div class="mw-translate-fuzzy">

## Ограничения


</div>


<div class="mw-translate-fuzzy">

-   В настоящее время нет автоматической системы для производства двумерных разрезанных листов из панельных объектов, но такая функция находится в планах и будет добавлена в будущем.
-   Этот инструмент недоступен в версиях FreeCAD до 0,15


</div>

## Options

-   Panels share the common properties and behaviours of all [Arch Components](Arch_Component.md).
-   The thickness of a panel can be adjusted after creation.
-   Press **Esc** or the **Cancel** button to abort the current command.
-   Double-clicking on the panel in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions.
-   It is possible to automatically make panels composed of more than one sheet of a material, by raising its Sheets property.
-   Panels can make use of <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the panel will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Panel\'s own Thickness value, after subtracting the other layers.

## Properties

-    **Length**: The length of the panel

-    **Width**: The width of the panel

-    **Thickness**: The thickness of the panel

-    **Area**: The area of the panel (automatic)

-    **Sheets**: The number of sheets of material the panel is made of

-    **Wave Length**: The length of the wave for corrugated panels

-    **Wave Height**: The height of the wave for corrugated panels

-    **Wave Type**: The type of the wave for corrugated panels, curved, trapezoidal or spiked

-    **Wave Direction**: The orientation of the waves for corrugated panels

-    **Bottom Wave**: If the bottom wave of the panel is flat or not


<div class="mw-translate-fuzzy">

## Написание скриптов 


</div>

The Panel tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Creates a `Panel` object from the given `baseobj`, which is a closed profile, and the given extrusion `thickness`.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width`, and `thickness` to create a block panel.
-   If a `placement` is given, it is used.

Example: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```

## Учебники

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)


<div class="mw-translate-fuzzy">


{{docnav/ru|[Arch CompPanel](Arch_CompPanel.md)|[Panel Cut](Arch_Panel_Cut.md)|[Arch](Arch_Workbench.md)|IconL=Arch_CompPanel.png |IconC=Workbench_Arch.svg |IconR=Arch_Panel_Cut.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Panel/ru
