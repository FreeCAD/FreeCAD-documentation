---
- GuiCommand:
   Name: Mesh Export
   Name/fr: Mesh Exporter le maillage
   MenuLocation: Maillages -> Exporter le maillage...
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Std_Export/fr, Import_Export/fr
---

# Mesh Export/fr

## Description

La commande **Exporter un maillage** exporte un objet maillé dans un format de fichier maillé. Plusieurs formats de fichiers sont pris en charge.



## Utilisation

1.  Sélectionnez un seul objet maillé.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_Export.svg" width=16px> [Exporter le maillage...](Mesh_Export/fr.md)**.
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_Export.svg" width=16px> Exporter le maillage...** du menu.
    -   Sélectionnez l\'option **<img src="images/Mesh_Export.svg" width=16px> Exporter le maillage...** du menu contextuel de la [vue en arborescence](Tree_view/fr.md) ou le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Sélectionnez le format de fichier correct dans la boîte de dialogue.
4.  Entrez un nom de fichier. Si vous avez sélectionné l\'option {{Value|Tous les fichiers (*.*)}} à l\'étape précédente et si vous ne spécifiez pas d\'extension de fichier ici, l\'extension **.stl** sera utilisée.
5.  Appuyez sur le bouton **Sauvegarder**.



## Remarques

-   Il existe des [préférences d\'exportation liées aux formats Mesh](Import_Export_Preferences/fr#Formats_Mesh.md) mais elles ne s\'appliquent pas à cette commande. Elles sont utilisées par la commande [Std Exporter](Std_Export/fr.md).



## Préférences

-   Le dernier emplacement de fichier utilisé est enregistré : **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.



## Script

Voir aussi : [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour exporter des objets (y compris des objets maillés) dans un format de fichier maillé, utilisez la méthode `export` du module Mesh.


```python
import FreeCAD
import Mesh

doc = FreeCAD.ActiveDocument

Mesh.export([doc.Cone, doc.Cylinder], 'D:/testfiles/mymodel.stl')
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Export/fr
