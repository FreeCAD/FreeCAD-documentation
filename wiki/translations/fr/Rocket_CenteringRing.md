---
- GuiCommand:/fr
   Name:Rocket CenteringRing
   Name/fr:Rocket Anneau de centrage
   MenuLocation:Rocket → Centering Ring
   Workbenches:[Rocket](Rocket_Workbench/fr.md)
   Version:0.19
---

# Rocket CenteringRing/fr

## Description

Un anneau de centrage est un objet solide utilisé pour maintenir un ou plusieurs tubes du corps à l\'intérieur d\'un autre tube du corps.
![](images/CR_with_tubes.png ) *Conique*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Rocket_CenteringRing.svg" width=16px> [Centering Ring](Rocket_CenteringRing/fr.md)**.
    -   Sélectionnez l\'option **Rocket  → <img src="images/Rocket_CenteringRing.svg" width=16px> Centering Ring** dans le menu.
    -   Double-cliquez sur un objet Centering Ring dans la vue du modèle.
2.  Définissez les options et appuyez sur **OK**.

## Options

### Encoche

Les anneaux de centrage, en particulier ceux utilisés pour les fusées de faible puissance, ont souvent besoin d\'une encoche pour accueillir un crochet de moteur. L\'outil **Centering Ring** peut les générer pour vous.
![](images/Notched_CR.png ) *Anneau de centrage avec une encoche de crochet moteur*

## Propriétés


{{TitleProperty|Rocket Component}}

Ces paramètres sont fournis à titre indicatif et n\'ont aucun effet sur la conception du composant.

-    {{PropertyData/fr|Manufacturer}}: Fabricant lorsqu\'il est connu

-    {{PropertyData/fr|Part Number}}: Numéro de pièce du fabricant

-    {{PropertyData/fr|Description}}: Description du composant

-    {{PropertyData/fr|Material}}: Matériau lorsqu\'il est connu


{{TitleProperty|Bulkhead}}

Ces propriétés sont héritées de **Bulkhead**, voir [Cloison](Rocket_Bulkhead/fr.md) pour plus d\'informations

-    {{PropertyData/fr|Diameter}}: Le diamètre extérieur de la cloison

-    {{PropertyData/fr|Thickness}}: L\'épaisseur, à l\'exclusion de toute marche, de la cloison

-    {{PropertyData/fr|Step}}: Vrai lorsque la cloison comprend une étape, voir [Options de Cloison](Rocket_Bulkhead/fr#Options.md)

-    {{PropertyData/fr|Step Diameter}}: Le diamètre extérieur de la marche

-    {{PropertyData/fr|Step Thickness}}: L\'épaisseur, sans compter l\'épaisseur de la cloison, de la marche

-    {{PropertyData/fr|Holes}}: Vrai lorsque la cloison comporte un ou plusieurs trous, voir [Options de Cloison](Rocket_Bulkhead/fr#Options.md)

-    {{PropertyData/fr|Hole Diameter}}: Le diamètre du trou

-    {{PropertyData/fr|Hole Center}}: La distance entre le centre du trou et le centre de la cloison

-    {{PropertyData/fr|Hole Count}}: Le nombre de trous appliqués dans un motif radial autour du centre de la cloison

-    {{PropertyData/fr|Hole Offset}}: Décalage à partir de 0 degré du premier trou


{{TitleProperty|Centering Ring}}

-    {{PropertyData/fr|Center Diameter}}: Le diamètre du trou intérieur

-    {{PropertyData/fr|Notched}}: Vrai lorsque le trou central comprend une encoche, voir [Options](#Options.md)

-    {{PropertyData/fr|Notch Height}}: La hauteur de l\'encoche

-    {{PropertyData/fr|Notch Width}}: La largeur de l\'encoche

## Script

Voir aussi : [:Category:API/fr](:Category:API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

A définir

## Tutoriels et apprentissage 

[Tubes de corps, cloisons et anneaux de centrage Atelier Rocket](https://youtu.be/xi7acpw3eDA) Tutoriel sur YouTube







[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)

---
[documentation index](../README.md) > [API/fr]] et ](Category:API/fr]] et .md) > Rocket CenteringRing/fr
