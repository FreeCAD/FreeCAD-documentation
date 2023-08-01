# Part Cut/cs
---
- GuiCommand:   Name:Part Cut   Name/cs:Díl Oddělit   MenuLocation:Díl → Oddělit   Workbenches:[SeeAlso:[[Part Union/cs|Díl Sjednotit](Part_Workbench/cs___Díl]].md), [Díl Společné](Part_Common/cs.md)---


</div>




<div class="mw-translate-fuzzy">

Usekává (odděluje) vybrané objekty Díl tak, že později vybraný díl vyjme z dříve vybraného dílu. Tato operace je plně parametrická a komponenty mohou být upravovány a výsledek přepočítáván.


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

Input objects must be [OpenCASCADE](OpenCASCADE.md) shapes. For example objects made with the Part, PartDesign or Sketcher workbenches. For meshes there are dedicated Boolean tools in [Mesh Workbench](Mesh_Workbench.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cut/cs
