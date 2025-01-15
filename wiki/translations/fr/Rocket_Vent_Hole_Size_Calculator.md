---
 GuiCommand:
   Name: Rocket Vent Hole Size Calculator
   Name/fr: Rocket Calcul taille trou d'évent
   Icon: Rocket_Calculator.svg
   MenuLocation: Rocket , Calculators , Vent Hole Size Calculator
   Workbenches: Rocket_Workbench/fr
   Version: 0.19
---

# Rocket Vent Hole Size Calculator/fr

## Description

Ce calculateur détermine la taille minimale des trous de ventilation pour les altimètres barométriques en fonction du volume de l\'espace et du nombre de trous de ventilation.

Le calcul est basé sur la règle empirique de 1/4\" de trou d\'aération pour chaque 100 pouces cubes de volume. Un seul trou d\'aération de la taille appropriée est sensible au bruit causé par les brises et les rafales de vent. Ces effets sont minimisés en utilisant plusieurs trous d\'aération répartis autour du volume, 3 trous étant considérés comme un minimum pratique. La surface combinée de tous les trous d\'aération sera équivalente à celle d\'un seul trou plus grand.

## Utilisation

![](images/Calc_vent_hole_size.png )

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Rocket_Calculator.svg" width=16px> [Vent Hole Size Calculator](Rocket_Vent_Hole_Size_Calculator/fr.md)**.
    -   Sélectionnez la **Rocket → Calculatrices → <img src="images/Rocket_Calculator.svg" width=16px> Vent Hole Size Calculator** dans le menu.
2.  Saisissez les paramètres de votre compartiment électronique.

## Calculs

La taille du trou de ventilation est calculée à l\'aide de la formule suivante :

$$D_{vent} = 0.004396 D \sqrt{\cfrac{L}{N}}$$

où

$$D_{vent} =$$taille du trou de ventilation

$$D =$$ diamètre du tube du corps

$$L =$$ longueur du tube du corps

$$N =$$ nombre de trous d\'aération

### Unités

Les calculs sont effectués en unités métriques, mais s\'affichent dans les unités de votre choix. Les valeurs peuvent également être saisies dans n\'importe quelle unité en incluant les unités dans la valeur (*ex* 5 oz, ou 23,2 g).

## Références

1.  <http://vernk.com/AltimeterPortSizing.htm>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > Rocket Vent Hole Size Calculator/fr
