# Part RefineShape/cs
---
- GuiCommand:   Name:Part RefineShape   Name/cs:Díl Vyčistit tvar   MenuLocation:Díl - Vyčistit tvar   Workbenches:[OpenSCAD](Part_Workbench/cs___Díl]],__[[OpenSCAD_Workbench/cs.md)|SeeAlso:---


</div>




<div class="mw-translate-fuzzy">

## Popis

Vyčistí zbytečné čáry. Po logických operacích zůstávají viditelné čáry, které definovaly původní tvary. Nástroj vytváří kopii vyčištěného objektu.


</div>

The **<img src="images/Part_RefineShape.svg" width=16px> [Part RefineShape](Part_RefineShape.md)** produces a non-parametric copy with a refined shape, that is, with certain edges and faces cleaned up.

After certain boolean operations, like [Part Fuse](Part_Fuse.md), some lines from the previous shapes may remain visible. This tool produces a copy of that boolean result, and cleans up those seams.

**Alternatively**, to produce other non-parametric copies use **<img src="images/Part_SimpleCopy.svg" width=16px> [Simple Copy](Part_SimpleCopy.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Transformed Copy](Part_TransformedCopy.md)**, and **<img src="images/Part_ElementCopy.svg" width=16px> [Element Copy](Part_ElementCopy.md)**

![](images/PartRefineShape_it.png ) 
*Original boolean result with 11 faces (left), and refined shape copy with 7 faces (right).*




<div class="mw-translate-fuzzy">

## Použití

1.  Vyberte tvar, který má být vyčištěn.
2.  Klikněte na menu **Díl → Vyčistit tvar**.

-   Je vytvořena kopie objektu a je kompletně vyčištěna, původní objekt je skryt.
-   Nově vytvořená kopie je nezávislá na originálu.


</div>

1.  Select an object that you wish to clean and copy.
2.  Go to the menu **Part → Create a copy → <img src="images/Part_RefineShape.svg" width=16px> Refine shape**.
3.  A cleaned, independent copy of the original object is created; the original object is hidden.

As of <small>(v0.19)</small>  the result defaults to a parametric (linked) copy.

This behavior can be changed in the <img alt="" src=images/Std_DlgParameter.svg  style="width:24px;"> [Parameter editor](Std_DlgParameter.md):

1.  Go to the subgroup: `BaseApp/Preferences/Mod/Part`
2.  Change `ParametricRefine` of type `Boolean` to `False` to get the old behavior (independent copy).

See other parameters in [Fine-tuning](Fine-tuning.md).

## Notes

-   This function can be used as the last step in the modelling work to clean up shapes in a traditional [constructive solid geometry](constructive_solid_geometry.md) workflow.
-   This function may help to clean up the model before applying another feature, such as a [Fillet](Part_Fillet.md).
-   This clean up may stop 3D printers from printing unwanted edges once the solid model is exported to a mesh format.
-   This function can also be used after converting a mesh to a shape ([ShapeFromMesh](Part_ShapeFromMesh.md)) to clean up the residual edges on flat faces.
-   Some interesting information about what is happening with placement and how to access by Python can be found in this [forum post](https://forum.freecad.org/viewtopic.php?t=77568#p675456).

## Limitations

-   The refinement algorithm only works on shells. Therefore it iterates over the shells of the input shape and then for each shell it creates a new shell with joined faces wherever possible. This means that if your input shape is only a face, wire, edge or vertex then the algorithm does nothing.
-   Unlike the <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [OpenSCAD RefineShapeFeature](OpenSCAD_RefineShapeFeature.md) command, <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part RefineShape](Part_RefineShape.md) won\'t update when the preceding shapes are changed.

## Scripting

The Python command for refining a shape is the following:


```python
shape.removeSplitter()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/cs
