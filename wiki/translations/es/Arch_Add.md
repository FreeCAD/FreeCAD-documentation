---
- GuiCommand   */es
   Name   *Arch Add
   Name/es   *Arch Add
   Workbenches   *[Entorno de Arquitectura](Arch_Workbench/es.md)
   MenuLocation   *Arquitectura → Adicción
   SeeAlso   *[Arch Suprimir](Arch_Remove/es.md)
---

# Arch Add/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta de adicción te permite realizar cuatro tipos de operaciones   *

-   Añadir objetos basados en [formas](Part_Workbench/es.md) a un componente de Arquitectura, tal como un [muro](Arch_Wall/es.md) o una [estructura](Arch_Structure/es.md). Estos objetos forman así parte del componente de Arquitectura, y te permiten modificar su forma pero manteniendo sus propiedades base tales como el ancho y alto.
-   Añadir componentes de Arquitectura, como [muros](Arch_Wall/es.md) o [estructuras](Arch_Structure/es.md), a un objeto de arquitectura como los [pisos](Arch_Floor/es.md).
-   Añadir [sistemas de ejes](Arch_Axis/es.md) a [objetos estructurales](Arch_Structure/es.md)
-   Añadir objetos a [planos de sección](Arch_SectionPlane/es.md)


</div>

The counterpart of this tool is the **<img src="images/Arch_Remove.svg" width=16px> [Arch Remove](Arch_Remove.md)** tool.

<img alt="" src=images/Arch_Add_example.jpg  style="width   *640px;">


<div class="mw-translate-fuzzy">

*En la imagen superior, un cubo se añade a un muro.*


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Selecciona el objeto(s) a ser añadido, luego el objeto \"huésped\" (el objeto huésped debe ser el último que selecciones)
2.  Presiona el botón <img alt="" src=images/Arch_Add.png  style="width   *16px;"> 
**Añadir**


</div>


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Añadir se puede utilizar en [macros](macros/es.md) y desde la consola de Python por medio de las siguientes instrucciones   *


</div>


   *   
    
```python
    addComponents(objectsList, host)
    
```
    


<div class="mw-translate-fuzzy">

-   Añade los objetos dados como componentes del objeto huesped dado. Utiliza esto por ejemplo para añadir ventanas a un muro, o muros a un piso.
-   No retorna nada.


</div>

Ejemplo   *


```python
import FreeCAD, Arch, Draft, Part

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Arch.addComponents(Wall2, Wall)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Add/es
