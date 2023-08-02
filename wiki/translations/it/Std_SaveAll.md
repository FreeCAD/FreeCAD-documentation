---
- GuiCommand:
   Name: Std_SaveAll
   Name/it: Salva tutto
   MenuLocation: File -> Salva tutto
   Workbenches: Tutti
   SeeAlso: Std_Save/it
---

# Std SaveAll/it



## Descrizione

Il comando **Salva tutto** salva tutti i documenti aperti.



## Utilizzo

1.  Selezionare l\'opzione **File → <img src="images/Std_SaveAll.svg" width=16px> Salva tutto** dal menu.
2.  Per i nuovi documenti: immettere un nome file nella finestra di dialogo e premere il pulsante **Salva**.



## Opzioni

-   Per i nuovi documenti: premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.



## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per salvare un documento, utilizzare il metodo `save` dell\'oggetto documento. Un nuovo documento deve prima essere salvato con il metodo `saveAs` dell\'oggetto documento. Per un esempio di scripting vedere [Nuovo](Std_New/it.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SaveAll/it
