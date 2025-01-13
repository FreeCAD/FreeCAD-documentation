# FEM Preferences/fr
## Introduction

Les préférences pour l\'<img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [atelier FEM](FEM_Workbench/fr.md) peuvent être trouvées dans l\'[éditeur de préférences](Preferences_Editor/fr.md). Dans le menu, sélectionnez **Édition → Préférences...** puis **<img src="images/Workbench_FEM.svg" width=16px> FEM**. Ce groupe n\'est disponible que si l\'atelier FEM a été chargé dans la session FreeCAD en cours.

Il y a sept pages : [Général](#Général.md), [Gmsh](#Gmsh.md), [CalculiX](#CalculiX.md), [Elmer](#Elmer.md), [Mystran](#Mystran.md), [Z88](#Z88.md) et [Netgen](#Netgen.md). Toutes les pages, à l\'exception de la première, contrôlent la manière dont FEM interagit avec les maillages et les solveurs externes.

Les solveurs externes actuellement acceptés sont :

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [CalculiX](FEM_SolverCalculixCxxtools/fr.md)
-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/fr.md)
-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Mystran](FEM_SolverMystran/fr.md)
-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Z88](FEM_SolverZ88/fr.md)



## Général

<img alt="" src=images/Preferences_FEM_Page_General.png  style="width:350px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                                                         | Description                                                                                                                                           |
+=============================================================================================================+=======================================================================================================================================================+
|                                                                                              | Répertoire dans lequel les fichiers de maillage et de solveur doivent être stockés                                                                    |
| **Répertoire de travail**                                                                       |                                                                                                                                                       |
|                                                                                                          |                                                                                                                                                       |
+++
|                                                                                              | S\'il y a plusieurs maillages, ils seront regroupés                                                                                                   |
| **Créer des collectes de maillage pour les formes de référence d'analyse (très expérimental)**  |                                                                                                                                                       |
|                                                                                                          |                                                                                                                                                       |
+++
|                                                                                              | Les [objets Résultats](FEM_ResultShow/fr.md) existants seront conservés, sinon ils seront écrasés par une nouvelle exécution du solveur.      |
| **Conserver les résultats après un nouveau calcul**                                             |                                                                                                                                                       |
|                                                                                                          |                                                                                                                                                       |
+++
|                                                                                              | Si coché, la fenêtre de dialogue [Afficher le résultat](FEM_ResultShow/fr.md) est ouverte avec les derniers paramètres utilisés.              |
| **Restaurer les paramètres de la fenêtre de dialogue des résultats**                            |                                                                                                                                                       |
|                                                                                                          |                                                                                                                                                       |
+++
|                                                                                              | Les contraintes seront cachées dans la vue du modèle lorsque la fenêtre de dialogue [Afficher le résultat](FEM_ResultShow/fr.md) est ouverte. |
| **Masquer les fonctions d'analyse lors de l'ouverture de la fenêtre de dialogue des résultats** |                                                                                                                                                       |
|                                                                                                          |                                                                                                                                                       |
+++
|                                                                                              | Le solveur par défaut à ajouter lors de l\'ajout d\'un [conteneur d\'analyse](FEM_Analysis/fr.md) ({{Version/fr|0.21}}).        |
| **Solveur par défaut**                                                                          |                                                                                                                                                       |
|                                                                                                          |                                                                                                                                                       |
+++

## Gmsh

<img alt="" src=images/Preferences_FEM_Page_Gmsh.png  style="width:350px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                             | Description                                                                                                                                   |
+=================================================================+===============================================================================================================================================+
|                                                  | Si cette case est cochée, FreeCAD cherchera le binaire de [Gmsh](FEM_MeshGmshFromShape/fr.md) dans les répertoires (habituels) connus |
| **Rechercher dans les répertoires binaires connus** |                                                                                                                                               |
|                                                              |                                                                                                                                               |
+++
|                                                  | Le chemin d\'accès au binaire de [Gmsh](FEM_MeshGmshFromShape/fr.md).                                                                 |
| **Chemin d'accès au binaire de Gmsh**               |                                                                                                                                               |
|                                                              |                                                                                                                                               |
+++

## CalculiX

<img alt="" src=images/Preferences_FEM_Page_CalculiX.png  style="width:350px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                           | Description                                                                                                                                                                                                                     |
+===============================================================================+=================================================================================================================================================================================================================================+
|                                                                | Si cette case est cochée, FreeCAD recherchera le binaire de [CalculiX](FEM_SolverCalculixCxxtools/fr.md) dans les répertoires connus (habituels)                                                                        |
| **Rechercher dans les répertoires des binaires connus**           |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Le chemin d\'accès au binaire de [CalculiX](FEM_SolverCalculixCxxtools/fr.md)                                                                                                                                           |
| **Chemin d'accès au binaire de CalculiX**                         |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Si cette case est cochée, un éditeur intégré de fichiers \*.inp avec coloration syntaxique est utilisé lors de l\'édition des jeux d\'entrée de CalculiX.                                                                       |
| **Utiliser l'éditeur interne pour les fichiers *.inp**            |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Le chemin d\'accès à l\'éditeur externe de fichiers \*.inp.                                                                                                                                                                     |
| **Éditeur externe**                                               |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Si la case est cochée, plusieurs fichiers \*.inp sont écrits et le fichier d\'entrée principal utilise les mots-clés \*INCLUDE pour référencer les autres. Si la case n\'est pas cochée, un seul gros fichier \*.inp est écrit. |
| **Diviser lors de l'écriture des fichiers *.inp**                 |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Type d\'analyse par défaut : Statique, Fréquence, Thermomecanique, Vérification du maillage ou Flambage.                                                                                                                        |
| **Type**                                                          |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Nombre de cœurs de processeurs physiques à utiliser pour le calcul parallèle.                                                                                                                                                   |
| **Nombre de cœurs du CPU à utiliser**                             |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Solveur de matrice par défaut : par défaut, PaStiX, Pardiso, Librairie d\'équations Spooles, Mise à l\'échelle itérative ou Solveur itératif de Cholesky.                                                                       |
| **Solveur de matrice**                                            |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Si cette case est cochée, la non-linéarité géométrique est incluse par défaut.                                                                                                                                                  |
| **Géométrie non-linéaire**                                        |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Si cette case est cochée, les contrôles du solveur ne sont pas ceux par défaut (ce qui n\'est pas recommandé dans la plupart des cas).                                                                                          |
| **Paramètre de contrôle de l'incrémentation du temps**            |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Nombre maximum d\'itérations dans un pas d\'analyse.                                                                                                                                                                            |
| **Nombre maximum d'itérations**                                   |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Taille de l\'incrémentation du temps initial (peut être modifiée par le solveur si l\'incrémentation automatique est utilisée).                                                                                                 |
| **Intervalle de temps initial**                                   |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Temps total de la simulation.                                                                                                                                                                                                   |
| **Durée de la simulation**                                        |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | La taille minimale de l\'intervalle de temps autorisé.                                                                                                                                                                          |
| **Intervalle de temps minimum**                                   |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | La taille maximale de l\'intervalle de temps autorisé.                                                                                                                                                                          |
| **Intervalle de temps maximum**                                   |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Si la case est cochée, les résultats pour les éléments 1D et 2D sont affichés par défaut avec une représentation 3D.                                                                                                            |
| **Format de sortie 3D pour les éléments de type poutre et coque** |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Si cette case est cochée, les analyses thermomécaniques sont par défaut de type permanent.                                                                                                                                      |
| **Type d'analyse (état transitoire ou stable)**                   |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Nombre par défaut de modes propres demandés dans les analyses fréquencielles.                                                                                                                                                   |
| **Nombre de modes propres**                                       |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Limite supérieure par défaut des fréquences propres évaluées dans les analyses de fréquence.                                                                                                                                    |
| **Limite de la fréquence haute**                                  |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++
|                                                                | Limite inférieure par défaut des fréquences propres évaluées dans les analyses de fréquence.                                                                                                                                    |
| **Limite de la fréquence basse**                                  |                                                                                                                                                                                                                                 |
|                                                                            |                                                                                                                                                                                                                                 |
+++

## Elmer

<img alt="" src=images/Preferences_FEM_Page_Elmer.png  style="width:350px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                           | Description                                                                                                                                                                                                                                                                                    |
+===============================================================================+================================================================================================================================================================================================================================================================================================+
|                                                                | Si cette option est cochée, FreeCAD recherchera le binaire de l\'utilitaire d\'écriture du réseau d\'[Elmer](FEM_SolverElmer.md) dans les répertoires (habituels) connus.                                                                                                              |
| **ElmerGrid : Rechercher dans les répertoires binaires connus**   |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Le chemin d\'accès au binaire de l\'utilitaire d\'écriture du réseau d\'[Elmer](FEM_SolverElmer/fr.md).                                                                                                                                                                                |
| **Chemin d'accès au binaire d'ElmerGrid**                         |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
| .                                                                             |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Si cette option est cochée, FreeCAD recherchera le solveur binaire d\'[Elmer](FEM_SolverElmer/fr.md) dans les répertoires (habituels) connus.                                                                                                                                          |
| **ElmerSolver : Rechercher dans les répertoires binaires connus** |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Le chemin d\'accès au binaire du solveur d\'[Elmer](FEM_SolverElmer/fr.md).                                                                                                                                                                                                            |
| **Chemin d'accès au binaire d'ElmerSolver**                       |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Le nombre de cœurs de CPU qui seront utilisés pour effectuer la résolution. **Important :** Elmer divise le maillage en portions. Le nombre de portions est égal au nombre de cœurs de CPU utilisés. Cela peut avoir des effets secondaires :                                                  |
| **Nombre de cœurs du CPU à utiliser**                             |                                                                                                                                                                                                                                                                                                |
|                                                                            | -   En fonction de votre maillage, un plus petit nombre de cœurs de CPU peut fonctionner plus rapidement que l\'utilisation d\'un plus grand nombre de cœurs.                                                                                                                                  |
|                                                                               | -   Dans certains cas, l\'utilisation de 12 cœurs, par exemple, ne permet pas de converger, alors que 8 cœurs fonctionnent parfaitement. La raison en est qu\'à un moment donné, les portions de maillage deviennent trop petites.                                                             |
|                                                                               |                                                                                                                                                                                                                                                                                                |
|                                                                               | Il est donc souvent nécessaire d\'ajuster le nombre de cœurs, en fonction du maillage.                                                                                                                                                                                                         |
|                                                                               |                                                                                                                                                                                                                                                                                                |
|                                                                               | **Limitation connue :** pour certains types de simulation, vous devez d\'abord installer les modules Elmer pour activer le multi-threading. Consultez le rapport d\'Elmer pour obtenir des informations à ce sujet. Cas typique pour la résolution directe, il faut installer le module MUMPS. |
+++
|                                                                | Les régions de volume maillé traitées par chaque cœur de CPU seront fusionnées pour rendre les limites du volume invisibles.                                                                                                                                                                   |
| **Résultats du filtre**                                           |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Si cette case est cochée, le format binaire des résultats est utilisé. Sinon, le format ASCII est utilisé. Le format binaire peut entraîner l\'absence de résultats en raison d\'un bogue. {{Version/fr|1.1}}                                                                    |
| **Utiliser le format binaire**                                    |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Si cette option est cochée, l\'index des entités géométriques est sauvegardé dans les résultats. {{Version/fr|1.1}}                                                                                                                                                              |
| **Sauvegarder les index géométriques**                            |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++

## Mystran

<img alt="" src=images/Preferences_FEM_Page_Mystran.png  style="width:350px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                               | Description                                                                                                                                       |
+===================================================================+===================================================================================================================================================+
|                                                    | Si cette option est cochée, FreeCAD recherchera le binaire de [Mystran](FEM_SolverMystran/fr.md) dans les répertoires (habituels) connus. |
| **Rechercher dans les répertoires binaires connus**   |                                                                                                                                                   |
|                                                                |                                                                                                                                                   |
+++
|                                                    | Le chemin d\'accès au binaire de [Mystran](FEM_SolverMystran/fr.md).                                                                      |
| **Chemin d'accès au binaire de Mystran**              |                                                                                                                                                   |
|                                                                |                                                                                                                                                   |
+++
|                                                    |                                                                                                                                                   |
| **Écrire des commentaires dans les fichiers sources** |                                                                                                                                                   |
|                                                                |                                                                                                                                                   |
+++

## Z88

<img alt="" src=images/Preferences_FEM_Page_Z88.png  style="width:350px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                  | Description                                                                                                                                                                                                                                             |
+======================================================================+=========================================================================================================================================================================================================================================================+
|                                                       | Si cette option est cochée, FreeCAD recherchera le binaire nommé *z88r* du solveur [Z88](FEM_SolverZ88/fr.md) dans les répertoires (habituels) connus.                                                                                          |
| **Recherche dans les répertoires binaires connus**       |                                                                                                                                                                                                                                                         |
|                                                                   |                                                                                                                                                                                                                                                         |
+++
|                                                       | Le chemin d\'accès au binaire nommé *z88r* du [solveur Z88](FEM_SolverZ88/fr.md).                                                                                                                                                               |
| **Chemin d'accès au binaire de z88r**                    |                                                                                                                                                                                                                                                         |
|                                                                   |                                                                                                                                                                                                                                                         |
+++
|                                                       | La méthode de résolution utilisée par le [solveur Z88](FEM_SolverZ88/fr.md) pour les nouvelles simulations.                                                                                                                                     |
| **Méthode du solveur**                                   |                                                                                                                                                                                                                                                         |
|                                                                   |                                                                                                                                                                                                                                                         |
| .                                                                    |                                                                                                                                                                                                                                                         |
+++
|                                                       | Ceci est pertinent lorsque la méthode du solveur *Simple Cholesky* est utilisée. Après avoir démarré le solveur, il peut vous indiquer que vous devez augmenter la valeur *MAXGS*. Dans ce cas, augmentez les valeurs maximales et relancez le solveur. |
| **Nombre maximum de points dans une matrice de raideur** |                                                                                                                                                                                                                                                         |
|                                                                   |                                                                                                                                                                                                                                                         |
+++
|                                                       | Ceci est pertinent lorsqu\'une des méthodes de solveur itératif est utilisée. Après avoir lancé le solveur, il peut vous indiquer que vous devez augmenter la valeur *MAXKOI*. Dans ce cas, augmentez les valeurs maximales et relancez le solveur.     |
| **Taille maximale dans le vecteur de coïncidence**       |                                                                                                                                                                                                                                                         |
|                                                                   |                                                                                                                                                                                                                                                         |
+++

## Netgen

<img alt="" src=images/Preferences_FEM_Page_Netgen.png  style="width:350px;">

Sur cette page, vous pouvez spécifier les éléments suivants :

+++
| Nom                               | Description                                                                                                                                                                                                                                                                                                                                                          |
+===================================+======================================================================================================================================================================================================================================================================================================================================================================+
|                    | Si cette option est cochée, l\'ancienne implémentation [Netgen](FEM_MeshNetgenFromShape/fr.md) est utilisée par FEM. Cela peut être nécessaire pour les utilisateurs (en général les vieux ordinateurs et Windows) qui ne peuvent pas installer les extensions Python de Netgen nécessaires à la nouvelle implémentation. ({{Version/fr|1.0}}) |
| **Netgen historique** |                                                                                                                                                                                                                                                                                                                                                                      |
|                                |                                                                                                                                                                                                                                                                                                                                                                      |
+++





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [FEM](Category_FEM.md) > FEM Preferences/fr
