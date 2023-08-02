---
- GuiCommand:
   Name: Sketcher ConstrainParallel
   Workbenches: Sketcher Workbench
   MenuLocation: Sketch -> Sketcher constraints -> Constrain parallel
   Shortcut: Shift + P
   SeeAlso: Sketcher ConstrainVertical, Sketcher ConstrainHorizontal
---

# Sketcher ConstrainParallel/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Constrângerea paralelă forțează două linii drepte sau margini selectate pentru a fi paralele una cu cealaltă.


</div>

## Operation


<div class="mw-translate-fuzzy">

## Utilizare

Schița conține două linii orientate aleatoriu.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel1.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">

Selectați ambele linii făcând clic succesiv pe fiecare dintre ele.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel2.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">

Aplicați constrângerea Paraleleă selectând iconița Constrain Parallel <img alt="" src=images/Constraint_Parallel.png  style="width:16px;"> din bara de instrumente, pe traseul Sketch → Contraintes d\'esquisse → Contrainte Parallèle de la barre d\'outils sau selectând opțiunea din meniul Contrainte Parallèle (sau Part Design, în funcție de instrumentul care este selecționat).


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/ConstrainParallel3.png  style="width:256px;">


</div>


<div class="mw-translate-fuzzy">

Liniile selectate sunt forțate să fie paralele unele cu altele. Schimbarea orientării unei linii va schimba orientarea celeilalte pentru a fi aceeași.


</div>

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Line1` and `Line2` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/ro
