---
 GuiCommand:
   Name: Part ColorPerFace
   Name/it: Part Colore per faccia
   MenuLocation: Visualizza , Colore per faccia
   Workbenches: Part Workbench/it, PartDesign Workbench/it
   SeeAlso: Std_SetAppearance/it
---

# Part ColorPerFace/it



## Descrizione

Il comando **Part Colore per faccia** imposta le proprietà di visualizzazione delle facce selezionate. Per modificare un intero oggetto utilizzare invece [Impostare l\'aspetto degli oggetti](Std_SetAppearance/it.md).

Questa pagina è stata aggiornata per la versione 1.0.

![](images/Part_ColorPerFace_Taskpanel.png ) 
*Il pannello delle azioni Imposta aspetto per faccia*



## Utilizzo

1.  Selezionare un singolo oggetto.
2.  Esistono diversi modi per richiamare il comando:
    -   Se l\'[Ambiente Part](Part_Workbench/it.md) è attivo: premere il pulsante **<img src="images/Part_ColorPerFace.svg" width=16px> [Colore per faccia](Part_ColorPerFace/it.md)**.
    -   Selezionare l\'opzione **Visualizza → <img src="images/Part_ColorPerFace.svg" width=16px> Colore per faccia** dal menu.
    -   Selezionare l\'opzione **<img src="images/Part_ColorPerFace.svg" width=16px> Imposta aspetto per la faccia...** dal menu contestuale [Vista ad albero](Tree_view/it.md).
3.  Si apre il pannello delle azioni **Imposta aspetto per la faccia**.
4.  Selezionare uno o più facce:
    -   Tenere premuto **Ctrl** per selezionare più facce.
    -   Facoltativamente, premere il pulsante **Box Selection**, fare clic in un\'area vuota e trascinare un rettangolo per selezionare tutte le facce appartenenti all\'oggetto che sono (parzialmente) all\'interno del rettangolo. È possibile specificare più selezioni di caselle.
5.  Effettuare una delle seguenti operazioni:
    -   Selezionare un materiale dall\'elenco.
        1.  Facoltativamente, premere il pulsante **Avvia editor** per avviare [Editor materiali](Materials_Edit/it.md).
    -   Specificare un **Aspetto personalizzato**:
        1.  Premere il pulsante **...**.
        2.  Si apre la finestra di dialogo **Proprietà del materiale**:
            ![](images/Material_Properties_Dialog.png )
        3.  Queste proprietà possono essere modificate:
            -   **Colore ambiente**: colore delle ombre sull\'oggetto.
            -   **Colore diffuso**: colore effettivo/base dell\'oggetto.
            -   **Colore emissivo**: colore della luce irradiata dall\'oggetto.
            -   **Colore speculare**: colore dell\'evidenziazione (riflessione) su una superficie lucida dell\'oggetto.
            -   **Lucentezza**
            -   **Trasparenza**
        4.  Facoltativamente, premere il pulsante **Reset** per modificare l\'aspetto in quello definito dal materiale.
        5.  Facoltativamente, premere il pulsante **Default** per modificare l\'aspetto in modo che corrisponda alle [preferenze](PartDesign_Preferences/it#Shape_appearance.md) attuali.
        6.  Al termine, premere il pulsante **Chiudi**.
    -   Premere il pulsante **Imposta su predefinito** per modificare l\'aspetto in quello definito dal materiale.
6.  Facoltativamente selezionare uno o più nuove facce di cui desidera modificare le proprietà.
7.  Premere il pulsante **OK** per chiudere il pannello delle azioni e terminare il comando.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ColorPerFace/it
