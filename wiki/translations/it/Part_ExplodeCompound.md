---
- GuiCommand:   Name: Part ExplodeCompound
   Name/it: Esplodi composto
   MenuLocation: Part -> Composto -> Esplodi composto
   Version: 0.18.15506
   Workbenches: Part_Workbench/it
   SeeAlso: Part_Compound/it, Draft Downgrade/it
---

# Part ExplodeCompound/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Strumento per dividere composti di forme, per rendere ogni forma contenuta (figlio) disponibile come oggetto separato nell\'albero del modello. I figli vengono automaticamente inseriti in [Gruppo](Std_Group/it.md) se c\'è più di un figlio.


</div>

È semi-parametrico: le forme dei figli si aggiorneranno man mano che il composto sorgente cambia, ma se viene modificato il numero di figli nel composto, nell\'esploso mancano alcune forme o ci sono oggetti ridondanti in una condizione di errore.

I posizionamenti delle forme estratte seguono i posizionamenti degli originali, oltre alla proprietà Posizionamento di ogni figlio.

Lo strumento esplode anche forme non composte nei loro costituenti di livello inferiore: solidi composti in solidi, solidi in gusci, gusci in facce, facce in contorni, contorni in bordi, bordi in vertici.

## Utilizzo

1.  Invocare il comando Esplodi il composto in uno di questi modi:
    -   Premere sul pulsante <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> nella barra degli strumenti di Part
    -   Usare **Parte → Composto → Esplodi il composto** dal menu principale

## Casi d\'uso 


<div class="mw-translate-fuzzy">

-   modificare le posizioni delle forme realizzate da una <img alt="" src=images/Draft_Array.svg  style="width:24px;"> [Serie](Draft_Array/it.md) di Draft
-   ottenere pezzi divisi dal risultato di <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Affetta in composto](Part_Slice/it.md) o da una <img alt="" src=images/Part_Cut.svg  style="width:24px;"> [Sottrazione booleana](Part_Cut/it.md)
-   ottenere i contorni individuali dagli schizzi e dalle facce multi-contorno
-   ottenere un solido puro da un solido in un composto, da utilizzare nell\'ambiente <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/it
