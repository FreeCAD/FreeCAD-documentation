---
- GuiCommand:/es
   Name:Arch Floor
   Name/es:Arch Floor
   Workbenches:[Entorno de Arquitectura](Arch_Workbench/es.md)
   MenuLocation:Arquitectura → Piso
   Shortcut:**F** **L**
   SeeAlso:[ Arch Celda](Arch_Cell/es.md)
---

# Arch Floor/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

El Piso de Arquitectura es un tipo especial de [Celda](Arch_Cell/es.md) que tiene un par de propiedades adicionales particularmente ajustadas para la construcción de pisos. En particular, tienen una propiedad de altura, que sus objetos descendientes ([muros](Arch_Wall/es.md) y [estructuras](Arch_Structure/es.md)) pueden utilizar para ajustar su altura automáticamente


</div>

As of <small>(v0.18)</small>  the Arch Floor is derived entirely from the [Arch BuildingPart](Arch_BuildingPart.md) object, which is a general container to organize a building model not limited to floors or storeys. Older Floor objects can be converted to the new type by right clicking on them and choosing `Convert to BuildingPart`.

## Como utilizar 


<div class="mw-translate-fuzzy">

1.  Opcionalmente, seleccione uno o más objetos para incluir en su nuevo piso
2.  Presione el botón **<img src="images/Arch_Floor.png" width=16px> '''Arch Floor'''
** o presione las teclas **F** y **L**


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Después de la creación de un piso, puedes añadirle más objetos arrastrando y soltándolos en la vista en árbol o utilizando la herramienta <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Añadir](Arch_Add/es.md)
-   Puedes eliminar objetos de un piso arrastrando y soltándolos fuera en la vista de árbol o utilizando la herramienta <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Remover](Arch_Remove/es.md)


</div>

## Propiedades

An Arch Floor object shares all properties from an [Arch BuildingPart](Arch_BuildingPart.md), with the **Ifc Type** set to `"Building Storey"`.


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramientas piso se puede utilizar en [macros](macros/es.md) y desde la consola de Python utilizando las siguiente funcion:


</div>


```python
Floor = makeFloor(objectslist=None, baseobj=None, name="Floor")
```


<div class="mw-translate-fuzzy">


:   Crea un piso incluyendo los objetos de la lista dada.


</div>

Ejemplo:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

Floor = Arch.makeFloor([Wall1, Wall2])

Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute() 
```


<div class="mw-translate-fuzzy">


{{docnav/es|[Rebar](Arch_Rebar.md)|[Building Part](Arch_BuildingPart.md)|[Arch](Arch_Workbench/es.md)|IconL=Arch_Rebar.svg |IconC=Workbench_Arch.svg |IconR=Arch_BuildingPart.svg}}


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Floor/es
