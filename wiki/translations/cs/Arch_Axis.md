# Arch Axis/cs
---
- GuiCommand:   Name: Arch Axis   Name/cs: Osy   Workbenches: [[Arch_Workbench/cs   Architektura]]|MenuLocation: Arch - Osy   Shortcut: A X---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Osy Vám umožňuje umístit osový systém do aktuálního dokumentu. Vzdálenosti a úhel mezi osami je uživatelsky nastavitelný, stejně jako styl číslování. Osy slouží především jako reference k uchopování objektů, ale může taky být použit společně se [strukturami](Arch_Structure/cs.md) k vytváření parametrizovaných polí příčníků nebo sloupů.


</div>

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;"> 
*Two axes objects positioned perpendicularly to each other to create a grid*


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Stiskněte tlačítko **<img src="images/Arch_Axis.png" width=16px> [Osy](Arch_Axis/cs.md)
** nebo klávesy **A** a potom **X**
2.  [Posun](Draft_Move/cs.md)/[otočit](Draft_Rotate/cs.md) osový systém do požadované pozice
3.  Přejděte do editačního módu dvojklikem na osový systém v panelu stromu a potvrďte nastavení počtu os, vzdáleností a úhlů mezi osami.


</div>

## Volby


<div class="mw-translate-fuzzy">

-   Každá osa v osovém systému má svou vlastní vzdálenost a úhel v relaci k předchozí ose. To umožňuje vytvořit velmi komplexní systémy jako například ne-ortogonální systémy, polární systémy nebo jakýkoliv nehomogenní systém.
-   Délka os, rozměry bublin a styly číslování jsou uživatelsky nastavitelné pomocí vlastností osového systému.


</div>

## Vlastnosti


<div class="mw-translate-fuzzy">

-    **Délka**: Délka os

-    **Velikost bubliny**: Velikost osové bubliny

-    **Styl číslování**: Jak jsou osy číslovány: 1,2,3, A,B,C, atd\...


</div>

## Use as section mark 

By setting the **Bubble Position** property to **Arrow left/right** or **Bar left/right**, the axis will display a filled arrow or bar instead of the bubble, so it can be used as a section mark. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Osy může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```


<div class="mw-translate-fuzzy">


:   vytváří osový systém založený na daném počtu os a vzdálenosti mezi osami


</div>

Příklad:


```python
import Draft, Arch

Axes = Arch.makeAxis(5, 1000)

Axes.ViewObject.LineWidth = 3
Axes.ViewObject.BubbleSize = 200
Axes.ViewObject.FontSize = 150

Axes2 = Arch.makeAxis(6, 500)

Axes2.ViewObject.LineWidth = 2
Axes2.ViewObject.BubbleSize = 200
Axes2.ViewObject.FontSize = 150
Axes2.ViewObject.NumberingStyle = "A,B,C"
FreeCAD.ActiveDocument.recompute()

Axes2.Length = 6000
Draft.rotate(Axes2, -90)
Draft.move(Axes2, FreeCAD.Vector(-1000, 2500, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Axis/cs
