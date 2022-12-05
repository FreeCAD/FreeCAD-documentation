---
- GuiCommand:/it
   Name:Drawing_ProjectShape
   Name/it:Proietta le forme
   Empty:1
   Workbenches:[Drawing](Drawing_Workbench/it.md)
   MenuLocation:Drawing → Proietta le forme
---

# Drawing ProjectShape/it

## Descrizione

Questo strumento crea una proiezione dell\'oggetto selezionato, l\'oggetto sorgente, nella vista 3D.

![](images/ProjectShape1_it.png )

## Utilizzo

+++
| ![](images/ProjectShapeSet_it.png ) | 1.  Selezionare un oggetto nella vista 3D o nella struttura del progetto                                                               |
|                                                      | 2.  fare clic sullo strumento **Proietta le forme**                                                                                    |
|                                                      | 3.  impostare le opzioni desiderate                                                                                                    |
|                                                      | 4.  cliccare su **OK**                                                                                               |
|                                                      |                                                                                                                                        |
|                                                      | Nell\'albero del progetto viene aggiunto un oggetto **Nome_proj**. Per le proiezioni successive, viene aggiunto un numero a tre cifre. |
+++

### Modificare una proiezione esistente 

+++
| ![](images/ProjectShapeOptions_it.png ) | I parametri della proiezione possono essere modificati nella scheda Dati della vista combinata.                                                                                                                            |
|                                                              | {{KEY/it|Base}}                                                                                                                                                                                              |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Label}}                                                                                                                                                                                                |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Placement}}                                                                                                                                                                                            |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | {{KEY/it|Projection}}                                                                                                                                                                                        |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Direction}}                                                                                                                                                                                            |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     : definisce la direzione della proiezione. Questa viene determinata dai valori xyz che definiscono un vettore normale alla pagina. La vista dall\'alto sul piano xy è (0,0,1). I valori possono anche essere negativi. |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|HCompound}}                                                                                                                                                                                            |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Iso Line HCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Iso Line VCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Out Line HCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Out Line VCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Rg1 Line HCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Rg1 Line VCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Rg NLine HCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Rg NLine VCompound}}                                                                                                                                                                                   |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|Source}}                                                                                                                                                                                               |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     : indica la forma sorgente utilizzata                                                                                                                                                                                  |
|                                                              |                                                                                                                                                                                                                            |
|                                                              | -                                                                                                                                                                                                           |
|                                                              |     {{ProprietaDati|VCompound}}                                                                                                                                                                                            |
|                                                              |                                                                                                                                                                                                                         |
|                                                              |     :                                                                                                                                                                                                                      |
+++


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing ProjectShape/it
