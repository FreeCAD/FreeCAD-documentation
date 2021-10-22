---
- GuiCommand:Addon/ru
   Name:Arch Rebar Helical   Name/ru:Arch Rebar Helical
   MenuLocation:Arch → Rebar tools
   Workbenches:[Arch](Arch_Workbench/ru.md), [BIM](BIM_Workbench/ru.md)
   Addon:Reinforcement
   Shortcut:None
   SeeAlso:[Arch Rebar](Arch_Rebar/ru.md), [Stirrup Rebar](Arch_Rebar_Stirrup/ru.md), [Column Reinforcement](Arch_Rebar_ColumnReinforcement/ru.md)
   Version:0.17
---

# Arch Rebar Helical/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Инструмент **<img src="images/Arch_Rebar_Helical.png" width=16px> Helical Rebar** позволяет пользователю создавать в структурном элементе арматурный стержень с изогнутой формой.


</div>

The [Helical Rebar](Arch_Rebar_Helical.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the _ via the **Tools → Addon manager → Reinforcement** menu.

:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/HelicalRebar.png  style="width:800px;">


</div>

## Применение

1.  Select any face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.

2.  Then select **<img src="images/Arch_Rebar_Helical.svg" width=16px> [Helical Rebar](Arch_Rebar_Helical.md)** from the rebar tools.

3.  A [task panel](task_panel.md) will pop-out on the left side of the screen as shown below.

4.  Select the desired orientation.

5.  Populate the inputs like \'Left Cover\', Right Cover, Top Cover, \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' and \'Diameter\' of the rebar.

6.  Select the mode of distribution either \'Amount\' or \'Spacing\'.
    -   If \'Spacing\' is selected, a user can also opt for [custom spacing](Custom_Spacing.md).

7.  
    **Pick Selected Face**is used to verify or change the face for rebar distribution.

8.  Click **OK** or **Apply** to generate the rebars.

9.  Click **Cancel** to exit the task panel.

:   <img alt="" src=images/HelicalRebarDialog.png  style="width:250px;">



*Taskview panel for the Arch Rebar Helical tool*

## Свойства

-    **Side Cover**: The distance between rebar to the curved face.

-    **Top Cover**: The distance between rebar from the top face of the structure.

-    **Bottom Cover**: The distance between rebar from the bottom face of the structure.

-    **Pitch**: The pitch of a helix is the height of one complete helix turn, measured parallel to the axis of the helix.

-    **Diameter**: Diameter of the rebar.


<div class="mw-translate-fuzzy">

## Сценарии


</div>

The Helical Rebar tool can be used in [macros](macros.md) and from the [Python](Python.md) console by using the following function:


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Creates a `Rebar` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `s_cover`, `b_cover`, and `t_cover` are inner offset distances for the rebar with respect to the faces of the structure. They are respectively the side, bottom, and top offsets.

-    `diameter`is the diameter of the reinforcement spiral inside the structure.

-    `pitch`is the parameter that determines how close or far apart each spiral loop is to each other.

### Пример


```python
import FreeCAD, Draft, Arch, HelicalRebar

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = HelicalRebar.makeHelicalRebar(10, 50, 8, 50, 50, structure, "Face2")
```

### Edition of the rebar 

You can change the properties of the rebar with the following function


```python
editHelicalRebar(Rebar, s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-    `Rebar`is a previously created `HelicalRebar` object.

-   The other parameters are the same as required by the `makeHelicalRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import HelicalRebar

HelicalRebar.editHelicalRebar(Rebar, 20, 100, 20, 20, 100)
```


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Helical/ru
