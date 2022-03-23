---
- GuiCommand:
   Name:Sketcher ConstrainDistance
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain distance
   Shortcut:Shift + D
   SeeAlso:[Constrain horizontal distance](Sketcher_ConstrainDistanceX.md), [Constrain vertical distance](Sketcher_ConstrainDistanceY.md)
---

# Sketcher ConstrainDistance/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

**Constrain distance** constrânge lungimea unei linii, distanța perpendiculară dintre un punct și o linie sau distanța dintre două puncte pentru a avea o valoare specificată.


</div>

![](images/Sketcher_ConstrainDistance_example.png )


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectează două puncte sau o linie sau un punct și o linie.
2.  Apăsați butonul **[<img src=images/Sketcher_ConstrainDistance.png style="width:24px"> '''Constrain distance'''** .
3.  Un dialog se deschide pentru a edita și a confirma valoarea. Apăsați **OK** pentru a valida.


</div>


<div class="mw-translate-fuzzy">

**Note:** instrumentul de constrângere poate fi pornit și fără o selecție prealabilă. Pentru a seta distanța perpendiculară dintre un punct și o linie, punctul trebuie selectat mai întâi. Implicit, comanda va fi în modul continuu pentru a crea noi constrângeri; apăsați butonul drept al mouse-ului sau **ESC** o dată pentru a părăsi comanda.


</div>

### Hint


<div class="mw-translate-fuzzy">

### Aluzie

Dacă este cazul, vă rugăm să luați în considerare utilizarea constrîngerii [Horizontal distance](Sketcher_ConstrainDistanceX.md) sau în loc a constrângerii [Vertical distance](Sketcher_ConstrainDistanceY.md) . Aceste constrângeri sunt mai robuste și mai rapide pentru a calcula decât constrângerea de lungime documentată aici.


</div>

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('DistanceX', Edge, PointOfEdge, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Length of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distance from point (`Edge, PointOfEdge`) to nearest point on line (`Line`):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge1`, `Edge2`, `Edge`, `PointOfEdge1`, `PointOfEdge2`, `PointOfEdge` and `Line`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/ro
