---
- GuiCommand   *
   Name   *Arch Rebar BentShape
   MenuLocation   *Arch → Rebar tools → Bent-Shape Rebar<br>3D/BIM → Reinforcement tools → Bent-Shape Rebar
   Workbenches   *[Arch](Arch_Workbench.md), [BIM](BIM_Workbench.md)
   Version   *0.17
   SeeAlso   *[Reinforcement](Reinforcement_Workbench.md), [Arch Rebar](Arch_Rebar.md), [Arch Rebar Stirrup](Arch_Rebar_Stirrup.md)
---

# Arch Rebar BentShape/pt-br

## Descrição

The [BentShape Rebar](Arch_Rebar_BentShape.md) tool allows the user to create a set of bent reinforcing bars inside an [Arch Structure](Arch_Structure.md) object.

The [BentShape Rebar](Arch_Rebar_BentShape.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_BentShape_example.png  style="width   *400px;"> 
*Two sets of bent reinforcement bars inside an [Arch Structure](Arch_Structure.md)*

## Utilização

1.  Select any face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.

2.  Then select **<img src="images/Arch_Rebar_BentShape.svg" width=16px> [BentShape Rebar](Arch_Rebar_BentShape.md)** from the rebar tools.

3.  A [task panel](task_panel.md) will pop-out on the left side of the screen as shown below.

4.  Select the desired orientation.

5.  Populate the inputs like \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' and \'Diameter\' of the rebar.

6.  Select the mode of distribution either \'Amount\' or \'Spacing\'.
    -   If \'Spacing\' is selected, a user can also opt for [custom spacing](Custom_Spacing.md).

7.  
    **Pick Selected Face**is used to verify or change the face for rebar distribution.

8.  Click **OK** or **Apply** to generate the rebars.

9.  Click **Cancel** to exit the task panel.

   *   <img alt="" src=images/BentShapeDialog.png  style="width   *250px;">



*Taskview panel for the Arch Rebar BentShape tool*

## Propriedades

-    **Orientation**   * It decides the orientation of the rebar (like a bottom, top, right and left).

-    **Front Cover**   * The distance between rebar and selected face.

-    **Left Cover**   * The distance between the left end of the rebar to the left face of the structure.

-    **Right Cover**   * The distance between the right end of the rebar to right face of the structure.

-    **Bottom Cover**   * The distance between rebar from the bottom face of the structure.

-    **Top Cover**   * The distance between rebar from the top face of the structure.

-    **Anchor Length**   * It is the arm\'s length of bent shape rebar.

-    **Bent Angle**   * It decides angle in bent shape rebar.

-    **Amount**   * The amount of rebars.

-    **Spacing**   * The distance between the axes of each bar.

## Scripting


**See also   ***

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The BentShape Rebar tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function   * 
```python
Rebar = makeBentShapeRebar(f_cover, b_cover, l_cover, r_cover,
                           diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                           structure=None, facename=None)
```

-   Creates a `Rebar` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover`, and `t_cover` are inner offset distances for the rebar elements with respect to the faces of the structure. They are respectively the front, bottom, left, right, and top offsets.

-    `diameter`is the diameter of the reinforcement bars inside the structure.

-    `rounding`is the parameter that determines the bending radius of the center reinforcement bars.

-    `bentLength`and `bentAngle` define the length of the tip of the reinforcement bars, and the bending angle from the center bars.

-    `amount_spacing_check`if it is `True` it will create as many reinforcement bars as given by `amount_spacing_value`; if it is `False` it will create reinforcement bars separated by the numerical value of `amount_spacing_value`.

-    `amount_spacing_value`specifies the number of reinforcement bars, or the value of the separation between them, depending on `amount_spacing_check`.

-    `orientation`specifies the orientation of the rebar; it can be `"Bottom"`, `"Top"`, `"Left"`, or `"Right"`.

### Exemplos


```python
import FreeCAD, Arch, BentShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=100)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = BentShapeRebar.makeBentShapeRebar(50, 20, 20, 20,
                                          8, 40, 100, 135, 2, True, 4, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = BentShapeRebar.makeBentShapeRebar(50, 40, 20, 20,
                                           8, 20, 100, 135, 2, True, 4, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```

### Edition of the rebar 

You can change the properties of the rebar with the following function


```python
editBentShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                   diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation,
                   structure=None, facename=None)
```

-    `Rebar`is a previously created `BentShapeRebar` object.

-   The other parameters are the same as required by the `makeBentShapeRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import BentShapeRebar

BentShapeRebar.editBentShapeRebar(Rebar, 50, 20, 20, 20,
                                  12, 20, 100, 155, 2, True, 6, "Top")

BentShapeRebar.editBentShapeRebar(Rebar2, 50, 35, 20, 20,
                                  12, 35, 100, 155, 2, True, 6, "Top")
```


<div class="mw-translate-fuzzy">





</div>


 

[Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar BentShape/pt-br
