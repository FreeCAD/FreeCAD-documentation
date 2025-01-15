---
 GuiCommand:
   Name: Sketcher External
   Name/ro: Sketcher External
   Workbenches: Sketcher Workbench/ro
   Shortcut: X
   MenuLocation: Sketch , Sketcher geometries , Sketcher External
   SeeAlso: Sketcher_ToggleConstruction/ro
---

# Sketcher External/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul de geometrie externă Sketcher( External Geometry) este folosit atunci când trebuie aplicată o constrângere între geometria schiței și ceva în afara schiței. Funcționează prin introducerea unei constrângeri a unei constrângeri de construcție geometrice în schiță. Culoarea implicită a marginilor exterioare conectate este purpurie. Ca și geometria standard a construcției, care nu este conectată (albastră), geometria externă conectată este de asemenea vizibilă numai atunci când desenul este în modul de editare și nu este utilizat în rezultatul următor și nici nu este utilizat într-un alt instrument. Ambele tipuri de geometrie a construcției din schiță pot fi folosite ca referințe la constrângeri.


</div>


<small>(v1.1)</small> 

: See <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projection](Sketcher_Projection.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*The two magenta lines are external geometry linked to edges of a pre-existing [Pad](PartDesign_Pad.md). They are used to constrain the circles.*




<div class="mw-translate-fuzzy">

## Utilizare


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Create a new sketch, or open an existing sketch.
-   Click \'Sketcher External\' button
-   Select an edge or a vertex that you want to link to in the sketch.
-   Press Esc, or select another tool to stop importing geometry into the sketch.


</div>

## Notes

-   Only edges and vertices from objects within the same coordinate system can be selected. The sketch and the object must be in same [Body](PartDesign_Body.md), or the same [Part](Std_Part.md), or both in the global coordinate system. Use a [Binder](PartDesign_SubShapeBinder.md) to bring a copy of the object into the current coordinate system if required.
-   Circular dependencies are not allowed. You cannot link to an object that depends on the sketch itself.
-   Links to elements from other sketches are possible, and encouraged, as they are more reliable than links to generated (solid) geometry. The latter can suffer from the [Topological Naming Problem](Topological_naming_problem.md). See [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).


<div class="mw-translate-fuzzy">


</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/ro
