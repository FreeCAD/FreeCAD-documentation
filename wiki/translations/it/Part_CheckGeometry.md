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
    -   Usando {{MenuCommand|Part → <img src="images/Part_CheckGeometry.svg" width=16px> Controlla la gometria}} dal menu principale.


</div>


<div class="mw-translate-fuzzy">

I risultati sono riportati nella [scheda Azioni](Task_panel/it.md).


</div>

**Note:** FreeCAD has no automatic repair methods for solids, so you need to look at the steps involved to model this specific geometry and try to fix the error on your own.

## Options

### Skip settings page {#skip_settings_page}

If ticked, subsequent invocations of the tool skip showing the {{MenuCommand|Settings}} task panel.

### Run BOP check {#run_bop_check}


<div class="mw-translate-fuzzy">

La funzione Controlla geometria verifica se il [Boundary representation](https://en.wikipedia.org/wiki/Boundary_representation) (BRep o [B-rep](Glossary#B.md)) del modello è valido. Oltre a questo controllo BRep, è possibile avere un controllo BOP aggiuntivo BOP (BOP= Boolean OPerations).


</div>

### Log errors {#log_errors}

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">





</div>


 
