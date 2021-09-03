---
- GuiCommand:/fr
   Name:PartDesign MoveFeatureInTree
   Name/fr:PartDesign Déplacer après un autre objet
   MenuLocation:Menu contextuel → Déplacer après un autre objet
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Désigner comme fonction résultante](PartDesign_MoveTip/fr.md), [PartDesign Déplacer vers un autre corps de pièce](PartDesign_MoveFeature/fr.md)
---

## Description

<img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:24px;"> [Déplacer après un autre objet](PartDesign_MoveFeatureInTree/fr.md), comme cette commande est étiquetée dans le menu contextuel, elle permet de réorganiser les objets sous un Corps. Les esquisses, la géométrie de référence et les fonctionnalités sont prises en charge.

## Utilisation

1.  Dans l\'arborescence du modèle, sélectionner l\'objet ou les objets à déplacer, puis faire un clic-droit pour ouvrir le menu contextuel.
2.  Sélectionner **Déplacer après un autre objet**.
3.  Dans la boîte de dialogue **Sélectionner la fonction**, sélectionner l\'objet sous lequel déplacer l\'objet ou les objets.
4.  Appuyez sur **OK**.

## Exemple

Les trois images ci-dessous montrent le même modèle avec une cavité définie par une esquisse appliquée sur un plan de référence. Les fonctions sont réordonnées d\'une image à l\'autre. Ceci a pour effet que la cavité soit ne perce aucun trou, ou perce des trous dans plusieurs protrusions, dépendant de l\'ordre des fonctions dans l\'arborescence Modèle.

![](images/PD_move_feature0.png ) ![](images/Hole_Pad002.png ) ![](images/PD_move_feature2.png )





{{PartDesign Tools navi

}} 
