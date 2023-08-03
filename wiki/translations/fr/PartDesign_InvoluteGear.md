---
 GuiCommand:
   Name: PartDesign InvoluteGear
   Name/fr: PartDesign Engrenage à développante
   Icon: PartDesign_InternalExternalGear.svg
   MenuLocation: Part Design , Engrenage à développante...
   Workbenches: PartDesign_Workbench/fr
   SeeAlso: FCGear_Workbench/fr
---

# PartDesign InvoluteGear/fr

## Description

Cet outil permet de créer un profil 2D d\'une roue d\'engrenage à développante ou un arbre cannelé. Ce profil 2D est pleinement paramétrique et peut être extrudé avec la fonction [PartDesign Protrusion](PartDesign_Pad/fr.md) ou [PartDesign Hélice additive](PartDesign_AdditiveHelix/fr.md).

Pour des informations plus détaillées, voir également [Engrenage](https://fr.wikipedia.org/wiki/Engrenage) et [fonction involute](https://fr.wikipedia.org/wiki/Involute)

<img alt="" src=images/PartDesign_Involute_Gear_01.png  style="width:200px;">



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



### Créer un moyeu pour un arbre cannelé en développante 


{{Version/fr|0.21}}

1.  Activez le corps.
2.  Créez un profil d\'engrenage à développante interne avec le nombre requis de rainures et adaptez les valeurs de l\'angle de pression, du coefficient de l\'addendum, du dedendum et du congé. Voir également le tableau dans les [Remarques](#Remarques.md) ci-dessous pour les valeurs réalisables. Par exemple :
    -   
        **External Gear**
        
        : faux

    -   
        **Number Of Teeth**
        
        : 12

    -   
        **Pressure Angle**
        
        : 37.5°

    -   
        **Addendum Coefficient**
        
        : 0.45

    -   
        **Dedendum Coefficient**
        
        : 0.7

    -   
        **Root Fillet Coefficient**
        
        : 0.3
3.  Sélectionnez le profil d\'engrenage dans la [vue en arborescence](Tree_view/fr.md).
4.  Appuyez sur le bouton **<img src="images/PartDesign_Pocket.svg" width=16px> '''Cavité'''**.
5.  Définissez **Type** de la cavité à **A travers tout**.
6.  Vérifiez l\'option **Symmetric To Plane** de la cavité.
7.  Cliquez sur **OK**.



## Propriétés

-    **Addendum Coefficient**: hauteur de la dent depuis le cercle primitif jusqu\'à sa pointe, normalisée par le module. La valeur par défaut est de 1,0 pour le système standard de pleine profondeur. {{Version/fr|0.21}}

-    **Dedendum Coefficient**: hauteur de la dent depuis le cercle primitif jusqu\'à sa racine, normalisée par le module. La valeur par défaut est 1,25 pour le système standard de pleine profondeur. {{Version/fr|0.21}}

-    **External Gear**: vrai ou faux

-    **High Precision**: vrai ou faux

-    **Modules**: diamètre de pas divisé par le nombre de dents.

-    **Number Of Teeth**: définit le nombre de dents désirées.

-    **Pressure Angle**: angle aigu entre la ligne d\'action et une normale à la ligne reliant les centres d\'engrenage. La valeur par défaut est de 20 degrés. Voir [Involute gear](https://en.wikipedia.org/wiki/Involute_gear).

-    **Profile Shift Coefficient**: distance par laquelle le profil de référence est décalé vers l\'extérieur, normalisé par le module. La valeur par défaut est zéro. Le décalage du profil peut être positif ou négatif. {{Version/fr|0.21}}

-    **Root Fillet Coefficient**: rayon du congé à la racine de la dent, normalisé par le module. La valeur par défaut est 0,38 comme défini par le rack ISO. {{Version/fr|0.21}}



## Remarques

-   Pour que deux engrenages puissent s\'engrener, ils doivent partager le même module et le même angle de pression. Des [expressions](Expressions/fr.md) peuvent aider à assurer la cohérence. Leur entraxe doit être `(NumberOfTeeth + OtherGear.NumberOfTeeth) * Modules / 2`. (c\'est-à-dire dans le cas où le décalage du profil de la somme est nul). Soustraire le nombre de dents dans le cas d\'un engrenage intérieur.

-   Le décalage de profil peut être utilisé pour éviter les contre-dépouilles sur les engrenages ayant un petit nombre de dents. Une autre application consiste à ajuster l\'entraxe de deux engrenages ayant un nombre donné de dents et un module.

-   Lors de la vérification visuelle d\'un engrenage ou des interférences, une valeur beaucoup plus faible de **Deviation** est utile, par exemple 0,05 au lieu de la valeur par défaut 0,5. Sinon, la représentation dans la [vue 3D](3D_view/fr.md) peut être trop grossière.

-   Pour les engrenages standard, l\'angle de pression le plus courant est de 20°, suivi de 14,5°. D\'autres applications, notamment les [arbres cannelés (en)](https://en.wikipedia.org/wiki/Spline_(mechanical)), utilisent des angles plus élevés.

-   Le système standard de pleine profondeur utilise un coefficient de tête de 1,0 et un coefficient de pied de 1,25, ce qui donne un jeu de 0,25 (la différence entre la tête d\'un engrenage et le pied de l\'autre). La longueur réelle des dents est la somme des deux coefficients, multipliée par le module.

-   Une réduction de la longueur des dents peut être nécessaire pour éviter la contre-dépouille ou pour renforcer les dents (voir [stub teeth](https://khkgears.net/new/gear_knowledge/gear-nomenclature/stub-teeth.html)). Pour les engrenages internes, il peut être nécessaire de raccourcir la denture (ici pointant vers l\'intérieur) pour éviter certaines interférences ou des flancs non-involutifs, si cela est indiqué en combinaison avec des dents plus longues du pignon.

-   Pour les arbres et les moyeux cannelés, la norme ISO 4156 définit les paramètres suivants :

:   {\| class=\"wikitable\"

\|- ! Angle de pression !! 30° (racine plate) !! 30° (racine avec congé) !! 37,5° !! 45° \|- \| Coefficient addendum \|\| 0,5 \|\| 0,5 \|\| 0,45 \|\| 0,4 \|- \| Coefficient dedendum \|\| 0,75 \|\| 0,9 \|\| 0,7 \|\| 0,6 \|- \| Coefficient du congé à la racine \|\| 0.2 \|\| 0.4 \|\| 0.3 \|\| 0.25 \|}

## Limitations

-   Il n\'est actuellement pas possible de régler l\'épaisseur des dents. Les dents et l\'espacement des dents sont répartis de manière égale sur le cercle primitif. Ainsi, la seule façon de contrôler le jeu est d\'ajuster la distance centrale dans un engrenage.
-   Il n\'y a actuellement pas de [undercut (contre-dépouille)](https://www.tec-science.com/mechanical-power-transmission/involute-gear/undercut/) dans le profil d\'engrenage généré. Cela signifie que les engrenages avec un faible nombre de dents peuvent interférer avec les dents de l\'engrenage correspondant. La limite inférieure dépend de l\'angle de pression **Pressure Angle** et se situe autour de 17 dents pour 20° et 32 pour 14,5°. La plupart des applications pratiques tolèrent cependant une contre-dépouille manquante pour des engrenages un peu plus petits que cette limite théorique.



## Tutoriels

Vidéo : [How to make gears in FreeCAD](https://www.youtube.com/watch?v=8VNhTrnFMfE)



## En relation 

-   [Atelier FCGear](FCGear_Workbench/fr.md)





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign InvoluteGear/fr
