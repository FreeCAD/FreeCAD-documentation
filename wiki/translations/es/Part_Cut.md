---
- GuiCommand:/es   Name:Part_Cut   Name/es:Part Cut   MenuLocation:Part → Cut   Workbenches:[Complete](Part_Workbench/es___Part]],[[Complete_Workbench/es.md)|SeeAlso:[Part Union](Part_Union/es.md), [Part Common](Part_Common/es.md)---


</div>


<div class="mw-translate-fuzzy">

Corta (resta) los objetos Pieza seleccionados, el último será sustraído del primero. Esta operación es completamente paramétrica y los componentes pueden ser modificados y el resultado recalculado.


</div>

Cuts (subtracts) selected Part objects, the last one being subtracted from the first one. This operation is fully parametric and the components can be modified and the result recomputed.

**Note:** This command is an automated form of the <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Boolean operation](Part_Boolean.md).

[480px\|left\|Cut](IMAGE:Part_Cut_01.png.md)

## Usage

1.  Select two shapes
2.  Invoke the Part Cut command several ways:
    -   Press the **![](images/) '''Cut'''** button in the Part toolbar
    -   Use the **Part → Boolean → Cut** entry from the Part menu

## Supported inputs 

Input objects must be [OpenCascade](OpenCascade.md) shapes. Examples: stuff made with Part, PartDesign, Sketcher workbenches. Not meshes (unless those were converted to shapes) - for meshes, there are specific Boolean tools in MeshDesign workbench.





  
