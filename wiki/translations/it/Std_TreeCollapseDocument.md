---
- GuiCommand:/it
   Name:Std_TreeCollapseDocument
   Name/it:Comprimi/Espandi
   MenuLocation:Visualizza → Azioni della vista ad albero → Comprimi/Espandi
   Workbenches:Tutti
   Version:0.19
   SeeAlso:[Documento singolo](Std_TreeSingleDocument/it.md), [Multi documento](Std_TreeMultiDocument/it.md)
---

# Std TreeCollapseDocument/it



## Descrizione

Il comando **Comprimi/espandi** imposta DocumentMode della [vista ad albero](Tree_view/it.md) su CollapseDocument. In questa modalità, l\'attivazione di una [vista 3D](3D_view/it.md) di un documento espande automaticamente quel documento nella vista ad albero e comprime tutti gli altri documenti. Le altre modalità sono [Documento singolo](Std_TreeSingleDocument/it.md) e [Multi documento](Std_TreeMultiDocument/it.md).



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Fare clic sulla freccia nera in basso a destra del pulsante **<img src="images/Std_TreeSyncView.svg" width=16px>** e selezionare l\'opzione **Comprimi/Espandi** dal riquadro a comparsa. Nota: l\'immagine del pulsante cambierà a seconda dell\'opzione selezionata.
    -   Selezionare l\'opzione **Visualizza → Azioni della vista ad albero → <img src="images/Std_TreeCollapseDocument.svg" width=16px> Comprimi/Espandi** dal menu.



## Preferenze

La modalità DocumentMode della vista ad albero è memorizzata: **Strumenti → Modifica parametri... → BaseApp → Preferences → TreeView → DocumentMode**. È un valore intero. I valori possibili sono `0` (SingleDocument), `1` (MultiDocument) o `2` (CollapseDocument). Il valore predefinito è `2`.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TreeCollapseDocument/it
