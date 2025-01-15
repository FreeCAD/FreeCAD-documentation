# Sketcher CreateFillet/cs
---
 GuiCommand:   Name: Sketcher CreateFillet   Name/cs:  Skicář Zaoblení   Workbenches: Sketcher Workbench/cs   Skicář|MenuLocation: Náčrt , Skicář Konstrukce ,  Vytvořit zaoblení   Shortcut: F   SeeAlso: ---


</div>



## Popis


<div class="mw-translate-fuzzy">

Tento nástroj vytvoří zaoblení mezi dvěma přímkami, které se spojí v bodě. Aktivuje se tento nástroj a potom se vyberou obě přímky nebo se klikne na rohový bod.


</div>


<small>(v1.0)</small> 

: If two straight edges connected by a [Coincident constraint](Sketcher_ConstrainCoincident.md) are filleted or chamfered, the corner point can optionally be preserved. The tool then adds a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both edges. Constraints connected to the corner point are transferred to the new point object.

![](images/SketcherCreateFilletExample.png‎ )




<div class="mw-translate-fuzzy">

## Použití


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Vyberte vrchol, kde se dotýkají dvě přímky nebo klikněte na dvě dotýkající se přímky. Vzdálenost mezi kliknutím a vrcholem určuje poloměr zaoblení.
-   Stisknutí klávesy **Esc** nebo kliknutí pravým tlačítkem myši přeruší nebo ukončí funkci nástroje.





</div>

## Notes

-   The construction geometry arc of a chamfer is not visible outside the sketch. It cannot be deleted without breaking the geometry of the chamfer.
-   Some ([conic](Sketcher_Workbench#Sketcher_CompCreateConic.md)) curves may need to be [trimmed](Sketcher_Trimming.md) before they can be filleted.
-   The fillet radius depends on the selection method. If a [Coincident constraint](Sketcher_ConstrainCoincident.md) connecting two straight edges is selected, the fillet radius is derived from the length of the shortest edge. If two edges are selected the radius is the distance from the first clicked point to the (extended) intersection of the edges.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/cs
