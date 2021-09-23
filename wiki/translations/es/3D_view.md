# 3D view/es


## Introducción


{{TOCright}}

La [vista 3D](3D_view/es.md) de FreeCAD es una instancia de una Coin3D [escenografía](Scenegraph/es.md) que forma la ventana más importante de la [interfaz](interface/es.md). Coin3D es una biblioteca que implementa el estándar de descripción de escenas OpenInventor 2.1.


<div class="mw-translate-fuzzy">

Ciertas propiedades de la vista, como el color de fondo, el estilo [navegación con ratón](Mouse_Model/es.md), y los pasos de zoom, pueden ser configurados en el [editor de preferencias](Preferences_Editor/es.md).


</div>

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">


*La [vista 3D](3D_view/es.md) es un componente de la [interfaz](interface/es.md) de FreeCAD. Por defecto muestra un pequeño widget con ejes de coordenadas, y el cubo de navegación también con ejes de coordenadas; la cuadrícula puede ser visualizada y configurada cargando el [ambiente de trabajo de borrador](Draft_Workbench/es.md).*

## Acciones


**Note:**

link actions <small>(v0.19)</small> .

Since the [tree view](tree_view.md) lists most objects that are visible in the 3D view, many of the actions are the same to those that can be executed from the [tree view](tree_view.md).

When the default [Start Workbench](Start_Workbench.md) is active, right clicking on the 3D view shows only one command:

-    **[Navigation styles](Mouse_navigation.md)**: different button styles to use with a 3-button mouse or laptop trackpad.

However, once a [Workbench](Workbenches.md) is loaded, there are additional commands:

-    **Link actions**: [Make Link](Std_LinkMake.md).

    -   
        **Make Link group**
        
        : [Simple group](Std_LinkMakeGroup.md), [Group with links](Std_LinkMakeGroup.md), [Group with transform links](Std_LinkMakeGroup.md).

-    **[Fit all](Std_ViewFitAll.md)**: pans and zooms the view to fit all objects in the document on the screen.

-    **[Fit selection](Std_ViewFitSelection.md)**: pans and zooms the view to tightly fit the currently selected object on the screen.

-    **[Draw style](Std_DrawStyle.md)**: as is, flat lines, shaded, wireframe, points, hidden line, no shading.

-    **[Standard views](Std_View_Menu.md)**: [isometric](Std_ViewIsometric.md), [front](Std_ViewFront.md), [top](Std_ViewTop.md), [right](Std_ViewRight.md), [rear](Std_ViewRear.md), [bottom](Std_ViewBottom.md), [left](Std_ViewLeft.md), [rotate left](Std_ViewRotateLeft.md), [rotate right](Std_ViewRotateRight.md).

-    **Measure**: [toggle measurement](View_Measure_Toggle_All.md), [clear measurement](View_Measure_Clear_All.md).

-    **Document window**: [docked](Std_ViewDockUndockFullscreen.md), [undocked](Std_ViewDockUndockFullscreen.md), and [fullscreen](Std_ViewDockUndockFullscreen.md).

Additionally, depending on the workbench and object that is active, other contextual commands may become available.

For example, with the [Part Workbench](Part_Workbench.md) and one object selected:

-    **[Appearance](Std_SetAppearance.md)**: launches the dialog to change color and sizes of lines and vertices, and color of faces.

-    **[Toggle visibility](Std_ToggleVisibility.md)**: makes the object visible or invisible in the 3D view.

-    **[Toggle selectability](Std_ToggleSelectability.md)**: makes the object no longer selectable in the 3D view; use again this command to cancel its effect. It sets the object\'s `Selectable` attribute to `True` or `False`. Change the property by toggling **Selectable** in the [property editor](property_editor.md).

-    **[Go to selection](Std_TreeSelection.md)**: expand the [tree view](tree_view.md) to show the selected object in the hierarchy.

-    **[Random color](Std_RandomColor.md)**: assigns a random color to the object. It sets the object\'s `ShapeColor` attribute to a tuple `(r,g,b)` with tree random floats between 0 and 1. Change the property by modifying **Shape Color** in the [property editor](property_editor.md).

-    **[Delete](Std_Delete.md)**: removes the object from the document, and from the 3D view, by calling the document\'s `removeObject()` method.

Another example, with the [Draft Workbench](Draft_Workbench.md) and one object selected, it shows the same commands as with the [Part Workbench](Part_Workbench.md), but also:

-    **Draft**: object creation and modification commands from the [Draft Workbench](Draft_Workbench.md).

-    **Utilities**: additional contextual commands provided by the [Draft Workbench](Draft_Workbench.md).

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
