# OpenSCAD RefineShapeFeature/it
---
- GuiCommand   */it   Name   *OpenSCAD RefineShapeFeature   Name/it   *Affina forma   MenuLocation   *OpenSCAD → Affina forma   Workbenches   *[[OpenSCAD_Workbench/it   OpenSCAD]]|SeeAlso   *---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Elimina le linee superflue. Dopo un\'operazione booleana alcune linee che definiscono le forme precedenti rimangono visibili, questo strumento crea una copia pulita del del risultato.


</div>

![](images/PartRefineShape_it.png )

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Selezionare la forma da pulire
2.  Avviare lo strumento dal menu **OpenSCAD → Refine Shape Feature**.

-   Viene creato un oggetto figlio e viene nascosto l\'oggetto genitore.


</div>

## Limitations


<div class="mw-translate-fuzzy">

## Limitazioni

-   L\'algoritmo di affinamento funziona solo sui gusci. Quindi itera sui gusci della forma di ingresso e poi per ogni guscio (shell) ne crea uno nuovo con le facce unite, dove è possibile. Questo significa che se la forma di ingresso è solo una faccia, contorno, bordo o vertice l\'algoritmo non fa nulla.
-   Al contrario della funzione [Refine Shape di Part](Part_RefineShape/it.md), questa funzione si aggiorna quando le forme sottostanti vengono modificate


</div>

## Notes


<div class="mw-translate-fuzzy">

## Note

-   La funzione non modifica la forma esistente, ma restituisce una nuova forma.
-   la funzione viene normalmente utilizzata come ultimo passo nella cronologia della modellazione
-   la funzione può aiutare a ottenere raccordi difficile da produrre
-   nella stampa 3D la funzione ha lo scopo di evitare la stampa di bordi indesiderati


</div>


<div class="mw-translate-fuzzy">





</div>


{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD RefineShapeFeature/it
