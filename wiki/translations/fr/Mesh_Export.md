---
- GuiCommand   */fr
   Name   *Mesh Export
   Name/fr   *Mesh Exporter le maillage
   MenuLocation   *Maillages → Exporter le maillage...
   Workbenches   *[Mesh](Mesh_Workbench/fr.md)
   SeeAlso   *[Std Exporter](Std_Export/fr.md), [Import Export](Import_Export/fr.md)
---

# Mesh Export/fr

## Description

La commande **Export de maillage** exporte un objet maillé dans un format de fichier maillé. Plusieurs formats de fichiers sont pris en charge.

## Utilisation

1.  Sélectionnez un seul objet maillé.
2.  Il existe plusieurs façons d\'appeler la commande   *
    -   Appuyez sur le bouton **<img src="images/Mesh_Export.svg" width=16px> [Mesh Exporte le maillage dans un fichier](Mesh_Export.md)**.
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_Export.svg" width=16px> Exporter le maillage...** dans le menu.
    -   Sélectionnez l\'option **<img src="images/Mesh_Export.svg" width=16px> Exporter le maillage...** dans le menu contextuel de la [vue en arborescence](tree_view/fr.md) ou le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Sélectionnez le format de fichier correct dans la boîte de dialogue.
4.  Entrez un nom de fichier. Si vous avez sélectionné l\'option {{Value|All files (*.*)}} à l\'étape précédente et si vous ne spécifiez pas d\'extension de fichier ici, l\'extension **.stl** sera utilisée.
5.  Appuyez sur le bouton **Sauvegarder**.

## Remarques

-   Il existe des [préférences d\'exportation liées aux formats Mesh](Import_Export_Preferences/fr#Formats_Mesh.md) mais elles ne s\'appliquent pas à cette commande. Elles sont utilisées par la commande [Std Exporter](Std_Export/fr.md).

## Préférences

-   Le dernier emplacement de fichier utilisé est stocké   * **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script

Voir aussi   * [FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour exporter des objets (y compris des objets maillés) dans un format de fichier maillé, utilisez la méthode `export` du module Mesh.


```python
import FreeCAD
import Mesh

doc = FreeCAD.ActiveDocument

Mesh.export([doc.Cone, doc.Cylinder], 'D   */testfiles/mymodel.stl')
```





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Export/fr
