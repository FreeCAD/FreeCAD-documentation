---
- GuiCommand:/it
   Name:Sketcher_CarbonCopy
   Name/it:Copia carbone
   MenuLocation:Sketch → Geometrie → Copia carbone
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   Version:0.17
---

# Sketcher CarbonCopy/it


</div>

## Descrizione

Lo strumento <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:16px;"> **Copia carbone** copia tutta la geometria e i vincoli di un altro schizzo nello schizzo attivo.

I vincoli dimensionali che esistono prima della funzione di copia rimangono collegati ai vincoli dimensionali dello schizzo originale attraverso le [espressioni](expressions/it.md).

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Assicurarsi di essere nella modalità di modifica di uno <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Schizzo](Sketcher_NewSketch/it.md).
2.  Premere il pulsante **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> Copia carbone**.
3.  Fare clic su un bordo in un altro schizzo.
4.  Gli elementi della geometria ed i vincoli vengono copiati nello schizzo attivo.
5.  Premere **Esc** o il pulsante destro del mouse per terminare l\'operazione.


</div>

## Notes

-   When sketches are used in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), normally the sketch to carbon copy should be in the same **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)** as the currently active sketch. If the sketch to be copied is not in the active [Body](PartDesign_Body.md), the mouse pointer will not allow selection. In this case, hold **Ctrl** to allow selection of sketches from other Bodies.
-   Normally, the sketch to select should be in a plane that is parallel to the currently active sketch. If the sketch to be copied is not parallel to the currently active sketch, hold **Ctrl**+**Alt** to allow selection of non-parallel sketches. The object will then be adjusted to the active sketch\'s plane. Noteː as of this writing this needs a save and reload of the document to make it visible. This works for sketches located outside of the currently active [Body](PartDesign_Body.md) as well.
-   Since carbon-copied dimensional constraints use expressions they are rendered in a different color. The color can be customized with the [Preferences Editor](Preferences_Editor.md) at **Edit → Preferences → Sketcher → Colors → Expression dependent constraint color**.
-   If the Sketcher mode has been changed to construction mode using **[<img src=images/Sketcher_ToggleConstruction.svg style="width:24px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** all copied geometry will be created in construction mode.

## Limitazioni


<div class="mw-translate-fuzzy">

-   Viene copiato tutto il contenuto dello schizzo; non è possibile selezionare solo una parte di esso.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/it
