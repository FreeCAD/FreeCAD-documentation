---
- GuiCommand   */it
   Name   *Std_CloseAllWindows
   Name/it   *Chiudi tutto
   Empty   *1
   MenuLocation   *File → Chiudi tutto
   Workbenches   *Tutti
   SeeAlso   *[Chiudi](Std_Close/it.md)
---

# Std CloseAllWindows/it


</div>

## Descrizione

Il comando **Chiudi tutto** chiude tutte le finestre, chiudendo così tutti i documenti.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare **File → Chiudi tutto** dal menu.
2.  Se il documento attivo non è stato salvato, una finestra di dialogo richiederà di salvarlo   *
    -   Premere il pulsante **Salva** Se necessario, inserire prima un nome per il file.
    -   Premere il pulsante **Tralascia** per eliminare il documento e perdere tutte le modifiche.


</div>

## Opzioni

-   Quando viene visualizzata la finestra di dialogo   * premere **Esc** o il pulsante **Annulla** per interrompere il comando.
-   Se sono presenti più documenti non salvati   * selezionare la casella di controllo {{CheckBox|TRUE|Applica la risposta a tutti}} per evitare che venga richiesto separatamente per ogni documento non salvato.

## Note

-   Un documento può anche essere chiuso facendo clic con il pulsante destro del mouse nella [Vista ad albero](Tree_view/it.md) e selezionando **Chiudi il documento** dal menu di scelta rapida.

## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in   * **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script


**Vedere anche   ***

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per chiudere un documento usare il metodo `closeDocument` dell\'applicazione FreeCAD. Per un esempio di scripting vedere [Std Nuovo](Std_New/it.md).


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std CloseAllWindows/it
