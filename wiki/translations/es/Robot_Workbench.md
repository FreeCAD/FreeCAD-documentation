# Robot Workbench/es







{{VeryImportantMessage|El Ambiente de trabajo Robot no se mantiene. Si tienes experiencia en el tema y estás interesado en mantenerlo, por favor declara tu intención en la sección de desarrolladores del [https://forum.freecadweb.org/index.php Foro de FreeCAD].

La razón por la que este ambiente de trabajo está todavía en el código fuente maestro es porque este ambiente de trabajo está programado en C++. Si este ambiente de trabajo pudiera ser programado en Python, entonces podría convertirse en un [Ambiente de trabajo externo](external_workbenches/es.md) y podría ser movido a un repositorio separado.
}}

## Introducción

<img alt="El icono del Ambiente de trabajo Robot" src=images/Workbench_Robot.svg  style="width:128px;">

El <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Ambiente de trabajo de robots](Robot_Workbench/es.md) es una herramienta para simular un [Robot de 6 ejes industrial](Robot_6-Axis/es.md) estándar, como [Kuka](http://kuka.com/).

Puede realizar las siguientes tareas:

-   Configurar un entorno de simulación con un robot y piezas de trabajo.
-   Crear y rellenar trayectorias de movimiento.
-   Descomponer las características de una pieza CAD en una trayectoria.
-   Simular el movimiento del robot y la distancia de alcance.
-   Exportar la trayectoria a un archivo de programa de robot.

Para empezar, prueba el [Tutorial de robots](Robot_tutorial/es.md), y mira la interfaz de programación en el archivo de ejemplo [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Herramientas

Aquí están los principales comandos que puedes utilizar para crear la configuración de un robot.

### Robots

Las herramientas para crear y manejar los robots de 6 ejes

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Crea un robot](Robot_CreateRobot/es.md): Inserta un nuevo robot en la escena
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Simula una trayectoria](Robot_Simulate/es.md): Abre el letrero de diálogo de simulación y te permite simular
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Exportar una trayectoria](Robot_Export/es.md): Exporta un archivo del programa del robot
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Establece la posición de inicio](Robot_SetHomePos/es.md): Establece la posición de inicio para un robot
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Restablece la posición de inicio](Robot_RestoreHomePos/es.md): Mueve el robot a su posición de inicio

### Trayectorias

Herramientas para crear y manipular trayectorias. Existen dos tipos, las paramétricas y las no paramétricas.

#### Trayectorias no paramétricas 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:30px;"> [Crea una trayectoria](Robot_CreateTrajectory/es.md): Inserta una nuevo objeto de trayectoria vacía en la escena
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width:30px;"> [Establece la orientación por defecto](Robot_SetDefaultOrientation/es.md): Establece la orientación en los puntos de paso creados por defecto
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width:30px;"> [Establece los parámetros de velocidad por defecto](Robot_SetDefaultValues/es.md): Establece los valores por defecto para la creación de los puntos de paso
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:30px;"> [Inserta un punto de paso](Robot_InsertWaypoint/es.md): Inserta un punto de paso desde la posición actual del robot en una trayectoria
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width:30px;"> [Inserta un punto de paso](Robot_InsertWaypointPre/es.md): Inserta un punto de paso desde las posición actual del ratón en una trayectoria

#### Trayectorias Paramétricas 

-   ![ 30px](images/Robot_Edge2Trac.svg ) [Create a trajectory out of edges](Robot_Edge2Trac/es.md): Inserta un nuevo objeto que descompone los bordes en una trayectoria
-   ![ 30px](images/Robot_TrajectoryDressUp.svg ) [Dress-up a trajectory](Robot_TrajectoryDressUp/es.md): Le permite sobreescribir una o más propiedades de una trayectoria
-   ![ 30px](images/Robot_TrajectoryCompound.svg ) [Trajectory compound](Robot_TrajectoryCompound/es.md): crea un compuesto a partir de algunas trayectorias individuales

## Archivos de guión 

Ver el [Ejemplo de la API del Robot](Robot_API_example/es.md) para ver una descripción de las funciones utilizadas para modelar los desplazamientos del robot.

## Tutorials

-   [Robot de 6 ejes](Robot_6-Axis/es.md)
-   [VRML Preparation for Robot Simulation](VRML_Preparation_for_Robot_Simulation/es.md)





{{Robot Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)
