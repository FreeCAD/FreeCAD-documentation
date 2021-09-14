---
- GuiCommand:/fr
   Name:Arch Fence
   Name/fr:Arch Clôture
   MenuLocation:Arch → Barrière
   Workbenches:[Arch](Arch_Workbench/fr.md)
   Version:0.19
---

## Description

L\'outil [Arch Clôture](Arch_Fence/fr.md) est un objet qui construit une clôture en répétant un poteau et une section de clôture le long d\'un chemin donné.

<img alt="" src=images/Arch_Fence_description_example.png  style="width:600px;">

## Utilisation

### Création à partir de zéro 

1.  Utilisez un atelier de votre choix pour créer un seul poteau de clôture et une seule section.
2.  Créez le chemin que la clôture doit suivre à l\'aide de l\'[atelier Sketcher](Sketcher_Workbench/fr.md) ou de l\'[atelier Draft](Draft_Workbench/fr.md).
3.  Revenez à l\'[atelier Arch](Arch_Workbench/fr.md).
4.  Sélectionnez la section, la publication et le chemin dans exactement cet ordre.
5.  Appuyez sur le bouton **<img src="images/Arch_Fence.svg" width=16px>[Créer un objet clôture...](Arch_Fence/fr.md)**.

## Options

Pour l\'instant, l\'outil suppose ce qui suit

1.  Le chemin est dessiné sur le plan XY
2.  La section et le poteau sont dessinés à l\'origine de manière à rester debout dans la vue de face

## Propriétés

### Données

-    {{PropertyData/fr|Path}}: chemin d\'accès que doit suivre la clôture

-    {{PropertyData/fr|Post}}: Un post de clôture unique à répéter

-    {{PropertyData/fr|Section}}: Une seule section à répéter

-    {{PropertyData/fr|Number Of Posts}}: nombre total de messages utilisés pour construire la clôture. Ceci est calculé automatiquement.

-    {{PropertyData/fr|Number Of Sections}}: nombre total de sections utilisées pour construire la clôture. Ceci est calculé automatiquement.

### Vue

-    {{PropertyView/fr|Use Original Colors}}: Lorsque l\'option est définie sur `True`, la clôture utilisera les couleurs de la section d\'origine. Sinon, la définition de ShapeColor de la clôture sera utilisée pour coloriser la clôture.

## Remarques

-   Arch Fence a été introduit dans FC v0.19 par l\'utilisateur furti.
-   [Sujet du forum](https://forum.freecadweb.org/viewtopic.php?t=36149) discutant de la fonctionnalité Arch Fence.

## Script

L\'outil Clôture peut être utilisé dans une [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante:


```python
Fence = buildFence(section, post, path)
```

Exemple :


```python
import FreeCAD
import Part
import Arch

parts = []

parts.append(Part.makeBox(2000, 50, 30, FreeCAD.Vector(0, 0, 1000 - 30)))
parts.append(Part.makeBox(2000, 50, 30))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(0, 15, 30)))
parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector(1980, 15, 30)))

for i in range(8):
    parts.append(Part.makeBox(20, 20, 1000 - 60, FreeCAD.Vector((2000 / 9 * (i + 1)) - 10, 15, 30)))

Part.show(Part.makeCompound(parts), "Fence_section")
fence_section = FreeCAD.ActiveDocument.Fence_section

sketch = FreeCAD.ActiveDocument.addObject("Sketcher::SketchObject", "Path")
sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(20000, 0, 0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(20000, 0, 0), FreeCAD.Vector(20000, 20000, 0)), False)

post = Part.makeBox(100, 100, 1000, FreeCAD.Vector(0, 0, 0))
Part.show(post, "Post")
post = FreeCAD.ActiveDocument.Post

Fence = Arch.buildFence(fence_section, post, sketch)
```





 
