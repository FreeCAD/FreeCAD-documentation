---
- GuiCommand:
   Name/ru: Переключить ограничения в построительные/основные
   Name: Sketcher_ToggleDrivingConstraint
   MenuLocation: Sketch - Ограничения эскиза - Переключить ограничения в построительные/основные
   Workbenches: [Sketcher](Sketcher_Workbench/ru.md)
   Version: 0.16
   SeeAlso: [Переключить построительную геометрию](Sketcher_ToggleConstruction/ru.md)
---

# Sketcher ToggleDrivingConstraint/ru


</div>



## Описание

The **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Toggle driving constraint](Sketcher_ToggleDrivingConstraint.md)** tool turns dimensional constraints (Lock, Horizontal/Vertical distance, Length, Radius and Angle) into reference mode, and back. The icons in the toolbar turn blue, and rather than dimensional constraints, reference dimensions are created. Reference dimensions do not constrain the sketch. It can be useful to create reference dimensions in a sketch as a way to check on measurements; when given a name, they can also be used to drive constraints in another sketch through [expressions](Expressions.md).

![](images/Sketcher_Constraint_Toolbar_ReferenceMode.png ) 
*The Sketcher Constraint toolbar with the dimensional constraints in reference dimension mode (blue).*

![](images/Sketcher_ToggleConstraint_example.png ) 
*A horizontal distance constraint (50 mm), a vertical constraint (30 mm) and an angle constraint (75°) were set to define the profile; a reference dimension was added on the slanted line segment to know its length (31.0583 mm).*



## Применение

1.  Press the **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Toggle driving constraint](Sketcher_ToggleDrivingConstraint.md)** button. The dimensional constraints icons in the Sketcher Constraints toolbar turn from red to blue.
2.  The usual method of creating dimensional constraints works the same, but a blue reference dimension is added instead.
3.  To turn the Sketcher Constraints toolbar back to constraint mode (red), press the Toggle Constraint button again.
4.  To turn a dimensional constraint into a reference dimension, or the reverse, select it and press the Toggle Constraint button.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/ru
