---
- GuiCommand:Addon/ro
   Name:Arch Rebar UShape
   Name/ro:Arch Rebar UShape
   MenuLocation:Arch → Rebar tools
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:None
   SeeAlso:[LShape Rebar](Arch_Rebar_LShape/ro.md)
   Addon:Reinforcement
---

# Arch Rebar UShape/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/UShapeRebar.png" width=16px> UShape Rebar** permite utilizatorului să creeze o armătură UShape reinforcing în elementul structural.


</div>

The **<img src="images/Arch_Rebar_UShape.svg" width=16px> [UShape Rebar](Arch_Rebar_UShape.md)** tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

<img alt="" src=images/Arch_Rebar_UShape_example.png  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Footing_UShapeRebar.png  style="width:800px;">


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Creați un element [structure](Arch_Structure.md)
2.  Selectați orice fațetă a structurii
3.  Apoi selectați butonul **<img src="images/UShapeRebar.png" width=16px> UShape Rebar** dintre instrumentele penru armături/rebar tools
4.  Un task panel contextual va apărea în stânga ecranului după cum se vede în ecranul de mai jos <img alt="" src=images/UShapeDialog.png  style="width:250px;">
5.  Selectați orientarea dorită
6.  Dați datele inițiale cum ar fi capacul frontal, capacul lateral din dreapta, capacul din partea stângă, capacul inferior, capacul superior, factorul de rotunjire și diametrul barei
7.  Selectați modul de distribuție sau mărimea spațiului
8.  Dacă spațierea este selectată, un utilizator poate de asemenea să opteze pentru [custom spacing](Custom_Spacing.md)
9.  Alegeți fața selectată care este utilizată pentru a verifica sau schimba fațeta pentru distribuția barei
10. Click pe tasta **OK** sau **Apply** pentru a genera armături rebars
11. Click pe tasta **Cancel** pentru a ieși din task panel


</div>


:   <img alt="" src=images/UShapeDialog.png  style="width:250px;">



*Taskview panel for the Arch Rebar UShape tool*

## Proprietăți

-    **Orientation**: Acesta decide orientarea armăturii (de ex. jos, sus, drepta și stânga).

-    **Front Cover**: Distanța dintre armături și fațetele selectate.

-    **Right Cover**: Distanța între capătul dintre capătul dreapta al armăturii și fațeta dreapta a structurii.

-    **Left Cover**: Distanța dintre capătul din stânga al armăturii și fațeta stângă a structurii

-    **Bottom Cover**: Distanța dintre armătură și fațeta de jos a structurii.

-    **Top Cover**: Distanța dintre armătură și fața superioară a structurii.

-    **Rounding**: O valoare de rotunjire care trebuie aplicată colțurilor barelor, exprimată în raport cu diametrul acestora.

-    **Amount**: Cantitatea de armătură

-    **Spacing**: Distnța dintre acele fiecărei bare.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/UShapeRebar.png" width=16px> UShape Rebar** poate fi utilizat în [macros](macros.md) și din consola Python prin utilizarea următoarea funcție:


</div>


```python
Rebar = makeUShapeRebar(f_cover, b_cover, r_cover, l_cover,
                        diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                        structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   Armătura UShape Rebar are patru orientări diferite:
    -   Bottom
    -   Top
    -   Right
    -   Left
-   Adaugă un obiect tip UShape reinforcing bar șa obiectul structural dat.
-   Dacă nu este dată nici o structură și nic o Facename, ea va avea ca intrare fațeta selectată de utilizator.
-   Returnează noul obiect Rebar


</div>


<div class="mw-translate-fuzzy">

Exemplu: Crearea unei armături tip bară în U.


</div>


```python
import FreeCAD, Arch, UShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = UShapeRebar.makeUShapeRebar(50, 20, 20, 20,
                                    8, 50, 4, True, 6, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = UShapeRebar.makeUShapeRebar(50, 50, 20, 20,
                                     8, 50, 4, True, 6, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```

### Edition of the rebar 


<div class="mw-translate-fuzzy">

Schimbarea proprietăților barei în U.


</div>


```python
editUShapeRebar(Rebar, f_cover, b_cover, r_cover, l_cover,
                diameter, t_cover, rounding, amount_spacing_check, amount_spacing_value, orientation,
                structure=None, facename=None) 
```

-    `Rebar`is a previously created `UShapeRebar` object.

-   The other parameters are the same as required by the `makeUShapeRebar()` function.

-    `structure`and `facename` may be omitted so that the rebar stays in the original structure.


```python
import UShapeRebar

UShapeRebar.editUShapeRebar(Rebar, 50, 50, 20, 20,
                            16, 20, 5, True, 5, "Top")

UShapeRebar.editUShapeRebar(Rebar2, 70, 50, 20, 20,
                            16, 70, 5, True, 5, "Top")
```


<div class="mw-translate-fuzzy">


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar UShape/ro
