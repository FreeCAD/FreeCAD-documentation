---
- GuiCommand:/fr
   Name:Part ShapeFromMesh
   Name/fr:Part Forme à partir du maillage
   MenuLocation:Pièce → Créer la forme à partir d'un maillage...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Convertir en solide](Part_MakeSolid/fr.md), [Part Affiner la forme](Part_RefineShape/fr.md), [Part Points à partir de maillage](Part_PointsFromMesh/fr.md)
---

# Part ShapeFromMesh/fr

## Introduction

Cette commande **<img src="images/Part_ShapeFromMesh.svg" width=16px> [Part Forme à partir du maillage](Part_ShapeFromMesh/fr.md)** crée une forme à partir d\'un [Maillage](Mesh/fr.md). Les objets maillés ont des capacités d\'édition limitées dans FreeCAD, les convertir en [shapes (formes)](Shape/fr.md) permettra leur utilisation avec de nombreux autres outils booléens et de modification.

L\'opération inverse est **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh Tesselation](Mesh_FromPartShape/fr.md)** de l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [atelier Mesh](Mesh_Workbench/fr.md).

## Utilisation

1.  Sélectionnez l\'objet mesh dans la [Vue en arborescence](Tree_view/fr.md).
2.  Allez dans le menu, **Pièce → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Créer une forme à partir d'un maillage...**.
3.  Un menu contextuel demandera la tolérance pour la forme de la pièce. La valeur par défaut est {{Value|0.1}}.
4.  Une [forme](Shape/fr.md) de l\'objet maillage est créée en tant que nouvel objet séparé.

L\'analyse et la réparation du maillage, si nécessaire, doivent être effectuées manuellement avant de lancer **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Créer la forme à partir d'un maillage... ](Part_ShapeFromMesh/fr.md)**. Les outils appropriés pour cette tâche sont disponibles dans l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Atelier Mesh](Mesh_Workbench/fr.md).

Après la création d\'une [Shape](Shape/fr.md), il peut être utile d\'utiliser **[Convertir en solide](Part_MakeSolid/fr.md)** (nécessaire pour les [Operations booléennes](Part_Boolean/fr.md)) et **[<img src=images/Part_RefineShape.svg style="width:16px"> [Affiner la forme](Part_RefineShape/fr.md)**.

## Liens

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) vidéo par AllVisuals4U.

## Script

La création d\'une [Shape](Shape/fr.md) à partir d\'un [Maillage](Mesh/fr.md) peut être fait en utilisant la méthode `makeShapeFromMesh` à partir d\'un [Part TopoShape](Part_TopoShape/fr.md). Vous devez spécifier le maillage source et la tolérance et affecter le résultat à un nouvel objet [Part Feature](Part_Feature/fr.md).

Notez que le maillage doit être recalculé avant d\'être converti en Forme (Shape) sinon il n\'y aura pas d\'informations de topologie et la conversion ne réussira pas.


```python
import FreeCAD as App
import Part

doc = App.newDocument()
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

solid = doc.addObject("Part::Feature", "Shape")
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid.Shape = shape
solid.Placement.Base = App.Vector(15, 0, 0)
solid.purgeTouched()
doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/fr
