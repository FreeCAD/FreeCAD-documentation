---
- GuiCommand:
   Name: Arch Panel   Name/uk: Arch Panel
   MenuLocation: Arch - Panel
   Workbenches: [Arch](Arch_Workbench/uk.md)
   Shortcut: **P** **A**
   SeeAlso: [Arch Structure](Arch_Structure/uk.md), [Arch Panel Cut](Arch_Panel_Cut/uk.md), [Arch Panel Sheet](Arch_Panel_Sheet/uk.md)
   Version: 0.15
---

# Arch Panel/uk


</div>

## Description

This tool allows you to build all kinds of panel-like elements, typically for panel constructions like the [WikiHouse](http://www.wikihouse.cc/) project, but also for all kinds of objects that are based on a flat profile.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*The above image shows a series of panel objects, simply made from imported 2D contours from a DXF file. They can then be rotated and assembled to create structures.*

Since version <small>(v0.17)</small>  the Arch Panel can also be used to create corrugated or trapezoidal profiles:

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">

## Usage

1.  Select a 2D shape (Draft object, face or sketch) - optional.
2.  Press the **<img src="images/Arch_Panel.svg" width=16px> [Arch Panel](Arch_Panel.md)** button, or press **P** then **A** keys.
3.  Adjust the desired properties.

### Limitations

-   There is currently no automatic system to produce 2D cutting sheets from panel objects, but such feature is in the plans and will be added in the future.

## Options

-   Panels share the common properties and behaviours of all [Arch Components](Arch_Component.md).
-   The thickness of a panel can be adjusted after creation.
-   Press **Esc** or the **Cancel** button to abort the current command.
-   Double-clicking on the panel in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions.
-   It is possible to automatically make panels composed of more than one sheet of a material, by raising its Sheets property.
-   Panels can make use of <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the panel will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Panel\'s own Thickness value, after subtracting the other layers.

## Properties

-    **Length**: The length of the panel

-    **Width**: The width of the panel

-    **Thickness**: The thickness of the panel

-    **Area**: The area of the panel (automatic)

-    **Sheets**: The number of sheets of material the panel is made of

-    **Wave Length**: The length of the wave for corrugated panels

-    **Wave Height**: The height of the wave for corrugated panels

-    **Wave Type**: The type of the wave for corrugated panels, curved, trapezoidal or spiked

-    **Wave Direction**: The orientation of the waves for corrugated panels

-    **Bottom Wave**: If the bottom wave of the panel is flat or not

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Panel tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Creates a `Panel` object from the given `baseobj`, which is a closed profile, and the given extrusion `thickness`.
    -   If no `baseobj` is given, you can provide the numerical values for the `length`, `width`, and `thickness` to create a block panel.
-   If a `placement` is given, it is used.

Example: 
```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```

## Tutorials

-   [Wikihouse porting tutorial](Wikihouse_porting_tutorial.md)


<div class="mw-translate-fuzzy">


{{docnav/uk|[Arch CompPanel](Arch_CompPanel.md)|[Panel Cut](Arch_Panel_Cut.md)|[Arch](Arch_Workbench.md)|IconL=Arch_CompPanel.png |IconC=Workbench_Arch.svg |IconR=Arch_Panel_Cut.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel/uk
