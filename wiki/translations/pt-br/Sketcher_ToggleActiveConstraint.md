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

The <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:24px;"> [Sketcher ToggleActiveConstraint](Sketcher_ToggleActiveConstraint.md) tool activates or deactivates selected constraints. Deactivating constraints allows you to test other geometry arrangements without deleting constraints.

This is tool is similar to [Sketcher ToggleDrivingConstraint](Sketcher_ToggleDrivingConstraint.md), but contrary to that tool also works for geometric constraints, and values of deactivated dimensional constraints are preserved.

## Usage

1.  Select one or more constraints.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> [Activate/deactivate constraint](Sketcher_ToggleActiveConstraint.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Activate/deactivate constraint** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ToggleActiveConstraint.svg" width=16px> Activate/deactivate constraint** option from the context menu.

    -   In the **Constraints** section of the [Sketcher Dialog](Sketcher_Dialog.md) select the **Activate** or **Deactivate** option from the context menu. The offered option depends on the state of the constraint under the cursor.

    -   Use the keyboard shortcut: **K** then **Z**.
3.  Active selected constraints are deactivated and turn grey (default [color](Sketcher_Preferences#Appearance.md)), while deactivated selected constraints are activated and return to red (default color).

## Example

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_active.png  style="width:400px;"> 
*A fully constrained sketch.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_1.png  style="width:400px;"> 
*One of the angular constraints has been deactivated, the sketch is no longer fully constrained.*

<img alt="" src=images/Sketcher_ToggleActiveConstraint_example_disabled_2.png  style="width:400px;"> 
*The unconstrained geometry can be moved around. The deactivated constraint is still available, and can be re-activated to return to the fully constrained sketch.*

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
