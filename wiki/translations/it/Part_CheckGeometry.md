# Part CheckGeometry/it
---
- GuiCommand:/it   Name:Part CheckGeometry   Name/it:Controlla geometria‏‎   MenuLocation:Part → Controlla geometria   Workbenches:[[Part Workbench/it   Part]]|SeeAlso:---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Lo strumento di controllo della geometria consente di verificare se si dispone di un solido valido


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una parte (attenzione a selezionare l\'intera parte e non solo una faccia per verificare la validità del solido)
2.  Invocare il comando in uno dei seguenti modi:
    -   Con il pulsante **<img src="images/Part_CheckGeometry.svg" width=16px>** della barra delle booleane di Part.
    -   Usando **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Controlla la gometria** dal menu principale.


</div>


<div class="mw-translate-fuzzy">

I risultati sono riportati nella [scheda Azioni](Task_panel/it.md).


</div>

**Note:** FreeCAD has no automatic repair methods for solids, so you need to look at the steps involved to model this specific geometry and try to fix the error on your own.

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 


<div class="mw-translate-fuzzy">

La funzione Controlla geometria verifica se il [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep o [B-rep](Glossary#B.md)) del modello è valido. Oltre a questo controllo BRep, è possibile avere un controllo BOP aggiuntivo BOP (BOP= Boolean OPerations).


</div>

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small> 

## Shape Content 

In addition to detecting potential geometry errors, this tool shows a range of properties regarding the selected object:

-   Checked object
-   Shape type
-   Number of geometric entities: vertices, edges, wires, faces, shells, solids, compsolids, compounds, total shapes
-   Geometric and mass properties:
    -   Area
    -   Volume
    -   Mass
    -   Length
    -   Center of mass
    -   Orientation
    -   Symmetry axis
    -   Symmetry point
    -   Moments
    -   First axis of inertia
    -   Second axis of inertia
    -   Third axis of inertia
    -   Radius of gyration
    -   Global placement


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/it
