---
 GuiCommand:
   Name: Sketcher ToggleActiveConstraint
   Workbenches: Sketcher_Workbench
   MenuLocation: Sketch , Sketcher constraints , Activate/deactivate constraint
   Shortcut: **K** **Z**
   Version: 0.19
   SeeAlso: Sketcher_ToggleDrivingConstraint
---

# Sketcher ToggleActiveConstraint/pt-br

## Description


**[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [ToggleActiveConstraint](Sketcher_ToggleActiveConstraint.md)**

allows you to activate and deactivate an already placed constraint. This allows you to keep the constraint in the background but temporarily test another arrangement of the existing geometry.

The **[<img src=images/Sketcher_ToggleDrivingConstraint.svg style="width:16px"> [Toggle driving constraint](Sketcher_ToggleDrivingConstraint.md)** tool is similar in that it disables the effect of the constraint; however, with this tool, the constraint does not keep its old value. On the other hand, with **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [ToggleActiveConstraint](Sketcher_ToggleActiveConstraint.md)** you can re-activate the old constraint immediately.

## Usage

1.  Select an already placed constraint, then press **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [ToggleActiveConstraint](Sketcher_ToggleActiveConstraint.md)**.
2.  Alternatively, got to the [task panel](task_panel.md), to the **Constraints** section, select the constraint, then open the context menu (right-click), and select **Deactivate**.
3.  To activate the constraint again, select it, and press **[<img src=images/Sketcher_ToggleActiveConstraint.svg style="width:16px"> [ToggleActiveConstraint](Sketcher_ToggleActiveConstraint.md)** again.

## Examples

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:" height="350px;"> 
*Fully constrained sketch.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:" height="350px;"> <img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:" height="350px;"> 
*Left: deactivated constraint; the sketch is no longer fully constrained. Right: the unconstrained geometry can be moved around; the older constraint is still available, and can be re-activated to return to the fully constrained sketch.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_task_panel.png  style="width:" height="350px;"> 
*Task panel with the deactivated constraint.*

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The active status of a constraint can be controlled in [macros](macros.md) and from the [Python console](Python_console.md). 
```python
SketchObject.toggleActive(index)
```

Use the `toggleActive` method of an existing [Sketcher SketchObject](Sketcher_SketchObject.md), and the `index` of the constraint to activate it or deactivate it. The index starts from `0` all the way to `N-1`, where `N` is the total number of constraints.

Example: 
```python
import FreeCAD as App

sketch = App.ActiveDocument.Sketch
sketch.toggleActive(3)
```





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleActiveConstraint/pt-br
