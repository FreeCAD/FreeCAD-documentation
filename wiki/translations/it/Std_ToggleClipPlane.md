---
 GuiCommand:
   Name: Std ToggleClipPlane
   Name/it: Piano di taglio
   MenuLocation: Visualizza , Piano di taglio
   Workbenches: Tutti
   SeeAlso: Part_SectionCut/it
---

# Std ToggleClipPlane/it



## Descrizione

Il comando **Piano di taglio** nasconde temporaneamente oggetti e parti di oggetti su un lato di un massimo di tre piani virtuali nella [Vista 3D](3D_view/it.md) attiva.

![](images/Std_ToggleClipPlane_example.png ) 
*Un oggetto cavo ritagliato*

![](images/Std_ToggleClipPlane_Dialog.png ) 
*La finestra dialogo delle attività di ritaglio*



## Utilizzo

1.  Selezionare l\'opzione **Visualizza → <img src="images/Std_ToggleClipPlane.svg" width=16px> Piano di taglio** dal menu.
2.  Si apre la finestra di dialogo **Ritaglio**.
3.  Effettuare una delle seguenti operazioni:
    -   Seleziona una o più caselle di controllo da **Ritaglio X** a **Ritaglio Z**.
        -   Facoltativamente modificare le distanze di offset.
        -   Facoltativamente, modificare la/le distanza/e di offset.
        -   Facoltativamente, premere il/i pulsante/i **Flip** per cambiare il lato del piano di taglio su cui sono nascosti gli oggetti.
    -   Selezionare la casella di controllo {{CheckBox|TRUE|Ritaglio in direzione personalizzata}}.
        -   Facoltativamente, modificare la distanza di offset.
        -   Effettuare una delle seguenti operazioni:
            -   Premere il pulsante **Visualizza** per utilizzare la direzione della vista corrente.
            -   Seleziona la casella di controllo **Orienta in direzione della vista** per una direzione che si adatti dinamicamente a visualizzare le modifiche.
            -   Specificare la direzione inserendo le coordinate X, Y e Z di un vettore normale.
4.  Facoltativamente, modificare la vista per ispezionare il modello.
5.  Premere il pulsante **Chiudi** per chiudere il pannello delle attività e terminare il comando.



## Note

-   Per distinguere chiaramente l\'interno di oggetti parzialmente tagliati, cambiare la loro proprietà {{PropertyView/it|Lighting}} in {{Value|One side}}. Il colore del lato interno delle loro facce dipenderà quindi dalle impostazioni di retroilluminazione: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Colore retroilluminazione - Intensità**. Vedi [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleClipPlane/it
