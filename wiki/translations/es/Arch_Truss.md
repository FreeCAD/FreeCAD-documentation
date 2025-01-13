---
 GuiCommand:
   Name: Arch Truss
   Name/es: Arquitectura Armadura
   MenuLocation: Arquitectura , Armadura
   Workbenches: Arch_Workbench/es
   Version: 0.19
---

# Arch Truss/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La herramienta [Arquitectura Armadura](Arch_Truss/es.md) construye un objeto [1](https://es.wikipedia.org/wiki/Armadura_(estructura)), bien a partir de un objeto lineal seleccionado (mientas que una [Línea de Borrador](Draft_Line/es.md) o [Boceto](Sketcher_NewSketch/es.md)), o bien desde cero, si no hay ningún objeto seleccionado al lanzar el comando.


</div>

<img alt="" src=images/Arch_Truss_example.png  style="width:600px;">



## Utilización



### Crear a partir de un objeto seleccionado 

1.  Use a workbench of your choice to create a single line
2.  Select that line
3.  Press the **<img src="images/Arch_Truss.svg" width=16px> [Truss](Arch_Truss.md)** button
4.  Adjust the truss properties to your liking



### Crear desde cero 

1.  Make sure nothing is selected
2.  Press the **<img src="images/Arch_Truss.svg" width=16px> [Truss](Arch_Truss.md)** button
3.  Click in the 3D view to define a first point, or manually enter X, Y and Z coordinates
4.  Click in the 3D view to define a second point, or manually enter X, Y and Z coordinates
5.  Adjust the truss properties to your liking



## Propiedades



### Datos

-    **TrussAngle**: The angle of the truss

-    **SlantType**: The slant type of this truss

-    **Normal**: The normal direction of this truss

-    **HeightStart**: The height of the truss at the start position

-    **HeightEnd**: The height of the truss at the end position

-    **StrutStartOffset**: An optional start offset for the top strut

-    **StrutEndOffset**: An optional end offset for the top strut

-    **StrutHeight**: The height of the main top and bottom elements of the truss

-    **StrutWidth**: The width of the main top and bottom elements of the truss

-    **RodType**: The type of the middle element of the truss

-    **RodDirection**: The direction of the rods

-    **RodSize**: The diameter or side of the rods

-    **RodSections**: The number of rod sections

-    **RodEnd**: If the truss has a rod at its endpoint or not

-    **RodMode**: How to draw the rods



## Archivos de guión 

The Truss tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
Truss = makeFence([baseobj])
```

Ejemplo:


```python
import FreeCAD
import Draft
import Arch

p1 = FreeCAD.Vector(0,0,0)
p2 = FreeCAD.Vector(2000,0,0)
baseline = Draft.makeLine(p1,p2)
truss = Arch.makeTruss(baseline)
truss.HeightStart = 200
truss.HeightEnd = 400
# adjust other needed properties
```


<div class="mw-translate-fuzzy">





</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Truss/es
