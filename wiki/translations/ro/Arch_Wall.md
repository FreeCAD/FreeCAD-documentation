---
- GuiCommand   */ro
   Name   *Arch Wall
   Name/ro   *Arch Wall
   MenuLocation   *Arch → Wall
   Workbenches   *[Arch](Arch_Workbench/ro.md)
   Shortcut   ***W** **A**
   SeeAlso   *[Arch Structure](Arch_Structure/ro.md)
---

# Arch Wall/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument construiește un obiect tip perete de la zero sau deasupra oricărui altul obeict tip [shape](Part_Workbench.md)-based sau [mesh](Mesh_Workbench.md)-based.Un perete poate fi construit fără obiect de bază, caz în care acesta se comportă ca un volum cubic, utilizând proprietăți de lungime, lățime și înălțime. Când este construit pe o formă existentă, un perete se poate baza pe   *


</div>


<div class="mw-translate-fuzzy">

-   A **linear 2D object**, such as lines, wires, arcs or sketches, in which case you can change thickness, alignment(right, left or centered) and height. The length property has no effect.
-   A **flat face**, in which case you can only change the height. Length and width properties have no effect. If the base face is vertical, however, the wall will use the width property instead of height, allowing you to build walls from space-like objects or mass studies.
-   A **solid**, in which case length, width and height properties have no effect. The wall simply uses the underlying solid as its shape.
-   A **mesh**, in which case the underlying mesh must be a closed, manifold solid.


</div>

<img alt="" src=images/Arch_Wall_example.jpg  style="width   *780px;"> 
*Walls built from a line, a wire, a face, a solid, and a sketch*


<div class="mw-translate-fuzzy">

Walls can also have additions or subtractions. Additions are other objects whose shapes are joined in this Wall\'s shape, while subtractions are subtracted. Additions and subtractions can be added with the [Arch Add](Arch_Add.md) and [Arch Remove](Arch_Remove.md) tools. Additions and subtractions have no influence over wall parameters such as height and width, which can still be changed. Walls can also have their height automatic, if they are included into a higher-level object such as [floors](Arch_Floor.md). The height must be kept at 0, then the wall will adopt the height specified in the parent object.


</div>

When several walls should intersect, you need to place them into a [floor](Arch_Floor.md) to have their geometry intersected.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>

### Desenarea unui zid de la zero 


<div class="mw-translate-fuzzy">

1.  Press the **<img src="images/Arch_Wall.png" width=16px> [[Arch Wall]]** button, or press **W** then **A** keys
2.  Click a first point on the 3D view, or type a coordinate
3.  Click a second point on the 3D view, or type a coordinate


</div>

### Desenarea unui zid deasupra unui obiect selectat 


<div class="mw-translate-fuzzy">

1.  Select one or more base geometry objects (Draft object, sketch, etc)
2.  Press the **<img src="images/Arch_Wall.png" width=16px> [[Arch Wall]]** button, or press the **W** then **A** keys
3.  Adjust needed properties such as height or width.


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   Walls share the common properties and behaviours of all [Arch Components](Arch_Component.md)
-   The height, width and alignment of a wall can be set during drawing, via the task panel
-   When snapping a wall to an existing wall, both walls will be joined into one. The way the two walls are joined depends on their properties   * If they have the same width, height and alignment, and if the option \"join base sketches\" is enabled in the Arch preferences, the resulting wall will be one object based on a sketch made of several segments. Otherwise, the latter wall will be added to the first one as addition.
-   Press **X**, **Y** or **Z** after the first point to constrain the second point on the given axis.
-   To enter coordinates manually, simply enter the numbers, then press **ENTER** between each X, Y and Z component.
-   Press **R** or click the checkbox to check/uncheck the **Relative** button. If relative mode is on, the coordinates of the second point are relative to the first one. If not, they are absolute, taken from the (0,0,0) origin point.
-   Press **SHIFT** while drawing to [constrain](Draft_Constrain.md) your second point horizontally or vertically in relation to the first one.
-   Press **ESC** or the **Cancel** button to abort the current command.
-   Double-clicking on the wall in the tree view after it is created allows you to enter edit mode and access and modify its additions and subtractions
-   Multi-layer walls can be easily created by building several walls from the same baseline. By setting their Align property to either left or right, and specifying an Offset value, you can effectively construct several wall layers. Placing a window in such a wall layer will propagate the opening to the other wall layers based on the same baseline.
-   Walls can also make use of [Multi-Materials](Arch_MultiMaterial.md). When using a multi-material, the wall will become multi-layer, using the thicknesses specified by the multi-material. Any layer with a thickness of zero will have its thickness defined automatically by the remaining space defined by the Wall\'s Width value, after subtracting the other layers.
-   Walls can be made to display blocks, instead of one single solid, by turning their **Make Blocks** property on. The size and offset of blocks can be configured with different properties, and the amount of blocks is automatically calculated. <small>(v0.18)</small> 


</div>

## Ancorarea


<div class="mw-translate-fuzzy">

Snapping funcționează un pic diferit cu pereții arcului decât alte obiecte Arch și Draft. Dacă un perete are un obiect de bază, snapping-ul se ancorează la obiectul de bază, în loc de geometria peretelui, permițând ușor alinierea pereților prin linia de bază. Dacă, totuși, doriți să vă apropiați de geometria peretelui, apăsând {{KEY | CTRL}} se va comuta pe obiect de perete.


</div>

<img alt="" src=images/Arch_wall_snap.jpg  style="width   *780px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Arch_wall_snap.jpg  style="width   *780px;">


</div>

## Proprietăți


<div class="mw-translate-fuzzy">

Obiectele de pe perete moștenesc proprietățile obiectelor [ Part](Part_Workbench.md) și au, de asemenea, următoarele proprietăți suplimentare   *

-    {{PropertyData | Align}}   * Alinierea peretelui pe linia de bază   * Stânga, dreapta sau centru

-    {{PropertyData | Base}}   * Obiectul de bază pe care este construit acest perete

-    {{PropertyData | Face}}   * Indicele feței de la obiectul de bază de folosit. Dacă vaue nu este setat sau 0, întregul obiect este utilizat

-    {{PropertyData | Force Wire}}   * Dacă este adevărat, iar peretele se bazează pe o față, se folosește numai firul frontal al feței, rezultând un perete care se învecinează cu fața

-    {{PropertyData | Lungime}}   * lungimea peretelui (nu este utilizată atunci când peretele se bazează pe un obiect)

-    {{PropertyData | Lățime}}   * Lățimea peretelui (nu este utilizată atunci când peretele se bazează pe o față)

-    {{PropertyData | Height}}   * Înălțimea peretelui (nu se utilizează atunci când peretele se bazează pe un solid). Dacă nu este dată nici o înălțime, iar peretele se află în interiorul unui obiect [ floor](Arch_Floor/ro.md) cu înălțimea definită, peretele va lua în mod automat valoarea înălțimii podelei.

-    {{PropertyData | Normal}}   * O direcție de extrudare pentru perete. Dacă este setată la (0,0,0), direcția de extrudare este automată.

-    {{PropertyData | Offset}}   * Aceasta specifică distanța dintre perete și linia de bază. Funcționează numai dacă proprietatea Align (Aliniere) este setată la dreapta sau la stânga.


</div>


<small>(v0.18)</small> 

-    **Make Blocks**   * Enable this to make the wall generate blocks

-    **Block Length**   * The length of each block

-    **Block Height**   * The height of each block

-    **Offset First**   * The horizontal offset of the first line of blocks

-    **Offset Second**   * The horizontal offset of the second line of blocks

-    **Joint**   * The size of the joints between each block

-    **Count Entire**   * The number of entire blocks (read-only)

-    **Count Broken**   * The number of broken blocks (read-only)

## Scripting


<div class="mw-translate-fuzzy">

## Scripturi


</div>


<div class="mw-translate-fuzzy">

Instrumentul Wall tool poate fi utilizat în [macros](macros.md) și de la consola python utilizând următoarele funcții   *


</div>


```python
Wall = makeWall(baseobj=None, length=None, width=None, height=None, align="Center", face=None, name="Wall")
```


<div class="mw-translate-fuzzy">

-   Creates a wall based on the given object, which can be a sketch, a draft object, a face or a solid. align can be \"Center\",\"Left\" or \"Right\". If you provide no base object, then you can use numeric values for length, width and height. Face can be used to give the index of a face from the underlying object, to build this wall on, instead of using the whole object.
-   Returns the created wall, or None if the operation failed.


</div>

Exempluː


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
Draft.move(Wall2, FreeCAD.Vector(0, -1000, 0))
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>


 

[Category   *Arch/ro](Category   *Arch/ro.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Wall/ro
