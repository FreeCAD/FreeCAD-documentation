---
 GuiCommand:
   Name: Sketcher Extend
   Name/ru: Продлить
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **G** **Q**
   MenuLocation: Эскиз , Геометрия эскиза , Продлить
   Version: 0.17
   SeeAlso: Sketcher_Trimming/ru
---

# Sketcher Extend/ru



## Описание

Инструмент **Продлить** позволяет продлить отрезок на эскизе до указанной грани или точки указанной указателем мыши.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*Слева показано (1), два элемента эскиза перед операцией; в середине (2), линия продлена до дуги; справа (3), конечный результат.*



## Применение


<div class="mw-translate-fuzzy">

1.  Нажмите кнопку <img alt="" src=images/Sketcher_Extend.svg  style="width:24px;"> **Продлить**.
2.  Выберите линию или дугу.
3.  В 3D виде переместите указатель мыши в направлении продления.
4.  Нажмите в произвольном месте, или что бы продлить до другого ребра, поместите указатель мыши на ребре; когда оно будет выделено и над ним появится<img alt="" src=images/Sketcher_ConstrainPointOnObject.png  style="width:24px;"> [точка](Sketcher_ConstrainPointOnObject/ru.md) ограничения, помимо указателя мыши, нажмите для подтверждения. На объект будет добавлена точка ограничения.
5.  Что бы продлить до точки на эскизе, поместите указатель мыши над точкой; когда она будет выделена и над ней появится значек <img alt="" src=images/Sketcher_ConstrainCoincident.png  style="width:24px;"> [ограничения совпадением](Sketcher_ConstrainCoincident.md), по мимо указателя мыши, нажмите для подтверждения. Будет добавленио ограничение совпадением.


</div>



## Примечания

-   Only arcs and lines can be extended at this time.
-   The target edge or point object may be modified as well if it is not fully constrained.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/ru
