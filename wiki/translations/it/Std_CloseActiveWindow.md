---
- GuiCommand:/it
   Name:Std_CloseActiveWindow
   Name/it:Chiudi
   Empty:1
   MenuLocation:File → Chiudi
   Workbenches:Tutti
   Shortcut:**Ctrl**+**F4**
   SeeAlso:[Chiudi tutto](Std_CloseAll/it.md)
---


</div>

## Descrizione

Il comando **Chiudi** chiude la finestra attiva. Per chiudere un documento, tutte le sue finestre devono essere chiuse.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare **File → Chiudi** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**F4**.
2.  Per chiudere un documento: ripetere questo per tutte le finestre che appartengono al documento.
3.  Quando si chiude l\'ultima finestra di un documento che non è stato salvato, una finestra di dialogo chiede se si vuole salvarlo:
    -   Premere il pulsante **Salva** Se necessario, inserire prima un nome per il file.
    -   Premere il pulsante **Tralascia** per eliminare il documento e perdere tutte le modifiche.


</div>

## Opzioni

-   Quando viene visualizzata la finestra di dialogo: premere **Esc** o il pulsante **Annulla** per annullare il comando.

## Note

-   Il comando può solo chiudere le finestre [agganciate](Std_ViewDockUndockFullscreen/it.md).
-   Un documento può anche essere chiuso facendo clic con il pulsante destro del mouse nella [Vista ad albero](Tree_view/it.md) e selezionando **Chiudi il documento** dal menu di scelta rapida.

## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per chiudere un documento usare il metodo `closeDocument` dell\'applicazione FreeCAD. Per un esempio di scripting vedere [Std Nuovo](Std_New/it.md).


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
