---
- GuiCommand:
   Name: Path Fixture
   Name/fr: Path Fixation
   MenuLocation: Path -> Autres commandes -> Fixation
   Workbenches: Path_Workbench/fr
---

# Path Fixture/fr

## Description

L\'outil <img alt="" src=images/Path_Fixture.svg  style="width:24px;"> [Fixation](Path_Fixture/fr.md) définit le dispositif de décalage de travail du contrôleur CNC de la machine.

Les coordonnées de décalage du travail cible incluent généralement: les codes G53 à G59. Le G-code est simplement l\'indication du code (G53, G54, etc \...). Les systèmes de décalage du travail représentent:

-   G53 → système de coordonnées absolues de la machine.
-   G54 → système de coordonnées de l\'origine de la pièce.
-   G55 à G59.9 → dispositifs de coordonnées permettant d\'effectuer des décalages de travail, par rapport aux capteurs de position d\'origine situés sur la machine CNC, à utiliser.

La commande G59 Fixation est utilisée pour étendre les fixations disponibles. Le degré d\'extension mis en œuvre est spécifique à la machine CNC, et cette commande permet de réaliser des extensions de G59.1 à G59.9.



## Utilisation

1.  Pressez le bouton **<img src="images/Path_Fixture.svg" width=16px> [Fixation](Path_Fixture/fr.md)** ou utilisez le raccourci clavier **P** puis **F**.
2.  Sélectionnez le dispositif de décalage de travail souhaité dans le menu déroulant.



## Propriétés

-    **Fixture**: définit le décalage courant.

-    **Active**: définit si cette commande est active ou non lors de l\'ajout dans un composé.



## Remarques

## Limitations



## Script





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Fixture/fr
