---
 GuiCommand:
   Name: Sketcher Scale
   MenuLocation: Sketch , Sketcher tools , Scale transform
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **P** **S**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Scale/en

## Description

The <img alt="" src=images/Sketcher_Scale.svg  style="width:24px;"> [Sketcher Scale](Sketcher_Scale.md) tool scales or optionally creates scaled copies of selected elements.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md).
Dim-OVP = Dimensional On-View-Parameters.

1.  Select one or more edges and/or [Point objects](Sketcher_CreatePoint.md). Constraints restricted to the selected elements are also processed. If the original elements are scaled, any other constraints associated with them will be deleted.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Scale.svg" width=16px> [Scale transform](Sketcher_Scale.md)** button.
    -   Select the **Sketch → Sketcher tools → <img src="images/Sketcher_Scale.svg" width=16px> Scale transform** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_Scale.svg" width=16px> Scale transform** option from the context menu.
    -   Use the keyboard shortcut: **Z** then **P**, then **S**.
3.  The cursor changes to a cross with the tool icon.
4.  The **Scale parameters** section is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Optionally press the **U** key or check the **Keep original geometries** checkbox to create scaled copies of the selected elements.
6.  Pick the base point for the scale operation. Or with Pos-OVP: enter its X and/or Y coordinate.
7.  Pick the end point of the first auxiliary line. Its angle and length are arbitrary.
8.  Pick the end point of the second auxiliary line. Its angle is also arbitrary. Its length relative to the length of the first auxiliary line defines the scale factor. Or with Dim-OVP: enter the scale factor.
9.  The original elements are scaled or scaled copies are created. No Pos-OVP or Dim-OVP based constraints are added.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Scale/en
