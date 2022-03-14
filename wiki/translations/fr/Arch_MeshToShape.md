---
- GuiCommand:/fr
   Name:Arch MeshToShape
   Name/fr:Arch Maillage vers une forme
   MenuLocation:Arch → Utilitaires → Maillage vers forme
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Séparer un objet Mesh](Arch_SplitMesh/fr.md), [Arch Supprimer la forme](Arch_RemoveShape/fr.md)
---

# Arch MeshToShape/fr

## Description

[Arch Maillage vers une forme](Arch_MeshToShape/fr.md) convertit un objet [Mesh](Mesh/fr.md) ([Mesh Feature](Mesh_Feature/fr.md)) sélectionné en un objet [Shape](Shape/fr.md) ([Part Feature](Part_Feature/fr.md)).

Cet outil est optimisé pour les objets à surfaces planes (pas de courbes). L\'outil correspondant **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part Créer une forme à partir du maillage](Part_ShapeFromMesh/fr.md)** à partir de l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Atelier Part](Part_Workbench/fr.md) peut être plus adapté aux objets qui contiennent des surfaces courbes.

## Utilisation

1.  Sélectionnez un objet mesh (maille)
2.  Appuyez sur l\'entrée **<img src="images/Arch_MeshToShape.svg" width=16px> [Maillage vers forme](Arch_MeshToShape/fr.md)** dans **Arch → Utilitaires → Maillage vers forme**.

## Propriétés

## Limitations

## Script


**Voir aussi:**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction : 
```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```

L\'extrait de code ci-dessus convertit le `obj` (un maillage) donné en une forme joignant les facettes coplanaires.

-   Si ` mark` est `True`, les objets non solides seront affichés en rouge.

-   Si ` fast` est `True`, il utilise un algorithme plus rapide en créant un shell à partir des facettes puis en supprimant le séparateur.

-    `tol`est la tolérance utilisée lors de la conversion de segments de maillage en fils.

-   Si `flat` est `True`, les fils seront parfaitement plans pour être sûr qu\'ils puissent être convertis en faces mais cela pourrait laisser des espaces dans le shell final.

-   Si `cut` est `True`, les trous dans les faces sont créés par soustraction.

Exemple: 
```python
import Arch, Mesh, BuildRegularGeoms

Box = FreeCAD.ActiveDocument.addObject("Mesh::Cube", "Cube")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

new_obj = Arch.meshToShape(Box)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MeshToShape/fr
