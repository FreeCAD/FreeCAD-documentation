---
- GuiCommand:/es
   Name:Arch Check
   Name/es:Arch Check
   MenuLocation:Arquitectura → Utilidades → Comprobar
   Workbenches:[Arquitectura](Arch_Workbench/es.md)
   SeeAlso:[Tapar agujeros](Arch_CloseHoles/es.md)
---

# Arch Check/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta comprueba el documento actual o los objetos no sólidos seleccionados de [Piezas](Part_Workbench/es.md) o objetos de [Arquitectura](Arch_Workbench/es.md), que puedan dar problemas, ya que la mayoría de las operaciones del entorno de arquitectura requieren objetos sólidos.


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Presiona **<img src="images/Arch_Check.png" width=16px> '''Comprobar'''** en el menú Arquitectura → Utilities menu


</div>


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

Esta herramienta se puede utilizar en [macros](macros/es.md) y desde la consola de Python por medio de las siguientes funciones:


</div>


```python
list_bad = check(objectslist, includehidden=False)
```


<div class="mw-translate-fuzzy">


:   comprueba si los objetos dados contienen sólo sólidos


</div>

Example:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Wall2 = Arch.makeWall(None, length=2000, width=200, height=1000)
FreeCAD.ActiveDocument.recompute()

Circle = Draft.makeCircle(450)
Wire = Draft.makeWire([FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(1500, 1000, 0), FreeCAD.Vector(2500, -1000, 0)])

list_bad = Arch.check([Wall1, Wall2, Circle, Wire], includehidden=True)
print(list_bad)
```

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Check/es
