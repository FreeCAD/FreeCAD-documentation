# PartDesign Groove/it
---
 GuiCommand:   Name: PartDesign_Groove   Name/it: Scanalatura   Workbenches: PartDesign Workbench/it   PartDesign---


</div>



## Descrizione

Questo strumento rivoluziona uno schizzo selezionato o un oggetto 2D attorno ad un dato asse, asportando del materiale dall\'oggetto di supporto.

![](images/PartDesign_Groove_example.svg )



*A sinistra lo schizzo (A) è ruotato attorno all'asse (B); a destra la scanalatura risultante sul solido (C).*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare lo schizzo da ruotare.

    :   È possibile utilizzare una faccia di un solido esistente. {{VersionPlus/it|0.17}}
    :   Lo schizzo deve essere mappato sulla faccia planare di un solido esistente o di una funzione di Part Design, altrimenti viene visualizzato un messaggio di errore. {{VersionMinus/it|0.16}}
2.  Premere il pulsante **<img src="images/PartDesign_Groove.svg" width=24px> '''Scanalatura'''**.
3.  Impostare i parametri della scanalatura (vedere la prossima sezione).
4.  Premere **OK**.


</div>



## Opzioni


<div class="mw-translate-fuzzy">

Quando si crea una scanalatura, i dialoghi **Parametri Groove** offrono diversi parametri che specificano come deve essere ruotato lo sketch.


</div>


<div class="mw-translate-fuzzy">

+++
| ![](images/Partdesign_groove_parameters_it.png ) | ### Assi                                                                                                                                                                                                                                                                                                                                      |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | </div>                                                                                                                                                                                                                                                                                                                                        |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | ### Type                                                                                                                                                                                                                                                                                                                                      |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                |
|                                                                                | <small>(v1.0)</small>                                                                                                                                                                                                                                                                                                                                |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | Type offers five different ways of specifying the angle of the groove:                                                                                                                                                                                                                                                                        |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | #### Dimension                                                                                                                                                                                                                                                                                                                                |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | Enter a numeric value for the **Angle** of the groove. With the option **Symmetric to plane** the groove will extend half the given angle to either side of the sketch or face.                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | #### Through all                                                                                                                                                                                                                                                                                                                |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | The groove will extend up to the last face of the support it encounters in its direction. With the option **Symmetric to plane** the groove will cut through all material in both directions.                                                                                                                                                 |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | #### To first                                                                                                                                                                                                                                                                                                                      |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | The groove will extend up to the first face of the support it encounters in its direction.                                                                                                                                                                                                                                                    |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | #### Up to face                                                                                                                                                                                                                                                                                                                  |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | The groove will extend up to a face. Press the **Face** button and select a face or a [datum plane](PartDesign_Plane.md) from the Body.                                                                                                                                                                          |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | #### Two dimensions                                                                                                                                                                                                                                                                                                          |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | This allows to enter a second angle in which the groove should extend in the opposite direction. The directions can be switched by checking the **Reversed** option.                                                                                                                                                                          |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | ### Axis                                                                                                                                                                                                                                                                                                                                      |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | Specifies the axis of the groove:                                                                                                                                                                                                                                                                                                             |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                              |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | Questa opzione specifica l\'asse attorno al quale deve essere ruotato lo schizzo.                                                                                                                                                                                                                                                             |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | -   **Vertical sketch axis**: seleziona l\'asse verticale dello schizzo.                                                                                                                                                                                                                                                                      |
|                                                                                | -   **Horizontal sketch axis**: seleziona l\'asse orizzontale dello schizzo.                                                                                                                                                                                                                                                                  |
|                                                                                | -   **Sketch axis**: seleziona una linea di costruzione contenuta nello schizzo utilizzato da Scanalatura. La prima linea di costruzione creata nello schizzo viene etichettata come *Sketch axis 0*. L\'elenco a discesa contiene un asse dello schizzo personalizzato per ogni linea di costruzione. {{VersionMinus/it|0.16}} |
|                                                                                | -   **Construction line**: seleziona una linea di costruzione contenuta nello schizzo utilizzato da Scanalatura. L\'elenco a discesa contiene una voce per ogni linea di costruzione. La prima linea di costruzione creata nello schizzo viene etichettata *Construction line 1*. {{VersionPlus/it|0.17}}                       |
|                                                                                | -   **Base (X/Y/Z) axis**: v0.17 e superiore seleziona l\'asse X, Y o Z dell\'origine del corpo; {{VersionPlus/it|0.17}}                                                                                                                                  |
|                                                                                | -   **Select reference\...**: v0.17 e superiore consente di selezionare nella vista 3D un bordo di un corpo o una [linea di riferimento](PartDesign_Line/it.md). {{VersionPlus/it|0.17}}                                                          |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | </div>                                                                                                                                                                                                                                                                                                                                        |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | Note that when changing the axis, the **Reversed** option may be (un)checked automatically.                                                                                                                                                                                                                                                   |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                     |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | ### Angolo                                                                                                                                                                                                                                                                                                                                    |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                              |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | Questa opzione specifica l\'angolo di rotazione dello schizzo. Per ottenere una scanalatura completa occorre impostare un angolo di 360°. Non è possibile specificare angoli negativi (se è necessario usare l\'opzione **Invertito**) o angoli maggiori di 360°.                                                                             |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | </div>                                                                                                                                                                                                                                                                                                                                        |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                |                                                                                                                                                                                                                                                                                        |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | ### Simmetrico al piano                                                                                                                                                                                                                                                                                                 |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                              |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | La rivoluzione si estende per metà dell\'angolo specificato in entrambe le direzioni rispetto al piano di schizzo.                                                                                                                                                                                                                            |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | </div>                                                                                                                                                                                                                                                                                                                                        |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                |                                                                                                                                                                                                                                                                                                  |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                | ### Invertito                                                                                                                                                                                                                                                                                                                                 |
|                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|                                                                                |                                                                                                                                                                                                                                                                                                                                     |
|                                                                                | <div class="mw-translate-fuzzy">                                                                                                                                                                                                                                                                                                              |
|                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|                                                                                | La direzione di rivoluzione viene invertita.                                                                                                                                                                                                                                                                                                  |
+++


</div>

### 2nd angle 


<small>(v1.0)</small> 

Defines the angle of the groove in the opposite direction. This option is only available if **Type** is **Two dimensions** and **Angle** is smaller than 360°.



## Proprietà

### Data


{{TitleProperty|Groove}}

-    **Type|Enumeration**
    

-    **Base|Vector**: (read-only)

-    **Axis|Vector**: (read-only)

-    **Angle|Angle**
    

-    **Angle2|Angle**
    

-    **Up To Face|LinkSub**
    

-    **Reference Axis|LinkSub**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**
    


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    

## Notes

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to selected in the [3D view](3D_view.md).


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Groove/it
