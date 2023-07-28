---
- GuiCommand:/fr
   Name:FCGear CrownGear
   Name/fr:FCGear Engrenage couronne
   MenuLocation:Gear → Crown Gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
   Shortcut:Aucun
   Version:v0.16
   SeeAlso:[FCGear Engrenage à développante](FCGear_InvoluteGear/fr.md)
---

# FCGear CrownGear/fr



## Description

La roue de la couronne ressemble à une crémaillère incurvée en forme d\'anneau. L\'angle de pression décroît continuellement du diamètre extérieur vers le diamètre intérieur. Ainsi, la vitesse périphérique variable au niveau de la couronne est compensée par la vitesse périphérique constante du pignon. Les dents externes pointues et les flancs de dents raides sur le diamètre intérieur limitent la largeur de dent utilisable. Les engrenages couronnes atteignent des rendements similaires à ceux des engrenages droits. Une couronne dentée peut entraîner plusieurs pignons.

Champ d\'application connu des couronnes:

-   Entraînement de l\'essieu arrière pour voitures et motos
-   Mécanisme pivotant pour tables d\'opération
-   Têtes de fraisage angulaires
-   Systèmes d\'outils motorisés avec plusieurs pignons et couronne dentée

![](images/Crown-Gear_example.png ) 
*Au-dessus : Engrenage couronne*



## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur **[<img src=images/FCGear_CrownGear.svg style="width:16px"> [Crown Gear](FCGear_CrownGear/fr.md)** dans la barre d\'outils.
    -   Sélectionnez l\'option **Gear → [<img src=images/FCGear_CrownGear.svg style="width:16px"> Crown Gear** dans le menu.
3.  La couronne dentée est affichée sans dents par défaut. ({{Version/fr|0.21}})
4.  Modifiez les paramètres de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).
5.  Définissez la propriété **preview_mode** à {{false}} pour afficher les dents (voir [Remarques](#Remarques.md)).



## Propriétés

Un objet FCGear CrownGear est dérivé d\'un [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**: valeur par défaut à {{Value|4}}. Nombre de profils utilisés pour le loft.

-    **preview_mode|Bool**: valeur par défaut à {{True}}.


{{Properties_Title|base}}

-    **height|Length**: valeur par défaut à {{Value|2 mm}}. Valeur pour la largeur de la dent.

-    **module|Length**: valeur par défaut à {{Value|1 mm}}. Module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir [Notes](#Notes.md)).

-    **other_teeth|Integer**: valeur par défaut à {{Value|15}}. Nombre de dents de l\'engrenage de construction (pignon) (voir [Remarques](#Remarques.md)).

-    **teeth|Integer**: valeur par défaut à {{Value|15}}. Nombre de dents.

-    **thickness|Length**: valeur par défaut à {{Value|5 mm}}. Hauteur de la pointe de la dent à la face inférieure de la couronne.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: valeur par défaut à {{Value|20 °}} (voir [Remarques](#Remarques.md)).


{{Properties_Title|version}}

-    **version|String**:



## Remarques

-   La propriété **preview_mode** est définie à {{true}} par défaut et lorsque l\'engrenage est créé, vous trouverez ce message dans la vue du rapport :

    :   *Gear module: Crown gear created, preview_mode = true for improved performance. Set preview_mode property to false when ready to cut teeth.*
    :   (Module d\'engrenage : création d\'une couronne dentée, preview_mode = true pour une meilleure performance. Définissez la propriété preview_mode à false lorsque vous êtes prêt à couper les dents.)

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

-    **other_teeth**: plusieurs pignons avec le même nombre de dents ne peuvent être utilisés que sur une seule couronne.

-    **pressure_parameter**: ne modifiez le paramètre que si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

-   La géométrie de la couronne dentée est principalement déterminée par la géométrie du pignon droit (**other_teeth**).

-   Créez une roue dentée avec l\'[Engrenage à développante de cercle](FCGear_InvoluteGear/fr.md). Le nombre de dents doit être identique au paramètre **other_teeth** de la couronne dentée.

-   Des ajustements pour des caractéristiques de fonctionnement optimales peuvent être effectués avec les paramètres de l\'engrenage à développante.



## Vue d\'ensemble de l\'ensemble couronne et pignon droit 

![](images/Crown-spur-gear-set_example.png )

-   \(1\) Engrenage droit
-   \(2\) Couronne dentée
-   \(3\) Largeur de dent
-   \(4\) Diamètre intérieur
-   \(5\) Diamètre extérieur



## Formules utiles 

-   **Diamètre intérieur (4)**
    -   
        **inner diamter**
        
        = **module (engrenage droit)** \* **teeth (couronne dentée)** \* **cos pressure_paramter (pignon)** : **cos pressure_parameter (couronne dentée)**

-   **Diamètre extérieur (5)**
    -   
        **outer diamter**
        
        = **inner diameter** + **2x height (couronne dentée)**



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CrownGear/fr
