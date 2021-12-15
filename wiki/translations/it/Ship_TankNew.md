# Ship TankNew/it
---
- GuiCommand:/it   Name:Ship TankNew   Name/it:Nuovo serbatoio   MenuLocation:Weights → Crea un nuovo serbatoio   |Workbenches:[[Ship Workbench/it   Ship]]|Shortcut:   SeeAlso:---


</div>

## Description

Create a new tank instance in a ship instance.

Tank instances are so far similar to **Weight instances** (see [Weights definition](Ship_Weight.md)), i.e. they act as weights that shall be considered for the center of gravity and displacement computation. However, they have small differences in the inputs required to setup a tank instance, as well as in the way its contribution to the ship weight is computed. Along this line tanks can only be created on top of solid/volumetric geometries, and the density is not queried until they are added to a **load condition** (see [Load conditions](Ship_Loading.md)). Afterwards, their contribution to the ship weight and center of gravity will depend on the filling level (to be defined in the **load condition**) and the ship roll and trim angle, as long as the fluid inside reshapes, effectively affecting the gravity center position (the so-called free-surface effect).

## Usage

In order to create a weight, select the tank solid geometry (the interior of the tank that will be eventually filled with fluids) and invoke **Weights → Create a new tank**.

The task panel is shown, where you must select the **Ship instance** (see [Ships creation](Ship_New.md)) in which the tank shall be added.

When the **Accept** button is pressed, a new tank instance is created inside the chosen **Ship instance**.

## Tutorial


<div class="mw-translate-fuzzy">

-   [Tutorial Ship s60, prima parte ](FreeCAD-Ship_s60_tutorial/it.md)
-   [Tutorial Ship s60, seconda parte](FreeCAD-Ship_s60_tutorial_(II)/it.md)


</div>





{{Ship_Tools_navi

}}

---
[documentation index](../README.md) > Ship TankNew/it
