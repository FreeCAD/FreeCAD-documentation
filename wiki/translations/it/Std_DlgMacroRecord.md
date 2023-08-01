---
- GuiCommand:/it
   Name:Std_DlgMacroRecord
   Name/it:Registra una macro
   MenuLocation:Macro → Registra una macro ...
   Workbenches:Tutti
   SeeAlso:[Interrompi la registrazione](Std_MacroStopRecord/it.md)
---

# Std DlgMacroRecord/it



## Descrizione

Il comando **Registra una macro** avvia una sessione di registrazione della [macro](Macros/it.md) durante la quale le azioni dell\'utente vengono memorizzate in una macro di FreeCAD, un file con estensione **.FCMacro**. Una macro può essere successivamente riprodotta, eseguita, per ripetere le azioni registrate.

![](images/Std_DlgMacroRecord_dialog.png ) 
*La finestra di dialogo Registrazione macro*



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_DlgMacroRecord.svg" width=16px> [Registra una macro](Std_DlgMacroRecord/it.md)**.
    -   Selezionare l\'opzione **Macro → <img src="images/Std_DlgMacroRecord.svg" width=16px> Registra una macro...** dal menu.
2.  Si apre la finestra di dialogo Registra macro.
3.  Immettere un nome per la macro nella casella di inserimento **Nome macro**.
4.  Opzionalmente cambiare il **Percorso macro** premendo il pulsante **...**.
5.  Il pulsante **Ferma** non funziona in questo momento.
6.  Premere il pulsante **Registra** per chiudere la finestra di dialogo e avviare la sessione di registrazione.
7.  Eseguire le azioni che si desidere registrare.
8.  Per terminare la sessione di registrazione, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Std_MacroStopRecord.svg" width=16px> [Ferma](Std_MacroStopRecord/it.md)**.
    -   Seleziona l\'opzione **Macro → <img src="images/Std_MacroStopRecord.svg" width=16px> Interrompi la registrazione** dal menu.



## Opzioni

-   Quando viene visualizzata la finestra di dialogo Registra macro: premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Per eseguire la macro registrata utilizzare il comando [Esegui la macro](Std_DlgMacroExecute/it.md).
-   Per ulteriori informazioni sulle macro, vedere la pagina [Macro](Macros/it.md).



## Preferenze

-   Il percorso della macro può essere modificato anche nelle preferenze: **Modifica → Preferenze... → Python → Macro → Percorso macro**. Vedi [Editor delle preferenze](Preferences_Editor/it#Macro.md).
-   Nella maggior parte dei casi non è consigliabile registrare azioni che non modificano il modello: in **Modifica → Preferenze... → Python → Macro → Comandi GUI** eseguire una delle seguenti operazioni:
    -   Per escludere queste azioni, deselezionare la casella di controllo {{CheckBox|FALSE|Registra comandi GUI}}.
    -   Per includerli solo come commenti selezionare entrambe le caselle di controllo {{CheckBox|TRUE|Registra comandi GUI}} e {{CheckBox|TRUE|Registra come commento}}.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std DlgMacroRecord/it
