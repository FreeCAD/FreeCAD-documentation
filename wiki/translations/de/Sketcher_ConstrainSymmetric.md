---
 GuiCommand:
   Name: Sketcher ConstrainSymmetric
   Name/de: Sketcher SymmetrischFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Symmetrisch festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **S**
   SeeAlso: 
---

# Sketcher ConstrainSymmetric/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Sketcher SymmetrischFestlegen](Sketcher_ConstrainSymmetric/de.md): Legt zwei Punkte symmetrisch zu einer Linie oder Achse bzw. zu einem dritten Punkt fest.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).



### [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> [Constrain symmetric](Sketcher_ConstrainSymmetric.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Constrain symmetric** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Constrain symmetric** option from the context menu.

    -   Use the keyboard shortcut: **S**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two points and a symmetry point (in that order).
    -   Select two points and a symmetry line (idem).
    -   Select a point, a symmetry line and another point (idem).
    -   Select a line and a symmetry point (idem).
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.



### Einmal-Ausführen-Modus 

1.  Do one of the following:
    -   Select two points and a symmetry point (in that order).
    -   Select two points and a symmetry line (in any order).
    -   Select a line and a symmetry point (idem).
2.  Invoke the tool as explained above, or with the following additional option:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainSymmetric.svg" width=16px> Constrain symmetric** option from the context menu.
3.  A constraint is added.



## Hinweise

-   Die Pfeile dieser Randbedingung zeigen die Farbe der maßeichen Randbedingungen.



## Skripten

Zwei Punkte und eine Symmetrielinie:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Zwei Punkte und ein Symmetriepunkt:


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

Eine Linie und ein Symmetriepunkt (In der GUI kann man eine Linie und einen Punkt auswählen, aber es wird intern die gleiche Form wie oben verwendet, mit den beiden Endpunkten der gleichen Linie):


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

Die [Skizzierer Skripten](Sketcher_scripting.md) Seite erklärt die Werte, die für `Linie1`, `Linie2`, `LinieS`, `Linie`, `PunktVonLinie1`, `PunktVonLinie2` und `PunktVonLinieS` verwendet werden können, und enthält weitere Beispiele, wie man Beschränkungen aus Python Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/de
