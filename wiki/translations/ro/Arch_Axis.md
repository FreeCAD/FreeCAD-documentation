---
- GuiCommand:/ro
   Name:Arch Axis
   Name/ro:Arch Axis
   MenuLocation:Arch → Axis
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:**A** **X**
   SeeAlso:[Axis System](Arch_AxisSystem/ro.md), [Grid](Arch_Grid.md)
---

# Arch Axis/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Axis vă permite să plasați o serie de axe în documentul curent. Distanța și unghiul dintre axe sunt personalizabile, precum și stilul de numerotare. Axa servește în principal ca trimiteri la obiecte de tip ancoră (snap), dar poate fi folosită și împreună cu [Axes Systems](Arch_AxisSystem.md), și poate fi conectat de alte obiecte Arch pentru a crea rețele parametrice, de exemplu grinzi sau coloane [Grids](Arch_Grid.md) can also be used in places of axes.


</div>

<img alt="" src=images/Arch_Axis_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

\"Imaginea de mai jos arată două obiecte diferite poziționate perpendicular una pe cealaltă\"


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  apăsați tasta **<img src="images/Arch_Axis.png" width=16px> [[Arch Axis]]**, sau **A** then **X** keys
2.  [Move](Draft_Move.md)/[rotate](Draft_Rotate.md) axele sistemului în poziția dorită
3.  Intrați în modul de editare făcând dublu clic pe sistemul de axe din vizualizarea arborescentă pentru a regla setările sale, cum ar fi numărul de axe, distanțele și unghiurile dintre axe.


</div>

## Opţiuni

-   Fiecare axă din serie are distanța și unghiul propriu față de axa anterioară. Aceasta permite realizarea unor sisteme foarte complexe, cum ar fi sistemele non-ortogonale, sistemele polar sau orice alt sistem neuniform
-   Dublu clic pe axă în arborele vederilor permite editarea distanțelor, unghiurilor și etichetei fiecărei axe
-   Lungimile axelor, dimensiunea bulelor și stilurile de numerotare sunt personalizabile direct prin proprietățile sistemului de axe
-   Fiecare axă poate afișa, de asemenea, o etichetă, editabilă și prin dialogul panoului de activități

## Proprietăți


<div class="mw-translate-fuzzy">

-    **Length**: Lungimea axelor

-    **Bubble Size**: Mărimea bulei axei

-    **Numeration style**: cum sunt numerotate axele: 1,2,3, A,B,C, etc\...

-    **Bubble Position**: Unde este plasată bula pe axă: La început, la capăt, ambele sau niciuna.

-    **Font Name**: Fontul folosit pentru a desena numprul bulei și/sau etichetei

-    **Font Size**: Mărimea etichetei text (Textul bulei este controlat de mărimea bulei)

-    **Show Labels**: Activează/dezactivează afișarea textului etichetei


</div>

## Use as section mark 

By setting the **Bubble Position** property to **Arrow left/right** or **Bar left/right**, the axis will display a filled arrow or bar instead of the bubble, so it can be used as a section mark. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

Instrumentul Axis poate fi utilizat în [macros](macros.md) și de la consola python utilizând umătoarea funcție:


</div>


```python
Axes = makeAxis(num=5, size=1000, name="Axes")
```


<div class="mw-translate-fuzzy">


:   makes an axes series bazat pe numărul dat de axe și de intervalul dintre ele


</div>

Exempluː


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


{{docnav|[Arch CompAxis](Arch_CompAxis.md)|[Axes system](Arch_AxisSystem.md)|[Arch](Arch_Workbench/ro.md)|IconL=Arch_CompAxis.png|IconC=Workbench_Arch.svg |IconR=Arch_AxisSystem.png}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Axis/ro
