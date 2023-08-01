# FEM ConstraintBodyHeatSource/it
---
- GuiCommand:/it   Name:FEM ConstraintBodyHeatSource   Name/it:Vincolo fonte di calore del corpo   Icon:Fem-constraint-heatflux.svg   MenuLocation: Modello → Vincoli termici → Vincolo fonte di calore del corpo   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Definisce un calore generato internamente e ceduto in W/kg (non J/m³). Per maggiori informazioni vedere <https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539> e seguenti e anche Elmer \"Tutorial 1 - Heat equation -- Temperature field of a solid object\" in <https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf>.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">


{{Userdocnavi/it}}


</div>

## Limitation


{{VersionMinus|0.20}}

: The body heat source is applied to the whole model, meaning all bodies of the setup. It is not possible to select an individual body.

## Notes

-   This constraint works only with the Elmer solver.
-   For more information see [this forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) and following posts. [This thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=28926) may also be useful.
-   Elmer examples can also be found in [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).




{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/it
