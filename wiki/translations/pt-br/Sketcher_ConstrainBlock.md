---
- GuiCommand:
   Name:Sketcher ConstrainBlock
   MenuLocation:Sketch - Sketcher constraints - Constrain block
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   Shortcut:**K** **B**
   Version:0.17
   SeeAlso:[Sketcher Constrain Lock](Sketcher_ConstrainLock.md)
---

# Sketcher ConstrainBlock/pt-br

## Description

**Constrain Block** blocks a geometric element in place with a single constraint.

It is mainly intended to be used with **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-splines](Sketcher_CreateBSpline.md)**, which can be difficult to fully constrain otherwise.

## Usage

1.  Select an element to constrain.
2.  Press the **[<img src=images/Sketcher_ConstrainBlock.svg style="width:16px"> [Constrain block](Sketcher_ConstrainBlock.md)** button.

Or press the button first, and then select the elements.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge` and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/pt-br
