---
 GuiCommand:
   Name: Std_ProjectInfo
   Name/it: Informazioni sul progetto
   MenuLocation: File , Informazioni documento...
   Workbenches: Tutti
   SeeAlso: Std_New/it
---

# Std ProjectInfo/it



## Descrizione

Il comando **Informazioni sul progetto** mostra una finestra di dialogo con i dettagli relativi al documento attivo. Alcune di queste informazioni possono essere modificate.



## Utilizzo

1.  Selezionare l\'opzione **File → <img src="images/Std_ProjectInfo.svg" width=16px> Informazioni documento...** dal menu.
2.  Viene visualizzata una finestra di dialogo con le seguenti informazioni:
    -   **Nome**: Il nome del documento. Corrisponde alla proprietà Label del documento. *Non modificabile.*
    -   **Percorso**: Il percorso completo del file. Vuoto se il file non è stato salvato. *Non modificabile.*
    -   **UUID**: FreeCAD inserisce automaticamente un valore di checksum. *Non modificabile.*
    -   **Versione del programma**: La versione di FreeCAD utilizzata per salvare il file. Vuoto se il file non è stato salvato. *Non modificabile.*
    -   **Sistema di unità**: Il sistema di unità del documento. *Il valore iniziale dipende dal [Sistema di unità predefinito](Preferences_Editor/it#Generale_2.md).* {{Version/it|1.0}}
    -   **Creato da**: inserire il nome dell\'autore. *Può essere preimpostato.*
    -   **Data di creazione**: FreeCAD inserisce automaticamente la data corretta. *Non modificabile.*
    -   **Ultima modifica di**: inserire il nome dell\'autore. *Può essere preimpostato.*
    -   **Data dell\'ultima modifica**: FreeCAD inserisce automaticamente la data corretta. *Non modificabile.*
    -   **Azienda**: inserire il nome dell\'azienda. *Può essere preimpostato.*
    -   **Informazioni sulla licenza**: selezionare una licenza dal menu a discesa. *Può essere preimpostato.*
    -   **URL licenza**: L\'URL cambierà con la licenza selezionata, ma può essere sovrascritto. *Può essere preimpostato.*
    -   **Commento**: inserire eventuali commenti applicabili.
3.  Inserire le informazioni richieste e premere il pulsante **OK**.



## Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Preferenze

Vedere anche: [Editor delle Preferenze](Preferences_Editor/it.md).

-   Alcune proprietà del documento: nome dell\'autore, nome dell\'azienda e informazioni sulla licenza, possono essere preimpostate: **Modifica → Preferenze... → Generale → Documento → Diritti d'autore e Licenza**.



---
⏵ [documentation index](../README.md) > Std ProjectInfo/it
