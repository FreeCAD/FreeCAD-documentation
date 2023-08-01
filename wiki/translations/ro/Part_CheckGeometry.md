# Part CheckGeometry/ro
---
- GuiCommand:   Name: Part CheckGeometry‏‎   MenuLocation: Part - Check geometry   Workbenches: [[Part Workbench   Part]]|SeeAlso: ---


</div>

## Description


<div class="mw-translate-fuzzy">

## Introducere

L'outil de vérification de la géométrie vous permet de vérifier si vous avez un solide valide.


</div>



## Utilizare


<div class="mw-translate-fuzzy">

Instrumentul este disponibil în bara de lucru Part din meniul Part sau cu butonul din bara de instrumente Booleene. Selectați o piesă (aveți grijă să selectați întreaga componentă și nu doar o fațetă pentru a verifica dacă există un solid valid), apoi lansați instrumentul. Veți vedea rezultatele în panoul Task.


</div>

Results will be reported in the [Task panel](Task_panel.md). If the check produced errors: click in the report on a specific error message and the corresponding geometric object (edge, face, etc.) will be highlighted in the [3D view](3D_view.md).

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 


<div class="mw-translate-fuzzy">

Dacă doriți să activați verificările extra BOP (BOP = Operații booleene), apoi urmați acești pași: Tools menu \> Edit Parameters \> Preferences \> Mod \> Part \> CheckGeometry apoi, în panoul din dreapta, faceți dublu clic sub valoarea pentru parametrul RunBOPCheck și setați la true, apoi faceți clic pe Save on disk, închideți și reporniți. Vedeți captura de ecran de mai jos.


</div>

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md).

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

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be checked using this tool. For [App Links](App_Link.md) the shape of the linked object is checked. For [App Part](App_Part.md) containers the visible objects within are checked as compounds. <small>(v0.20)</small> 
-   FreeCAD has no methods to automatically repair geometry. If faults are detected the steps involved to create the model need to be examined and fixed manually.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/ro
