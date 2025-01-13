# Reinforcement BentShapeRebar/ro
---
 GuiCommand:Addon   Name: Arch Rebar BentShape   Workbenches: Arch_Workbench/ro   Arch---


</div>

---
 GuiCommand:Addon   Name: Arch Rebar BentShape   Workbenches: Arch_Workbench/ro   Arch---



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/Arch_Rebar_BentShape.png" width=16px> Bent Shape Rebar** permite utilizatorului să creeze o formă de armătură bent shape reinforcing bar în elementul de structură.


</div>

This tool is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md).

<img alt="" src=images/Arch_Rebar_BentShape_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/BentShapeRebar.png  style="width:800px;">


</div>



## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Creați un elemente de [structure](Arch_Structure.md)
2.  Selectați orice fațetă a structurii
3.  Apoi selectați **<img src="images/Arch_Rebar_BentShape.png" width=16px> Bent Shape Rebar** dintre instrumentele dedicate rebar tools
4.  Un panou de activități contextual va apărea în partea stângă a ecranului, după cum se arată mai jos ![ 250px](images/_BentShapeDialog.png )
5.  Selectați orientarea dorită
6.  Definiți datele inițiale ca și capacul frontal, capacul din stânga, capacul din dreapta, capacul inferior, capacul superior, lungimea ancorei, unghiul îndoit, rotunjirea și diametrul barei
7.  Selectați modul de distribuire fie cantitate, fie spațiere
8.  Dacă spațiul este selectat, un utilizator poate de asemenea să opteze pentru [ spacing custom](Custom_Spacing.md)
9.  Selectați fațete utilizată petnru a verifica sau schimba faștea pentru distrubuția armăturii/ rebar distribution
10. Click pe **OK** sau pe **Apply** pentru a genera armăturile
11. Click pe **Cancel** pentru a ieși din task panel


</div>

<img alt="" src=images/BentShapeDialog.png  style="width:250px;"> 
*Task panel for the tool*



## Proprietăți

-    **Orientation**: Acesta decide orientarea armăturii (de ex. jos, sus, drepta și stânga).

-    **Front Cover**: Distanța dintre armături și fațetele selectate.

-    **Right Cover**: Distanța între capătul dintre capătul dreapta al armăturii și fațeta dreapta a structurii.

-    **Left Cover**: Distanța dintre capătul din stânga al armăturii și fațeta stângă a structurii

-    **Bottom Cover**: Distanța dintre armătură și fațeta de jos a structurii.

-    **Top Cover**: Distanța dintre armătură și fața superioară a structurii.

-    **Anchor Length**: Aceasta este lungimea brațelor armăturii îndoite/bent shape rebar.

-    **Bent Angle**: Stabilește unghiul de îndoire a bent shape rebar.

-    **Amount**: Cantitatea de armătură.

-    **Spacing**: Distanța între acele fiecărei bare.




<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/Arch_Rebar_BentShape.png" width=16px> Bent Shape Rebar** poate fi utilizat în [macros](macros.md) și de la consola Python console utilizând următorele funcții:


</div>


```python
Rebar = makeBentShapeRebar(f_cover, b_cover, l_cover, r_cover,
                           diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                           structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   Bent Shape Rebar are patru orientări diferite:
    -   Bottom
    -   Top
    -   Left
    -   Right
-   Adaugă un obiect Bent Shape reinforcing bar la obeictul structural selectat .
-   Dacă nu este dată nici o structură și nici o Facename, ea va avea ca intrare fațeta selectată de utilizator.
-   Aici argumentul CoverAlong este de tip tuplă.
-   Returnează noul obiect Rebar.


</div>

### Example


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

You can change the properties of the rebar with the following function:


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


{{docnav|[LShape Rebar](Arch_Rebar_LShape.md)|[Stirrup Rebar](Arch_Rebar_Stirrup.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Rebar_LShape.svg |IconC=Workbench_Arch.svg |IconR=Arch_Rebar_Stirrup.svg}}


</div>

{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement BentShapeRebar/ro
