---
- GuiCommand:/es
   Name/es:Part Union
   Icon:Part Fuse.png
   MenuLocation:Part → Boolean → Union
   Workbenches:[Part](Part_Workbench/es.md)
   SeeAlso:[Part Cut](Part_Cut/es.md), [Part Common](Part_Common/es.md)
---

# Part Fuse/es


</div>

## Descripción

Fusiona (unión) los objetos Pieza seleccionados en uno. Esta operación es completamente paramétrica y los componentes pueden ser modificdos y el resultado recalculado.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

## Usage

1.  Select two or more shapes
2.  There are several ways to invoke the command:
    -   Press the **![](images/) Part Fuse** button in the **Part tools** toolbar
    -   Use the **Part → Boolean → Union** entry in the Part menu

## Supported inputs 

Input objects must be [OpenCascade](OpenCascade.md) shapes. Examples: stuff made with Part, PartDesign, Sketcher workbenches. Not meshes (unless those were converted to shapes) - for meshes, there are specific Boolean tools in MeshDesign workbench.

-   Solid + Solid: the result is a solid that occupies all the volume covered by the inputs

-   Shell + Shell, Shell + Face, Face + Face: the result is a shell. Where faces intersect, they are split. Shells can be non-manifold. After fusion, faces can be united by [Refining](Part_RefineShape.md) the result.

-   Wire + Wire, Edge + Wire, Edge + Edge: the result is a wire. Edges are split where they intersect.

Compounds are supported; however, it is assumed that shapes packed into a compound do not touch or intersect. If they actually do, Fusion will likely fail, or produce an incorrect result.

## Options

Items can be added and removed from the fusion, by dragging them in or out of the fusion feature in the tree view with the mouse. A manual recompute (press **F5** key or click on the <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Refresh/Recompute](Std_Refresh.md) icon) is required to see the results.

After this operation is complete, it may be necessary to clean up the shape with <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [RefineShape](Part_RefineShape.md).

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/es
