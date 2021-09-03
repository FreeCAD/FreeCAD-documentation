---
- GuiCommand:   Name:Part CheckGeometry‏‎   MenuLocation:Part → Check geometry   Workbenches:[[Part Workbench   Part]]|SeeAlso:---


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

**Note:** FreeCAD has no automatic repair methods for solids, so you need to look at the steps involved to model this specific geometry and try to fix the error on your own.

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 


<div class="mw-translate-fuzzy">

Dacă doriți să activați verificările extra BOP (BOP = Operații booleene), apoi urmați acești pași: Tools menu \> Edit Parameters \> Preferences \> Mod \> Part \> CheckGeometry apoi, în panoul din dreapta, faceți dublu clic sub valoarea pentru parametrul RunBOPCheck și setați la true, apoi faceți clic pe Save on disk, închideți și reporniți. Vedeți captura de ecran de mai jos.


</div>

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small> 





 
