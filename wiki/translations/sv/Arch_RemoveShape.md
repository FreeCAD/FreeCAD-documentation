---
- GuiCommand:/sv
   Name:Arch RemoveShape
   Name/sv:Arch RemoveShape
   Workbenches:[Arch](Arch_Workbench/sv.md)
   MenuLocation:Arch → Utilities → Remove Shape
   SeeAlso:[MeshToShape](Arch_SplitMesh]],_[[Arch_MeshToShape/sv.md)
---

# Arch RemoveShape/sv


</div>

## Beskrivning

This tool attempts at removing the inner cubic shape of an **<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall.md)** or **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)**, and adjusting its properties, making it totally parametric. This tool will only work if the underlying shape is cubic (exactly 6 faces, all corners have only right angles).

## Bruk

1.  Select an **<img src="images/Arch_Wall.svg" width=16px> [Arch Wall](Arch_Wall.md)
** or **<img src="images/Arch_Structure.svg" width=16px> [Arch Structure](Arch_Structure.md)**
2.  Press the **<img src="images/Arch_RemoveShape.svg" width=16px>** button or use **Arch** → **Utilities** → **<img src="images/Arch_RemoveShape.svg" width=16px> [Remove Shape](Arch_RemoveShape.md)** from the top menu.

## Scripting


<div class="mw-translate-fuzzy">

## Skript


</div>

This tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function: 
```python
removeShape(objs, mark=True)
```

-   Takes a list of Arch objects (`objs`) built on a cubic shape, and removes the inner shape, keeping the length, width and height as properties of the Arch object.
    -   
        `objs`
        
        is a single object, [Arch Wall](Arch_Wall.md) or [Arch Structure](Arch_Structure.md), or a list of them.
-   If `mark` is `True`, objects that cannot be processed by this function will become red.


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


{{docnav/sv|[Select non-solid meshes](Arch_SelectNonSolidMeshes.md)|[Close Holes](Arch_CloseHoles.md)|[Arch](Arch_Workbench.md)|IconL=Arch_SelectNonSolidMeshes.png |IconC=Workbench_Arch.svg |IconR=Arch_CloseHoles.svg}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/sv
