---
- GuiCommand:
   Name: Arch_Rebar_Dimensioning
   Name/it: Dimensiona un'armatura
   MenuLocation: Arch - Armatura
   Workbenches: [Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso: [Disegna un'armatura](Arch_Rebar_Drawing/it.md), [Addon Reinforcement](Reinforcement_Addon/it.md)
   Version: 0.19
---

# Arch Rebar Dimensioning/it


</div>

Please Note: The below work is present in develop branch of Reinforcement workbench [here](https://github.com/amrit3701/FreeCAD-Reinforcement/tree/develop)

## Description

The [Reinforcement Dimensioning](Arch_Rebar_Dimensioning.md) tool allows the user to create dimensioning for reinforcing bars in [Reinforcement Drawing](Arch_Rebar_Drawing.md).

This command is part of the [Reinforcement Addon](Reinforcement_Addon.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Drawing_Dimensioning_example.svg  style="width:1000px;">



*Drawing and dimensioning of reinforcing bars*

## Usage

1\. Open FreeCAD Model containing reinforcement bars created using [Reinforcement Addon](Reinforcement_Addon.md).

2\. In FreeCAD Python console, copy below code snippet to generate reinforcement drawing and dimensioning from different views for each [Arch Structure](Arch_Structure.md) element. 
```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    struct_drawing_page_dict = makeStructuresReinforcementDrawing(
        view=view, perform_dimensioning=True
    )
    for drawing_page in struct_drawing_page_dict.values():
        drawing_view = drawing_page.Views[0]
        drawing_view.setExpression(
            "LeftOffset",
            u".Template.Width.Value / 2 - .Width.Value * .Scale / 2",
        )
        drawing_view.setExpression(
            "TopOffset",
            u".Template.Height.Value / 2 - .Height.Value * .Scale / 2",
        )
        drawing_view.recompute(True)
        drawing_page.recompute(True)

```

## ReinforcementDimensioning Object 

A Rebar Dimensioning SVG View object.

### Properties

-    **ParentDrawingView**: The parent ReinforcementDrawingView object containing drawing of [Rebar](Arch_Rebar.md) object.

-    **Rebar**: The [Rebar](Arch_Rebar.md) object to perform dimensioning.

-    **WayPointsType**: The WayPoints type of dimension line. It can be \"Automatic\" (to automatically perform dimensioning of [Rebar](Arch_Rebar.md) object) or \"Custom\" to use **WayPoints** to perform dimensioning.

-    **WayPoints**: A list of vector points to be used to generate dimension line.

-    **TextPositionType**: The position type of dimension text. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".

-    **DimensionFormat**: The dimension label format.

   Example: "%M %C⌀%D,span=%S"
   Here: %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    **Font**: The font family of dimension label.

-    **FontSize**: The font size of dimension label.

-    **StrokeWidth**: The stroke width of dimension line.

-    **LineStyle**: The stroke style of dimension line. It can be \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" or \"DashDotDot\".

-    **LineColor**: The color of dimension line.

-    **TextColor**: The color of dimension label.

-    **LineStartSymbol**: The start symbol of dimension line. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    **LineEndSymbol**: The end symbol of dimension line. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    **LineMidPointSymbol**: The mid points symbol of dimension line. It can be \"Tick\", \"Dot\" or \"None\".

-    **DimensionLeftOffset**: The left offset for automated reinforcement dimensioning.

-    **DimensionRightOffset**: The right offset for automated reinforcement dimensioning.

-    **DimensionTopOffset**: The top offset for automated reinforcement dimensioning.

-    **DimensionBottomOffset**: The bottom offset for automated reinforcement dimensioning.

-    **SingleRebar_LineStartSymbol**: The dimension line start symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\". It is used only when **WayPointsType** is set to \"Automatic\".

-    **SingleRebar_LineEndSymbol**: The dimension line end symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\". It is used only when **WayPointsType** is set to \"Automatic\".

-    **MultiRebar_LineStartSymbol**: The dimension line start symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\". It is used only when **WayPointsType** is set to \"Automatic\".

-    **MultiRebar_LineEndSymbol**: The dimension line end symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\". It is used only when **WayPointsType** is set to \"Automatic\".

-    **SingleRebar_OuterDimension**: It specifies if dimension lines are to be outside of reinforcement drawing, in case of single rebar is visible. It is used only when **WayPointsType** is set to \"Automatic\".

-    **MultiRebar_OuterDimension**: It specifies if dimension lines are to be outside of reinforcement drawing, in case of multiple rebars are visible. It is used only when **WayPointsType** is set to \"Automatic\".

-    **SingleRebar_TextPositionType**: It specifies the dimension label position type, in case of single rebar is visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\". It is used only when **WayPointsType** is set to \"Automatic\".

-    **MultiRebar_TextPositionType**: It specifies the dimension label position type, in case of multiple rebars are visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\". It is used only when **WayPointsType** is set to \"Automatic\".

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md), [Reinforcement Drawing](Arch_Rebar_Drawing.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The [Reinforcement Dimensioning](Arch_Rebar_Dimensioning.md) tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following functions:

### Create Reinforcement Dimensioning Object 


```python
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)

dimension_object = makeReinforcementDimensioningObject(
    rebar,
    parent_drawing_view,
    drawing_page=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset_increment=10,
    dimension_right_offset_increment=10,
    dimension_top_offset_increment=10,
    dimension_bottom_offset_increment=10,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)
```

-   Creates and return a `ReinforcementDimensioning` object for given `rebar` object.

-    `parent_drawing_view`is the `ReinforcementDrawingView` object containing drawing of `rebar` object.

-    `drawing_page`is the object of type TechDraw::DrawPage used to show `parent_drawing_view`.

-    `dimension_label_format`is the format used for dimension label.

   Example: "%M %C⌀%D,span=%S"
   Here: %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    `dimension_font_family`is the font family of dimension label.

-    `dimension_font_size`is the font size of dimension label.

-    `dimension_stroke_width`is the stroke-width of dimension line.

-    `dimension_line_style`is the stroke style of dimension line. It can be \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" or \"DashDotDot\".

-    `dimension_line_color`is the color of dimension line.

   Format: (r, g, b)
   r, g, b value should be between 0 to 1, so you may need to divide value of r, g, b by 255 to get its value between 0 to 1
   Make sure r, g, b must be float

-    `dimension_text_color`is the color of dimension label.

-    `dimension_single_rebar_line_start_symbol`is the dimension line start symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_single_rebar_line_end_symbol`is the dimension line end symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_multi_rebar_line_start_symbol`is the dimension line start symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_multi_rebar_line_end_symbol`is the dimension line end symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_line_mid_point_symbol`is the dimension line mid points symbol. It can be \"Tick\", \"Dot\" or \"None\".

-    `dimension_left_offset_increment`is the increment in left offset to move each new dimension label away from drawing.

-    `dimension_right_offset_increment`is the increment in right offset to move each new dimension label away from drawing.

-    `dimension_top_offset_increment`is the increment in top offset to move each new dimension label away from drawing.

-    `dimension_bottom_offset_increment`is the increment in bottom offset to move each new dimension label away from drawing.

-    `dimension_single_rebar_outer_dim`specifies if dimension lines are to be outside of reinforcement drawing, in case of single rebar is visible.

-    `dimension_multi_rebar_outer_dim`specifies if dimension lines are to be outside of reinforcement drawing, in case of multiple rebars are visible.

-    `dimension_single_rebar_text_position_type`specifies the dimension label position type, in case of single rebar is visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`specifies the dimension label position type, in case of multiple rebars are visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".

##### Example


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)


# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Create Straight Rebars
TwoTiesSixRebars.makeTwoTiesSixRebars(
    l_cover_of_ties=40,        
    r_cover_of_ties=40,
    t_cover_of_ties=40,
    b_cover_of_ties=40,
    offset_of_ties=100,
    bent_angle_of_ties=135,
    extension_factor_of_ties=2,
    dia_of_ties=8,
    number_spacing_check=True,
    number_spacing_value=10,
    dia_of_main_rebars=16,
    t_offset_of_rebars=40,
    b_offset_of_rebars=40,
    main_rebars_type="StraightRebar",
    hook_orientation="Top Inside",
    hook_extend_along="x-axis",
    l_rebar_rounding=None,
    hook_extension=None,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure,
    facename="Face6",
)

rebars = Draft.get_objects_of_type(FreeCAD.ActiveDocument.Objects, "Rebar")

# Create Reinforcement Drawing
drawing_page = make_reinforcement_drawing.makeReinforcementDrawing(
    structure=Structure,
    rebars_list=rebars,
    view="Front",
    rebars_stroke_width=0.35,
    rebars_color_style="Automatic",
    rebars_color=(0.67, 0.0, 0.0),
    structure_stroke_width=0.5,
    structure_color_style="Automatic",
    structure_color=(0.3, 0.9, 0.91),
    drawing_left_offset=20,
    drawing_top_offset=20,
    drawing_min_right_offset=20,
    drawing_min_bottom_offset=20,
    drawing_max_width=0,                    # It is set to 0 to automatically set default width based on other parameters
    drawing_max_height=0,                   # It is set to 0 to automatically set default height based on other parameters
    template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
    dimension_left_offset=10,
    dimension_right_offset=10,
    dimension_top_offset=10,
    dimension_bottom_offset=10,
)

visible_rebars = drawing_page.Views[0].VisibleRebars

# Create Reinforcement Dimensioning for single rebar
makeReinforcementDimensioningObject(
    visible_rebars[0],
    parent_drawing_view,
    drawing_page=None,
    dimension_label_format="%M %C⌀%D,span=%S",
    dimension_font_family="DejaVu Sans",
    dimension_font_size=3,
    dimension_stroke_width=0.25,
    dimension_line_style="Continuous",
    dimension_line_color=(0.0, 0.0, 0.50),
    dimension_text_color=(0.0, 0.33, 0.0),
    dimension_single_rebar_line_start_symbol="None",
    dimension_single_rebar_line_end_symbol="FilledArrow",
    dimension_multi_rebar_line_start_symbol="FilledArrow",
    dimension_multi_rebar_line_end_symbol="FilledArrow",
    dimension_line_mid_point_symbol="Dot",
    dimension_left_offset_increment=10,
    dimension_right_offset_increment=10,
    dimension_top_offset_increment=10,
    dimension_bottom_offset_increment=10,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)

# Create Reinforcement Dimensioning for all visible rebars in drawing view
for visible_rebar in visible_rebars:
    makeReinforcementDimensioningObject(
        visible_rebar,
        parent_drawing_view,
        drawing_page=None,
        dimension_label_format="%M %C⌀%D,span=%S",
        dimension_font_family="DejaVu Sans",
        dimension_font_size=3,
        dimension_stroke_width=0.25,
        dimension_line_style="Continuous",
        dimension_line_color=(0.0, 0.0, 0.50),
        dimension_text_color=(0.0, 0.33, 0.0),
        dimension_single_rebar_line_start_symbol="None",
        dimension_single_rebar_line_end_symbol="FilledArrow",
        dimension_multi_rebar_line_start_symbol="FilledArrow",
        dimension_multi_rebar_line_end_symbol="FilledArrow",
        dimension_line_mid_point_symbol="Dot",
        dimension_left_offset_increment=10,
        dimension_right_offset_increment=10,
        dimension_top_offset_increment=10,
        dimension_bottom_offset_increment=10,
        dimension_single_rebar_outer_dim=False,
        dimension_multi_rebar_outer_dim=True,
        dimension_single_rebar_text_position_type="StartOfLine",
        dimension_multi_rebar_text_position_type="MidOfLine",
    )
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Dimensioning/it
