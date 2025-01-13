---
 GuiCommand:
   Name: Sketcher Intersection
   MenuLocation: Sketch , Sketcher tools , Create external intersection geometry
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **I**
   Version: 1.1
   SeeAlso: Sketcher_ToggleConstruction
---

# Sketcher Intersection/en

## Description

The <img alt="" src=images/Sketcher_Intersection.svg  style="width:24px;"> [Sketcher Intersection](Sketcher_Intersection.md) tool intersects faces and/or edges belonging to objects outside the sketch with the sketch plane. The intersected geometry is called \"external geometry\". It stays parametrically linked to its source objects. External geometry is marked with a dedicated [color](Sketcher_Preferences#Appearance.md) (default magenta) and linetype. It can be defining geometry that is visible outside the sketch or construction geometry that is not visible outside the sketch.

## Usage

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Intersection.svg" width=16px> [Create external intersection geometry](Sketcher_Intersection.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_Intersection.svg" width=16px> Create external intersection geometry** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_Intersection.svg" width=16px> Create external intersection geometry** option from the context menu.
    -   Use the keyboard shortcut: **G** then **I**.
2.  The cursor changes to a cross with the tool icon.
3.  Select one or more external faces and/or edges. See [Notes](#Notes.md).
4.  External geometry is created.
5.  This tool always runs in continue mode: optionally keep selecting external faces and/or edges.
6.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   A face results in one or more edges, an edge in one or more points. Geometry not touching the sketch plane is ignored.
-   External geometry is created as defining geometry or construction geometry according to the status of the [Toggle construction geometry](Sketcher_ToggleConstruction.md) tool. This tool can also be used to toggle the mode of individual edges. Check the **Edit → Preferences... → Sketcher → General → Always add external geometry as reference** option to ignore the status of this tool and always add external geometry as construction geometry.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Intersection/en
