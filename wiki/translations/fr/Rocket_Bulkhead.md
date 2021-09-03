---
- GuiCommand:/fr
   Name:Rocket Bulkhead
   Name/fr:Rocket Cloison
   MenuLocation:Rocket → Bulkhead
   Workbenches:[Rocket](Rocket_Workbench/fr.md)
   Version:0.19
---

## Description

Une cloison est une section solide de matériau utilisée pour fermer une section du tube du corps ou pour fournir une base pour une coiffe.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Rocket_Bulkhead.svg" width=16px> [Bulkhead](Rocket_Bulkhead/fr.md)**.
    -   Sélectionnez l\'option **Rocket  → <img src="images/Rocket_Bulkhead.svg" width=16px> Bulkhead** dans le menu.
    -   Double-cliquez sur un objet Bulkhead dans la vue du modèle.
2.  Définissez les options et appuyez sur **OK**.

## Options

### Étape

Les cloisons peuvent comporter une marche.

Une marche peut être considérée comme une cloison supplémentaire de plus petit diamètre empilée sur le dessus de la cloison d\'origine. L\'utilisation la plus courante est de boucher l\'extrémité d\'un tube du corps, comme pour une baie électronique. Dans ce cas, le diamètre extérieur de la cloison correspondrait au diamètre extérieur du tube du corps et le diamètre extérieur de la marche correspondrait au diamètre intérieur du tube du corps.

![](images/Stepped_Bulkhead.png ) *Une cloison étagée utilisée pour boucher un tube du corps*

### Trous

Une cloison peut nécessiter des trous pour diverses raisons, telles que la fixation d\'un crochet à œil. Cet outil vous permet de spécifier un ou plusieurs trous identiques appliqués selon un schéma radial.

![](images/Bulkhead_2.png ) *Une cloison étagée à 4 trous*

## Propriétés


{{TitleProperty|Rocket Component}}

Ces paramètres sont fournis à titre indicatif et n\'ont aucun effet sur la conception du composant.

-    {{PropertyData/fr|Manufacturer}}: Fabricant lorsqu\'il est connu

-    {{PropertyData/fr|Part Number}}: Numéro de pièce du fabricant

-    {{PropertyData/fr|Description}}: Description du composant

-    {{PropertyData/fr|Material}}: Matériau lorsqu\'il est connu


{{TitleProperty|Bulkhead}}

-    {{PropertyData/fr|Diameter}}: Le diamètre extérieur de la cloison

-    {{PropertyData/fr|Thickness}}: L\'épaisseur, à l\'exclusion de toute marche, de la cloison

-    {{PropertyData/fr|Step}}: Vrai lorsque la cloison comprend une marche, voir [Options](#Options.md)

-    {{PropertyData/fr|Step Diameter}}: Le diamètre extérieur de la marche

-    {{PropertyData/fr|Step Thickness}}: L\'épaisseur, sans compter l\'épaisseur de la cloison, de la marche

-    {{PropertyData/fr|Holes}}: Vrai lorsque la cloison comporte un ou plusieurs trous, voir [Options](#Options.md)

-    {{PropertyData/fr|Hole Diameter}}: Le diamètre du trou

-    {{PropertyData/fr|Hole Center}}: La distance entre le centre du trou et le centre de la cloison

-    {{PropertyData/fr|Hole Count}}: Le nombre de trous appliqués dans un motif radial autour du centre de la cloison

-    {{PropertyData/fr|Hole Offset}}: Décalage à partir de 0 degré du premier trou

## Script

Voir aussi : [:Category:API/fr](:Category:API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

A définir

## Tutoriels et apprentissage 

[Tubes de corps, cloisons et anneaux de centrage Atelier Rocket](https://youtu.be/xi7acpw3eDA) Tutoriel sur YouTube







[Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md)
