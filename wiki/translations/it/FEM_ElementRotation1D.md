# FEM ElementRotation1D/it
---
 GuiCommand:   Name: FEM_ElementRotation1D   Name/it: Rotazione di trave   Icon: Fem-beam-rotation.svg   MenuLocation:  Modello , Rotazione di trave   ---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione


</div>

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo


</div>

## Properties


**Rotation**

: specifies the angle of rotation.

## Limitations

-   Currently, multiple rotations are not supported (a single rotation is applied to all beams in the model).

## Notes

-   To visualize the rotated cross-section it is necessary to set `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) to `True` and run the analysis.
-   This feature uses the [\*BEAM SECTION card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/it
