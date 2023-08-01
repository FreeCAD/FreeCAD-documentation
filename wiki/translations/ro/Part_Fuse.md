---
- GuiCommand:
   Name/ro: Part Union
   Icon: Part Fuse.png
   MenuLocation: Part - Boolean - Union
   Workbenches: [Part](Part_Workbench/ro.md)
   SeeAlso: [Part Cut](Part_Cut/ro.md), [Part Common](Part_Common/ro.md)
---

# Part Fuse/ro


</div>

## Descriere

Unites (fuses) selected Part objects into one. This operation is fully parametric and the components can be modified and the result recomputed.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

## Cum se folosește 

1.  Selectați două forme
2.  Apăsați butonul **<img src="images/Part_Fuse.png" width=16px> '''Part Union'''**.




1.  Select two or more shapes
2.  There are several ways to invoke the command:
    -   Press the **![](images/) Part Fuse** button in the **Part tools** toolbar
    -   Use the **Part → Boolean → Union** entry in the Part menu

## Intrări suportate 


<div class="mw-translate-fuzzy">

Elementele de intrare trebuie să fie forme OpenCascade. Exemple: chestii realizate cu Atelierele: Part, PartDesign, Sketcher. Nu este vorba despre plase (cu excepția cazului în care acestea au fost convertite în forme) - pentru ochiurile de plasă, există unelte specifice Booleene în Atelierul de lucru MeshDesign.


</div>

-   Solid + Solid: the result is a solid that occupies all the volume covered by the inputs

-   Shell + Shell, Shell + Face, Face + Face: the result is a shell. Where faces intersect, they are split. Shells can be non-manifold. After fusion, faces can be united by [Refining](Part_RefineShape.md) the result.

-   Wire + Wire, Edge + Wire, Edge + Edge: the result is a wire. Edges are split where they intersect.

Compounds are supported; however, it is assumed that shapes packed into a compound do not touch or intersect. If they actually do, Fusion will likely fail, or produce an incorrect result.

## Options


<div class="mw-translate-fuzzy">

## Opțiuni

Elementele pot fi adăugate și scoase din fuziune/uniune, tragându-le în sau în afara funcției de siguranțe din arborele cu mouse-ul. Este necesară o recalculare manuală (apăsați tasta F5 sau faceți clic pe pictograma recompute) pentru a vedea rezultatele.


</div>

După această operație, este posibil să fie necesară curățarea formei [RefineShape](Part_RefineShape.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/ro
