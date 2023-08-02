---
- GuiCommand:
   Name: Sketcher ConstrainLock
   Name/ro: Constrângere fixă
   Workbenches: Sketcher Workbench/ro
   MenuLocation: Sketch -> Constrângeri desenator -> Constrângere fixă
   SeeAlso: Sketcher ConstrainBlock/ro
---

# Sketcher ConstrainLock/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

**Constraint Lock** aplică <img alt="" src=images/Constraint_HorizontalDistance.png  style="width:24px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md) și <img alt="" src=images/Constraint_VerticalDistance.png  style="width:24px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md) constrângeri pentru a selecta vârfuri(puncte) în schiță. Dacă este selectat un singur vertex, constrângerile orizontale și verticale ale distanței se vor referi la punctul de origine a schiței. Dacă sunt selectate două sau mai multe puncte, se va adăuga o distanță orizontală și verticală fiecărei perechi de puncte. Nu există nici un prompt automat pentru a edita valorile constrângerilor, acestea trebuie editate manual.


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați unul sau mai multe vârfuri(puncte) în schiță.
2.  Apăsați butonul**[<img src=images/Sketcher_ConstrainLock.png style="width:24px"> '''Constrain Lock'''** .
3.  Pentru a editavaloarea constrângerilor, dublu-click pe valoarea constrângerii într-o vizualizare 3D , sau dublu click pe constrângere sau click drapta și selectați **Edit value** în liset Constrângerilor din tab-ul Tasks.


</div>

**Notă:** instrumentul de constrângere poate fi pornit și fără o selecție prealabilă, dar va lucra doar cu un singur vârf și referința de constrângeri la punctul de origine al schiței. Implicit, comanda va fi în modul continuu pentru a crea noi constrângeri; apăsați o dată butonul drept al mouse-ului sau **ESC** pentru a părăsi comanda.

## Scripting

The <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Lock](Sketcher_ConstrainLock.md) constraint is a GUI command which creates a <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md) and a <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md) constraint, it is not a constraint of its own. See the [Sketcher scripting](Sketcher_scripting.md) page for details and examples on how to create these constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/ro
