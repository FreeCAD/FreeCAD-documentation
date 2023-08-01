---
- GuiCommand:
   Name: Std_TreeMultiDocument
   Name/it: Multi documento
   MenuLocation: Visualizza - Azioni della vista ad albero - Multi documento
   Workbenches: Tutti
   Version: 0.19
   SeeAlso: [Documento singolo](Std_TreeSingleDocument/it.md), [Comprimi/espandi](Std_TreeCollapseDocument/it.md)
---

# Std TreeMultiDocument/it



## Descrizione

Il comando **Multi documento** imposta DocumentMode della [vista ad albero](Tree_view/it.md) su MultiDocument. In questa modalità tutti i documenti sono visibili nella vista ad albero e si possono espandere più documenti. Le altre modalità sono [Documento singolo](Std_TreeSingleDocument/it.md) e [Comprimi/espandi](Std_TreeCollapseDocument/it.md).



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Fare clic sulla freccia nera in basso a destra del pulsante **<img src="images/Std_TreeSyncView.svg" width=16px>** e selezionare l\'opzione **Multi documento** dal riquadro a comparsa. Nota: l\'immagine del pulsante cambierà a seconda dell\'opzione selezionata.
    -   Selezionare l\'opzione **Visualizza → Azioni della vista ad albero → <img src="images/Std_TreeMultiDocument.svg" width=16px> Multi documento** dal menu.



## Preferenze

La modalità DocumentMode della vista ad albero è memorizzata: **Strumenti → Modifica parametri... → BaseApp → Preferences → TreeView → DocumentMode**. È un valore intero. I valori possibili sono `0` (SingleDocument), `1` (MultiDocument) o `2` (CollapseDocument). Il valore predefinito è `2`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeMultiDocument/it
