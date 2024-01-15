# Sketcher CreateRectangle/ro
---
 GuiCommand:   Name: Sketcher CreateRectangle   Name/ro: Sketcher CreateRectangle   Workbenches: Sketcher Workbench/ro   Sketcher---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Desenează un dreptunghi definit prin două puncte diagonal opuse. Când pornește instrumentul, indicatorul mouse-ului se schimbă într-o cruce albă cu o iconițo cu un dreptunghi roșu. Coordonatele indicatorului sunt afișate lângă indicator în culoarea albastră și în timp real.


</div>

To define a rectangle via a center point and an edge point, use the [Centered rectangle](Sketcher_CreateRectangle_Center.md) tool.

![](images/SketcherCreateRectangleExample.png‎ )




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

-   Duă ce apăsați butonul \'Create Rectangle\', click o dată pentru a defini primul colț, apoi glisăm mouse-ul și click a doua oară pentru a stabili al doilea unghi/colț.
-   Apăsați tasta **Esc** sau click butonul drepta al mouse-ului pentru a abandona/anula această funcție.


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





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/ro
