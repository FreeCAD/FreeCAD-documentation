---
- GuiCommand   */it
   Name   *PartDesign InvoluteGear
   Name/it   *DisegnoPezzo IngranaggioEvolvente
   MenuLocation   *DisegnoPezzo → Ingranaggio Evolvente...
   Workbenches   *[DisegnoPezzo](PartDesign_Workbench/it.md)
---

# PartDesign InvoluteGear/it


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Questo strumento consente di creare un profilo 2D dell\'evolvente di un ingranaggio. Questo profilo 2D è completamente parametrico, e può essere estruso con la funzione [DisegnoPezzo Pad](PartDesign_Pad/it.md) di PartDesign.
Per informazioni più dettagliate consultare le voci di Wikipedia per   * [Gear](https   *//en.wikipedia.org/wiki/Gear) e [Involute Gear](https   *//en.wikipedia.org/wiki/Involute_gear)


</div>

For more detailed information see Wikipedia\'s entries for   * [Gear](https   *//en.wikipedia.org/wiki/Gear) and [Involute Gear](https   *//en.wikipedia.org/wiki/Involute_gear)

![](images/PartDesign_Involute_Gear_01.png )

## Usage

### Create the profile 


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Andare nel menu **Part Design → [<img src=images/PartDesign_InternalExternalGear.svg style="width   *24px"> Involute gear...**.
2.  Impostare i parametri dell\'evolvente
3.  Cliccare su **OK**.
4.  L\'evolvente dell\'ingranaggio viene creato al di fuori del corpo attivo. Trascinalo e rilascialo in un corpo per applicarvi ulteriori funzioni, come il riempimento.


</div>

### Create a spur gear 

1.  Select the gear profile in the [Tree view](Tree_view.md).
2.  Press the **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Pad](PartDesign_Pad.md)** button.
3.  Set the pad\'s **Length** to the desired face width of the gear.
4.  Click **OK**

### Create a helical gear 


<small>(v0.19)</small> 

1.  Select the gear profile in the [Tree view](Tree_view.md).
2.  Press the **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [PartDesign AdditiveHelix](PartDesign_AdditiveHelix.md)** button.
3.  Choose as Axis the normal of the gear profile, that is **Normal sketch axis** <small>(v0.20)</small> . (In earlier versions the **Base Z axis** can be used as long as the profile\'s plane has not been altered.)
4.  Choose a **Height-Turns** mode.
5.  Set the **Height** to the desired face width of the gear.
6.  To set the desired helical angle an [Expression](Expressions.md) for the **Turns** is required.
    1.  Click the blue <img alt="" src=images/Bound-expression.svg  style="width   *16px;"> icon at the right of the input field.
    2.  Enter the following formula   * `Height * tan(25°) / (InvoluteGear.NumberOfTeeth * InvoluteGear.Modules * pi)`, where `25°` is an example for the desired helical angle (also known as beta-value) and `InvoluteGear` is the **Name** of the profile.
    3.  Click **OK** to close the formula editor.
7.  Click **OK** to close the task panel.

Hint   * To make the helical angle an accessible parameter, use a *dynamic property*   *

1.  Select the profile.
2.  In the [Property editor](Property_editor.md) activate the **Show all** option in the context menu.
3.  Again in the context menu, select **Add Property**. Note   * this entry is only available when **Show all** is active.
4.  In the **Add Property** dialog   *
    1.  Choose `App   *   *PropertyAngle` as Type.
    2.  Set `Gear` as Group.
    3.  Set `HelicalAngle` as Name (without a space).
    4.  Click **OK**
5.  Now a new property **Helical Angle** (space added automatically), with an initial value of `0.0°`, becomes available.
6.  Assign the desired helical angle to the new property.
7.  In the formula of the **Turns** property of the AdditiveHelix, you can now reference `InvoluteGear.HelicalAngle` instead of the hard coded value of e.g. `25°`; again assuming `InvoluteGear` is the **Name** of the profile.

## Properties


<div class="mw-translate-fuzzy">

-   External gear   * True o false


</div>


<div class="mw-translate-fuzzy">

-   Alta precisione   * True o False


</div>


<div class="mw-translate-fuzzy">

-   Modulo   * Diametro diviso per il numero di denti.


</div>


<div class="mw-translate-fuzzy">

-   Numero di denti   * Impostare il numero di denti.


</div>


<div class="mw-translate-fuzzy">

-   Angolo di pressione   * Angolo acuto tra la retta di pressione e la normale alla congiungente i centri degli ingranaggi. Di default è 20 gradi. ([Altre info](http   *//en.wikipedia.org/wiki/Involute_gear))


</div>

## Limitations

-   It is currently not possible to adjust the tooth thickness. Tooth and tooth space are distributed equally on the pitch circle. Thus the only way to control backlash is to adjust the center distance in a gear paring.
-   There is currently no [undercut](https   *//www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/) in the generated gear profile. That means gears with a low number of teeth can interfere with the teeth of the mating gear. The lower limit depends on the **Pressure Angle** and is around 17 teeth for 20° and 32 for 14.5°. Most practical applications tolerate a missing undercut for gears a little smaller than this theoretical limit though.

## Tutorials

[How to make gears in FreeCAD](https   *//www.youtube.com/watch?v=8VNhTrnFMfE)

## Correlazioni

-   [Ambiente FCGear](FCGear_Workbench/it.md)


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/it
