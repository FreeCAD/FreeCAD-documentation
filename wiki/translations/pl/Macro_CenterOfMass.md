# Macro CenterOfMass/pl
{{Macro
|Name=Macro CenterOfMass
|Description=Compute and show the center of mass for multiple solids.
|Author=Schupins, SyProLei
|Version=0.7.3
|Date=2023-09-07
|FCVersion=0.19 and above
}}

## Description

Gives the total mass and the location of the center of mass of selected objects. Different densities can be chosen for each object.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/CenterOfMass.FCMacro}}

<img alt="" src=images/CenterOfMass_exemple.png  style="width:600px;">

## Usage

1.  Select one or more solids.
2.  Launch the macro.
3.  You\'ll have a window listing the solids. You can specify the density of your material in different unit systems or choose from predefined materials.

### Available Options 

-   Color the solids according to density.
-   Display the location of the center of mass.
-   Export and import *masses*, *materials* and *densities* (even if it\'s not a **.csv** file from the macro, but columns must be named accordingly).
-   Save densities in the document (remove them again when setting material to {{ComboBox|default}}).
-   You can change some preferences at **Tools → Edit parameters → Preferences → Macros**.

## Script

You can download the macro from GitHub: [Macro CenterOfMass.FCMacro](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Information/CenterOfMass.FCMacro)

You can use this icon file as a toolbar icon: ![](images/Macro_CenterOfMass.svg )

## Link

The forum discussion: [Macro to compute center of mass](https://forum.freecad.org/viewtopic.php?f=24&t=31883)

## Version

Version / Date of merge

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

0.4.1 / 2019-05-25: Last update with old requirements and GUI available in official repository

0.1.2 / 2018-11-10: Initial version from chupins merged in official repository



---
⏵ [documentation index](../README.md) > Macro CenterOfMass/pl
