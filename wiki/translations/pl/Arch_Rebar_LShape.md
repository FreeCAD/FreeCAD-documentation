---
- GuiCommand:
   Name:Arch Rebar LShape
   MenuLocation:Arch → Rebar tools → LShape Rebar or 3D/BIM → Reinforcement → LShape Rebar
   Workbenches:[Arch](Arch_Workbench.md), [BIM](BIM_Workbench.md)
   Version:0.17
   SeeAlso:[Reinforcement](Reinforcement_Workbench.md), [Arch Rebar](Arch_Rebar.md), [Arch Rebar Bent](Arch_Rebar_BentShape.md)
---

# Arch Rebar LShape/pl

## Description

The [LShape Rebar](Arch_Rebar_LShape.md) tool allows the user to create a set of L-shaped reinforcing bars inside an [Arch Structure](Arch_Structure.md) object.

The [LShape Rebar](Arch_Rebar_LShape.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_LShape_example.png  style="width:400px;"> 
*Four sets of L-shaped reinforcement bars inside an [[Arch Structure]]*

## Usage

1.  Select any face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [[Arch Structure]]** object.

2.  Then select **<img src="images/Arch_Rebar_LShape.svg" width=16px> [LShape Rebar](Arch_Rebar_LShape.md)** from the rebar tools.

3.  A [task panel](task_panel.md) will pop-out on the left side of the screen as shown below.

4.  Select the desired orientation.

5.  Populate the inputs like \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' and \'Diameter\' of the rebar.

6.  Select the mode of distribution either \'Amount\' or \'Spacing\'.
    -   If \'Spacing\' is selected, a user can also opt for [custom spacing](Custom_Spacing.md).

7.  
    **Pick Selected Face**is used to verify or change the face for rebar distribution.

8.  Click **OK** or **Apply** to generate the rebars.

9.  Click **Cancel** to exit the task panel.

:   <img alt="" src=images/LShapeDialog.png  style="width:250px;">



*Taskview panel for the Arch Rebar LShape tool*

## Properties

-    **Orientation**: It decides the orientation of the rebar (like a bottom, top, right and left).

-    **Front Cover**: The distance between rebar and selected face.

-    **Right Cover**: The distance between the right end of the rebar to right face of the structure.

-    **Left Cover**: The distance between the left end of the rebar to the left face of the structure.

-    **Bottom Cover**: The distance between rebar from the bottom face of the structure.

-    **Top Cover**: The distance between rebar from the top face of the structure.

-    **Rounding**: A rounding value to be applied to the corners of the bars, expressed in times the diameter.

-    **Amount**: The amount of rebars.

-    **Spacing**: The distance between the axes of each bar.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The LShape Rebar tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function: 
```python
Rebar = makeLShapeRebar(f_cover, b_cover, l_cover, r_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom Left",
                        structure=None, facename=None):
```

-   Creates a `Rebar` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover`, and `t_cover` are inner offset distances for the rebar elements with respect to the faces of the structure. They are respectively the front, bottom, left, right, and top offsets.

-    `diameter`is the diameter of the reinforcement bars inside the structure.

-    `rounding`is the parameter that determines the bending radius of the reinforcement bars.

-    `amount_spacing_check`if it is True it will create as many reinforcement bars as given by amount\_spacing\_value; if it is False it will create reinforcement bars separated by the numerical value of amount\_spacing\_value.

-    `amount_spacing_value`specifies the number of reinforcement bars, or the value of the separation between them, depending on amount\_spacing\_check.

-    `orientation`specifies the orientation of the rebar; it can be `"Bottom Right"`, `"Bottom Left"`, `"Top Right"`, or `"Top Left"`.

### Example


```python
import FreeCAD, Arch, LShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = LShapeRebar.makeLShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom Left", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = LShapeRebar.makeLShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom Left", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```

### Edition of the rebar 

You can change the properties of the rebar with the following function 
```python
editLShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None)
```

-    `Rebar`is a previously created `LShapeRebar` object.

-   The other parameters are the same as required by the `makeLShapeRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import LShapeRebar

LShapeRebar.editLShapeRebar(Rebar, 50, 50, 20, 20,
                            12, 50, 6, True, 5, "Top Right")

LShapeRebar.editLShapeRebar(Rebar2, 50, 50, 20, 20,
                            12, 70, 6, True, 5, "Top Right")
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar LShape/pl
