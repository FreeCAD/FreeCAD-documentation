---
 GuiCommand:
   Name: Arch Fence
   Name/fr: Arch Clôture
   MenuLocation: 3D/BIM , Clôture
   Workbenches: BIM_Workbench/fr
   Version: 0.19
---

# Arch Fence/fr

## Description

L\'outil **Arch Clôture** est un objet qui construit une clôture en répétant un poteau et une section de clôture le long d\'un tracé donné.

<img alt="" src=images/Arch_Fence_description_example.png  style="width:600px;">



## Utilisation



### Création à partir de zéro 

1.  Utilisez un atelier de votre choix pour créer un seul poteau de clôture et une seule section.
2.  Créez le tracé que la clôture doit suivre à l\'aide de l\'[atelier Sketcher](Sketcher_Workbench/fr.md) ou de l\'[atelier Draft](Draft_Workbench/fr.md).
3.  Revenez à l\'[atelier BIM](BIM_Workbench/fr.md).
4.  Sélectionnez la section, la publication et le tracé dans exactement cet ordre.
5.  Appuyez sur le bouton **<img src="images/Arch_Fence.svg" width=16px>[Clôture](Arch_Fence/fr.md)**.

## Options

Pour l\'instant, l\'outil part du principe que

1.  Le tracé est dessiné sur le plan XY
2.  La section et le poteau sont dessinés à l\'origine de manière à rester debout dans la vue de face



## Propriétés



### Données

-    **Path**: tracé que doit suivre la clôture

-    **Post**: un seul poteau de clôture à répéter

-    **Section**: une seule section à répéter

-    **Number Of Posts**: nombre total de poteaux utilisés pour construire la clôture. Calculé automatiquement.

-    **Number Of Sections**: nombre total de sections utilisées pour construire la clôture. Calculé automatiquement.



### Vue

-    **Use Original Colors**: lorsque l\'option est définie à `True`, la clôture utilisera les couleurs de la section d\'origine et du piquet. Sinon, la définition de ShapeColor de la clôture sera utilisée pour coloriser la clôture.



## Remarques

-   Arch Clôture a été introduit dans FC v0.19 par l\'utilisateur furti.
-   [Sujet du forum](https://forum.freecadweb.org/viewtopic.php?t=36149) discutant de la fonctionnalité Arch Clôture.



## Script

L\'outil Clôture peut être utilisé dans une [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de la fonction suivante :


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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Fence/fr
