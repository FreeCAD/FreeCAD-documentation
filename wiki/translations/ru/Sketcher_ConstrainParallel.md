---
- GuiCommand:/ru
   Name:Sketcher Constraint Parallel
   Name/ru:Ограничение параллельности
   MenuLocation:Sketch → Ограничения эскиза → Ограничение параллельности
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   SeeAlso:[Ограничение вертикальности](Sketcher_ConstrainVertical/ru.md), [Ограничение горизонтальности](Sketcher_ConstrainHorizontal/ru.md)
---

## Описание

The Constrain Parallel constraint forces two selected straight lines or edges to be parallel to each other.

## Operation

The sketch contains two randomly oriented lines.

<img alt="" src=images/ConstrainParallel1.png  style="width:500px;">


*Select both lines by clicking successively on each of them.*

<img alt="" src=images/ConstrainParallel2.png  style="width:500px;">

Apply the Constrain Parallel constraint by either:

-   Pressing the **<img src=images/Sketcher_ConstrainParallel.svg style="width:16px"> [Constrain parallel](Sketcher_ConstrainParallel.md)** button from the Sketcher constraints toolbar by selecting the Constraint Parallel menu item from the Sketcher constraints sub menu of the Sketcher (Sketcher workbench selected) or Part Design (Part Design workbench selected) menu item.
-   Use the **Shift** + **P** keyboard shortcut.
-   Use the {{MenuCommand|Sketch → Sketcher constraints → Constrain parallel}} entry from the top menu.

<img alt="" src=images/ConstrainParallel3.png  style="width:500px;">


*Result: The selected lines are forced to be parallel to each other. Changing the orientation of one line will change the orientation of the other to be the same.*

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1` and `Line2` and contains further examples on how to create constraints from Python scripts.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}  
