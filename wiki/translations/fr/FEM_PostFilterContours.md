---
 GuiCommand:
   Name: FEM PostFilterContours
   Name/fr: FEM Filtre par contours
   MenuLocation: Résultats , Filtre par contours
   Workbenches: FEM_Workbench/fr
   Version: 0.21
   SeeAlso: FEM_PostPipelineFromResult/fr, FEM_PostCreateFunctions/fr, FEM_tutorial/fr
---

# FEM PostFilterContours/fr

## Description

Crée des iso-contours et des iso-lignes dans le maillage des résultats.

<img alt="" src=images/FEM_PostFilterContours_Example.png  style="width:400px;"> 
*Iso-contours, décrivant la composante y de l'induction magnétique absolue dans et autour<br>d'un fil de cuivre traversé par un courant électrique à une fréquence de 100 kHz.<br>
Pour plus d'informations sur ce modèle, consultez la section 14 des [https://www.nic.funet.fi/index/elmer/doc/ElmerTutorials.pdf tutoriels d'Elmer].*



## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) déjà créé.
2.  Créez le filtre soit en appuyant sur le bouton **<img src="images/FEM_PostFilterContours.svg" width=16px> '''Filtre par contours'''** ou en utilisant le menu **Résultats → <img src="images/FEM_PostFilterContours.svg" width=16px> Filtre par contours**.
3.  Ajustez les **Options d'affichage des résultats** comme pour le [pipeline de résultats](FEM_PostPipelineFromResult/fr.md). Vous devrez peut-être cacher le pipeline pour voir l\'effet du filtre dans l\'aperçu.
4.  Dans la fenêtre de dialogue qui apparaît, définissez le champ du résultat et le nombre de contours.
5.  Cliquez sur le bouton **OK** pour terminer la commande.

## Options

La fenêtre de dialogue propose les paramètres suivants :

-   **Champ** : le champ de résultats à dessiner.
-   **Vecteur** : si le **Champ** est un vecteur, les composantes du vecteur.
-   **Nombre de contours** : nombre de contours à créer. Remarque : selon la géométrie, le nombre de contours créés peut être supérieur à celui spécifié. Ceci est dû à l\'algorithme de création. Cependant, pour les géométries 2D et 3D simples, le nombre devrait être correct.
-   **Lissage** : si cette option est cochée, le filtre de lissage Laplacien est appliqué au filtre Contours pour rendre les isosurfaces moins grossières. {{Version/fr|1.1}}
-   **Facteur de relaxation** : contrôle le niveau de lissage via la quantité de déplacement des sommets (si le lissage est activé). {{Version/fr|1.1}}
-   **Pas de couleur** : ne pas appliquer de couleur aux contours.

**Remarque** : un **champ** ne peut être défini que si une fonction de filtre existe et a été appliquée avec <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:16px;"> [Appliquer les modifications](FEM_PostApplyChanges/fr.md). Vous pouvez également rouvrir la boîte de dialogue du filtre.



## Information sur la taille du fichier 

La mise en place d\'un filtre par contours peut augmenter la taille du fichier de manière significative. La raison en est que l\'algorithme doit copier le [pipeline des résultats](FEM_PostPipelineFromResult/fr.md). Un seul contour ne nécessite pas le maillage entier et l\'algorithme n\'a besoin que de la moitié de la taille de stockage du pipeline pour créer un contour. Mais la taille augmentera pour chaque contour. Prenons par exemple le cas où la taille de stockage du pipeline est de 1 Mo, l\'ajout d\'un filtre par contours avec 10 contours entraînera une augmentation de la taille du fichier de 5 Mo.

La taille de stockage du pipeline dépend du maillage utilisé. Plus le maillage est fin, plus la taille du pipeline est importante. Soyez donc prudent si vous avez de grandes mailles et un grand nombre de contours.

Si vous n\'utilisez les contours que sur une partie du maillage, par exemple lorsque vous avez un filtre d\'écrêtage, alors créez le filtre pa contours sur le filtre et non sur le pipeline. Si vous avez besoin de l\'ensemble du pipeline, commencez par quelques contours, puis augmentez progressivement jusqu\'à ce que la taille du fichier reste acceptable et que la visualisation soit telle que vous la souhaitez.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterContours/fr
