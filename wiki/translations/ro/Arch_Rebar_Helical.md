---
- GuiCommand:Addon/ro
   Name: Arch Rebar Helical
   Name/ro: Arch Rebar Helical
   MenuLocation: Arch -> Rebar tools
   Workbenches: Arch_Workbench/ro
   Shortcut: None
   SeeAlso: Arch_Rebar/ro
   Addon: Reinforcement
---

# Arch Rebar Helical/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/Arch_Rebar_Helical.png" width=16px> Helical Rebar** permite utilizatorului să creeze o armătură elicoidală în elementul de structură.


</div>

The [Helical Rebar](Arch_Rebar_Helical.md) tool is also integrated into [BIM Workbench](BIM_Workbench.md).

This command is part of the [Reinforcement Workbench](Reinforcement_Workbench.md), an [external workbench](External_workbenches.md) that can be installed with the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) via the **Tools → Addon manager → Reinforcement** menu.

:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/HelicalRebar.png  style="width:800px;">


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Creați un element [structure](Arch_Structure.md)
2.  Selectați orice fațetă a structurii
3.  Apoi selectați {{KEY | <img src="images/_Arch_Rebar_Helical.png_" width= 16px> Helix Rebar}} din uneltele pentru bare
4.  Va apărea un panou de sarcini în partea stângă a ecranului, după cum se arată mai jos ![ 250px](images/_HelicalRebarDialog.png )
5.  Selectați orientarea dorită
6.  Dați intrările ca și capacul frontal, capacul lateral din dreapta, capacul lateral din stânga, capacul inferior și diametrul barei
7.  Selectați fie modul de distribuire fie cantitate, fie spațiere
8.  Dacă spațiul este selectat, un utilizator poate de asemenea să opteze pentru [ spacing custom](Custom_Spacing.md)
9.  Selectează fațeta selectată este utilizată pentru a verifica sau schimba fața pentru distribuția barei
10. Faceți clic pe {{KEY | OK}} sau pe {{KEY | Apply}} pentru a genera barele de armare
11. Faceți clic pe {{KEY | Cancel}} pentru a ieși din panoul de activități


</div>


:   <img alt="" src=images/HelicalRebarDialog.png  style="width:250px;">



*Taskview panel for the Arch Rebar Helical tool*



## Proprietăți

-    **Side Cover**:distanța dintre armatură și fața curbată.

-    **Top Cover**: Distanța dintre armătură din fața superioară a structurii.

-    **Bottom Cover**: distanța dintre barele din partea inferioară a structurii.

-    {{PropertyData | Pitch}}: Pasul unei spirale este înălțimea unei singure rotiri helix, măsurată paralel cu axa spiralei.

-    {{PropertyData | Diameter}}: Diametrul barei.




<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


**See also:**

[Arch API](Arch_API.md), [Reinforcement API](Reinforcement_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Instrumentul **<img src="images/Arch_Rebar_Helical.png" width=16px> Helical Rebar** poate fi utilizat în [macros](macros.md) și de la consola Python prin utilizarea următoarei funcției:


</div>


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```


<div class="mw-translate-fuzzy">

-   Adaugă un obiect Straight reinforcing bar la obiectul structural dat.
-   Dacă nu este dată nici o structură și Facename, ea va avea ca intrare fațeta selectată de utilizator.
-   Aici argumentul CoverAlong este de tip tuplă .
-   Returnează noul obiect Rebar.


</div>

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


<div class="mw-translate-fuzzy">


{{docnav|[Stirrup Rebar](Arch_Rebar_Stirrup.md)|[Circular Column Reinforcement](Arch_Rebar_Circular_ColumnReinforcement.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Rebar_Stirrup.svg|IconC=Workbench_Arch.svg |IconR=Arch_Rebar_ColumnReinforcement.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar Helical/ro
