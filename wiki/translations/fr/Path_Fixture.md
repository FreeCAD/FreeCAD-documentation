---
- GuiCommand:/fr
   Name:Path Fixture
   Name/fr:Path Point de fixation
   MenuLocation:Path → Supplemental commands → Point de fixation
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path Fixture/fr

## Description

Cet outil définit le dispositif de décalage de travail du contrôleur CNC de la machine.

Les coordonnées de décalage du travail cible incluent généralement: les codes G53 à G59. Le G-Code est simplement l\'indication du code (G53, G54, etc \...). Les systèmes de décalage du travail représentent:

-   G53 → Système de coordonnées absolues de la machine.
-   G54 → Système de coordonnées de l\'Origine Pièce.
-   G55 à G59.9 → Dispositifs de coordonnées permettant d\'effectuer des décalages de travail (plusieurs pièces identiques à usiner, décalées sur la table de la machine), par rapport aux capteurs de position d\'origine situés sur la machine CNC, à utiliser.

Le code G59 est utilisé pour étendre les capacités disponibles (nombre de points de fixation de pièces). Le degré d\'expansion mis en œuvre est spécifique à la machine CNC, et cette commande permet G59.1 à G59.9.

## Utilisation

1.  Pressez le bouton **<img src="images/Path_Fixture.svg" width=16px> [Path Point de Fixation](Path_Fixture/fr.md)** ou utilisez le raccourci clavier **P** puis **F**.
2.  Sélectionnez le dispositif de décalage de travail souhaité dans le menu déroulant.

## Propriétés

-    {{PropertyData/fr|Fixture}}: Définit le décalage courant.

-    {{PropertyData/fr|Active}}: Définit si cette commande est active ou non lors de l\'ajout dans un composé.

## Remarques

## Limitations

## Script





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Fixture/fr
