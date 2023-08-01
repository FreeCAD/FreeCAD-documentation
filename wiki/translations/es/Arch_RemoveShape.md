---
- GuiCommand:
   Name:Arch RemoveShape
   Name/es:Arch RemoveShape
   MenuLocation:Arch → Utilities → Remove Shape
   Workbenches:[Arch](Arch_Workbench/es.md)
   SeeAlso:[Arch MeshToShape](Arch_MeshToShape/es.md)
---

# Arch RemoveShape/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta intenta eliminar la forma cúbica interna de una [Arch Wall](Arch_Wall/es.md) o [Arch Structure](Arch_Structure/es.md) y ajustar sus propiedades, por lo que es totalmente paramétrica. Esta herramienta solo funcionará si la forma subyacente es cúbica (exactamente 6 caras, todas las esquinas tienen solo ángulos rectos).


</div>

## Utilización


<div class="mw-translate-fuzzy">

1.  Seleccione un [Arch Wall](Arch_Wall/es.md) o [Arch Structure](Arch_Structure/es.md)
2.  Presione la opción **<img src="images/Arch_RemoveShape.png" width=16px> '''Remove Shape'''** en Arch -\> Menu de Utilidades


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

Esta herramienta se puede utilizar en [macros](macros/es.md) y desde la consola de Python por medio de las siguientes funciones:


</div>


```python
removeShape(objs, mark=True)
```


<div class="mw-translate-fuzzy">

toma un objeto Arch (pared o estructura) construido en una forma cúbica, y elimina la forma interna, manteniendo su longitud, ancho y alto como parámetros.


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


{{docnav/es|[Select non-solid meshes](Arch_SelectNonSolidMeshes.md)|[Close Holes](Arch_CloseHoles.md)|[Arch](Arch_Workbench.md)|IconL=Arch_SelectNonSolidMeshes.png |IconC=Workbench_Arch.svg |IconR=Arch_CloseHoles.svg}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch RemoveShape/es
