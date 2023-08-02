---
- GuiCommand:
   Name/ru: Ограничение вертикальности
   Name: Sketcher_ConstrainVertical
   MenuLocation: Sketch -> Ограничения эскиза -> Ограничение вертикальности
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **V**
   SeeAlso: Sketcher_ConstrainHorizontal/ru
---

# Sketcher ConstrainVertical/ru

## Описание

Накладывает ограничение вертикальности на выделенные линии или элементы полилинии. В <small>(v0.17)</small> , оно так же накладывает ограничение вертикальности на вершины. Может быть выделено несколько объектов.

## Применение


<div class="mw-translate-fuzzy">

1.  Выделите линии или вершины, которые надо ограничить вертикальностью
2.  Для вызова команды вертикального ограничения:
    -   Нажмите иконку **[<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Ограничение вертикальности](Sketcher_ConstrainVertical/ru.md)**.
    -   Используйте клавиатурное сокращение **V**
    -   Используйте в ниспадающем меню Sketch пункт **Sketch → Ограничения эскиза → Ограничение вертикальности**
3.  Или инструмент может быть запущен без предварительного выделения и будет ожидать выделения; но выделяемыми станут только линии.
4.  Сделайте правый клик или нажмите **Esc** для выхода из инструмента.


</div>

## Программирование


```pythonSketch.addConstraint(Sketcher.Constraint('Vertical', Line))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainVertical/ru
