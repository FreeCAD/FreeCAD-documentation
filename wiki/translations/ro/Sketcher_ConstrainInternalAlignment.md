---
- GuiCommand:
   Name:Constraint InternalAlignment
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   MenuLocation:Sketch → Sketcher constraints → Constrain InternalAlignment
   Shortcut:Ctrl + A
   SeeAlso:[Show/Hide Internal Geometry](Sketcher_RestoreInternalAlignmentGeometry.md), [Ellipse](Sketcher_CreateEllipseByCenter.md)
---

# Sketcher ConstrainInternalAlignment/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Această constrângere aliniază liniile și punctele particulare ale unui element complex tip schiță (există doar un element \"complex\"[Ellipse](Sketcher_CreateEllipseByCenter.md)).


</div>


<div class="mw-translate-fuzzy">

Pentru [Ellipse](Sketcher_CreateEllipseByCenter.md) și al său [Arc](Sketcher_CreateArcOfEllipse.md), susține liniile de constrângere pentru a deveni axe majore și minore, și constrângere [points](Sketcher_CreatePoint.md) la poziția focarelor elipsei.


</div>


<div class="mw-translate-fuzzy">

The constraint requires a lot of effort to use in the way other constraints are. It is hidden in the menu, and not exposed on any toolbars by default. There is a helper tool called [Show/Hide Internal Geometry](Sketcher_RestoreInternalAlignmentGeometry.md) which is exposed on workbenches\' toolbars and aimed to completely remove the need to invoke the constraint manually.


</div>

## Operation on Ellipse 


<div class="mw-translate-fuzzy">

## Operații cu Elipse 

1.  Selectați elementele pentru a fi aliniate ți o elipsă.

Elipsa trebuie aleasă ultima dată. Sunt acceptate până la două linii și până la două puncte.

1.  Invocați constrângerea selectând elementul din meniu (Sketch → Sketcher constraints → Constrain InternalAlignment).


</div>

Prima linie selectată va fi aliniată pentru a deveni axa cea mai mare al elipsei (dar dacă nu este ocupată de altă linie, altfel va deveni un diametru minor). A doua linie este aliniată pentru a deveni o semiaxaă minoră. Liniile sunt schimbate automat [construction](Sketcher_ToggleConstruction.md).


<div class="mw-translate-fuzzy">

În mod similar, primul punct este forțat să devină primul focar neocupat, iar al doilea este îndreptat spre celălalt focar. 


</div>

**Note:** By default new ellipses have an internal construction geometry. When this defines the ellipse already completely, you cannot directly use the InternalAlignment constraint. You first need to delete the construction geometry or parts of it. In case you don\'t see the construction geometry, select the ellipse and use the tool **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Show/Hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** to make it visible.

## Scripturi


```python
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseMajorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseMinorDiameter', index_of_line, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseFocus1', index_of_point, 1, index_of_ellipse))
Sketch.addConstraint(Sketcher.Constraint('InternalAlignment:EllipseFocus2', index_of_point, 1, index_of_ellipse))
```


<div class="mw-translate-fuzzy">

Remarks:

:   Sketch is a sketch object.
:   Number 1 in the focus calls stands for starting point of a point element (it is ignored).


</div>

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `index_of_line`, `index_of_point` and `index_of_ellipse` and contains further examples on how to create constraints from Python scripts.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainInternalAlignment/ro
