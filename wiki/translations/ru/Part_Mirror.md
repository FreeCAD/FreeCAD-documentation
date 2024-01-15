---
 GuiCommand:
   Name: Part_Mirror
   Name/ru: Зеркальное отражение
   MenuLocation: Деталь -> Зеркальное отражение...
   Workbenches: Part_Workbench/ru
   SeeAlso: 
---

# Part Mirror/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

\'Зеркальное отражение\' - этот инструмент создаёт новый объект (изображение), которое является отражением исходного объекта (источника). Объект отражения создаётся за зеркальной плоскостью. Плоскостью зеркального отражения может быть стандартная (**XY**, **YZ** или **XZ**) или любая другая плоскостью, параллельная стандартной плоскости.


</div>

Пример:

![](images/PARTMirrorBeforev11.png )



*Before*

![](images/PARTMirrorAfterv11.png )



*After mirrored through YZ plane*



## Применение

![](images/PartMirroring_Scr1.png )


<div class="mw-translate-fuzzy">

1.  Выберите исходный объект из списка Фигуры.
2.  Выберите стандартную **Плоскость симметрии** из раскрывающегося меню.
3.  Нажмите **OK**, чтобы создать объект.


</div>

When the select button label says **Selecting** you are in reference selection mode and there is a selection gate in effect, which disallows the selection of unsupported reference objects. Click the button to toggle the selection gate off, the button label then changes to **Select reference**.

The mirror plane is defined by a **Normal** (direction) and a **Base** (position). When the **Mirror Plane** property contains a reference object these properties are made read-only as they are then computed based on that object. The plane is infinite even if the reference object is not.

A reference object can be a planar face, such as the face of a [Part Box](Part_Box.md), a circular edge, a [Datum Plane](PartDesign_Plane.md), an [origin plane](App_OriginGroupExtension.md) of a [Std Part](Std_Part.md) container, or any object with a single planar face or single circular edge. There is also support for [Links](App_Link.md). Note, however, that B-spline surfaces, such as [ruled surfaces](Part_RuledSurface.md) or [loft faces](Part_Loft.md) are not supported.



## Опции


<div class="mw-translate-fuzzy">

Поля ввода **Базовая точка** можно использовать для перемещения плоскости отражения параллельно выбранной стандартной плоскости отражения. Только одно поле ввода **X**, **Y** или **Z** будет иметь эффект для данной стандартной плоскости.


</div>


<div class="mw-translate-fuzzy">

  Плоскость симметрии   Базовая точка   Эффект
    
  **XY**                **Z**           Перемещает плоскость симметрии вдоль оси **Z**.
  **XY**                **X**, **Y**    Эффекта нет.
  **XZ**                **Y**           Перемещает плоскость симметрии вдоль оси **Y**.
  **XZ**                **X**, **Z**    Эффекта нет.
  **YZ**                **X**           Перемещает плоскость симметрии вдоль оси **X**.
  **YZ**                **Y**, **Z**    Эффекта нет.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Ограничения

-   Произвольные плоскости отражения (т.е. непараллельные стандартной плоскости) не поддерживаются.


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/ru
