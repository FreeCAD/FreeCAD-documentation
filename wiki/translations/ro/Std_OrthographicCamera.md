# Std OrthographicCamera/ro
---
- GuiCommand:   Name:Std OrthographicCamera   MenuLocation:[|Workbenches:All   Shortcut:O   SeeAlso:[[Std PerspectiveCamera|Perspective View](Std_View_Menu___View]]_→_Orthographic_view.md)---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Puneți camera foto în modul de vizualizarea ortogonal.
Ortogonal este (conform Wikipedia):
\... o modalitate de reprezentare a unui obiect tridimensional în două dimensiuni\...


</div>

The **Std OrthographicCamera** command switches the camera in the active [3D view](3D_view.md) to orthographic view mode. In this mode, objects that are further from the camera do not appear smaller than those that are closer.

![](images/Std_OrthographicCamera_example.svg ) *Two cubes with the same dimensions in orthographic view*


<div class="mw-translate-fuzzy">

## Utilizare

Alegeți ** View** → **<img src="images/View-isometric.png" width=24px> Orthographic view** din meniul principal


</div>

1.  There are several ways to invoke the command:
    -   Select the **View → <img src="images/Std_OrthographicCamera.svg" width=16px> Orthographic view** option from the menu.
    -   Use the keyboard shortcut: **V** then **O**.

## Notes

-   It is also possible to switch to orthographic view mode via the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).

## Preferences

-   The camera type can be changed in the preferences: **Edit → Preferences... → Display → 3D View → Camera type**. The selected type will be used for all 3D views of all opened documents and also for new documents. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To change the view to orthographic use the `setCameraType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Orthographic')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std OrthographicCamera/ro
