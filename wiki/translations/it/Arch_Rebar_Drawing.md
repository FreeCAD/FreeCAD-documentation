---
- GuiCommand:/it
   Name:Arch_Rebar_Drawing
   Name/it:Disegna un'armatura
   MenuLocation:Arch → Armatura
   Workbenches:[Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   SeeAlso:[Dimensiona un'armatura](Arch_Rebar_Dimensioning/it.md), [Addon Reinforcement](Reinforcement_Addon/it.md)
   Version:0.19
---

# Arch Rebar Drawing/it


</div>

Please Note: The below work is present in develop branch of Reinforcement workbench [here](https://github.com/amrit3701/FreeCAD-Reinforcement/tree/develop)

## Description

The [Reinforcement Drawing](Arch_Rebar_Drawing.md) tool allows the user to create drawing of reinforcing bars.

This command is part of the [Reinforcement Addon](Reinforcement_Addon.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Drawing_example.svg  style="width:800px;">


*Drawing and dimensioning of reinforcing bars*

## Usage

1\. Open FreeCAD Model containing reinforcement bars created using [Reinforcement Addon](Reinforcement_Addon.md).

2\. In FreeCAD Python console, copy below code snippet to generate reinforcement drawing from different views for each [Arch Structure](Arch_Structure.md) element. 
```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

for view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    makeStructuresReinforcementDrawing(view=view)
```

## ReinforcementDrawingView Object 

A Rebars Drawing SVG View object.

### Properties

-    **Structure**: The structure object acting as Host for rebars to be included in drawing.

-    **Rebars**: The list of rebar objects to be included in drawing.

-    **View**: The reinforcement drawing view to be generated. It can be \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" or \"Bottom\".

-    **PositionType**: The position type of Reinforcement Drawing on Template. It can be \"Automatic\" to calculate drawing placement using **LeftOffset**, **TopOffset**, **MinRightOffset** and **MinBottomOffset** OR \"Custom\" to set placement using **X** and **Y**.

-    **RebarsStrokeWidth**: The stroke width of rebars in Reinforcement Drawing svg.

-    **RebarsColorStyle**: The color style of rebars in Reinforcement Drawing svg. Set it to \"Automatic\" to automatically select rebars color OR \"Custom\" to choose shape color value from **RebarsColor**.

-    **RebarsColor**: The color of rebars in Reinforcement Drawing svg.

-    **StructureStrokeWidth**: The stroke width of structure in Reinforcement Drawing svg.

-    **StructureColorStyle**: The color style of structure in Reinforcement Drawing svg. Set it to \"Automatic\" to automatically select rebars color, \"Custom\" to choose shape color value from **StructureColor** OR \"None\" to not fill structure.

-    **StructureColor**: The color of structure in Reinforcement Drawing svg.

-    **Template**: The template for Reinforcement Drawing view.

-    **Width**: The width of Reinforcement Drawing view svg.

-    **Height**: The height of Reinforcement Drawing view svg.

-    **LeftOffset**: The left offset of Reinforcement Drawing view on template.

-    **TopOffset**: The top offset of Reinforcement Drawing view on template.

-    **MinRightOffset**: The minimum right offset of Reinforcement Drawing view on template.

-    **MinBottomOffset**: The minimum bottom offset of Reinforcement Drawing view on template.

-    **MaxWidth**: The maximum width of Reinforcement Drawing view.

-    **MaxHeight**: The maximum height of Reinforcement Drawing view.

-    **VisibleRebars**: The list of visible rebar objects in drawing view.

-    **DimensionLeftOffset**: The left offset for each new ReinforcementDimensioning object.

-    **DimensionRightOffset**: The right offset for each new ReinforcementDimensioning object.

-    **DimensionTopOffset**: The top offset for each new ReinforcementDimensioning object.

-    **DimensionBottomOffset**: The bottom offset for each new ReinforcementDimensioning object.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The [Reinforcement Drawing](Arch_Rebar_Drawing.md) tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following functions:

### Create Reinforcement Drawing View 

#### For one structure 


```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeReinforcementDrawing,
)

reinforcement_drawing_page = makeReinforcementDrawing(
    structure,
    rebars_list,
    view,
    rebars_stroke_width,
    rebars_color_style,
    rebars_color,
    structure_stroke_width,
    structure_color_style,
    structure_color,
    drawing_left_offset,
    drawing_top_offset,
    drawing_min_right_offset,
    drawing_min_bottom_offset,
    drawing_max_width,
    drawing_max_height,
    template_file,
    dimension_left_offset,
    dimension_right_offset,
    dimension_top_offset,
    dimension_bottom_offset,
)
```

-   Creates a `ReinforcementDrawingView` object for given [structure](Arch_Structure.md) and [rebar](Arch_Rebar.md) objects list.

-   It returns the `reinforcement_drawing_page` of type `TechDraw::DrawPage`.

-    `view`specifies the view of drawing to be generated. It can be \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" or \"Bottom\".

-    `rebars_stroke_width`specifies the stroke-width of rebars in drawing svg.

-    `rebars_color_style`specifies the color style of rebars. Set it to \"Automatic\" to automatically select rebars color or \"Custom\" to choose shape color value from variable `rebars_color`.

-    `rebars_color`specifies the fill color for rebars in drawing svg.

   Format: (r, g, b)
   r, g, b value should be between 0 to 1, so you may need to divide value of r, g, b by 255 to get its value between 0 to 1
   Make sure r, g, b must be float
   Example: (0.67, 0.0, 0.0)

-    `structure_stroke_width`specifies the stroke-width of structure in drawing svg.

-    `structure_color_style`specifies the fill style of structure. Set it to \"Automatic\" to automatically select structure color or \"Custom\" to choose structure color value from variable `structure_color`.

-    `structure_color`specifies the fill color for structure in drawing svg. Format: (r, g, b)

-    `drawing_left_offset`specifies the left offset of drawing view on `template_file`.

-    `drawing_top_offset`specifies the top offset of drawing view on `template_file`.

-    `drawing_min_right_offset`specifies the minimum right offset of drawing view on `template_file`.

-    `drawing_min_bottom_offset`specifies the minimum bottom offset of drawing view on `template_file`.

-    `drawing_max_width`specifies the maximum width of drawing on `template_file`.

-    `drawing_max_height`specifies the maximum height of drawing on `template_file`.

-    `template_file`is the template file to be used for reinforcement drawing page.

-    `dimension_left_offset`specifies the left offset of dimension from drawing.

-    `dimension_right_offset`specifies the right offset of dimension from drawing.

-    `dimension_top_offset`specifies the top offset of dimension from drawing.

-    `dimension_bottom_offset`specifies the bottom offset of dimension from drawing.

##### Example


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing


# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

# Create Straight Rebars
RebarGroup = TwoTiesSixRebars.makeTwoTiesSixRebars(
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
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    make_reinforcement_drawing.makeReinforcementDrawing(
        structure=Structure,
        rebars_list=rebars,
        view=drawing_view,
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
```

#### For multiple structures 


```python
from ReinforcementDrawing.make_reinforcement_drawing import (
    makeStructuresReinforcementDrawing,
)

structure_drawing_page_dict = makeStructuresReinforcementDrawing(
    structure_list=None,
    rebars_list=None,
    view="Front",
    rebars_stroke_width=REBARS_STROKE_WIDTH,
    rebars_color_style=REBARS_COLOR_STYLE,
    rebars_color=REBARS_COLOR,
    structure_stroke_width=STRUCTURE_STROKE_WIDTH,
    structure_color_style=STRUCTURE_COLOR_STYLE,
    structure_color=STRUCTURE_COLOR,
    drawing_left_offset=DRAWING_LEFT_OFFSET,
    drawing_top_offset=DRAWING_TOP_OFFSET,
    drawing_min_right_offset=DRAWING_MIN_RIGHT_OFFSET,
    drawing_min_bottom_offset=DRAWING_MIN_BOTTOM_OFFSET,
    drawing_max_width=DRAWING_MAX_WIDTH,
    drawing_max_height=DRAWING_MAX_HEIGHT,
    template_file=TEMPLATE_FILE,
)
```

-   It returns `structure_drawing_page_dict`, a dictionary with structure as key and corresponding reinforcement drawing page as value.

-    `structure_list`is the list of structural objects to generate their reinforcement drawing. If not provided, structures will be selected from active document acting as Host for rebar objects.

-    `rebars_list`is the list of rebar objects to be included in drawing. If not provided, rebars objects having Host in structure\_list will be selected from active document.

##### Example 


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing


# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure1 = Arch.makeStructure(Rect, height=1600)
Structure1.ViewObject.Transparency = 80
Structure2 = Arch.makeStructure(Rect, height=1600)
Structure2.ViewObject.Transparency = 80
Structure2.Placement = FreeCAD.Placement(FreeCAD.Vector(1000, 0, 0), FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), 0))
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
    structure=Structure1,
    facename="Face6",
)

# Create LShaped Rebars with hook along x-axis
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
    t_offset_of_rebars=-40,
    b_offset_of_rebars=-40,
    main_rebars_type="LShapeRebar",
    hook_orientation="Top Outside",
    hook_extend_along="x-axis",
    l_rebar_rounding=2,
    hook_extension=40,
    ties_sequence=("Tie1", "Tie2"),
    structure=Structure2,
    facename="Face6",
)

# Create Reinforcement Drawing
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    make_reinforcement_drawing.makeStructuresReinforcementDrawing(
        structure_list=None,
        rebars_list=None,
        view=drawing_view,
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
```


<div class="mw-translate-fuzzy">





</div>




[Category:External Command Reference](Category:External_Command_Reference.md) [Category:Reinforcement](Category:Reinforcement.md)

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Rebar Drawing/it
