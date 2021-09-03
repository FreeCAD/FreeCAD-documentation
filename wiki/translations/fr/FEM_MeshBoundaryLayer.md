---
- GuiCommand:/fr
   Name:FEM MeshBoundaryLayer
   Name/fr:FEM Couche limite de maillage MEF
   MenuLocation:Mesh → Couche limite de maillage MEF
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

## Description

Couche limite de maillage MEF permet à l\'utilisateur de définir un ensemble localisé de paramètres de maillage en sélectionnant un ensemble d\'éléments (Vertex, Edge, Face) et en lui appliquant les paramètres. Elle est particulièrement utile pour affiner les maillages près des bords ou des surfaces dans les simulations d\'écoulement. Par exemple, elle peut être utilisée pour raffiner le maillage à proximité d\'une feuille d\'air ou d\'un obstacle dans un écoulement.

La couche limite présente l\'avantage de créer des maillages anisotropes hautement définis. Comme son nom l\'indique, elle permet d\'effectuer des calculs précis près des frontières, par exemple une paroi où se produit un frottement, générant un gradient de vitesse.

## Utilisation

1.  Pour activer la fonction, un maillage doit d\'abord être fourni <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM Maillage MEF à partir d\'une forme avec Gmsh](FEM_MeshGmshFromShape/fr.md).
    -   Sélectionnez l\'objet Mesh dans l\'arbre du modèle et cliquez sur le bouton <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;">.
    -   Sélectionnez l\'objet Mesh dans l\'arborescence du modèle et sélectionnez l\'option **Mesh → <img src="images/FEM_MeshBoundaryLayer.svg" width=32px> Couche limite de maillage FEM** dans le menu.
2.  Modifiez la taille de l\'élément de départ, le taux de croissance et le nombre de couches de croissance.
3.  Sélectionnez un sommet, une arête, une face.
4.  Cliquez sur le bouton **OK**.
5.  Fermez la tâche.

    :   Résultat : Vous devriez maintenant voir un nouvel objet `FEMMeshBoundaryLayer` sous l\'objet `FEMMeshGMSH` (voir l\'exemple 3 ci-dessous) dans votre conteneur d\'analyse actif.
6.  Double-cliquez sur l\'objet parent `FEMMeshGMSH` dans votre arbre de modèle et appuyez sur **Appliquer** pour forcer un recalcul de maillage.
7.  Fermez la tâche.

Une fois que le maillage a été créé, vous pouvez modifier ses propriétés à l\'aide de l\'[Éditeur de propriétés](Property_editor/fr.md). Après avoir modifié une propriété, vous devez rouvrir le dialogue Gmsh et cliquer sur le bouton **Appliquer**. (Vous pouvez laisser la boîte de dialogue ouverte pendant la modification des propriétés).

Vous pouvez créer autant de couches limites de maillage différentes que nécessaire.

## Exemples visuels 

<img alt="" src=images/FEMMeshBoundaryLayer_Example1.png.png  style="width:300px;"> 
*Exemple 1 : le maillage grossier initial de FEMMeshGMSH sur un cas 2D*

<img alt="" src=images/FEMMeshBoundaryLayer_Example2.png.png  style="width:300px;"> 
*Exemple 2 : après l'application d'une couche limite de maillage*

<img alt="" src=images/FEMMeshBoundaryLayer_Example3.png.png  style="width:300px;"> 
*Exemple 3 : un exemple simple de l'arborescence résultante*

## Remarques

## En relation 





{{FEM Tools navi

}}  
