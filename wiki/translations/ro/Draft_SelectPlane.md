---
 GuiCommand:
   Name: Draft SelectPlane
   Name/ro: Draft SelectPlane
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   MenuLocation: Draft , Utilities , Select Plane
   Shortcut: **W** **P**
   SeeAlso: Draft SetWorkingPlaneProxy
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


<small>(v1.0)</small> 

: For each 3D view a separate working plane is stored.

The ![](images/Draft_tray_button_plane.png ) button in the [Draft Tray](Draft_Tray.md) changes depending on the current working plane. <small>(v1.0)</small> : If the working plane is not set to **Auto** an asterisk (*****) is appended to the button label if the origin of the working plane does not match the global origin.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Shapes created on different working planes*

## Usage with pre-selection 

1.  Do one of the following:
    -   Select a single object. The following objects are supported:
        -   [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md): the **View Data** (the camera position) and the **Visibility Map** (the saved visibility of objects) of the working plane proxy are also restored.
        -   [Arch Axes](Arch_Axis.md) (<small>(v1.0)</small> )
        -   [Arch AxisSystems](Arch_AxisSystem.md) (<small>(v1.0)</small> )
        -   [Arch BuildingParts](Arch_BuildingPart.md)
        -   [Arch SectionPlanes](Arch_SectionPlane.md)
        -   [Std Parts](Std_Part.md): to avoid selecting subelements it is advisable to select these in the [Tree view](Tree_view.md).
        -   Non-solid objects that consist of a single flat face or a single curved edge, or (<small>(v1.0)</small> ) that have three or more vertices.
        -   Solid objects or objects without a shape that have a **Placement** property. (<small>(v1.0)</small> )
    -   Select one or more subelements. You can select:
        -   A flat face.
        -   A curved edge.
        -   Three vertices.
        -   An edge and a vertex, or two edges. The combined vertices must define a plane. (<small>(v1.0)</small> )
2.  There are several ways to invoke the command:
    -   Press the ![](images/Draft_tray_button_plane.png ) button in the [Draft Tray](Draft_Tray.md).
    -   [Draft](Draft_Workbench.md): Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select plane** option from the menu, or from the [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu.
    -   Draft: Use the keyboard shortcut: **W** then **P**.
3.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with post-selection 

1.  Invoke the command as explained above.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md).
    -   Select one or more subelements. See the [previous paragraph](#Usage_with_pre-selection.md).
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 

1.  Invoke the command as explained above.
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

-   The grid settings in the task panel as well as several other grid settings are available as preferences: **Edit → Preferences... → Draft → Grid and snapping**.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Scripting


<div class="mw-translate-fuzzy">

## Script

Obiectul plan de lucru poate fi ușor creat și manipulat în scripturi și în [macros](macros.md). Puteți crea propriele dvs. planuri de lucru și le puteți folosi independent de planul curent de lucru curent.


</div>


<small>(v1.0)</small> 

The WorkingPlane module offers two classes to create working plane objects: the `PlaneBase` class and the `PlaneGui` class. The second class inherits from the first. Objects of the `PlaneGui` class interact with the GUI (the [Draft Tray](Draft_Tray.md) button), the [3D view](3D_view.md) and the [grid](Draft_Snap_Grid.md). `PlaneBase` objects do not.

Use the `get_working_plane()` method of the WorkingPlane module to get an instance of the `PlaneGui` class linked to the current 3D view. The method either returns the existing working plane linked to the view or creates a new working plane if required.


```python
import FreeCAD as App
import WorkingPlane

wp = WorkingPlane.get_working_plane()

origin = App.Vector(0, 0, 0)
normal = App.Vector(1, 1, 1).normalize()
offset = 17
wp.align_to_point_and_axis(origin, normal, offset)

point = App.Vector(10, 15, 2)
projection = wp.project_point(point)
print(projection)
```

The `PlaneBase` class can be used to create working planes independent of the GUI:


```python
import WorkingPlane

wp = WorkingPlane.PlaneBase()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/ro
