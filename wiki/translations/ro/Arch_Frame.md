---
- GuiCommand   */ro
   Name   *Arch Frame
   MenuLocation   *Arch → Frame
   Workbenches   *[Arch](Arch_Workbench.md)
   Shortcut   ***F** **R**
   SeeAlso   *[[Arch Wall]], [[Arch Structure]]
---

# Arch Frame/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Instrumentul de cadru/dulgherie este utilizat pentru a construi toate tipurile de obiecte de tâmplărie pe baza unui profil și a unei căi. Profilul este extrudat de-a lungul liniilor căii care poate consta din orice obiect 2D, de exemplu dintr-un [sketch](Sketcher_Workbench/it.md) sau dintr-un [draft object](Draft_Workbench.md). Este deosebit de util pentru crearea de balustrade sau ziduri de tamplarie. Obiectele de dulgherie pot fi transformate cu ușurință în obiecte [wall](Arch_Wall.md) sau

[structure](Arch_Structure.md) ..


</div>

<img alt="" src=images/Arch_Frame_example.jpg  style="width   *640px;">


<div class="mw-translate-fuzzy">

*În imaginea de mai sus, un [line](Draft_Line.md) a fost transformat într-un [array](Draft_Array.md) și un obiect cadru a fost făcut utilizând matricele ca aspect și un [circleca](Draft_Circle.md) profil.*


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Creați un aspect al unui obiect și profilul unui un obiect, de exemplu cu [Draft Workbench](Draft_Workbench.md) sau [Sketcher Workbench](Sketcher_Workbench.md)
2.  Selectați primul obiect în aspect, apoi țineți apăsată tasta {{KEY | CTRL}} și selectați obiectul care urmează a fi profilat
3.  Apăsați butonul **<img src="images/Arch_Frame.png" width=16px> [[Arch Frame]]
**, sau apăsați tastele în ordine **F** apoi **R**


</div>

## Opţiuni


<div class="mw-translate-fuzzy">

-   Articolele de tâmplărie/Frames partajează proprietățile și comportamentele comune ale tuturor componentelor [ Arc Components](Arch_Component.md)
-   Prin setarea proprietății Offset, obiectul de dulgherie poate fi poziționat la distanța dorită de obiectul urmărit.
-   Profilul va fi copiat la baza fiecărei margini a obiectului de aspect, apoi extrudat de-a lungul acestuia. Puteți controla modul în care profilul este plasat la baza fiecărei margini cu proprietățile Align and Rotation.


</div>

## Proprietăți

-    **Base**   * The layout this frame is based on.

-    **Profile**   * The profile this frame is based on.

-    **Align**   * Specifies if the profile must be rotated to have its normal axis aligned with each edge.

-    **Offset**   * An optional distance between the layout object and the frame object.

-    **Rotation**   * The rotation of the profile around its extrusion axis.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Frame poate fi utilizat în [macros](macros.md) și de la consola python utilizând următoarele funcții   *


</div>


```python
Frame = makeFrame(baseobj, profile)
```


<div class="mw-translate-fuzzy">

-   Creează un obiect cadru dintr-o schiță de bază (sau orice alt obiect care conține fire) și un obiect profil (un obiect extrudabil 2D care conține fețe sau fire închise)
-   Returnează noul obiect cadru sau Niciunul dacă operația a eșuat.


</div>

Exempluː 
```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/ro|[Nest](Arch_Nest.md)|[Fence](Arch_Fence.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Nest.svg |IconC=Workbench_Arch.svg |IconR=Arch_Fence.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Frame/ro
