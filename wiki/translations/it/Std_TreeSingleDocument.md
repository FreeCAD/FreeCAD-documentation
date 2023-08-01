---
- GuiCommand:/it
   Name:Std_TreeSingleDocument
   Name/it:Documento singolo
   MenuLocation:Visualizza → Azioni della vista ad albero → Documento singolo
   Workbenches:Tutti
   Version:0.19
   SeeAlso:[Multi documento](Std_TreeMultiDocument/it.md), [Comprimi/espandi](Std_TreeCollapseDocument/it.md)
---

# Std TreeSingleDocument/it



## Descrizione

Il comando **Documento singolo** imposta DocumentMode della [vista ad albero](Tree_view/it.md) su SingleDocument. In questa modalità è visibile solo un singolo documento nella vista ad albero. Le altre modalità sono [Multi documento](Std_TreeMultiDocument/it.md) e [Comprimi/espandi](Std_TreeCollapseDocument/it.md).

Nella modalità Documento singolo è possibile passare a un altro documento attivando una vista 3D appartenente a quel documento. Si attivarlo tramite l\'[area di visualizzazione principale](Main_view_area/it.md) o tramite il menu **Finestre**.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Fare clic sulla freccia nera in basso a destra del pulsante **<img src="images/Std_TreeSyncView.svg" width=16px>** e selezionare l\'opzione **Documento singolo** dal riquadro a comparsa. Nota: l\'immagine del pulsante cambierà a seconda dell\'opzione selezionata.
    -   Selezionare l\'opzione **Visualizza → Azioni della vista ad albero → <img src="images/Std_TreeSingleDocument.svg" width=16px> Documento singolo** dal menu.



## Preferenze

La modalità DocumentMode della vista ad albero è memorizzata: **Strumenti → Modifica parametri... → BaseApp → Preferences → TreeView → DocumentMode**. È un valore intero. I valori possibili sono `0` (SingleDocument), `1` (MultiDocument) o `2` (CollapseDocument). Il valore predefinito è `2`.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std TreeSingleDocument/it
