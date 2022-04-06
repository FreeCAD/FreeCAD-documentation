# FEM Preferences/fr
{{TOCright}} La fenêtre des préférences de l\'[atelier FEM](FEM_Workbench/fr.md) se trouve dans l\'[Éditeur de préférences](Preferences_Editor/fr.md), **Édition → Préférences → FEM**.

Il y a plusieurs onglets dans les préférences de l\'atelier FEM, en commençant par la configuration **Générale** de l\'atelier. Le reste des onglets contrôle la façon dont FEM interagit avec les solveurs externes supportés.

Les solveurs externes actuellement acceptés sont :

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [CalculiX](FEM_SolverCalculixCxxtools/fr.md)
-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/fr.md)
-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Mystran](FEM_SolverMystran/fr.md) {{Version/fr|0.20}}
-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Z88](FEM_SolverZ88/fr.md)

## Général

Dans l\'onglet *Général*, vous pouvez spécifier les éléments suivants:

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
| Nom                                                                           | Description                                                                                                                                                                       |
+===============================================================================+===================================================================================================================================================================================+
|                                                                | Si cette option est cochée, FreeCAD recherchera le binaire de l\'utilitaire d\'écriture du réseau d\'[Elmer](FEM_SolverElmer.md) dans les répertoires (habituels) connus. |
| **ElmerGrid : Rechercher dans les répertoires binaires connus**   |                                                                                                                                                                                   |
|                                                                            |                                                                                                                                                                                   |
+++
|                                                                | Le chemin vers le binaire de l\'utilitaire d\'écriture du réseau d\'[Elmer](FEM_SolverElmer/fr.md).                                                                       |
| **Chemin du binaire d'ElmerGrid**                                 |                                                                                                                                                                                   |
|                                                                            |                                                                                                                                                                                   |
| .                                                                             |                                                                                                                                                                                   |
+++
|                                                                | Si cette option est cochée, FreeCAD recherchera le solveur binaire d\'[Elmer](FEM_SolverElmer/fr.md) dans les répertoires (habituels) connus.                             |
| **ElmerSolver : Rechercher dans les répertoires binaires connus** |                                                                                                                                                                                   |
|                                                                            |                                                                                                                                                                                   |
+++
|                                                                | Le chemin vers le binaire du solveur d\'[Elmer](FEM_SolverElmer/fr.md).                                                                                                   |
| **Chemin du binaire d'ElmerSolver**                               |                                                                                                                                                                                   |
|                                                                            |                                                                                                                                                                                   |
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
|                                                                                                          | Les cartes de matériaux provenant également du répertoire spécifié seront répertoriées comme disponibles.                                                                                                           |
| **Utiliser les matériaux du répertoire défini par l'utilisateur**                                           |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
+++
|                                                                                                          | Les cartes en double seront supprimées de la liste des cartes de matériaux affichée.                                                                                                                                |
| **Supprimer les doublons de cartes**                                                                        |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
+++
|                                                                                                          | Les cartes de matériaux apparaîtront triées par leurs ressources (emplacements). Si cette option n\'est pas cochée, elles seront triées par leur nom.                                                               |
| **Trier par ressources**                                                                                    |                                                                                                                                                                                                                     |
|                                                                                                                      |                                                                                                                                                                                                                     |
| .                                                                                                                       |                                                                                                                                                                                                                     |
+++

![](images/Preference_Fem_Tab_Material.png )


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [FEM](Category_FEM.md) > FEM Preferences/fr
