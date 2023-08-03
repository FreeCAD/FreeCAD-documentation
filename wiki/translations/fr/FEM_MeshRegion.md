---
 GuiCommand:
   Name: FEM MeshRegion
   Name/fr: FEM Région de maillage FEM
   MenuLocation: Maillage , Région de maillage FEM
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM MeshRegion/fr

## Description

FEM Région de maillage FEM permet à l\'utilisateur de définir un ensemble localisé de paramètres de maillage en sélectionnant un ensemble d\'éléments (Vertex-points, Edge-arêtes, Face) et en lui appliquant les paramètres. Cette fonction est particulièrement utile pour affiner les maillages dans les zones d\'intérêt ou les zones où le solveur générera un gradient plus fort d\'une variable. Par exemple, elle peut être utilisée pour raffiner le maillage autour des points de contrainte (arêtes vives, cercles\...) en analyse mécanique, ou aux zones de contraction dans un écoulement de fluide.

L\'affinage du maillage présente l\'avantage de permettre une simulation précise là où c\'est nécessaire, tout en autorisant un maillage plus grossier dans le domaine plus large, ce qui permet d\'optimiser considérablement le temps de calcul tout en conservant des solutions significatives en sortie.



## Utilisation

1.  Pour activer la fonction, un maillage doit d\'abord être fourni <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM Maillage FEM à partir d\'une forme de Gmsh](FEM_MeshGmshFromShape/fr.md).
    -   Sélectionnez l\'objet Mesh dans l\'arbre du modèle et cliquez sur le bouton <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;">.
    -   Sélectionnez l\'objet Mesh dans l\'arbre du modèle et sélectionnez l\'option **Maillage →  <img src="images/FEM_MeshRegion.svg" width=32px> Région de maillage FEM** dans le menu.
2.  Modifiez la taille maximale des éléments pour la région.
3.  Cliquez sur le bouton **OK**.
4.  Fermez la tâche.
5.  Résultat : vous devriez maintenant voir un nouvel objet `FEMMeshRegion` sous l\'objet `FEMMeshGMSH` (voir exemple #3 ci-dessous) dans votre conteneur d\'analyse actif.
6.  Double-cliquez sur l\'objet parent `FEMMeshGMSH` dans votre arborescence de modèle et appuyez sur **Appliquer** pour forcer un recalcul de maillage.
7.  Fermez la tâche.

Une fois que le maillage a été créé, vous pouvez modifier ses propriétés à l\'aide de l\'[Éditeur de propriétés](Property_editor/fr.md). Après avoir modifié une propriété, vous devez rouvrir le dialogue Gmsh et cliquer sur le bouton **Appliquer**. (Vous pouvez laisser la boîte de dialogue ouverte pendant la modification des propriétés).

Vous pouvez créer autant de maillages différents que nécessaire.



## Exemples visuels 

<img alt="" src=images/FEMMeshRegion_Example1.png style="width:300px;"> 
*Exemple 1 : le maillage FEM grossier initial par GMSH*

<img alt="" src=images/FEMMeshRegion_Example2.png  style="width:300px;"> 
*Exemple 2 : après application d'un raffinement du maillage à l'aide de deux régions de maillage FEM, le grand trou est affiné jusqu'à une taille d'élément maximale de 3 mm, le petit trou est affiné jusqu'à 1 mm*

<img alt="" src=images/FEMMeshRegion_Example3.png  style="width:300px;"> 
*Exemple 3 : un exemple simple de la vue en arborescence résultante*



## Remarques

L\'ordre dans lequel les régions sont affichées dans la [vue en arborescence](Tree_view/fr.md) peut modifier le résultat du maillage. Voir ce [fil de forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=41955)



## En relation 

-   \"Mesh Regions for a Better Analysis\" - Tutoriel vidéo par Joko Engineering ([lien](https://www.youtube.com/watch?v=X5RVe2SDPvw))





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshRegion/fr
