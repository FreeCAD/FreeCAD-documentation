# Sketcher CreateFillet/ro
---
 GuiCommand:   Name: Sketcher CreateFillet   Name/ro: Sketcher CreateFillet   Workbenches: Sketcher Workbench/ro   Sketcher|Shortcut: F   MenuLocation: Sketch , Sketcher geometries , Create fillet---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument creează o racordarea între două linii care se unesc într-un punct. Activați instrumentul, apoi selectați ambele linii sau click pe punctul de colț.


</div>


<small>(v1.0)</small> 

: If two straight edges connected by a [Coincident constraint](Sketcher_ConstrainCoincident.md) are filleted or chamfered, the corner point can optionally be preserved. The tool then adds a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both edges. Constraints connected to the corner point are transferred to the new point object.

![](images/SketcherCreateFilletExample.png‎ )




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Selectați vertex-ul care conectează cele două linii; sau click pe cele două linii conectate, distanța la care se face click determină raza racordării.
-   Apăsați **Esc** sau click dreapta pe butonul mouse-ului și abandonați sau terminați acestă funcție.





</div>

## Notes

-   The construction geometry arc of a chamfer is not visible outside the sketch. It cannot be deleted without breaking the geometry of the chamfer.
-   Some ([conic](Sketcher_Workbench#Sketcher_CompCreateConic.md)) curves may need to be [trimmed](Sketcher_Trimming.md) before they can be filleted.
-   The fillet radius depends on the selection method. If a [Coincident constraint](Sketcher_ConstrainCoincident.md) connecting two straight edges is selected, the fillet radius is derived from the length of the shortest edge. If two edges are selected the radius is the distance from the first clicked point to the (extended) intersection of the edges.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/ro
