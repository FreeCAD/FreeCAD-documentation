---
 GuiCommand:
   Name: Std_BoxElementSelection
   Name/it: Seleziona elementi
   MenuLocation: Modifica , Box di selezione di elementi
   Workbenches: Tutti
   Shortcut: **Shift**+**E**
   SeeAlso: Part BoxSelection/it, Std_BoxSelection/it, 
Std_SelectAll/it 
---

# Std BoxElementSelection/it



## Descrizione

Il comando **Box di selezione di elementi** seleziona le facce in un\'area rettangolare definita dall\'utente, una casella, nella vista 3D.

Si noti che se un intero oggetto rientra nel rettangolo, viene selezionato l\'oggetto stesso, anziché le sue facce. Per evitare ciò, creare due selezioni di riquadri per ciascun oggetto (tenendo premuto **Ctrl** mentre si trascina il 2° rettangolo), oppure utilizzare il comando [Part Box di selezione](Part_BoxSelection/it.md).



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare **Modifica → <img src="images/Std_BoxElementSelection.svg" width=16px> Box di selezione di elementi** dal menu.
    -   Usare la scorciatoia da tastiera: **Maiusc**+**E**.
2.  Effettuare una delle seguenti operazioni:
    -   Trascinare un rettangolo da sinistra a destra per selezionare le facce il cui centro geometrico si trova all\'interno del rettangolo.
    -   Trascinare un rettangolo da destra a sinistra per selezionare le facce che si trovano (parzialmente) all\'interno del rettangolo o che saranno da lui toccate.



## Note

-   Utilizzare il comando [Box di selezione](Std_BoxSelection/it.md) per selezionare gli oggetti anziché le facce.
-   Questo comando non può essere utilizzato per selezionare elementi in uno schizzo. Vedere [Sketcher](Sketcher_Workbench/it#Metodi_di_selezione.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std BoxElementSelection/it
