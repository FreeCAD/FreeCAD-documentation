# PartDesign SubtractiveWedge/ro
---
- GuiCommand:   Name: PartDesign SubtractiveWedge   Workbenches: [MenuLocation: Part Design - Create a subtractive primitive - Subtractive Wedge   Shortcut: None   SeeAlso: [[PartDesign CompPrimitiveSubtractive](PartDesign_Workbench___PartDesign]].md)---


</div>

## Descriere

Se introduce o pană subtractivă în corpul activ. Forma sa este scăzută de solidul existent.

![](images/PartDesign_SubtractiveWedge_example.svg ) *În stânga, corpul activ (A) în gri și pana substractivă (B) în roșu transparent; rezultatul final este în partea dreaptă.*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Press the **<img src="images/PartDesign_SubtractiveWedge.png" width=24px> '''Subtractive Wedge'''** button. **Note**: Wedge-ul subtractiv face parte dintr-un meniu de iconițe *Create an additive primitive*. După lansarea FreeCAD, Subtractive Box este afișată în toolbar. Pentru a obține Wedge, faceți clic pe săgeată pentru a vizualiza Wedge subtractive din meniu.
2.  Definițăi parametrii Primitivei și [Attachment](Part_EditAttachment.md).
3.  Click **OK**.
4.  O funcționalitate Wedge apare sub corpul (Body) activ.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

Pana(Wedge) poate fi editată după crearea ei în douăî moduri:

-   Dublu-clicking în arborescența Model, sau prin clic drapta și selectarea **Edit primitive** ăn meniul contextula; aceasta aduce parametrii Primitive .
-   Via [Property editor](Property_editor.md).


</div>

## Proprietăți

Utilizarea plasamentului implicit, intrările de mai jos sunt:

-    **X min/max**: Base face X axis span

-    **Y min/max**: Wedge height span

-    **Z min/max**: Base face Z axis span

-    **X2 min/max**: Top face X axis span

-    **Z2 min/max**: Top face Z axis span

Nu există o valoare Y pentru vârf, astfel încât poziția sa o să fie 0 în mod implicit.

## Pyramids

Wedges can be used to create pyramids by setting **X2 min/max** and **Z2 min/max** each so that min = max.





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveWedge/ro
