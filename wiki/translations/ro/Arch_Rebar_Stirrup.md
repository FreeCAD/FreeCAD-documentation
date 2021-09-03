---
- GuiCommand:/ro
   Name/ro:Arch Rebar Stirrup
   MenuLocation:Arch → Rebar tools
   Workbenches:[Arch](Arch_Workbench/ro.md), [BIM](BIM_Workbench/ro.md)
   SeeAlso:[Helical Rebar](Arch_Rebar_Helical/ro.md), [Rebar](Arch_Rebar/ro.md)
   Version:0.17
---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/Arch_Rebar_Stirrup.png" width=16px> Stirrup Rebar** permite utilizatorului să creeze un

stirrup reinforcing bar în elementul de structură.


</div>

The [Stirrup Rebar](Arch_Rebar_Stirrup.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Stirrup.png  style="width:800px;">


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Creează un element [structure](Arch_Structure.md)
2.  Select any face of the structure
3.  Then select **<img src="images/Arch_Rebar_Stirrup.png" width=16px> Stirrup Rebar** from the rebar tools
4.  A task panel will pop-out on the left side of the screen as shown below <img alt="" src=images/StirrupDialog.png  style="width:250px;">
5.  Select the desired orientation
6.  Give the inputs like left cover, right cover, top cover, bottom, front cover, bent angle, bent factor, rounding and diameter of the rebar
7.  Select the mode of distribution either amount or spacing
8.  If spacing is selected, a user can also opt for [custom spacing](Custom_Spacing.md)
9.  Pick selected face is used to verify or change the face for rebar distribution
10. Click **OK** or **Apply** to generate the rebars
11. Click pe **Cancel** ieșirea din task panel


</div>


:   <img alt="" src=images/StirrupDialog.png  style="width:250px;">


*Taskview panel for the Arch Rebar Stirrup tool*

## Proprietăți

-    **Front Cover**: Distanța dintre armături și fațetele selectate.

-    **Right Cover**: Distanța între capătul dintre capătul dreapta al armăturii și fațeta dreapta a structurii.

-    **Left Cover**: Distanța dintre capătul din stânga al armăturii și fațeta stângă a structurii

-    **Bottom Cover**: Distanța dintre armătură și fațeta de jos a structurii.

-    **Top Cover**: Distanța dintre armătură și fața superioară a structurii.

-    **Bent Angle**: Bent angle defines the angle at the ends of a stirrup.

-    **Bent Factor**: Bent Factor defines length of stirrup end.

-    **Amount**: Cantitatea de armătură

-    **Spacing**: Distanța dintre acele fiecărei bare.


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/Arch_Rebar_Stirrup.png" width=16px> Stirrup Rebar** poate fi utilizat în [macros](macros.md) și de la consola Python prin utilizarea următoarei funcției:


</div>


```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   Adds a Stirrup reinforcing bar object to the given structural object.
-   If no Structure and Facename is given, it will take user selected face as input.
-   Here CoverAlong argument is having type tuple.
-   Returns the new Rebar object.


</div>


<div class="mw-translate-fuzzy">

Exemplu: Crearea unei armături tip Stirrup rebar.


</div>


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


<div class="mw-translate-fuzzy">

Schimbarea proprietăților barei Stirrup.


</div>


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


{{docnav/ro|[Bent Shape Rebar](Arch_Rebar_BentShape/ro.md)|[Helical Rebar](Arch_Rebar_Helical/ro.md)|[Arch](Arch_Module/ro.md)|IconL=Arch_Rebar_BentShape.svg |IconC=Workbench_Arch.svg |IconR=Arch_Rebar_Helical.svg}}


</div>


 

[Category:Reinforcement{{\#translation:}}](Category:Reinforcement.md)
