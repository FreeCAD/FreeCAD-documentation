---
- GuiCommand:/ro
   Name:Sketcher ConstrainBlock
   Name/ro:Constrângere de blocare
   Workbenches:[Sketcher](Sketcher_Workbench/ro.md)
   MenuLocation:Sketch → Constrângeri desenator → Constrain Block
   SeeAlso:[Constrângere fixă](Sketcher_ConstrainLock/ro.md)
---

# Sketcher ConstrainBlock/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

**Constrain Block** permite blocarea unui element geometric pe loc cu ajutorul unei singure constrângeri. Scopul său principal este de a lucra cu [B-Splines](Sketcher_CreateBSpline.md) ceea ce poate fi dificil de restrâns complet în alt mod.


</div>

It is mainly intended to be used with **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [B-Splines](Sketcher_CreateBSpline.md)**, which can be difficult to fully constrain otherwise.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectează un element de constrângere;
2.  Apăsă butonul **[<img src=images/Sketcher_ConstrainBlock.png style="width:24px"> '''Constrain Block'''** .

**Note:** pașii 1 și 2 pot fi inversați.


</div>

Or press the button first, and then select the elements.

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Block', Edge))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainBlock/ro
