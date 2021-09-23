# Std Open/it
---
- GuiCommand:/it   Name:Std_Open   Name/it:Apri   MenuLocation:File → Apri   Workbenches:Tutti   Shortcut:**Ctrl**+**O**   SeeAlso:[Nuovo](Std_New.md), [Importa](Std_Import/it.md)---

## Descrizione

Il comando **Apri** apre un file. Se il file non è un file FreeCAD nativo (\*.FCStd) la sua geometria viene importata in un nuovo documento. Per ulteriori informazioni vedere [Importa](Std_Import/it.md).

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_Open.svg" width=16px> '''Apri'''**.
    -   Selezionare l\'opzione **File → <img src="images/Std_Open.svg" width=16px> Apri...** dal menu.
    -   Usare la scorciatoia da tastiera: **Ctrl**+**O**.
2.  Facoltativamente, selezionare il formato file corretto nella finestra di dialogo.
3.  Selezionare un file.
4.  Premere il pulsante **Apri**.

## Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.

## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)


<div class="mw-translate-fuzzy">

Per chiudere un documento usare il metodo `open` dell\'applicazione FreeCAD. Per un esempio di scripting vedere [Std Nuovo](Std_New/it.md).


</div>

These methods create and return a document and load a project file into it. The `filepath` argument must be a string pointing to an existing file. If the file doesn\'t exist or the file cannot be loaded an I/O exception is thrown. In this case the created document is kept, but will be empty. If `hidden<nowiki>=</nowiki>True` is used, the document won\'t be displayed in the GUI and no tab will appear for it. This allows performing automatic operations on a document and closing it without disrupting the user interface.

For a scripting example see [Std New](Std_New#Scripting.md).


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std Open/it
