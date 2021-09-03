---
- GuiCommand:/it
   Name:Std_DlgMacroRecord
   Name/it:Registra una macro
   MenuLocation:Macro → Registra una macro ...
   Workbenches:Tutti
   SeeAlso:[Interrompi la registrazione](Std_MacroStopRecord/it.md)
---

## Descrizione

Il comando **Registra una macro** avvia una sessione di registrazione della [macro](Macros/it.md) durante la quale le azioni dell\'utente vengono memorizzate in una macro di FreeCAD, un file con estensione {{FileName|.FCMacro}}. Una macro può essere successivamente riprodotta, eseguita, per ripetere le azioni registrate.

![](images/Std_DlgMacroRecord_dialog.png ) *La finestra di dialogo Registrazione macro*

## Utilizzo


<div class="mw-translate-fuzzy">

La funzione è accessibile tramite **Macro → Registra macro ...**, oppure tramite il pulsante **<img src=images/Std_DlgMacroRecord.png style="width:16px"> Registra macro** della barra degli strumenti delle macro <img alt="" src=images/Macros_toolbar.jpg  style="width:96px;">.


</div>

## Options

-   When the Macro recording dialog box is displayed: press **Esc** or the **Cancel** button to abort the command.

## Notes

-   To execute the recorded macro use the [Std DlgMacroExecute](Std_DlgMacroExecute.md) command.
-   To learn more about macros see the [Macros](Macros.md) page.

## Preferences

-   The macro path can also be changed in the preferences: **Edit → Preferences... → General → Macro → Macro path**. See [Preferences Editor](Preferences_Editor#Macro.md).
-   In most cases it is undesirable to record actions that do not change the model: under **Edit → Preferences... → General → Macro → GUI commands** do one of the following:
    -   To exclude these actions uncheck the {{CheckBox|FALSE|Record GUI commands}} checkbox.
    -   To include them as comments only check both the {{CheckBox|TRUE|Record GUI commands}} and {{CheckBox|TRUE|Record as comment}} checkboxes.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
