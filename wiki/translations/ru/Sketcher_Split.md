---
- GuiCommand:/ru
   Name/ru:Разделить ребро
   Name:Sketcher_Split
   MenuLocation:Sketch → Геометрия эскиза → Разделить ребро
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Version:0.20
   SeeAlso:[Обрезать кривую](Sketcher_Trimming/ru.md)
---

# Sketcher Split/ru

## Описание

Данный инструмент позволяет разделить ребро на две абсолютно одинаковые части, с сохранением большинства ограничений. Ограничения сохраняются для вновь созданных ребер, за исключением точки в которой произошло разделение. Окружность в случае её разделения, делится на дуги концы которых не связанны между собой, при этом ограничения которые имела окружность, переносятя на вновь созданные созданные дуги.

![](images/SketcherSplitExample1.png ) ![](images/SketcherSplitExample2.png ) ![](images/SketcherSplitExample3.png )

## Применение

1.  Нажмите кнопку **[<img src=images/Sketcher_Split.svg style="width:16px"> [Разделить](Sketcher_Split.md)**. Указатель мыши примет форму белого перекрестия с значком разделения.
2.  Кликните на ребро в том месте, где вы хотите его разделить.
3.  Ребра в форме линии или дуги будут поделены на два новых фрагмента, соединенных точкой в месте разделения. Окружность будет разделена на дуги с той же центральной точкой и другими ограничениями, которые были у исходной окружности.
4.  Нажатие **Esc** или нажатие правой кнопки мыши завершит работу функции.

## Ограничения

-   Для эллипса, параболы, гиперболы и B-сплайнов действие данной команды пока еще не поддерживается.

## Примечания

-   All coincidences are transferred - start point, end point and center point (if applicable).
-   Point on object constraint is transferred to the closer newly created edge.
-   Vertical and horizontal constraints are copied to both offsprings.
-   Parallel and perpendicular constraints are copied for both line segments, for arc only once, to the closer part.
-   Equality constraint is transferred only for resulting arc edges, line segments do not receive it.
-   Symmetry constraint is currently not transferred.
-   Block constraint is currently not transferred.
-   Horizontal, vertical and length constraints between points are transferred to the outer points of the new edges.
-   Point distance constraint is assigned only once, to the closer edge segment.
-   Radius and diameter constraints are copied to any resulting arc.
-   Angle constraint is currently not transferred





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/ru
