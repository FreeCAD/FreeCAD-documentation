---
 GuiCommand:
   Name: Sketcher CarbonCopy
   MenuLocation: Sketch , Sketcher geometries , Create carbon copy
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy

## Description

The **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Sketcher CarbonCopy](Sketcher_CarbonCopy.md)** tool copies all the geometry and constraints from another sketch into the active sketch.

Dimensional constraints which exist before the copy function remain linked to the original sketch\'s dimensional constraints through [expressions](expressions.md).

## Usage

1.  Make sure you are in the edit mode of an existing **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketch](Sketcher_NewSketch.md)**. This sketch is the target of the operation.
2.  Press the **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Create carbon copy](Sketcher_CarbonCopy.md)** button.
3.  Click on an edge from another sketch. This sketch is the source of the operation.
4.  Geometry elements as well as constraints are copied into the active sketch.
5.  Press **Esc** or the right mouse button to terminate the operation.

## Notes

-   When sketches are used in the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md), normally the sketch to carbon copy should be in the same **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)** as the currently active sketch. If the sketch to be copied is not in the active [Body](PartDesign_Body.md), the mouse pointer will not allow selection. In this case, hold **Ctrl** to allow selection of sketches from other Bodies.
-   Normally, the sketch to select should be in a plane that is parallel to the currently active sketch. If the sketch to be copied is not parallel to the currently active sketch, hold **Ctrl**+**Alt** to allow selection of non-parallel sketches. The object will then be adjusted to the active sketch\'s plane. Noteː as of this writing this needs a save and reload of the document to make it visible. This works for sketches located outside of the currently active [Body](PartDesign_Body.md) as well.
-   Since carbon-copied dimensional constraints use expressions they are rendered in a different color. The color can be customized with the [Preferences Editor](Preferences_Editor.md) at **Edit → Preferences → Sketcher → Colors → Expression dependent constraint color**.
-   If the Sketcher mode has been changed to construction mode using **[<img src=images/Sketcher_ToggleConstruction.svg style="width:24px"> [Toggle construction geometry](Sketcher_ToggleConstruction.md)** all copied geometry will be created in construction mode.

## Limitations

-   The complete sketch is copied, it is not possible to select only a portion. However, after copying you can delete unwanted elements from the copied sketch.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy
