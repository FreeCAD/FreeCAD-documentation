---
- GuiCommand:/es   Name:Std PerspectiveCamera   Name/es:Std PerspectiveCamera   MenuLocation:[|Workbenches:All   Shortcut:   SeeAlso:[[Std OrthographicCamera/es|Orthographic view](Std_View_Menu/es___View]]_→_Perspective_view‏‎.md)---


</div>


<div class="mw-translate-fuzzy">

## Description

Puts the camera in perspective view mode.
Perspective has depth while Orthographic is a fixed depth . You can zoom in and out. You can judge distances. Cameras can be distanced from the scene.


</div>

The **Std PerspectiveCamera** command switches the camera in the active [3D view](3D_view.md) to perspective view mode. In this mode, objects that are further from the camera appear smaller than those that are closer.

![](images/Std_PerspectiveCamera_example.svg ) *Two cubes with the same dimensions in perspective view*

## Usage

1.  There are several ways to invoke the command:
    -   Select the {{MenuCommand|View → <img src="images/Std_PerspectiveCamera.svg" width=16px> Perspective view}} option from the menu.
    -   Use the keyboard shortcut: **V** then **P**.

## Notes

-   It is also possible to switch to perspective view mode via the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).

## Preferences

-   The camera type can be changed in the preferences: {{MenuCommand|Edit → Preferences... → Display → 3D View → Camera type}}. The selected type will be used for all 3D views of all opened documents and also for new documents. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to perspective use the `setCameraType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Perspective')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}  
