---
- GuiCommand:
   Name:Std BoxSelection
   MenuLocation:[Edit](Std_Edit_Menu.md) → Box Selection
   Workbenches:All
   Shortcut:Shift + B
   SeeAlso:[Fit Selection](Std_ViewFitSelection.md)
---

# Std BoxSelection/ro


</div>


<div class="mw-translate-fuzzy">

## Descriere

Vă permite să delimitați o zonă dreptunghiulară în spațiul de lucru și să selectați toate elementele din interiorul acestei zone.


</div>

The **Std BoxSelection** command selects objects from a user defined rectangular area, a box, in the [3D view](3D_view.md).

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

-   Alegeți ** Edit** → **<img src="images/Std_BoxSelection.png" width=24px> Box selection** din meniul principal.
-   Plasați cursorul mouse-ului în zona de lucru și desenați un dreptunghi din STÂNGA spre dreapta pentru a selecta numai obiectele aflate INTEGRAL din interiorul dreptunghiului.
-   Plasați indicatorul mouse-ului în zona de lucru și desenați un dreptunghi din DREAPTA în stânga pentru a selecta obiectele din interiorul dreptunghiului și cele traversate de dreptunghi.


</div>

## Notes

-   Use the [Std BoxElementSelection](Std_BoxElementSelection.md) command to box select faces instead of objects.
-   This command cannot be used to select elements in a [sketch](sketch.md). To \'box select\' when the [Sketcher Dialog](Sketcher_Dialog.md) is open:
    1.  Make sure that no command is active.
    2.  Do one of the following:
        -   Click in an empty area and drag a rectangle from left to right to select objects that lie completely inside the rectangle.
        -   Click in an empty area and drag a rectangle from right to left to also select objects that touch or cross the rectangle.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std BoxSelection/ro
