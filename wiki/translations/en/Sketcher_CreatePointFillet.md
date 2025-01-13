---
 GuiCommand:
   Name: Sketcher CreatePointFillet
   MenuLocation: Sketch , Sketcher geometries , Create corner-preserving fillet
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **F** **P**
   Version: 0.19
   SeeAlso: Sketcher_CreateFillet
---

# Sketcher CreatePointFillet/en

## Description

The <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:24px;"> [Sketcher CreatePointFillet](Sketcher_CreatePointFillet.md) tool creates a fillet between two non-parallel edges. If two straight edges connected by a [Coincident constraint](Sketcher_ConstrainCoincident.md) are filleted, the related common point is preserved by adding a [Point object](Sketcher_CreatePoint.md) that has a [Point onto object constraint](Sketcher_ConstrainPointOnObject.md) with both edges. Constraints connected to the common point are transferred to the new point object. Apart from that this tool is identical to the [Sketcher CreateFillet](Sketcher_CreateFillet.md) tool. See there for more information.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> [Corner-preserving sketch fillet](Sketcher_CreatePointFillet.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreatePointFillet.svg" width=16px> Create corner-preserving fillet** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> Create corner-preserving fillet** option from the context menu.
    -   Use the keyboard shortcut: **G** then **F**, then **P**.
2.  For further steps see [Sketcher CreateFillet](Sketcher_CreateFillet#Usage.md).

## Notes

See [Sketcher CreateFillet](Sketcher_CreateFillet#Notes.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePointFillet/en
