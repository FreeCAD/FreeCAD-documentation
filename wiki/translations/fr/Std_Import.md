---
- GuiCommand:
   Name:Std_Import
   Name/fr:Std Importer
   MenuLocation:Fichier - Importer...
   Workbenches:Tous
   Shortcut:**Ctrl**+**I**
   SeeAlso:[Std Ouvrir](Std_Open/fr.md), [Import Export](Import_Export/fr.md), [Préférences d'Import Export](Import_Export_Preferences/fr.md)
---

# Std Import/fr

## Description

La commande **Std Importer** importe la géométrie d\'un format de fichier différent dans le document actif. De nombreux formats de fichiers sont pris en charge et pour certains formats, plusieurs options d\'importation existent. Voir [Import Export](Import_Export/fr.md) pour plus d\'informations.


{{Version/fr|0.21}}

: si un format d\'image est sélectionné, la commande créera un [plan d\'image](#Plan_d'image.md).



## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Sélectionnez l\'option **Fichier → <img src="images/Std_Import.svg" width=16px> Importer...** dans le menu.
    -   Utilisez le raccourci clavier: **Ctrl**+**I**.
2.  Sélectionnez éventuellement le format de fichier correct dans la boîte de dialogue.
3.  Sélectionner un fichier.
4.  Appuyez sur le bouton **Ouvrir**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.



## Remarques

-   Pour convertir un [maillage](Mesh_Workbench/fr.md) importé en tant que solide, consultez le tutoriel [Importer depuis STL ou OBJ](Import_from_STL_or_OBJ/fr.md).
-   Pour importer dans un nouveau document, vous pouvez utiliser la commande [Std Ouvrir](Std_Open/fr.md).
-   Certains ateliers ont des commandes d\'importation supplémentaires. Voir: [Import Export](Import_Export/fr.md).



## Préférences

-   Voir : [Préférences Import Export](Import_Export_Preferences/fr.md).
-   Le dernier emplacement de fichier utilisé est stocké : **Outils → Éditer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.
-   Le dernier filtre d\'importation utilisé est stocké : **Outils → Éditer les paramètres... → BaseApp → Preferences → General → FileImportFilter**.



## Plan d\'image 

Un plan d\'image est une représentation plane d\'une image dans la [vue 3D](3D_view/fr.md). Il peut par exemple être utilisé lors de la création d\'un modèle basé sur des photographies d\'un objet existant.

Par défaut, un plan d\'image est placé sur le plan global XY. La taille initiale d\'un plan d\'image est calculée sur la base d\'une résolution de 96 px/pouce.



### Modifier

1.  Pour modifier un plan d\'image, effectuez l\'une des opérations suivantes :
    -   Double-cliquez sur le plan d\'image dans la [vue en arborescence](Tree_view/fr.md).
    -   Cliquez avec le bouton droit de la souris sur le plan d\'image dans la vue en arborescence et sélectionnez **<img src="images/Image-scaling.svg" width=16px> Modifier l'image...** dans le menu contextuel.
2.  Si le plan de l\'image n\'est pas parallèle au plan XY, XZ ou YZ du système de coordonnées global, il est réaligné pour être parallèle au plan XY.
3.  Le panneau de tâches **Réglages du plan de l'image** s\'ouvre.
4.  Sélectionnez **Plan XY**, **Plan XZ** ou **Plan YZ** du système de coordonnées global.
5.  Cochez **Inverser le sens** pour faire pivoter le plan de l\'image de 180°. L\'axe de rotation dépend du plan sélectionné. Pour le plan XY, il s\'agit de l\'axe X global. Pour les plans XZ et YZ, il s\'agit de l\'axe Z global.
6.  Les **Décalage**, **Distance X** et **Distance Y** sont relatifs au système de coordonnées du plan de l\'image. Un petit décalage négatif peut être utile pour tracer l\'image avec une [esquisse](Sketcher_Workbench/fr.md) ou une géométrie de [Draft](Draft_Workbench/fr.md).
7.  Modifier éventuellement la **Transparence**.
8.  Options de **Dimension de l'image** :
    -   Mise à l\'échelle par entrée numérique :
        1.  Décochez éventuellement **Conserver les proportions** pour une mise à l\'échelle inégale.
        2.  Entrez une **Largeur** et/ou une **Hauteur**.
    -   Mettre à l\'échelle en choisissant des points :
        1.  Appuyez sur le bouton **Calibrer**.
        2.  Choisissez deux points dans l\'image.
        3.  Une ligne de dimension est affichée.
        4.  Saisissez la dimension souhaitée.
        5.  Appuyez sur **Entrée** ou sur le bouton **Appliquer**.
9.  Appuyez sur le bouton **OK** pour confirmer les modifications et fermer le panneau de tâches.



### Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet Plan d\'image est dérivé d\'un objet [App GeoFeature](App_GeoFeature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Image Plane}}

-    **Image File|FileIncluded**: le fichier d\'image utilisé pour le plan d\'image. Ce fichier est stocké dans le fichier **.FCStd**.

-    **XSize|Length**: largeur du plan de l\'image.

-    **YSize|Length**: hauteur du plan de l\'image.



#### Vue


{{TitleProperty|Object Style}}

-    **Lighting|Enumeration**: comment le plan de l\'image est éclairé dans la [vue 3D](3D_view/fr.md). Peut être {{value|Two side}} ou {{value|One side}}.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Import/fr
