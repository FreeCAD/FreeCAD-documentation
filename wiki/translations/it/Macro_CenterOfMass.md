# Macro CenterOfMass/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro CenterOfMass
|Translate=Centro di massa
|Description=Fornisce il centro di massa degli oggetti selezionati.
|Author=chupins, s-quirin
|Version=0.5.0
|Date=2022-04-06
|FCVersion>=0.19
}}


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Fornisce la massa totale e la posizione del centro di massa risultante da più oggetti selezionati. È possibile scegliere diverse densità per ciascun oggetto.


</div>


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/CenterOfMass.FCMacro}}

<img alt="" src=images/CenterOfMass_exemple.png  style="width:600px;">



## Utilizzo


<div class="mw-translate-fuzzy">

Selezionare gli oggetti


</div>

### Available Options 

-   Color the solids according to density.
-   Display the location of the center of mass.
-   Export and import *masses*, *materials* and *densities* (even if it\'s not a **.csv** file from the macro, but columns must be named accordingly).
-   Save densities in the document (remove them again when setting material to {{ComboBox|default}}).
-   You can change some preferences at **Tools → Edit parameters → Preferences → Macros**.

## Script


<div class="mw-translate-fuzzy">

Scarica la macro da GitHub:


</div>

[Macro CenterOfMass.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Information/CenterOfMass.FCMacro)


<div class="mw-translate-fuzzy">

Scaricare e incollare i file icona in una sottodirectory denominata CenterOfMass nella directory delle macro:


</div>

![](images/Macro_CenterOfMass.svg )

## Link


<div class="mw-translate-fuzzy">

La discussione nel forum [Macro to compute center of mass](https://forum.freecadweb.org/viewtopic.php?f=24&t=31883)


</div>



## Versione

Version / Date of merge

0.8.0 / 2025-01-06: Thanks to farahats9 for the contribution

-   New: Show Volume and Surface area
-   New: Calculate Moments of Inertia
-   Fix: Macro now works with the Assembly example in FreeCAD 1.0
-   Fix: Automatically select material for solids if it is already assigned by the new material system
-   Minor UI changes

0.7.6 / 2024-08-01: Prepare for major FreeCAD release

-   Fix: Make 0.22.0dev AssemblyExample work
-   Fix: BOM Import containing custom material
-   Fix: Support the new material cards
-   Fix: Changed or missing icons, version checks

0.7.3 / 2023-09-11:

-   New: Added buttons for Copy to clipboard
-   New: Scalable Vector Graphics icon
-   Fix: Compatibility for FreeCAD versions and web

0.7.0 / 2023-02-13:

-   New: Searchbar for solids
-   New: Reworked import function to improve external bill of materials (BOM) import with better input tolerance. Caption \"weight\" has to be changed to \"mass\" if you want to import mass from an old file export of the macro.
-   New: Mass can be set zero to exclude solid from calculation and visualization
-   Fix: Behaviour of default value spin and \"Apply to all\"
-   Fix: Preserve original solids color when \"New\" button pressed

0.6.0 / 2022-08-27:

-   New: Masses are editable (a highly requested feature)
-   New: Highlights the solid you are working on
-   New: No duplicate entries when container and content selected concurrently
-   New: Pie charts show density relation in combo box
-   New: Legibility of text on colored combo box with WCAG21 1.4.6 Contrast (Enhanced) conformity
-   Fix: A Part used as a container for meshes (e.g. .stl\'s) is recognized correctly
-   Fix: Fixes for error and language handling, material editing, combo box and GUI size adjustment

0.5.8 / 2022-05-31:

-   Reinserted: Bounding Box
-   New: Setting to color spheres
-   New: Setting to change color maps
-   Rearranged GUI: Update calculation added, Total density added
-   Fix: Message Boxes could not be used when not running FreeCAD on primary screen in a multimonitor setup
-   Fix: More than one Mesh was not calculated correctly

0.5.0 / 2022-04-07: complete rewrite by s-quirin (SyProLei project at Saarland University)

-   New: Code base, Requirement raised to Qt5.12+ and Python3 (FreeCAD 0.19).
-   New: Show mass of each solid.
-   New: Start window docked or floating (can be set in Parameter Editor).
-   New: Selection matches up tree view or is sorted by name (can be set in Parameter Editor).
-   New: Option to save densities in document.
-   Improved: FreeCAD alike Gui look and feel.
-   Improved: Scaled color palette (from green to red) to colorify shapes.
-   Improved: Visualising the displacement of centre of mass to the geometry.
-   Improved: Internal tracking of units.
-   Fix: Handling of groups and group objects.
-   Fix: Handling of App::Link.
-   Fix: Replaced deprecated Qt class.


<div class="mw-translate-fuzzy">

0.4.1 / 2019-05-25: Add default density button, sphere cursor, change window behavior, correct a container part issue.


</div>


<div class="mw-translate-fuzzy">

0.1.2 / 2018-11-10:


</div>



---
⏵ [documentation index](../README.md) > Macro CenterOfMass/it
