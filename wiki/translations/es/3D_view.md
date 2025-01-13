# 3D view/es
## Introducción




La [vista 3D](3D_view/es.md) de FreeCAD es una instancia de una Coin3D [escenografía](Scenegraph/es.md) que forma la ventana más importante de la [interfaz](interface/es.md). Coin3D es una biblioteca que implementa el estándar de descripción de escenas OpenInventor 2.1.


<div class="mw-translate-fuzzy">

Ciertas propiedades de la vista, como el color de fondo, el estilo [navegación con ratón](Mouse_Model/es.md), y los pasos de zoom, pueden ser configurados en el [editor de preferencias](Preferences_Editor/es.md).


</div>

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*La [vista 3D](3D_view/es.md) es un componente de la [interfaz](interface/es.md) de FreeCAD. Por defecto muestra un pequeño widget con ejes de coordenadas, y el cubo de navegación también con ejes de coordenadas; la cuadrícula puede ser visualizada y configurada cargando el [ambiente de trabajo de borrador](Draft_Workbench/es.md).*

## Context menu 

The options in the context menu of the 3D view depend on the selected object(s) and the currently active workbench. To display this menu optionally select one or more objects and then right-click in the 3D view.



## Detalles

FreeCAD uses the Quarter library to use Coin3D in a Qt environment.

It is possible to interact directly with the 3D view scenegraph from the [Python console](Python_console.md) by using the Python library Pivy.

For more information see the power user documentation:

-   [Scenegraph](Scenegraph.md), description of Coin3D.
-   [Pivy](Pivy.md), usage of Coin3D from the Python console.
-   [Third party libraries](Third_Party_Libraries.md) used by FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ documentation.


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > 3D view/es
