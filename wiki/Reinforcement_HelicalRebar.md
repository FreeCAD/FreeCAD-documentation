---
 GuiCommand:
   Name: Reinforcement HelicalRebar
   MenuLocation: 3D/BIM , Reinforcement tools , Helical Rebar
   Workbenches: Reinforcement_Workbench, BIM_Workbench
   Version: 0.17
   SeeAlso: 
---

# Reinforcement HelicalRebar

## Description

The [Reinforcement HelicalRebar](Reinforcement_HelicalRebar.md) tool allows the user to create a continuous helical reinforcing bar inside an [Arch Structure](Arch_Structure.md) object.

This tool is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).



:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">

 
*One continuous helical reinforcement bar inside an [Arch Structure](Arch_Structure.md)*

## Usage

1.  Select any face of a previously created **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)** object.

2.  Then select **<img src="images/Reinforcement_HelicalRebar.svg" width=16px> [Helical Rebar](Reinforcement_HelicalRebar.md)** from the rebar tools.

3.  A [task panel](Task_panel.md) will pop-out on the left side of the screen as shown below.

4.  Select the desired orientation.

5.  Populate the inputs like \'Left Cover\', \'Right Cover\', \'Top Cover\', \'Bottom Cover\', \'Front Cover\', \'Bent Angle\', \'Bent Factor\', \'Rounding\' and \'Diameter\' of the rebar.

6.  Select the mode of distribution either \'Amount\' or \'Spacing\'.
    -   If \'Spacing\' is selected, a user can also opt for [custom spacing](Reinforcement_Custom_Spacing.md).

7.  
    **Pick Selected Face**is used to verify or change the face for rebar distribution.

8.  Click **OK** or **Apply** to generate the rebars.

9.  Click **Cancel** to exit the task panel.

 <img alt="" src=images/HelicalRebarDialog.png  style="width:250px;">  
*Task panel for the tool*

## Properties

-    **Side Cover**: The distance between rebar to the curved face.

-    **Top Cover**: The distance between rebar from the top face of the structure.

-    **Bottom Cover**: The distance between rebar from the bottom face of the structure.

-    **Pitch**: The pitch of a helix is the height of one complete helix turn, measured parallel to the axis of the helix.

-    **Diameter**: Diameter of the rebar.

## Scripting


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The Reinforcement HelicalRebar tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

 
```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Creates a `Rebar` object from the given `structure`, which is an [Arch Structure](Arch_Structure.md), and `facename`, which is a face of that structure.
    -   If no `structure` nor `facename` are given, it will take the user selected face as input.

-    `s_cover`, `b_cover`, and `t_cover` are inner offset distances for the rebar with respect to the faces of the structure. They are respectively the side, bottom, and top offsets.

-    `diameter`is the diameter of the reinforcement spiral inside the structure.

-    `pitch`is the parameter that determines how close or far apart each spiral loop is to each other.

### Example

 
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




 {{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement HelicalRebar
