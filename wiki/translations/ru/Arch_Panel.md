---
- GuiCommand:/ru
   Name/ru:Паенль
   Name:Arch_Panel
   MenuLocation:Arch → Инструменты панелирования → Панель
   Workbenches:[Arch](Arch_Workbench/ru.md)
   Shortcut:**P** **A**
   Version:0.15
   SeeAlso:[Панельный контур](Arch_Panel_Cut/ru.md), [Панельный лист](Arch_Panel_Sheet/ru.md)
---

# Arch Panel/ru

## Описание

Этот инструмент позволяет создавать все виды панельных элементов, как правило, для панельных конструкций, таких как проект [WikiHouse](http://www.wikihouse.cc/), но также для всех видов объектов, которые основаны на плоском профиле.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*На приведенном выше рисунке показана серия объектов панели, просто сделанных из импортированных 2D-контуров из файла DXF. Затем они могут быть повернуты и собраны для создания структур.*

Данный инструмент может также применятся для создания гофрированных или трапециевидных профилей ({{VersionPlus/ru|0.17}}):

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">

## Применение

1.  Select a 2D shape (Draft object, face or sketch) - optional.
2.  Press the **<img src="images/Arch_Panel.svg" width=16px> [Arch Panel](Arch_Panel.md)** button, or press **P** then **A** keys.
3.  Adjust the desired properties.

### Ограничения

-   В настоящее время нет автоматической системы для создания листов 2D-резки из панельных объектов, но такая функция есть в планах и будет добавлена в будущем.

## Опции

-   Panels share the common properties and behaviours of all [Arch Components](Arch_Component.md).
-   The thickness of a panel can be adjusted after creation.
-   Press **Esc** or the **Cancel** button to abort the current command.
-   Double-clicking on the panel in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions.
-   It is possible to automatically make panels composed of more than one sheet of a material, by raising its Sheets property.
-   Panels can make use of <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the panel will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Panel\'s own Thickness value, after subtracting the other layers.

## Свойства

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

## Scripting


<div class="mw-translate-fuzzy">

## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

The Panel tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Creates a `Panel` object from the given `baseobj`, which is a closed profile, and the given extrusion `thickness`.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width`, and `thickness` to create a block panel.
-   If a `placement` is given, it is used.

Пример: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```

## Материалы для самостоятельного изучения 


<div class="mw-translate-fuzzy">

-   [Руководство по портированию файлов проекта Wikihouse в FreeCAD](Wikihouse_porting_tutorial/ru.md)


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel/ru
