---
 GuiCommand:
   Name: PartDesign SubtractiveHelix
   Name/it: Elica sottrattiva
   MenuLocation: Part Design , Crea una funzione sottrattiva , Elica sottrattiva
   Workbenches: PartDesign_Workbench/it
   Version: 0.19
   SeeAlso: PartDesign_AdditiveHelix/it
---

# PartDesign SubtractiveHelix/it



## Descrizione

Lo strumento **Elica sottrattiva** modifica un solido spostando uno schizzo selezionato o un oggetto 2D lungo un percorso elicoidale asportando il materiale.

![](images/PartDesign_SubtractiveHelix_example_overview.png )

*Il profilo (B), viene trascinato attorno all\'asse (A) in modo da realizzare la scanalatura elicoidale (C) nel pezzo preesistente*



## Utilizzo

1.  Selezionare lo schizzo da trascinare nell\'elica. In alternativa è possibile utilizzare una faccia del solido esistente.
2.  Premere il pulsante **<img src="images/PartDesign_SubtractiveHelix.svg" width=24px> [Elica sottrattiva](PartDesign_SubtractiveHelix/it.md)**.
3.  Impostare i parametri dell\'elica (vedere la sezione successiva).
4.  Verificare l\'elica nella finestra della vista, per garantire che i parametri non risultino in un\'elica autointersecante.
5.  Cliccare su **OK**.



## Opzioni

Quando si crea un\'Elica sottrattiva, la finestra di dialogo **Parametri dell\'elica** offre diversi parametri che specificano come deve essere fatto scorrere lo schizzo.

![](images/PartDesign_SubtractiveHelix_taskpanel.png )



### Asse

Questa opzione specifica l\'asse attorno al quale lo schizzo deve essere spostato.

-   **Asse normale allo schizzo**: seleziona la normale dello schizzo che attraversa l\'origine dello schizzo come asse. {{Version/it|0.20}}
-   **Asse verticale dello schizzo**: seleziona l\'asse verticale dello schizzo.
-   **Asse orizzontale dello schizzo**: seleziona l\'asse orizzontale dello schizzo.
-   **Linea di costruzione**: seleziona una linea di costruzione contenuta nello schizzo utilizzato dall\'Elica. L\'elenco a discesa conterrà una voce per ciascuna linea di costruzione. La prima linea di costruzione creata nello schizzo verrà etichettata *Linea di costruzione 1*.
-   **Asse (X/Y/Z) di Base**: seleziona l\'asse X, Y o Z dell\'Origine del Corpo;
-   **Seleziona riferimento\...**: consente la selezione nella vista 3D di un bordo sul Corpo, o di una [linea di riferimento](PartDesign_Line/it.md).



### Modalità

This controls what parameters will be used to define the helix. The choices are:

-   **Pitch-Height-Angle**: definition via the height per turn and the overall height
-   **Pitch-Turns-Angle**: definition via the height per turn and the number of turns
-   **Height-Turns-Angle**: definition via the overall height and the number of turns
-   **Height-Turns-Growth** <small>(v0.20)</small> : definition via the overall height, the number of turns and the growth of the helical radius. So a Height of zero leads to a path in form of a spiral. A Height and Growth of zero to leads to a path in form of a circle.



### Passo

The distance between turns in the helix.



### Altezza

The height of the helix (center-center).



### Numero giri 

The number of turns in the helix. Define as Height/Pitch



### Angolo cono 

Angle of the cone that forms a hull around the helix. Allowable range: \[-89°, +89°\].



### Sinistrorsa

If checked, the turning direction of helix is reversed from default clockwise to counterclockwise.



### Invertita

If checked, the axis direction of helix is reversed from default.

### Remove outside of profile 

If checked, the result will be the intersection of the swept profile and the preexisting body.



### Aggiorna la vista 

If checked, the helix will be shown in the view, and updated automatically on every change of the parameters.



## Preferenze

-   A subtractive helix that does not intersect the body will be visible in the preview if **Tools → Edit parameters... → BaseApp → Preferences → Mod → PartDesign → SubtractiveHelixPreview** is set to `True`. The default for this preference is `True`. <small>(v0.20)</small> 



## Proprietà

-    **Pitch**: The axial distance between two turns.

-    **Height**: The total length of the helix (not accounting for the extent of the profile)

-    **Turns**: The number of turns (does not need to be a whole number)

-    **Left Handed**: See [Left Handed](#Left_handed.md).

-    **Reversed**: See [Reversed](#Reversed.md).

-    **Angle**: The rate at which the radius of the helix increase along the axis. Allowable range: \[-89°, +89°\].

-    **Reference axis**: The helix axis

-    **Mode**: The helix input mode (pitch-height, pitch-turns, turns-height)

-    **Outside**: If true, the result will be the intersection of the swept profile and the preexisting body.

-    **Has Been Edited**: If false, the tool will propose an initial value for pitch based on the profile bounding box, so that self intersection is avoided.

-    **Refine**: true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

-    **Profile**: Either a sketch containing a closed contour, or a face.

-    **Midplane**: Not used.

-    **Up to face**: Not used.

-    **Allow multiple face**: Not used.



## Note

-   A <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:16px;"> [ShapeBinder](PartDesign_ShapeBinder.md) cannot be used for the profile.
-   When using a <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:16px;"> [SubShapeBinder](PartDesign_SubShapeBinder.md) for the profile, selecting the binder in the [Tree view](Tree_view.md) will fail, instead the binder\'s face has to selected in the [3D view](3D_view.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveHelix/it
