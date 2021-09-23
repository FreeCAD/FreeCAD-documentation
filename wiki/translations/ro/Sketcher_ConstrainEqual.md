---
- GuiCommand:
   Name:Sketcher ConstrainEqual
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain equal
   Shortcut:E
   SeeAlso:[Constrain radius](Sketcher_ConstrainRadius.md)
---

# Sketcher ConstrainEqual/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

**Constrângerea de egalitate** forțează două sau mai multe segmente de linie, o poli-linie sau un dreptunghi să aibă o lungime egală. Dacă se aplică la arce sau cercuri, razele sunt constrânse să fie egale. Nu poate fi aplicată primitivelor geometrice care nu sunt de același tip (de exemplu, segmente de linie și arcuri de cerc).


</div>


<div class="mw-translate-fuzzy">

## Utilizare

Schema de exemplu de mai jos conține un număr de primitive de schiță (linie, poli-linie, dreptunghi, arc și cerc).
<img alt="" src=images/EqualConstraint1.png  style="width:256px;">
Selectați două sau mai multe segmente de linie (de exemplu linia și o parte a dreptunghiului).
<img alt="" src=images/EqualConstraint2.png  style="width:256px;">
Click on the Constrain Equal icon <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> în bara de instrumente Sketcher (în Aelierele Sketcher sau Part Design) sau selectați elementul de meniu Constrain Equal din elementul de submeniu al constrângerilor Sketcher din elementul de meniu Sketch or Part Design în funcție de ce Atelier este selectat (Sketcher sau Design Part) aplică constrângerea la elementele selectate.
<img alt="" src=images/EqualConstraint3.png  style="width:256px;">
Acum, selectați arcul de cerc și cercul din schiță.
<img alt="" src=images/EqualConstraint4.png  style="width:256px;">
and apply the Constrain Equal <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> constraint as before.
<img alt="" src=images/EqualConstraint5.png  style="width:256px;">
Now select the line segment, all segments of the poly-line and one of the remaining unconstrained sides of the rectangle
<img alt="" src=images/EqualConstraint6.png  style="width:256px;">
and apply the Constrain Equal <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> constraint as before.
<img alt="" src=images/EqualConstraint7.png  style="width:256px;">
Select the line segment and the arc
<img alt="" src=images/EqualConstraint8.png  style="width:256px;">
and apply the Constrain Equal <img alt="" src=images/Constraint_EqualLength.png  style="width:16px;"> constrângere ca înainte. Un dialog contextula indică faptul că elementele constrânse trebuie să fie de același tip geometric (linii cu curbură nulă sau linii cu curbură non-nulă).
<img alt="" src=images/EqualConstraint9.png  style="width:256px;">


</div>

The example sketch below contains a number of sketch primitives (line, poly-line, rectangle, arc and circle).

![](images/EqualConstraint1.png )

Select two or more line segments (e.g. line and one side of the rectangle).

![](images/EqualConstraint2.png )

Click on **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** in the Sketcher toolbar (in either the Sketcher or Part Design workbenches) or select the Constrain Equal menu item from the Sketcher constraints sub menu item in either the Sketch or Part Design menu item depending upon which workbench is selected (Sketcher or Part Design) to apply the constraint to the selected items.

![](images/EqualConstraint3.png )

Now select the arc and the circle in the sketch.

![](images/EqualConstraint4.png )

and apply **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint5.png )

Now select the line segment, all segments of the poly-line and one of the remaining unconstrained sides of the rectangle

![](images/EqualConstraint6.png )

and apply **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before.

![](images/EqualConstraint7.png )

Select the line segment and the arc

![](images/EqualConstraint8.png )

and apply **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Constrain equal](Sketcher_ConstrainEqual.md)** as before. A pop-up message indicates that the constrained items have to be of the same geometrical type (lines of zero curvature or lines of non-zero curvature).

![](images/EqualConstraint9.png )

## Scripting


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1` and `Edge2` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/ro
