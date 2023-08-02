---
- GuiCommand:
   Name: Part Compound‏‎
   Name/es: Pieza Compuesto‏‎
   MenuLocation: Pieza -> Hacer Compuesto
   Workbenches: Part Workbench/es
   Version: 0.14
   SeeAlso: Part Union/es, Part CompoundFilter/es, Part ExplodeCompound/es
---

# Part Compound/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

Este comando crea un compuesto de cualquier tipo de formas topológicas. Pueden ser sólidos o mallas o cualquier otro tipo de formas topológicas.


</div>

## Usage

1.  Mark the topological shapes to be added to the compound in the [tree view](Tree_view.md)
2.  Choose **Part → Compound → Make Compound** entry in the Part menu or click on the <img alt="" src=images/Part_Compound.svg  style="width:24px;"> button.

## Notes

A compound containing pieces that intersect or touch is **invalid** for Boolean operations. Because of performance issues, checking if the pieces intersect is not done by default. Automatic geometry check (available for Boolean operations) is disabled for part compound as well.

To turn this check on go to **Tools → Edit Parameters → Preferences... → Mod → Part → CheckGeometry → RunBOPCheck** and set the parameter to `true`.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Compound/es
