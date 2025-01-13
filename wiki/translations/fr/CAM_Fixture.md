---
 GuiCommand:
   Name: CAM Fixture
   Name/fr: CAM Décaler l'origine
   MenuLocation: CAM , Autres commandes , Décaler l'origine
   Workbenches: CAM_Workbench/fr
---

# CAM Fixture/fr

## Description

L\'outil <img alt="" src=images/CAM_Fixture.svg  style="width:24px;"> [Décaler l\'origine](CAM_Fixture/fr.md) définit la position décalée du système de coordonnées de travail du contrôleur CNC de la machine-outil.

Les coordonnées de décalage du travail cible incluent généralement : les codes G53 à G59. Le G-code est simplement l\'indication du code (G53, G54, etc \...). Les systèmes de décalage de l\'origine sont :

-   G53 → système de coordonnées absolues de la machine.
-   G54 → système de coordonnées de l\'origine de la pièce.
-   G55 à G59.9 → dispositifs de coordonnées permettant d\'effectuer des décalages de travail, par rapport aux capteurs de position d\'origine situés sur la machine CNC, à utiliser.

La commande G59 de décalage d\'origine est utilisée pour étendre les décalages disponibles. Le degré d\'extension mis en œuvre est spécifique à la machine CNC, et cette commande permet de réaliser des extensions de G59.1 à G59.9.



## Utilisation

1.  Pressez le bouton **<img src="images/CAM_Fixture.svg" width=16px> [Décaler l'origine](CAM_Fixture/fr.md)** ou utilisez le raccourci clavier **P** puis **F**.
2.  Sélectionnez le dispositif de décalage de travail souhaité dans le menu déroulant.



## Propriétés

-    **Fixture**: définit le point de décalage courant.

-    **Active**: définit si cette commande est active ou non lors de l\'ajout dans un composé.



## Remarques

## Limitations



## Script





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Fixture/fr
