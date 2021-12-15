---
- GuiCommand:/fr
   Name:FCGear WormGear
   Name/fr:FCGear WormGear
   MenuLocation:FCGear → Create a Worm gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:[PartDesign Engrenage droit à développante](PartDesign_InvoluteGear/fr.md)
---

# FCGear WormGear/fr

## Description

La vis sans fin peut être considérée comme un cas particulier d\'engrenage hélicoïdal. Imaginez qu\'il n\'y ait qu\'une seule dent sur un engrenage droit. Augmentez maintenant l\'angle d\'hélice de telle sorte que la dent s\'enroule plusieurs fois autour de l\'engrenage droit avant d\'émerger du côté opposé. Le résultat serait une vis sans fin à un seul filet.

Pour une vis sans fin à démarrage unique, chaque tour complet (360 degrés) de la vis sans fin fait avancer l\'engrenage d\'une dent. Ainsi, un engrenage de 24 dents donnera une réduction de 24:1. Pour une vis sans fin à plusieurs démarrages, la réduction est égale au nombre de dents de l\'engrenage, divisé par le nombre de démarrages de la vis sans fin.

Une vis sans fin ne peut être utilisée qu\'avec une roue à vis sans fin. C\'est ce qu\'on appelle un entraînement par vis sans fin. Comme d\'autres systèmes de transmission, un entraînement à vis sans fin peut réduire la vitesse de rotation ou transmettre un couple plus élevé. L\'un des principaux avantages des engrenages à vis sans fin est qu\'ils peuvent transmettre un mouvement à 90 degrés. Un entraînement à vis sans fin est également autobloquant.

![](images/Worm-Gear_example.png ) 
*Engrenage à vis sans fin (nombre de dents 3)*

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Lancez la commande d\'une de ces manières :
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_WormGear.svg  style="width:22px;"> [Create a Worm gear](FCGear_WormGear/fr.md) dans la barre d\'outils.
    -   Utilisez le **Menu → Worm gear**.
3.  Modifier le paramètre d\'engrenage selon les conditions requises (voir **Propriétés → Données** ci-dessous).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans la [vue en arborescence](tree_view/fr.md).


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|beta}}: Angle d\'attaque, non modifiable - est calculé automatiquement (voir aussi les informations dans les **Remarques** et **Formules utiles**).

-    {{PropertyData/fr|clear}}: La valeur par défaut est 0,25 (voir aussi les informations dans les **Remarques**).

-    {{PropertyData/fr|diamètre}}: Diamètre de pas.

-    {{PropertyData/fr|head}}: La valeur par défaut est 0,00. Cette valeur est utilisée pour modifier la hauteur de la dent.

-    {{PropertyData/fr|height}}: Valeur de la longueur du ver.

-    {{PropertyData/fr|module}}: Module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir aussi les informations dans les **Remarques**).

-    {{PropertyData/fr|reverse_pitch}}: **True** change le sens de rotation de droite à gauche.

-    {{PropertyData/fr|teeth}}: Nombre de dents (voir aussi les informations dans les **Remarques**).


{{Properties_Title|involute_parameter}}

-    {{PropertyData/fr|pressure_parameter}}: valeur par défaut 20 (voir aussi les informations dans les **Remarques**).

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-    **beta**: Si l\'angle d\'attaque est inférieur à 5°, il s\'agit d\'un engrenage autobloquant. Un exemple typique sont les chevilles d\'accord sur une guitare ou un ukulélé.

-    **clearance**: Dans un engrenage à vis sans fin, le jeu est la distance entre la pointe de la dent de la vis sans fin et la racine de la dent de la roue à vis sans fin.

-    **module**: En utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p). Le pas est la distance entre les points correspondants sur les dents adjacentes. Si le module est modifié, l\'angle principal change également (**beta**).

-    **teeth**: Le nombre de dents dans une vis est appelé le nombre de filets. De même, on parle de vis à filet simple, double ou multiple. En général, des vis à filet simple sont principalement produites mais dans des cas particuliers, le nombre de démarrages peut aller jusqu\'à quatre (parfois aussi plus). Si le nombre de dents est modifié, **beta** change également.

-    **pressure_parameter**: modifiez le paramètre uniquement si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

## Limitations

Les limitations ne sont pas encore connues.

## Formules utiles 

-    **beta (lead angle)**= arctan (**module** \* **teeth** : **pitchdiameter (diameter)**)

-    **axial pitch**= **pi** \* **module** \* **teeth**

-    **beta (lead angle)**= arctan (**axial pitch** : (**pitchdiameter (diameter)** \* **pi**))

-    **worm length**= 4,5 \* **module** \* **pi**

## Roue à vis sans fin 

La roue à vis sans fin doit être conçue manuellement. À cet effet, **FCGear InvoluteGear** peut être utilisé pour une construction simple. Dans tous les cas, une connaissance approfondie des types d\'engrenages est requise.

![](images/Worm-Gear_example3.png ) 
*Vis sans fin avec roue à vis sans fin*




_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear WormGear/fr
