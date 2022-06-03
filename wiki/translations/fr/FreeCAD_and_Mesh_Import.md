# FreeCAD and Mesh Import/fr
{{TOCright}}

## Après l\'importation 

Après l\'importation, le modèle n\'est (pour FreeCAD) qu\'un assemblage de faces. Vous voudrez peut-être convertir le modèle en une forme que FreeCAD peut reconnaître et qui pourra être modifiée dans FreeCAD.

Pour ce faire    *

1.  Basculez vers l\'<img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [atelier Part](Part_Workbench/fr.md).
2.  Sélectionnez le maillage et accédez au menu **Part → [Créer une forme à partir du maillage](Part_ShapeFromMesh/fr.md)** ou cliquez sur <img alt="" src=images/Part_ShapeFromMesh.svg  style="width   *24px;"> [Part Créer une forme à partir du maillage](Part_ShapeFromMesh/fr.md).
3.  Cliquez sur **OK** dans le dialogue.
4.  Sélectionnez la forme nouvellement créée.
5.  Sélectionnez **Part → [Convertir en solide](Part_MakeSolid/fr.md)**.
6.  Sélectionnez le nouveau solide créé.
7.  Aller à **Part → [Affiner la forme](Part_RefineShape/fr.md)** ou pressez le bouton <img alt="" src=images/Part_RefineShape.svg  style="width   *24px;"> [Affiner la forme](Part_RefineShape/fr.md).

**Remarque   *** la dernière étape n'est pas nécessaire mais elle nettoiera le solide de la plupart de ses arêtes résiduelles sur les surfaces planes et cylindriques.

## Erreurs

### \"Impossible de convertir car la forme n\'est pas une coque\" 

Eh bien, votre coque semble avoir des erreurs, peut-être qu\'elle n\'est pas fermée (elle serait trouée). Étant donné que les fonctionnalités du maillage dans FreeCAD sont un peu limitées pour le moment, vous pouvez essayer d'examiner et de réparer votre modèle avec un logiciel tiers. Après cela, vous pouvez essayer à nouveau d'importer et de convertir votre modèle.

## Programmes tierces 

-   [Meshlab](http   *//meshlab.sourceforge.net/)
    -   licence    * Open Source (GPL V2)
    -   fonctionne sous Windows 32/64 bits, Linux et Mac OS X
-   [netFabb basique](http   *//www.netfabb.com/downloadcenter.php?basic=1)
    -   Licence    * Freeware
    -   fonctionne sous Windows XP/7/8, Linux et Mac OS X

## Tutoriels

-   [Import depuis STL ou OBJ](Import_from_STL_or_OBJ/fr.md)
-   [Export vers STL ou OBJ](Export_to_STL_or_OBJ/fr.md)

## En relation 

-   [FreeCAD Howto Import Export](FreeCAD_and_Mesh_Import/fr.md)

[Category   *User\_Documentation](Category_User_Documentation.md) [Category   *File\_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and Mesh Import/fr
