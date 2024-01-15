# Sketcher CreateRectangle/it
---
 GuiCommand:   Name: Sketcher CreateRectangle   Name/it: Rettangolo   Workbenches: Sketcher Workbench/it   Sketcher---


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Disegna un rettangolo definendo nella vista 3D due punti di vertice opposti.

Quando si avvia lo strumento, il puntatore del mouse assume la forma di croce bianca accompagnata dall\'icona rossa di rettangolo.

Accanto al puntatore sono visualizzate, in blu, le coordinate della sua posizione, aggiornate in tempo reale.


</div>

To define a rectangle via a center point and an edge point, use the [Centered rectangle](Sketcher_CreateRectangle_Center.md) tool.

![](images/SketcherCreateRectangleExample.png‎ )



## Utilizzo


<div class="mw-translate-fuzzy">

-   Dopo aver premuto il pulsante <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> Rettangolo, selezionare il primo vertice nell\'area della vista 3D, o su un oggetto esistente, poi spostare il puntatore e selezionare il vertice opposto. I vincoli automatici (auto constraints) si attivano nella scheda **Azioni → Modifica controlli → Autovincoli** del pannello **Vista combinata**.
-   Premere il tasto **Esc**, o cliccare sul tasto destro del mouse, per annullare l\'operazione.


</div>

## Notes

-   When launched the rectangle tools add a **Rectangle parameters** section at the top of the Sketcher [Task panel](Task_panel.md) (<small>(v0.22)</small> ). It contains:

1.  A **Mode** spinbox to chose one of the modes to draw the rectangle:
    -   Corner, length & width
    -   Center, length & width
    -   3 corners
    -   Center and two corners
2.  A **Rounded corners** checkbox to apply round corners to the rectangle.
3.  A **Frame** checkbox to add a contour with a constant offset to the (rounded) rectangle.

-   All three buttons in this selection now launch the same tool but with different preset combinations of mode and options that can still be altered after the first click.
-   If **Rounded corners** is enabled, the offset is inward, and the offset value is larger than the corner radius, the offset contour will be created without fillets.
-   The modes **3 corners**, and **Center and two corners** create parallelograms rather than rectangles.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/it
