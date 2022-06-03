# Macro CenterOfMass/hr
<div class="mw-translate-fuzzy">


{{Macro/hr
|Name=Macro CenterOfMass
|Translate=Makro Središte mise
|Description=Centru daje višestruku masu odabranih više objekata.
|Author=schupin
|Version=0.4.1
|Date=2019-05-25
|FCVersion=0.18
|Download=Download the [https   *//forum.freecadweb.org/download/file.php?id=84270 Macro_CenterOfMass_Icon] package and extract it in the same directory of the macro.
}}


</div>

## Opis

Daje ukupnu masu i mjesto središta mase koje proizlazi iz odabranih više objekata. Za svaki objekt mogu se odabrati različite gustoće. {{Codeextralink|https   *//raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/CenterOfMass.FCMacro}}

![](images/CenterOfMass_exemple.png )


<div class="mw-translate-fuzzy">

## Kako koristiti 


</div>

Odaberite objekte

Pokrenite makronaredbu

## Skripta


<div class="mw-translate-fuzzy">

Preuzmite u Github


</div>

[Macro CenterOfMass.FCMacro](https   *//github.com/FreeCAD/FreeCAD-macros/blob/master/Information/CenterOfMass.FCMacro)


<div class="mw-translate-fuzzy">

preuzmite datoteku s ikonom i zalijepite ju u podmapu pod nazivom CenterOfMass u direktoriju makronaredbe


</div>

![](images/Macro_CenterOfMass.png )

## Poveznice

Raspravu na forumu [Macro to compute center of mass](https   *//forum.freecadweb.org/viewtopic.php?f=24&t=31883)

## Verzija

0.5.0 / 2022-04-06   * complete rewrite by s-quirin (SyProLei project (Saarland University))

-   New   * Code base, Requirement raised to Qt5.12+ and Python3 (FreeCAD 0.19).
-   New   * Show mass of each solid.
-   New   * Start window docked or floating (can be set in Parameter Editor).
-   New   * Selection matches up tree view or is sorted by name (can be set in Parameter Editor).
-   New   * Option to save densities in document.
-   Improved   * FreeCAD alike Gui look and feel.
-   Improved   * Scaled color palette (from green to red) to colorify shapes.
-   Improved   * Visualising the displacement of centre of mass to the geometry.
-   Improved   * Internal tracking of units.
-   Fix   * Handling of groups and group objects.
-   Fix   * Handling of App   *   *Link.
-   Fix   * Replaced deprecated Qt class.

0.4.2 / 2019-06-09   *

-   Check last version number on github and popup if not last version.
-   Automatic update of show CdG (if it exists) when densities are changed.
-   Bug correction when changing radius.

0.4.1 / 2019-05-25   * Add default density button, sphere cursor, change window behavior, correct a container part issue.


<div class="mw-translate-fuzzy">

0.2.3 / 2018-11-22    * new icon name


</div>

0.3.5 / 2019-05-21   * Arrays and clone correction.

0.3.4 / 2019-03-18   * Minor.

0.3.3 / 2019-03-17   * Loading .csv corrections.

0.3.2 / 2019-03-14   * Add a colorify push button to add color to shapes depending on their density.

0.3.0 / 2019-03-03   * Python 3 compatibility.


<div class="mw-translate-fuzzy">

0.1.2 / 2018-11-10    * xx


</div>

0.1.2 / 2018-11-10   *



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro CenterOfMass/hr
