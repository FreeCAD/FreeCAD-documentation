# PartDesign Pocket/it
---
 GuiCommand:   Name: PartDesign_Pocket   Name/it: Tasca   MenuLocation: PartDesign , Tasca   Workbenches: PartDesign Workbench/it---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Lo strumento **Tasca** scava un solido estrudendo uno schizzo, o una faccia di un solido, in un percorso rettilineo e sottraendolo dal solido.


</div>

![](images/PartDesign_Pocket_example.svg ) *A sinistra lo schizzo del profilo (A) è mappato sulla faccia superiore del solido di base (B); a destra il risultato della tasca.*

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Selezionare lo schizzo da usare per lo scavo.

    :   Lo schizzo selezionato deve essere mappato su una faccia planare di un solido esistente o su un oggetto Part Design, altrimenti si riceve un messaggio di errore. {{VersionMinus/it|0.16}}
2.  Premere il pulsante **<img src="images/PartDesign_Pocket.svg" width=16px> '''Pocket'''**.
3.  Impostare i parametri Pocket (vedere successiva sezione).
4.  Cliccare OK.


</div>




<div class="mw-translate-fuzzy">

### Opzioni

![](images/Pocket_options_it.png )


</div>

When creating a pocket, or after double-clicking an existing pocket in the [Tree view](Tree_view.md), the **Pocket parameters** task panel is shown. It offers the following settings:

![](images/PartDesign_Pocket_Taskpanel.png )

### Type

Type offers five different ways of specifying the length of the pocket:

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

The pocket will extend up to the last face of the support it encounters in its direction. With the option **Symmetric to plane** the pocket will cut through all material in both directions. Note that for technical reasons, *Through All* is actually a 10 meter deep pocket. If you need deeper pockets, use the type **Dimension**.

#### To first 

The pocket will extend up to the first face of the support it encounters in its direction.

#### Up to face 

The pocket will extend up to a face. Press the **Select face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.

#### Two dimensions 

This allows to enter a second length in which the pocket should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

#### Up to shape 


<small>(v1.0)</small> 

: The pocket will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select** button and select the faces up to which the pocket should be created.

### Offset to face 

Offset from face at which the pocket will end. This option is only available if **Type** is **Through all**, **To first** or **Up to face**.

### Length

Defines the length of the pocket. This option is only available if **Type** is **Dimension** or **Two dimensions**. The length is measured along the direction vector, or along the normal of the sketch or face. Negative values are not possible. Use the **Reversed** option instead.

### 2nd length 

Defines the length of the pocket in the opposite direction. This option is only available if **Type** is **Two dimensions**.

### Symmetric to plane 

Check this option to extrude half the given length to either side of the sketch or face, if **Type** is **Dimension**, or **Through all** if that is the **Type**.

### Reversed

Reverses the direction of the pocket.

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Sketch normal** or **Face normal:** The sketch or face is extruded in the opposite direction of its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used.
-   **Select reference\...:** The sketch or face is extruded in the opposite direction of a straight edge or a [datum line](PartDesign_Line.md) selected from the Body.
-   **Custom direction:** The sketch or face is extruded in the direction of the specified vector.

#### Show direction 

If checked, the pocket direction will be shown. In case the pocket uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pocket length is measured along the sketch or face normal, otherwise along the custom direction.

### Taper angle 

Tapers the pocket in the extrusion direction by the given angle. A positive angle means the outer pocket border gets wider. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts. This option is only available if **Type** is **Dimension** or **Two dimensions**.

### 2nd taper angle 

Tapers the pocket in the opposite extrusion direction by the given angle. See **Taper angle**. This option is only available if **Type** is **Two dimensions**.

## Properties

### Data


{{TitleProperty|Part Design}}

-    **Refine|Bool**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part Design → General → Model settings**).


{{TitleProperty|Pocket}}

-    **Type|Enumeration**: Defines how the pocket will be extruded, see [Options](#Options.md).

-    **Length|Length**: Defines the length of the pocket, see [Options](#Options.md).

-    **Length2|Length**: Second pocket length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector|Bool**: If checked, the pocket direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction|Vector**: Vector of the pocket direction if **Use Custom Vector** is used.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: If *true*, the pocket length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face|LinkSub**: A face the pocket will extrude up to, see [Options](#Options.md).

-    **Offset|Length**
    

-    **Taper Angle|Angle**
    

-    **Taper Angle2|Angle**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

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
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pocket/it
