---
 GuiCommand:
   Name: Sketcher CarbonCopy
   MenuLocation: Sketch , Sketcher tools , Create carbon copy
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy/hr

## Description

The <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:24px;"> [Sketcher CarbonCopy](Sketcher_CarbonCopy.md) tool copies all geometry and constraints from another sketch into the active sketch.

Dimensional constraints which exist before the copy function remain linked to the original sketch\'s dimensional constraints through [expressions](Expressions.md).

## Usage

1.  Make sure you are in the edit mode of an existing [sketch](Sketcher_NewSketch.md). This sketch is the target of the operation.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CarbonCopy.svg" width=16px> [Create carbon copy](Sketcher_CarbonCopy.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_CarbonCopy.svg" width=16px> Create carbon copy** option from the menu.
    -   Use the keyboard shortcut: **G** then **W**.
3.  The cursor changes to a cross with the tool icon.
4.  Pick an edge from another sketch. This sketch is the source of the operation. See [Notes](#Notes.md).
5.  Geometry elements as well as constraints are copied into the active sketch.
6.  This tool always runs in continue mode: optionally copy additional sketches.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   In the [PartDesign Workbench](PartDesign_Workbench.md) it is possible to select the sketch to carbon copy from outside the [Body](PartDesign_Body.md) of the currently active sketch, but only if the **Ctrl** key is held down during selection.
-   The sketch to carbon copy should be plane-parallel to the currently active sketch. If that is not the case the **Ctrl** and **Alt** keys must be held down during selection. This works for sketches located outside the active Body as well.
-   If [construction mode](Sketcher_ToggleConstruction.md) is active, copied geometry is created as construction geometry.
-   The complete sketch is copied, it is not possible to select only a portion. But after copying you can delete unwanted elements.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/hr
