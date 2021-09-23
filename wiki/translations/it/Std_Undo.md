---
- GuiCommand:/it
   Name:Std_Undo
   Name/it:Annulla
   MenuLocation:Modifica → Annulla
   Workbenches:Tutti
   Shortcut:**Ctrl**+**Z**
   SeeAlso:[Ripristina](Std_Redo/it.md)
---

# Std Undo/it

## Descrizione

Il comando **Annulla** annulla l\'ultima azione.

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_Undo.svg" width=16px> Annulla**.
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_Undo.svg" width=16px> Annulla** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**Z**.

## Opzioni


<div class="mw-translate-fuzzy">

-   Per annullare più azioni, fare clic sulla freccia nera a destra del pulsante **<img src="images/Std_Undo.svg" width=16px> Annulla** e selezionare dall\'elenco.


</div>

## Preferenze

-   La funzione Annulla o Ripristina può essere disabilitata impostando **Strumenti → Modifica parametri ... → BaseApp → Preferenze → Documento → UsingUndo** su `False`, ma questo non è raccomandato. Questa impostazione può anche essere modificata nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).
-   Il numero massimo di passaggi di Annulla o Ripristina è controllato da **Strumenti → Modifica parametri ... → BaseApp → Preferenze → Documento → MaxUndoSize**. Questa impostazione può anche essere modificata nell\'[editor delle preferenze](Preferences_Editor/it#Documento.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per annullare l\'ultima azione, utilizzare il metodo `undo` dell\'oggetto documento.


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std Undo/it
