---
- GuiCommand:/es
   Name:Arch Remove
   Name/es:Sustraer
   MenuLocation:Arquitectura → Sustraer
   Workbenches:[Entorno de Arquitectura](Arch_Workbench/es.md)
   SeeAlso:[Añadir](Arch_Add/es.md)
---

# Arch Remove/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Sustraer te permite hacer dos tipos de operaciones:

-   Eliminar un subcomponente de un objeto de Arquitectura, por ejemplo eliminar un cubo que se ha añadido a un muro, como en el ejemplo de [Añadir](Arch_Add/es.md)
-   Restar un objeto basado en [formas](Part_Workbench/es.md) de un objeto de Arquitectura como un [muro](Arch_Wall/es.md) o [estructura](Arch_Structure/es.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Add.svg" width=16px> [Arch Add](Arch_Add.md)** tool.

<img alt="" src=images/Arch_Remove_example.jpg  style="width:600px;">


<div class="mw-translate-fuzzy">

*En la imagen superior, un cubo es sustraído de un muro*


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Selecciona un subcomponente de un objeto de Arquitectura, **o**:
2.  Selecciona objeto(s) a ser sustraídos, y luego el componente de Arquitectura del cual se desean sustraer (el componente de Arquitectura debe ser el último que selecciones)
3.  Presiona el botón <img alt="" src=images/Arch_Remove.png  style="width:16px;"> 
**Sustraer**


</div>

Or

1.  Select objects to be subtracted, the last object selected must the Arch object from which the other objects will be subtracted.
2.  Press the **<img src="images/Arch_Remove.svg" width=16px>** button, or **Arch** → **<img src="images/Arch_Remove.svg" width=16px> [Remove](Arch_Remove.md)** from the top menu.


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramientas Eliminar se puede utilizar en [macros](macros/es.md) y desde la consola de Python mediante la utilización de las siguientes funciones:


</div>


```python
removeComponents(objectsList, host=None)
```


<div class="mw-translate-fuzzy">

Elimina los componentes dados de sus padres. Si se especifica un objeto huésped, esta función tratará de añadir los componente como agujeros.


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
```


<div class="mw-translate-fuzzy">


{{docnav/es|[Add component](Arch_Add.md)|[Survey](Arch_Survey.md)|[Arch](Arch_Workbench.md)|IconL=Arch_Add.svg |IconC=Workbench_Arch.svg |IconR=Arch_Survey.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Remove/es
