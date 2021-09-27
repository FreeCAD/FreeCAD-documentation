---
- GuiCommand:/fr
   Name:FCGear CrownGear
   Name/fr:FCGear CrownGear
   MenuLocation:FCGear → Create an Crown gear
   Workbenches:[FCGear](FCGear_Workbench/fr.md)
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

:   ![](images/Crown-Gear_example.png )
:   
    *Au-dessus : Engrenage couronne*
    

## Utilisation

1.  Basculez vers l\'<img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Lancez la commande d\'une de ces manières :
    -   Appuyez sur le bouton <img alt="" src=images/FCGear_CrownGear.svg  style="width:22px;"> [Create a Crown gear](FCGear_CrownGear/fr.md) dans la barre d\'outils.
    -   Utilisez le **Menu → Crown gear**.
3.  Modifier le paramètre d\'engrenage selon les conditions requises (voir **Propriétés → Données** ci-dessous).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Placement}}: [Placement](Placement/fr.md) est l\'emplacement et l\'orientation d\'un objet dans l\'espace.

-    {{PropertyData/fr|Label}}: nom d\'utilisateur de l\'objet dans [vue en arborescence](tree_view/fr.md).


{{Properties_Title|accuracy}}

-    {{PropertyData/fr|construct}}: valeur par défaut est **True**. Passez à **False** et le composant de construction disparaît. **construct** appartient à **other_teeth**.

-    {{PropertyData/fr|num_profiles}}: nombre de profils utilisés pour le loft.


{{Properties_Title|gear_parameter}}

-    {{PropertyData/fr|height}}: valeur de la largeur de dent.

-    {{PropertyData/fr|module}}: module est le rapport du diamètre de référence de l\'engrenage divisé par le nombre de dents (voir aussi les informations dans **Remarque**).

-    {{PropertyData/fr|other_teeth}}: nombre de dents de l\'engrenage (pignon) de **construction**. (voir aussi les informations dans **Remarque**).

-    {{PropertyData/fr|teeth}}: nombre de dents

-    {{PropertyData/fr|thickness}}: hauteur de la pointe de la dent au côté inférieur de la couronne.


{{Properties_Title|involute_parameter}}

-    {{PropertyData/fr|pressure_parameter}}: valeur par défaut 20 (voir aussi les informations dans **Remarque**).

### Vue

La description des paramètres de l\'onglet **View** se trouve dans l\'[Éditeur de propriétés](Property_editor/fr.md) dans **Exemple de propriétés d'un objet PartDesign**.

## Remarques

-    **module**: en utilisant les directives ISO (Organisation internationale de normalisation), la taille du module est désignée comme l\'unité représentant la taille des dents des engrenages. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Si vous multipliez Module par Pi, vous pouvez obtenir Pitch (p) (le pas). Le pas est la distance entre les points correspondants sur les dents adjacentes.

-    **other_teeth**: Plusieurs pignons avec le même nombre de dents ne peuvent être utilisés que sur une seule couronne.

-    **pressure_parameter**: ne modifiez le paramètre que si une connaissance suffisante de la géométrie de l\'engrenage est disponible.

-   La géométrie de la couronne dentée est principalement déterminée par la géométrie du pignon droit (**other_teeth**).

-   Créez une roue dentée avec l\'<img alt="link = FCGear InvoluteGear" src=images/FCGear_InvoluteGear.svg  style="width:22px;"> [Engrenage à développante de cercle](FCGear_InvoluteGear/fr.md). Le nombre de dents doit être identique au paramètre **other_teeth** de la couronne dentée.

-   Des ajustements pour des caractéristiques de fonctionnement optimales peuvent être effectués avec les paramètres de l\'engrenage à développante.

## Limitations

Aucune limitation n\'est connue.

## Vue d\'ensemble de l\'ensemble couronne et pignon droit 

:   ![](images/Crown-spur-gear-set_example.png )

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




_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear CrownGear/fr
