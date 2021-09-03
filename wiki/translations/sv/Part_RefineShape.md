---
- GuiCommand:/sv   Name:Part RefineShape   Name/sv:Part RefineShape   MenuLocation:Part → Refine Shape   Workbenches:[OpenSCAD](Part_Workbench/sv___Part]],_[[OpenSCAD_Workbench/sv.md)|SeeAlso:---


</div>

## Description

The **<img src="images/Part_RefineShape.svg" width=16px> [Part RefineShape](Part_RefineShape.md)** produces a non-parametric copy with a refined shape, that is, with certain edges and faces cleaned up.

After certain boolean operations, like [Part Fuse](Part_Fuse.md), some lines from the previous shapes may remain visible. This tool produces a copy of that boolean result, and cleans up those seams.

**Alternatively**, to produce other non-parametric copies use **<img src="images/Part_SimpleCopy.svg" width=16px> [Simple Copy](Part_SimpleCopy.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Transformed Copy](Part_TransformedCopy.md)**, and **<img src="images/Part_ElementCopy.svg" width=16px> [Element Copy](Part_ElementCopy.md)**

![](images/PartRefineShape_it.png )


<div class="mw-translate-fuzzy">

![](images/PartRefineShape_it.png )


</div>

## Usage

1.  Select an object that you wish to clean and copy.
2.  Go to the menu {{MenuCommand|Part → Create a copy → <img src="images/Part_RefineShape.svg" width=16px> Refine shape}}.
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

## Limitations

-   The refinement algorithm only works on shells. Therefore it iterates over the shells of the input shape and then for each shell it creates a new shell with joined faces wherever possible. This means that if your input shape is only a face, wire, edge or vertex then the algorithm does nothing.
-   Unlike the <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [OpenSCAD RefineShapeFeature](OpenSCAD_RefineShapeFeature.md) command, <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part RefineShape](Part_RefineShape.md) won\'t update when the preceding shapes are changed.

## Scripting

The Python command for refining a shape is the following:


```python
shape.removeSplitter()
```

The **Part RefineShape** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Part_RefineShape')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





 
