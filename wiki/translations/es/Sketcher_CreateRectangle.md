---
 GuiCommand:
   Name: Sketcher CreateRectangle
   Name/es: Croquizador CrearRectángulo
   Workbenches: Sketcher Workbench/es
   MenuLocation: Croquizador, Geometrías del Croquizador , Crear rectángulo
   Shortcut: **R**
   SeeAlso: Sketcher_CreatePolyline/es
---

# Sketcher CreateRectangle/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta dibuja un rectángulo seleccionando dos puntos opuestos.

Cuando se inicia esta herramienta, el puntero del ratón cambia a una cruz blanca con un icono de un rectángulo rojo. Las coordenadas del puntero se muestran al lado en color azul en tiempo real.


</div>

To define a rectangle via a center point and an edge point, use the [Centered rectangle](Sketcher_CreateRectangle_Center.md) tool.

![](images/SketcherCreateRectangleExample.png‎ )



## Utilización


<div class="mw-translate-fuzzy">

-   Después de pulsar el **[<img src=images/Sketcher_CreateRectangle.svg style="width:16px"> [Crear Rectángulo](Sketcher_CreateRectangle/es.md)** boton, clic una vez para establecer la primera esquina, luego mueve el ratón y haz clic una segunda vez para establecer la esquina opuesta.
-   Presionando **Esc** o haciendo click con el botón derecho del ratón se cancela la función.


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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/es
