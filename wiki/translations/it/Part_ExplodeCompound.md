---
 GuiCommand:
   Name: Part ExplodeCompound
   Name/it: Part esplodi composto
   MenuLocation: Part , Composto , Esplodi composto
   Workbenches: Part_Workbench/it
   Version: 0.18
   SeeAlso: Part_Compound/it, Draft Downgrade/it
---

# Part ExplodeCompound/it



## Descrizione

Lo strumento <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> **Part Esplodi composto** suddivide un composto di forme, per rendere disponibile ciascuna forma contenuta (figlio) come oggetto separato nell\'albero del modello. I figli vengono automaticamente inseriti in un [Gruppo](Std_Group/it.md) se c\'è più di un figlio.

È semi-parametrico: le forme dei figli si aggiorneranno man mano che il composto sorgente cambia, ma se viene modificato il numero di figli nel composto, nell\'esploso mancheranno alcune forme o ci saranno oggetti ridondanti in una condizione di errore.

I posizionamenti delle forme estratte seguono i posizionamenti degli originali, oltre alla proprietà Posizionamento di ogni figlio.

Lo strumento esplode anche forme non composte nei loro costituenti di livello inferiore: solidi composti in solidi, solidi in gusci, gusci in facce, facce in contorni, contorni in bordi, bordi in vertici.



## Utilizzo

1.  Selezionare un singolo composto.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Part_ExplodeCompound.svg" width=16px> [Esplodi composto](Part_ExplodeCompound/it.md)**.
    -   Selezionare l\'opzione **Parte → Composto → <img src="images/Part_ExplodeCompound.svg" width=16px> Esplodi composto** dal menu.



## Casi d\'uso 

-   La modifica delle posizioni delle forme create da <img alt="" src=images/Draft_OrthoArray.svg  style="width:16px;"> [Draft Serie ortogonale](Draft_OrthoArray/it.md)
-   L\'ottenimento di pezzi divisi dal risultato di <img alt="" src=images/Part_Slice.svg  style="width:16px;"> [Part Affetta](Part_Slice/it.md) e <img alt="" src=images/Part_Cut.svg  style="width:16px;"> [Part Taglio](Part_Cut/it.md)
-   L\'ottenimento di contorni individuali da schizzi e facce a più contorni
-   L\'ottenimento di un solido puro da un solido in composto, da utilizzare in <img alt="" src=images/Workbench_FEM.svg  style="width:16px;"> [Ambiente FEM](FEM_Workbench/it.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/it
