---
 GuiCommand:
   Name: Sketcher ConstrainDistance
   Workbenches: Sketcher Workbench
   MenuLocation: Sketch , Sketcher constraints , Constrain distance
   Shortcut: Shift + D
   SeeAlso: Sketcher ConstrainDistanceX, Sketcher ConstrainDistanceY
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

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


<div class="mw-translate-fuzzy">

1.  Selectează două puncte sau o linie sau un punct și o linie.
2.  Apăsați butonul **[<img src=images/Sketcher_ConstrainDistance.png style="width:24px"> '''Constrain distance'''** .
3.  Un dialog se deschide pentru a edita și a confirma valoarea. Apăsați **OK** pentru a valida.


</div>

### Run-once mode 

1.  Do one of the following:
    -   Select a single line.

    -   Select two points.

    -   Select a point and a line (in any order).

    -   Select the edges of two circles or arcs.

    -   Select the edge of a circle or arc and a line (idem).

    -   
        <small>(v1.0)</small> 
        
        : Select the edge of a single arc.
2.  Invoke the tool as explained above.
3.  Optionally [edit the constraint value](Sketcher_Workbench#Edit_constraints.md).
4.  A constraint is added.

## Notes


<div class="mw-translate-fuzzy">

### Aluzie

Dacă este cazul, vă rugăm să luați în considerare utilizarea constrîngerii [Horizontal distance](Sketcher_ConstrainDistanceX.md) sau în loc a constrângerii [Vertical distance](Sketcher_ConstrainDistanceY.md) . Aceste constrângeri sunt mai robuste și mai rapide pentru a calcula decât constrângerea de lungime documentată aici.


</div>

## Scripting

Distance from origin:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, -1, 1, App.Units.Quantity('123.0 mm')))```

Distance between two vertices:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge1, PointOfEdge1, Edge2, PointOfEdge2, App.Units.Quantity('123.0 mm')))```

Length of line (the GUI allows selecting the edge itself, but it is just a shorthand for using the two extremities of the same line):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Line, 1, Line, 2, App.Units.Quantity('123.0 mm')))```

Distance from point (`Edge, PointOfEdge`) to perpendicular point on line (`Line`):


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Edge, PointOfEdge, Line, 0, App.Units.Quantity('123.0 mm')))```

Distance between the edges of two circles:


```pythonSketch.addConstraint(Sketcher.Constraint('Distance', Circle1, 0, Circle2, 0, App.Units.Quantity('123.0 mm')))```

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `Edge`, `Edge1`, `Edge2`, `PointOfEdge`, `PointOfEdge1`, `PointOfEdge2`, `Line`, `Circle1` and `Circle2`, and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDistance/ro
