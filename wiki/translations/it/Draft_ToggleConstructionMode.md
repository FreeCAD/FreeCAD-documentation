---
 GuiCommand:
   Name: Draft ToggleConstructionMode
   Name/it: Modalità Costruzione
   MenuLocation: Utilità , Attiva/Disattiva modalità di costruzione
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Shortcut: **C** **M**
   SeeAlso: Draft_AddConstruction/it
---

# Draft ToggleConstructionMode/it



## Descrizione

Il comando <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Draft Attiva/Disattiva modalità di costruzione** attiva o disattiva la modalità di costruzione Draft. Se la modalità di costruzione è su nuovi oggetti [Draft](Draft_Workbench/it.md), eccetto [Draft Punti](Draft_Point/it.md), vengono posizionati in un gruppo dedicato e dotati di un colore predefinito. Questa funzione è destinata alla geometria di costruzione, spesso temporanea, utilizzata per fornire nuovi [punti di aggancio](Draft_Snap/it.md) per la creazione di altri oggetti. Quando la geometria di costruzione non è più necessaria, il gruppo di costruzione può essere facilmente [nascosto](Std_HideSelection/it.md) o [eliminato](Std_Delete/it.md).

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Geometria di costruzione, in blu, utilizzata per determinare il centro e il raggio di un cerchio*



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Attiva/Disattiva modalità di costruzione](Draft_ToggleConstructionMode/it.md)** nel [Vassoio di Draft](Draft_Tray/it.md). Questo pulsante è premuto se la modalità di costruzione Draft è attualmente attiva.
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Attiva/Disattiva modalità di costruzione** dal menu.
    -   Usare la scorciatoia da tastiera: **C** poi **M**.
2.  Il pulsante nel [Vassoio di Draft](Draft_Tray.md) viene aggiornato.



## Note

-   Se la modalità di costruzione Draft è attivata, il [layer](Draft_Layer/it.md) attivo viene ignorato.



## Preferenze

-   Per cambiare l\'etichetta del gruppo di costruzione: **Modifica → Preferenze... → Draft → Generale → Etichetta gruppo di Costruzione**.
-   Per cambiare il colore utilizzato: **Modifica → Preferenze... → Draft → Generale → Colore della geometria di costruzione**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/it
