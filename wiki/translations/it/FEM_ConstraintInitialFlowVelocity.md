---
- GuiCommand:/it   Name:FEM_ConstraintInitialFlowVelocity   Name/it:Vincolo velocità iniziale del flusso   Icon:Fem-constraint-initial-flow-velocity.svg   MenuLocation: Modello → Vincoli per fluidi → Vincolo velocità iniziale del flusso   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---

## Descrizione

Crea un vincolo di velocità iniziale del flusso per un\'analisi del flusso del fluido.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/Fem-constraint-initial-flow-velocity.svg  style="width:24px;"> o usare {{MenuCommand|Modello → Vincoli per fluidi  → **<img src="images/Fem-constraint-initial-flow-velocity.svg" width=16px> Vincolo velocità iniziale del flusso**}} dal menu.
2.  Immettere un valore di velocità iniziale del flusso per l\'analisi. Il valore viene inserito come una combinazione dei 3 principali componenti dei vettori cartesiani (X,Y,Z).


</div>

## Limitazioni

-   Il vincolo applica la velocità del flusso iniziale a tutti i nodi nel modello FEA
-   Il vincolo non può essere orientato se non utilizzando le principali componenti cartesiane.

## Note

Nelle analisi più semplici non è necessario specificare la velocità di flusso iniziale, tuttavia è consigliata come buona pratica.





{{FEM Tools navi

}}  
