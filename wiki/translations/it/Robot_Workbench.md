# Robot Workbench/it
**L'ambiente Robot non è mantenuto. Se avete esperienza con l'argomento e se siete interessati a mantenerlo, vi preghiamo di dichiarare la vostra intenzione nella sezione degli sviluppatori del [https   *//forum.freecadweb.org/index.php forum di FreeCAD].

Il motivo per cui questo ambiente è ancora nel codice sorgente principale è perché esso è programmato in C++. Se fosse programmato in Python, allora potrebbe essere creato un [ambiente esterno](external_workbenches/it.md) e potrebbe essere spostato in un repository separato.
**

## Introduzione

<img alt="L\'icona dell\'ambiente Robot" src=images/Workbench_Robot.svg  style="width   *128px;">

L\'[Ambiente Robot](Robot_Workbench/it.md) <img alt="" src=images/Workbench_Robot.svg  style="width   *24px;"> è uno strumento per simulare un [Robot a 6 assi](Robot_6-Axis/it.md) di tipo industriale, come per esempio i robot [Kuka](http   *//kuka.com/).

È possibile eseguire le seguenti operazioni   *

-   Impostare un ambiente di simulazione con un robot e dei pezzi in lavorazione
-   Creare e compilare traiettorie
-   Scomporre le componenti di una Parte CAD in una traiettoria
-   Simulare il movimento del robot e il raggio d\'azione
-   Esportare la traiettoria in un file di programma robot

Per iniziare, provare il [tutorial Robot](Robot_tutorial/it.md) e consultare l\'interfaccia di programmazione nel file di esempio [RobotExample.py](https   *//github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width   *500px;">

## Strumenti

Ecco i principali comandi utilizzabili per creare il set-up di un robot.

### Robot

Gli strumenti per creare e gestire i robot a 6 assi

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width   *30px;"> [Inserisci un robot](Robot_CreateRobot/it.md)   * inserisce un nuovo robot nella scena.
-   <img alt="" src=images/Robot_Simulate.svg  style="width   *30px;"> [Simula una traiettoria](Robot_Simulate/it.md)   * apre la finestra di simulazione e permette di simulare un percorso.
-   <img alt="" src=images/Robot_Export.svg  style="width   *30px;"> [Esporta una traiettoria](Robot_Export/it.md)   * esporta un file di programmazione robotica.
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width   *30px;"> [Imposta la posizione iniziale](Robot_SetHomePos/it.md)   * imposta la posizione iniziale di un robot.
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width   *30px;"> [Sposta alla posizione iniziale](Robot_RestoreHomePos/it.md)   * sposta il robot nella posizione di partenza.

### Traiettorie

Strumenti per creare e modificare i percorsi. Ci sono due tipi di strumenti, quelli parametrici e quelli non parametrici.

#### Traiettorie non parametriche 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width   *30px;"> [Crea una traiettoria](Robot_CreateTrajectory/it.md)   * inserisce un nuovo oggetto traiettoria vuoto nella scena.
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width   *30px;"> [Imposta l\'orientamento predefinito](Robot_SetDefaultOrientation/it.md)   * imposta il modo in cui vengono creati i punti di orientamento di default.
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width   *30px;"> [Imposta i valori di velocità predefiniti](Robot_SetDefaultValues/it.md)   * imposta i valori predefiniti per la velocità.
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width   *30px;"> [Inserisci un punto nella traiettoria](Robot_InsertWaypoint/it.md)   * inserisce il punto della posizione corrente del robot in una traiettoria.
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width   *30px;"> [Inserisci un punto preselezionato nella traiettoria](Robot_InsertWaypointPre/it.md)   * inserisce il punto della posizione corrente del mouse in una traiettoria.

#### Traiettorie parametriche 

-   <img alt="" src=images/Robot_Edge2Trac.svg  style="width   *30px;"> [Crea una traiettoria da un bordo](Robot_Edge2Trac/it.md)   * genera un percorso da un insieme di spigoli.
-   <img alt="" src=images/Robot_TrajectoryDressUp.svg  style="width   *30px;"> [Vesti una traiettoria](Robot_TrajectoryDressUp/it.md)   * permette di modificare una o più proprietà di un percorso.
-   <img alt="" src=images/Robot_TrajectoryCompound.svg  style="width   *30px;"> [Raggruppa le traiettorie](Robot_TrajectoryCompound/it.md)   * raggruppa alcune traiettorie in un unico percorso.

## Script

Vedere l\'esempio [Esempio di API Robot](Robot_API_example/it.md) per una descrizione delle funzioni utilizzate per modellare gli spostamenti del robot.

## Tutorials

-   [6-Axis\_Robot](Robot_6-Axis/it.md)
-   [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation/it.md)





{{Robot Tools navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Robot](Category_Robot.md) > Robot Workbench/it
