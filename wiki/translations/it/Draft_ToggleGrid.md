---
 GuiCommand:
   Name: Draft ToggleGrid
   Name/it: Draft Attiva/disattiva Griglia
   MenuLocation: Utilità , Attiva/disattiva Griglia<br>Aggancio , Attiva/disattiva Griglia
   Workbenches: Draft_Workbench/it, BIM_Workbench/it
   Shortcut: **G** **R**
   SeeAlso: Draft_Snap_Grid/it, Draft_SelectPlane/it
---

# Draft ToggleGrid/it



## Descrizione

Il comando <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> **Draft Attiva/disattiva Griglia** modifica la visibilità della griglia.


{{Version/it|1.0}}

: Ogni [Vista 3D](3D_view/it.md) ha la propria griglia che può essere sempre visibile, visibile solo durante i comandi o invisibile. La visibilità iniziale della griglia nelle nuove visualizzazioni dipende dalle [preferenze](#Preferenze.md).



## Utilizzo

1.  Il comando può essere utilizzato mentre è attivo un altro comando.
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Draft_ToggleGrid.svg" width=16px> [Attiva/disattiva Griglia](Draft_ToggleGrid.md)** nella barra degli strumenti di aggancio di Draft.
    -   [Draft](Draft_Workbench/it.md): Premere il pulsante **<img src="images/Draft_ToggleGrid.svg" width=16px> [Attiva/disattiva Griglia](Draft_ToggleGrid.md)** nel [Draft snap widget](Draft_snap_widget/it.md).
    -   Draft: Selezionare l\'opzione **Utilità → <img src="images/Draft_ToggleGrid.svg" width=16px> Attiva/disattiva griglia** dal menu o dalla [Vista ad albero](Tree_view/it.md) o dal menu contestuale della [Vista 3D](3D_view/it.md) .
    -   [BIM](BIM_Workbench/it.md): Selezionare l\'opzione **Snapping → <img src="images/Draft_ToggleGrid.svg" width=16px> Attiva/disattiva Griglia** dal menu o dal menu contestuale della vista 3D.
    -   Usare la scorciatoia da tastiera: **G** quindi **R**. Questa scorciatoia non può essere utilizzata se è attivo un altro comando.
3.  La visibilità della griglia appartenente alla vista 3D corrente è cambiata:
    -   Se nessun altro comando è attivo:
        -   Se la griglia era invisibile ora è sempre visibile.
        -   Se la griglia era visibile ora non è più sempre visibile, ma la visibilità della griglia durante i comandi rimane invariata.
    -   Se è attivo un altro comando:
        -   Se la griglia era invisibile ora è visibile solo durante i comandi.
        -   Se la griglia era visibile ora non è più visibile durante i comandi e non è più sempre visibile.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Sono disponibili diverse preferenze della griglia: **Modifica → Preferenze... → Draft → Griglia e aggancio**.
-   Per mantenere la griglia attiva quando si passa ad altri ambienti di lavoro vedere [Ottimizzazione](Fine-tuning/it#Draft_Workbench.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleGrid/it
