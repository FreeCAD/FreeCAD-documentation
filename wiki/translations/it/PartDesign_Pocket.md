# PartDesign Pocket/it
---
- GuiCommand:/it   Name:PartDesign_Pocket   Name/it:Tasca   MenuLocation:PartDesign → Tasca   Workbenches:[PartDesign](PartDesign_Workbench/it.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Lo strumento **Tasca** scava un solido estrudendo uno schizzo, o una faccia di un solido, in un percorso rettilineo e sottraendolo dal solido.


</div>

![](images/PartDesign_Pocket_example.svg ) \'\'A sinistra lo schizzo del profilo (A) è mappato sulla faccia superiore del solido di base (B); a destra il risultato della tasca. \'\'

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Selezionare lo schizzo da usare per lo scavo.

    :   Lo schizzo selezionato deve essere mappato su una faccia planare di un solido esistente o su un oggetto Part Design, altrimenti si riceve un messaggio di errore. {{VersionMinus/it|0.16}}
2.  Premere il pulsante **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''**.
3.  Impostare i parametri Pocket (vedere successiva sezione).
4.  Cliccare OK.


</div>

When selecting a single sketch, it can have multiple enclosed profiles inside a larger one, for example a rectangle with two circles inside it. But the profiles may not intersect each other. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

### Opzioni

![](images/Pocket_options_it.png )


</div>

When creating a pocket, the the **Pocket parameters** dialog will be shown. It offers the following settings:

![](images/pocket_parameters_cropped.png )

### Type

Type offers four different ways of specifying the length to which the pocket will be extruded:

#### Dimension


<div class="mw-translate-fuzzy">

Quando si crea una cavità, la finestra di dialogo **Parametri Tasca** offre quattro diversi modi per specificare la lunghezza (profondità) di estrusione dello scavo:

#### Quota

Inserire un valore numerico per la profondità della tasca. La direzione di default per l\'estrusione è verso l\'interno del supporto. Le estrusioni si realizzano [normali](http://en.wikipedia.org/wiki/Surface_normal) al piano di definizione dello schizzo.

Le quote negative non sono possibili. Al suo posto usare invece l\'opzione **Invertita**.

#### Fino al primo 

La tasca viene prodotta fino alla prima faccia del supporto nella direzione di estrusione. In altre parole, viene asportato tutto il materiale fino a raggiungere uno spazio vuoto.

#### Attraverso tutto 

La tasca scava attraverso tutto il materiale nella direzione di estrusione. Quando si attiva l\'opzione **Simmetrico al piano** lo scavo viene prodotto attraverso tutto il materiale in entrambe le direzioni.

#### Fino alla faccia 

La tasca si estrude fino a una faccia del supporto che può essere scelta facendo clic su di essa.

### Due dimensioni 

Questo permette di inserire una seconda lunghezza per estendere la tasca nella direzione opposta (nel supporto). Anche questa può essere cambiata spuntando l\'opzione **Invertita**. {{VersionPlus/it|0.17}}


</div>

#### Through all 

The pocket will extrude through all objects in the extrusion direction. With the option **Symmetric to plane** the pad will cut through all material in both directions.**Note:** For technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.

#### To first 

The pocket will extrude up to the first face of the support in the extrusion direction. In other words, it will cut through all material until it reaches an empty space.

#### Up to face 

The pocket will extrude up to a face in the model that can be chosen by clicking on it.

#### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction (into the support). The directions can be switched by ticking the **Reversed** option.

### Length

Defines the length of the pocket. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available when **Type** is either **Dimension** or **Two dimensions**.

### Offset to face 

Offset from face at which the pocket will end. This option is only available when **Type** is either **Through all**, **To first** or **Up to face**.

### Direction


<small>(v0.20)</small> 

#### Direction/edge

You can select the direction of the extrusion:

-   **Face/Sketch normal** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion.
-   **Custom direction** The sketch is extruded along a direction that can be specified via vector values.

#### Show direction 

If checked, the pocket direction will be shown. In case the pocket uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pocket length is measured along the sketch normal, otherwise along the custom direction.

### Symmetric to plane 

Tick the checkbox to extrude half of the given length to either side of the sketch or plane.

### Reversed

Reverses the direction of the pocket.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations:

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pocket would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pocket in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pocket in the opposite extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

## Properties

-    **Type**: Type of ways how the pocket will be extruded, see [Options](#Options.md).

-    **Length**: Defines the length of the pocket, see [Options](#Options.md).

-    **Length2**: Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector**: <small>(v0.20)</small>  If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**: <small>(v0.20)</small>  Vector of the pocket direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**: <small>(v0.20)</small>  If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face**: A face the pocket will extrude up to, see [Options](#Options.md).

-    **Refine**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part design → General → Model settings**). It can be manually changed afterwards. This property will be saved with the FreeCAD document.

## Limitations


<div class="mw-translate-fuzzy">

### Limitazioni

-   Quando è possibile utilizzare il tipo **Quota** oppure **Attraverso tutto** perché gli altri tipi a volte danno problemi quando essi vengono utilizzati per essere replicati in schiere.
-   Inoltre, la funzione tasca ha le stesse [limitazioni](PartDesign_Pad#Limitations.md) della funzione Pad.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/it
