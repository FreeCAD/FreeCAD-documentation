---
- GuiCommand:/fr
   Name:FCGear BevelGear
   Name/fr:FCGear BevelGear
   MenuLocation:FCGear → Create a Bevel gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Version:v0.16
---

## Description

Les engrenages coniques ne sont pas utilisés aussi souvent que les autres types d\'engrenages, en partie à cause du bruit qu\'ils génèrent. Mais ils sont encore utilisés dans certains secteurs, tels que les emballages alimentaires et les aliments en conserve, les équipements de jardin et de pelouse, les machines telles que les perceuses et les broyeurs, les systèmes de compression pour le marché du gaz et du pétrole et les vannes de régulation de débit.

Les engrenages coniques en spirale ont des dents incurvées pour fournir un engagement plus doux et un plus grand contact dent sur dent par rapport à un engrenage conique droit. Cela réduit les vibrations et le bruit. Ils peuvent être utilisés à des vitesses élevées et sont généralement utilisés dans les transmissions de motos et de vélos.

:   ![](images/Bevel-Gear_example.png )
:   
    *De gauche à droite : engrenage droit, engrenage en spirale*
    

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Lancez la commande d\'une de ces manières :
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_BevelGear.svg  style="width:22px;"> [Create a Bevel gear](FCGear_BevelGear/fr.md) dans la barre d\'outils.
    -   Utilisez le **Menu → Bevel gear**.
3.  Modifiez le paramètre de démultiplication aux conditions requises (voir **Propriétés → Données** ci-dessous).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans la [vue en arborescence](tree_view/fr.md).


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|beta}}: avec l\'angle β, un engrenage conique hélicoïdal est créé (valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche).


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|backslash}}: valeur par défaut est 0.00. Le recul, également appelé battement ou jeu, est la distance entre les dents d\'une paire d\'engrenages.

-    {{PropertyData/fr|clearance}}: valeur par défaut est 0.10 (voir aussi les informations dans **Remarque**).

-    {{PropertyData/fr|height}}: valeur de la largeur de l\'engrenage conique.

-    {{PropertyData/fr|module}}: module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir aussi les informations dans **Remarque**).

-    {{PropertyData/fr|numpoints}}: valeur par défaut est 6, modification du profil de développante. La modification de la valeur peut entraîner des résultats inattendus.

-    {{PropertyData/fr|reset_origin}}: si la valeur est **True**, le centre de l\'axe est au centre du bas de l\'engrenage (voir aussi les informations dans **Remarques**).

-    {{PropertyData/fr|teeth}}: nombre de dents.


{{Properties_Title|involute_parameter}}

-    **pitch_angle**: angle de dépouille.

-    **pressure_parameter**: valeur par défaut est 20 (voir aussi les informations dans **Remarque**).

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-    **clearance**: sur une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

-    **reset_origin**: cela peut être avantageux pour le montage si le paramètre est défini sur **false**. L\'origine du corps se situe alors à la pointe du cône primitif.

-    **pressure_parameter**: modifiez le paramètre uniquement si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

## Limitations

Les limitations ne sont pas encore connues.

## Formules utiles 

-    **pitch diameter**= **module** \* **teeth**

-    **addendum diameter**= **pitch diameter** + 2 \* **module** \* **cos angle du cône de référence**

-    **tip angle 1**= **(dents 1 + 2)** \* **(cos reference angle de cône 1)** : **(dents 2 - 2)** \* **(sin angle de cône de référence 1)**

-    **tip angle 2**= **(teeth 2 + 2)** \* **(cos reference angle de cône 2)** : **(teeth 1 - 2)** \* **(sin angle de cône de référence 2)**

-    **angle du cône de référence 1**= **(teeth 1)**: **(teeth 2)**

-    **angle du cône de référence 2**= **(teeth 2)**: **(teeth 1)**

-    **angle total de l'axe**= **angle du cône de référence 1** + **angle du cône de référence 2**

Angle du cône de référence substantiel \[TECH.\]




[Category:Addons{{\#translation:}}](Category:Addons.md) [Category:FCGear{{\#translation:}}](Category:FCGear.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
