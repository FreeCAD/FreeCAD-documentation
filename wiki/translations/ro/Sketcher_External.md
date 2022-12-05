---
- GuiCommand:/ro
   Name:Sketcher External
   Name/ro:Sketcher External
   Workbenches:[Sketcher](Sketcher_Workbench/ro.md)
   Shortcut:X
   MenuLocation:Sketch → Sketcher geometries → Sketcher External
   SeeAlso:[ConstructionMode](Sketcher_ToggleConstruction/ro.md)
---

# Sketcher External/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul de geometrie externă Sketcher( External Geometry) este folosit atunci când trebuie aplicată o constrângere între geometria schiței și ceva în afara schiței. Funcționează prin introducerea unei constrângeri a unei constrângeri de construcție geometrice în schiță. Culoarea implicită a marginilor exterioare conectate este purpurie. Ca și geometria standard a construcției, care nu este conectată (albastră), geometria externă conectată este de asemenea vizibilă numai atunci când desenul este în modul de editare și nu este utilizat în rezultatul următor și nici nu este utilizat într-un alt instrument. Ambele tipuri de geometrie a construcției din schiță pot fi folosite ca referințe la constrângeri.


</div>

A note of caution, using this tool to link to generated (solid) geometry can lead to unexpected results due to [Topological Naming Problem](Topological_naming_problem.md). Also see [Advice for stable models](Feature_editing#Advice_for_creating_stable_models.md).

<FILE:Sketcher_ExternalEsempio1.png>


<div class="mw-translate-fuzzy">

## Utilizare


</div>


<div class="mw-translate-fuzzy">

-   Create a new sketch, or open an existing sketch.
-   Click \'Sketcher External\' button
-   Select an edge or a vertex that you want to link to in the sketch.
-   Press Esc, or select another tool to stop importing geometry into the sketch.


</div>


<div class="mw-translate-fuzzy">

### Regulile de selecție 

Selection rules for what objects can be imported differ drastically between FC v0.16 and FC v0.17.


</div>


<div class="mw-translate-fuzzy">

That is, the sketch and the object must be in same Body, or in same Part, or both outside of any Parts and Bodies.


</div>

For example, If the open sketch is in Body, you can use another sketch from Body as external geometry, but you can\'t use a sketch from Body001, or an edge from a Part Cube in the root of the project. Use Shapebinder feature to bring in a copy of the object into the coordinate system of open sketch. Then you will be able to use edges/vertices of Shapebinder object.

-   No circular dependencies are allowed.

That means, you can\'t link to Pocket made with this sketch. You can\'t link to any object that depends on the sketch.


<div class="mw-translate-fuzzy">

Unlike in v0.16, sketch doesn\'t have to be on any face in order to use this tool. Links directly between sketches are possible, and encouraged, as they are more reliable.


</div>

### Appearance When Successfully Linked 

A (default magenta) coloured line will be overlaid when an edge is successfully linked (the vertices will be red), and will be visible in your sketch only while your sketch is in edit mode.

### Similarity to Construction Lines 

External geometry (default colour magenta) lines are similar (default colour blue) [Contruction lines](Sketcher_ToggleConstruction.md) except in that the external geometry magenta lines are parametrically linked back to an element of the solid to which the sketch is mapped. Construction geometry are lines that are internal to the sketch, are only visible when the sketch is in edit mode and will be used for constraint references only, and not directly for later solid operations, like Pad or Pocket.

### Use Of External Geometry in a PartDesign Workbench Work Flow 

In the PartDesign workbench work flow, the External Geometry tool is used to assist in the positioning of an aspect of the solid you are constructing, relative to the previous stage in its construction. PartDesign workbench is intended to produce one single solid, therefore these sketches with external geometry are used to create a new feature of that one single solid.

The external geometry can, for example, be used as a reference for a constraint being used to position a hole in an object at a specific location relative to an edge or vertex.

### Use Of External Geometry in a Part Workbench Work Flow 

You can use any Part geometry that is in coordinate system of the sketch. It is advised to link to the earliest feature possible, as it forms a more stable link.

## Exemplu

Mai jos este o schiță desenată pe fața superioară a unui solid creat dintr-un obiect creat cu o schiță construită anterior. Linile magenta sunt linii de geometrie externă legate de ambele margini ale acestui obiect pre-existent.

În acest caz, ele sunt folosite ca referință pentru constrângerile de tangență cu circumferința unui cerc. Ele sunt, de asemenea, utilizate ca referință pentru o constrângere orizontală și verticală pentru a localiza centrul celui de-al doilea cerc în raport cu capătul și vârful obiectului.

<FILE:Sketcher_ExternalEsempio2.png>

Aceasta este aceeași schiță în modul de editare, cu Pad-ul pe care este mapată ascunsă.

<FILE:Sketcher_ExternalEsempio4.png>

When the sketch edit mode is closed, External Geometry lines are not visible.

<FILE:Sketcher_ExternalEsempio3.png>


<div class="mw-translate-fuzzy">


</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/ro
