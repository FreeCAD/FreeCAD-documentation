---
 GuiCommand:
   Name: Std_DlgMacroExecute
   Name/it: Esegui la macro
   MenuLocation: Macro , Esegui la macro
   Workbenches: Tutti
   SeeAlso: Std_DlgMacroExecuteDirect/it
---

# Std DlgMacroExecute/it



## Descrizione

Il comando **Macro\...** apre la finestra di dialogo Esegui macro. Da questa finestra di dialogo è possibile eseguire, modificare e gestire le macro.

<img alt="" src=images/Std_DlgMacroExecute_dialog.png  style="width:300px;"> 
*La finestra di dialogo Esegui macro*



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_DlgMacroExecute.svg" width=16px> [Macro...](Std_DlgMacroExecute/it.md)**.
    -   Selezionare l\'opzione **Macro → <img src="images/Std_DlgMacroExecute.svg" width=16px> Macro...** dal menu.
2.  Si apre la finestra di dialogo **Esegui macro**. Vedere [Opzioni](#Opzioni.md).



## Opzioni



### Trova file / Trova nei file 

:   
    {{Version/it|1.0}}
    





:   Queste due caselle di input possono essere utilizzate per filtrare le macro dall\'elenco dei file nella scheda **Macro utente** o nella scheda **Macro di sistema**. Si possono utilizzare espressioni regolari o semplicemente inserire testo. Tutte le corrispondenze non fanno distinzione tra maiuscole e minuscole.





:   **Trova file** filtra l\'elenco per nome file. Nell\'elenco verranno visualizzati solo i nomi di file che corrispondono al testo immesso. **Trova nei file** filtra l\'elenco in base al contenuto del file. Nell\'elenco verranno visualizzati solo i file il cui contenuto testuale corrisponde al testo immesso.





:   Rimuove tutto il testo dalla casella di input di un filtro per disabilitarlo. Se entrambe le caselle di input contengono testo, vengono applicati entrambi i filtri. Il filtraggio potrebbe risultare un elenco vuoto.



### Macro utente 

:   La scheda **Macro utente** elenca le macro disponibili nella **Posizione macro utente**.

1.  Fare clic su una macro nell\'elenco per selezionarla.
2.  Il nome della macro selezionata apparirà nella casella **Nome macro**.



### Macro di sistema 

:   Per utilizzare la scheda **Macro di sistema** è necessario creare una cartella denominata **Macro** come cartella gemella della cartella **bin** in cui è installato FreeCAD e inserire all\'interno alcune macro.





:   Per trovare la cartella **bin** inserire questo nella [Console Python](Python_console/it.md):





:   
    
```python
    App.getHomePath()
    
```
    

1.  Fare clic su una macro nell\'elenco per selezionarla.
2.  Il nome della macro selezionata apparirà nella casella **Nome macro**.



### Posizione delle macro utente 

1.  Premere il pulsante **...** per modificare la posizione delle macro utente.
2.  Passare ad una cartella diversa e selezionala.



### Eseguire

1.  Per eseguire una macro, eseguire una delle seguenti operazioni:
    -   Selezionare la macro nell\'elenco e premere il pulsante **Esegui**.
    -   Fare doppio clic sulla macro nell\'elenco.
2.  La finestra di dialogo si chiude.
3.  La macro viene eseguita.



### Chiudi

1.  Premere **Esc** o il pulsante **Chiudi** per chiudere la finestra di dialogo.



### Crea

1.  Premere il pulsante **Crea** per creare un nuovo file macro.
2.  Immettere un nome nella finestra di dialogo che si apre. Non è necessario includere l\'estensione **.FCMacro**.
3.  Premere **Enter** o il pulsante **OK**.
4.  Entrambe le finestre di dialogo si chiudono.
5.  Il nuovo file viene aperto nell\'editor Macro.



### Elimina

1.  Selezionare la macro che si desidera eliminare nell\'elenco.
2.  Premere il pulsante **Elimina**.
3.  Premere il pulsante **Si** nella finestra di dialogo di conferma che si apre.



### Modifica

1.  Selezionare la macro che si desidera modificare nell\'elenco.
2.  Premere il pulsante **Modifica**.
3.  La finestra di dialogo si chiude.
4.  Il file selezionato viene aperto nell\'editor Macro.



### Rinomina

1.  Selezionare la macro che si desidera rinominare nell\'elenco.
2.  Premere il pulsante **Rinomina**.
3.  Immettere un nuovo nome nella finestra di dialogo che si apre. Non è necessario includere l\'estensione **.FCMacro**.
4.  Premere **Enter** o il pulsante **OK**.



### Duplica

1.  Selezionare la macro che si desidera duplicare nell\'elenco.
2.  Premere il pulsante **Duplica**.
3.  Immettere un nuovo nome nella finestra di dialogo che si apre. Non è necessario includere l\'estensione **.FCMacro**.
4.  Premere **Enter** o il pulsante **OK**.



### Barra degli strumenti 

1.  Selezionare la macro che si desidera aggiungere a una barra degli strumenti personalizzata nell\'elenco.
2.  Premere il pulsante **Barra degli strumenti**.
3.  Due finestre di dialogo \"procedura dettagliata\" guideranno attraverso i passaggi richiesti. Vedere [Personalizzazione dell\'interfaccia](Interface_Customization/it.md) per ulteriori informazioni.

### Download

1.  Premere il pulsante **Download** per avviare [Addon manager](Std_AddonMgr/it.md).



## Note

-   Per ulteriori informazioni sulle macro, vedere la pagina [Macro](Macros/it.md).



## Preferenze

Vedere anche: [Editor delle Preferenze](Preferences_Editor/it.md).

-   La posizione delle macro utente può anche essere modificata nelle preferenze: **Modifica → Preferenze... → Python → Macro → Percorso macro**.



---
⏵ [documentation index](../README.md) > Std DlgMacroExecute/it
