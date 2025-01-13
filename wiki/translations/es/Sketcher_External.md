---
 GuiCommand:
   Name: Sketcher External
   Name/es: Croquizador Externo
   MenuLocation: Croquis , Croquizador Geometrías , Croquizador Externo
   Workbenches: Sketcher_Workbench/es
   Shortcut: X
   SeeAlso: Sketcher_ToggleConstruction/es
---

# Sketcher External/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Usa la herramienta **<img src="images/Sketcher_External.svg" width=16px> [Geometría externa](Sketcher_External/es.md)** cuando necesites aplicar una restricción entre la geometría del croquis y algo fuera del mismo. Funciona insertando una geometría de construcción vinculada en el croquis. El color por defecto de los bordes vinculadas externamente es el magenta. Al igual que con la geometría de construcción no vinculada estándar (azul), la geometría vinculada externamente sólo es visible cuando el croquis está en modo de edición y no se utiliza directamente en el resultado posterior del uso del croquis en otra herramienta. Ambos tipos de geometría de construcción pueden utilizarse como referencia para las restricciones dentro del croquis.


</div>


<small>(v1.1)</small> 

: See <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projection](Sketcher_Projection.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*The two magenta lines are external geometry linked to edges of a pre-existing [Pad](PartDesign_Pad.md). They are used to constrain the circles.*



## Utilización

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


<div class="mw-translate-fuzzy">

-   Crear un nuevo croquis, o abrir un croquis existente.
-   Haga clic en el botón \'Croquizador Externo\'.
-   Selecciona un borde o un vértice que quieras enlazar en el croquis.
-   Pulsa Esc, o selecciona otra herramienta para dejar de importar geometría al croquis.


</div>

## Notes

-   Only edges and vertices from objects within the same coordinate system can be selected. The sketch and the object must be in same [Body](PartDesign_Body.md), or the same [Part](Std_Part.md), or both in the global coordinate system. Use a [Binder](PartDesign_SubShapeBinder.md) to bring a copy of the object into the current coordinate system if required.
-   Circular dependencies are not allowed. You cannot link to an object that depends on the sketch itself.
-   Links to elements from other sketches are possible, and encouraged, as they are more reliable than links to generated (solid) geometry. The latter can suffer from the [Topological Naming Problem](Topological_naming_problem.md). See [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/es
