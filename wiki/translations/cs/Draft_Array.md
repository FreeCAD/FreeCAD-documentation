# Draft Array/cs
---
- GuiCommand:   Name: Draft_Array   Name/cs: Kreslení Pole   Workbenches: [Architektura](Draft_Workbench/cs___Kreslení]],_[[Arch_Workbench/cs.md)|MenuLocation: Draft - Array   SeeAlso: [PathArray](Draft_PathArray/cs.md)---


</div>




<div class="mw-translate-fuzzy">

## Popis

Nástroj Pole vytváří ortogonální (3-osy) nebo polární pole z vybraných objektů. Není-li vybrán žádný objekt, budete vyzváni k jeho výběru.


</div>

The <img alt="" src=images/Draft_Array.svg  style="width:24px;"> **Draft Array** command creates an orthogonal (3-axes) array from a selected object. The created array can be turned into a [polar array](Draft_PolarArray.md) or a [circular array](Draft_CircularArray.md) by changing its **Array Type** property.

The command can be used on 2D objects created with the [Draft Workbench](Draft_Workbench.md) or [Sketcher Workbench](Sketcher_Workbench.md), but also on many 3D objects such as those created with the [Part Workbench](Part_Workbench.md), [PartDesign Workbench](PartDesign_Workbench.md) or [Arch Workbench](Arch_Workbench.md).

This command is now obsolete. Use the [Draft OrthoArray](Draft_OrthoArray.md), [Draft PolarArray](Draft_PolarArray.md) or [Draft CircularArray](Draft_CircularArray.md) command instead.

## Usage


<div class="mw-translate-fuzzy">

## Použití

1.  Vyberte objekt, ze kterého chcete udělat pole
2.  Stiskněte tlačítko **<img src="images/Draft_Array.png" width=16px> [Pole](Draft_Array/cs.md)**.

(pozn.překl.: Pro začátečníky jako jsem já - defaultně jsou intervaly X,Y a Z nastaveny na 1. Když pracujete v mm, tak to vypadá jakoby se pole nevytvořilo, protože se elementy překrývají. Je potřeba alespoň jeden index zvýšit minimálně na rozměr základního prvku.)


</div>

## Properties

See [Draft OrthoArray](Draft_OrthoArray#Properties.md).

## Scripting

See [Draft OrthoArray](Draft_OrthoArray#Scripting.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/cs
