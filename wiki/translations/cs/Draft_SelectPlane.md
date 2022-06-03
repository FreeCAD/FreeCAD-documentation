# Draft SelectPlane/cs
---
- GuiCommand   */cs   Name   *Draft SelectPlane   Name/cs   *Kreslení VýběrRoviny   Workbenches   *[Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation   *Kreslení -> Utility -> Výběr roviny---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Modul kreslení má pracovní rovinu, která umožňuje specifikovat uživatelskou rovinu ve 3D, na které se bude realizovat následujíci kreslicí příkaz. Pro definování pracovní roviny existuje několik metod   *

-   Z vybrané plochy
-   Z aktuálního pohledu
-   Z předvolby   * horní, přední nebo boční
-   Žádná, v tomto případě je pracovní rovina automaticky adaptována podle aktuálního pohledu, kde spouštíte příkaz nebo na ploše, pokud začínáte kreslení na existující ploše.


</div>

<img alt="" src=images/WorkingPlane_example.png  style="width   *400px;"> 
*Shapes created on different working planes*

## Usage with pre-selection 

1.  Do one of the following   *
    -   Select a single object. The following objects are supported   *
        -   [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md)   * the **View Data** (the camera position) and the **Visibility Map** (the saved visibility of objects) of the working plane proxy are also restored.
        -   [Arch BuildingParts](Arch_BuildingPart.md).
        -   [Arch SectionPlanes](Arch_SectionPlane.md).
        -   [Std Parts](Std_Part.md)   * to avoid selecting subelements it is advisable to select these in the [Tree view](Tree_view.md).
        -   [Part Feature](Part_Feature.md) objects that have a single face. [Part Planes](Part_Plane.md) for example.
        -   Objects that are not [Part Feature](Part_Feature.md) objects and have a **Placement** property.
    -   Select one or more subelements. You can select   *
        -   A flat face.
        -   Three vertices.
        -   A circular edge.
        -   Two straight edges that are co-planar but not co-linear.
        -   A straight edge and a vertex that does not lie on the (extended) edge.
2.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut   * **W** then **P**.
3.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with post-selection 

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut   * **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following   *
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md) for the supported objects.
    -   Select one or more subelements. You can select   *
        -   A flat face.
        -   Three vertices.
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut   * **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Press any of the buttons to finish the command.
4.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Options


<div class="mw-translate-fuzzy">

## Volby

-   Pro nastavení pracovní roviny na existující plochu   * vyberte existující objekt ve 3D pohledu a potom stiskněte tlačítko **<img src="images/Draft_SelectPlane.png" width=16px> [VýběrRoviny](Draft_SelectPlane/cs.md)
**
-   Stisknutí tlačítka **'''POHLED'''** nastaví pracovní rovinu jako je rovina pohledu, kolmo k osám kamery a procházející počátkem (0,0,0).
-   Stisknutí tlačítka **'''ŽÁDNÁ'''** zruší nastavení aktuální pracovní roviny. Následující 2D operace budou závislé na pohledu.
-   Múžete také specifikovat hodnotu odsunutí, což odsune pracovní rovinu o zadanou vzdálenost od vybrané roviny.


</div>

## Notes

-   It can be useful to align the [3D view](3D_view.md) with the selected Draft working plane. For example after switching the working plane to Front you may want to switch to the [Front view](Std_ViewFront.md) as well.
-   The grid can be toggled with the [Draft ToggleGrid](Draft_ToggleGrid.md) command.
-   By double-clicking [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) in the [Tree view](Tree_view.md) you can quickly switch between working planes.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The grid settings in the task panel as well as several other grid settings are available as preferences   * **Edit → Preferences... → Draft → Grid and snapping → Grid**.
-   To use the grid the **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid** option must be selected. After changing this preference you must restart FreeCAD.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing   * **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování

Objekt pracovní roviny může být snadno vyvořen a manipulován ve skriptech a [makrech](macros/cs.md). Můžete vytvářet vlastní a používat je nezávisle na aktuální pracovní ploše Kreslení.


</div>


<div class="mw-translate-fuzzy">

Můžete také přistupovat na aktuální pracovní rovinu Kreslení   *


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

Příklad   *


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/cs
