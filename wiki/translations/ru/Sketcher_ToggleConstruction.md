---
- GuiCommand:/ru
   Name/ru:Переключить построительную геометрию
   Name:Sketcher_ToggleConstruction
   MenuLocation:Sketch → Геометрия эскиза → Переключить построительную геометрию
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
---

# Sketcher ToggleConstruction/ru


</div>

## Описание

Этот инструмент переключает геометрию эскиза из/в вспомогательный режим. Может использоваться для любого типа геометрии: линии, дуги или круга.

Вспомогательная геометрия является важным инструментом в создании эскизов. При использовании эскиза для 3D-операций вспомогательная геометрия игнорируется.


<div class="mw-translate-fuzzy">

В <img alt="" src=images/Sketcher_EditSketch.svg  style="width:24px;"> [режиме редактирования эскиза](Sketcher_EditSketch/ru.md) вспомогательная геометрия отображается синим цветом и не становится зеленой, когда эскиз полностью ограничен. После <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:24px;"> [выхода из режима эскиза](Sketcher_LeaveSketch/ru.md) вспомогательная геометрия скрывается из [3D-вида](3D_view/ru.md).


</div>

Линии вспомогательной геометрии могут использоваться в качестве осей вращения с помощью функции **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Вращение](PartDesign_Revolution/ru.md)**.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">

## Применение


<div class="mw-translate-fuzzy">

1.  Выберите один или несколько элементов эскиза в [трёхмерном виде](3D_view/ru.md)
2.  Вызовите инструмент Sketcher ToggleConstruction одним из способов:
    -   Нажав кнопку <img alt="" src=images/Sketcher_AlterConstruction.svg  style="width:24px;"> button
    -   Используя пункт меню Sketcher **Sketch → Геометрия эскиза → Переключить построительную геометрию**


</div>

## Пример

Использование вспомогательного режима на некоторых элементах эскиза.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">


<div class="mw-translate-fuzzy">

и как только вы <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:24px;"> [покинете режим редактирования эскиза](Sketcher_LeaveSketch/ru.md), геометрия, которая была преобразована в вспомогательную, станет невидимой в [3D-виде](3D_view/ru.md) (но она все еще присутствует в режиме редактирования эскиза).


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">

## Notes

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Create point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** to change them to normal geometry. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/ru
