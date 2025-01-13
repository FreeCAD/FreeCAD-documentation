---
 GuiCommand:
   Name: Std SetAppearance
   Name/it: Impostare l'aspetto degli oggetti
   MenuLocation: Visualizza , Aspetto...
   Workbenches: Material_Workbench/it, Part_Workbench/it, PartDesign_Workbench/it e altro
   Shortcut: **Ctrl**+**D**
   SeeAlso: Std_SetMaterial/it,Part_ColorPerFace/it
---

# Std SetAppearance/it



## Descrizione

Il comando **Aspetto** imposta le proprietà di visualizzazione degli oggetti selezionati.

Questa pagina è stata aggiornata per la versione 1.0.

![](images/Std_SetAppearance_Taskpanel.png ) 
*Il pannello delle azioni delle proprietà di Visualizzazione*



## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_SetAppearance.svg" width=16px> Aspetto...** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_SetAppearance.svg" width=16px> Aspetto...** dal menu contestuale [Vista albero](Tree_view/it.md) o dal menu contestuale [Vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Ctrl**+**D**.
3.  Si apre il pannello delle azioni **Proprietà di visualizzazione**. Vedere [Opzioni](#Opzioni.md).
4.  Modificare una o più proprietà.
5.  Gli oggetti vengono aggiornati immediatamente.
6.  Facoltativamente selezionare uno o più nuovi oggetti di cui si desidera modificarne le proprietà.
7.  Premere il pulsante **Chiudi** per chiudere il pannello delle azioni e terminare il comando.



## Opzioni



### Modalità di visualizzazione 

-   Selezionare una **Modalità di visualizzazione** dall\'elenco a discesa. Le opzioni disponibili sono: {{Value|Linee piatte}}, {{Value|Ombreggiato}} (non per oggetti [Draft](Draft_Workbench/it.md)), {{Value|Fil di ferro}} e {{Value|Punti}}. Vedere il comando [Stile di disegno](Std_DrawStyle/it.md) per maggiori informazioni.



### Materiale

-   Selezionare un materiale dall\'elenco.
    1.  Selezionare facoltativamente una categoria dall\'elenco a discesa sotto l\'elenco dei materiali per filtrare i materiali. Le categorie disponibili sono {{Value|Aspetto base}}, {{Value|Aspetto texture}} (tali materiali non sono ancora disponibili) e {{Value|Tutti i materiali}}.
    2.  Facoltativamente, premere il pulsante **Avvia editor** per avviare l\'[Editor materiali](Materials_Edit/it.md).
-   **Aspetto personalizzato:** premere il pulsante **...** per sovrascrivere l\'aspetto del materiale. Si apre la finestra di dialogo **Proprietà del materiale**. Vedere [Part Colore per faccia](Part_ColorPerFace/it#Utilizzo.md).
-   **Color plot:** non supportata al momento.
-   **Colore linea:** imposta la proprietà **Line Color**. Premere il pulsante per aprire la finestra di dialogo Seleziona colore.
-   **Colore punto:** imposta la proprietà **Point Color**. Premere il pulsante per aprire la finestra di dialogo Seleziona colore.



### Visualizzazione

-   **Dimensione punto:** imposta la proprietà **Point Size** (in pixel).
-   **Spessore linea:** imposta la proprietà **Line Width** (in pixel).
-   **Transparenza:** imposta la proprietà **Transparency** (in percentuale). 0% è opaco, 100% è completamente trasparente.
-   **Trasparenza linea:** non supportata al momento.



## Note

-   Le proprietà di visualizzazione menzionate possono essere modificate anche nell\'[Editor delle proprietà](Property_editor/it.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std SetAppearance/it
