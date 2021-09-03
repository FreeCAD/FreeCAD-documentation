---
- GuiCommand:/de
   Name:FEM ConstraintBodyHeatSource
   Name/de:FEM BeschränkungKörperWärmeQuelle
   Icon:Fem-constraint-heatflux.svg
   MenuLocation: Modell → Thermische Beschränkungen→ Beschränkung Körper Wärme Quelle
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Definiert eine intern erzeugte Körperwärme, angegeben in W/kg (nicht J/m³). Siehe <https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539> und folgende sowie Elmer \"Tutorium 1 - Wärmegleichung - Temperaturfeld eines Festkörpers\" in <https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf> für ausführlichere Informationen.


</div>

## Anwendung

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> [FEM ConstraintBodyHeatSource](FEM_ConstraintBodyHeatSource.md)** button.
    -   Select the {{MenuCommand|Model → Thermal Constraints → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Constraint temperature}} option from the menu.
2.  In the [3D view](3D_view.md) select the objects the constraint should be applied to, which can be a vertices (corners), edges, or faces.
3.  Enter a specific heat value to apply to the objects.

## Notes

-   For more information see [this forum thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) and following posts.
-   Elmer examples can also be found in [Elmer GUI Tutorials](https://www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf).


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  
