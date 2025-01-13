---
 GuiCommand:
   Name: Sketcher Translate
   MenuLocation: Sketch , Sketcher tools , Array transform
   Workbenches: Sketcher_Workbench
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Translate/it


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Sketcher_Translate.svg  style="width:24px;"> [Sketcher Translate](Sketcher_Translate.md) tool moves or optionally creates copies of selected elements. Copies are evenly distributes along one or two directions.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md).
Dim-OVP = Dimensional On-View-Parameters.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Move geometry 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select one or more edges and/or [Point objects](Sketcher_CreatePoint.md). Constraints restricted to the selected elements are also processed. Any other constraints associated with the elements will be deleted.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Translate.svg" width=16px> [Array transform](Sketcher_Translate.md)** button.
    -   Select the **Sketch → Sketcher tools → <img src="images/Sketcher_Translate.svg" width=16px> Array transform** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_Translate.svg" width=16px> Array transform** option from the context menu.
    -   Use the keyboard shortcut: **W**.
3.  The cursor changes to a cross with the tool icon.
4.  The **Translate parameters** section is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Pick the start point of the translation vector. Or with Pos-OVP: enter its X and/or Y coordinate.
6.  Pick the end point of the translation vector. Or with Dim-OVP: enter the length and/or angle of the vector. The angle is relative to the X axis of the sketch.
7.  The elements are moved. No Pos-OVP or Dim-OVP based constraints are added.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Copy geometry 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select one or more edges and/or [Point objects](Sketcher_CreatePoint.md). Constraints restricted to the selected elements are also processed.
2.  Invoke the tool as explained above.
3.  The cursor changes to a cross with the tool icon.
4.  The **Translate parameters** section is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Optionally change the number of **Copies** along the first vector:
    -   Enter a number.
    -   Press the **U** key to increase the number.
    -   Press the **J** key to decrease the number.
6.  Optionally change the number of **Rows** along the second vector:
    -   Enter a number.
    -   Press the **R** key to increase the number.
    -   Press the **F** key to decrease the number.
7.  Optionally check the **Apply equal constraints** checkbox to exclude dimensional constraints from the operation, and instead apply <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [Equal constraints](Sketcher_ConstrainEqual.md) between the original objects and their copies.
8.  Pick the start point of the first vector. Or with Pos-OVP: enter its X and/or Y coordinate. This vector defines the offset between copies.
9.  Pick the end point of the first vector. Or with Dim-OVP: enter the length and/or angle of the vector. The angle is relative to the X axis of the sketch.
10. If there are two or more rows: Pick the end point of the second vector. Or with Dim-OVP: enter the length and/or angle of the vector. The angle is relative to the X axis of the sketch. This vector defines the offset between rows.
11. The elements are copied. No Pos-OVP or Dim-OVP based constraints are added.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Translate/it
