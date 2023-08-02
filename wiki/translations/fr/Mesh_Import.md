---
- GuiCommand:
   Name: Mesh Import‏‎
   Name/fr: Mesh Importer un maillage
   MenuLocation: Maillages -> Importer un maillage...
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Std_Import/fr, Std_Open/fr, Import_Export/fr
---

# Mesh Import/fr

## Description

La commande **Importer un maillage** importe la géométrie d\'un format de fichier de maillage dans le document actif. Plusieurs formats de fichiers sont pris en charge. La commande crée un objet maillage non paramétrique, un [Mesh Feature](Mesh_Feature/fr.md).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_Import.svg" width=16px> [Importer un maillage...](Mesh_Import/fr.md)**.
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_Import.svg" width=16px> Importer un maillage...** du menu.
    -   Sélectionnez l\'option **<img src="images/Mesh_Import.svg" width=16px> Importer un maillage...** du menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou le menu contextuel de la [vue 3D](3D_view/fr.md). Cette option n\'est disponible que si un objet maillé existant a été sélectionné. Notez que l\'objet sélectionné n\'est en fait pas utilisé ou modifié par la commande.
2.  Sélectionnez éventuellement le format de fichier correct dans la boîte de dialogue.
3.  Sélectionner un fichier.
4.  Appuyez sur le bouton **Ouvrir**.



## Formats de fichiers supportés 

La commande accepte : les fichiers stl, ast, bms, obj, off, iv, ply, nas et bdf. Pour le format de fichier NASTRAN (nas/bdf), seules les cartes GRID, CTRIA3 et CQUAD4 sont supportées.



## Préférences

-   Le dernier emplacement de fichier utilisé est enregistré : **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.



## Propriétés

Voir : [Mesh Feature](Mesh_Feature/fr.md).



## Script

Voir aussi : [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour importer un fichier maillé, utilisez la méthode `insert` du module Mesh.


```python
import Mesh
Mesh.insert('D:/testfiles/cylinder.stl')
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Import/fr
