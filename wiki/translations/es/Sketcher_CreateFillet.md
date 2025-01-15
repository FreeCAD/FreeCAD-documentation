---
 GuiCommand:
   Name: Sketcher CreateFillet
   Name/es: Sketcher CreateFillet
   MenuLocation: Croquizador , Geometrías del Croquizador , Crear redondeo
   Workbenches: Sketcher Workbench/es
   Shortcut: F
---

# Sketcher CreateFillet/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta crea un redondeo entre dos líneas unidas en un punto. Activa la herramienta, selecciona ambas líneas o pulsa sobre el punto de dicha esquina.


</div>


<small>(v1.0)</small> 

: If two straight edges connected by a [Coincident constraint](Sketcher_ConstrainCoincident.md) are filleted or chamfered, the corner point can optionally be preserved. The tool then adds a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both edges. Constraints connected to the corner point are transferred to the new point object.

![](images/SketcherCreateFilletExample.png‎ )



## Utilización

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

1.  Pulse el **[<img src=images/Sketcher_CreateFillet.svg style="width:16px"> [CrearRedondeo](Sketcher_CreateFillet/es.md)**.
2.  Elige un vértice que conecte dos líneas; o haz clic en dos líneas conectadas, la distancia a la que hagas clic del vértice establecerá el radio del filete.
3.  Pulsando **Esc** o haciendo clic con el botón derecho del ratón se cancela o finaliza la función.


</div>

## Notes

-   The construction geometry arc of a chamfer is not visible outside the sketch. It cannot be deleted without breaking the geometry of the chamfer.
-   Some ([conic](Sketcher_Workbench#Sketcher_CompCreateConic.md)) curves may need to be [trimmed](Sketcher_Trimming.md) before they can be filleted.
-   The fillet radius depends on the selection method. If a [Coincident constraint](Sketcher_ConstrainCoincident.md) connecting two straight edges is selected, the fillet radius is derived from the length of the shortest edge. If two edges are selected the radius is the distance from the first clicked point to the (extended) intersection of the edges.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/es
