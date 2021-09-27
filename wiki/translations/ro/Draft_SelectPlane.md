---
- GuiCommand:/ro
   Name:Draft SelectPlane
   Name/ro:Draft SelectPlane
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   MenuLocation:Draft → Utilities → Select Plane
   Shortcut:**W** **P**
   SeeAlso:[[Draft SetWorkingPlaneProxy]]
---

# Draft SelectPlane/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Modulul Draft dispune de un sistem de plan de lucru, care vă permite să specificați un plan personalizat în spațiul 3D pe care va apărea următoarea comandă Draft. Există mai multe metode pentru a defini planul de lucru:

-   De pe o fațetă selectată
-   De la 3 noduri selectate
-   Din vizualizarea curentă
-   De la o presetare: de sus, frontal sau lateral
-   Nici unul, caz în care planul de lucru este adaptat automat la vizualizarea curentă atunci când porniți o comandă sau la o față dacă începeți să desenați pe o față existentă.


</div>

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Shapes created on different working planes*

## Usage with pre-selection 

1.  Do one of the following:
    -   Select a single object. The following objects are supported:
        -   [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md): the **View Data** (the camera position) and the **Visibility Map** (the saved visibility of objects) of the working plane proxy are also restored.
        -   [Arch BuildingParts](Arch_BuildingPart.md).
        -   [Arch SectionPlanes](Arch_SectionPlane.md).
        -   _.
        -   [Part Feature](Part_Feature.md) objects that have a single face. [Part Planes](Part_Plane.md) for example.
        -   Objects that are not [Part Feature](Part_Feature.md) objects and have a **Placement** property.
    -   Select one or more subelements. You can select:
        -   A flat face.
        -   Three vertices.
        -   A circular edge.
        -   Two straight edges that are co-planar but not co-linear.
        -   A straight edge and a vertex that does not lie on the (extended) edge.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut: **W** then **P**.
3.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with post-selection 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut: **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md) for the supported objects.
    -   Select one or more subelements. You can select:
        -   A flat face.
        -   Three vertices.
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut: **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Press any of the buttons to finish the command.
4.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Options


<div class="mw-translate-fuzzy">

## Opțiuni

-   Pentru a seta planul de lucru la geometria existentă: selectați o fațetă a unui obiect existent în vizualizarea 3D sau {{Version | 0.17}}, cu CTRL apăsat, 3 vârfuri pe orice obiect. Apoi apăsați tasta {{KEY | <img src="images/Draft_SelectPlane.png_" width= 16px> [ SelectPlane](Draft_SelectPlane_.md)}}
-   Apăsarea butonului {{KEY | '''VIEW'''}} va stabili planul de lucru drept planul de vizualizare, perpendicular pe axa camerei și trecând prin punctul de origine (0,0,0).
-   Apăsarea butonului {{KEY | '''AUTO'''}} va decupla orice plan de lucru curent. Următoarele operații 2D vor fi dependente de vizualizare.
-   De asemenea, puteți specifica o valoare de offset, care vă va stabili planul de lucru la o anumită distanță de planul pe care îl selectați.
-   Puteți să ascundeți și să arătați grila cu comanda rapidă {{KEY | '''G'''}} {{KEY |''' R'''}}


</div>

## Notes

-   It can be useful to align the [3D view](3D_view.md) with the selected Draft working plane. For example after switching the working plane to Front you may want to switch to the [Front view](Std_ViewFront.md) as well.
-   The grid can be toggled with the [Draft ToggleGrid](Draft_ToggleGrid.md) command.
-   By double-clicking [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) in the [Tree view](Tree_view.md) you can quickly switch between working planes.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The grid settings in the task panel as well as several other grid settings are available as preferences: **Edit → Preferences... → Draft → Grid and snapping → Grid**.
-   To use the grid the **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid** option must be selected. After changing this preference you must restart FreeCAD.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Scripting


<div class="mw-translate-fuzzy">

## Script

Obiectul plan de lucru poate fi ușor creat și manipulat în scripturi și în [macros](macros.md). Puteți crea propriele dvs. planuri de lucru și le puteți folosi independent de planul curent de lucru curent.


</div>


<div class="mw-translate-fuzzy">

De asemenea, puteți accesa planul curent de lucru al Draft-ului actual:


</div>


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui

workplane = App.DraftWorkingPlane

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()

workplane.alignToPointAndAxis(v1, v2, 17)
Gui.Snapper.toggleGrid()
Gui.Snapper.toggleGrid()
```


<div class="mw-translate-fuzzy">

Exempluː


</div>


```python
import WorkingPlane

my_plane = WorkingPlane.plane()

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()
my_plane.alignToPointAndAxis(v1, v2, 17)

projection = my_plane.projectPoint(App.Vector(10, 15, 2))
print(projection)
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/ro
