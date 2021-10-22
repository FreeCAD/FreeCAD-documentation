---
- GuiCommand:/fr
   Name:FCGear CycloideGear
   Name/fr:FCGear CycloideGear
   MenuLocation:FCGear → Create a Cycloide gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:[FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md)
---

# FCGear CycloideGear/fr

## Description

Les engrenages cycloïdaux sont très sensibles à un ajustement inexact de la distance centrale, ce qui entraîne alors une modification du rapport de transmission. Pour ces raisons, les engrenages cycloïdaux sont peu présents dans la construction mécanique mais ne sont utilisés que dans des cas particuliers tels que dans l\'industrie horlogère, pour les compresseurs mécaniques ou pour l\'entraînement de crémaillères.

:   ![](images/Cycloid-Gear_example_1.png )
:   
    
*De gauche à droite: Engrenage droit, engrenage hélicoïdal, engrenage double hélicoïdal*
    

## Utilisation

1.  Basculez vers <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Appelez la commande de plusieurs manières:
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_CycloideGear.svg  style="width:22px;"> [Create a Cycloide gear](FCGear_CycloideGear/fr.md) dans la barre d\'outils.
    -   En utilisant **Gear Menu → Cycloide gear**.
3.  Modifiez le paramètre d\'engrenage aux conditions requises (voir ci-dessous **Properties → Data**).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [Placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans la [vue en arborescence](tree_view/fr.md).


{{Properties_Title|cycloid_parameter}}

-    {{PropertyData/fr|inner_diameter}}: valeur par défaut est 5,00. Cercle roulant d\'hypocycloïde (voir aussi les informations dans les {{Emphasis |Remarques}}).

-    {{PropertyData/fr|outer_diameter}}: valeur par défaut est 5,00. Cercle roulant d\'épicycloïde (voir aussi les informations dans les {{Emphasis |Remarques}}).


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|backslash}}: valeur par défaut est 0,00. Le recul, également appelé battement ou jeu, est la distance entre les dents d\'une paire d\'engrenages.

-    {{PropertyData/fr|beta}}: avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé (valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche).

-    {{PropertyData/fr|clearance}}: valeur par défaut est 0,25 (voir aussi les informations dans **Remarques**).

-    **double_helix**: **True** crée un engrenage à double hélice (voir aussi les informations dans **Remarques**).

-    {{PropertyData/fr|height}}: valeur de la largeur de l\'engrenage.

-    {{PropertyData/fr|module}}: module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir aussi les informations dans **Remarques**).

-    {{PropertyData/fr|numpoints}}: valeur par défaut est de 15, changement du profil de la développante. La modification de la valeur peut entraîner des résultats inattendus.

-    {{PropertyData/fr|teeth}}: nombre de dents.

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-   Les engrenages cycloïdaux doivent toujours être spécialement adaptés les uns aux autres et ne peuvent généralement pas être échangés à volonté!

-   Dans une paire d\'engrenages, les deux vitesses ont les mêmes valeurs pour **inner_diameter** et **outer_diameter**. Voir également les informations dans **Propriétés de la vue des paramètres cycloïdes** ci-dessous.

-    **clearance**: sur une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **double_helix**: pour utiliser l\'engrenage hélicoïdal double, l\'angle d\'hélice β (**beta**) pour l\'engrenage hélicoïdal doit d\'abord être saisi.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

## Limitations

Les limitations ne sont pas encore connues.

## Formules utiles 

Pour plus d\'informations voir <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:22px;"> [Engrenage à développante de cercle](FCGear_InvoluteGear/fr.md).

## Propriétés vue paramètres cycloïdes 

<img alt="" src=images/CycloidGear_inner-outer-diameter_2.svg  style="width:400px;">




_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear CycloideGear/fr
