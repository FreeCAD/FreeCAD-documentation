---
- GuiCommand   */it
   Name   *Std_Export
   Name/it   *Esporta
   Empty   *1
   MenuLocation   *File → Esporta...
   Workbenches   *All
   Shortcut   ***Ctrl**+**E**
   SeeAlso   *[Esporta PDF](Std_PrintPdf/it.md), [Importazione e Esportazione](Import_Export/it.md), [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md)
---

# Std Export/it


</div>

## Descrizione

Il comando **Esporta** esporta gli oggetti selezionati in un formato file diverso. Sono supportati molti formati di file e per alcuni formati esistono più opzioni di esportazione. Vedere [Importazione e esportazionet](Import_Export/it.md) per ulteriori informazioni.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare uno o più oggetti. Per evitare l\'esportazione di oggetti invisibili o duplicati   *
    -   Fare attenzione quando si usa **Ctrl** + **A** per selezionare tutti gli oggetti. Questo seleziona anche oggetti invisibili.
    -   Selezionare un [Corpo di PartDesign](PartDesign_Body/it.md) selezionando solo il corpo stesso o la sua ultima funzione.
    -   Selezionare un [Gruppo](Std_Group/it.md) o una [Parte](Std_Part/it.md) selezionando solo l\'oggetto genitore stesso o gli oggetti nidificati al suo interno.
    -   Non utilizzare il comando [Seleziona tutto](Std_SelectAll/it.md) in quanto selezionerà anche i sotto-elementi dei corpi di PartDesign.
    -   Per lo stesso motivo, il comando [Box di selezione](Std_BoxSelection/it.md) dovrebbe essere evitato nelle versioni 0.18 e precedenti di FreeCAD.
2.  Esistono diversi modi per invocare il comando   *
    -   Selezionare l\'opzione **File → Esporta...** dal menu.
    -   Usare la scorciatoia da tastiera   * **Ctrl**+**E**.
3.  Selezionare il formato file corretto nella finestra di dialogo.
4.  Inserire un nome file.
5.  Premere il pulsante **Salva**.


</div>

## Opzioni

-   Premere il tasto **Esc** o il pulsante **Annulla** per annullare il comando.

## Note

-   Per esportare un [oggetto mesh](Mesh_Workbench/it.md) come solido, bisogna prima convertirlo. Vedere il tutorial [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md).
-   Alcuni ambienti hanno comandi di esportazione aggiuntivi. Vedere   * [Importazione e esportazione](Import_Export/it.md).

## Preferenze

-   Vedere [Preferenze di Importa e esporta](Import_Export_Preferences/it.md).
-   L\'ultima posizione del file utilizzato è memorizzata in   * {{MenuCommand | Strumenti → Modifica parametri ... → BaseApp → Preferenze → Generale → FileOpenSavePath}}.
-   L\'ultimo filtro di esportazione utilizzato è memorizzato in   * {{MenuCommand | Strumenti → Modifica parametri ... → BaseApp → Preferenze → Generale → FileExportFilter}}.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  

[Category   *File\_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/it
