---
 GuiCommand:
   Name: Arch MeshToShape
   Name/fr: Arch Maillage vers une forme
   MenuLocation: Utilitaires , Maillage vers une forme
   Workbenches: BIM_Workbench/fr
   SeeAlso: Arch_SplitMesh/fr, Arch_RemoveShape/fr
---

# Arch MeshToShape/fr

## Description

L\'outil **Arch Maillage vers une forme** convertit un [maillage](Mesh/fr.md) ([Mesh Feature](Mesh_Feature/fr.md)) en une [forme](Shape/fr.md) ([Part Feature](Part_Feature/fr.md)).

Cet outil est optimisé pour les objets à surfaces planes (pas de courbes). L\'outil correspondant **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part Forme à partir d'un maillage](Part_ShapeFromMesh/fr.md)** à partir de l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md) peut être plus adapté aux objets qui contiennent des surfaces courbes.



## Utilisation

1.  Sélectionnez un objet maillé
2.  Sélectionnez l\'option **Utilitaires → <img src="images/Arch_MeshToShape.svg" width=16px> Maillage vers une forme** du menu.



## Propriétés

## Limitations



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Cet outil peut être utilisé dans une [macro](Macros/fr.md) et utilisé dans la console [Python](Python/fr.md) en utilisant la fonction :


```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```

L\'extrait de code ci-dessus convertit le `obj` (un maillage) donné en une forme joignant les facettes coplanaires.

-   Si ` mark` est `True`, les objets non solides seront affichés en rouge.

-   Si ` fast` est `True`, il utilise un algorithme plus rapide en créant un shell à partir des facettes puis en supprimant le séparateur.

-    `tol`est la tolérance utilisée lors de la conversion de segments de maillage en fils.

-   Si `flat` est `True`, les polylignes seront parfaitement plans pour être sûr qu\'ils puissent être convertis en faces mais cela pourrait laisser des espaces dans le shell final.

-   Si `cut` est `True`, les trous dans les faces sont créés par soustraction.

Exemple :


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
⏵ [documentation index](../README.md) > Arch MeshToShape/fr
