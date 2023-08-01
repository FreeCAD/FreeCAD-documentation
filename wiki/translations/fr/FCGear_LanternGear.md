---
- GuiCommand:
   Name:FCGear LanternGear
   Name/fr:FCGear Pignon lanterne
   MenuLocation:Gear → Lantern Gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:
---

# FCGear LanternGear/fr

## Description

La denture du pignon lanterne a une forme spéciale de denture cycloïdale dans laquelle le cercle de roulement et le cercle primitif sont de taille égale. De plus, les dents de la plus grande roue d\'une boîte de vitesses sont remplacées par des cylindres. La petite roue est dotée d\'un engrenage cycloïde. Il en résulte un engrenage ponctuel unilatéral. Les engrenages du pignon lanterne ne peuvent être que des dents droites.

Parce que leur construction est très simple, ils sont parmi les plus anciennes formes d\'engrenage. Les engrenages pignon lanterne sont utilisés lorsque de grands rapports de démultiplication sont nécessaires, par exemple dans les engrenages de pivotement des moulins ou des grues de manutention du bois.

La roue dentée du pignon lanterne avec chaînes à rouleaux est une alternative économique et robuste aux entraînements à pignon et crémaillère. En guidant la chaîne de roue dentée de lanterne étirée tangentiellement le long de la roue dentée du pignon lanterne, un mouvement linéaire de la chaîne est converti en un mouvement de rotation de la roue. A l\'inverse, un mouvement linéaire de la chaîne peut également être obtenu par le mouvement de rotation du pignon lanterne (moto/vélo).

![](images/Lantern-Gear_example.png ) 
*Ci-dessus : pignon lanterne*

## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_LanternGear.svg style="width:16px"> [Lantern Gear](FCGear_LanternGear/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Gear → [<img src=images/FCGear_LanternGear.svg style="width:16px"> Lantern Gear** dans le menu.
3.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).

## Propriétés

### Données

Un objet FCGear LanternGear est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**: valeur par défaut à {{Value|10}}. La valeur n\'a normalement pas besoin d\'être modifiée.


{{Properties_Title|base}}

-    **bolt_radius|Length**: valeur par défaut à {{Value|1 mm}}. Diamètre du cylindre du disque rotatif qui fait office de deuxième \"roue dentée\".

-    **height|Length**: valeur par défaut à {{Value|5 mm}}. Valeur de la largeur de l\'engrenage.

-    **module|Length**: valeur par défaut à {{Value|1 mm}}. Le module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir [Remarques](#Remarques.md)).


{{Properties_Title|gear_parameter}}

-    **teeth|Integer**: valeur par défaut à {{Value|15}}. Nombre de dents.


{{Properties_Title|tolerance}}

-    **head|Float**: valeur par défaut à {{Value|0}}.


{{Properties_Title|version}}

-    **version|String**:

## Remarques

-    **module**: En utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents d\'engrenage. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p). Le pas (Pitch) est la distance entre les points correspondants sur les dents adjacentes.

## Formules utiles 

-    **addendum diameter**= **module** \* **(teeth +2)**

-    **pitch diameter**= **module** \* **teeth**

-    **axle base**= **pitch diameter (lantern gear 1 + 2)**: 2



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear LanternGear/fr
