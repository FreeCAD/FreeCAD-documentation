---
 GuiCommand:
   Name: Std Transform
   Name/it: Trasforma
   MenuLocation: Modifica , Trasforma
   Workbenches: All
   SeeAlso: Std_UserEditMode
---

# Std TransformManip/it



## Descrizione

Il comando **Trasforma** consente di applicare incrementi di rotazione e incrementi di traslazione a un oggetto.

<img alt="" src=images/Std_TransformManip_Example.png  style="width:400px;">



## Utilizzo

1.  Selezionare un oggetto con una proprietà **Placement**. Vedere [Note](#Note.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_TransformManip.svg" width=16px> Trasforma** dal menu.
    -   Seleziona l\'opzione **<img src="images/Std_TransformManip.svg" width=16px> Trasforma** dal menu contestuale [Vista ad albero](Tree_view/it.md).
    -   Se [modalità modifica](Std_UserEditMode/it.md) è impostato su **<img src="images/Std_UserEditModeTransform.svg" width=16px> Trasforma** si può anche fare doppio clic sull\'oggetto nella vista ad albero.
3.  Si apre il pannello delle attività **Increments**.
4.  Facoltativamente regolare i parametri degli incrementi.
5.  Effettuare una o più delle seguenti operazioni:
    -   Tenere premuto il pulsante sinistro del mouse sulla freccia di un asse e trascinare per traslare l\'oggetto lungo quell\'asse.
    -   Tenere premuto il pulsante sinistro del mouse su un piano e trascinare per traslare l\'oggetto lungo quel piano.
    -   Tenere premuto il pulsante sinistro del mouse su una sfera e trascinarla per ruotare l\'oggetto attorno a quell\'asse.
6.  Effettuare una delle seguenti operazioni:
    -   Premere il pulsante **OK** per confermare e terminare il comando.
    -   Premere il pulsante **Annulla** per annullare le trasformazioni applicate e terminare il comando. {{Version/it|1.0}}



## Note

-   Non appena si ruota/sposta l\'oggetto nella [Vista 3D](3D_view/it.md), le modifiche vengono applicate.
-   Alcuni oggetti con una proprietà **Placement**, come gli schizzi, non possono essere manipolati, né lo possono essere gli oggetti collegati ad altri oggetti.
-   Non c\'è il pulsante **Annulla** in {{VersionMinus/it|0.21}}, in quelle versioni si può premere il pulsante **OK** e utilizzare il comando <img alt="" src=images/Std_Undo.svg  style="width:16px;"> [Annulla](Std_Undo/it.md) per annullare le modifiche successivamente.



---
⏵ [documentation index](../README.md) > Std TransformManip/it
