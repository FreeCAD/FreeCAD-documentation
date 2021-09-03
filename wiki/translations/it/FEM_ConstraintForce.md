---
- GuiCommand:/it   Name:FEM_ConstraintForce   Name/it:Vincolo forza   MenuLocation:Modello → Vincoli meccanici → Vincolo forza   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial di FEM](FEM_Module/it___FEM]].md)---


</div>

## Descrizione

Questo comando applica una forza del valore dato \[N\] alla geometria di destinazione selezionata.

## Utilizzo


<div class="mw-translate-fuzzy">

1\) Applicare di una forza in direzione normale a una faccia

-   -   In ambiente FEM, cliccare su <img alt="Vincolo forza" src=images/Fem-constraint-force.svg  style="width:24px;"> o selezionare **Modello** → **Vincoli meccanici** → **Forza** per aprire la finestra di dialogo delle Proprietà del Vincolo forza

![](images/FEMForceConstraintProperties.PNG )

-   -   Se c\'è l\'oggetto Mesh visualizzato, bisogna nasconderlo (selezionare l\'oggetto Mesh e premere **spazio** oppure fare clic con il tasto destro e selezionare **Nascondi**) e mostrare il modello originale.
    -   Cliccare sulla faccia *faccia* a cui deve essere applicata una forza. Essa appare nell\'elenco degli oggetti geometrici.
    -   Compilare il campo **Carico** con un valore di forza in \[N\] (attenzione: *Non* di pressione in \[N/m\])

![](images/ApplyingForceToFace.PNG )

-   -   
        **Direzione**
        
        : In un caso tipico, fare clic su questo campo vuoto per applicare una forza in direzione normale alla faccia. È possibile invertire la direzione della forza selezionando **Inverti direzione**. In altri casi, è necessario selezionare una faccia o un piano, che sia normale alla direzione della forza (può essere diversa dalla faccia a cui viene applicata la forza)

    -   Cliccare su **OK** per chiudere il dialogo e creare un oggetto **<img src=images/FEM_ConstraintForce.png style="width:24px"> Vincolo forza**.


</div>


<div class="mw-translate-fuzzy">

2\) Applicare una forza lungo una linea nella direzione selezionata

-   -   In ambiente FEM, cliccare su <img alt="Vincolo forza" src=images/Fem-constraint-force.svg  style="width:24px;"> o selezionare **Modello** → **Vincoli meccanici** → **Forza** per aprire la finestra di dialogo delle Proprietà del Vincolo forza

    -   Se c\'è l\'oggetto Mesh visualizzato, bisogna nasconderlo (selezionare l\'oggetto Mesh e premere **spazio** oppure fare clic con il tasto destro e selezionare **Nascondi**) e mostrare il modello originale.

    -   Cliccare su un *segmento di linea* a cui deve essere applicata una forza. Essa appare nell\'elenco degli oggetti geometrici.

    -   Compilare il campo **Carico sul bordo** con un valore di forza in \[N\]

    -   
        **Direzione**
        
        : Ora, con il segmento di linea selezionato, è probabile che la forza venga applicata in una direzione sbagliata. Bisogna specificare la direzione facendo clic sul pulsante **Direzione** e poi facendo clic su una faccia che punta con la sua normale verso la direzione della forza (o nella direzione inversa). Di nuovo, si può invertire la direzione della forza facendo clic su **Direzione inversa**.

![](images/FEMforceonline.PNG )

-   -   Cliccare su **OK** per chiudere il dialogo e creare un oggetto **<img src=images/FEM_ConstraintForce.png style="width:24px"> Vincolo forza**.


</div>


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  
