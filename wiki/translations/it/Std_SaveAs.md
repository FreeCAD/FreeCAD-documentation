---
- GuiCommand:
   Name: Std_SaveAs
   Name/it: Salva con nome
   MenuLocation: File -> Salva con nome...
   Workbenches: Tutti
   SeeAlso: Std_SaveCopy/it, Std_Save/it
---

# Std SaveAs/it



## Descrizione

Il comando **Salva con nome** salva il documento attivo con un nuovo nome di file.



## Utilizzo

1.  Selezionare **File →  <img src="images/Std_SaveAs.svg" width=16px> Salva con nome...** nel menu.
2.  Immettere un nome per il file nella finestra di dialogo.
3.  Premere il pulsante **Salva**.



## Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Note

-   Questo comando può essere utilizzato anche per salvare i grafici delle dipendenze. Vedere [Grafico delle dipendenze](Std_DependencyGraph/it.md).



## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per salvare un documento con un nuovo nome, utilizzare il metodo `saveAs` dell\'oggetto documento. Per un esempio di scripting vedere [Nuovo](Std_New/it.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SaveAs/it
