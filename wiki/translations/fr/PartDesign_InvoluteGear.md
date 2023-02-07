---
- GuiCommand:/fr
   Name:PartDesign InvoluteGear
   Name/fr:PartDesign Engrenage à développante
   MenuLocation:Part Design → Engrenage à développante...
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[Atelier FCGear](FCGear_Workbench/fr.md)
---

# PartDesign InvoluteGear/fr

## Description

Cet outil permet de créer un profil 2D d\'une roue d\'engrenage à développante. Ce profil 2D est pleinement paramétrique et peut être extrudé avec la fonction [PartDesign Protrusion](PartDesign_Pad/fr.md) ou [PartDesign Hélice additive](PartDesign_AdditiveHelix/fr.md).

Pour des informations plus détaillées, voir également [Engrenage](https://fr.wikipedia.org/wiki/Engrenage) et [Involute Gear](https://en.wikipedia.org/wiki/Involute_gear)

![](images/PartDesign_Involute_Gear_01.png )



## Utilisation



### Créer le profil 

1.  Activez le bon corps.
2.  Allez dans le menu **Part Design → [<img src=images/PartDesign_InternalExternalGear.svg style="width:16px"> Engrenage à développante...**.
3.  Définissez les paramètres de l\'engrenage à développante.
4.  Cliquez sur **OK**.
5.  S\'il n\'y avait pas de corps actif : faites glisser et déposez l\'engrenage dans un corps pour appliquer d\'autres fonctions comme une protrusion.



### Créer un engrenage droit 

1.  Sélectionnez le profil d\'engrenage dans la [Vue en arborescence](Tree_view/fr.md).
2.  Appuyez sur le bouton **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.
3.  Réglez la longueur de la protrusion **Length** à la largeur de la face souhaitée pour l\'engrenage.
4.  Cliquez sur **OK**.



### Créer un engrenage hélicoïdal 


{{Version/fr|0.19}}

1.  Sélectionnez le profil d\'engrenage dans la [vue en arborescence](Tree_view/fr.md).
2.  Appuyez sur le bouton **<img src="images/PartDesign_AdditiveHelix.svg" width=16px> [PartDesign Hélice additive](PartDesign_AdditiveHelix/fr.md)**.
3.  Choisissez comme axe la normale du profil de l\'engrenage, c\'est-à-dire l\'**Axe normal de l'esquisse**. {{Version/fr|0.20}}. (Dans les versions antérieures, l\'axe **Base Z** pouvait être utilisé tant que le plan du profil n\'avait pas été modifié).
4.  Choisissez un mode **Hauteur-Tours**.
5.  Réglez la hauteur **Height** à la largeur de la face souhaitée de l\'engrenage.
6.  Pour définir l\'angle de l\'hélice souhaité, il faut une [expression](Expressions/fr.md) pour les tours **Turns**.
    1.  Cliquez sur l\'icône bleue <img alt="" src=images/Bound-expression.svg  style="width:16px;"> à droite du champ de saisie.
    2.  Saisissez la formule suivante : `Height * tan(25°) / (InvoluteGear.NumberOfTeeth * InvoluteGear.Modules * pi)`, où `25°` est un exemple d\'angle d\'hélice souhaité (également appelé valeur bêta) et `InvoluteGear` est le nom **Name** du profil.
    3.  Cliquez sur **OK** pour fermer l\'éditeur de formule.
    4.  Cliquez sur **OK** pour fermer le panneau des tâches.

Conseil : pour faire de l\'angle d\'hélice un paramètre accessible, utilisez une *propriété dynamique* :

1.  Sélectionnez le profil.
2.  Dans l\'[éditeur de propriétés](Property_editor/fr.md), activez l\'option **Tout afficher** dans le menu contextuel.
3.  Toujours dans le menu contextuel, sélectionnez l\'option **Ajouter une propriété**. Remarque : cette entrée n\'est disponible que lorsque l\'option **Tout afficher** est active.
4.  Dans la boîte de dialogue **Ajouter une propriété** :
    1.  Choisissez `App::PropertyAngle` comme Type.
    2.  Définissez `Gear` comme Groupe.
    3.  Définissez `HelicalAngle` comme Nom (sans espace).
    4.  Cliquez sur **OK**.
    5.  Maintenant une nouvelle propriété **Helical Angle** (espace ajouté automatiquement), avec une valeur initiale de `0.0°`, devient disponible.
5.  Attribuez l\'angle hélicoïdal souhaité à la nouvelle propriété.
6.  Dans la formule de la propriété **Turns** de l\'Hélice additive, vous pouvez maintenant faire référence à `InvoluteGear.HelicalAngle` au lieu de la valeur codée en dur de `25°`, en supposant que `InvoluteGear` est la **Name** du profil.



## Propriétés

-    **External Gear**: vrai ou faux

-    **High Precision**: vrai ou faux

-    **Modules**: diamètre de pas divisé par le nombre de dents.

-    **Number Of Teeth**: définit le nombre de dents désirées.

-    **Pressure Angle**: angle aigu entre la ligne d\'action et une normale à la ligne reliant les centres d\'engrenage. La valeur par défaut est de 20 degrés. ([plus d\'info](https://fr.wikipedia.org/wiki/Roue_dent%C3%A9e))

## Limitations

-   Il n\'est actuellement pas possible de régler l\'épaisseur des dents. Les dents et l\'espacement des dents sont répartis de manière égale sur le cercle primitif. Ainsi, la seule façon de contrôler le jeu est d\'ajuster la distance centrale dans un engrenage.
-   Il n\'y a actuellement pas de [undercut (contre-dépouille)](https://www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/) dans le profil d\'engrenage généré. Cela signifie que les engrenages avec un faible nombre de dents peuvent interférer avec les dents de l\'engrenage correspondant. La limite inférieure dépend de l\'angle de pression **Pressure Angle** et se situe autour de 17 dents pour 20° et 32 pour 14,5°. La plupart des applications pratiques tolèrent cependant une contre-dépouille manquante pour des engrenages un peu plus petits que cette limite théorique.



## Tutoriels

[How to make gears in FreeCAD](https://www.youtube.com/watch?v=8VNhTrnFMfE)



## En relation 

-   [Atelier FCGear](FCGear_Workbench/fr.md)





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/fr
