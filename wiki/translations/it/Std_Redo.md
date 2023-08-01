---
- GuiCommand:
   Name:Std_Redo
   Name/it:Ripristina
   MenuLocation:Modifica → Ripristina
   Workbenches:Tutti
   Shortcut:**Ctrl**+**Y**
   SeeAlso:[Annulla](Std_Undo/it.md)
---

# Std Redo/it

## Descrizione

Il comando **Ripristina** inverte l\'azione del comando [Annulla](Std_Undo/it.md).

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_Redo.svg" width=16px> Ripristina**.
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_Redo.svg" width=16px> Ripristina** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**Y**.

## Opzioni

-   Per ripristinare più azioni, fare clic sulla freccia nera a destra del pulsante **<img src="images/Std_Redo.svg" width=16px> Ripristina** e selezionare dall\'elenco.

## Preferenze

-   La funzione Annulla o Ripristina può essere disabilitata impostando **Strumenti → Modifica parametri ... → BaseApp → Preferenze → Documento → UsingUndo** su `False`, ma questo non è raccomandato. Questa impostazione può anche essere modificata nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).
-   Il numero massimo di passaggi di Annulla o Ripristina è controllato da **Strumenti → Modifica parametri ... → BaseApp → Preferenze → Documento → MaxUndoSize**. Questa impostazione può anche essere modificata nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per ripristinare un\'azione che è stata appena annullata, utilizzare il metodo `redo` dell\'oggetto documento.


```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Redo/it
