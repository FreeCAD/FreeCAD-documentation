---
- GuiCommand:
   Name:Part Fuse
   MenuLocation:Part → Boolean → Union
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part Boolean](Part_Boolean.md), [Part Cut](Part_Cut.md), [Part Common](Part_Common.md)
---

# Part Fuse/pt-br

## Description

The **![](images/)_[Part_Fuse](Part_Fuse.md)** tool fuses (unites) selected Part objects into one. This operation is fully parametric and the components can be modified and the result recomputed.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

## Usage

1.  Select two or more shapes
2.  There are several ways to invoke the command:
    -   Press the **![](images/) Part Fuse** button in the **Part tools** toolbar
    -   Use the **Part → Boolean → Union** entry in the Part menu

## Supported inputs 

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. Examples: stuff made with Part, PartDesign, Sketcher workbenches. Not meshes (unless those were converted to shapes) - for meshes, there are specific Boolean tools in MeshDesign workbench.

-   Solid + Solid: the result is a solid that occupies all the volume covered by the inputs

-   Shell + Shell, Shell + Face, Face + Face: the result is a shell. Where faces intersect, they are split. Shells can be non-manifold. After fusion, faces can be united by [Refining](Part_RefineShape.md) the result.

-   Wire + Wire, Edge + Wire, Edge + Edge: the result is a wire. Edges are split where they intersect.

Compounds are supported; however, it is assumed that shapes packed into a compound do not touch or intersect. If they actually do, Fusion will likely fail, or produce an incorrect result.

## Options

Items can be added and removed from a fusion, by dragging them in or out of the fusion feature in the tree view with the mouse. To drag items out of a fusion you have to drop them onto the document node (the filename) of your model. A manual recompute (press **F5** key or click on the <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Refresh/Recompute](Std_Refresh.md) icon) is required to see the results.

After this operation is complete, it may be necessary to clean up the shape with <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [RefineShape](Part_RefineShape.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/pt-br
