---
 GuiCommand:
   Name: Sketcher ToggleDrivingConstraint
   MenuLocation: Sketch , Sketcher constraints , Toggle driving/reference constraint
   Workbenches: Sketcher_Workbench
   Shortcut: **K** **X**
   Version: 0.16
   SeeAlso: Sketcher_ToggleActiveConstraint
---

# Sketcher ToggleDrivingConstraint/en

## Description

The <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:24px;"> [Sketcher ToggleDrivingConstraint](Sketcher_ToggleDrivingConstraint.md) tool either toggles the [dimensional constraint creation tools](Sketcher_Workbench#Sketcher_CompDimensionTools.md) between driving and reference mode, or toggles selected dimensional constraints between those modes.

Contrary to driving constraints, reference constraints do not constrain the sketch, their value depends on other constraints, they are driven. They can be useful to verify measurements. They can be used in [expressions](Expressions.md), but not in the sketch itself.

![](images/Sketcher_ToggleConstraint_example.png ) 
*A driving horizontal distance constraint (50 mm), a driving vertical distance constraint (30 mm) and a driving angle constraint (75°) were set to define the profile; a reference dimension was added on the slanted line segment to know its length (31.0583 mm).*

## Usage

### Toggle tools 

1.  Make sure no dimensional constraints have been selected.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> [Toggle driving/reference constraint](Sketcher_ToggleDrivingConstraint.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Toggle driving/reference constraint** option from the menu.
    -   Use the keyboard shortcut: **K** then **X**.
3.  The mode of the dimensional constraint creation tools is toggled:
    -   In driving mode their menu and toolbar icons are red, and they create driving constraints (default [color](Sketcher_Preferences#Appearance.md) red). The icon of this tool is then: <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:16px;">.
    -   In reference mode their menu and toolbar icons are blue, and they create reference constraints (default color blue). The icon of this tool is then: <img alt="" src=images/Sketcher_ToggleConstraint_Driven.svg  style="width:16px;">.

### Toggle constraints 

1.  Select one or more dimensional constraints.
2.  Invoke the tool as described above, or with one of the following additional options:
    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Toggle driving/reference constraint** option from the context menu.

    -   Right-click in the **Constraints** section of the [Sketcher Dialog](Sketcher_Dialog.md) and select the **Toggle to/from reference** option from the context menu.
3.  The selected constraints are changed from driving to reference mode or vice versa. Their appearance changes accordingly.
4.  The mode of the dimensional constraint creation tools is not changed.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/en
