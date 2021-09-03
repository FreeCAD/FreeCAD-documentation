---
- GuiCommand:/fr
   Name:Path DressupDogbone
   Name/fr:Path Usinage des angles
   MenuLocation:Path → Path Dressup → Dogbone Dress-up
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Balise d'attache](Path_DressupTag/fr.md), [Path Rampe d'entrée](Path_DressupRampEntry/fr.md), [Path Parcours de couteau](Path_DressupDragKnife/fr.md)
---


</div>

## Description

Cet outil permet de rajouter des sur-découpes dans le cas d\'angles intérieurs d\'un profil ou pour la decoupe de coins. Une fraise cylindrique ne peut pas usiner un coin aigu sans entrer en collision avec le modèle. Dans certains cas, il peut être préférable de violer le modèle et de s\'assurer que le matériau du coin est enlevé. Ceci est particulièrement nécessaire si les pièces se croisent/s\'imbriquent les unes avec les autres.

## Utilisation

1.  Sélectionner un objet contour ou profil [Path](Path_Workbench/fr.md)
2.  Cliquez sur l\'élément de menu <img alt="" src=images/Path_DressupDogbone.svg  style="width:24px;"> [Dégagement des angles](Path_DressupDogbone/fr.md) ou 
**Path** → **Path Dressup** → **<img src="images/Path_DressupDogbone.svg" width=24px> [Dégagement des angles](Path_DressupDogbone/fr.md)**

## Options

-   Side - Côté du tracé où la modification sera ajoutée.
-   Style - Style de surcoupe (Dogbone, T-Bone Horizontal, T-Bone Vertical, T-Bone Short Edge).
-   Incision - L\'algorithme à utiliser pour calculer la longueur de la sur-dépouille.
-   Custom - Si Incision est personnalisé, la propriété personnalisée est utilisée pour définir la longueur.

## Limitations


<div class="mw-translate-fuzzy">

## Limitations {#limitations_1}

Pour déterminer le tracé de correction des coins, il faut un segment droit (G1) avant et après le coin où la correction doit être insérée.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}} 
