---
- GuiCommand:/ro
   Name:Arch Stairs
   Name/ro:Arch Stairs
   MenuLocation:Arch → Stairs
   Workbenches:[Arch](Arch_Workbench/ro.md)
   Shortcut:**S** **R**
   SeeAlso:[[Arch Structure/ro]], [[Arch Equipment/ro]]
   Version:0.14
---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Instrumentul Scara vă permite să construiți automat mai multe tipuri de scări. În prezent, sunt suportate doar scările drepte (cu sau fără odihnă centrală). Scările pot fi construite de la zero sau dintr-o linie [linie](Draft_Line.md), caz în care scările urmează linia. Dacă linia nu este orizontală, dar are o înclinație verticală, scările vor urma și ele această pantă.


</div>

A se vedea [Stairs entry in wikipedia](http://en.wikipedia.org/wiki/Stairs) pentru o definiție a diferitor termeni utilizați pentru a descrie piese/părți ale scărilor. (pentru liMba română avem <https://www.spatiulconstruit.ro/ghid-de-constructii/scari-notiuni-generale-clasificari/9> )

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*În imaginea de mai suse, două scări au fost create, una cu o structură masivă și o odihnă, alta cu un singur vang central.*


</div>

## Opţiuni

-   Scările partajează proprietățile și comportamentele comune tuturor [Arch Components](Arch_Component.md)


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Apăsați butonul **<img src="images/Arch_Stairs.png" width=16px> [[Arch Stairs]]
** button, sau apăsați testele **S**, **R**
2.  Adjust the desired properties. Some parts of the stairs, such as the structure, might not appear immediately, if any of the properties makes it impossible, such as a structure thickness of 0.


</div>

## Proprietăți

Base

-    **Align**: Alinerea acestor scări cu linia de bază, dacă se poate aplica.

-    **Base**: The baseline of these stairs, if any.

-    **Height**: The total height of these stairs, if not based on a baseline, or the baseline is horizontal.

-    **Length**: The total length of these stairs if no baseline is defined.

-    **Width**: Lățimea acestor scări.

Steps

-    **Nosing**: Mărimea proeminenței treptei (nasul).

-    **Number of Steps**: Numărul de trepte a scării.

-    **Riser Height**: Înălțimea contratreptei.

-    **Tread Depth**: Adâncimea treptei.

-    **Tread Thickness**: Grosimea treptelor.

Structure

-    **Landings**: Tipul odihnelor/palierelor.

-    **Stringer Offset**: The offset between the border of the stairs and the structure.

-    **Stringer Width**: Lățimea vangurilor/lonjeroanelor.

-    **Structure**: Tipul și structura acestor scări.

-    **Structure Thickness**: Grosimea structurii.

-    **Winders**: Tipul treptelor de schimbare a direcției (mai înguste pe o latură).


<div class="mw-translate-fuzzy">

## Limitări

-   Instrumetnul este disponibil de la versiunea FreeCAD 0.14 sau una mai recentă
-   Momentan sunt disponibile doar scări drepte
-   Consultați intrarea forumului [forum entry](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) pentru scări circulare.
-   A se vedea [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564)..


</div>


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Stairs pot fi creat din scripturi Python și [macros](macros.md) utilizând urmăotarea funcție:


</div>


```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```


<div class="mw-translate-fuzzy">

-   Creează obiecte tip cu atributele specificate.
-   Returnează scările ca pe un obiect nou.


</div>

Exempluː 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```


<div class="mw-translate-fuzzy">


{{docnav/ro|[Space/ro](Arch_Space/ro.md)|[Arch CompPanel/ro](Arch_CompPanel/ro.md)|[Arch](Arch_Module/ro.md)|IconL=Arch_Space.svg |IconC=Workbench_Arch.svg |IconR=Arch_CompPanel.png}}


</div>


 
