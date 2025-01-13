# PartDesign Revolution/it
---
 GuiCommand:   Name: PartDesign Revolution   Name/it: Rivoluzione   MenuLocation: PartDesign , Rivoluzione   Workbenches: PartDesign Workbench/it---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Lo strumento **Rivoluzione** crea un solido ruotando uno schizzo selezionato o un oggetto 2D attorno ad un dato asse.


</div>

![](images/PartDesign_Revolution_example.svg )


<div class="mw-translate-fuzzy">

*Sopra: lo schizzo (A) è ruotato di 270 gradi in senso antiorario attorno all\'asse (B); a destra è mostrato il solido risultante (C).*


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Seleziona lo schizzo da rivoluzionare. v0.17 e superiore In alternativa, è possibile utilizzare una faccia di un solido esistente.
2.  Premere il pulsante **<img src="images/PartDesign_Revolution.svg" width=24px> '''Rivoluzione'''**.
3.  Impostare i parametri Rivoluzione (vedere la sezione successiva).
4.  Premere **OK**.


</div>

## Options


<div class="mw-translate-fuzzy">

## Opzioni in Parametri rivoluzione 

Durante la creazione di una rivoluzione, il dialogo **Parametri rivoluzione** permette di specificare diversi parametri per stabilire come deve essere ruotato il disegno.


</div>

![](images/partdesign_revolution_parameters.png )

### Type


<small>(v1.0)</small> 

Type offers five different ways of specifying the angle of the revolution:

#### Dimension

Enter a numeric value for the **Angle** of the revolution. With the option **Symmetric to plane** the revolution will extend half the given angle to either side of the sketch or face.

#### To last 

The revolution will extend up to the last face of the support it encounters in its direction. If there is no support, an error message will appear.

#### To first 

The revolution will extend up to the first face of the support it encounters in its direction. If there is no support, an error message will appear.

#### Up to face 

The revolution will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.

#### Two dimensions 

This allows to enter a second angle in which the revolution should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.

### Axis

Specifies the axis of the revolution:


<div class="mw-translate-fuzzy">

+++
| ![](images/Partdesign_revolution_parameters_it.png ) | ### Assi                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | Questa opzione specifica l\'asse attorno al quale deve essere ruotato lo schizzo.                                                                                                                                                                                                                                                                                                                             |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | -   **Asse verticale dello schizzo**: seleziona l\'asse verticale dello schizzo.                                                                                                                                                                                                                                                                                                                              |
|                                                                                        | -   **Asse orizzontale dello schizzo**: seleziona l\'asse orizzontale dello schizzo.                                                                                                                                                                                                                                                                                                                          |
|                                                                                        | -   **Sketch axis**: v0.16 e precedenti seleziona una linea di costruzione contenuta nello schizzo utilizzato da Rivoluzione. La prima linea di costruzione creata nello schizzo viene etichettata *Schizzo asse 0*. L\'elenco a discesa contiene un asse dello schizzo personalizzato per ogni linea di costruzione.                    |
|                                                                                        | -   **Linea di costruzione**: v0.17 e successive seleziona una linea di costruzione contenuta nello schizzo utilizzato da Rivoluzione. L\'elenco a discesa contiene una voce per ogni linea di costruzione. La prima linea di costruzione creata nello schizzo verrà etichettata *Linea di costruzione 1*.                              |
|                                                                                        | -   **Asse (X/Y/Z) di base**: v0.17 e successive seleziona l\'asse X, Y o Z dell\'origine del corpo;                                                                                                                                                                                                                                    |
|                                                                                        | -   **Seleziona riferimento\...**: v0.17 e successive consente di selezionre un bordo del corpo o una [linea di riferimento](PartDesign_Line/it.md) nella vista 3D.                                                                                                                                                             |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                        | </div>                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                        | Note that when changing the axis, the **Reversed** option may be (un)checked automatically.                                                                                                                                                                                                                                                                                                                   |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | ### Angle                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                        | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                        | ### Angolo                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | Questa opzione specifica l\'angolo di rivoluzione dello schizzo. Per ottenere una rivoluzione completa occorre impostare un angolo di 360°. Le immagini della sezione [esempi](#Examples/it.md) documentano alcune delle possibilità utilizzando diversi angoli di rotazione. Non è possibile specificare angoli negativi (se è necessario usare l\'opzione **Invertita**) o angoli maggiori di 360°. |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | ### Simmetrica al piano                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | Se selezionato, la rivoluzione si estende per metà dell\'angolo specificato in entrambe le direzioni rispetto al piano di schizzo.                                                                                                                                                                                                                                                                            |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | ### Invertita                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                        | Se selezionato, la direzione di rotazione viene invertita passando da quella predefinita in senso orario a quella antioraria.                                                                                                                                                                                                                                                                                 |
+++





</div>

### Symmetric to plane 

Check this option to extend the revolution half the given angle to either side of the sketch or face. This option is only available if **Type** is **Dimension**.

### Reversed

Reverses the direction of the revolution.

### 2nd angle 


<small>(v1.0)</small> 

Defines the angle of the revolution in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.




<div class="mw-translate-fuzzy">

## Proprietà


</div>

### Data


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Revolution}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (read-only)

-    **Axis|Vector**: (read-only)

-    **Angle|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Angle2|Angle**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Notes

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to be selected in the [3D view](3D_view.md).


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Revolution/it
