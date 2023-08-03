---
 GuiCommand:
   Name: Arch AxisSystem
   Name/ro: Arch AxisSystem
   MenuLocation: Arch , Axis System
   Workbenches: Arch_Workbench/ro
   SeeAlso: Arch Axis/ro, Arch Grid/ro
---

# Arch AxisSystem/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul Axis System vă permite să combinați 2 sau 3 obiecte [Arch Axis](Arch_Axis.md). Funcția principală a acestui instrument este de a calcula punctele de intersecție dintre diferitele axe incluse în acest sistem. Obiectele atelierului Arch pot folosi acest sistem pentru a duplica/multiplica forma lor la diferite punctele de intersecție.


</div>

This is useful to define the intersection points between the different axes. Arch objects can then use this system to duplicate their shape on the different intersection points.

<img alt="" src=images/Arch_AxisSystem_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*Imaginea de mai jos arată trei obiecte [Arch Axis](Arch_Axis.md) combinate într-un Axis System. Un obiect coloană utilizează acest sistem ca pe propria **Axis** , pentru a avea propria formă duplicată la fiecare punct de intersecție.*


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Opțional, selectați opbeictele [Arch Axis](Arch_Axis.md) pe are doriți să le introduceți în acest sistem
2.  Apăsați butonul **<img src="images/Arch_AxisSystem.png" width=16px> [[Arch AxisSystem]]
**
3.  Faceți clic drapta pe noul obiect axes system creat în arborele de vederă și add/edit obeictele [Arch Axis](Arch_Axis.md) incluse în sistem
4.  Selectați orice [Arch Axis](Arch_Axis.md) și apăsați butonul Add sau or Delete pentru a-l adăuga sau a-l șterge to/from acest sistem
5.  Definiți proprietățile **Axis** pentru orice obiect Arch pentru a-l point pe acest sistem, pentru a avea forma duplicată la punctul de intersecție al sistemului acesta


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   Același obiect [Arch Axis](Arch_Axis.md) poate face parte din mai multe siteme
-   Orice obiect shape-based poate fi utilizat ca proprietate**Axis** a obiectelor Arch. În acest caz, obiectul formă va fi duplicat de-a lungul vortexurilor obiectului Axă


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


</div>


<div class="mw-translate-fuzzy">

Instrumentul Axis System poate fi utilizat în [macros](macros.md) și de la consola python utilizând umătoarea funcție:


</div>


```python
AxisSystem = makeAxisSystem(axes, name="Axis System")
```


<div class="mw-translate-fuzzy">

Face un Axis System bazat pe lista dată de [Arch Axis](Arch_Axis.md)


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

AxisSystem = Arch.makeAxisSystem([Axes, Axes2])

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = AxisSystem
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav|[Axis](Arch_Axis.md)|[Grid](Arch_Grid.md)|[Arch](Arch_Workbench/ro.md)|IconL=Arch_Axis.svg |IconC=Workbench_Arch.svg |IconR=Arch_Grid.svg}}


</div>



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch AxisSystem/ro
