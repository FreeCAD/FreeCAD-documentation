# FEM ConstraintFlowVelocity/it
---
- GuiCommand:   Name:FEM_ConstraintFlowVelocity   Name/it:Vincolo velocità del flusso   Icon:Fem-constraint-flow-velocity.svg   MenuLocation: Modello - Vincoli dei fluidi - Vincolo velocità del flusso   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---


</div>



## Descrizione

Applica una velocità del flusso come condizione al contorno a un bordo in 2D o a una faccia in 3D.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Cliccare su <img alt="" src=images/Fem-constraint-flow-velocity.svg  style="width:24px;"> o scegliere **Modello → Vincoli dei fluidi  →  **<img src="images/Fem-constraint-flow-velocity.svg" width=20px> Vincolo velocità del flusso**** dal menu.
2.  Il [pannello delle azioni](task_panel/it.md) visualizzerà i menu per vincolare la velocità del flusso.

    :   ![](images/FEM-constraint-flow-velocity_task-panel.png )
    :   
        
*Sopra: il menu per vincolare la velocità del flusso nella scheda azioni*
        
3.  Selezionare i bordi o le facce di destinazione.
4.  Cliccare su **Aggiungi**
5.  Deselezionare \"non specificato\" per attivare i campi necessari per l\'edizione.
6.  Immettere i valori in mm/s per i componenti cartesiani principali.


</div>

## Formulas


<small>(v0.21)</small> 

It is possible to define a velocity by specifying the velocity profile as formula. In this case the solver sets the velocities at the different positions according to the profile.

To specify for example the velocity profile

$\quad
v_{x} (y)=6\left(y-1\right)\left(2-y\right)$

for $y\in[1;2]$ (assuming that e.g. a pipe has the wall at y = 1 m and y = 2 m)

enter this to the *Formula* field: ` Variable Coordinate 2; Real MATC "6*(tx-1)*(2-tx)"`

This code has the following syntax:

-   the prefix *Variable* specifies that the velocity is not a constant but a variable
-   the variable to calculate the velocity is *Coordinate 2*, meaning y
-   the velocity values are returned as *Real* (floating point value)
-   *MATC* is the prefix for the Elmer solver that the following code is a formula
-   *tx* is always the name of the variable in *MATC* formulas, no matter that *tx* in our case is actually *y*

That *y* will only be in the range $y\in[1;2]$ is set because *MATC* only evaluates the *tx* range where the result is positive. This behavior is a bit special but has the advantage that one does not need to specify the range manually.

It is also possible to use more than one variable. See as example the definition of rotations in the [displacement constraint](FEM_ConstraintDisplacement#Rotations.md).

## Notes


<div class="mw-translate-fuzzy">

## Note

-   I componenti del vettore contrassegnati come \"non specificati\" verranno interpolati dal risolutore selezionato.

    :   Tutti i vettore che dovrebbero essere il risultato del risolutore devono essere contrassegnati come \"non specificato\".
-   Se la faccia o il bordo di destinazione non è allineato con il sistema di coordinate cartesiane principale, è possibile selezionare \"normale al contorno\".

    :   Se \"normale al contorno\" è spuntato, il vettore normale al bordo o alla faccia selezionati è X e sarà orientato lontano dal dominio della mesh.
    :   Ad esempio, se un flusso d\'aria di 20 mm/s deve entrare nel dominio, dopo aver spuntato \"normale al contorno\" l\'utente dovrà inserire -20 mm/s nel campo \"velocità X\".


</div>


<div class="mw-translate-fuzzy">

-   Per una parete con una condizione antiscivolo, il flusso sarà (0,0,0)
-   Per una condizione di simmetria, il flusso sarà (0, Non specificato, Non specificato) se \"normale al contorno\" è selezionato.


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFlowVelocity/it
