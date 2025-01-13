---
 GuiCommand:
   Name: Part ExplodeCompound
   Name/fr: Part Éclater le composé
   MenuLocation: Part , Composés , Éclater le composé
   Workbenches: Part_Workbench/fr
   Version: 0.18
   SeeAlso: Part_Compound/fr, Draft_Downgrade/fr
---

# Part ExplodeCompound/fr

## Description

L\'outil <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> **Part Éclater le composé** fractionne un composé de formes afin de rendre chaque forme contenue (enfant) disponible en tant qu'objet distinct dans l'arborescence du modèle. Les enfants sont automatiquement placés dans un [groupe](Std_Group/fr.md) s\'il y a plus d\'un enfant.

Il est semi-paramétrique : les formes des enfants seront mises à jour à mesure que le composé source change, mais si le nombre d\'enfants dans le composé est modifié, l\'éclaté sera soit dépourvu de certaines formes, soit comportera des objets redondants dans un état d\'erreur.

Les emplacements des formes extraites suivent les emplacements des originaux, plus la propriété Placement de chaque enfant.

L\'outil fera également exploser des formes non composées dans leurs constituants de niveau inférieur: composé solide en solides, solides en coquilles, coquilles en faces, faces en fils, fils en arêtes, arêtes en arêtes en sommets.



## Utilisation

1.  Sélectionnez un seul composé.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Part_ExplodeCompound.svg" width=16px> [Éclater le composé](Part_ExplodeCompound/fr.md)**.
    -   Sélectionnez l\'option **Part → Composés → <img src="images/Part_ExplodeCompound.svg" width=16px> Éclater le composé** du menu.



## Cas d\'utilisation 

-   Ajustement des positions des formes faites par <img alt="" src=images/Draft_OrthoArray.svg  style="width:16px;"> [Draft Réseau orthogonal](Draft_OrthoArray/fr.md).
-   Obtention de pièces séparées à partir du résultat de <img alt="" src=images/Part_Slice.svg  style="width:16px;"> [Part Scinder](Part_Slice/fr.md) et <img alt="" src=images/Part_Cut.svg  style="width:16px;"> [Part Couper](Part_Cut/fr.md).
-   Obtention des contours individuels à partir d\'esquisses et de faces à contours multiples.
-   Obtention d\'un solide pur à partir d\'un solide en composé pour une utilisation dans l\'<img alt="" src=images/Workbench_FEM.svg  style="width:16px;"> [atelier FEM](FEM_Workbench/fr.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/fr
