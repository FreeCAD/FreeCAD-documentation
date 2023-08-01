---
- GuiCommand:
   Name:Std ToggleClipPlane
   Name/it:Piano di taglio
   MenuLocation:Visualizza → Piano di taglio
   Workbenches:Tutti
   SeeAlso:[Taglio sezione persistente](Part_SectionCut/it.md)
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
2.  Nella finestra dialogo delle attività di ritaglio, eseguire una delle seguenti operazioni:
    -   Selezionare una o più caselle di controllo da {{CheckBox|TRUE|Clipping X}} a {{CheckBox|TRUE|Clipping Z}}.
        -   Facoltativamente, modificare la/le distanza/e di offset.
        -   Facoltativamente, premere il/i pulsante/i **Flip** per cambiare il lato del piano di taglio su cui sono nascosti gli oggetti.
    -   Selezionare la casella di controllo {{CheckBox|TRUE|Ritaglio in direzione personalizzata}}.
        -   Facoltativamente, modificare la distanza di offset.
        -   Effettuare una delle seguenti operazioni:
            -   Premere il pulsante **Visualizza** per utilizzare la direzione della vista corrente.
            -   Selezionare la casella di controllo {{CheckBox|TRUE|Orienta in direzione della vista}} per una direzione che si adatta dinamicamente ai cambiamenti della vista.
            -   Specificare la direzione inserendo le coordinate X, Y e Z di un vettore normale.
3.  Facoltativamente, modificare la vista per ispezionare il modello.
4.  Premere il pulsante **Chiudi** per chiudere il pannello delle attività e terminare il comando.



## Note

-   Per distinguere chiaramente l\'interno di oggetti parzialmente tagliati, cambiare la loro proprietà {{PropertyView/it|Illuminazione}} in \'Un lato\'. Il colore del lato interno delle loro facce dipenderà quindi dalle impostazioni di retroilluminazione: **Modifica → Preferenze... → Visualizzazione → Vista 3D → Colore retroilluminazione - Intensità**. Vedi [Editor delle preferenze](Preferences_Editor/it#Vista_3D.md).





{{Std_Base_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ToggleClipPlane/it
