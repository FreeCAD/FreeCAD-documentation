


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}


<div class="mw-translate-fuzzy">

Acesta este un proiect de articol despre simularea Robotică. Acesta urmează regulile procesului \[<http://en.wikipedia.org/wiki/Getting_Things_Done#GTD_methodology>\| Getting things done\]. Proiectelșe sunt colectate în [Development roadmap](Development_roadmap.md).


</div>

## Scop și principii 

Acest proiect ar trebui să stabilească principalele tehnologii pentru o simulare realistă a robotului în FreeCAD. În primul pas acesta vizează robotul industrial standard cu 6 axe.

## Rezultat

Simularea Robotului

![](images/Robot.jpg )

## Brainstorming


<div class="mw-translate-fuzzy">

### Biblioteci în domeniu 

-   [OROCOS](http://www.orocos.org/)libs for inverse kinematic
-   [ROBOOP](http://www.cours.polymtl.ca/roboop/) targets directly to robot simulation, but seems inactive.
-   [Beremiz](http://www.beremiz.org/) a OpenSource PLC.


</div>


<div class="mw-translate-fuzzy">

### Standarde de comuncție 

-   [OPC UA](http://en.wikipedia.org/wiki/OPC_Unified_Architecture) to communicate with PLCs
-   [RRS-II](http://www.ipk.fraunhofer.de/geschaeftsfelder/automatisierungstechnik/prozessautomatisierung-und-robotik/forschung-und-entwicklung/rrs-realistic-robot-simulation) German standard for robot simulation communication


</div>

### Middleware pentru comuncație 


<div class="mw-translate-fuzzy">

-   [D-Bus](http://en.wikipedia.org/wiki/D-Bus)
-   [CORBA](http://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture)


</div>

### Produse comercial în acest domeniu 

-   [Visual Components](http://www.visualcomponents.com/Solutions/Robot-Simulation)
-   [Delmia](http://www.3ds.com/products/delmia/welcome/)
-   [KUKA Sim](http://www.kuka-robotics.com/germany/en/products/software/kuka_sim/start.htm)


<div class="mw-translate-fuzzy">

### Cunoaștere

-   [Kinematic definition](http://prt.fernuni-hagen.de/lehre/KURSE/PRT001/course_main/node15.html)
-   [Roboter VRML modele](http://www.iha.tut.fi/education/IHA-3500/robotlib/)


</div>

## Organizare

-   Reprezentarea vizuală a roboților cu 6 axe (realizată)
-   Calculul cinematic direct și invers al roboților arbitrar aleși (făcut)
-   RobotLib, tipuri de robot care pot fi citite dinamic (lucrare în desfășurare)
-   Simularea traiectoriei (lucrări în curs)
    -   simulare de coliziune
    -   detectarea modificărilor de configurație și a singularităților
    -   estimarea timpului
    -   volumul utilizat (planificat)
-   Procesor Post pentru roboți Kuka (lucrări în curs)
-   Procesul și controlul celulelor de lucru (planificate)
-   Film realizarea simulării (planificate)

## Următoarele acțiuni 

-   Managementul traiectoriei și a punctelor de trecere.



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
