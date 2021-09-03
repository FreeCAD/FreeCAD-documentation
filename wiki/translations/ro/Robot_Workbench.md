


<div class="mw-translate-fuzzy">


{{docnav|FEM Workbench|Standard Menu}}


</div>


{{VeryImportantMessage|The Robot Workbench is unmaintained. If you have experience with the topic and are interested in maintaining it, please state your intention in the developer's section of the [https://forum.freecadweb.org/index.php FreeCAD forum].

The reason this workbench is still in the master source code is because this workbench is programmed in C++. If this workbench could be programmed in Python, then it could be made an [external workbench](external_workbenches.md) and it could be moved to a separate repository.
}}

## Introducere

<img alt="Robot workbench icon" src=images/Workbench_Robot.svg  style="width:128px;">


<div class="mw-translate-fuzzy">

Atelierul robotică [Robot Workbench](Robot_Workbench.md) este un instrument pentru a simula un robot industrial standard având 6 axe de libertate [6-axis industrial robot](Robot_6-Axis.md), cum ar fi de ex. [Kuka](http://kuka.com/).


</div>

Puteți efectua următoarele activități:

-   Configurați un mediu de simulare cu un robot și piese de lucru;
-   Creați și urmați traiectoriile;
-   Descompuneți caracteristicile/funcționalitățile unei piese CAD într-o traiectorie;
-   Simulați mișcarea și accesibilitatea robotului;
-   Exportați traiectoria într-un fișier de program de robot.


<div class="mw-translate-fuzzy">

Pentru a începe încercați [Robot tutorial](Robot_tutorial.md), și vedeți interfața de programare în fișierul exemplu aici: [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py)


</div>


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Instrumente

Aici sunt comenzile principale pe care le puteți utiliza pentru a seta un robot.

### Roboți

Instrumentele pentru crearea și gestionarea roboților cu 6 axe


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Robot_CreateRobot.png  style="width:30px;"> [Creați un robot](Robot_CreateRobot.md): Introduceți un nou robot în scenă
-   <img alt="" src=images/Robot_Simulate.png  style="width:30px;"> [Simulate a trajectory](Robot_Simulate.md): Deschide dialogul de simulare și vă permite să simulați
-   <img alt="" src=images/Robot_Export.png  style="width:30px;"> [Export a trajectory](Robot_Export.md): Exportați un fișier conținând programul robotului
-   <img alt="" src=images/Robot_SetHomePos.png  style="width:30px;"> [Set home position](Robot_SetHomePos.md): Stabiliți poziția 0 a robotului
-   <img alt="" src=images/Robot_RestoreHomePos.png  style="width:30px;"> [Restore home position](Robot_RestoreHomePos.md): Mutați robotul în poziția zero


</div>

### Traiectorii

Instrumente pentru crearea și manipularea traiectoriilor. Există două tipuri, cele parametrice și cele neparametrice.


<div class="mw-translate-fuzzy">

#### Traiectoriile Non Parametrice {#traiectoriile_non_parametrice}

-   <img alt="" src=images/Robot_CreateTrajectory.png  style="width:30px;"> [Creați o traiectorie](Robot_CreateTrajectory.md): Introduceți o traiectorie goală în scenă
-   <img alt="" src=images/Robot_SetDefaultOrientation.png  style="width:30px;"> [Stabiliți orientarea implicită](Robot_SetDefaultOrientation.md): Definiți orientarea implicită a punctelor de trecere
-   <img alt="" src=images/Robot_SetDefaultValues.png  style="width:30px;"> [/Definiți parametrul implicit al vitezei](Robot_SetDefaultValues.md): Stabiliți valorile implicite pentru crearea punctelor de trecere
-   <img alt="" src=images/Robot_InsertWaypoint.png  style="width:30px;"> [Inserați un punct de trecere](Robot_InsertWaypoint.md): Inserați un punct de trecere de la poziția curentă a robotului într-o traiectorie
-   <img alt="" src=images/Robot_InsertWaypointPre.png  style="width:30px;"> [Inserați un punct de trecere](Robot_InsertWaypointPre.md): Inserați un punct de trecere de la poziția curentă a mouse-ului într-o traiectorie


</div>


<div class="mw-translate-fuzzy">

#### Traiectorii Parametrice {#traiectorii_parametrice}

-   <img alt="" src=images/Robot_Edge2Trac.png  style="width:30px;"> [Generează o traiectorie dintr-un set de muchii](Robot_Edge2Trac.md): Include un obiect nou ale cărui muchii vor forma o traiectorie
-   <img alt="" src=images/Robot_TrajectoryDressUp.png  style="width:30px;"> [Traiectorie suplimentară(Dress-up)](Robot_TrajectoryDressUp.md): Creați o traiectorie suplimentară care va suprascrie anumite proprietăți ale traiectoriei inițiale
-   <img alt="" src=images/Robot_TrajectoryCompound.png  style="width:30px;"> [Gruparea și conectarea traiectoriilor](Robot_TrajectoryCompound.md): Conectează un set de traiectorii și creează o traiectorie mai complexă


</div>

## Script


<div class="mw-translate-fuzzy">

A se vedea [Robot API example](Robot_API_example.md) pentru o descriere a funcțiilor utilizate pentru a modela deplasările robotului .


</div>

## Tutoriale

-   [Robot 6-Axis](Robot_6-Axis.md)
-   [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation.md)


<div class="mw-translate-fuzzy">





</div>


{{Robot Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
