---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM MeshBoundaryLayer
   Name/fr: FEM Couche limite de maillage FEM
   MenuLocation: Maillage , Créer une couche limite de maillage
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: Tous
}}
---

# FEM MeshBoundaryLayer/fr

## Description

La commande **FEM Couche limite de maillage** permet à l\'utilisateur de définir un jeu donné de paramètres de maillage en sélectionnant un ensemble d\'éléments (sommet, arête, face) et en lui appliquant des paramètres.

Elle est particulièrement utile pour mailler plus finement à proximité des bords ou des surfaces dans les simulations d\'écoulement. Par exemple, elle peut être utilisée pour mailler plus finement à proximité d\'un profil aérodynamique ou d\'un obstacle dans un écoulement.

La couche limite présente l\'avantage de créer des maillages anisotropes hautement définis. Comme son nom l\'indique, elle permet d\'effectuer des calculs précis aux frontières, par exemple une paroi où se produit un frottement, générant un gradient de vitesse.



## Utilisation

1.  Pour activer la fonction, un maillage doit d\'abord être fourni par <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [FEM Mailler avec Gmsh](FEM_MeshGmshFromShape/fr.md).
    -   Sélectionnez l\'objet Mesh dans l\'arborescence du modèle et cliquez sur le bouton **<img src="images/FEM_MeshBoundaryLayer.svg" width=32px> [Créer une couche limite de maillage](FEM_MeshBoundaryLayer/fr.md)**.
    -   Sélectionnez l\'objet Mesh dans l\'arborescence du modèle et sélectionnez l\'option **Maillage → <img src="images/FEM_MeshBoundaryLayer.svg" width=32px> Créer une couche limite de maillage** du menu.
2.  Modifiez la taille de l\'élément de départ, le taux de croissance et le nombre de couches de croissance.
3.  Sélectionnez un sommet, une arête, une face.
4.  Cliquez sur le bouton **OK**.
5.  Fermez la tâche.

    :   Résultat : vous devriez maintenant voir un nouvel objet `FEMMeshBoundaryLayer` sous l\'objet `FEMMeshGMSH` (voir l\'exemple 3 ci-dessous) dans votre conteneur d\'analyse actif.
6.  Double-cliquez sur l\'objet parent `FEMMeshGMSH` dans votre arbre de modèle et appuyez sur **Appliquer** pour forcer un recalcul de maillage.
7.  Fermez la tâche.

Une fois que le maillage a été créé, vous pouvez modifier ses propriétés à l\'aide de l\'[éditeur de propriétés](Property_editor/fr.md). Après avoir modifié une propriété, vous devez rouvrir la fenêtre de dialogue Gmsh et cliquer sur le bouton **Appliquer**. (Vous pouvez laisser la fenêtre de dialogue ouverte pendant la modification des propriétés).

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



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshBoundaryLayer/fr
