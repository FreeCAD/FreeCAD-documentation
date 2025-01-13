---
 GuiCommand:
   Name: Part Taglio
   MenuLocation: Parte , Operazione booleana , Taglio
   Workbenches: Part_Workbench/it
   SeeAlso: Part_Boolean/it, Part_Fuse/it, Part_Common/it
---

# Part Cut/it



## Descrizione

Lo strumento <img alt="" src=images/Part_Cut.svg  style="width:24px;"> **Part Taglio** taglia (sottrae) gli oggetti Part selezionati, l\'ultimo viene sottratto dal primo. Questa operazione è completamente parametrica e i componenti possono essere modificati e il risultato ricalcolato.

Questo strumento è una forma automatizzata di <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Operazione booleana](Part_Boolean/it.md).

<img alt="" src=images/Part_Cut_01.png  style="width:480px;">



## Utilizzo

1.  Selezionare due forme.
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/Part_Cut.svg" width=16px> [Taglio](Part_Cut/it.md)**.
    -   Selezionare l\'opzione **Parte → Operazione booleana → <img src="images/Part_Cut.svg" width=16px> Taglio** dal menu.



## Input supportati 

Gli oggetti di input devono essere forme [OpenCASCADE](OpenCASCADE/it.md). Ad esempio oggetti realizzati con gli ambienti Part, PartDesign o Sketcher. Per le mesh sono disponibili strumenti booleani dedicati nell\' [Ambiente Mesh](Mesh_Workbench/it.md).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/it
