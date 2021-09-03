


{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{VeryImportantMessage|(2020) This page refers to an attempt to update the [Raytracing Workbench](Raytracing_Workbench.md), proposed around 2012. Its original author never completed the implementation so this information is outdated, and should not be considered current.

New development is happening in the [https://github.com/FreeCAD/FreeCAD-render Render Workbench], a complete Python replacement for the [Raytracing Workbench](Raytracing_Workbench.md).
}}


{{TOCright}}

Este es el proyecto de desarrollo de la implementación de un módulo de Raytracing en FreeCAD. Sigue las reglas de la metodología [Getting things done](https://en.wikipedia.org/wiki/Getting_Things_Done). Los proyectos se recogen en el [Mapa de desarrollo](Development_roadmap/es.md).


<div class="mw-translate-fuzzy">

## Propósito y principios 

Este proyecto pretende actualizar el \[Raytracing\_Module/es\|módulo de renderizado\] que actualmente utiliza Povray, un renderizador parcial que proporciona unos resultados satisfactorios y permitir utilizar renderizadores más modernos como Lux Render, Yafaray o Indigo.


</div>

También proporcionar un interfaz genérico que permita utilizar múltiples back-ends de renderizado con FreeCad. Proporcionando un interfaz de programación más genérico se permitirá crear módulos de renderizado de forma más sencilla.

El interfaz permitirá tanto rederizadores en código libre como renderizadores propietarios externos que se puedan utilizar para crear un archivo de escena compatible y lanzar un proceso separado en modo oculto. El resultado se podrá previsualizar dentro de Freecad directamente abriendo el archivo temporal de salida (si está disponible).

Cada renderizador será un plugin dentro de un interfaz genérico y proporcionará materiales y modos de renderizado compatibles.

## Resultado

Excelentes visualizaciones!!! Producir resultados de alta calidad de piezas con archivos de Freecad y proporcionar una interfaz muy simple con parámetros por defecto para permitir ráoidas instalaciones para el renderizado y la previsualización.

La interfaz de usuario debería permitir situaciones más complejas y posiblemente previsualizar sus cambios tales como el modificar los parámetros de iluminación, luces y sus posiciones. Sin embargo, la intención no es proporcionar una suite de renderizado repleta de características.

## Tormenta de ideas 

\'Debe\' crearse una biblioteca de materiales para cada plugin de renderizado con parámetros por defecto. Las propiedades de los materiales se podrán cambiar. Los parámetros por defecto de la escena deberían permitir a los usuarios con poca experiencia con los renderizadores producir buenas visualizaciones en poco tiempo.

## Organización

La interfaz genérica se está creando actualmente y para comprobar la integración [Lux render](http://www.luxrender.net/en_GB/index), un renderizador imparcial será implementado en primer lugar. El trabajo actualmente está realizado por completo por mrlukeparry en su ramal de renderizaqdo [Github Render Branch](https://github.com/mrlukeparry/FreeCAD_sf_master/tree/raytracing).

**Actualmente es posible renderizar objetos con Lux Render:**

![](images/LuxRenderOutput.png )

Se muestra una pieza creada utilizando Diseño de Piezas / Croquizador y luego renderizada utilizando el nuevo módulo de renderizado siendo desarrollado en Lux Render. Lux Render permite excelentes efectos como DOF que pueden crearse para incrementar el realismo.

## Siguientes acciones 

-   Crear la Abstracción para proporcionar la interfaz entre renderizaadores **(Terminado)**

-   Implementar una interfaz para la descripción genérica de los materiales y las colecciones de los mismos **(Terminado)**

-   Implementar una interfaz para describir los parámetros de configuración del renderizado **(Terminado)**

-   Implementar una interfaz para la descripción de plantillas **(Terminado)**

-   Implementar una característica para almacenar toda esta información de forma permanente **(En proceso)**

-   Crear un módulo de entorno para mostrar los resultados del renderizado **(Terminado)**

-   Crear herramientas de entorno para cambiar las propiedades del renderizado **(Terminado)**

-   Crear herramientas de entorno para navegar, cambiar y aplicar materiales a las características de las piezas **(Terminado)**

-   Crear archivos de guión de automake **(En proceso)**

-   Eliminar cualquier dependencia de la interfaz gráfica de usuario de Raytracing/App **(Terminado)**

¬ La estructura de datos Bounding Box no debería utilizar coin3d SbBox3f **(Terminado)**

¬ QWidget incluido en QProcess por alguna razón? **(Solucionado)**

-   Comprobar la compatibilidad con Windows **(En proceso)**

¬ Actualizar Libpack para incluir QT 4.7 - QT 4.8

¬ Eliminar errores y advertencias del compilador

-   Implementar el guardado de propiedades de materiales **(Terminado)**

-   Ordenar la interfaz de QML **(En proceso)**

-   Creación de plantillas de renderizado / materiales de Renderizado / configuraciones predeterminadas de Renderizado

-   Crear una platilla de conversión de escena de Blender a Lux

-   Convertir los materiales de LuxBlender .lbm (http://www.luxrender.net/lrmdb/en/material/) a materiales de renderizado útiles

-   Crear vínculos de Python para materiales de renderizado, cámaras, luces

-   Crear un objeto de documento RenderCamera

-   Permitir que las plantillas de escenas se importen en la operación de renderizado.

-   Directorios definidos por el usuario de configuraciones predeterminadas / materiales / plantillas

-   Mejorar el proveedor del visor

-   Convertir Povray/Yafaray para utilizar la nueva infraestructura de renderizado

-   Hacer pruebas



[Category:Roadmap{{\#translation:}}](Category:Roadmap.md)
