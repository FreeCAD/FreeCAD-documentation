---
 GuiCommand:
   Name: Sketcher ToggleConstruction
   Name/pt: Ativa/desativa a geometria de construção
   Icon: Sketcher_AlterConstruction.svg
   Workbenches: Sketcher Workbench/pt
   MenuLocation: Sketch , Geometrias do Sketcher , Ativa/desativa a geometria de construção
---

# Sketcher ToggleConstruction/pt


</div>

## Description

This tool toggles sketch geometry from/to construction mode. It affects all geometry.

Construction geometry is an important tool of the sketcher. When using a sketch for a 3D operation, construction geometry is ignored.

In **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [Edit sketch](Sketcher_EditSketch.md)**, construction geometry is shown as blue, and won\'t turn green when a sketch is fully constrained. Once you **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Leave sketch](Sketcher_LeaveSketch.md)**, construction geometry is hidden in the [3D view](3D_view.md).

Construction lines can be used as rotation axis by the **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Revolution](PartDesign_Revolution.md)** feature.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">

## Usage

There are two ways of using this tool:

1.  Without having anything selected in the [3D view](3D_view.md):
    -   Invoke construction mode by clicking on the **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** button or by using the **Sketch → Sketcher geometries → [<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> Toggle construction geometry** entry in the Sketcher menu.
    -   This will change the color for creating new geometric elements to blue.
    -   Newly created geometric elements will now be created in construction mode.
2.  With one or more geometric elements selected in the [3D view](3D_view.md)
    -   Invoke the tool by clicking on the **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** button or by selecting it from the menu
    -   The selected elements will now be changed to construction mode.
    -   Afterwards newly created elements will again be normal geometry.

## Notes

-    **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Create point](Sketcher_CreatePoint.md)**will always create points in construction mode regardless of the toolbar toggle state, select the desired points in the [3D view](3D_view.md) after creation and click **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** to change them to normal geometry.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/pt
