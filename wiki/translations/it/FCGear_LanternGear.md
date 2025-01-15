---
 GuiCommand:
   Name: FCGear_LanternGear
   Name/it: Ingranaggio a lanterna
   MenuLocation: FCGear , Create a Lantern gear
   Workbenches: FCGear Workbench/it
   Shortcut: None
   Version: v0.16
   SeeAlso: 
---

# FCGear LanternGear/it


</div>

## Descrizione

La dentatura dell\'ingranaggio a lanterna è una forma speciale di dentatura cicloidale in cui il cerchio di rotolamento e il cerchio primitivo hanno la stessa dimensione. Inoltre, in un cambio i denti della ruota più grande sono sostituiti da cilindri. La piccola ruota è dotata di un ingranaggio cicloide. Ciò si traduce in un ingranaggio unilaterale. Gli ingranaggi delle lanterne possono essere solo dentati diritti.

Poiché la loro costruzione è molto semplice, sono tra le più antiche forme di ingranaggi. Gli ingranaggi delle lanterne vengono utilizzati quando sono richiesti rapporti di trasmissione elevati, ad esempio negli ingranaggi dei mulini o gru per la movimentazione del legname.

L\'ingranaggio a lanterna combinato con una catena a rulli rappresenta un\'alternativa economica e robusta alle trasmissioni a pignone e cremagliera. Muovendo la catena tesa tangenzialmente lungo la ruota dentata, il movimento lineare della catena viene convertito in un movimento rotatorio della ruota. Viceversa, il movimento lineare della catena può essere ottenuto anche dal moto rotatorio della ruota dentata (moto o bicicletta).

![](images/Lantern-Gear_example.png ) 
*Above: Lantern gear*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_LanternGear.svg style="width:16px"> [Lantern Gear](FCGear_LanternGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_LanternGear.svg style="width:16px"> Lantern Gear** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

### Data

An FCGear LanternGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**: Default is {{Value|10}}. The value normally does not need to be changed.


{{Properties_Title|base}}

-    **bolt_radius|Length**: Default is {{Value|1 mm}}. Diameter of the cylinder on the rotating disc which functions as a second \"gear wheel\".

-    **height|Length**: Default is {{Value|5 mm}}. Value of the gear width.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).


{{Properties_Title|gear_parameter}}

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.


{{Properties_Title|tolerance}}

-    **head|Float**: Default is {{Value|0}}.


{{Properties_Title|version}}

-    **version|String**:

## Notes

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

## Useful formulas 

-    **addendum diameter**= **module** \* **(teeth +2)**

-    **pitch diameter**= **module** \* **teeth**

-    **axle base**= **pitch diameter (lantern gear 1 + 2)** : 2


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear LanternGear/it
