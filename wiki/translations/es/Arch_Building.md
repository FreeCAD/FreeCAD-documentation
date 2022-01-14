---
- GuiCommand:/es
   Name:Arch Building
   Name/es:Arch Building
   MenuLocation:Arch → Building
   Workbenches:[Entorno de Arquitectura](Arch_Workbench/es.md)
   Shortcut:**B** **U**
   SeeAlso:[Piso](Arch_Floor/es.md), [Ubicación](Arch_Site/es.md)
---

# Arch Building/es


</div>

## Descripción

Las Construcciones son un tipo especial de objeto grupo de FreeCAD particularmente ajustadas para la representación de una unidad de construcción completa. Se utilizan principalmente para organizar el modelo, conteniendo objetos [piso](Arch_Floor/es.md).


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Opcionalmente, selecciona uno o más objetos para incluirlos en tu nueva consdtrucción
2.  Presiona el botón **<img src="images/Arch_Building.png" width=16px> '''Construcción'''
**, o presiona las teclas **B** y **U**


</div>

## Opciones


<div class="mw-translate-fuzzy">

-   Después de la creación de uina construcción, puedes añadirle más objetos arrastrando y soltándolos en la vista en árbol o utilizando la herramienta <img alt="" src=images/Arch_Add.png  style="width:16px;"> [Añadir](Arch_Add/es.md)
-   Puedes eliminar objetos de una construcción arrastrando y soltándolos fuera desde la vista de árbol o utilizando la herramienta <img alt="" src=images/Arch_Remove.png  style="width:16px;"> [Eliminar](Arch_Remove/es.md)


</div>

## Properties

-    **Building Type**: The type of this building, to choose from a list


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

La herramienta Construcción se puede utilizar en [macros](macros/es.md) y desde la consola de Python por medio de las siguientes instrucciones:


</div>


```python
Building = makeBuilding(objectslist=None, baseobj=None, name="Building")
```


<div class="mw-translate-fuzzy">


:   crea una construcción incluyendo los objetos de la lista dada.


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

Building = Arch.makeBuilding([Wall1, Wall2])

Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


</div>


 

[<img src="images/Property.png" style="width:16px"> Arch/es](<img src="images/Property.png" style="width:16px"> Arch/es.md)

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Building/es
