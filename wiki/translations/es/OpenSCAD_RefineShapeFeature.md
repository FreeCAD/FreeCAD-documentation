---
- GuiCommand:/es   Name:OpenSCAD RefineShapeFeature   Name/es:OpenSCAD RefineShapeFeature   MenuLocation:OpenSCAD → Refine Shape Feature   Workbenches:[[OpenSCAD_Workbench/es   OpenSCAD]]|SeeAlso:..---


</div>

## Description

Cleans unnecessary lines. After a Boolean operation some lines defining the previous form remain visible, this tool creates a copy of the totally cleaned.

![](images/PartRefineShape_it.png )

## Usage

1.  Select the shape to be cleaned.
2.  Click the **OpenSCAD → Refine shape** menu.

-   A parent-object is created and totally cleaned, the original object is rendered hidden.

## Limitations

-   The refinement algorithm only works on shells. Therefore it iterates over the shells of the input shape and then for each shell it creates a new shell with joined faces wherever possible. This means if your input shape is only a face, wire, edge or vertex then the algorithm does nothing.
-   As opposed to <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part RefineShape](Part_RefineShape.md) in the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) workbench, this feature **WILL** update when the underlying shapes are changed.

## Notes

-   the function does not modify the existing shape, but returns a new shape
-   the function is normally used as last step in the modelling history
-   the function can help to get difficult fillets to work
-   the function is intended to stop 3D printers from printing unwanted edges





{{OpenSCAD_Tools_navi

}} 
