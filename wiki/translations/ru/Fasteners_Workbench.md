# <img alt="Логотип верстака Fasteners" src=images/Fasteners_workbench_icon.svg  style="width:64px;"> Fasteners Workbench/ru


{{TOCright}}

## Введение

Верстак <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [Fasteners (Стандартные Изделия)](Fasteners_Workbench/ru.md) предназначен для быстрого и удобного добавления различных крепежных изделий. На данный момент является [внешним верстаком](External_workbenches/ru.md).

## Применение

Применить верстак достаточно легко:

1.  Установите верстак Fasteners через [менеджер дополнений](Addon_Manager/ru.md).
2.  Создайте новый документ в FreeCAD.
3.  Выберите <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:24px;"> [верстак Fasteners](Fasteners_Workbench/ru.md) из [списка верстаков](Std_Workbench/ru.md).
4.  После чего будут отображены [панели инструментов](#Toolbars.md), принадлежащие данному рабочему столу.

Простые примеры применения верстака: Нажатие на любую из кнопок с изображением стандартного изделия что бы создать это стандартное изделие в центре координат со свойствами по умолчанию. Для того, чтобы изменить свойства стандартного изделия, выберите его и откройте вкладку **Data** в [редакторе свойств](Property_editor/ru.md).

## Известные проблемы 

-   Other issues/feature requests can be found on the [Fastener Workbench GitHub issue queue](https://github.com/shaise/FreeCAD_FastenersWB/issues?utf8=✓&q=is%3Aissue)

## Справочные данные 

-   Автор: [shaise](http://theseger.com/projects/author/shaise/)
    -   Автор ScrewMaker: Ulrich Brammer
    -   Автор обертки (wrapper) верстака: Shai Seger
-   Домашняя страница: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Исходный код на github: <https://github.com/shaise/FreeCAD_FastenersWB>

## Установка

This workbench can be installed from the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). For manual installation see [Installing more workbenches](Installing_more_workbenches.md).

## Панели инструментов 

The Fasteners Workbench has two toolbars. The **FS Screws** toolbar contains many tools. If required it can be expanded by pressing the **&gt;&gt;** button.

![](images/Fasteners_toolbars.png ) 
*Панель инструментов верстака Fasteners*

## Инструменты

Подробное описание смотрите по ссылке: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>.

### Команды

-   <img alt="" src=images/Fasteners_Flip.svg  style="width:32px;"> [Invert fastener](Fasteners_Flip.md): меняет ориентацию крепежа на противоположную.

-   <img alt="" src=images/Fasteners_Move.svg  style="width:32px;"> [Move fastener](Fasteners_Move.md): перемещает крепеж.

-   <img alt="" src=images/Fasteners_Shape.svg  style="width:32px;"> [Simplify shape](Fasteners_Shape.md): преобразует объект в простую не параметрическую фигуру.

-   <img alt="" src=images/Fasteners_MatchTypeInner.svg  style="width:32px;"> [Match screws by inner thread diameter (Tap hole)](Fasteners_MatchTypeInner.md): подобрать резьбу по диаметру внутренний резьбы (отверстия).

-   <img alt="" src=images/Fasteners_MatchTypeOuter.svg  style="width:32px;"> [Match screws by outer thread diameter (Pass hole)](Fasteners_MatchTypeOuter.md): подобрать резьбу по диаметру внутренний резьбы (отверстия под метчик).

-   <img alt="" src=images/Fasteners_BOM.svg  style="width:32px;"> [Generate BOM](Fasteners_BOM.md): генерирует спецификацию стандартных изделий.

-   <img alt="" src=images/Fasteners_ScrewCalculator.svg  style="width:32px;"> [Screw calculator](Fasteners_ScrewCalculator.md): открывает калькулятор резьбы.

-   <img alt="" src=images/Fasteners_ChamferHole.svg  style="width:32px;"> [Make countersunk](Fasteners_ChamferHole.md): делает фаску для крепежа с потайной головкой.

-   <img alt="" src=images/Fasteners_ChangeParameters.svg  style="width:32px;"> [Change fastener parameters](Fasteners_ChangeParameters.md): позволяет изменить параметры стандартных изделий.

### Fasteners

**Note:** Fasteners with metric dimensions have light orange icons. Fasteners with inch dimensions have green icons.


<div class="mw-translate-fuzzy">

### Самозатягивающиеся крепёжные изделия и крепёжные изделия для Печатных Плат 


</div>

-   <img alt="" src=images/Fasteners_PEMPressNut.svg  style="width:32px;"> Self-clinching metric nut.

-   <img alt="" src=images/Fasteners_PEMTHStandoff.svg  style="width:32px;"> Self-clinching metric standoff.

-   <img alt="" src=images/Fasteners_PEMStud.svg  style="width:32px;"> Self-clinching metric stud.

-   <img alt="" src=images/Fasteners_PCBStandoff.svg  style="width:32px;"> **PCB** Metric standoff Female/Male.

-   <img alt="" src=images/Fasteners_PCBSpacer.svg  style="width:32px;"> **PCB** Metric spacer Female/Female.


<div class="mw-translate-fuzzy">

### Крепежные изделия DIN, EN и ISO 


</div>

ISO, DIN and EN fasteners have metric dimensions.

-   <img alt="" src=images/Fasteners_ISO4017.svg  style="width:32px;"> 
**ISO 4017** Hexagon head screw. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4014.svg  style="width:32px;"> 
**ISO 4014** Hexagon head bolt. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_EN1662.svg  style="width:32px;"> **EN 1662** Hexagon head bolt with flange, small series.

-   <img alt="" src=images/Fasteners_EN1665.svg  style="width:32px;"> **EN 1665** Hexagon bolt with flange, heavy series.

-   <img alt="" src=images/Fasteners_ISO4762.svg  style="width:32px;"> **ISO 4762** Hexagon socket head cap screw.

-   <img alt="" src=images/Fasteners_DIN7984.svg  style="width:32px;"> **DIN 7984** Hexagon socket head cap screw with low head.

-   <img alt="" src=images/Fasteners_DIN6912.svg  style="width:32px;"> **DIN 6912** Hexagon socket head cap screw with low head with center.

-   <img alt="" src=images/Fasteners_ISO7380-1.svg  style="width:32px;"> **ISO 7380-1** Hexagon socket button head screw.

-   <img alt="" src=images/Fasteners_ISO7380-2.svg  style="width:32px;"> **ISO 7380-2** Hexagon socket button head screw with collar.

-   <img alt="" src=images/Fasteners_ISO10642.svg  style="width:32px;"> **ISO 10642** Hexagon socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ISO2009.svg  style="width:32px;"> 
**ISO 2009** Slotted countersunk flat head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO2010.svg  style="width:32px;"> 
**ISO 2010** Slotted raised countersunk head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO1580.svg  style="width:32px;"> 
**ISO 1580** Slotted pan head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO1207.svg  style="width:32px;"> 
**ISO 1207** Slotted cheese head screw. *Product grade A.*

-   <img alt="" src=images/Fasteners_DIN967.svg  style="width:32px;"> **DIN 967** Cross recessed pan head screw with collar.

-   <img alt="" src=images/Fasteners_ISO7045.svg  style="width:32px;"> 
**ISO 7045** Pan head screw type H cross recess. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7046.svg  style="width:32px;"> 
**ISO 7046** Countersunk flat head screw H cross recess. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7047.svg  style="width:32px;"> 
**ISO 7047** Raised countersunk head screw H cross recess. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7048.svg  style="width:32px;"> **ISO 7048** Cheese head screw with type H cross recess.

-   <img alt="" src=images/Fasteners_ISO14579.svg  style="width:32px;"> **ISO 14579** Hexalobular socket head cap screw.

-   <img alt="" src=images/Fasteners_ISO14580.svg  style="width:32px;"> **ISO 14580** Hexalobular socket cheese head screw.

-   <img alt="" src=images/Fasteners_ISO14582.svg  style="width:32px;"> **ISO 14582** Hexalobular socket countersunk head screw, high head.

-   <img alt="" src=images/Fasteners_ISO14583.svg  style="width:32px;"> **ISO 14583** Hexalobular socket pan head screw.

-   <img alt="" src=images/Fasteners_ISO14584.svg  style="width:32px;"> **ISO 14584** Hexalobular socket raised countersunk head screw.

-   <img alt="" src=images/Fasteners_ISO7379.svg  style="width:32px;"> **ISO 7379** Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ISO7089.svg  style="width:32px;"> 
**ISO 7089** Plain washer, normal series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7090.svg  style="width:32px;"> 
**ISO 7090** Plain washer chamfered, normal series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7092.svg  style="width:32px;"> **ISO 7092** Plain washer, small series.

-   <img alt="" src=images/Fasteners_ISO7093-1.svg  style="width:32px;"> 
**ISO 7093-1** Plain washer, large series. *Product grade A.*

-   <img alt="" src=images/Fasteners_ISO7094.svg  style="width:32px;"> **ISO 7094** Plain washer, extra large series.

-   <img alt="" src=images/Fasteners_ISO4026.svg  style="width:32px;"> **ISO 4026** Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ISO4027.svg  style="width:32px;"> **ISO 4027** Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ISO4028.svg  style="width:32px;"> **ISO 4028** Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ISO4029.svg  style="width:32px;"> **ISO 4029** Hexagon socket set screw with cup point.

-   <img alt="" src=images/Fasteners_ISO4032.svg  style="width:32px;"> 
**ISO 4032** Hexagon nut, style 1. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4033.svg  style="width:32px;"> 
**ISO 4033** Hexagon nut, style 2. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_ISO4035.svg  style="width:32px;"> 
**ISO 4035** Hexagon thin nut, chamfered. *Product grades A and B.*

-   <img alt="" src=images/Fasteners_EN1661.svg  style="width:32px;"> **EN 1661** Hexagon nut with flange.

-   <img alt="" src=images/Fasteners_DIN557.svg  style="width:32px;"> **DIN 557** Square nut.

-   <img alt="" src=images/Fasteners_DIN562.svg  style="width:32px;"> **DIN 562** Square nut.

-   <img alt="" src=images/Fasteners_DIN985.svg  style="width:32px;"> **DIN 985** Nyloc nut.


<div class="mw-translate-fuzzy">

### Крепежные изделия ASME (American Society of Mechanical Engineers) 


</div>

ASME fasteners have inch dimensions.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.6.svg  style="width:32px;"> **ASME B18.2.1.6** UNC Hex head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.2.1.8.svg  style="width:32px;"> **ASME B18.2.1.8** UNC Hex head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.1A.svg  style="width:32px;"> **ASME B18.2.2.1A** UNC Machine screw nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4A.svg  style="width:32px;"> **ASME B18.2.2.4A** UNC Hexagon nut.

-   <img alt="" src=images/Fasteners_ASMEB18.2.2.4B.svg  style="width:32px;"> **ASME B18.2.2.4B** UNC Hexagon thin nut.

-   <img alt="" src=images/Fasteners_ASMEB18.3.1A.svg  style="width:32px;"> **ASME B18.3.1A** UNC Hex socket head cap screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.2.svg  style="width:32px;"> **ASME B18.3.2** UNC Hex socket countersunk head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3A.svg  style="width:32px;"> **ASME B18.3.3A** UNC Hex socket button head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.3B.svg  style="width:32px;"> **ASME B18.3.3B** UNC Hex socket button head screw with flange.

-   <img alt="" src=images/Fasteners_ASMEB18.3.4.svg  style="width:32px;"> **ASME B18.3.4** UNC Hexagon socket head shoulder screw.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5A.svg  style="width:32px;"> **ASME B18.3.5A** UNC Hexagon socket set screw with flat point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5B.svg  style="width:32px;"> **ASME B18.3.5B** UNC Hexagon socket set screw with cone point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5C.svg  style="width:32px;"> **ASME B18.3.5C** UNC Hexagon socket set screw with dog point.

-   <img alt="" src=images/Fasteners_ASMEB18.3.5D.svg  style="width:32px;"> **ASME B18.3.5D** UNC Hexagon socket set screw with cup point.

-   <img alt="" src=images/Fasteners_ASMEB18.6.3.1A.svg  style="width:32px;"> **ASME B18.6.3.1A** UNC slotted countersunk flat head screw.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12A.svg  style="width:32px;"> **ASME B18.21.1.12A** UN washer, narrow series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12B.svg  style="width:32px;"> **ASME B18.21.1.12B** UN washer, regular series.

-   <img alt="" src=images/Fasteners_ASMEB18.21.1.12C.svg  style="width:32px;"> **ASME B18.21.1.12C** UN washer, wide series.

### Другие крепежные изделия 

-   <img alt="" src=images/Fasteners_ScrewTap.svg  style="width:32px;"> Arbitrary length threaded rod for tapping holes (metric).

-   <img alt="" src=images/Fasteners_ScrewTapInch.svg  style="width:32px;"> Arbitrary length threaded rod for tapping holes (inch).

-   <img alt="" src=images/Fasteners_ScrewDie.svg  style="width:32px;"> Arbitrary length threaded tube for cutting external threads (metric).

-   <img alt="" src=images/Fasteners_ScrewDieInch.svg  style="width:32px;"> Arbitrary length threaded tube for cutting external threads (inch).

-   <img alt="" src=images/Fasteners_ThreadedRod.svg  style="width:32px;"> Arbitrary length **DIN 975** threaded rod (metric).

-   <img alt="" src=images/Fasteners_ThreadedRodInch.svg  style="width:32px;"> Arbitrary length **UNC** threaded rod (inch).

## Прочие

-   <img alt="" src=images/preferences-fasteners.svg  style="width:32px;"> 
**Fasteners Preferences**
-   <img alt="" src=images/Fasteners_workbench_icon.svg  style="width:32px;"> 
**Fasteners Workbench icon**

## Ссылки связанные с верстаком 

-   Workbench Wiki: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   FreeCAD Wiki: <https://www.freecadweb.org/wiki/Fasteners_Workbench>
-   FreeCAD Forum: <https://forum.freecadweb.org/viewtopic.php?t=11429>
-   Tutorials - How to use: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>
-   Videos:
-   Files:
-   Report bugs: Please report bugs at <https://github.com/shaise/FreeCAD_FastenersWB/issues>
-   Installation: <http://theseger.com/projects/2015/06/fasteners-workbench-for-freecad/>

## Другие ссылки 

-   [Generating holes for countersunk screws in freecad](http://theseger.com/projects/2015/07/generating-holes-for-countersunk-screws-in-freecad/)
-   [BOLTS](https://github.com/jreinhardt/BOLTS): An Open Library for Technical Specifications
-   [External workbenches](External_workbenches.md)
-   [Macros recipes](Macros_recipes.md)



_ _ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Fasteners Workbench/ru
