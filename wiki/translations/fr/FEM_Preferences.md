# FEM Preferences/fr
La fenêtre des préférences de l\'[atelier FEM](FEM_Workbench/fr.md) se trouve dans l\'[Éditeur de préférences](Preferences_Editor/fr.md), **Édition → Préférences → FEM**.

Il y a plusieurs onglets dans les préférences de l\'atelier FEM, en commençant par la configuration **Générale** de l\'atelier. Le reste des onglets contrôle la façon dont FEM interagit avec les solveurs externes supportés.

Les solveurs externes actuellement acceptés sont :

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [CalculiX](FEM_SolverCalculixCxxtools/fr.md)
-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/fr.md)
-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Mystran](FEM_SolverMystran/fr.md) ({{Version/fr|0.20}})
-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Z88](FEM_SolverZ88/fr.md)



## Général

Dans l\'onglet *Général*, vous pouvez spécifier les éléments suivants:

+++
| Nom                                                                                              | Description                                                                                                                                         |
+==================================================================================================+=====================================================================================================================================================+
|                                                                                   | Répertoire dans lequel les fichiers de maillage et de solveur doivent être stockés                                                                  |
| **Répertoire de travail**                                                            |                                                                                                                                                     |
|                                                                                               |                                                                                                                                                     |
+++
|                                                                                   | S\'il y a plusieurs maillages, ils seront regroupés                                                                                                 |
| **Créer des groupes de maillage**                                                    |                                                                                                                                                     |
|                                                                                               |                                                                                                                                                     |
+++
|                                                                                   | Les [objets Résultats](FEM_ResultShow/fr.md) existants seront conservés, sinon ils seront écrasés par une nouvelle exécution du solveur.    |
| **Conserver les résultats lors d'une nouvelle exécution du calcul**                  |                                                                                                                                                     |
|                                                                                               |                                                                                                                                                     |
+++
|                                                                                   | Si coché, la boîte de dialogue [Afficher le résultat](FEM_ResultShow/fr.md) est ouverte avec les derniers paramètres utilisés.              |
| **Restaurer les paramètres de la boîte de dialogue des résultats**                   |                                                                                                                                                     |
|                                                                                               |                                                                                                                                                     |
+++
|                                                                                   | Les contraintes seront cachées dans la vue du modèle lorsque la boîte de dialogue [Afficher le résultat](FEM_ResultShow/fr.md) est ouverte. |
| **Cacher les contraintes lors de l'ouverture de la boîte de dialogue des résultats** |                                                                                                                                                     |
|                                                                                               |                                                                                                                                                     |
+++
|                                                                                   | Le solveur par défaut à ajouter lors de l\'ajout d\'un [conteneur d\'analyse](FEM_Analysis/fr.md) ({{Version/fr|0.21}}).      |
| **Solveur par défaut**                                                               |                                                                                                                                                     |
|                                                                                               |                                                                                                                                                     |
+++

![](images/Preference_Fem_Tab_01.png )

## Gmsh

Dans l\'onglet *Gmsh*, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                             | Description                                                                                                                                   |
+=================================================================+===============================================================================================================================================+
|                                                  | Si cette case est cochée, FreeCAD cherchera le binaire de [Gmsh](FEM_MeshGmshFromShape/fr.md) dans les répertoires (habituels) connus |
| **Rechercher dans les répertoires binaires connus** |                                                                                                                                               |
|                                                              |                                                                                                                                               |
+++
|                                                  | Le chemin vers le binaire de [Gmsh](FEM_MeshGmshFromShape/fr.md).                                                                     |
| **Chemin binaire de Gmsh**                          |                                                                                                                                               |
|                                                              |                                                                                                                                               |
+++

![](images/Preference_Fem_Tab_03.png )

## CalculiX

Dans l\'onglet *CalculiX*, vous pouvez spécifier les éléments suivants :

![](images/Preference_Fem_Tab_02.png )

## Elmer

Dans l\'onglet *Elmer*, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                           | Description                                                                                                                                                                                                                                                                                    |
+===============================================================================+================================================================================================================================================================================================================================================================================================+
|                                                                | Si cette option est cochée, FreeCAD recherchera le binaire de l\'utilitaire d\'écriture du réseau d\'[Elmer](FEM_SolverElmer.md) dans les répertoires (habituels) connus.                                                                                                              |
| **ElmerGrid : Rechercher dans les répertoires binaires connus**   |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Le chemin vers le binaire de l\'utilitaire d\'écriture du réseau d\'[Elmer](FEM_SolverElmer/fr.md).                                                                                                                                                                                    |
| **Chemin du binaire d'ElmerGrid**                                 |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
| .                                                                             |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Si cette option est cochée, FreeCAD recherchera le solveur binaire d\'[Elmer](FEM_SolverElmer/fr.md) dans les répertoires (habituels) connus.                                                                                                                                          |
| **ElmerSolver : Rechercher dans les répertoires binaires connus** |                                                                                                                                                                                                                                                                                                |
|                                                                            |                                                                                                                                                                                                                                                                                                |
+++
|                                                                | Le chemin vers le binaire du solveur d\'[Elmer](FEM_SolverElmer/fr.md).                                                                                                                                                                                                                |
| **Chemin du binaire d'ElmerSolver**                               |                                                                                                                                                                                                                                                                                                |
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

![](images/Preference_Fem_Tab_05.png )

## Mystran

Dans l\'onglet *Mystran*, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                             | Description                                                                                                                                       |
+=================================================================+===================================================================================================================================================+
|                                                  | Si cette option est cochée, FreeCAD recherchera le binaire de [Mystran](FEM_SolverMystran/fr.md) dans les répertoires (habituels) connus. |
| **Rechercher dans les répertoires binaires connus** |                                                                                                                                                   |
|                                                              |                                                                                                                                                   |
+++
|                                                  | Le chemin vers le binaire de [Mystran](FEM_SolverMystran/fr.md).                                                                          |
| **Chemin du binaire de Mystran**                    |                                                                                                                                                   |
|                                                              |                                                                                                                                                   |
+++

![](images/Preference_Fem_Tab_Mystran.png )

## Z88

Dans l\'onglet *Z88*, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                              | Description                                                                                                                                                                                                                                             |
+==================================================================+=========================================================================================================================================================================================================================================================+
|                                                   | Si cette option est cochée, FreeCAD recherchera le binaire nommé *z88r* du solveur [Z88](FEM_SolverZ88/fr.md) dans les répertoires (habituels) connus.                                                                                          |
| **Recherche dans les répertoires binaires connus**   |                                                                                                                                                                                                                                                         |
|                                                               |                                                                                                                                                                                                                                                         |
+++
|                                                   | Le chemin vers le binaire nommé *z88r* du [solveur Z88](FEM_SolverZ88/fr.md).                                                                                                                                                                   |
| **Chemin du binaire de z88r**                        |                                                                                                                                                                                                                                                         |
|                                                               |                                                                                                                                                                                                                                                         |
+++
|                                                   | La méthode de résolution utilisée par le [solveur Z88](FEM_SolverZ88/fr.md) pour les nouvelles simulations.                                                                                                                                     |
| **Méthode du solveur**                               |                                                                                                                                                                                                                                                         |
|                                                               |                                                                                                                                                                                                                                                         |
| .                                                                |                                                                                                                                                                                                                                                         |
+++
|                                                   | Ceci est pertinent lorsque la méthode du solveur *Simple Cholesky* est utilisée. Après avoir démarré le solveur, il peut vous indiquer que vous devez augmenter la valeur *MAXGS*. Dans ce cas, augmentez les valeurs maximales et relancez le solveur. |
| **Valeurs maximales dans la matrice de rigidité**    |                                                                                                                                                                                                                                                         |
|                                                               |                                                                                                                                                                                                                                                         |
+++
|                                                   | Ceci est pertinent lorsqu\'une des méthodes de solveur itératif est utilisée. Après avoir lancé le solveur, il peut vous indiquer que vous devez augmenter la valeur *MAXKOI*. Dans ce cas, augmentez les valeurs maximales et relancez le solveur.     |
| **Valeurs maximales dans le vecteur de coïncidence** |                                                                                                                                                                                                                                                         |
|                                                               |                                                                                                                                                                                                                                                         |
+++

![](images/Preference_Fem_Tab_04.png )



## Matériau

Dans l\'onglet *Matériau*, vous pouvez spécifier les éléments suivants :

+++
| Nom                                                                                                                     | Description                                                                                                                                                                                                         |
+=========================================================================================================================+=====================================================================================================================================================================================================================+
|                                                                                                          | Les cartes intégrées à FreeCAD seront listées comme disponibles.                                                                                                                                                    |
| **Utiliser les matériaux intégrés**                                                                         |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
| .                                                                                                                       |                                                                                                                                                                                                                     |
+++
| \\AppData\\Roaming\\FreeCAD\\Material*. |
| **Utiliser les matériaux du répertoire Matériaux du répertoire de préférences de FreeCAD de l'utilisateur** |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
+++
|                                                                                                          | Les jeux de paramètres de matériaux provenant également du répertoire spécifié seront répertoriées comme disponibles.                                                                                               |
| **Utiliser les matériaux du répertoire défini par l'utilisateur**                                           |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
+++
|                                                                                                          | Les jeux de paramètres en double seront supprimées de la liste des jeux de paramètres de matériaux affichée.                                                                                                        |
| **Supprimer les doublons de jeu de paramètres**                                                             |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
+++
|                                                                                                          | Les jeux de paramètres de matériaux apparaîtront triées par leurs ressources (emplacements). Si cette option n\'est pas cochée, elles seront triées par leur nom.                                                   |
| **Trier par ressources**                                                                                    |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
| .                                                                                                                       |                                                                                                                                                                                                                     |
+++

![](images/Preference_Fem_Tab_Material.png )


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [FEM](Category_FEM.md) > FEM Preferences/fr
