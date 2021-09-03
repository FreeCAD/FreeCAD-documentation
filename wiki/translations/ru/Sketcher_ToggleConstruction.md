---
- GuiCommand:/ru
   Name:Sketcher ToggleConstruction
   Name/ru:Вспомогательный режим
   MenuLocation:Sketch → Геометрия эскиза → Переключить построительную геометрию
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
---

## Описание

Этот инструмент переключает геометрию эскиза из/в вспомогательный режим. Может использоваться для любого типа геометрии: линии, дуги или круга.

Вспомогательная геометрия является важным инструментом в создании эскизов. При использовании эскиза для 3D-операций вспомогательная геометрия игнорируется.


<div class="mw-translate-fuzzy">

В <img alt="" src=images/Sketcher_EditSketch.svg  style="width:24px;"> [режиме редактирования эскиза](Sketcher_EditSketch/ru.md) вспомогательная геометрия отображается синим цветом и не становится зеленой, когда эскиз полностью ограничен. После <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:24px;"> [выхода из режима эскиза](Sketcher_LeaveSketch/ru.md) вспомогательная геометрия скрывается из [3D-вида](3D_view/ru.md).


</div>


<div class="mw-translate-fuzzy">

Линии вспомогательной геометрии могут использоваться в качестве осей вращения с помощью функции [PartDesign Вращение](PartDesign_Revolution/ru.md).


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">

## Использование


<div class="mw-translate-fuzzy">

1.  Выберите один или несколько элементов эскиза в [трёхмерном виде](3D_view/ru.md)
2.  Вызовите инструмент Sketcher ToggleConstruction одним из способов:
    -   Нажав кнопку <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> button
    -   Используя пункт меню Sketcher {{MenuCommand|Sketch → Геометрия эскиза → Переключить построительную геометрию}}


</div>

## Пример

Использование вспомогательного режима на некоторых элементах эскиза.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">


<div class="mw-translate-fuzzy">

и как только вы <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:24px;"> [покинете режим редактирования эскиза](Sketcher_LeaveSketch/ru.md), геометрия, которая была преобразована в вспомогательную, станет невидимой в [3D-виде](3D_view/ru.md) (но она все еще присутствует в режиме редактирования эскиза).


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}  
