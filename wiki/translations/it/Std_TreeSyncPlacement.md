---
- GuiCommand:
   Name: Std_TreeSyncPlacement
   Name/it: Sincronizza la posizione
   MenuLocation: Visualizza -> Azioni della vista ad albero -> Sincronizza la posizione
   Workbenches: Tutti
   Shortcut: **T** **3**
   Version: 0.19
---

# Std TreeSyncPlacement/it



## Descrizione

Il comando **Sincronizza la posizione** attiva la modalità SyncPlacement della [vista ad albero](Tree_view/it.md). Se questa modalità è attiva, il posizionamento **Placement** degli oggetti viene regolato automaticamente quando essi vengono trascinati e rilasciati da un contenitore in un altro contenitore con un sistema di coordinate diverso, preservandone il posizionamento rispetto al sistema di coordinate globale.



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Fare clic sulla freccia nera in basso a destra del pulsante **<img src="images/Std_TreeSyncView.svg" width=16px>** e selezionare l\'opzione **Sincronizza posizionamento** dal riquadro a comparsa. Nota: l\'immagine del pulsante cambierà a seconda dell\'opzione selezionata.
    -   Selezionare l\'opzione **Visualizza → Azioni della vista ad albero → <img src="images/Std_TreeSyncPlacement.svg" width=16px> Sincronizza posizionamento** dal menu.
    -   Usare la scorciatoia da tastiera: **T** poi **3**.



## Preferenze

La modalità Sincronizza la posizione è memorizzata: **Strumenti → Modifica parametri... → BaseApp → Preferences → TreeView → SyncPlacement**. È un valore booleano, il valore predefinito è `False`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeSyncPlacement/it
