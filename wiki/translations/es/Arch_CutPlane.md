---
- GuiCommand:/es
   Name:Arch CutPlane
   Name/es:Arch CutPlane
   MenuLocation:Arch → Cut Plane
   Workbenches:[Arch](Arch_Workbench/es.md)
   SeeAlso:[Arch Remove](Arch_Remove/es.md)
---

# Arch CutPlane/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

La herramienta Plano de corte le permite cortar un objeto Arch de acuerdo a un plano:

-   Puede cortar un objeto Arch con la cara seleccionada, normal u opuesta al plano frontal.
-   Esto agrega un componente de sustracción CutVolume al objeto Arch


</div>

<img alt="" src=images/Arch_CutPlane_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">

*En la imagen de arriba, dos Arch estructuras se cortan con el plano respectivo.*


</div>


<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Seleccione el objeto que se va a cortar, luego la cara (la cara debe ser la última que seleccionó, y debe seleccionarse en la vista 3D)
2.  Presione el botón {{KEY | <img src="images/_Arch_CutPlane.svg_" width= 16px> '''Plano de corte'''}}
3.  Elija si el objeto está cortado **detrás** de la cara normal o **frente** de la cara normal
4.  Haz clic en el botón Aceptar


</div>


<div class="mw-translate-fuzzy">

## Programación


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

La herramienta Plano de Corte se puede usar en [macros](macros/es.md) y desde la consola de Python mediante la siguiente función:


</div>


```python
cutObj = cutComponentwithPlane(archObject, cutPlane, sideFace)
```


<div class="mw-translate-fuzzy">

-   archObject es el objeto a cortar
-   la cara es la cara de un objeto del que proviene el plano
-   faceSide es el lado de la cara para cortar. 0 = Detrás, 1 = Delantero


</div>

Example: 
```python
import FreeCAD, FreeCADGui, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 2000, 0)

Line = Draft.makeWire([p1, p2])
Wall = Arch.makeWall(Line, width=150, height=2000)

p3 = FreeCAD.Vector(0, 2000, 0)
p4 = FreeCAD.Vector(3000, 0, 0)

Line2 = Draft.makeWire([p3, p4])
Wall2 = Arch.makeWall(Line2, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

# Select the Wall
main_object = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall2
selection = FreeCADGui.Selection.getSelectionEx()[0]
cut_face = selection.SubObjects[0]

cutObj = Arch.cutComponentwithPlane(main_object, cut_face, 0)
FreeCAD.ActiveDocument.recompute()

Wall3 = Draft.move(Wall, FreeCAD.Vector(-4000, 0, 0), copy=True)
Wall4 = Draft.move(Wall2, FreeCAD.Vector(-4000, 0, 0), copy=True)
FreeCAD.ActiveDocument.recompute()

# Select the Wall3
main_object2 = FreeCADGui.Selection.getSelectionEx()[0]

# Select the face of Wall4
selection2 = FreeCADGui.Selection.getSelectionEx()[0]
cut_face2 = selection2.SubObjects[0]

cutObj2 = Arch.cutComponentwithPlane(main_object2, cut_face2, 1)
FreeCAD.ActiveDocument.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CutPlane/es
