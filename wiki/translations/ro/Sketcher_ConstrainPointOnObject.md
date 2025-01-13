---
 GuiCommand:
   Name: Sketcher ConstrainPointOnObject
   Workbenches: Sketcher Workbench
   MenuLocation: Sketch , Sketcher constraints , Constrain point onto object
   Shortcut: Shift+O
   SeeAlso: Sketcher ConstrainCoincident
---

# Sketcher ConstrainPointOnObject/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Aplică un punct pe un alt obiect, cum ar fi o linie, un arc sau o axă de schiță.


</div>


<small>(v1.0)</small> 

: This tool is replaced by the [Sketcher ConstrainCoincidentUnified](Sketcher_ConstrainCoincidentUnified.md) tool if the **Unify Coincident and PointOnObject** option is selected in the [preferences](Sketcher_Preferences#General.md).




<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Selectați punctul pe care doriți să îl aplicați pe o linie/arc/etc. (Odată selectat punctul devine verde).
2.  Selectați linia pe care doriți să o atașați la punctul pe care tocmai l-ați selectat(Odată selecatată linia devine verde).
3.  Apăsați butonul **[<img src=images/Constraint_PointOnObject.png style="width:24px"> '''Constrain point unto object'''**.


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> [Constrain point on object](Sketcher_ConstrainPointOnObject.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainPointOnObject.svg" width=16px> Constrain point on object** option from the menu.
    -   Use the keyboard shortcut: **O**.
3.  The cursor changes to a cross with the tool icon.
4.  Select a single point and a single edge (in any order).
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select a single point and a single edge (in any order).
    -   Select several points and a single edge (idem).
    -   Select a single point and several edges (idem).
2.  Invoke the tool as explained above.
3.  Depending on the selection one or more constraints are added.

## Scripting


<div class="mw-translate-fuzzy">

### Script

Constrângerea poate fi creată din macrocomenzi și din consola Python folosind următoarea comandă:


</div>


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`


<div class="mw-translate-fuzzy">

-   Sketch este un obiect sketch
-   LineMoving este numărul care desemnează linia, care conține punctul care trebuie mutat pe LineFixed (Linia care este fixă)
-   PointOfLineMoving este numărul vârfului liniei LineMoving, care trebuie mutat pe LineFixed
-   LinedFixed este numărul liniei care trebuie aplicată pe punctul PointOfLineMoving


</div>


<div class="mw-translate-fuzzy">

Pentru a identifica numărul care are indică liniile și punctele? Vă rog să vă referinți la parte de script a [Sketcher ConstrainCoincident](Sketcher_ConstrainCoincident.md).


</div>





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/ro
