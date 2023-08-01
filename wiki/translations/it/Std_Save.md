---
- GuiCommand:/it
   Name:Std_Save
   Name/it:Salva
   MenuLocation:File → Salva
   Workbenches:Tutti
   Shortcut:**Ctrl**+**S**
   SeeAlso:[Salva con nome](Std_SaveAs/it.md), [Salva una copia](Std_SaveCopy/it.md), [Salva tutto](Std_SaveAll/it.md)
---

# Std Save/it



## Descrizione

Il comando **Salva** salva il documento attivo.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_Save.svg" width=16px> '''Salva'''**.
    -   Selezionare l\'opzione **File → <img src="images/Std_Save.svg" width=16px> Salva** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**S**.
2.  Per i nuovi documenti: immettere un nome file nella finestra di dialogo e premere il pulsante **Salva**.



## Opzioni

-   Per i nuovi documenti: premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Note

-   Questo comando può essere utilizzato anche per salvare i grafici delle dipendenze. Vedere [Grafico delle dipendenze](Std_DependencyGraph/it.md).



## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per salvare un documento, utilizzare il metodo `save` dell\'oggetto documento. Un nuovo documento deve prima essere salvato con il metodo `saveAs` dell\'oggetto documento. Per un esempio di scripting vedere [Nuovo](Std_New/it.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Save/it
