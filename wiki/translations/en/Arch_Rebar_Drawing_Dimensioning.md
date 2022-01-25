---
- GuiCommand:
   Name:Arch Rebar Drawing Dimensioning
   MenuLocation:
   Workbenches:[Arch](Arch_Workbench.md), [BIM](BIM_Workbench.md)
   Version:0.19
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Rebar Bill Of Material](Arch_Rebar_BOM.md), [Reinforcement Rebar Shape Cut List](Reinforcement_Bar_Shape_Cut_List.md)
---

# Arch Rebar Drawing Dimensioning/en

## Description

The [Reinforcement Drawing Dimensioning](Arch_Rebar_Drawing_Dimensioning.md) tool allows the user to create drawing and dimensioning of reinforcing bars.

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Drawing_Dimensioning_example.svg  style="width:800px;">



*Drawing and dimensioning of reinforcing bars*

## Usage

1\. Open FreeCAD Model containing reinforcement bars created using [Reinforcement Workbench](Reinforcement_Workbench.md).

2\. Select **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object and then click on **<img src="images/Arch_Rebar_Drawing_Dimensioning.svg" width=16px> [Reinforcement Drawing Dimensioning](Arch_Rebar_Drawing_Dimensioning.md)**.

3\. A dialog box will pop-out on the screen as shown below.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog1.png  style="width:800px;">

4\. Enter all the details related to stroke width and color of rebar and structure.

5\. Click on **Next** button and the dialog box will be updated as shown below.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog2.png  style="width:800px;">

6\. Enter drawing views option, dimensioning and offset details.

7\. Click on **Next** button and the dialog box will be updated as shown below.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog3.png  style="width:800px;">

8\. Enter dimension label and line details.

9\. Click on **Next** button and the dialog box will be updated as shown below.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog4.png  style="width:800px;">

10\. Enter single rebar and multi rebar dimension details.

11\. Click on **Next** button and the dialog box will be updated as shown below.

<img alt="" src=images/ArchRebarDrawingDimensioning_dialog5.png  style="width:800px;">

12\. Enter details of dimension and dimension line offsets.

13\. Click **Finish** button to generate drawings.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The [Reinforcement Drawing Dimensioning](Arch_Rebar_Drawing_Dimensioning.md) tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:

### Create Reinforcement Drawing And Dimensioning 


```python
from ReinforcementDrawing import make_reinforcement_drawing

structure_drawing_page_dict = make_reinforcement_drawing.makeStructuresReinforcementDrawing(
    structure_list=None,
    rebars_list=None,
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
    drawing_max_width=0,                        # It is set to 0 to automatically set the default width based on other parameters
    drawing_max_height=0,                       # It is set to 0 to automatically set the default height based on other parameters
    template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
    perform_dimensioning=True,
    dimension_rebars_filter_list=None,
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
    dimension_left_offset=10,
    dimension_right_offset=10,
    dimension_top_offset=10,
    dimension_bottom_offset=10,
    dimension_left_offset_increment=6,
    dimension_right_offset_increment=6,
    dimension_top_offset_increment=6,
    dimension_bottom_offset_increment=6,
    dimension_single_rebar_outer_dim=False,
    dimension_multi_rebar_outer_dim=True,
    dimension_single_rebar_text_position_type="StartOfLine",
    dimension_multi_rebar_text_position_type="MidOfLine",
)
```

-   It returns `structure_drawing_page_dict`, a dictionary with structure as key and corresponding reinforcement drawing page as the value.

-    `structure_list`is the list of structural objects to generate their reinforcement drawing. If not provided, structures will be selected from the active document acting as Host for rebar objects.

-    `rebars_list`is the list of rebar objects to be included in the drawing. If not provided, rebars objects having Host in structure\_list will be selected from the active document.

-    `view`specifies the view of drawing to be generated. It can be \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" or \"Bottom\".

-    `rebars_stroke_width`specifies the stroke-width of rebars in drawing SVG.

-    `rebars_color_style`specifies the color style of rebars. Set it to \"Automatic\" to automatically select rebars color or \"Custom\" to choose shape color value from variable `rebars_color`.

-    `rebars_color`specifies the fill color for rebars in drawing SVG.

   Format: (r, g, b)
   r, g, b value should be between 0 to 1, so you may need to divide the value of r, g, b by 255 to get its value between 0 to 1
   Make sure r, g, b must be float
   Example: (0.67, 0.0, 0.0)

-    `structure_stroke_width`specifies the stroke-width of structure in drawing SVG.

-    `structure_color_style`specifies the fill style of the structure. Set it to \"Automatic\" to automatically select structure color or \"Custom\" to choose structure color value from variable `structure_color`.

-    `structure_color`specifies the fill color for structure in drawing SVG. Format: (r, g, b)

-    `drawing_left_offset`specifies the left offset of the drawing view on `template_file`.

-    `drawing_top_offset`specifies the top offset of the drawing view on `template_file`.

-    `drawing_min_right_offset`specifies the minimum right offset of the drawing view on `template_file`.

-    `drawing_min_bottom_offset`specifies the minimum bottom offset of the drawing view on `template_file`.

-    `drawing_max_width`specifies the maximum width of drawing on `template_file`.

-    `drawing_max_height`specifies the maximum height of drawing on `template_file`.

-    `template_file`is the template file to be used for the reinforcement drawing page.

-    `perform_dimensioning`specifies if dimensioning needs to be created for rebars in drawing.

-    `dimension_rebars_filter_list`is the list of rebars to perform dimensioning. Set it to None to dimension all visible rebars in drawing.

-    `dimension_label_format`is the format used for the dimension label.

   Example: "%M %C⌀%D,span=%S"
   Here: %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    `dimension_font_family`is the font family of dimension label.

-    `dimension_font_size`is the font size of the dimension label.

-    `dimension_stroke_width`is the stroke-width of dimension line.

-    `dimension_line_style`is the stroke style of dimension line. It can be \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" or \"DashDotDot\".

-    `dimension_line_color`is the color of the dimension line.

   Format: (r, g, b)
   r, g, b value should be between 0 to 1, so you may need to divide the value of r, g, b by 255 to get its value between 0 to 1
   Make sure r, g, b must be float

-    `dimension_text_color`is the color of the dimension label.

-    `dimension_single_rebar_line_start_symbol`is the dimension line start symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_single_rebar_line_end_symbol`is the dimension line end symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_multi_rebar_line_start_symbol`is the dimension line start symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_multi_rebar_line_end_symbol`is the dimension line end symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_line_mid_point_symbol`is the dimension line midpoints symbol. It can be \"Tick\", \"Dot\" or \"None\".

-    `dimension_left_offset`specifies the left offset of the dimension from drawing.

-    `dimension_right_offset`specifies the right offset of the dimension from drawing.

-    `dimension_top_offset`specifies the top offset of the dimension from drawing.

-    `dimension_bottom_offset`specifies the bottom offset of the dimension from drawing.

-    `dimension_left_offset_increment`is the increment in the left offset to move each new dimension label away from drawing.

-    `dimension_right_offset_increment`is the increment in the right offset to move each new dimension label away from drawing.

-    `dimension_top_offset_increment`is the increment in the top offset to move each new dimension label away from drawing.

-    `dimension_bottom_offset_increment`is the increment in the bottom offset to move each new dimension label away from drawing.

-    `dimension_single_rebar_outer_dim`specifies if dimension lines are to be outside of reinforcement drawing, in case of single rebar is visible.

-    `dimension_multi_rebar_outer_dim`specifies if dimension lines are to be outside of reinforcement drawing, in case of multiple rebars are visible.

-    `dimension_single_rebar_text_position_type`specifies the dimension label position type, in case of single rebar is visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`specifies the dimension label position type, in case of multiple rebars are visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".


<div class="mw-collapsible toccolours mw-collapsed">

##### Example


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

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

# Create Reinforcement Drawing and Dimensioning
for drawing_view in ("Front", "Rear", "Left", "Right", "Top", "Bottom"):
    struct_drawing_page_dict = make_reinforcement_drawing.makeStructuresReinforcementDrawing(
        structure_list=None,
        rebars_list=None,
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
        drawing_max_width=0,                        # It is set to 0 to automatically set the default width based on other parameters
        drawing_max_height=0,                       # It is set to 0 to automatically set the default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        perform_dimensioning=True,
        dimension_rebars_filter_list=None,
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
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
        dimension_left_offset_increment=6,
        dimension_right_offset_increment=6,
        dimension_top_offset_increment=6,
        dimension_bottom_offset_increment=6,
        dimension_single_rebar_outer_dim=False,
        dimension_multi_rebar_outer_dim=True,
        dimension_single_rebar_text_position_type="StartOfLine",
        dimension_multi_rebar_text_position_type="MidOfLine",
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


</div>


</div>

# <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width:32px;"> Reinforcement Drawing 

## Usage 

1\. Open FreeCAD Model containing reinforcement bars created using [Reinforcement Addon](Reinforcement_Addon.md).

2\. In FreeCAD Python console, copy the below code snippet to generate reinforcement drawing from different views for each [Arch Structure](Arch_Structure.md) element. 
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

-    **Structure**: The structure object acting as a Host for rebars to be included in the drawing.

-    **Rebars**: The list of rebar objects to be included in the drawing.

-    **View**: The reinforcement drawing view to be generated. It can be \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" or \"Bottom\".

-    **PositionType**: The position type of Reinforcement Drawing on Template. It can be \"Automatic\" to calculate drawing placement using **LeftOffset**, **TopOffset**, **MinRightOffset** and **MinBottomOffset** OR \"Custom\" to set placement using **X** and **Y**.

-    **RebarsStrokeWidth**: The stroke width of rebars in Reinforcement Drawing SVG.

-    **RebarsColorStyle**: The color style of rebars in Reinforcement Drawing SVG. Set it to \"Automatic\" to automatically select rebars color OR \"Custom\" to choose shape color value from **RebarsColor**.

-    **RebarsColor**: The color of rebars in Reinforcement Drawing SVG.

-    **StructureStrokeWidth**: The stroke width of the structure in Reinforcement Drawing SVG.

-    **StructureColorStyle**: The color style of structure in Reinforcement Drawing SVG. Set it to \"Automatic\" to automatically select rebars color, \"Custom\" to choose shape color value from **StructureColor** OR \"None\" to not fill structure.

-    **StructureColor**: The color of structure in Reinforcement Drawing SVG.

-    **Template**: The template for the Reinforcement Drawing view.

-    **Width**: The width of the Reinforcement Drawing view SVG.

-    **Height**: The height of Reinforcement Drawing view SVG.

-    **LeftOffset**: The left offset of Reinforcement Drawing view on a template.

-    **TopOffset**: The top offset of Reinforcement Drawing view on a template.

-    **MinRightOffset**: The minimum right offset of Reinforcement Drawing view on a template.

-    **MinBottomOffset**: The minimum bottom offset of Reinforcement Drawing view on a template.

-    **MaxWidth**: The maximum width of the Reinforcement Drawing view.

-    **MaxHeight**: The maximum height of the Reinforcement Drawing view.

-    **VisibleRebars**: The list of visible rebar objects in the drawing view.

-    **DimensionLeftOffset**: The left offset for each new ReinforcementDimensioning object.

-    **DimensionRightOffset**: The right offset for each new ReinforcementDimensioning object.

-    **DimensionTopOffset**: The top offset for each new ReinforcementDimensioning object.

-    **DimensionBottomOffset**: The bottom offset for each new ReinforcementDimensioning object.

## Scripting 


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Reinforcement Drawing functions can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following functions:

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

-   Creates a `ReinforcementDrawingView` object for the given [structure](Arch_Structure.md) and [rebar](Arch_Rebar.md) objects list.

-   It returns the `reinforcement_drawing_page` of type `TechDraw::DrawPage`.

-    `view`specifies the view of drawing to be generated. It can be \"Front\", \"Rear\", \"Left\", \"Right\", \"Top\" or \"Bottom\".

-    `rebars_stroke_width`specifies the stroke-width of rebars in drawing SVG.

-    `rebars_color_style`specifies the color style of rebars. Set it to \"Automatic\" to automatically select rebars color or \"Custom\" to choose shape color value from variable `rebars_color`.

-    `rebars_color`specifies the fill color for rebars in drawing SVG.

   Format: (r, g, b)
   r, g, b value should be between 0 to 1, so you may need to divide the value of r, g, b by 255 to get its value between 0 to 1
   Make sure r, g, b must be float
   Example: (0.67, 0.0, 0.0)

-    `structure_stroke_width`specifies the stroke-width of structure in drawing SVG.

-    `structure_color_style`specifies the fill style of the structure. Set it to \"Automatic\" to automatically select structure color or \"Custom\" to choose structure color value from variable `structure_color`.

-    `structure_color`specifies the fill color for structure in drawing SVG. Format: (r, g, b)

-    `drawing_left_offset`specifies the left offset of the drawing view on `template_file`.

-    `drawing_top_offset`specifies the top offset of the drawing view on `template_file`.

-    `drawing_min_right_offset`specifies the minimum right offset of the drawing view on `template_file`.

-    `drawing_min_bottom_offset`specifies the minimum bottom offset of the drawing view on `template_file`.

-    `drawing_max_width`specifies the maximum width of drawing on `template_file`.

-    `drawing_max_height`specifies the maximum height of drawing on `template_file`.

-    `template_file`is the template file to be used for the reinforcement drawing page.

-    `dimension_left_offset`specifies the left offset of the dimension from drawing.

-    `dimension_right_offset`specifies the right offset of the dimension from drawing.

-    `dimension_top_offset`specifies the top offset of the dimension from drawing.

-    `dimension_bottom_offset`specifies the bottom offset of the dimension from drawing.


<div class="mw-collapsible toccolours mw-collapsed">

##### Example 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

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
        drawing_max_width=0,                    # It is set to 0 to automatically set the default width based on other parameters
        drawing_max_height=0,                   # It is set to 0 to automatically set the default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```


</div>


</div>

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

-   It returns `structure_drawing_page_dict`, a dictionary with structure as key and corresponding reinforcement drawing page as the value.

-    `structure_list`is the list of structural objects to generate their reinforcement drawing. If not provided, structures will be selected from the active document acting as Host for rebar objects.

-    `rebars_list`is the list of rebar objects to be included in the drawing. If not provided, rebars objects having Host in structure\_list will be selected from the active document.


<div class="mw-collapsible toccolours mw-collapsed">

##### Example 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing

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
        drawing_max_width=0,                    # It is set to 0 to automatically set the default width based on other parameters
        drawing_max_height=0,                   # It is set to 0 to automatically set the default height based on other parameters
        template_file=str(Path(make_reinforcement_drawing.__file__).parent.absolute() / "Templates" / "A4_Landscape_blank.svg"),
        dimension_left_offset=10,
        dimension_right_offset=10,
        dimension_top_offset=10,
        dimension_bottom_offset=10,
    )
```


</div>


</div>

# <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width:32px;"> Reinforcement Dimensioning 

## Usage 

1\. Open FreeCAD Model containing reinforcement bars created using [Reinforcement Addon](Reinforcement_Addon.md).

2\. In FreeCAD Python console, copy the below code snippet to generate reinforcement drawing and dimensioning from different views for each [Arch Structure](Arch_Structure.md) element. 
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

-    **ParentDrawingView**: The parent ReinforcementDrawingView object containing the drawing of [Rebar](Arch_Rebar.md) object.

-    **Rebar**: The [Rebar](Arch_Rebar.md) object to perform dimensioning.

-    **WayPointsType**: The WayPoints type of dimension line. It can be \"Automatic\" (to automatically perform dimensioning of [Rebar](Arch_Rebar.md) object) or \"Custom\" to use **WayPoints** to perform dimensioning.

-    **WayPoints**: A list of vector points to be used to generate a dimension line.

-    **TextPositionType**: The position type of dimension text. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".

-    **DimensionFormat**: The dimension label format.

   Example: "%M %C⌀%D,span=%S"
   Here: %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    **Font**: The font family of dimension label.

-    **FontSize**: The font size of the dimension label.

-    **StrokeWidth**: The stroke width of the dimension line.

-    **LineStyle**: The stroke style of the dimension line. It can be \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" or \"DashDotDot\".

-    **LineColor**: The color of the dimension line.

-    **TextColor**: The color of the dimension label.

-    **LineStartSymbol**: The start symbol of the dimension line. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    **LineEndSymbol**: The end symbol of the dimension line. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    **LineMidPointSymbol**: The midpoints symbol of the dimension line. It can be \"Tick\", \"Dot\" or \"None\".

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

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Reinforcement Dimensioning functions can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following functions:

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

-   Creates and returns a `ReinforcementDimensioning` object for the given `rebar` object.

-    `parent_drawing_view`is the `ReinforcementDrawingView` object containing a drawing of `rebar` object.

-    `drawing_page`is the object of type TechDraw::DrawPage used to show `parent_drawing_view`.

-    `dimension_label_format`is the format used for the dimension label.

   Example: "%M %C⌀%D,span=%S"
   Here: %M -> Rebar.Mark
         %C -> Rebar.Amount
         %D -> Rebar.Diameter
         %S -> Rebar span length

-    `dimension_font_family`is the font family of dimension label.

-    `dimension_font_size`is the font size of the dimension label.

-    `dimension_stroke_width`is the stroke-width of dimension line.

-    `dimension_line_style`is the stroke style of dimension line. It can be \"Continuous\", \"Dash\", \"Dot\", \"DashDot\" or \"DashDotDot\".

-    `dimension_line_color`is the color of the dimension line.

   Format: (r, g, b)
   r, g, b value should be between 0 to 1, so you may need to divide the value of r, g, b by 255 to get its value between 0 to 1
   Make sure r, g, b must be float

-    `dimension_text_color`is the color of the dimension label.

-    `dimension_single_rebar_line_start_symbol`is the dimension line start symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_single_rebar_line_end_symbol`is the dimension line end symbol, in case of single rebar is visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_multi_rebar_line_start_symbol`is the dimension line start symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_multi_rebar_line_end_symbol`is the dimension line end symbol, in case of multiple rebars are visible. It can be \"FilledArrow\", \"Tick\", \"Dot\" or \"None\".

-    `dimension_line_mid_point_symbol`is the dimension line midpoints symbol. It can be \"Tick\", \"Dot\" or \"None\".

-    `dimension_left_offset_increment`is the increment in the left offset to move each new dimension label away from drawing.

-    `dimension_right_offset_increment`is the increment in the right offset to move each new dimension label away from drawing.

-    `dimension_top_offset_increment`is the increment in the top offset to move each new dimension label away from drawing.

-    `dimension_bottom_offset_increment`is the increment in the bottom offset to move each new dimension label away from drawing.

-    `dimension_single_rebar_outer_dim`specifies if dimension lines are to be outside of reinforcement drawing, in case of single rebar is visible.

-    `dimension_multi_rebar_outer_dim`specifies if dimension lines are to be outside of reinforcement drawing, in case of multiple rebars are visible.

-    `dimension_single_rebar_text_position_type`specifies the dimension label position type, in case of single rebar is visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".

-    `dimension_multi_rebar_text_position_type`specifies the dimension label position type, in case of multiple rebars are visible. It can be \"StartOfLine\", \"MidOfLine\" or \"EndOfLine\".


<div class="mw-collapsible toccolours mw-collapsed">

##### Example 


<div class="mw-collapsible-content">


```python
from pathlib import Path
import FreeCAD, Draft, Arch
from ColumnReinforcement import TwoTiesSixRebars
from ReinforcementDrawing import make_reinforcement_drawing
from ReinforcementDrawing.ReinforcementDimensioning import (
    makeReinforcementDimensioningObject,
)

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
    drawing_max_width=0,                    # It is set to 0 to automatically set the default width based on other parameters
    drawing_max_height=0,                   # It is set to 0 to automatically set the default height based on other parameters
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


</div>


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Drawing Dimensioning/en
