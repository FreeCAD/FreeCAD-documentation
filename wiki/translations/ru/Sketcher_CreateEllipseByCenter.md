---
 GuiCommand:
   Name/ru: Создать эллипс от центра
   Name: Sketcher_CreateEllipseByCenter
   MenuLocation: Sketch , Геометрия эскиза , Создать эллипс от центра
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **G** **E** **E**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseBy3Points/ru, Sketcher_CreateCircle/ru, Sketcher_CreateArcOfEllipse/ru
---

# Sketcher CreateEllipseByCenter/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Этот инструмент рисует эллипс, по трем указанным точкам: центральной, большому радиусу, малому радиусу. При запуске инструмента указатель мыши меняется на белый крест с красным значком эллипса. Кроме того, координаты отображаются в режиме реального времени.


</div>

![](images/Sketcher_CreateEllipseByCenter_Example.png ) 
*Ellipse (white) with internal geometry (dark yellow)*



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 
Dim-OVP = Dimensional On-View-Parameters. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   Вызовите команду, нажав кнопку на панели инструментов, выбрав пункт меню или используя сочетание клавиш (сперва вы должны назначить их в [Настройках интерфейса](Interface_Customization/ru.md)).
-   Сначала в 3D-виде нажатием задайте центр эллипса. Вторым нажатием задайте первый радиус и ориентацию эллипса. Третьим нажатием задайте другой радиус (расстояние от линии, определенной первыми двумя нажатиями, является вторым радиусом).
-   После третьего нажатия создается эллипс вместе с набором вспомогательной геометрии, привязанной к нему (большой диаметр, малый диаметр, два фокуса). Вспомогательная геометрия может быть удалена вручную, если не нужна, и воссоздана позже. Смотрите [Sketcher Показать Скрытую Внутреннюю Геометрию](Sketcher_RestoreInternalAlignmentGeometry/ru.md).
-   Нажатие **ESC** или правой кнопки мыши отменяет функцию.


</div>

## Notes


<div class="mw-translate-fuzzy">

-   Большая и малая оси эллипсов являются строго определенными и не могут быть поменяны путем изменения размера эллипса. Это является следствием используемой параметризации решателя (Центр (x,y), фокус1 (x,y) и длина малого радиуса (b)) и точно такое же строгое поведение у OpenCascade. Что бы поменять оси, эллипс необходимо вращать.
-   Эллипс может функционировать как круг, когда его линии большого и малого диаметра удалены, и один из фокусов ограничен, чтобы совпадать с центром. Но ограничения радиуса не будут работать на таком круге.
-   Перемещение эллипса за ребро - это то же самое, что перемещение эллипса за центр.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/ru
