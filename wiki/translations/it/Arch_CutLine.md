---
 GuiCommand:
   Name: Arch CutLine
   Name/it: Taglio con una linea
   MenuLocation: Arch , Taglio con una linea
   Workbenches: Arch_Workbench/it
   Version: 0.19
   SeeAlso: Arch_CutPlane/it
---

# Arch CutLine/it



## Descrizione

Lo strumento **Arch CutLine** taglia un oggetto Arch solido come un [Muro](Arch_Wall/it.md) o una [Struttura](Arch_Structure/it.md) con un bordo dritto. Sulla base di quel bordo e della normale al [Piano di lavoro](Draft_SelectPlane/it.md) viene generato un piano di taglio.

<img alt="" src=images/Arch_CutLine_example_1.png  style="width:" height="300px;"> <img alt="" src=images/Arch_CutLine_example_2.png  style="width:" height="300px;">



*Muro tagliato da una linea. A sinistra: parallelepipedo sottrattivo che appare quando si utilizza lo strumento. A destra: parete risultante dopo il taglio.*



## Utilizzo

1.  Se necessario allineare il piano di lavoro:
    -   Il bordo selezionato potrebbe non essere parallelo alla normale del piano di lavoro.
    -   Il piano di taglio generato sarà perpendicolare al piano di lavoro.
2.  Selezionare l\'oggetto da tagliare nella [Vista ad albero](Tree_view/it.md) o nella [Vista 3D](3D_view/it.md).
3.  Seleziona un bordo dritto. Questo deve essere selezionato nella [vista 3D](vista_3D/it.md).
4.  Premi il pulsante **<img src="images/Arch_CutLine.svg" width=16px> [Taglio con una linea](Arch_CutLine/it.md)**.
5.  Scegliere **Behind** o **Front** per indicare su quale lato della superficie di taglio il materiale deve essere rimosso.
6.  Cliccare il pulsante **OK**.



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CutLine/it
