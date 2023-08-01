# Part TopoShape/fr
{{TOCright}}

## Introduction

[Part TopoShape](Part_TopoShape/fr.md) ou officiellement `Part::TopoShape` est une classe qui définit une **topological shape** (forme topologique) paramétrique dans le logiciel. Les objets dans le document qui montrent quelque chose dans la [Vue 3D](3D_view/fr.md) ont normalement une TopoShape.

Les formes topologiques, ainsi que leurs méthodes, sont définies par le noyau [OpenCASCADE](OpenCASCADE/fr.md) (OCCT). FreeCAD utilise ces formes et construit [App DocumentObjects](App_DocumentObject/fr.md) autour d\'eux.

Un autre type de classe est celui de [mesh](Mesh/fr.md). Cette classe n\'est pas très paramétrique car elle ne peut pas être redéfinie facilement sauf en spécifiant des sommets individuels et des surfaces triangulaires.

![](images/Shape_and_mesh.svg )



*A gauche: paramétrique [Part TopoShape](Part_TopoShape/fr.md) définie par les propriétés. A droite: un [maillage](Mesh/fr.md) non paramétrique défini par des sommets et des surfaces triangulaires.*

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. La classe `Part::TopoShape* est incorporée dans l'objet {{incode|Part::Feature` et à partir de là, elle est propagée à tous les objets qui en sont dérivés.}}

## Utilisation

Part TopoShape est un objet attribué à certains [App DocumentObjects](App_DocumentObject/fr.md).

En particulier, l\'objet de base qui gère ces types d\'attributs est la classe [Part Feature](Part_Feature/fr.md) (`Part::Feature` class). Tous les objets dérivés de cette classe auront accès à un Part TopoShape.

Certains des objets les plus importants avec Part TopoShape sont les suivants:

-   Tout solide primitif créé avec l\'[Atelier Part](Part_Workbench/fr.md).
-   Tout [PartDesign Corps](PartDesign_Body/fr.md) et [PartDesign Feature](PartDesign_Feature/fr.md) créés avec l\'[Atelier Part](Part_Workbench/fr.md).
-   Tout objet dérivé de [Part Part2DObject](Part_Part2DObject/fr.md), comme la plupart des objets créés avec l\'[Atelier Draft](Draft_Workbench/fr.md).
-   Toute [Esquisse](Sketch/fr.md), c\'est-à-dire [Sketcher SketchObject](Sketcher_SketchObject/fr.md), créé avec l\'[Atelier Sketcher](Sketcher_Workbench/fr.md).
-   Tout objet créé en important un fichier STEP, BREP et des fichiers au format solide similaires.

## Script


**Voir aussi :**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](Scripted_objects/fr.md).

Tous les objets dérivés de `Part::Feature` auront un [Part TopoShape](Part_TopoShape/fr.md) qui est normalement accessible à partir de son attribut `Shape`. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Box", "Box")
print(obj.Shape)
```

Une TopoShape possède de nombreux attributs (variables) et méthodes qui contiennent des informations à son sujet et qui permettent d\'effectuer des opérations avec elle. Ces variables et méthodes peuvent être testées dans la [Console Python](Python_console/fr.md). 
```python
print(obj.Shape.Area)
print(obj.Shape.BoundBox)
print(obj.Shape.CenterOfMass)
print(obj.Shape.ShapeType)

obj.Shape.check()
obj.Shape.copy()
obj.Shape.exportStep("my_file.step")
obj.Shape.exportStl("my_file.stl")
```

Pour une liste complète des attributs et des méthodes, consultez l\'outil [Documentation du code source](Source_documentation/fr.md) et l\'outil**[<img src=images/Std_PythonHelp.svg style="width:16px"> [Std Documentation modules Python](Std_PythonHelp/fr.md)**.

Vous pouvez obtenir un résumé rapide de toutes les méthodes en utilisant la fonction intégrée `help()` en Python. 
```python
help(obj.Shape)
```


 {{Document objects navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part TopoShape/fr
