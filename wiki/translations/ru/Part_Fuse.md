---
 GuiCommand:
   Name/ru: Part Union
   Icon: Part Fuse.svg
   MenuLocation: Деталь , Булевы операции , Объединение
   Workbenches: Part_Workbench/ru
   SeeAlso: Part Cut/ru, Part Common/ru, Part Boolean/ru
---

# Part Fuse/ru

## Описание

The **![](images/)_[Part_Fuse](Part_Fuse.md)** tool fuses (unites) selected Part objects into one. This operation is fully parametric and the components can be modified and the result recomputed.

**Примечание:** Эта команда - автоматизированная форма <img alt="" src=images/Part_Booleans.svg  style="width:24px;"> [Булевой операции](Part_Boolean/ru.md).

## Применение

1.  Select two or more shapes
2.  There are several ways to invoke the command:
    -   Press the **![](images/) Part Fuse** button in the **Part tools** toolbar
    -   Use the **Part → Boolean → Union** entry in the Part menu

## Supported inputs 

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. Examples: stuff made with Part, PartDesign, Sketcher workbenches. Not meshes (unless those were converted to shapes) - for meshes, there are specific Boolean tools in MeshDesign workbench.

-   Solid + Solid: the result is a solid that occupies all the volume covered by the inputs

-   Shell + Shell, Shell + Face, Face + Face: the result is a shell. Where faces intersect, they are split. Shells can be non-manifold. After fusion, faces can be united by [Refining](Part_RefineShape/ru.md) the result.

-   Wire + Wire, Edge + Wire, Edge + Edge: the result is a wire. Edges are split where they intersect.

Compounds are supported; however, it is assumed that shapes packed into a compound do not touch or intersect. If they actually do, Fusion will likely fail, or produce an incorrect result.

## Options

Items can be added and removed from a fusion, by dragging them in or out of the fusion feature in the tree view with the mouse. To drag items out of a fusion you have to drop them onto the document node (the filename) of your model. A manual recompute (press **F5** key or click on the <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Refresh/Recompute](Std_Refresh.md) icon) is required to see the results.

После завершения этой операции может оказаться полезным уточнить форму с помощью команды <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Уточнить форму](Part_RefineShape/ru.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/ru
