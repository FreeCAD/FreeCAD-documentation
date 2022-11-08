# Macro CenterOfMass/it
{{Macro/it
|Name=Macro CenterOfMass
|Translate=Centro di massa
|Description=Fornisce il centro di massa degli oggetti selezionati.
|Author=chupins, s-quirin
|Version=0.5.0
|Date=2022-04-06
|FCVersion>=0.19
}}

## Descrizione

Fornisce la massa totale e la posizione del centro di massa risultante da più oggetti selezionati. È possibile scegliere diverse densità per ciascun oggetto. {{Codeextralink|https   *//raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Information/CenterOfMass.FCMacro}}

![](images/CenterOfMass_exemple.png )

## Utilizzo

Selezionare gli oggetti

Lanciare la macro

## Script

Scarica la macro da GitHub   * [Macro CenterOfMass.FCMacro](https   *//github.com/FreeCAD/FreeCAD-macros/blob/master/Information/CenterOfMass.FCMacro)

Scaricare e incollare i file icona in una sottodirectory denominata CenterOfMass nella directory delle macro   * ![](images/Macro_CenterOfMass.png )

## Link

La discussione nel forum [Macro to compute center of mass](https   *//forum.freecadweb.org/viewtopic.php?f=24&t=31883)

## Versione

0.5.0 / 2022-04-06   * riscrittura completa by s-quirin (SyProLei project (Saarland University))

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

0.3.6 / 2019-05-22   * Radius of spheres representing centers of mass of solids depends on their masses.

0.3.5 / 2019-05-21   * Arrays and clone correction.

0.3.4 / 2019-03-18   * Minor.

0.3.3 / 2019-03-17   * Loading .csv corrections.

0.3.2 / 2019-03-14   * Add a colorify push button to add color to shapes depending on their density.

0.3.0 / 2019-03-03   * Python 3 compatibility.

0.2.3 / 2018-11-22   * New icon name.

0.1.2 / 2018-11-10   *



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro CenterOfMass/it
