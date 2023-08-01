---
- GuiCommand:
   Name:Part ExplodeCompound
   Name/fr:Part Éclater le composé
   MenuLocation:Part - Composés - Éclater le composé
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.18
   SeeAlso:[Part Composé](Part_Compound/fr.md), [Draft Désagréger](Draft_Downgrade/fr.md)
---

# Part ExplodeCompound/fr

## Description

Outil permettant de fractionner des composés de formes afin de rendre chaque forme contenue (enfant) disponible en tant qu'objet distinct dans l'arborescence du modèle. Les enfants sont automatiquement placés dans un [Groupe](Std_Group/fr.md) s\'il y a plus d\'un enfant.

Il est semi-paramétrique: les formes des enfants seront mises à jour à mesure que le composé source change, mais si le nombre d\'enfants dans le composé est modifié, il manquera certaines formes dans l\'explosion ou des objets redondants seront en état d\'erreur.

Les emplacements des formes extraites suivent les emplacements des originaux, plus la propriété Placement de chaque enfant.

L\'outil fera également exploser des formes non composées dans leurs constituants de niveau inférieur: composé solide en solides, solides en coquilles, coquilles en faces, faces en fils, fils en arêtes, arêtes en arêtes en sommets.

## Utilisation

1.  Lancez l\'outil Part Éclater le composé de plusieurs manières :
    -   En appuyant sur le bouton <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> dans la barre d\'outils Part
    -   Utilisation de l\'entrée **Part → Composés → Éclater le composé** dans le menu Part

## Cas d\'utilisation 

-   Ajustement des positions des formes faites par <img alt="" src=images/Draft_OrthoArray.svg  style="width:24px;"> [Draft Réseau orthogonal](Draft_OrthoArray/fr.md).
-   Obtention de pièces séparées à partir du résultat de <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part Scinder](Part_Slice/fr.md) et <img alt="" src=images/Part_Cut.svg  style="width:24px;"> [Part Couper](Part_Cut/fr.md).
-   Obtention des contours individuels à partir d\'esquisses et de faces à contours multiples.
-   Obtention d\'un solide pur à partir d\'un solide en composé pour une utilisation dans l\'<img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [atelier FEM](FEM_Workbench/fr.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/fr
