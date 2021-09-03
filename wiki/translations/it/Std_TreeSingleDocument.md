---
- GuiCommand:/it
   Name:Std_TreeSingleDocument
   Name/it:Documento singolo
   MenuLocation:Visualizza → Azioni della vista ad albero → Documento singolo
   Workbenches:Tutti
   SeeAlso:[Multi documento](Std_TreeMultiDocument/it.md), [Comprimi/espandi](Std_TreeCollapseDocument/it.md)
---


</div>

## Descrizione

Il comando **Documento singolo** imposta DocumentMode della [vista ad albero](Tree_view/it.md) su SingleDocument. In questa modalità è visibile solo un singolo documento nella vista ad albero. Le altre modalità sono [Multi documento](Std_TreeMultiDocument/it.md) e [Comprimi/espandi](Std_TreeCollapseDocument/it.md).

Nella modalità Documento singolo è possibile passare a un altro documento attivando una vista 3D appartenente a quel documento. Si attivarlo tramite l\'[area di visualizzazione principale](Main_view_area/it.md) o tramite il menu **Finestre**.

## Utilizzo

1.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the **Single document** option from the flyout. Note: the button image will change depending on the selected option.
    -   Select the **View → TreeView actions → <img src="images/Std_TreeSingleDocument.svg" width=16px> Single document** option from the menu.

## Preferenze

The Tree view DocumentMode mode is stored: **Tools → Edit parameters... → BaseApp → Preferences → TreeView → DocumentMode**. It is an integer value. Possible values are `0` (SingleDocument), `1` (MultiDocument) or `2` (CollapseDocument). The default is `2`.


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
