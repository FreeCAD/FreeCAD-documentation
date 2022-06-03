# Sketcher ConstrainParallel/cs
---
- GuiCommand   */cs   Name   *Constraint Parallel   Name/cs   *Constraint Parallel   Workbenches   *[PartDesign](Sketcher_Workbench/cs___Sketcher]],_[[PartDesign_Workbench/cs.md)|MenuLocation   *Sketch → Sketcher constraints → Constrain parallel   SeeAlso   *[Constraint Vertical](Sketcher_ConstrainVertical/cs.md), [Constraint Horizontal](Sketcher_ConstrainHorizontal/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

#### Popis

Vazba rovnoběžnosti zajistí, že dvě vybrané přímky nebo hrany jsou vzájemně rovnoběžné.


</div>

## Operation


<div class="mw-translate-fuzzy">

#### Postup

Náčrt obsahuje dvě náhodně orientované přímky.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel1.png  style="width   *256px;">


</div>


<div class="mw-translate-fuzzy">

Postupným kliknutím vyberte obě přímky.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel2.png  style="width   *256px;">


</div>


<div class="mw-translate-fuzzy">

Aplikujte vazbu rovnoběžnosti výběrem její ikony <img alt="" src=images/Constraint_Parallel.png  style="width   *16px;"> z pruhu nástrojů vazeb Náčrtu nebo výběrem položky Vazba rovnoběžnosti ze submenu vazeb náčrtu v Náčrtu (pracovní plocha Náčrt) nebo Návrh dílu (pracovní plocha Návrh Dílu).


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel3.png  style="width   *256px;">


</div>


<div class="mw-translate-fuzzy">

Vybrané přímky jsou upraveny tak, že jsou vzájemně rovnoběžné. Změna orientace jedné z nich změní stejně i orientaci druhé.


</div>

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1` and `Line2` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/cs
