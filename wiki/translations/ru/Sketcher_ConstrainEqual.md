---
 GuiCommand:
   Name/ru: Ограничение эквивалентностью
   Name: Sketcher_ConstrainEqual
   MenuLocation: Sketch , Ограничения эскиза , Ограничение эквивалентностью
   Workbenches: Sketcher_Workbench/ru
   Shortcut: E
   SeeAlso: Sketcher_ConstrainRadius/ru
---

# Sketcher ConstrainEqual/ru


</div>

## Описание

Ограничение эквивалентности делает равным длину указанных отрезков в линии, ломаной или прямоугольнике. При применении к дугам или окружностям их радиусы становятся равными. Данное ограничение нельзя применять к геометрическим примитивам, которые не относятся к одному и тому же типу (например, нельзя применить к отрезку и дуге).

## Oперация

The example sketch below contains a number of sketch primitives (line, poly-line, rectangle, arc and circle).

![](images/EqualConstraint1.png )

Select two or more line segments (e.g. line and one side of the rectangle).

![](images/EqualConstraint2.png )

Click on **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** in the Sketcher toolbar (in either the Sketcher or Part Design workbenches) or select the Constrain Equal menu item from the Sketcher constraints sub menu item in either the Sketch or Part Design menu item depending upon which workbench is selected (Sketcher or Part Design) to apply the constraint to the selected items.

![](images/EqualConstraint3.png )

Now select the arc and the circle in the sketch.

![](images/EqualConstraint4.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint5.png )

Now select the line segment, all segments of the poly-line and one of the remaining unconstrained sides of the rectangle

![](images/EqualConstraint6.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint7.png )

Select the line segment and the arc

![](images/EqualConstraint8.png )

and apply **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before. A pop-up message indicates that the constrained items have to be of the same geometrical type (lines of zero curvature or lines of non-zero curvature).

![](images/EqualConstraint9.png )

## Программирование


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/ru
