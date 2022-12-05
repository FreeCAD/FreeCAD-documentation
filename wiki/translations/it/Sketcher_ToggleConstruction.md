---
- GuiCommand:/it
   Name:Sketcher ToggleConstruction
   Name/it:Geometria di costruzione
   Icon:Sketcher_AlterConstruction.svg
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketcher → Geometrie → Geometrie di costruzione
---

# Sketcher ToggleConstruction/it


</div>

## Descrizione

Questo strumento commuta una geometria dello schizzo da/in modalità Geometria di costruzione. Può essere utilizzato su qualsiasi tipo di geometria: linea, arco o cerchio.

La funzione **Elemento di costruzione** costituisce uno strumento importante e molto utile nel disegno di uno schizzo.

Quando si utilizza lo schizzo per una operazione 3D, la geometria definita di **costruzione** viene ignorata e non produce nessun effetto.


<div class="mw-translate-fuzzy">

In modalità <img alt="" src=images/Sketcher_EditSketch.svg  style="width:24px;"> [Modifica schizzo](Sketcher_EditSketch/it.md), la geometria di costruzione è indicata in **blu**, e non diventa **verde** fino a quando tutto lo schizzo non è **completamente vincolato**.

Quando si esce dalla modalità di disegno, la geometria di costruzione viene nascosta e non è più visibile sullo schermo.


</div>


<div class="mw-translate-fuzzy">

Le linee di costruzione possono essere utilizzate come assi di rotazione per eseguire operazioni di [rivoluzione](PartDesign_Revolution/it.md) in PartDesign.


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una o più geometrie nello schizzo in vista 3D, poi fare clic sullo strumento o accedere alla funzione tramite il menu.


</div>

## Esempio

Utilizzando la modalità di costruzione lo schizzo viene modificato,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">


<div class="mw-translate-fuzzy">

e finito lo schizzo gli elementi utilizzati per la costruzione diventano invisibili sullo schermo (ma sono ancora presenti in modalità modifica di Sketcher).


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">

## Notes

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Create point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** to change them to normal geometry. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/it
