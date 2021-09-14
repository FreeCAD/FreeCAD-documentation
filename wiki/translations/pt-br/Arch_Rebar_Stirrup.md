---
- GuiCommand:
   Name:Arch Rebar Stirrup
   MenuLocation:Arch → Rebar tools → Stirrup or 3D/BIM → Reinforcement → Stirrup
   Workbenches:[Arch](Arch_Workbench.md), [BIM](BIM_Workbench.md)
   Version:0.17
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Rebar](Arch_Rebar.md), [Arch Rebar Helical](Arch_Rebar_Helical.md)
---

## Description

The [Stirrup Rebar](Arch_Rebar_Stirrup.md) tool allows the user to create a set of stirrup reinforcing bars inside an [Arch Structure](Arch_Structure.md) object.

The [Stirrup Rebar](Arch_Rebar_Stirrup.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;"> 
*One set of stirrup reinforcement bars inside an [Arch Structure](Arch_Structure.md) object*

## Usage

1.  Select any face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.

2.  Then select **<img src="images/Arch_Rebar_Stirrup.svg" width=16px> [Stirrup Rebar](Arch_Rebar_Stirrup.md)** from the rebar tools.

3.  A [task panel](task_panel.md) will pop-out on the left side of the screen as shown below.

4.  Select the desired orientation.

5.  Populate the inputs like \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' and \'Diameter\' of the rebar.

6.  Select the mode of distribution either \'Amount\' or \'Spacing\'.
    -   If \'Spacing\' is selected, a user can also opt for [custom spacing](Custom_Spacing.md).

7.  
    **Pick Selected Face**is used to verify or change the face for rebar distribution.

8.  Click **OK** or **Apply** to generate the rebars.

9.  Click **Cancel** to exit the task panel.

:   <img alt="" src=images/StirrupDialog.png  style="width:250px;">


*Taskview panel for the Arch Rebar Stirrup tool*

## Properties

-    **Front Cover**: The distance between rebar and selected face.

-    **Right Cover**: The distance between the right end of the rebar to right face of the structure.

-    **Left Cover**: The distance between the left end of the rebar to the left face of the structure.

-    **Bottom Cover**: The distance between rebar from the bottom face of the structure.

-    **Top Cover**: The distance between rebar from the top face of the structure.

-    **Bent Angle**: Bent angle defines the angle at the ends of a stirrup.

-    **Bent Factor**: Bent Factor defines length of stirrup end.

-    **Amount**: The amount of rebars.

-    **Spacing**: The distance between the axes of each bar.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Stirrup Rebar tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```

-   Creates a `Rebar` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `l_cover`, `r_cover`, `t_cover`, `b_cover`, and `f_cover` are inner offset distances for the rebar elements with respect to the faces of the structure. They are respectively the left, right, top, bottom, and front offsets.

-    `diameter`is the diameter of the reinforcement bars inside the structure.

-    `rounding`is the parameter that determines the bending radius of the reinforcement bars as they make a loop.

-    `bentLength`and `bentAngle` define the length and angle of the tip of the reinforcement loop.

-    `amount_spacing_check`if it is `True` it will create as many reinforcement loops as given by `amount_spacing_value`; if it is `False` it will create reinforcement loops separated by the numerical value of `amount_spacing_value`.

-    `amount_spacing_value`specifies the number of reinforcement loops, or the value of the separation between them, depending on `amount_spacing_check`.

### Example


```python
import Draft, Arch, Stirrup

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = Stirrup.makeStirrup(20, 20, 20, 20, 20,
                            115, 4, 8, 2, True, 10, Structure, "Face6")
```

### Edition of the rebar 

You can change the properties of the rebar with the following function 
```python
editStirrup(Rebar, l_cover, r_cover, t_cover, b_cover, f_cover,
            bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
            structure=None, facename=None)
```

-    `Rebar`is a previously created `StirrupRebar` object.

-   The other parameters are the same as required by the `makeStirrup()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import Stirrup

Stirrup.editStirrup(Rebar, 20, 20, 20, 20, 50,
                    100, 4, 14, 8, True, 8)
```





 

[Category:Reinforcement](Category:Reinforcement.md)
