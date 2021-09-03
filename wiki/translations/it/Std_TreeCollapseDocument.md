---
- GuiCommand:/it
   Name:Std_TreeCollapseDocument
   Name/it:Comprimi/espandi
   MenuLocation:Visualizza → Azioni della vista ad albero → Comprimi/espandi
   Workbenches:Tutti
   SeeAlso:[Documento singolo](Std_TreeSingleDocument/it.md), [Multi documento](Std_TreeMultiDocument/it.md)
---


</div>

## Descrizione

Il comando **Comprimi/espandi** imposta DocumentMode della [vista ad albero](Tree_view/it.md) su CollapseDocument. In questa modalità, l\'attivazione di una [vista 3D](3D_view/it.md) di un documento espande automaticamente quel documento nella vista ad albero e comprime tutti gli altri documenti. Le altre modalità sono [Documento singolo](Std_TreeSingleDocument/it.md) e [Multi documento](Std_TreeMultiDocument/it.md).

## Utilizzo

1.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the {{MenuCommand|Collapse/Expand}} option from the flyout. Note: the button image will change depending on the selected option.
    -   Select the {{MenuCommand|View → TreeView actions → <img src="images/Std_TreeCollapseDocument.svg" width=16px> Collapse/Expand}} option from the menu.

## Preferenze

The Tree view DocumentMode mode is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → TreeView → DocumentMode}}. It is an integer value. Possible values are `0` (SingleDocument), `1` (MultiDocument) or `2` (CollapseDocument). The default is `2`.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
