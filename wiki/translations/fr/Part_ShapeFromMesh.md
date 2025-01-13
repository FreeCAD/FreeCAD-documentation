---
 GuiCommand:
   Name: Part ShapeFromMesh
   Name/fr: Part Forme à partir du maillage
   MenuLocation: Part , Créer une forme à partir d'un maillage...
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_MakeSolid/fr, Part_RefineShape/fr, Part_PointsFromMesh/fr
---

# Part ShapeFromMesh/fr



## Introduction

La commande <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:24px;"> **Part Forme à partir du maillage** crée des formes à partir d\'[objets Mesh](Mesh/fr.md). Les objets Mesh ont des capacités d\'édition limitées dans FreeCAD, les convertir en [formes](Shape/fr.md) permettra de les utiliser avec bien plus d\'outils booléens et de modifications.

L\'opération inverse est [Mesh Tesselation](Mesh_FromPartShape/fr.md) de l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [atelier Mesh](Mesh_Workbench/fr.md).



## Utilisation

1.  L\'analyse et la réparation de l\'objet maillé, si nécessaire, doivent être effectuées avant de lancer cette commande. Les outils appropriés pour cette tâche sont disponibles dans l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">[atelier Mesh](Mesh_Workbench/fr.md).
2.  Sélectionnez un ou plusieurs objets Mesh.
3.  Sélectionnez l\'option **Part → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Créer une forme à partir d'un maillage...** du menu.
4.  La fenêtre de dialogue **Forme à partir du maillage** s\'ouvre.
5.  Vous pouvez cocher la case **Recomposer la forme** et spécifiez une tolérance :
    -   Cette option n\'est généralement pas nécessaire. Elle est destinée aux objets maillés qui ne sont pas étanches et présentent de petits espaces entre les arêtes.
    -   Si l\'option est sélectionnée, un composé de coques, au lieu d\'un composé de faces, est créé.
    -   L\'opération de recomposition peut être exigeante en termes de calcul.
6.  Pressez sur le bouton **OK**.
7.  Pour chaque objet sélectionné, une [forme](Shape/fr.md) est créée en tant que nouvel objet séparé.
8.  Vous pouvez utiliser <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Part Affiner la forme](Part_RefineShape/fr.md) sur ces objets.
9.  Vous pouvez transformer les objets finaux en solides avec <img alt="" src=images/Part_MakeSolid.svg  style="width:16px;"> [Part Convertir en solide](Part_MakeSolid/fr.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

La commande Part Forme à partir du maillage crée des objets [Part Feature](Part_Feature/fr.md) sans propriétés supplémentaires.



## Script

La création d\'une forme [Shape](Shape/fr.md) à partir d\'un [maillage](Mesh/fr.md) peut être faite en utilisant la méthode `makeShapeFromMesh` à partir d\'un [Part TopoShape](Part_TopoShape/fr.md). Vous devez spécifier le maillage source et la tolérance puis affecter le résultat à un nouvel objet [Part Feature](Part_Feature/fr.md).

Notez que le maillage doit être recalculé avant d\'être converti en Forme (Shape) sinon il n\'y aura pas d\'informations de topologie et la conversion ne réussira pas.


```python
import FreeCAD as App
import Part

doc = App.ActiveDocument
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid = doc.addObject("Part::Feature", "Solid")
solid.Shape = Part.Solid(shape.removeSplitter())
solid.Placement.Base = App.Vector(15, 0, 0)
doc.recompute()
```



## Liens

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) vidéo par AllVisuals4U.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/fr
