# Sketcher CreateRectangle/cs
---
 GuiCommand:   Name: Sketcher CreateRectangle   Name/cs: Skicář Obdélník   Workbenches: Sketcher Workbench/cs   Skicář---


</div>



## Popis


<div class="mw-translate-fuzzy">

Tento nástroj nakreslí obdélník zadáním dvou protějších bodů. Při spuštění nástroje se ukazatel myši změní na bílý křížek s ikonou červeného obdélníku. Vedle jsou zobrazeny souřadnice v reálném čase.


</div>

To define a rectangle via a center point and an edge point, use the [Centered rectangle](Sketcher_CreateRectangle_Center.md) tool.

![](images/SketcherCreateRectangleExample.png‎ )




<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

-   Po stisknutí tlačítka **<img src="images/Sketcher_CreateRectangle.png" width=24px> Vytvořit Obdélník**, klikněte nejdříve na místo prvního bodu, potom přesuňte myš a klikněte do místa druhého bodu v protějším rohu.
-   Stisknutím klávesy **Esc** nebo kliknutím na pravé tlačítko myši se funkce přeruší.


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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/cs
