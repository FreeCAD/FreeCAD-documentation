---
 GuiCommand:Container|
{{GuiCommand
   Name: FEM ElementRotation1D
   MenuLocation: Model , Element Geometry , Beam rotation
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ElementRotation1D/pt-br

## Description


<div class="mw-translate-fuzzy">

## Descrição


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilização


</div>

## Properties


**Rotation**

: specifies the angle of rotation.

## Limitations

-   Currently, multiple rotations are not supported (a single rotation is applied to all beams in the model).

## Notes

-   To visualize the rotated cross-section it is necessary to set `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) to `True` and run the analysis.
-   This feature uses the [\*BEAM SECTION card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/pt-br
