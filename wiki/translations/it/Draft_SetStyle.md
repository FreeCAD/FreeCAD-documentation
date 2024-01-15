---
 GuiCommand:
   Name: Draft SetStyle
   Name/it: Draft Imposta stile
   MenuLocation: Utilità , Imposta stile
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Shortcut: **S** **S**
   Version/it: 0.19
   SeeAlso: Draft_AnnotationStyleEditor/it, Draft_ApplyStyle/it
---

# Draft SetStyle/it



## Descrizione

Il comando <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft Imposta stile** imposta lo stile predefinito per i nuovi oggetti.

<img alt="" src=images/Draft_SetStyle_Taskpanel.png  style="width:" height="550px;"> 
*Il pannello delle attività delle impostazioni di stile*



## Utilizzo

1.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante ![](images/Draft_tray_button_style.png ) nel [Vassoio di Draft](Draft_Tray/it.md). A seconda delle impostazioni di stile correnti, questo pulsante può avere un aspetto diverso.
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_SetStyle.svg" width=16px> Imposta lo stile** dal menu.
    -   Usare la scorciatoia da tastiera: **S** quindi **S**.
2.  Si apre il pannello delle attività **Impostazioni dello stile**. Vedere [Opzioni](#Opzioni.md) per ulteriori informazioni.
3.  Facoltativamente modificare una o più impostazioni.
4.  Premere il pulsante **OK** per salvare le impostazioni.
5.  Il pulsante nella [Vassoio di Draft](Draft_Tray.md) viene aggiornato.



## Opzioni

-   Dall\'elenco a discesa nella parte superiore del pannello delle attività è possibile selezionare uno stile predefinito.
-   Premere il pulsante **<img src="images/Document-save.svg" width=16px>** per salvare le impostazioni correnti dello stile come preimpostazione.
-   Nella sezione **Forme** è possibile specificare le seguenti impostazioni:
    -   
        **Colore forma**
        
        .

    -   
        **Trasparenza**
        
        .

    -   
        **Colore linea**
        
        .

    -   
        **Spessore linea**
        
        .

    -   
        **Colore punto**
        
        . {{Version/it|0.22}}

    -   
        **Dimensione punto**
        
        . {{Version/it|0.22}}

    -   
        **Stile disegno**
        
        .

    -   
        **Modalità visualizzazione**
        
        .
-   Le impostazioni nella sezione **Annotatzioni** si applicano a [Draft Testi](Draft_Text/it.md), [Draft Quote](Draft_Dimension/it.md) e [Draft Etichette](Draft_Label/it.md). È possibile specificare le seguenti impostazioni (vedere [Draft Testo](Draft_Text/it#Vista.md) per i dettagli):
    -   
        **Colore testo**
        
        .

    -   
        **Carattere del testo**
        
        .

    -   
        **Dimensione carattere**
        
        . Questa è infatti l\'altezza della riga predefinita, le lettere sono più piccole.

    -   
        **Interlinea**
        
        . Non utilizzato per le quote.

    -   
        **Moltiplicatore di scala**
        
        . Questo è l\'inverso della scala impostata nel [Dispositivo scala annotazione di Draft](Draft_annotation_scale_widget/it.md). Se la scala è {{value|1:100}} il moltiplicatore è {{Value|100}}. {{Version/it|0.22}}
-   Nella sezione **Quotatura** è possibile specificare le seguenti impostazioni (vedere [Draft Quotatura](Draft_Dimension/it#Vista.md) per i dettagli):
    -   
        **Colore linea e freccia**
        
        . {{Version/it|0.22}}

    -   
        **Spessore linea**
        
        . {{Version/it|0.22}}

    -   
        **Tipo di freccia**
        
        .

    -   
        **Dimensione freccia**
        
        .

    -   
        **Mostra unità**
        
        .

    -   
        **Sostituzione unità**
        
        .

    -   
        **Estensione della linea di misura**
        
        . {{Version/it|0.21}}

    -   
        **Lunghezza delle linee di riferimento**
        
        . {{Version/it|0.21}}

    -   
        **Estensione delle linee di riferimento**
        
        . {{Version/it|0.21}}

    -   
        **Spaziatura testo**
        
        .
-   Premere il pulsante **<img src="images/Draft_SetStyle.svg" width=16px> Selezionato** per applicare le impostazioni agli oggetti o ai gruppi selezionati. Gli oggetti possono essere selezionati mentre il pannello delle attività è aperto.
-   Premere il pulsante **<img src="images/Draft_Text.svg" width=16px> Annotazioni** per applicare le impostazioni a tutti i [Testi](Draft_Text/it.md), [Quote](Draft_Dimension.md) e [ Etichette](Draft_Label.md) nel documento corrente. {{Version/it|0.21}}
-   Premere il pulsante **Annulla** per terminare il comando senza salvare le impostazioni.



## Note

-   Le impostazioni nella sezione **Forme**, eccetto **Stile disegno** e **Modalità di visualizzazione**, non vengono utilizzate solo per gli oggetti Draft, ma anche per gli oggetti creati con altri ambienti di lavoro.
-   Tutte le impostazioni, eccetto **Stile di disegno** e **Modalità di visualizzazione**, possono essere modificate anche nelle preferenze. Vedere [Preferenze PartDesign](PartDesign_Preferences/it#Shape_appearance.md) e [Preferenze Draft](Draft_Preferences/it#Testi_e_quotature.md).
-   Gli stili vengono salvati in un file con un nome fisso: **StylePresets.json** che è archiviato nella cartella utente **Draft** dell\'utente di FreeCAD:
    -   Su Linux solitamente è **/home/<nomeutente>/.local/share/FreeCAD/Draft/**.
    -   Su Windows è **%APPDATA%\FreeCAD\Draft\**, che solitamente è **C:\Users\<nomeutente>\Appdata\Roaming\FreeCAD\Draft\**.
    -   Su macOS di solito è **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/it
