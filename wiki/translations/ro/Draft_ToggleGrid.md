---
 GuiCommand:
   Name: Draft ToggleGrid
   Name/ro: Draft ToggleGrid
   MenuLocation: Draft , Utilities , Toggle grid
   Workbenches: Draft_Workbench/ro, Arch_Workbench/ro
   Shortcut: **G** **R**
   SeeAlso: Draft_Snap, Draft_Snap_Grid, Draft_SelectPlane
---

# Draft ToggleGrid/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Această comandă comută modul de ancorare la nodurile grilei Draft (if visible) on/off.


</div>


<small>(v0.22)</small> 

: Each [3D view](3D_view.md) has its own grid that can either always be visible, only be visible during commands, or invisible. The initial visibility of the grid in new views depends on the [preferences](#Preferences.md).

## Usage

1.  The command can be used while another command is active.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ToggleGrid.svg" width=16px> [Toggle grid](Draft_ToggleGrid.md)** button in the Draft snap toolbar.
    -   Press the **<img src="images/Draft_ToggleGrid.svg" width=16px> [Toggle grid](Draft_ToggleGrid.md)** button in the [Draft snap widget](Draft_snap_widget.md).
    -   Use the keyboard shortcut: **G** then **R**. This shortcut cannot be used if another command is active.
3.  The visibility of the grid belonging to the current 3D view has changed:
    -   If no other command is active:
        -   If the grid was invisible it is now always visible.
        -   If the grid was visible it is now no longer always visible, but the grid\'s visibility during commands remains unchanged.
    -   If another command is active:
        -   If the grid was invisible it is now only visible during commands.
        -   If the grid was visible it is now no longer visible during commands and no longer always visible.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   Several grid preferences are available: **Edit → Preferences... → Draft → Grid and snapping**.
-   To keep the grid when switching to other workbenches see [Fine-tuning](Fine-tuning#Draft_Workbench.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleGrid/ro
