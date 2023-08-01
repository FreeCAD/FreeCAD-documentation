---
- GuiCommand:
   Name:Sketcher ConstrainDistanceY
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain vertical distance
   Shortcut:Shift+V
   SeeAlso:[Constrain Horizontal Distance](Sketcher_ConstrainDistanceX.md), [Constrain Length](Sketcher_ConstrainDistance.md)
---

# Sketcher ConstrainDistanceY/ro


</div>




<div class="mw-translate-fuzzy">

## Descriere

Fixează distanța verticală între 2 puncte sau capetele liniei. Dacă este selectat un singur punct, distanța este setată la originea schiței.


</div>

Fixes the vertical distance between 2 points or line ends. If only one point is selected, the distance is set to the sketch origin.

![](images/Sketcher_ConstraintDistanceY_example.png )




<div class="mw-translate-fuzzy">

## Utilizare

1.  Selectați unul sau două puncte sau o linie.
2.  Apăsați butonul **[<img src=images/Sketcher_ConstrainDistanceY.png style="width:24px"> '''Constrain vertical distance'''** .
3.  Un dialog contextual se deschide pentru a edita sau a confirma valoarea. Apăsați **OK** pentru a valida.


</div>

1.  Pick one or two points or one line.
2.  Invoke the command several ways:
    -   Press the **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Constrain vertical distance](Sketcher_ConstrainDistanceY.md)** button.
    -   Use the **I** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> Constrain vertical distance** entry from the top menu.
3.  A pop up dialog opens to edit or confirm the value. Press **OK** to validate.


<div class="mw-translate-fuzzy">

**Note:** instrumentul de constrângere poate fi pornit și fără o selecție prealabilă, dar va necesita selecția a două puncte ori a unei linii. Pentru a seta distanța de la origine, punctul de origine Sketch trebuie să fie selectat de asemenea. Implicit, comanda va fi în modul continuu pentru a crea noi constrângeri; apăsați butonul drept al mouse-ului sau **ESC** o dată pentru a părăsi comanda.


</div>

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Vertical span of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceY', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, ` PointOfEdge1`, ` PointOfEdge2` and `Line`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistanceY/ro
