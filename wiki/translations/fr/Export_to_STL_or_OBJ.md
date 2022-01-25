---
- TutorialInfo:/fr
   Topic:Exportation de fichier STL ou OBJ
   Level:Débutant
   Time:20 minutes
   Author:r-frank
   FCVersion:0.16.6703
---

# Export to STL or OBJ/fr





## Introduction

Dans ce tutoriel, nous allons découvrir comment exporter les fichiers de FreeCAD au formats STL/OBJ. Les formats de maillage STL/OBJ n\'ont aucune dimension. L\'exportation par FreeCAD supposera que l\'unité utilisée dans le modèle est exprimée en mm. Si ce n\'est pas le cas, vous devez mettre votre modèle à l\'échelle. Une façon de le faire est d\'utiliser <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> [Draft Échelle](Draft_Scale/fr.md).

## Faire un test 

Vous pouvez utiliser votre propre fichier FreeCAD, mais vous pouvez aussi créer un fichier test

-   Lancer FreeCAD
-   Créer un nouveau document
-   Basculer sur l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md)
-   Insérer un <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Part Cube](Part_Box/fr.md)
-   Insérer un <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Part Cône](Part_Cone/fr.md)
-   Sélectionnez les deux objets dans la [Vue en arborescence](Tree_view/fr.md)
-   Créer une fusion avec les deux éléments <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Part Union](Part_Fuse/fr.md)
-   Sauvegarder votre fichier.

## Méthode d\'exportation 1: Utilisation de \"Fichier → Exporter\" 

-   Sélectionnez le solide à exporter dans la vue arborescente.
-   Choisissez **Fichier** → **Exporter...** et définissez le type de fichier sur \"STL Mesh (\*.stl \*.ast)\".
-   Entrez votre nom de fichier. L\'extension par défaut est \".stl\". Vous devez inclure l\'extension \".ast\" dans le nom du fichier pour générer un fichier \".ast\". Choisissez **Sauvegarder**.

## Méthode d\'exportation 2: Utilisation de l\'atelier Mesh dans FreeCAD 

-   Basculez vers l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Atelier Mesh](Mesh_Workbench/fr.md).
-   Sélectionnez le solide à mailler dans la vue arborescente.
-   Choisissez **Maillages** → **<img src="images/Mesh_FromPartShape.svg" width=32px> Créez un maillage à partir de la forme...** à partir du menu principal (supérieur).
-   Sélectionnez l\'un des mailleurs disponibles et spécifiez les options disponibles. Pour plus d\'informations, voir [Mesh Maillage à partir d\'une forme‏‎](Mesh_FromPartShape/fr.md).
-   Choisissez **OK**. L\'objet maillé sera créé dans l\'arborescence (avec l\'icône de maillage verte <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">).
-   Cliquez avec le bouton droit de la souris sur l'objet maillé dans l'arborescence et choisissez **<img src="images/Mesh_ExportMesh.png" width=32px> Exporter le maillage...**.
-   Remplissez le nom du fichier; l\'extension n\'est pas nécessaire. L\'extension sera définie en fonction du type de fichier. Si vous incluez une extension qui ne correspond pas au type de fichier sélectionné, une extension pour le type sélectionné sera ajoutée lors de l\'enregistrement du fichier. Si vous incluez une extension qui correspond au type de fichier, aucune extension supplémentaire ne sera ajoutée.
-   Le type de fichier par défaut est un \"Binary STL (\*.stl)\". Changez le type si vous le souhaitez.
-   Choisissez **Sauvegarder**.

## Quelle méthode choisir? 

La méthode 2 est à privilégier. Parmi les raisons :

-   Lorsque vous avez plus d\'un corps à convertir, vous pouvez utiliser les outils de l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Atelier Mesh](Mesh_Workbench/fr.md). Par exemple, vous pouvez fusionner des maillages avant de les exporter.
-   Les surfaces courbes sont représentées dans le STL comme une série de segments de lignes droites, générés par tessellation. Cela se traduit par des dimensions intérieures légèrement inférieures à celles des surfaces courbes. Si vous exportez le fichier pour l\'utiliser dans l\'impression 3D, cela peut se traduire par un trou de taille insuffisante, par exemple. Dans ce cas, vous devrez peut-être choisir une valeur de tessellation plus fine. Lorsque vous exportez à partir d\'un autre atelier en utilisant **Fichier** → **Exporter...**, la tessellation est contrôlée par la tessellation de l\'affichage global défini dans **Edition**. → **Préférences...** → Part Design → Vue de la forme. Cependant, comme ces paramètres contrôlent la tessellation utilisée pour le rendu des formes à l\'écran, leur diminution ralentit le rendu de l\'affichage, souvent de manière significative. En outre, exporter immédiatement après avoir modifié la valeur de la préférence de tessellation d\'affichage n\'aura pas l\'effet escompté, car la tessellation d\'affichage n\'est pas mise à jour immédiatement. Il faut forcer une modification du modèle sous-jacent pour que la tessellation soit recalculée, par exemple en modifiant un paramètre de l\'esquisse (il suffit de le remettre à sa valeur initiale).

## Liens

-   [Importer un fichier STL ou OBJ](Import_from_STL_or_OBJ/fr.md)
-   [Import Export](Import_Export/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Export to STL or OBJ/fr
