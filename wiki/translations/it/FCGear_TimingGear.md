---
- GuiCommand   */it
   Name   *FCGear_TimingGear
   Name/it   *Ingranaggio di distribuzione
   MenuLocation   *FCGear → Create a Timing gear
   Workbenches   *[FCGear](FCGear_Workbench/it.md)
   Shortcut   *None
   Version   *v0.16
   SeeAlso   *
---

# FCGear TimingGear/it

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Lo scopo degli ingranaggi di distribuzione è quello di consentire all\'albero a camme e all\'albero motore di far ruotare la catena di distribuzione. L\'albero motore gira per muovere i pistoni su e giù all\'interno dei cilindri. L\'albero a camme ruota per consentire l\'apertura e la chiusura delle valvole di aspirazione e di scarico sui cilindri. Questi componenti sono importanti per la corretta sincronizzazione del motore.


</div>

Gli ingranaggi di distribuzione sono collegati a una cinghia o catena di distribuzione.

![](images/Timing-Gear_example.png ) 
*Above   * Timing gear*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width   *22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way   *
    -   Press the <img alt="" src=images/FCGear_TimingGear.svg  style="width   *22px;"> [Create a Timing gear](FCGear_TimingGear.md) button in the tool bar.
    -   Using the **Gear Menu → Timing gear**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Properties

### Data


{{Properties_Title|Base}}

-    **Placement**   * [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**   * User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|computed}}

-    **h**   * Radial height of teeth (not changeable, is calculated automatically).

-    **offset**   * X-Offset of second arc mid-point (not changeable, is calculated automatically).

-    **pitch**   * Pitch of gear (not changeable, is calculated automatically).

-    **r0**   * Radius of first arc (not changeable, is calculated automatically).

-    **r1**   * Radius of second arc (not changeable, is calculated automatically).

-    **rs**   * Radius of third arc (not changeable, is calculated automatically).

-    **u**   * Radial difference between pitch ... diameter and head of gear (not changeable, is calculated automatically).


{{Properties_Title|gear_parameter}}

-    **height**   * Default is 5,00 mm. Value of the gear width.

-    **teeth**   * Default is 20. Number of teeth.

-    **type**   * Default is gt2. Type of timing gear -- profile pitch for timing belts (see also the information in **Notes**).

### View

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Notes

-    **type**   * The pitch of the timing belts (distance from tooth centre to tooth centre of consecutive teeth) is specified in types. GT2 has a pitch of 2 mm, GT3 of 3 mm, GT5 of 5 mm etc..

## Useful formulas 

-    **addendum diameter**= **pitch diameter** + 2 \* **module**

-    **belt length**= 2 \* **axle base** + **belt tooth pitch**    * 2 \* **(teeth 1 + 2)** + **belt tooth pitch²**    * 4 \* pi² \* **axle base** \* **(teeth 1 - 2)²**

-    **axle base**= **belt length**    * 4 - **belt tooth pitch**    * 8 \* **(teeth 1+2)** + ¼ \* sqrt \[**belt length** - ½ \* **belt tooth pitch** \* **(teeth 1+2)²** - 2 \* **belt tooth pitch²** \* **(teeth 1+2)²**    * pi²\]


<div class="mw-translate-fuzzy">





</div>

[Category   *Addons](Category_Addons.md) [Category   *FCGear](Category_FCGear.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear TimingGear/it
