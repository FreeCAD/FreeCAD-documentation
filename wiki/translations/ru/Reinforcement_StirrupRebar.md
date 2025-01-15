---
 GuiCommand:
   Name/ru: Кольцевая арматура
   Name: Arch_Rebar_Stirrup
   MenuLocation: Arch , Rebar tools , Stirrup<br>3D/BIM , Reinforcement tools , Stirrup
   Workbenches: Arch_Workbench/ru, BIM_Workbench/ru
   Version: 0.17
   SeeAlso: Reinforcement_Workbench/ru, Arch_Rebar/ru, Arch_Rebar_Helical/ru
---

# Reinforcement StirrupRebar/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Инструмент **<img src="images/Arch_Rebar_Stirrup.png" width=16px> Stirrup Rebar** позволяет пользователю создавать в структурном элементе арматурный стержень с изогнутой формой.


</div>

This tool is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Stirrup.png  style="width:800px;">


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  Создайте элемент [structure](Arch_Structure.md)
2.  Выберите любую грань структуры
3.  Then select **<img src="images/Arch_Rebar_Stirrup.png" width=16px> Stirrup Rebar** from the rebar tools
4.  A task panel will pop-out on the left side of the screen as shown below <img alt="" src=images/StirrupDialog.png  style="width:250px;">
5.  Select the desired orientation
6.  Give the inputs like left cover, right cover, top cover, bottom, front cover, bent angle, bent factor, rounding and diameter of the rebar
7.  Select the mode of distribution either amount or spacing
8.  If spacing is selected, a user can also opt for [custom spacing](Custom_Spacing.md)
9.  Pick selected face is used to verify or change the face for rebar distribution
10. Нажмите {{KEY | OK}} или {{KEY | Apply}}, чтобы создать арматуру
11. Нажмите {{KEY | Cancel}}, чтобы выйти из панели задач


</div>

<img alt="" src=images/StirrupDialog.png  style="width:250px;"> 
*Task panel for the tool*



## Свойства

-    **Front Cover**:

Расстояние между арматурой и выбранной поверхностью.

-    **Right Cover**: The distance between the right end of the rebar to right face of the structure.

-    **Left Cover**: The distance between the left end of the rebar to the left face of the structure.

-    **Bottom Cover**: The distance between rebar from the bottom face of the structure.

-    **Top Cover**: The distance between rebar from the top face of the structure.

-    **Bent Angle**: Bent angle defines the angle at the ends of a stirrup.

-    **Bent Factor**: Bent Factor defines length of stirrup end.

-    **Amount**: The amount of rebars.

-    **Spacing**:Расстояние между осями каждого стержня.




<div class="mw-translate-fuzzy">

## Сценарии


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Инструмент {{KEY | <img src="images/_Arch_Rebar_Stirrup.png_" width= 16px> Stirrup Rebar}} можно использовать в [macros](macros.md) и на консоли python с помощью следующей функции:


</div>


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



### Пример


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

You can change the properties of the rebar with the following function:


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


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement StirrupRebar/ru
