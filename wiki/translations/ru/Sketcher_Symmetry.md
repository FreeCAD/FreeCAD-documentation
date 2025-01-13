---
 GuiCommand:
   Name/ru: Симметрия
   Name: Sketcher_Symmetry
   MenuLocation: Sketch , Инструменты для эскиза , Симметрия
   Workbenches: Sketcher_Workbench/ru
   Version: 0.16
   SeeAlso: Sketcher_MirrorSketch/ru
---

# Sketcher Symmetry/ru


</div>



## Описание

The <img alt="" src=images/Sketcher_Symmetry.svg  style="width:24px;"> [Sketcher Symmetry](Sketcher_Symmetry.md) creates mirrored copies of selected elements.



## Применение

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  Select one or more edges and/or points.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Symmetry.svg" width=16px> [Symmetry](Sketcher_Symmetry.md)** button.
    -   Select the **Sketch → Sketcher tools → <img src="images/Sketcher_Symmetry.svg" width=16px> Symmetry** option from the menu.
    -   The keyboard shortcut: **Z** then **S**.
3.  The cursor changes to a cross with the tool icon.
4.  The **Symmetry parameters** section (<small>(v1.0)</small> ) is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Optionally press the **U** key or check the **Delete original geometries** checkbox to only keep the mirrored elements. <small>(v1.0)</small> 
6.  Optionally press the **J** key or check the **Create Symmetry constraints** checkbox to add a [Symmetric constraint](Sketcher_ConstrainSymmetric.md) between each original and mirrored point. <small>(v1.0)</small> 
7.  Select a line or a sketch axis to define the symmetry line, or a point to define the symmetry point.
8.  Mirrored copies are created. Constraints restricted to the selected elements are also processed.
    -   If **Create Symmetry constraints** has been selected Symmetric constraints are added.
    -   If **Delete original geometries** has been selected the original geometry is removed.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Symmetry/ru
