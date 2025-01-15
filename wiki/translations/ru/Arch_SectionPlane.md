---
 GuiCommand:
   Name: Arch SectionPlane
   Name/ru: Arch SectionPlane
   MenuLocation: Архитектура -> Плоскость сечения
   Workbenches: Arch_Workbench/ru
   Shortcut: **S** **P**
   SeeAlso: Draft_Shape2DView/ru, TechDraw_ArchView/ru
---

# Arch SectionPlane/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент помещает в текущий документ \"что-то\" секущей плоскости, которое определяет сечение или план. \"Что-то\" получает своё положение в соответствии с текущей [рабочей плоскостью](Draft_SelectPlane/ru.md), и может быть перемещён и переориентирован через её перемещение и вращение, пока не получится требуемый двумерный вид. Секущая плоскость учитывает только определённый набор объектов. Выделенные в момент создания секущей плоскости добавляются в этот набор автоматически. Другие объекты могут быть позднее добавлены или удалены из объекта SectionPlane инструментами [Arch Add component](Arch_Add/ru.md) или [Arch Remove component](Arch_Remove/ru.md), или двойным кликом секущей плоскости в древе проекта.


</div>


<div class="mw-translate-fuzzy">

Сама по себе плоскость сечения не создаст никакого вида набора своих объектов. Для этого вы должны либо создать [Drawing DraftView](Draft_Drawing/ru.md), чтобы создать вид на [странице чертежа](Drawing_Workbench/ru.md), [Draft Shape2DView](Draft_Shape2DView/ru.md) для создания вида в самом 3D-документе, или [TechDraw ArchView](TechDraw_ArchView/ru.md) для создания представления на [странице TechDraw](TechDraw_Workbench/ru.md).


</div>

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">



## Применение


<div class="mw-translate-fuzzy">

1.  Если нужно, установить [Draft Working Plane](Draft_SelectPlane/ru.md) для отражения плоскости, на которой вы хотите разместить плоскость сечения.
2.  Выделить объекты, которые должны быть включены в сечение
3.  Нажмите кнопку **<img src="images/Arch_SectionPlane.svg" width=16px> [SectionPlane](Arch_SectionPlane/ru.md)
** или нажмите **S**, затем **P**
4.  [Move](Draft_Move/ru.md)/[rotate](Draft_Rotate/ru.md) Section Plane в правильное положение, если нужно.
5.  Выберите плоскость сечения, если она еще не выбрана.
6.  Используйте [Drawing DraftView](Draft_Drawing/ru.md), [Draft Shape2DView](Draft_Shape2DView/ru.md) или [TechDraw ArchView](TechDraw_ArchView/ru.md) для создания вида.


</div>



## Опции

-   The Section plane object will only consider a certain set of objects, not all the objects of the document. Objects can be added or removed from a SectionPlane object by using the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools, or by double-clicking the Section Plane in the tree view, selecting objects either in the list of in the 3D scene, and pressing the **add** or **remove** buttons.


<div class="mw-translate-fuzzy">

-   С выбранным объектом сечения используйте инструмент [Draft Shape2DView](Draft_Shape2DView/ru.md) для создания объекта, представляющего вид сечения в документе.


</div>

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Создайте дополнительные [Drawing DraftViews](Draft_Drawing.md), если Вы работаете с [верстаком Drawing](Drawing_Workbench/ru.md), или [TechDraw ArchView](TechDraw_ArchView/ru.md), если Вы используете [верстак TechDraw](TechDraw_Workbench/ru.md).


</div>

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   The Section Plane can also be used to show the entire 3D view cut by an infinite plane. This is only visual, and won\'t affect the geometry of the objects being cut.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">



## Свойства


<div class="mw-translate-fuzzy">

-    **Only Solids**: Если это `True`, объекты не твердых тел не будут учитываться в наборе.

-    **Display Length**: Длина \"чего-то\" плоскости сечения на трехмерном виде. Не влияет на итоговый вид

-    **Display Height**: Высота \"чего-то\" плоскости сечения в трехмерном виде. Не влияет на итоговый вид

-    **Arrow Size**: Размер стрелок в \"чём-то\" секущей плоскости в трёхмерном виде. Не влияет на итоговый вид

-    **Cut View**: Если это `True`, весь трёхмерный вид будет рассечён по месту этой секущей плоскости.

-    **Clip view**: Если это `True`, он будет обрезать вид до отображаемой высоты и длины плоскости сечения. Это эффективно превращает плоскость сечения в ортогональную камеру, ограничивая поле зрения. <small>(v0.19)</small> 


</div>

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*The Arch SectionPlane with the clip view option will behave like a camera, limiting the field of view.*

## Tweaks

-   Adding manually a property named **RotateSolidRender** of type **App::PropertyAngle** to the section plane\'s **View** properties (right-click the properties view -\> show all, right-click again -\> add property) allows to rotate the render when using Solid mode. This is useful when a rendered view has for example both Arch and Draft elements, and the rendering of the Arch elements is rotated in relation to the Draft elements.

## Scripting


<div class="mw-translate-fuzzy">

## Программирование


**См. так же:**

[Arch API](Arch_API/ru.md) и [Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>


<div class="mw-translate-fuzzy">

Инструмент SectionPlane может использоваться в [макросах](macros/ru.md) и в консоли [Python](Python.md) с использованием следующих функций:


</div>


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```

-   Создаёт объект `Section` из `objectslist`, который есть список объектов.

Пример:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Arch SectionPlane/ru
