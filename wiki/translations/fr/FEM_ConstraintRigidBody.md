---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintRigidBody
   Name/fr: FEM Contrainte de corps rigide
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Contrainte de corps rigide
   Workbenches: FEM_Workbench/fr
   Version: 1.0
   SeeAlso: FEM_ConstraintDisplacement/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM ConstraintRigidBody/fr

## Description

Définit la contrainte de corps rigide de CalculiX qui contraint le mouvement des nœuds d\'une entité géométrique sélectionnée au mouvement d\'un nœud de référence dont l\'emplacement est défini par l\'utilisateur. En pratique, cette contrainte peut être utilisée pour appliquer une condition limite ou une charge qui sera propagée à l\'objet sélectionné. Le nœud de référence ayant des degrés de liberté de rotation, il est possible d\'appliquer un moment de charge ou une condition limite de rotation à n\'importe quelle face de cette manière. L\'emplacement du nœud de référence peut être sélectionné. Si il est décalé par rapport à une entité géométrique, une charge à distance (une force agissant sur un levier) peut être appliquée.



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintRigidBody.svg" width=16px> [Contrainte de corps rigide](FEM_ConstraintRigidBody/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintRigidBody.svg" width=16px> Contrainte de corps rigide** du menu.
2.  Appuyez sur le bouton **Ajouter**.
3.  Dans la [vue 3D](3D_view/fr.md), sélectionnez le ou les éléments géométriques (sommets, arêtes ou faces, mais pas un mélange de ces éléments) auxquels la contrainte doit être appliquée. Pour supprimer des objets de la sélection, appuyez sur le bouton **Supprimer** et cliquez dessus.
4.  Spécifiez les coordonnées du nœud de référence. Après avoir fermé le panneau des tâches, un symbole sphérique indiquera cet emplacement.
5.  Choisissez les modes pour les 3 degrés de liberté (DDL) de translation et 3 degrés de liberté de rotation :
    -   *Libre* : par défaut, pas de condition de limite ou de charge sur ce DDL.
    -   *Contrainte* : condition limite de déplacement/rotation avec une valeur spécifiée (par défaut : 0 = fixe) pour ce DDL. Pour la rotation, il faut définir un axe (X, Y ou Z) et spécifier l*\'Angle*.
    -   *Charge* : charge de la force/moment avec une valeur spécifiée pour ce DDL.

## Limitations

-   Pour l\'instant, les unités de moment peuvent prêter à confusion. Pour appliquer 1 N\*m, il faut mettre 1 J dans le champ de saisie (ces unités sont équivalentes).
-   La fonction ne peut être appliquée qu\'aux sommets, aux arêtes et aux faces pour l\'instant, la prise en charge des solides (pour rendre des volumes entiers/parties rigides) devrait suivre à l\'avenir.
-   L\'objet sélectionné est rendu rigide. Pour appliquer des charges d\'une manière plus flexible, il faudrait utiliser les contraintes de couplage de distribution de CalculiX, qui ne sont actuellement pas prises en charge.



## Remarques

-   Cette contrainte est le moyen standard d\'appliquer un couple à des pièces arbitraires. Les autres options sont le [système de coordonnées locales](FEM_ConstraintTransform/fr.md) (uniquement pour les faces cylindriques) ou une paire de forces, mais la contrainte de corps rigide devrait être suffisante dans presque tous les cas.
-   Aucune autre contrainte ou condition limite ne doit être appliquée aux nœuds concernés par une contrainte de corps rigide.
-   Lors de l\'application de cette contrainte à un sommet ou à une arête, il convient de mettre à zéro un DDF de rotation approprié (dans le cas d\'une arête, celui qui empêchera la rotation autour d\'elle).
-   Cette fonction utilise le jeu de paramètres [\*RIGID BODY card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node236.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintRigidBody/fr
