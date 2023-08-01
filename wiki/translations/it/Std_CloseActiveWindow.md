---
- GuiCommand:/it
   Name:Std_CloseActiveWindow
   Name/it:Chiudi
   MenuLocation:File → Chiudi
   Workbenches:Tutti
   Shortcut:**Ctrl**+**F4**
   SeeAlso:[Chiudi tutto](Std_CloseAllWindows/it.md)
---

# Std CloseActiveWindow/it



## Descrizione

Il comando **Chiudi** chiude la finestra attiva. Per chiudere un documento, tutte le sue finestre devono essere chiuse.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare **File →  <img src="images/Std_CloseActiveWindow.svg" width=16px> Chiudi** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**F4**.
2.  Per chiudere un documento: ripetere questo per tutte le finestre che appartengono al documento.
3.  Quando si chiude l\'ultima finestra di un documento che non è stato salvato, una finestra di dialogo chiede se si vuole salvarlo:
    -   Premere il pulsante **Salva**. Se necessario, inserire prima un nome per il file.
    -   Premere il pulsante **Tralascia** per eliminare il documento e perdere tutte le modifiche.



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





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std CloseActiveWindow/it
