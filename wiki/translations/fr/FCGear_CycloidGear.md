---
- GuiCommand:
   Name:FCGear CycloidGear
   Name/fr:FCGear Engrenage cycloïde
   MenuLocation:Gear - Cycloid Gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:[FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md)
---

# FCGear CycloidGear/fr

## Description

Les engrenages cycloïdaux sont très sensibles à un ajustement inexact de la distance centrale, ce qui entraîne alors une modification du rapport de transmission. Pour ces raisons, les engrenages cycloïdaux sont peu présents dans la construction mécanique mais ne sont utilisés que dans des cas particuliers tels que dans l\'industrie horlogère, pour les compresseurs mécaniques ou pour l\'entraînement de crémaillères.

![](images/Cycloid-Gear_example_1.png ) 
*De gauche à droite: Engrenage droit, engrenage hélicoïdal, engrenage double hélicoïdal*

## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_CycloidGear.svg style="width:16px"> [Cycloid Gear](FCGear_CycloidGear/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Gear → [<img src=images/FCGear_CycloidGear.svg style="width:16px"> Cycloid Gear** dans le menu.
3.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).

## Propriétés

### Données

Un objet FCGear CycloidGear est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: valeur par défaut à {{Value|15}}, Modification du profil de la développante. Changer la valeur peut conduire à des résultats inattendus.


{{Properties_Title|base}}

-    **height|Length**: valeur par défaut à {{Value|5 mm}}. Valeur de la largeur de l\'engrenage.

-    **module|Length**: valeur par défaut à {{Value|1 mm}}. Le module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir [Remarques](#Remarques.md)).

-    **teeth|Integer**: valeur par défaut à {{Value|15}}. Nombre de dents.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (lecture seule)

-    **dw|Length**: (lecture seule) diamètre du pas de travail.


{{Properties_Title|cycloid}}

-    **inner_diameter|Float**: (lecture seule). Diamètre du cercle de roulement de l\'hypocycloïde, normalisé par le **module**. (voir [Remarques](#Remarques.md)).

-    **outer_diameter|Float**: valeur par défaut à {{Value|7.5}}. Diamètre du cercle de roulement de l\'épicycloïde, normalisé par le **module**. (voir [Remarques](#Remarques.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: valeur par défaut à {{value|0 mm}}.

-    **root_fillet|Float**: valeur par défaut à {{value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: valeur par défaut à {{value|0 °}}. Avec l\'angle d\'hélice β, un engrenage hélicoïdal est créé (valeur positive → sens de rotation à droite, valeur négative → sens de rotation à gauche).

-    **double_helix|Bool**: valeur par défaut à {{false}}. **True** crée un engrenage à double hélice (voir [Remarques](#Remarques.md)).


{{Properties_Title|tolerance}}

-    **backlash|Length**: valeur par défaut à {{value|0}}. Le jeu, également appelé lash ou play, est la distance entre les dents d\'une paire d\'engrenages.

-    **clearance|Float**: valeur par défaut à {{value|0,25}} (voir [Remarques](#Remarques.md)).

-    **head|Float**: valeur par défaut à {{value|0}}. Longueur supplémentaire de la pointe des dents, normalisée par **module**. La valeur par défaut est 0.


{{Properties_Title|version}}

-    **version|String**:

## Remarques

-   Les engrenages cycloïdaux doivent toujours être spécialement adaptés les uns aux autres et ne peuvent généralement pas être échangés à volonté : Dans une paire d\'engrenages, la valeur de **inner_diameter** sur un engrenage doit être égale à **outer_diameter** sur l\'autre, et vice versa. Voir aussi les informations dans **Propriétés vue paramètres cycloïdes** ci-dessous.

-    **clearance**: sur une paire d\'engrenages, le jeu est la distance entre l\'extrémité de la dent du premier engrenage et la racine de la dent du deuxième engrenage.

-    **double_helix**: pour utiliser l\'engrenage hélicoïdal double, l\'angle d\'hélice β (**beta**) pour l\'engrenage hélicoïdal doit d\'abord être saisi.

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

## Cas particuliers 

### Ligne droite comme hypocycloïde 

Pour obtenir une ligne droite, directement vers le centre, comme l\'hypocycloïde, utilisez l\'[expression](Expressions/fr.md) suivante pour **inner_diameter** : `teeth / 2`. Une telle forme de dent se retrouve souvent dans les horloges historiques et est donc appelée \"denture d\'horloge\". Une **clearance** plus grande rend l\'effet encore plus visible.

### Hypocycloïde/épicycloïde complet en tant que dent 

Pour obtenir un engrenage constitué de courbes hypocycloïdes et épicycloïdes complètes, utilisez les [expressions](Expressions/fr.md) suivantes :

-    **inner_diameter**: `0.5 + 1e-6`

-    **outer_diameter**: `inner_diameter`

-    **clearance**: `(-1 + inner_diameter/1mm) * 2`

-    **head**: `(-1 + outer_diameter/1mm) * 2`

Le diamètre de référence est *d = m \* z*, avec *m* étant le **module** et *z* étant les dents **teeth**. Pour une hypocycloïde complète, le diamètre de roulement doit être *d_i = d / (z\*2) = m\*z / (z\*2)*. Et si nous normalisons maintenant cela par le module, nous obtenons *d_in = m\*z / (z\*2) / m = 1 / 2*. La valeur de tolérance explicite supplémentaire (`1e-6` dans l\'expression ci-dessus) est nécessaire pour surmonter les problèmes de coïncidence.

Les diamètres des cercles de roulement des cycloïdes doivent maintenant correspondre à l\'addedum/dedendum de l\'engrenage. L\'addendum, c\'est-à-dire la longueur de la dent au-dessus du cercle de référence, est égal à 1 + **head**. Le dedendum, c\'est-à-dire la longueur de la dent en dessous du cercle de référence, est de 1 + **clearance**. Les deux sont normalisés par le module, donc nous avons besoin d\'une valeur de tête/dégagement (head/clearance) de *1 - d_in*. Les valeurs supplémentaires ` / 1mm` et ` * 2` sont nécessaires pour pallier les défauts déjà corrigés dans la version de développement de l\'atelier FCGear, mais le portage de ces corrections dans la version stable peut casser les modèles existants.

De tels \"engrenages\" permettent de réduire le nombre de dents à \"deux\" et sont utilisés comme palettes rotatives dans les pompes ou les compresseurs (cf. [Compresseur mécanique à lobes](https://fr.wikipedia.org/wiki/Compresseur_m%C3%A9canique#%C3%80_lobe(s))).

### Epicycloïde infiniment grand 

Si le rayon du cercle de roulement de l\'épicycloïde devient infiniment grand, il devient une ligne droite de roulement. Une telle épicycloïde dégénérée est appelée développante. Les engrenages avec une telle forme de dent sont gérés par la commande [engrenage à développante](FCGear_InvoluteGear/fr.md). C\'est de loin la forme de dent la plus courante aujourd\'hui.

## Formules utiles 

Voir [FCGear InvoluteGear](FCGear_InvoluteGear/fr#Formules_utiles.md).

## Propriétés vue paramètres cycloïdes 

<img alt="" src=images/CycloidGear_inner-outer-diameter_2.svg  style="width:400px;">



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CycloidGear/fr
