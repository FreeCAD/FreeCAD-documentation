---
 GuiCommand:
   Name: Arch SplitMesh
   Name/es: Arch SplitMesh
   MenuLocation: Arquitectura , Utilidades , Dividir malla
   Workbenches: Arch_Workbench/es
   SeeAlso: Arch SelectNonSolidMeshes/es
---

# Arch SplitMesh/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta divide un objeto [Malla](Mesh_Workbench/es.md) seleccionado en sus componentes separados


</div>




<div class="mw-translate-fuzzy">

## Utilización


</div>


<div class="mw-translate-fuzzy">

1.  Seleccionar un objeto malla
2.  Presionar **<img src="images/Arch_SplitMesh.png" width=16px> '''Dividir malla'''** en el manú Arquitectura -\> Menu de utilidades


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

Esta herramienta se puede utilizar en [macros](macros/es.md) y desde la consola de Python mediante las siguientes funciones:


</div>


```python
new_list = splitMesh(obj, mark=True)
```


<div class="mw-translate-fuzzy">


:   Divide el objeto malla dado en sus componentes separados.


</div>

Example:


```python
import FreeCAD, Draft, Arch, Mesh, MeshPart

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

Shape = Wall.Shape.copy(False)
Shape.Placement = Wall.getGlobalPlacement()

mesh_obj = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh_obj.Mesh = MeshPart.meshFromShape(Shape=Shape, MaxLength=520)
mesh_obj.ViewObject.DisplayMode = "Flat Lines"

new_list = Arch.splitMesh(mesh_obj)
```



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch SplitMesh/es
