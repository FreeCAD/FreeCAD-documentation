---
- GuiCommand:/cs
   Name:Sketcher ToggleConstruction
   Name/cs: Skicář Změna konst.módu
   Icon:Sketcher_AlterConstruction.svg
   Workbenches:[Skicář](Sketcher_Workbench/cs.md)
   MenuLocation:Náčrt → Skicář Konstrukce →  Změna konst.módu
---

# Sketcher ToggleConstruction/cs


</div>

## Popis

Tento nástroj přepíná náčrt konstrukce do a z konstrukčního módu. Může to být použito na jakýkoliv typ konstrukce: přímka, oblouk nebo kružnice.


<div class="mw-translate-fuzzy">

Konstrukční mód je důležitý nástroj Náčrtu. Při použití náčrtu ve 3D je konstrukční mód ignorován.


</div>


<div class="mw-translate-fuzzy">

V editačním módu náčrtu jsou podpůrné konstrukce zobrazeny modře a nezezelenají když je náčrt plně zavazben. Když ukončíte konstrukční mód, podpůrné konstrukce jsou na displeji skryty.


</div>


<div class="mw-translate-fuzzy">

**Poznámka:** od verze v0.13, mohou být pomocné přímky použity nástrojem [Návrh dílu Obtáčení](PartDesign_Revolution/cs.md).


</div>

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

-   Vyberte jeden nebo více náčrtů konstrukcí ve 3D pohledu a klikněte na tento nástroj nebo ho použijte prostřednictvím menu.


</div>

## Příklad

Use Construction mode on some sketch elements,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">

and once you **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [leave the sketcher editing mode](Sketcher_LeaveSketch.md)**, geometry that was turned into construction have become invisible in the [3D view](3D_view.md) (but are still present in the Sketcher editing mode).

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">

## Notes

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Create Point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** to change them to normal geometry. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">


</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/cs
