# Arch SplitMesh/cs
---
- GuiCommand:   Name:Arch SplitMesh   Name/cs:Arch Rozděl síť   Workbenches:[MenuLocation:Arch - Utilities - Split Mesh   SeeAlso:[[Arch SelectNonSolidMeshes/cs|Arch SelectNonSolidMeshes](Arch_Workbench/cs___Arch]].md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj rozdělí vybrané [Síťové](Mesh_Workbench.md) objekty do jejich vlastních oddělených komponent.


</div>


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

1.  Vyberte objekt sítě
2.  Stiskněte tlačítko **<img src="images/Arch_SplitMesh.png" width=16px> '''Rozděl síť'''** pro vstup do Architektura -\> Menu Utility


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Nástroj Rozděl síť může být využit v [makrech](macros.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
new_list = splitMesh(obj, mark=True)
```


<div class="mw-translate-fuzzy">

rozdělí vybraný síťový objekt do oddělených komponent.


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
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SplitMesh/cs
