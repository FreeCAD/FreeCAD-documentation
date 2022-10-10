# FEM ConstraintFlowVelocity/it
---
- GuiCommand   */it   Name   *FEM_ConstraintFlowVelocity   Name/it   *Vincolo velocità del flusso   Icon   *Fem-constraint-flow-velocity.svg   MenuLocation   * Modello → Vincoli dei fluidi → Vincolo velocità del flusso   |Workbenches   *[Shortcut   *   SeeAlso   *[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---

## Descrizione

Applica una velocità del flusso come condizione al contorno a un bordo in 2D o a una faccia in 3D.

<img alt="" src=images/FEM-constraint-flow-velocity_task-panel.png  style="width   *400px;"> 
*Constraint flow velocity menus within the [task panel](Task_panel.md)*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/Fem-constraint-flow-velocity.svg  style="width   *24px;"> o scegliere **Modello → Vincoli dei fluidi  →  **<img src="images/Fem-constraint-flow-velocity.svg" width=20px> Vincolo velocità del flusso**** dal menu.
2.  Il [pannello delle azioni](task_panel/it.md) visualizzerà i menu per vincolare la velocità del flusso.

       *   ![](images/FEM-constraint-flow-velocity_task-panel.png )
       *   
        
*Sopra   * il menu per vincolare la velocità del flusso nella scheda azioni*
        
3.  Selezionare i bordi o le facce di destinazione.
4.  Cliccare su **Aggiungi**
5.  Deselezionare \"non specificato\" per attivare i campi necessari per l\'edizione.
6.  Immettere i valori in mm/s per i componenti cartesiani principali.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Note

-   I componenti del vettore contrassegnati come \"non specificati\" verranno interpolati dal risolutore selezionato.

       *   Tutti i vettore che dovrebbero essere il risultato del risolutore devono essere contrassegnati come \"non specificato\".
-   Se la faccia o il bordo di destinazione non è allineato con il sistema di coordinate cartesiane principale, è possibile selezionare \"normale al contorno\".

       *   Se \"normale al contorno\" è spuntato, il vettore normale al bordo o alla faccia selezionati è X e sarà orientato lontano dal dominio della mesh.
       *   Ad esempio, se un flusso d\'aria di 20 mm/s deve entrare nel dominio, dopo aver spuntato \"normale al contorno\" l\'utente dovrà inserire -20 mm/s nel campo \"velocità X\".


</div>

-   Per una parete con una condizione antiscivolo, il flusso sarà (0,0,0)
-   Per una condizione di simmetria, il flusso sarà (0, Non specificato, Non specificato) se \"normale al contorno\" è selezionato.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity/it
