---
 GuiCommand:
   Name: Sketcher Projection
   MenuLocation: Sketch , Sketcher tools , Create external projection geometry
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **X**
   Version: 1.1
   SeeAlso: Sketcher_ToggleConstruction
---

# Sketcher Projection/en

## Description

The <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Sketcher Projection](Sketcher_Projection.md) tool projects edges and/or vertices belonging to objects outside the sketch onto the sketch plane. The projected geometry is called \"external geometry\". It stays parametrically linked to its source objects. External geometry is marked with a dedicated [color](Sketcher_Preferences#Appearance.md) (default magenta) and linetype. It can be defining geometry that is visible outside the sketch or construction geometry that is not visible outside the sketch.

## Usage

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Projection.svg" width=16px> [Create external projection geometry](Sketcher_Projection.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_Projection.svg" width=16px> Create external projection geometry** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_Projection.svg" width=16px> Create external projection geometry** option from the context menu.
    -   Use the keyboard shortcut: **G** then **X**.
2.  The cursor changes to a cross with the tool icon.
3.  Select one or more external faces, edges and/or vertices. See [Notes](#Notes.md).
4.  External geometry is created.
5.  This tool always runs in continue mode: optionally keep selecting external faces, edges and/or vertices.
6.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   All edges of a face are projected onto the sketch plane.
-   External geometry is created as defining geometry or construction geometry according to the status of the [Toggle construction geometry](Sketcher_ToggleConstruction.md) tool. This tool can also be used to toggle the mode of individual edges. Check the **Edit → Preferences... → Sketcher → General → Always add external geometry as reference** option to ignore the status of this tool and always add external geometry as construction geometry.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Projection/en
