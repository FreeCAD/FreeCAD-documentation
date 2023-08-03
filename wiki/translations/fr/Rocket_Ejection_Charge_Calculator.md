---
 GuiCommand:
   Name: Rocket Ejection Charge Calculator
   Name/fr: Rocket Calcul charge d'éjection
   Icon: Rocket_Calculator.svg
   MenuLocation: Rocket , Calculators , Ejection Charge Calculator
   Workbenches: Rocket_Workbench/fr
   Version: 0.19
---

# Rocket Ejection Charge Calculator/fr

## Description


**Ce calculateur ne donne qu'une estimation de la quantité de poudre nécessaire. Une quantité trop importante ou trop faible peut entraîner l'échec de la récupération ou endommager votre fusée<br>'''TOUJOURS''' faire un essai au sol de votre fusée avant le vol**

L\'éjection se produit lorsque la chambre contenant le système de récupération est pressurisée avec une force suffisante pour éjecter le système de récupération de la chambre. La force nécessaire peut varier en fonction d\'un certain nombre de facteurs :

  - Diamètre et volume du tube du corps

  - Masse du système de nez et de récupération

  - Méthode d\'éjection, par exemple, les systèmes de piston nécessitent moins de pression

  - Présence de goupilles de cisaillement utilisés pour empêcher la séparation de la traînée

  - Ajustement du système de récupération dans le tube de corps

En tant que tel, ce calculateur ne vous donnera qu\'une estimation de départ. Une quantité de poudre trop faible entraînera l\'échec de l\'éjection et de la récupération. Trop de poudre peut endommager la fusée ou le système de récupération, ce qui peut également entraîner l\'échec de la récupération. Il est **TOUJOURS** nécessaire de faire un test au sol avant de faire voler votre fusée.

Lors du calcul du volume du tube de la carlingue, il est rarement nécessaire d\'inclure la longueur totale. Par exemple, l\'épaulement de la coiffe ou la baie électronique peuvent consommer un certain volume. Ajustez votre spécification de longueur en conséquence.

Il existe quelques règles empiriques qui peuvent être appliquées sur la base d\'années d\'expérience de plusieurs constructeurs de fusées. La principale préoccupation ici est la force appliquée à la partie éjectable, généralement le cône de la coiffe ou la baie électronique. Les forces d\'éjection à cette interface doivent être comprises entre 150 et 200 lbf (\~667 à 890 N). La pression requise peut alors être calculée en fonction du volume de la chambre. Cette pression sera moindre pour les grands diamètres et plus importante pour les petits diamètres. Il existe des préréglages dans le calculateur pour définir ces forces (réglages bas et haut dans la boîte combo).

Les essais au sol doivent commencer à l\'extrémité inférieure de la plage recommandée pour éviter d\'endommager votre fusée. Augmentez la quantité au besoin pour assurer une récupération sécuritaire.

## Utilisation

![](images/Calc_ejection_charge.png )

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Rocket_Calculator.svg" width=16px> [Ejection Charge Calculator](Rocket_Ejection_Charge_Calculator/fr.md)** .
    -   Sélectionnez l\'option **Rocket → Calculatrices → <img src="images/Rocket_Calculator.svg" width=16px> Ejection Charge Calculator** dans le menu.
2.  Saisissez le poids de votre fusée et les paramètres de votre parachute.

## Calculs

La pression est définie par la force désirée, ou la force peut être définie en spécifiant la pression désirée. Celle-ci est basée sur la force appliquée à la zone située à l\'extrémité du volume à pressuriser.

$$P = \cfrac{F}{\pi {\left ( \cfrac{D}{2} \right )}^2}$$

où

$$F =$$ force désirée
$$D =$$ diamètre du tube du corps

Une fois que la pression souhaitée est connue, la quantité de poudre noire peut être calculée en utilisant la formule suivante

$$m = \cfrac{ PV }{ R_{c}Tg }$$

où

$$P =$$la pression calculée dans l\'équation précédente
.

$$V =$$ le volume de la chambre à pressuriser
$$R_{c} = 12.1579\, \frac{m}{K}$$, constante des gaz de combustion pour la poudre noire FFFFg
.

$$T = 1739\, K$$, température des gaz de combustion
$$g = 9.807\, \frac{m}{s^2}$$, accélération due à la gravité

### Unités

Les calculs sont effectués en unités métriques, mais s\'affichent dans les unités de votre choix. Les valeurs peuvent également être saisies dans n\'importe quelle unité en incluant les unités dans la valeur (*ex* 5 oz, ou 23,2 g).

## Références

1.  <http://vernk.com/EjectionChargeSizing.htm>
2.  <https://www.insanerocketry.com/blackpowder.html>
3.  <https://rocketrycalculator.com/rocketry-calculator/bp-estimator>
4.  <http://www.rockethead.net/black_powder_calculator.htm>
5.  <http://hararocketry.org/hara/resources/how-to-size-ejection-charge/>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Rocket Ejection Charge Calculator/fr
