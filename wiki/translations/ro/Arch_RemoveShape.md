---
- GuiCommand:/ro
   Name:Arch RemoveShape   Name/ro:Arch RemoveShape
   Workbenches:[Arch](Arch_Workbench/ro.md)
   MenuLocation:Arch → Utilities → Remove Shape
   SeeAlso:[Arch MeshToShape](Arch_MeshToShape.md)
---

# Arch RemoveShape/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument încearcă să înlăture forma cubică interioară a unui [Arc Wall](Arc_Wall.md) sau [Arch Structure](Arch_Structure.md) și să-și ajusteze proprietățile, făcând-o complet parametrică. Acest instrument va funcționa numai dacă forma subiacentă este cubică (exact 6 fețe, toate colțurile au doar unghiuri drepte).


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați un [Arch Wall](Arch_Wall.md) sau o [Arch Structure](Arch_Structure.md)
2.  Apăsați tasta **<img src="images/Arch_RemoveShape.png" width=16px> '''Remove Shape'''** din meniul Arch -\> Utilities menu


</div>


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Acest instrument poate fi utilizat în [macros](macros.md) și din consola Python utilizând următoarea funcție:


</div>


```python
removeShape(objs, mark=True)
```


<div class="mw-translate-fuzzy">

ia un obiect arc (perete sau o structură) construit pe o formă cubică și îndepărtează forma interioară, păstrând lungimea, lățimea și înălțimea ca parametri.


</div>


```python
import FreeCAD, Draft, Arch

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(Box)
FreeCAD.ActiveDocument.recompute()

Arch.removeShape(Structure)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/ro|[Select non-solid meshes](Arch_SelectNonSolidMeshes.md)|[Close Holes](Arch_CloseHoles.md)|[Arch](Arch_Workbench.md)|IconL=Arch_SelectNonSolidMeshes.png |IconC=Workbench_Arch.svg |IconR=Arch_CloseHoles.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/ro
