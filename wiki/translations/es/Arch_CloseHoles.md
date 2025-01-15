---
 GuiCommand:
   Name: Arch CloseHoles
   Name/es: Tapar agujeros
   MenuLocation: Arquitectura , Utilidades , Tapar agujeros
   Workbenches: Arch_Workbench/es
   SeeAlso: Arch Check/es
---

# Arch CloseHoles/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta identifica agujeros (secuencia circular de aristas abiertas) in un objeto [Forma](Part_Workbench/es.md) y trata de cerrarlo añadiendo una nueva cara a partir de dicha secuencia de aristas. Aunque debes verificar que el resultado es un sólido.


</div>




<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione un objeto [Shape](Part_Workbench.md)
2.  Presione la entrada {{KEY | <img src="images/_Arch_CloseHoles.png_" width= 16px> '''Cerrar agujeros'''}} en Arch -\> Menú Utilidades


</div>




<div class="mw-translate-fuzzy">

## Programación


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Esta herramienta se puede utilizar en [macros](macros/es.md) y desde la consola de Python por medio de las siguientes funciones:


</div>


```python
solid = closeHole(shape)
```


<div class="mw-translate-fuzzy">

cierra un agujero en una forma abierta


</div>

Example: 
```python
import FreeCAD, Draft, Arch

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)

Box = FreeCAD.ActiveDocument.addObject("Part::Box", "Box")
Box.Length = 900
Box.Width = 450
Box.Height = 2000
FreeCAD.ActiveDocument.recompute()

Draft.rotate(Box, 45)
Draft.move(Box, FreeCAD.Vector(1000, 700, 0))

Arch.removeComponents(Box, Wall)
FreeCAD.ActiveDocument.recompute() 

solid = Arch.closeHole(Wall.Shape)
```



---
⏵ [documentation index](../README.md) > Arch CloseHoles/es
