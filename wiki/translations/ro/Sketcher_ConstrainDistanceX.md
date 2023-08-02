---
- GuiCommand:
   Name: Sketcher ConstrainDistanceX
   Workbenches: Sketcher Workbench
   MenuLocation: Sketch -> Sketcher constraints -> Constrain horizontal distance
   Shortcut: Shift + H
   SeeAlso: Sketcher_ConstrainDistance, Sketcher ConstrainDistanceY
---

# Sketcher ConstrainDistanceX/ro


</div>




<div class="mw-translate-fuzzy">

## Descriere

Fixează distanța orizontală între 2 puncte sau capetele liniei. Dacă este selectat un singur punct, distanța este setată la originea schiței.


</div>

Fixes the horizontal distance between 2 points or line ends. If only one point is selected, the distance is set to the sketch origin.

![](images/Constraint_H_Distance.png )




<div class="mw-translate-fuzzy">

## Folosire

1.  Selectați unul sau două puncte sau o linie.
2.  Apăsați butonul **[<img src=images/Sketcher_ConstrainDistanceX.png style="width:24px"> '''Constrain horizontal distance'''** .
3.  Un dialog contextual deschide pentru a edita sua a confirma valoarea. Apăsați **OK** pentru a valida.


</div>

1.  Pick one or two points or one line.
2.  Invoke the tool several ways:
    -   Press the **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Constrain horizontal distance](Sketcher_ConstrainDistanceX.md)** button in the toolbar.
    -   Use the **L** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> Constrain horizontal distance** from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.


<div class="mw-translate-fuzzy">

**Note:** instrumentul de constrângere poate fi pornit și fără o selecție prealabilă. Pentru a seta distanța de la origine, punctul de origine Sketch trebuie să fie selectat de asemenea. Implicit, comanda va fi în modul continuu pentru a crea noi constrângeri; apăsați butonul drept al mouse-ului sau **ESC** o dată pentru a părăsi comanda.


</div>

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Horizontal span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, ` PointOfEdge1`, ` PointOfEdge2` and `Line`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceX/ro
