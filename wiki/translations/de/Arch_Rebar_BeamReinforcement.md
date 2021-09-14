---
- GuiCommand:/de
   Name:Arch_Rebar_BeamReinforcement
   Name/de:Architektur Bewehrung BalkenVerstärkung
   MenuLocation:Arch → Bewehrungswerkzeuge oder 3D/BIM → Reinforcement → BalkenVerstärkung
   Workbenches:[Arch](Arch_Workbench/de.md), [BIM](BIM_Workbench/de.md)
   Version:0.19
   SeeAlso:[Reinforcement_Workbench/de](Reinforcement_Workbench/de.md), [Arch Rebar](Arch_Rebar/de.md), [SäulenVerstärkung ZweiBinderSechsStäbe](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/de.md), [Architektur Bewehrung](Arch_Rebar/de.md)
---

## Beschreibung

Das [Balken Verstärkung](Arch_Rebar_BeamReinforcement/de.md) Werkzeug erlaubt dem Anwender Bewehrungsstäbe innerhalb eines Balken [Architektur Struktur](Arch_Structure/de.md) Objekts erzeugen.

Das [Arch Balkenverstärkung](Arch_Rebar_BentReinforcement/de.md)-Werkzeug ist auch im [BIM-Arbeitsbereich](BIM_Workbench/de.md) integriert.

Dieser Befehl ist Teil der [BewehrungsErweiterung](Reinforcement_Workbench/de.md), eines [externen Arbeitsbereichs](External_Workbenches.md), der mit dem <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Erweiterungsverwalter](Addon_Manager/de.md) über das {{MenuCommand/de|Werkzeuge → Erweiterungsverwalter → Bewehrung}}-Menü installiert werden kann.

![](images/Arch_Rebar_BeamReinforcement_example.png )


*Balkenbewehrung innerhalb eines Balkenss [Architektur Struktur](Arch_Structure/de.md)*

## Anwendung

1\. Select right face of a previously created beam **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object having length along x-axis. Or select front face of a previously created beam **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object having length along y-axis.

2\. Then select **<img src="images/Arch_Rebar_ColumnReinforcement.svg" width=16px> [Beam Reinforcement](Arch_Rebar_BeamReinforcement.md)** from the rebar tools.

3\. A dialog box will pop-out on screen as shown below.

:   <img alt="" src=images/BeamReinforcementDialog_Stirrups.png  style="width:700px;">


*Dialog Box for the Arch Rebar BeamReinforcement tool*

4\. Select the desired type of beam reinforcement.

5\. Give inputs for data related to stirrups.

6\. Click **Next** and the dialog box will be updated as shown below.

:   <img alt="" src=images/BeamReinforcementDialog_TopRebars.png  style="width:700px;">


*Dialog Box for Top Rebars data*

7\. Set data for top rebars.


{{ColoredParagraph|#f8f9fa|

: To edit Number#Diameter@Offset value, click on the **Edit** button next to Number#Diameter@Offset label. A dialog box will pop-out as shown below.

:<img src="images/Beam_TopReinforcement_NumberDiameterOffset.png" width=500px>

: To edit Rebar Type value, click on the **Edit** button next to Rebar Type label. A dialog box will pop-out as shown below.

:<img src="images/Beam_TopReinforcement_RebarType.png" width=300px>

: To edit Hook Orientation value, click on the **Edit** button next to Hook Orientation label. A dialog box will pop-out as shown below.

:<img src="images/Beam_TopReinforcement_HookOrientation.png" width=300px>

: To edit Hook Extension value, click on the **Edit** button next to Hook Extension label. A dialog box will pop-out as shown below.

:<img src="images/Beam_TopReinforcement_HookExtension.png" width=300px>

: To edit LRebar Rounding value, click on the **Edit** button next to Rounding label. A dialog box will pop-out as shown below.

:<img src="images/Beam_TopReinforcement_LRebarRounding.png" width=300px>

: To edit Layer Spacing value, click on the **Edit** button next to Layer Spacing label. A dialog box will pop-out as shown below.

:<img src="images/Beam_TopReinforcement_LayerSpacing.png" width=300px>
}}

8\. Click **Next** and the dialog box will be updated as shown below.

:   <img alt="" src=images/BeamReinforcementDialog_BottomRebars.png  style="width:700px;">


*Dialog Box for Bottom Rebars data*

9\. Set data for bottom rebars similar to top rebars data.

10\. Click **Next** and the dialog box will be updated as shown below.

:   <img alt="" src=images/BeamReinforcementDialog_LeftRebars.png  style="width:700px;">


*Dialog Box for Left Shear Rebars data*

11\. Set data for left shear rebars.


{{ColoredParagraph|#f8f9fa|

: To edit Number#Diameter@Offset value, click on the **Edit** button next to Number#Diameter@Offset label. A dialog box will pop-out as shown below.

:<img src="images/Beam_ShearReinforcement_NumberDiameterOffset.png" width=500px>

: To edit Rebar Type value, click on the **Edit** button next to Rebar Type label. A dialog box will pop-out as shown below.

:<img src="images/Beam_ShearReinforcement_RebarType.png" width=300px>

: To edit Hook Orientation value, click on the **Edit** button next to Hook Orientation label. A dialog box will pop-out as shown below.

:<img src="images/Beam_ShearReinforcement_HookOrientation.png" width=300px>

: To edit Hook Extension value, click on the **Edit** button next to Hook Extension label. A dialog box will pop-out as shown below.

:<img src="images/Beam_ShearReinforcement_HookExtension.png" width=300px>

: To edit LRebar Rounding value, click on the **Edit** button next to Rounding label. A dialog box will pop-out as shown below.

:<img src="images/Beam_ShearReinforcement_LRebarRounding.png" width=300px>
}}

12\. Click **Next** and the dialog box will be updated as shown below.

:   <img alt="" src=images/BeamReinforcementDialog_RightRebars.png  style="width:700px;">


*Dialog Box for Right Shear Rebars data*

13\. Set data for right shear rebars similar to left shear rebars data.

14\. Click **OK** or **Apply** to generate beam reinforcement.

15\. Click **Cancel** to exit the dialog box.

## Eigenschaften

**Stirrups:**

-    **Left Cover**: The distance between the left end of the stirrup to the left face of the structure.

-    **Right Cover**: The distance between the right end of the stirrup to right face of the structure.

-    **Top Cover**: The distance between stirrup from the top face of the structure.

-    **Bottom Cover**: The distance between stirrup from the bottom face of the structure.

-    **Offset**: The distance between stirrup from the selected/back face of the structure.

-    **Diameter**: Diameter of the stirrup.

-    **Bent Angle**: Bent angle defines the angle at the ends of a stirrup.

-    **Extension Factor**: Extension Factor defines length of end of stirrup, expressed in times the diameter.

-    **Number**: The number of stirrup.

-    **Spacing**: The distance between the axes of each stirrup.

**Top/Bottom Reinforcement Rebars:** Rebars present at top/bottom side of beam

-    **NumberDiameterOffset**: A tuple of Number\#Diameter\@Offset string. Each element of tuple represents reinforcement for each new layer.

-    **Rebar Type**: List of tuple of type of reinforcement bars.

-    **Hook Orientation**: List of tuple of orientation of LShaped hooks.

-    **Hook Extension**: List of tuple of length of hook of LShaped rebars.

-    **Rounding**: List of tuple of a rounding value to be applied to the corners of the LShape rebars, expressed in times the diameter.

-    **Layer Spacing**: List of spacing between two consecutive reinforcement layers.

**Left/Right Reinforcement Rebars:** Rebars present at left/right side of beam

-    **NumberDiameterOffset**: String of Number\#Diameter\@Offset set for reinforcement bars.

-    **Rebar Type**: List of type of reinforcement bars.

-    **Hook Orientation**: List of orientation of LShaped hooks.

-    **Hook Extension**: List of length of hook of LShaped rebars.

-    **Rounding**: List of a rounding value to be applied to the corners of the LShape rebars, expressed in times the diameter.

-    **Rebar Spacing**: Clear spacing between consecutive reinforcement bars.

## Skripten


**Siehe auch:**

[Architektur API](Arch_API/de.md), [Bewehrung API](Reinforcement_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

The BeamReinforcement tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:

### Create Two Legged Stirrups 


```python
RebarGroup = makeReinforcement(
    l_cover_of_stirrup,
    r_cover_of_stirrup,
    t_cover_of_stirrup,
    b_cover_of_stirrup,
    offset_of_stirrup,
    bent_angle,
    extension_factor,
    dia_of_stirrup,
    number_spacing_check,
    number_spacing_value,
    top_reinforcement_number_diameter_offset,
    top_reinforcement_rebar_type,
    top_reinforcement_layer_spacing,
    bottom_reinforcement_number_diameter_offset,
    bottom_reinforcement_rebar_type,
    bottom_reinforcement_layer_spacing,
    left_rebars_number_diameter_offset,
    left_rebars_type,
    left_rebars_spacing,
    right_rebars_number_diameter_offset,
    right_rebars_type,
    right_rebars_spacing,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=40,
    top_reinforcement_hook_orientation="Front Inside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=40,
    bottom_reinforcement_hook_orientation="Front Inside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=40,
    left_rebars_hook_orientation="Front Inside",
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=40,
    right_rebars_hook_orientation="Front Inside",
    structure=None,
    facename=None,
)

```

-   Creates a `RebarGroup` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover_of_stirrup`, `r_cover_of_stirrup`, `t_cover_of_stirrup`, `b_cover_of_stirrup` and `offset_of_stirrup` are inner offset distances for the stirrup elements with respect to the faces of the structure. They are respectively the left, right, top, bottom and front/rear offsets.

-    `bent_angle`define the angle of the tip of the reinforcement loop of stirrup.

-    `extension_factor`define the length of the tip of the reinforcement loop of stirrup, expressed in times the diameter.

-    `dia_of_stirrup`is the diameter of the stirrup.

-    `number_spacing_check`if it is `True` it will create as many stirrup as given by `number_spacing_value`; if it is `False` it will create stirrup separated by the numerical value of `number_spacing_value`.

-    `number_spacing_value`specifies the number of stirrups, or the value of the separation between them, depending on `number_spacing_check`.

-    `top_reinforcement_number_diameter_offset`and `bottom_reinforcement_number_diameter_offset` are tuple of number\_diameter\_offset string. Each element of tuple represents reinforcement for each new layer.

   Syntax: (
               "number1#diameter1@offset1+number2#diameter2@offset2+...",
               "number3#diameter3@offset3+number4#diameter4@offset4+...",
               ...,
           )

-    `top_reinforcement_rebar_type`and `bottom_reinforcement_rebar_type` specifies type of top/bottom reinforcement bars.

   Possible values:
   1. 'StraightRebar' or 'LShapeRebar'
', ...) and number of elements of tuple must be equal to number of reinforcement
      layers.
   3. [
', ...),
', ...),
          ...,
      ]
      each element of list is a tuple, which specifies rebar type of each reinforcement layer. And each element of
      tuple represents rabar_type for each set of rebars.
   4. [
,
', ...),
          ...,
      ]

-    `top_reinforcement_layer_spacing`and `bottom_reinforcement_layer_spacing` is the spacing between two consecutive reinforcement layers.

   Possible values:

, ...) and number of elements of tuple must be
      equal to one less than number of layers.

-    `left_rebars_number_diameter_offset`and `right_rebars_number_diameter_offset` are string of number\_diameter\_offset.

   Syntax: "number1#diameter1@offset1+number2#diameter2@offset2+..."

-    `left_rebars_type`and `right_rebars_type` specifies type of left/right reinforcement bars.

   Possible values:
   1. 'StraightRebar' or 'LShapeRebar'
', ...) and each element of tuple represents rabar_type for each set of rebars.

-    `left_rebars_spacing`and `right_rebars_spacing` is clear spacing between consecutive reinforcement bars.

-    `top_reinforcement_l_rebar_rounding`and `bottom_reinforcement_l_rebar_rounding` is the parameter that determines the bending radius of the LShaped top/bottom rebars, expressed as times the diameter. Possible syntax are similar to as discussed above for `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_extension`and `bottom_reinforcement_hook_extension` is the length of hook of LShaped rebars. Possible syntax are similar to as discussed above for `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `top_reinforcement_hook_orientation`and `bottom_reinforcement_hook_orientation` specifies the orientation of LShaped hook; it can be `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` or `"Rear Outside"`. Possible syntax are similar to as discussed above for `top_reinforcement_rebar_type` / `bottom_reinforcement_rebar_type`.

-    `left_l_rebar_rounding`and `right_l_rebar_rounding` is the parameter that determines the bending radius of the LShaped left/right rebars, expressed as times the diameter. Possible syntax are similar to as discussed above for `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_extension`and `right_rebars_hook_extension` is the length of hook of LShaped rebars. Possible syntax are similar to as discussed above for `left_rebars_type` / `right_rebars_type`.

-    `left_rebars_hook_orientation`and `right_rebars_hook_orientation` specifies the orientation of LShaped hook; it can be `"Front Inside"`, `"Front Outside"`, `"Rear Inside"` or `"Rear Outside"`. Possible syntax are similar to as discussed above for `left_rebars_type` / `right_rebars_type`.

#### Example


```python
import FreeCAD, Arch
from BeamReinforcement import TwoLeggedBeam

Structure = Arch.makeStructure(length=3000.0,width=200.0,height=400.0)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = TwoLeggedBeam.makeReinforcement(
    l_cover_of_stirrup=20,
    r_cover_of_stirrup=20,
    t_cover_of_stirrup=20,
    b_cover_of_stirrup=20,
    offset_of_stirrup=100,
    bent_angle=135,
    extension_factor=4,
    dia_of_stirrup=8,
    number_spacing_check=False,
    number_spacing_value=200,
    top_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    top_reinforcement_rebar_type="LShapeRebar",
    top_reinforcement_layer_spacing=30,
    bottom_reinforcement_number_diameter_offset=("1#20@-60+2#16@-60+1#20@-60", "3#16@-100"),
    bottom_reinforcement_rebar_type="LShapeRebar",
    bottom_reinforcement_layer_spacing=30,
    left_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    left_rebars_type="LShapeRebar",
    left_rebars_spacing=30,
    right_rebars_number_diameter_offset="1#16@-100+1#16@-100+1#16@-100",
    right_rebars_type="LShapeRebar",
    right_rebars_spacing=30,
    top_reinforcement_l_rebar_rounding=2,
    top_reinforcement_hook_extension=100,
    top_reinforcement_hook_orientation="Rear Outside",
    bottom_reinforcement_l_rebar_rounding=2,
    bottom_reinforcement_hook_extension=100,
    bottom_reinforcement_hook_orientation="Rear Outside",
    left_l_rebar_rounding=2,
    left_rebars_hook_extension=80,
    left_rebars_hook_orientation=("Rear Inside", "Front Inside", "Rear Inside"),
    right_l_rebar_rounding=2,
    right_rebars_hook_extension=80,
    right_rebars_hook_orientation=("Front Inside", "Rear Inside", "Front Inside"),
    structure=Structure,
    facename="Face6",
)
```





 

[Category:Reinforcement](Category:Reinforcement.md)
