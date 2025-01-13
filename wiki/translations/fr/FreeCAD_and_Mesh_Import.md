# FreeCAD and Mesh Import/fr
## Après l\'importation 

Après l\'importation, le modèle n\'est (pour FreeCAD) qu\'un assemblage de faces. Vous voudrez peut-être convertir le modèle en une forme que FreeCAD peut reconnaître et qui pourra être modifiée dans FreeCAD.

Pour ce faire :

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md).
2.  Sélectionnez le maillage et allez au menu **Part → [Créer une forme à partir du maillage](Part_ShapeFromMesh/fr.md)** ou cliquez sur le bouton <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:24px;"> [Créer une forme à partir du maillage](Part_ShapeFromMesh/fr.md).
3.  Cliquez sur **OK** dans la fenêtre de dialogue.
4.  Sélectionnez la forme créée.
5.  Sélectionnez **Part → [Convertir en solide](Part_MakeSolid/fr.md)**.
6.  Sélectionnez le nouveau solide créé.
7.  Allez à **Part → Créer une copie → [Affiner la forme](Part_RefineShape/fr.md)** ou pressez le bouton <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Affiner la forme](Part_RefineShape/fr.md).

**Remarque :** la dernière étape n'est pas nécessaire mais elle nettoiera le solide de la plupart de ses arêtes résiduelles sur les surfaces planes et cylindriques.



## Erreurs

### \"cannot convert because shape is not a shell\" 

Votre coque semble avoir des erreurs, peut-être qu\'elle n\'est pas fermée (elle serait trouée). Étant donné que les fonctions de l\'atelier Mesh de FreeCAD sont un peu limitées pour le moment, vous pouvez essayer d'examiner et de réparer votre modèle avec un logiciel tiers. Après cela, vous pouvez essayer à nouveau d'importer et de convertir votre modèle.



## Programmes tierces 

-   [MeshLab](https://www.meshlab.net/)
    -   licence : open source (GPL V2)
    -   fonctionne sous Windows 32/64 bits, Linux et macOS
-   [Meshmixer](https://meshmixer.com/)
    -   Licence : freeware
    -   fonctionne sous Windows 64-bit



## Tutoriels

-   [Importer des STL ou OBJ](Import_from_STL_or_OBJ/fr.md)
-   [Exporter des STL ou OBJ](Export_to_STL_or_OBJ/fr.md)



## En relation 

-   [FreeCAD How to Import Export](FreeCAD_Howto_Import_Export/fr.md)



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and Mesh Import/fr
