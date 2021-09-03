---
- GuiCommand:/it
   Name:Std_TreeMultiDocument
   Name/it:Multi documento
   MenuLocation:Visualizza → Azioni della vista ad albero → Multi documento
   Workbenches:Tutti
   SeeAlso:[Documento singolo](Std_TreeSingleDocument/it.md), [Comprimi/espandi](Std_TreeCollapseDocument/it.md)
---


</div>

## Descrizione

Il comando **Multi documento** imposta DocumentMode della [vista ad albero](Tree_view/it.md) su MultiDocument. In questa modalità tutti i documenti sono visibili nella vista ad albero e si possono espandere più documenti. Le altre modalità sono [Documento singolo](Std_TreeSingleDocument/it.md) e [Comprimi/espandi](Std_TreeCollapseDocument/it.md).

## Utilizzo

1.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the {{MenuCommand|Multi document}} option from the flyout. Note: the button image will change depending on the selected option.
    -   Select the {{MenuCommand|View → TreeView actions → <img src="images/Std_TreeMultiDocument.svg" width=16px> Multi document}} option from the menu.

## Preferenze

The Tree view DocumentMode mode is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → TreeView → DocumentMode}}. It is an integer value. Possible values are `0` (SingleDocument), `1` (MultiDocument) or `2` (CollapseDocument). The default is `2`.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
