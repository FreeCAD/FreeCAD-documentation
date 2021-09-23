# Robot tutorial/it
 {{TutorialInfo/it
|Topic= Robot Workbench
|Level= Base
|Time=
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}


<div class="mw-translate-fuzzy">

Questo tutorial serve per spiegare come usare l\'ambiente [Robot](Robot_Workbench/it.md) per simulare il set-up di una cella robotizzata.


</div>


<div class="mw-translate-fuzzy">

![](images/Robot_Tutorial_RobotSimulation.gif )


</div>

## Premessa

Questo tutorial è scritto per FreeCAD versione 0.16.6703 o superiore. Quindi, se non avete FreeCAD sul computer andate alla pagina [Download](Download/it.md) e installatelo.


<div class="mw-translate-fuzzy">

Questo tutorial è finalizzato all\'uso di [robot industriali](http://en.wikipedia.org/wiki/Industrial_robot) e non di robot mobili o di servizio (vedere [qui](http://en.wikipedia.org/wiki/Robot#Modern_robots)).


</div>


<div class="mw-translate-fuzzy">

## Impostare la scena 

1.  Passare all\'ambiente [Robot](Robot_Workbench/it.md)
2.  Creare un nuovo documento scegliendo ** File ** → ** Nuovo ** dal menu principale
3.  Inserire un robot Kuka IR500 nella scena scegliendo ** Robot ** → ** Inserisci robot ** → ** Kuka IR500 ** dal menu principale
4.  Passare alla vista assonometrica cliccando su <img alt="" src=images/View-axometric.png  style="width:32px;">
5.  Adattare la vista cliccando su <img alt="" src=images/View-zoom-all.png  style="width:32px;">
6.  Salvare il file \...


</div>


<div class="mw-translate-fuzzy">

## Impostare una traiettoria 

1.  Passare all\'ambiente [Robot](Robot_Workbench/it.md)
2.  Attivare la scheda del modello nella vista ad albero facendo clic su di essa
3.  Creare una nuova traiettoria cliccando su <img alt="" src=images/Robot_CreateTrajectory.png  style="width:32px;">
4.  Selezionare il robot nella vista ad albero
5.  Impostare la posizione iniziale del robot cliccando su <img alt="32px" src=images/Robot_SetHomePos.png  style="width:32px;">
6.  Passare al Pannello Azioni
7.  Cambiare la posizione del robot utilizzando i cursori
8.  Quando il robot e la traiettoria sono selezionati in vista ad albero, cliccando su <img alt="" src=images/Robot_InsertWaypoint.png  style="width:32px;"> si inserisce il punto intermedio nella traiettoria
9.  Ogni punto intermedio è indicato con una croce gialla, i punti intermedi sono collegati con linee arancione
10. Definire almeno tre differenti punti intermedi e inserirli nella traiettoria


</div>


<div class="mw-translate-fuzzy">

## Simulare il movimento del robot 

1.  Selezionare il robot e la traiettoria nella vista ad albero
2.  Selezionare la simulazione cliccando su <img alt="" src=images/Robot_Simulate.png  style="width:32px;">
3.  Cliccare sul pulsante Avanti ** I> **
4.  Guardare la simulazione


</div>


{{Tutorials navi

}} {{Robot Tools navi}} 
