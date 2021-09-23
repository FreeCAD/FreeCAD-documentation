---
- GuiCommand:/fr
   Name:FCGear LanternGear
   Name/fr:FCGear LanternGear
   MenuLocation:FCGear → Create a Lantern gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Version:v0.16
---

# FCGear LanternGear/fr

## Description

La denture du pignon lanterne a une forme spéciale de denture cycloïdale dans laquelle le cercle de roulement et le cercle primitif sont de taille égale. De plus, les dents de la plus grande roue d\'une boîte de vitesses sont remplacées par des cylindres. La petite roue est dotée d\'un engrenage cycloïde. Il en résulte un engrenage ponctuel unilatéral. Les engrenages du pignon lanterne ne peuvent être que des dents droites.

Parce que leur construction est très simple, ils sont parmi les plus anciennes formes d\'engrenage. Les engrenages pignon lanterne sont utilisés lorsque de grands rapports de démultiplication sont nécessaires, par exemple dans les engrenages de pivotement des moulins ou des grues de manutention du bois.

La roue dentée du pignon lanterne avec chaînes à rouleaux est une alternative économique et robuste aux entraînements à pignon et crémaillère. En guidant la chaîne de roue dentée de lanterne étirée tangentiellement le long de la roue dentée du pignon lanterne, un mouvement linéaire de la chaîne est converti en un mouvement de rotation de la roue. A l\'inverse, un mouvement linéaire de la chaîne peut également être obtenu par le mouvement de rotation du pignon lanterne (moto/vélo).

:   ![](images/Latern_Gear_example.png )
:   
    *Au-dessus: pignon lanterne*
    

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Lancez la commande d\'une de ces manières :
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_LaternGear.svg  style="width:22px;"> [Create a Lantern gear](FCGear_LanternGear/fr.md) dans la barre d\'outils.
    -   Utilisez le **Menu → Lantern gear**.
3.  Modifier le paramètre d\'engrenage selon les conditions requises (voir **Propriétés → Données** ci-dessous).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans la [vue en arborescence](tree_view/fr.md).


{{Properties_Title|accuracy}}

-    {{PropertyData/fr|num_profiles}}: la valeur par défaut est 10. La valeur n\'a normalement pas besoin d\'être modifiée.


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|bolt_radius}}: la valeur par défaut est 1,00 mm. Diamètre du cylindre sur le disque rotatif qui fonctionne comme une seconde \"roue dentée\".

-    {{PropertyData/fr|height}}: La valeur par défaut est 5,00 mm. Valeur de la largeur de l\'engrenage.

-    {{PropertyData/fr|module}}: la valeur par défaut est 1,00 mm. Le module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir aussi les informations dans **Remarques**.

-    {{PropertyData/fr|teeth}}: La valeur par défaut est 15. Nombre de dents.

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-    **module**: En utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents d\'engrenage. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p). Le pas (Pitch) est la distance entre les points correspondants sur les dents adjacentes.

## Limitations

Les limitations ne sont pas encore connues.

## Formules utiles 

-    **addendum diameter**= **module** \* **(teeth +2)**

-    **ptch diameter**= **module** \* **teeth**

-    **axle base**= **pitch diameter (lantern gear 1 + 2)**: 2




[Category:Addons](Category:Addons.md) [Category:FCGear](Category:FCGear.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [Addons](Category:Addons.md) > FCGear LanternGear/fr
