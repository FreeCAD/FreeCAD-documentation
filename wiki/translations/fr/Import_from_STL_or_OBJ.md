# Import from STL or OBJ/fr
{{TutorialInfo/fr
|Topic= Importation depuis STL ou OBJ
|Level= Débutant
|Time= 30 minutes
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}

## Introduction

Dans ce tutoriel, nous aborderons comment importer des fichiers STL/OBJ dans FreeCAD. Étant donné que le format de maille STL/OBJ est sans dimension, FreeCAD supposera à l\'importation que les unités utilisées dans le modèle sont mm. Si ce n\'est pas le cas, vous devez étaler votre modèle, soit dans l\'application où il a été créé avec (avant de l\'exporter) ou vous devez mettre à l\'échelle votre modèle dans FreeCAD après l\'importation et la convertir en un solide.

## Pièce d\'échantillon 

Pour ce tutoriel, vous pouvez utiliser votre propre fichier STL ou créer un fichier de démonstration en procédant comme suit:

-   Ouvrir FreeCAD
-   Créer un nouveau document
-   Passer à l\'atelier Maillage
-   Insérer un tor en cliquant sur **Meshes** → **<img src="images/Mesh_BuildRegularSolid.svg" width=32px> Solide Régulier...** en choisissant des paramètres comme:
    -   Rayon 1: 10 mm
    -   Radius2: 2 mm
    -   Échantillonnage: 50
-   Cliquez sur **Créer**, puis sur **Fermer**
-   Enregistrez votre fichier avec **Fichier** → **Sauvegarder** pour obtenir un fichier FreeCAD contenant un objet maillage

Pour importer un fichier STL ou OBJ dans FreeCAD, créez un nouveau document FreeCAD et choisissez **Fichier** → **Importer** dans le menu supérieur.

## Nettoyage et réparation du fichier STL / OBJ pour la préparation de l\'importation 

Fondamentalement, FreeCAD importerait n\'importe quel fichier STL/OBJ. Mais notre objectif est d\'avoir un solide qui peut être mesuré et modifié (ajout de blocs / trou\...). Pour une conversion réussie de maillage en solide, nous devons nous assurer que le maillage est \"imperméable à l\'eau\" (n\'a pas de trous) ou n\'a pas d\'autres erreurs.
Le but de FreeCAD n\'est pas d\'être un bon modélisateur de maillage, il est conçu pour être un modélisateur de solide. FreeCAD dispose de certaines fonctionnalités pour l\'opération de maillage dans un atelier de Maillage et un atelier OpenSCAD (certaines opérations ont besoin d\'OpenSCAD pour être installées et configurées dans les préférences FreeCAD).
Certains utilisateurs aiment utiliser un logiciel tiers pour nettoyer et réparer des mailles, par exemple

-   [Netfabb Basic](http://www.netfabb.com/downloadcenter.php?basic=1) (Windows/Linux/Mac) - gratuit pour un usage personnel (réparation de maillage automatique disponible)
-   [Meshlab](http://meshlab.sourceforge.net/) (Windows/Linux/Mac) - Open Source

Dans ce tutoriel, nous utiliserons le l\'atelier de Maillage dans FreeCAD pour nettoyer/réparer/vérifier le maillage de notre fichier exemple.

### Test et réparation automatique 

-   Ouvrez FreeCAD et l\'exemple de fichier FreeCAD contenant l\'objet maillage
-   Passer l\'atelier Maillage
-   Assurez-vous que votre objet maillé est sélectionné dans l\'arborescence
-   Choisissez **Mailles** → **Analyser** → **Évaluez et réparez le maillage ...** dans le menu supérieur
-   Assurez-vous que le menu déroulant dans le coin supérieur droit affiche le nom de votre objet maillé
-   Avec le dernier point dans la liste en lisant \"All above tests together\", cliquez sur **Analyser**
-   Les textes à côté des cases à cocher changeront pour tenir compte des résultats des différents tests
-   Si des erreurs ont été détectées, les cases à cocher correspondantes seront cochées et vous pourrez sélectionner **Réparation**
-   Choisissez **Fermez** pour fermer le menu

### Harmonisation des normales 

L\'harmonisation des normales d\'un objet maillé peut être effectuée par

-   Sélection de votre objet maillage dans l\'arborescence
-   Choisissez **Meshes** → **<img src="images/Mesh_HarmonizeNormals.svg" width=32px> Harmoniser les normales** dans le menu principal.

Astuce: En choisissant l\'objet maillage dans l\'arborescence, en allant dans l\'onglet Vue dans la vue de la propriété et en changeant \"Éclairage\" de \"Deux côtés\" sur \"Un côté\", vous pouvez identifier des triangles avec des normales inversées. Si les normales pointent dans le maillage, le triangle sera affiché en noir.

### Fermeture des trous 

Vous pouvez également fermer manuellement des trous dans votre objet maillage par

-   Sélection de votre objet maillage dans l\'arborescence
-   Choisissez **Meshes** → **Fill holes...** dans le menu supérieur
-   Spécifiez le nombre maximum d\'arêtes à remplir (3 est par défaut)
-   Étant donné que STL et OBJ sont des mailles constituées de triangles, le nombre d\'arêtes par défaut devrait être suffisant

Une autre méthode de fermeture manuelle des trous dans votre objet maillé serait:

-   Sélection de votre objet maillage dans l\'arborescence
-   Choisissez **Meshes** → **<img src="images/Mesh_FillInteractiveHole.svg" width=32px> Close hole** dans le menu principal
-   Sélectionnez l\'un des bords du trou dans l\'objet maillage dans la vue 3D
-   Cliquez avec le bouton droit de la souris dans la vue 3D et choisissez **Leave hole-filling mode** pour quitter la commande

## Conversion du maillage en solide 

-   Passer à l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md)
-   Assurez-vous que votre objet maillé est sélectionné dans l\'arborescence, sinon, sélectionnez-le
-   Choisissez **Pièce** → **<img src="images/Part_ShapeFromMesh.svg" width=32px> Create shape from mesh...** dans le menu principal
-   Précisez la tolérance pour la forme de couture (0,1 est par défaut)
-   Un nouvel objet sera créé dans l\'arborescence (avec l\'icône de forme bleue, au lieu de l\'icône de maillage vert)
-   Sélectionnez l\'objet nouvellement créé dans l\'arborescence
-   Choisissez **Pièce** → **Create a copy** → **<img src="images/Part_RefineShape.svg" width=32px> Affiner forme** dans le menu principal
-   Un nouvel objet sera créé dans l\'arborescence et le précédent sera rendu invisible
-   Sélectionnez l\'objet nouvellement créé dans l\'arborescence
-   Choisissez **Pièce** → **Convertir en solide** dans le menu principal
-   Un nouvel objet sera créé dans l\'arborescence, portant \"(Solid)\" dans son nom, pour indiquer qu\'il s\'agit d\'un solide

Étant donné que le solide créé n\'a pas d\'historique et aucune fonctionnalité éditable (comme une copie simple dans FreeCAD) vous pouvez supprimer tous les objets précédents de l\'arborescence. Cela réduirait votre taille de fichier\...

## Liens

-   [Importer un fichier STL ou OBJ](Import_from_STL_or_OBJ/fr.md)
-   [Import Export](Import_Export/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Import](Import_Workbench.md) > Import from STL or OBJ/fr
