---
- GuiCommand:/cs
   Name:Arch RemoveShape   Name/cs:Arch RemoveShape
   Workbenches:[Arch](Arch_Workbench/cs.md)
   MenuLocation:Arch → Utilities → Remove Shape
   SeeAlso:[Arch MeshToShape](Arch_MeshToShape/cs.md)
---

# Arch RemoveShape/cs


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj se pokouší odebrat trojrozměrný tvar ze [zdi](Arch_Wall.md) nebo [stavební struktury](Arch_Structure.md) a nastavit její vlastnosti, tak že ji udělá plně parametrickou. Tento nástroj funguje pouze tehdy když základní tvar je trojrozměrný (přesně 6 ploch, všechny úhly jsou pravé).


</div>

## Použití


<div class="mw-translate-fuzzy">

1.  Vyberte [zeď](Arch_Wall.md) nebo [strukturu](Arch_Structure.md)
2.  Stiskem tlačítka **<img src="images/Arch_RemoveShape.png" width=16px> '''Odebrat tvar'''** přejdete od Architektura -\> Menu Utility


</div>


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Tento nástroj může být použit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
removeShape(objs, mark=True)
```


<div class="mw-translate-fuzzy">

vezme stavební objekt (zeď nebo struktura) založený na trojrozměrném tvaru a odebere z něj vnitřní tvar o délce, šířce a výšce daný parametry.


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


{{docnav/cs|[Select non-solid meshes](Arch_SelectNonSolidMeshes.md)|[Close Holes](Arch_CloseHoles.md)|[Arch](Arch_Workbench.md)|IconL=Arch_SelectNonSolidMeshes.png |IconC=Workbench_Arch.svg |IconR=Arch_CloseHoles.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/cs
