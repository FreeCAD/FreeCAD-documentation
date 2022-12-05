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

Per aprire un documento usare il metodo `open(filepath)` o il metodo `openDocument(filepath, [hidden<nowiki>=</nowiki>False])` dell\'applicazione FreeCAD.

Questi metodi creano e restituiscono un documento e vi caricano un file di progetto. L\'argomento `filepath` deve essere una stringa che punta a un file esistente. Se il file non esiste o non è possibile caricare il file, viene generata un\'eccezione di I/O. In questo caso il documento creato viene conservato, ma sarà vuoto. Se viene utilizzato `hidden<nowiki>=</nowiki>True`, il documento non verrà visualizzato nella GUI e non verrà visualizzata alcuna scheda. Ciò consente di eseguire operazioni automatiche su un documento e chiuderlo senza interrompere l\'interfaccia utente.

Per esempi di scripting vedere [Nuovo](Std_New/it#Scripting.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Open/it
