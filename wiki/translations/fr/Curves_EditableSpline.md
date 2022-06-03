---
- GuiCommand   */fr
   Name   *Curves EditableSpline
   Name/fr   *Curves Modifier une B-spline
   MenuLocation   *Curves → Freehand BSpline
   Workbenches   *[Curves](Curves_Workbench/fr.md)
---

# Curves EditableSpline/fr

## Description

<img alt="" src=images/Curves_EditableSpline.svg  style="width   *24px;"> [Curves Modifier une B-spline](Curves_EditableSpline/fr.md) crée une courbe B-spline à main levée. Cet outil fait partie des [ateliers externes](External_workbenches/fr.md) appelé [Curves](Curves_Workbench/fr.md).

## Utilisation

1.  Passer à l\'atelier <img alt="" src=images/Curves_workbench_icon.svg  style="width   *24px;"> [Curves](Curves_Workbench/fr.md) (à installer à partir du <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) si ce n\'est pas déjà fait)
2.  Pour appeler la commande, effectuez l\'une des opérations suivantes   *
    -   Appuyez sur le bouton <img alt="" src=images/Curves_EditableSpline.svg  style="width   *24px;"> dans la barre d\'outils Curves.
    -   Utilisez l\'entrée **Curves → Freehand BSpline** dans le menu déroulant.

## Options

Pendant la commande, un mode d\'édition spécial est actif et il y a plusieurs actions et comportements qui peuvent être contrôlés par des touches et des clics de souris.

-   Pour déplacer un sommet ou une ligne de guidage (les lignes de guidage sont les lignes droites entre les sommets), maintenez le bouton gauche de la souris enfoncé et déplacez la souris.
-   La touche **A** sélectionne ou désélectionne tous les sommets et lignes de guidage.
-   La touche **I** ajoute un sommet au segment appartenant à la ligne de guidage sélectionnée. Le nouveau sommet sera sélectionné.
-   La touche **T** active ou désactive le mode tangent pour les sommets ou lignes de guidage sélectionnés (par rapport à la direction de la vue).
-   La touche **P** aligne les objets sélectionnés.
-   La touche **S** peut être utilisée pour accrocher un sommet à un sommet appartenant à une autre B-spline. Un sommet de la courbe B-spline en cours d\'édition étant sélectionné, maintenez la touche **Ctrl** enfoncée et ajoutez le sommet cible à la sélection, puis appuyez sur la touche **S**. Les sommets sont accrochés ensemble.
-   Pour désassembler les sommets, sélectionnez la paire de sommets assemblés et appuyez à nouveau sur la touche **S**. Le sommet de la courbe B-spline en cours d\'édition reste sélectionné et peut maintenant être déplacé.
-   La touche **L** active ou désactive l\'interpolation linéaire.
-   Les touches **X**, **Y** ou **Z** peuvent être utilisées pour contraindre le mouvement de l\'objet que l\'on fait glisser. Tout en faisant glisser l\'objet, appuyez sur la touche de l\'axe souhaité. Appuyez à nouveau sur la même touche pour désactiver la contrainte.
-   La touche **Q** termine la commande et quitte le mode d\'édition.

## Limitations

## Propriétés

## Script





{{Curves Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves EditableSpline/fr
