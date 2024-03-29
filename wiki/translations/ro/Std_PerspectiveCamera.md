# Std PerspectiveCamera/ro
---
 GuiCommand:   Name: Std PerspectiveCamera   MenuLocation: Std View Menu   View , Perspective view‏‎---


</div>




<div class="mw-translate-fuzzy">

## Descriere

Puneți camera în modul vedere perspectivă.
Perspectivă are adâncime pe când modul Ortogonal areadâncime fixă . Puteți mări și micșora imaginile. Puteți judeca distanțele. Camerele pot fi distanțate de scenă.


</div>

The **Std PerspectiveCamera** command switches the camera in the active [3D view](3D_view.md) to perspective view mode. In this mode, objects that are further from the camera appear smaller than those that are closer.

![](images/Std_PerspectiveCamera_example.svg ) 
*Two cubes with the same dimensions in perspective view*




<div class="mw-translate-fuzzy">

## Utilizare

Alegeți ** View** → **<img src="images/View-perspective.svg" width=32px> Perspective view** din meniul de sus/top.


</div>

1.  There are several ways to invoke the command:
    -   Select the **View → <img src="images/Std_PerspectiveCamera.svg" width=16px> Perspective view** option from the menu.
    -   Select the **<img src="images/Std_PerspectiveCamera.svg" width=16px> Perspective view** option from the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).
    -   Use the keyboard shortcut: **V** then **P**.

## Preferences

-   The camera type can be changed in the preferences: **Edit → Preferences... → Display → 3D View → Camera type**. The selected type will be used for all 3D views of all opened documents and also for new documents. See [Preferences Editor](Preferences_Editor#3D_View.md).

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



---
⏵ [documentation index](../README.md) > Std PerspectiveCamera/ro
