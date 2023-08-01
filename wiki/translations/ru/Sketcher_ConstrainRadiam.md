---
- GuiCommand:
   Name/ru:Ограничить радиус/диаметр автоматически
   Name:Sketcher_ConstrainRadiam
   MenuLocation:Sketch → Ограничения эскиза → Ограничить радиус/диаметр автоматически
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   SeeAlso:[Ограничить расстояние](Sketcher_ConstrainDistance/ru.md), [Ограничение расстояния по горизонтали](Sketcher_ConstrainDistanceX/ru.md), [Ограничение расстояния по вертикали](Sketcher_ConstrainDistanceY/ru.md)
   Version:0.20
---

# Sketcher ConstrainRadiam/ru


</div>

## Описание

This constraint automatically constrains the value of the radius/diameter of a circle or arc to have a specific value. Following rules are applied :

-   If object is a B-spline pole, a weight constrain is added
-   If object is a complete circle, a diameter constrain is added
-   In other cases (typically an arc), a radius constrain is added

If more than one circle or arc is selected before launching the command :

-   If the constrain is applied in \'Reference\' mode, a new reference constrain is added to each object separately according above rules
-   If the constrain is applied in \'Normal\' (driving) mode, following rules are applied
    -   A reference constrain is applied separately on each object which is an external geometry

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Equal constrains](Sketcher_ConstrainEqual.md)**
        
        are applied sequentially between all real/construction geometry objects and a dimensional constrain is applied to the first selected object according above rules

NB : B-spline poles can\'t be mixed with other object type in the selection


<div class="mw-translate-fuzzy">

## Как использовать 


</div>

1.  Pick one or more circles or arcs.
2.  Press the **[<img src=images/Sketcher_ConstrainRadiam.svg style="width:16px"> [Constrain auto radius/diameter](Sketcher_ConstrainRadiam.md)** button.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.
4.  Optionally the dimension label and line can be moved and rotated in the 3D view by clicking on the value and dragging while keeping the left mouse button pressed.

**Note:** the constraint tool can also be started with no prior selection. By default the command will be in continue mode to create new constraints; press the right mouse button or **Esc** once to quit the command.

## Программирование

No specific scripting applies. See the [Sketcher scripting](Sketcher_scripting.md) page that explains the values which can be used for `ArcOrCircle` and `Circle`, and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/ru
