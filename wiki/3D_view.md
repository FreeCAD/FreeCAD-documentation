# 3D view
## Introduction

 

The [3D view](3D_view.md) of FreeCAD is an instance of a Coin3D [scenegraph](Scenegraph.md) that forms the most important window in the [interface](interface.md). Coin3D is a library that implements the OpenInventor 2.1 scene description standard.

Certain properties of the view, like background color, [mouse navigation](Mouse_navigation.md) style, and zooming steps, can be configured in the [preferences editor](Preferences_Editor.md).

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*The [Draft Workbench](3D_view]]_is_a_component_of_the_FreeCAD_[[interface]]. By default it shows a small widget with coordinate axes, and the navigation cube also with coordinate axes; the grid can be displayed and configured by loading the [[Draft Workbench.md).*

## Actions

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

## Details

FreeCAD uses the Quarter library to use Coin3D in a Qt environment.

It is possible to interact directly with the 3D view scenegraph from the [Python console](Python_console.md) by using the Python library Pivy.

For more information see the power user documentation:

-   [Scenegraph](Scenegraph.md), description of Coin3D.
-   [Pivy](Pivy.md), usage of Coin3D from the Python console.
-   [Third party libraries](Third_Party_Libraries.md) used by FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ documentation.

 {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > 3D view
