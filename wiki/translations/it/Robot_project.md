# Robot project/it
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}


<div class="mw-translate-fuzzy">

Questo è l\'articolo di progetto per il progetto Robot. Esso segue le regole della metodologia \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\]. I progetti sono raccolti nel [Piano di sviluppo](Development_roadmap/it.md) (Development roadmap).


</div>

## Finalità e principi 

Questo progetto dovrebbe impostare le tecnologie principali per una simulazione realistica di robot in FreeCAD. Nella prima fase ha come riferimento i robot industriali a 6 assi.

## Risultati

Simulazione di robot

![](images/Robot.jpg )

## Riflessioni


<div class="mw-translate-fuzzy">

### Librerie in questo campo 

-   [OROCOS](http://www.orocos.org/) librerie per la cinematica inversa
-   [ROBOOP](http://www.cours.polymtl.ca/roboop/) mira direttamente alla simulazione di robot, ma sembra inattivo.
-   [Beremiz](http://www.beremiz.org/) un PLC OpenSource.


</div>


<div class="mw-translate-fuzzy">

### Norme per la comunicazione 

-   [OPC UA](http://en.wikipedia.org/wiki/OPC_Unified_Architecture) per comunicare con i PLC
-   [RRS-II](http://www.ipk.fraunhofer.de/geschaeftsfelder/automatisierungstechnik/prozessautomatisierung-und-robotik/forschung-und-entwicklung/rrs-realistic-robot-simulation) standard tedesco per la comunicazione nella simulazione di robot


</div>

### Middleware per la comunicazione 


<div class="mw-translate-fuzzy">

Middleware sono i programmi intermediari

-   [D-Bus](http://en.wikipedia.org/wiki/D-Bus)
-   [CORBA](http://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture)


</div>

### Prodotti commerciali in questo settore 

-   [Visual Components](http://www.visualcomponents.com/Solutions/Robot-Simulation)
-   [Delmia](http://www.3ds.com/products/delmia/welcome/)
-   [KUKA Sim](http://www.kuka-robotics.com/germany/en/products/software/kuka_sim/start.htm)


<div class="mw-translate-fuzzy">

### Conoscenze

-   [Kinematic definition](http://prt.fernuni-hagen.de/lehre/KURSE/PRT001/course_main/node15.html)
-   [Roboter VRML modele](http://www.iha.tut.fi/education/IHA-3500/robotlib/)


</div>

## Organizzazione

-   Rappresentazione visiva di robot a 6 assi (fatto)
-   Calcolo della cinematica in avanti e inversa di robot arbitrari (fatto)
-   RobotLib, dynamic readably robot types (work in progress)
-   Simulazione della traiettoria (in corso)
    -   Simulazione di collisione
    -   rilevamento delle modifiche di configurazione e delle singolarità
    -   Stima del tempo
    -   volume utilizzato (in programma)
-   Post processore per robot Kuka (in corso)
-   Processo e controllo della cella di lavoro (prevista)
-   Creazione di filmati di simulazione (in programma)

## Azioni successive 

-   Gestione della traiettoria e dei punti del percorso.



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Robot](Robot_Workbench.md) > Robot project/it
