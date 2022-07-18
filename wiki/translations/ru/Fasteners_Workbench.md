# <img alt="Логотип верстака Fasteners" src=images/Fasteners_workbench_icon.svg  style="width   *64px;"> Fasteners Workbench/ru


{{TOCright}}

## Введение


<div class="mw-translate-fuzzy">

Верстак <img alt="" src=images/Fasteners_workbench_icon.svg  style="width   *24px;"> [Fasteners (Стандартные Изделия)](Fasteners_Workbench/ru.md) предназначен для быстрого и удобного добавления различных крепежных изделий. На данный момент является [внешним верстаком](External_workbenches/ru.md).


</div>

![](images/Fasteners_toolbars.png )


<div class="mw-translate-fuzzy">

![](images/Fasteners_toolbars.png ) 
*Панель инструментов верстака Fasteners*


</div>

## Установка


<div class="mw-translate-fuzzy">

Применить верстак достаточно легко   *

1.  Установите верстак Fasteners через [менеджер дополнений](Std_AddonMgr/ru.md).
2.  Создайте новый документ в FreeCAD.
3.  Выберите <img alt="" src=images/Fasteners_workbench_icon.svg  style="width   *24px;"> [верстак Fasteners](Fasteners_Workbench/ru.md) из [списка верстаков](Std_Workbench/ru.md).
4.  После чего будут отображены [панели инструментов](#Toolbars.md), принадлежащие данному рабочему столу.


</div>

## Применение

Fasteners can be attached or unattached. Attached fasteners have a **base Object**, a circular edge, and their **Placement** is dynamically linked to that object. The <img alt="" src=images/Fasteners_Move.svg  style="width   *16px;"> [Fasteners Move](Fasteners_Move.md) command can be used to attach or detach a fastener.

### Unattached fasteners 

1.  Select the desired fastener by clicking its button or by picking it from the menu.
2.  A fastener is created at the origin.
3.  Optionally change the dimensions and other properties of the fastener   *
    1.  Select the fastener.
    2.  Go to the **Data** tab of the [Property editor](Property_editor.md).
    3.  Change the required properties.

### Attached fasteners 

<img alt="" src=images/Fasteners_Attached_Selected.png  style="width   *200px;"> <img alt="" src=images/Fasteners_Attached_Created.png  style="width   *200px;"> 
*On the left two selected circular edges. On the right the attached fasteners.*

1.  Specify if the selected holes are tap holes or pass holes by selecting <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width   *16px;"> [Fasteners MatchTypeInner](Fasteners_MatchTypeInner.md) or <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width   *16px;"> [Fasteners MatchTypeOuter](Fasteners_MatchTypeOuter.md) respectively (not used for countersunk screws).
2.  Select one or more circular edges and/or faces with circular edges. For countersunk screws the top edge of the [chamfered hole](Fasteners_ChamferHole.md) must be selected.
3.  Select the desired fastener by clicking its button or by picking it from the menu.
4.  A fastener is attached to each of the selected circular edges.
5.  The default dimensions of each fastener depend on the radius of the circular edge it is attached to. Countersunk screws are matched by their head diameter, other fasteners are matched by their shaft diameter.
6.  Optionally change the dimensions and other properties of the fasteners. See above.
7.  Fasteners that appear upside-down can be inverted with the <img alt="" src=images/Fasteners_Flip.svg  style="width   *16px;"> [Fasteners Flip](Fasteners_Flip.md) command or by changing their **invert** property.
8.  Optionally change the **offset** property to create space between the fasteners and the edges they are attached to.

## Notes

-   To generate threads, the **thread** property of a fastener must be changed to `True`. Generating threads is costly. Recomputes take much longer if there are many fasteners with threads in a document.
-   The **invert** property and the **offset** property are ignored for unattached fasteners.


<div class="mw-translate-fuzzy">

### Команды


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_Flip.svg  style="width   *32px;"> [Invert fastener](Fasteners_Flip.md)   * меняет ориентацию крепежа на противоположную.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_Move.svg  style="width   *32px;"> [Move fastener](Fasteners_Move.md)   * перемещает крепеж.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_Shape.svg  style="width   *32px;"> [Simplify shape](Fasteners_Shape.md)   * преобразует объект в простую не параметрическую фигуру.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width   *32px;"> [Match screws by inner thread diameter (Tap hole)](Fasteners_MatchTypeInner.md)   * подобрать резьбу по диаметру внутренний резьбы (отверстия).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width   *32px;"> [Match screws by outer thread diameter (Pass hole)](Fasteners_MatchTypeOuter.md)   * подобрать резьбу по диаметру внутренний резьбы (отверстия под метчик).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_BOM.svg  style="width   *32px;"> [Generate BOM](Fasteners_BOM.md)   * генерирует спецификацию стандартных изделий.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width   *32px;"> [Screw calculator](Fasteners_ScrewCalculator.md)   * открывает калькулятор резьбы.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width   *32px;"> [Make countersunk](Fasteners_ChamferHole.md)   * делает фаску для крепежа с потайной головкой.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width   *32px;"> [Change fastener parameters](Fasteners_ChangeParameters.md)   * позволяет изменить параметры стандартных изделий.


</div>

## Fasteners

Fasteners with metric dimensions have orange icons. Fasteners with inch dimensions have green icons.


<div class="mw-translate-fuzzy">

### Самозатягивающиеся крепёжные изделия и крепёжные изделия для Печатных Плат 


</div>

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width   *32px;"> Self-clinching nut.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width   *32px;"> Self-clinching standoff.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width   *32px;"> Self-clinching stud.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width   *32px;"> PCB standoff Female/Male.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width   *32px;"> PCB spacer Female/Female.

-   <img alt="" src=images/Fasteners_IUTHeatInsert.svg  style="width   *32px;"> Heat staked insert.

### Hexagon head screws and bolts 

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width   *32px;"> 
**ISO 4017** Hexagon head screw. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width   *32px;"> 
**ISO 4014** Hexagon head bolt. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width   *32px;"> **EN 1662** Hexagon head bolt with flange, small series.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width   *32px;"> **EN 1665** Hexagon head bolt with flange, heavy series.

-   <img alt="" src=images/Fasteners_DIN571.svg  style="width   *32px;"> **DIN 571** Hexagon head wood screw.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width   *32px;"> **ASME B18.2.1.6** UNC Hexagon head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width   *32px;"> **ASME B18.2.1.8** UNC Hexagon head screw with flange.

### Hexagon socket screws 

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width   *32px;"> **ISO 4762** Hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width   *32px;"> **DIN 7984** Hexagon socket head cap screw with low head.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width   *32px;"> **DIN 6912** Hexagon socket head cap screw with low head with center.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width   *32px;"> **ISO 7380-1** Hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width   *32px;"> **ISO 7380-2** Hexagon socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width   *32px;"> **ISO 10642** Hexagon socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width   *32px;"> **ISO 7379** Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width   *32px;"> **ISO 4026** Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width   *32px;"> **ISO 4027** Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width   *32px;"> **ISO 4028** Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width   *32px;"> **ISO 4029** Hexagon socket set screw with cup point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width   *32px;"> **ASME B18.3.1A** UNC Hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width   *32px;"> **ASME B18.3.2** UNC Hexagon socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width   *32px;"> **ASME B18.3.3A** UNC Hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width   *32px;"> **ASME B18.3.3B** UNC Hexagon socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width   *32px;"> **ASME B18.3.4** UNC Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width   *32px;"> **ASME B18.3.5A** UNC Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width   *32px;"> **ASME B18.3.5B** UNC Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width   *32px;"> **ASME B18.3.5C** UNC Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width   *32px;"> **ASME B18.3.5D** UNC Hexagon socket set screw with cup point.

### Hexalobular socket head screws 

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width   *32px;"> **ISO 14579** Hexalobular socket head cap screw.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width   *32px;"> **ISO 14580** Hexalobular socket cheese head screw.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width   *32px;"> **ISO 14582** Hexalobular socket countersunk head screw, high head.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width   *32px;"> **ISO 14583** Hexalobular socket pan head screw.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width   *32px;"> **ISO 14584** Hexalobular socket raised countersunk head screw.

### Slotted head screws 

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width   *32px;"> 
**ISO 2009** Slotted countersunk flat head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width   *32px;"> 
**ISO 2010** Slotted raised countersunk head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width   *32px;"> 
**ISO 1580** Slotted pan head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width   *32px;"> 
**ISO 1207** Slotted cheese head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width   *32px;"> **ASME B18.6.3.1A** UNC slotted countersunk flat head screw.

### H cross head screws 

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width   *32px;"> **DIN 967** Pan head screw with collar with type H cross recess.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width   *32px;"> 
**ISO 7045** Pan head screw with type H cross recess. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width   *32px;"> 
**ISO 7046** Countersunk flat head screw with type H cross recess. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width   *32px;"> 
**ISO 7047** Raised countersunk head screw with type H cross recess. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width   *32px;"> **ISO 7048** Cheese head screw with type H cross recess.

### Other head bolts 

-   <img alt="" src=images/Fasteners_ASMEB18.5.2.svg  style="width   *32px;"> **ASME B18.5** UNC Round head square neck bolt.

### Nuts

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width   *32px;"> 
**ISO 4032** Hexagon nut, style 1. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width   *32px;"> 
**ISO 4033** Hexagon nut, style 2. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width   *32px;"> 
**ISO 4035** Hexagon thin nut, chamfered. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width   *32px;"> **EN 1661** Hexagon nut with flange.

-   <img alt="" src=images/Fasteners_DIN917.svg  style="width   *32px;"> **DIN 917** Cap nut, low form.

-   <img alt="" src=images/Fasteners_DIN1587.svg  style="width   *32px;"> **DIN 1587** Cap nut.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width   *32px;"> **DIN 557** Square nut.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width   *32px;"> **DIN 562** Square nut.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width   *32px;"> **DIN 985** Nyloc nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width   *32px;"> **ASME B18.2.2.1A** UNC Machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width   *32px;"> **ASME B18.2.2.4A** UNC Hexagon nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width   *32px;"> **ASME B18.2.2.4B** UNC Hexagon thin nut.

### Washers

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width   *32px;"> 
**ISO 7089** Plain washer, normal series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width   *32px;"> 
**ISO 7090** Plain washer chamfered, normal series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width   *32px;"> **ISO 7092** Plain washer, small series.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width   *32px;"> 
**ISO 7093-1** Plain washer, large series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width   *32px;"> **ISO 7094** Plain washer, extra large series.

-   <img alt="" src=images/Fasteners_NFE27-619.svg  style="width   *32px;"> **NFE27-619** Countersunk washer.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width   *32px;"> **ASME B18.21.1.12A** UN washer, narrow series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width   *32px;"> **ASME B18.21.1.12B** UN washer, regular series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width   *32px;"> **ASME B18.21.1.12C** UN washer, wide series.

### Другие крепежные изделия 

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width   *32px;"> Arbitrary length threaded rod for tapping holes.

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width   *32px;"> Arbitrary length threaded rod for tapping holes.

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width   *32px;"> Arbitrary length threaded tube for cutting external threads.

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width   *32px;"> Arbitrary length threaded tube for cutting external threads.

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width   *32px;"> Arbitrary length **DIN 975** threaded rod.

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width   *32px;"> Arbitrary length **UNC** threaded rod.

## Справочные данные 


<div class="mw-translate-fuzzy">

-   Автор   * [shaise](http   *//theseger.com/projects/author/shaise/)
    -   Автор ScrewMaker   * Ulrich Brammer
    -   Автор обертки (wrapper) верстака   * Shai Seger
-   Домашняя страница   * <http   *//theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Исходный код на github   * <https   *//github.com/shaise/FreeCAD_FastenersWB>


</div>

## Links

-   [Generating holes for countersunk screws in freecad](http   *//theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [BOLTS](https   *//github.com/jreinhardt/BOLTS)   * An open library for technical specifications.
-   [External workbenches](External_workbenches.md)
-   [Macros recipes](Macros_recipes.md)



[Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md) [Category   *External Workbenches](Category_External_Workbenches.md) [Category   *Fasteners](Category_Fasteners.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > [External Workbenches](Category_External Workbenches.md) > [Fasteners](Category_Fasteners.md) > Fasteners Workbench/ru
