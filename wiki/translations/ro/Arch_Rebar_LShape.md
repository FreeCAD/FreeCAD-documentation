---
- GuiCommand   */ro
   Name   *Arch Rebar LShape
   Name/ro   *Arch Rebar LShape
   MenuLocation   *Arch → Rebar tools
   Workbenches   *[Arch](Arch_Workbench/ro.md), [BIM](BIM_Workbench/ro.md)
   SeeAlso   *[Bent Rebar](Arch_Rebar_BentShape/ro.md), [Rebar](Arch_Rebar/ro.md)
   Version   *0.17
---

# Arch Rebar LShape/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/Arch_Rebar_LShape.png" width=16px> LShape Rebar** permite utilizatorului să creeze o armătură LShape reinforcing bar în elementele structurale.


</div>

The [LShape Rebar](Arch_Rebar_LShape.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_LShape_example.png  style="width   *400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/LShapeRebarNew.png  style="width   *800px;">


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Create a [structure](Arch_Structure.md) element
2.  Select any face of the structure
3.  Then select **<img src="images/Arch_Rebar_LShape.png" width=16px> LShape Rebar** from the rebar tools
4.  A task panel will pop-out on the left side of the screen as shown below <img alt="" src=images/LShapeDialog.png  style="width   *250px;">
5.  Select the desired orientation
6.  Give the inputs like front cover, left side cover, right side cover, bottom cover, top cover, rounding and diameter of the rebar
7.  Select the mode of distribution either amount or spacing
8.  If spacing is selected, a user can also opt for [custom spacing](Custom_Spacing.md)
9.  Pick selected face is used to verify or change the face for rebar distribution
10. Click **OK** or **Apply** to generate the rebars
11. Click **Cancel** to exit the task panel


</div>


   *   <img alt="" src=images/LShapeDialog.png  style="width   *250px;">



*Taskview panel for the Arch Rebar LShape tool*

## Proprietăți

-    **Orientation**   * Stabilește orientarea armăturii (ca de ex jos, sus, dreapta și stânga).

-    **Front Cover**   * Distanța dintre armături și fațetele selectate.

-    **Right Cover**   * Distanța între capătul dintre capătul dreapta al armăturii și fațeta dreapta a structurii.

-    **Left Cover**   * Distanța dintre capătul din stânga al armăturii și fațeta stângă a structurii

-    **Bottom Cover**   * Distanța dintre armătură și fațeta de jos a structurii.

-    **Top Cover**   * Distanța dintre armătură și fața superioară a structurii.

-    **Rounding**   * o valoarea a racordării de aplicat la colțutile barelor , exprimată în raport cu diametrul acestora.

-    **Amount**   * Cantitatea de armătură

-    **Spacing**   * Distanța dintre acele fiecărei bare.


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

The **<img src="images/Arch_Rebar_LShape.png" width=16px> LShape Rebar** tool can by used in [macros](macros.md) and from the python console by using the following function   *


</div>


```python
Rebar = makeLShapeRebar(f_cover, b_cover, l_cover, r_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom Left",
                        structure=None, facename=None)   *
```


<div class="mw-translate-fuzzy">

-   O armătură tip LShape Rebar are patru orientări diferite   *
    -   Bottom Right
    -   Bottom Left
    -   Top Right
    -   Top Left
-   Adaugă obiectul LShape reinforcing bar la obiectul structural selectat.
-   Dacă nu este dată nici o Structură și nici o Facename, ea va avea ca intrare fațeta selectat de utilizator.
-   Aici argumentul CoverAlong este de tip tuplă.
-   Returnează noul obiect Rebar.


</div>

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


<div class="mw-translate-fuzzy">


{{docnav/ro
|[UShape Rebar](Arch_Rebar_UShape/ro.md)
|[Bent Shape Rebar](Arch_Rebar_BentShape/ro.md)
|[Arch](Arch_Workbench/ro.md)
|IconL=Arch_Rebar_UShape.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_Rebar_BentShape.svg
}}


</div>


 

[Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar LShape/ro
