---
- GuiCommand:/it   Name:FEM_MaterialSolid   Name/it:FEM Materiale per solidi   MenuLocation:Modello → Materiale solido   Workbenches:[Shortcut:**M** **M**   SeeAlso:[[FEM_tutorial/it|FEM tutorial](FEM_Module/it___FEM]].md)---


</div>

## Descrizione

Aggiunge le proprietà dei materiali ad una parte.

![](images/FEMMaterialSolidProperties.png ) *The FEM material task panel*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Cliccare su <img alt="" src=images/FEM_MaterialSolid.png  style="width:32px;"> o scegliere **Modello** → **<img src="images/FEM_MaterialSolid.png" width=32px> Materiale solido** dal menu principale.
-   Fare doppio clic sull\'oggetto **<img src="images/FEM_MaterialSolid.png" width=32px> Materiale solido** appena creato

![](images/FEMMaterialSolidProperties.png )

-   -   Selezionare un materiale. Per l\'analisi meccanica di ingegneria, **CalculiX-Steel** è un\'opzione tipica.
    -   A condizione che si stia applicando lo stesso materiale all\'intero oggetto, non selezionare alcuna entità geometrica (lasciare vuota l\'elenco dei riferimenti). Il materiale viene applicato a tutto il modello. In caso contrario, assegnare manualmente il materiale a particolari parti del modello selezionandone alcune per ciascun materiale inserito, ma non lasciare alcuna parte del modello senza materiale assegnato.
    -   È possibile regolare le proprietà del materiale come la densità, il modulo di Young, il rapporto di Poisson, ecc., Tuttavia la maggior parte dei materiali comuni sono già disponibili nei materiali predefini e non necessitano di alcun ritocco.
    -   Se si apportano delle modifiche, è possibile salvare il materiale personalizzato.

-   Cliccare su **Chiudi** per chiudere la finestra di dialogo e creare un oggetto **<img src="images/FEM_MaterialSolid.png" width=32px> Materiale solido
**


</div>

## Note


<div class="mw-translate-fuzzy">

1.  Il materiale utilizza la \*MATERIAL card in CalculiX. I dettagli sul materiale meccanico sono spiegati in <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html>


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  
