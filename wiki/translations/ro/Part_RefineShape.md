---
 GuiCommand:
   Name: Part RefineShape
   MenuLocation: Part , Create a copy , Refine Shape
   Workbenches: Part_Workbench
   SeeAlso: Part_SimpleCopy, Part_TransformedCopy, Part_ElementCopy, OpenSCAD_RefineShapeFeature
---

# Part RefineShape/ro


</div>




<div class="mw-translate-fuzzy">

## Descriere

Curata liniile inutile. După o operație booleană, unele linii care definesc forma anterioară rămân vizibile, această unealtă creează o copie total curățată a originalului.


</div>

The **<img src="images/Part_RefineShape.svg" width=16px> [Part RefineShape](Part_RefineShape.md)** produces a non-parametric copy with a refined shape, that is, with certain edges and faces cleaned up.

After certain boolean operations, like [Part Fuse](Part_Fuse.md), some lines from the previous shapes may remain visible. This tool produces a copy of that boolean result, and cleans up those seams.

**Alternatively**, to produce other non-parametric copies use **<img src="images/Part_SimpleCopy.svg" width=16px> [Simple Copy](Part_SimpleCopy.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Transformed Copy](Part_TransformedCopy.md)**, and **<img src="images/Part_ElementCopy.svg" width=16px> [Element Copy](Part_ElementCopy.md)**

![](images/PartRefineShape_it.png )


<div class="mw-translate-fuzzy">

![](images/PartRefineShape_it.png )


</div>




<div class="mw-translate-fuzzy">

## Utilizare

1.  Selectați forma de curățat.
2.  Click pe meniul **Part → Refine shape** .

-   O copie a obiectului este creată și complet curățată, obiectul original este randat.
-   Copia nou creată este independentă de original.


</div>

1.  Select an object that you wish to clean and copy.
2.  Go to the menu **Part → Create a copy → <img src="images/Part_RefineShape.svg" width=16px> Refine shape**.
3.  A cleaned, independent copy of the original object is created; the original object is hidden.

As of <small>(v0.19)</small>  the result defaults to a parametric (linked) copy.

This behavior can be changed in the <img alt="" src=images/Std_DlgParameter.svg  style="width:24px;"> [Parameter editor](Std_DlgParameter.md):

1.  Go to the subgroup: `BaseApp/Preferences/Mod/Part`
2.  Change `ParametricRefine` of type `Boolean` to `False` to get the old behavior (independent copy).

See other parameters in [Fine-tuning](Fine-tuning.md).




<div class="mw-translate-fuzzy">

## Note

-   funcția nu modifică forma existentă, dar returnează o nouă formă
-   funcția este folosită în mod normal ca ultim pas în istoricul de modelare
-   funcția poate ajuta la obținerea rotunjirilor dificile pentru de lucrat
-   funcția este destinată să împiedice imprimantele 3D să printeze marginile nedorite
-   funcția poate fi utilizată după transformarea unei rețele în formă pentru a curăța marginile reziduale pe fațetele plane.


</div>

-   This function can be used as the last step in the modelling work to clean up shapes in a traditional [constructive solid geometry](constructive_solid_geometry.md) workflow.
-   This function may help to clean up the model before applying another feature, such as a [Fillet](Part_Fillet.md).
-   This clean up may stop 3D printers from printing unwanted edges once the solid model is exported to a mesh format.
-   This function can also be used after converting a mesh to a shape ([ShapeFromMesh](Part_ShapeFromMesh.md)) to clean up the residual edges on flat faces.
-   Some interesting information about what is happening with placement and how to access by Python can be found in this [forum post](https://forum.freecad.org/viewtopic.php?t=77568#p675456).




<div class="mw-translate-fuzzy">

## Limitări

-   Algoritmul de rafinare funcționează numai pe cochilii. Prin urmare, acesta iterează peste cochilia formei de intrare și apoi pentru fiecare coajă creează o coajă nouă cu fațete fizionate ori de câte ori este posibil. Aceasta înseamnă că, dacă forma dvs. de intrare este doar o fațetă, un filament/polilinie sârmă, o margine sau un vârf, atunci algoritmul nu face nimic.
-   Spre deosebire de[RefineShapeFeature](OpenSCAD_RefineShapeFeature.md) în Atelierul OpenSCAD, această funcți(e)onalitate nu se va actualiza când se schimbă formele precedente.


</div>

-   The refinement algorithm only works on shells. Therefore it iterates over the shells of the input shape and then for each shell it creates a new shell with joined faces wherever possible. This means that if your input shape is only a face, wire, edge or vertex then the algorithm does nothing.
-   Unlike the <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [OpenSCAD RefineShapeFeature](OpenSCAD_RefineShapeFeature.md) command, <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part RefineShape](Part_RefineShape.md) won\'t update when the preceding shapes are changed.




<div class="mw-translate-fuzzy">

## Script

Comanda Python pentru rafinarea formei este următoarea:


</div>

The Python command for refining a shape is the following:


```python
shape.removeSplitter()
```



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/ro
