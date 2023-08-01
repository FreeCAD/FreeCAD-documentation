---
- GuiCommand:
   Name:Std SetAppearance
   Name/it:Impostare l'aspetto degli oggetti
   MenuLocation:Visualizza - Aspetto...
   Workbenches:Tutti
   Shortcut:**Ctrl**+**D**
   SeeAlso:[Impostare il colore delle facce](Part_FaceColors/it.md)
---

# Std SetAppearance/it



## Descrizione

Il comando **Impostare l\'aspetto degli oggetti** mostra le proprietà di visualizzazione [Scheda Azioni](Task_panel/it.md) per gli oggetti selezionati.

<img alt="" src=images/DlgDisplayProperties.png  style="width:250px;"> 
*Il pannello delle attività delle proprietà di visualizzazione*



## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → <img src="images/Std_SetAppearance.svg" width=16px> Aspetto...** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_SetAppearance.svg" width=16px> Aspetto...** dal menu contestuale [Vista albero](Tree_view/it.md) o dal menu contestuale [Vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Ctrl**+**D**.
3.  Modificare una o più proprietà di visualizzazione. Vedere [Opzioni](#Opzioni.md). Gli oggetti verranno aggiornati immediatamente.
4.  Facoltativamente selezionare uno o più nuovi oggetti di cui si desidera modificare le proprietà di visualizzazione.
5.  Premere il pulsante **Chiudi** per chiudere il pannello delle attività e terminare il comando.



## Opzioni



### Modalità di visualizzazione 

-   Selezionare una **Modalità di visualizzazione** dall\'elenco a discesa. Le opzioni disponibili sono: \'Linee piatte\', \'Ombreggiato\' (non per oggetti [Draft](Draft_Workbench/it.md)), \'Fil di ferro\' e \'Punti\'. Vedere il comando [Stile di disegno](Std_DrawStyle/it.md) per maggiori informazioni.



### Materiale

-   Selezionare un materiale predefinito dall\'elenco a discesa (\'Predefinito\', \'Alluminio\', \'Ottone\', \'Bronzo\', ecc.).
-   Premere il pulsante **...** per aprire la finestra di dialogo delle proprietà del materiale e modificare i colori ambientali, diffusi, emissivi e speculari, nonché la brillantezza.
-   **Colore trama:** non supportato in questo momento.
-   **Colore forma:** imposta la proprietà **Shape Color**. Premere il pulsante per aprire la finestra di dialogo Seleziona colore.
-   **Colore linea:** imposta la proprietà **Line Color**. Premere il pulsante per aprire la finestra di dialogo Seleziona colore.
-   **Colore punto:** imposta la proprietà **Point Color**. Premere il pulsante per aprire la finestra di dialogo Seleziona colore.



### Visualizzazione

-   **Dimensione punto:** imposta la proprietà **Point Size** (in pixel).
-   **Spessore linea:** imposta la proprietà **Line Width** (in pixel).
-   **Transparenza:** imposta la proprietà **Transparency** (in percentuale). 0% è opaco, 100% è completamente trasparente.
-   **Trasparenza linea:** non supportata al momento.



## Note

-   Le proprietà della vista menzionate possono anche essere modificate nell\'[Editor delle proprietà](Property_editor/it.md) o nella [Vista combinata](Combo_view/it.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SetAppearance/it
