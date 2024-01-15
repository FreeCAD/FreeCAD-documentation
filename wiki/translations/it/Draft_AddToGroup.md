---
 GuiCommand:
   Name: Draft_AddToGroup
   Name/it: Sposta nel gruppo
   MenuLocation: Utilità , Sposta nel gruppo...
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Std_Group/it, Draft_AddNamedGroup/it, Draft_AddConstruction/it, Draft_AutoGroup/it
---

# Draft AddToGroup/it



## Descrizione

Il comando <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> **Draft Sposta nel gruppo** sposta gli oggetti in un [Gruppo](Std_Group/it.md) o in un oggetto [Arch](Arch_Workbench/it.md) simile a un gruppo. Può anche separare gli oggetti.



## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Draft_AddToGroup.svg" width=16px> [Draft Sposta nel gruppo](Draft_AddToGroup/it.md)**.
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_AddToGroup.svg" width=16px> Sposta nel gruppo...** dal menu.
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_AddToGroup.svg" width=16px> Sposta nel gruppo...** dal menù contestuale alle [Vista ad albero](Tree_view/it.md) o [Vista 3D](3D_view/it.md).
3.  Viene visualizzato un menu vicino al cursore. Effettuare una delle seguenti operazioni:
    -   Selezionare **Separa** per spostare gli oggetti fuori dai gruppi in cui si trovano.
    -   Selezionare il gruppo in cui si vogliono spostare gli oggetti.
    -   Selezionare **+ Aggiungi nuovo gruppo** per spostare gli oggetti in un nuovo gruppo:
        1.  Si apre il pannello delle attività **Aggiungi gruppo**.
        2.  Inserire un **Nome gruppo**.
        3.  Premere il pulsante **OK**.



## Note

-   Gli oggetti possono anche essere spostati in un gruppo trascinandoli sul gruppo nella [Vista ad albero](Tree_view/it.md).
-   Questo comando può essere utilizzato per spostare oggetti nel [Gruppo di costruzione Draft](Draft_ToggleConstructionMode/it.md), ma, contrariamente al comando [Draft Aggiungi al gruppo Costruzione](Draft_AddConstruction/it.md), non applica il [colore della geometria di costruzione ](Draft_ToggleConstructionMode/it#Preferenze.md).
-   Per ulteriori informazioni sull\'organizzazione del proprio modello vedere [Struttura del documento](Document_structure/it.md) e [Arch tutorial](Arch_tutorial/it#Organizzare_il_modello.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddToGroup/it
