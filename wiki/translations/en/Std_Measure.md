---
 GuiCommand:
   Name: Std Measure
   MenuLocation: Tools , Measure
   Workbenches: All
   Version: 1.0
   SeeAlso: Draft_Dimension
---

# Std Measure/en

## Description

The **Std Measure** command gives access to the Unified Measurement Facility. It replaces several previous measurement commands, providing a versatile measurement functionality.

## Usage

1.  Optionally preselect the entities to be measured.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Measure.svg" width=16px> [Std Measure](Std_Measure.md)** button.
    -   Select the **Tools → <img src="images/Std_Measure.svg" width=16px> Measure** option from the menu.
3.  The **Measurement** task panel opens. See [Options](#Options.md) for more information.
4.  If no geometrical entities were preselected, do one of the following:
    -   Select the geometrical entities while leaving the *Mode* as *Auto* so that the mode will be automatically determined based on the selection.
    -   Choose a *Mode* other than *Auto* and then select the geometrical entities (clicking on them again will deselect them):
        -   *Distance* - the shortest distance between the selected entities, if circular edges are selected then the distance between the centers of the circles is measured,
        -   *Distance Free* - distance between two freely selected points (belonging to different entities - edges, faces),
        -   *Angle* - angle between the selected entities,
        -   *Length* - length of the selected edge,
        -   *Position* - coordinates of the selected vertex,
        -   *Area* - area of the selected face,
        -   *Radius* - radius of the selected circular edge,
        -   *Center of Mass* - COM of the selected edge, face or solid (only if preselected in the tree).
5.  The measurement result will be shown in the *Result* field and on a label displayed in the [3D view](3D_view.md). That label will also include an icon indicating the type of measurement. The labels can be customized in the [Preferences](Preferences_Editor.md). They can be moved in the 3D view by dragging them with a cursor.
6.  Press the **Reset** button to delete the measurement or the **Save** button to keep it. Saved measurements are put in a Measurements [group](Std_Group.md) in the [Tree view](Tree_view.md).
7.  Press **Esc** or the **Close** button to finish the command.

## Options

-    <small>(v1.1)</small> Press the **<img src="images/Preferences-system.svg" width=x16px> <img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button to change the settings:

    -   *Auto Save* - if checked, the last measurement is saved when starting a new measurement (holding **Shift** can temporarily disable this behavior),
    -   *Additive Selection* - if checked, clicking on subsequent geometrical entities adds them as selections for the same measurement, otherwise **Ctrl** must be pressed to do this.

-   For the *Distance* and *Distance Free* modes the **Show Delta** checkbox is displayed. If this checkbox is checked, the **Show Delta** property of the measurement is set to `True` and 3 additional projected measurements are shown in the [3D view](3D_view.md).

## Properties

### Data


{{TitleProperty|Measurement}}

-    **Element1|LinkSub**: First element of the measurement.

-    **Element2|LinkSub**: Second element of the measurement.

-    **Distance|Distance**: Distance between the two elements.

-    **Distance X|Distance**: Distance in the X direction (only for *Distance* and *Distance Free* measurements).

-    **Distance Y|Distance**: Distance in the Y direction (idem).

-    **Distance Z|Distance**: Distance in the Z direction (idem).

-    **Position1|Vector|Hidden**: Position of the first measured point (read-only).

-    **Position2|Vector|Hidden**: Position of the second measured point (read-only).

### View


{{TitleProperty|Appearance}}

-    **Font Size|Integer**: Defines the font size for the label of the saved dimension.

-    **Line Color|Color**: Defines the color of the dimension lines displayed in 3D view.

-    **Show Delta|Bool**: If `True`, projected distance measurements are displayed in 3D view (only for *Distance* and *Distance Free* measurements).

-    **Text Background Color|Color**: Defines the background color of the dimension label.

-    **Text Color|Color**: Defines the color of the dimension label text and symbol.

## Notes

-   This command is the result of a [GSoC 2023 project](Unified_Measurement_Facility.md).



---
⏵ [documentation index](../README.md) > Std Measure/en
