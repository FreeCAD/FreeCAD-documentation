# Robot project/es




{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}


<div class="mw-translate-fuzzy">

Este es el articulo de proyecto del proyecto de simulación de Robots. Sigue las reglas de la metodología [\|Getting things done](http://es.wikipedia.org/wiki/Getting_Things_Done). Los proyectos se recopilan en el [mapa de desarrollo](Development_roadmap/es.md).


</div>

## Propósito y principios 

Este proyecto debería ofrecer las principales tecnologías para una simulación de robots realista en FreeCAD. En el primer paso su objetivo es el robot industrial estándar de 6 ejes.

## Resultado

Simulación del robot

![](images/Robot.jpg )

## Tormenta de ideas 


<div class="mw-translate-fuzzy">

### Bibliotecas en este campo 

-   [OROCOS](http://www.orocos.org/) Bibliotecas para cinemática inversa
-   [ROBOOP](http://www.cours.polymtl.ca/roboop/) cuyo objetivo es directamente la simulación de robots, pero parece que no está activo.
-   [Beremiz](http://www.beremiz.org/) un PLC de código libre.


</div>


<div class="mw-translate-fuzzy">

### Estándares de comunicación 

-   [OPC UA](http://en.wikipedia.org/wiki/OPC_Unified_Architecture) para comunicarse con PLCs
-   [RRS-II](http://www.ipk.fraunhofer.de/geschaeftsfelder/automatisierungstechnik/prozessautomatisierung-und-robotik/forschung-und-entwicklung/rrs-realistic-robot-simulation) estándar alemán para la comunicación de simulación de robots


</div>

### Mecanismos de comunicación 


<div class="mw-translate-fuzzy">

-   [D-Bus](http://en.wikipedia.org/wiki/D-Bus)
-   [CORBA](http://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture)


</div>

### Productos comerciales en este campo 

-   [Visual Components](http://www.visualcomponents.com/Solutions/Robot-Simulation)
-   [Delmia](http://www.3ds.com/products/delmia/welcome/)
-   [KUKA Sim](http://www.kuka-robotics.com/germany/en/products/software/kuka_sim/start.htm)


<div class="mw-translate-fuzzy">

### Conocimiento

-   [Kinematic definition](http://prt.fernuni-hagen.de/lehre/KURSE/PRT001/course_main/node15.html)
-   [Roboter VRML modele](http://www.iha.tut.fi/education/IHA-3500/robotlib/)


</div>

## Organización

-   Representación visual de robots de 6 ejes (terminado)
-   Cálculos posteriores y cinemática inversa en robots arbitrarios (terminado)
-   RobotLib, dynamic tipos de robots dinámicos (en progreso)
-   Simulación de trayectoria (en progreso)
    -   Simulación de colisiones
    -   Detección y configuración de cambios y singularidades
    -   Estimación de tiempo
    -   Volumen utilizado (planificado)
-   Post procesador para los robots Kuka (en progreso)
-   Proceso y control de la célula de trabajo (planificado)
-   Fabricación de película de animación (planificado)

## Siguientes acciones 

-   Gestión de la trayectoria y de los puntos de paso.



[Category:Roadmap](Category:Roadmap.md)
