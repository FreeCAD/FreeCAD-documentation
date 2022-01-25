---
- GuiCommand:
   Name:Sketcher ToggleConstruction
   MenuLocation:Sketch → Sketcher geometries → Toggle construction geometry
   Workbenches:[Sketcher](Sketcher_Workbench.md)
   SeeAlso:[Sketcher ToggleDrivingConstraint](Sketcher_ToggleDrivingConstraint.md)
---

# Sketcher ToggleConstruction/en

## Description

This tool toggles sketch geometry from/to construction mode. It can be used on any type of geometry: line, arc or circle.

Construction geometry is an important tool of the sketcher. When using a sketch for a 3D operation, construction geometry is ignored.

In **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [Edit sketch](Sketcher_EditSketch.md)**, construction geometry is shown as blue, and won\'t turn green when a sketch is fully constrained. Once you **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Leave sketch](Sketcher_LeaveSketch.md)**, construction geometry is hidden in the [3D view](3D_view.md).

Construction lines can be used as rotation axis by the **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Revolution](PartDesign_Revolution.md)** feature.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">

## Usage

There are two ways of using this tool:

1.  Without having anything selected in the [3D view](3D_view.md):
    -   Invoke construction mode by clicking on the **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** or by using the **Sketch → Sketcher geometries → [<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> Toggle construction geometry** entry in the Sketcher menu.
    -   This will change the color for creating new geometric elements to blue.
    -   Newly created geometric elements will now be created in construction mode.
2.  With one or more geometric elements selected in the [3D view](3D_view.md)
    -   Invoke the Sketcher ToggleConstruction tool by clicking on the **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** or by selecting it from the menu
    -   The selected elements will now be changed to construction mode.
    -   Afterwards newly created elements will again be normal geometry.

## Example

Use Construction mode on some sketch elements,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">

and once you **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [leave the sketcher editing mode](Sketcher_LeaveSketch.md)**, geometry that was turned into construction have become invisible in the [3D view](3D_view.md) (but are still present in the Sketcher editing mode).

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">

## Notes

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Create Point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction](Sketcher_ToggleConstruction.md)** to change them to normal geometry. <small>(v0.19)</small> 





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/en
