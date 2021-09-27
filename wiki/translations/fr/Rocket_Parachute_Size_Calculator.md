---
- GuiCommand:/fr
   Name:Rocket Parachute Size Calculator
   Name/fr:Rocket Calcul taille parachute
   Icon:Rocket_Calculator.svg
   MenuLocation:Rocket → Calculators → Parachute Size Calculator
   Workbenches:[Rocket](Rocket_Workbench/fr.md)
   Version:0.19
---

# Rocket Parachute Size Calculator/fr

## Description

Ce calculateur détermine la taille du parachute nécessaire pour atteindre le taux de descente souhaité en fonction des paramètres du parachute.

Le taux de descente souhaité dépend de vos besoins. En règle générale, le parachute principal devrait ralentir la fusée à environ $6.1\,m/s\,(20\,f/s)$ tandis que le drone devrait permettre au parachute de descendre beaucoup plus rapidement $18.3\,m/s\,(60\,f/s)$ - $21.3\,m/s\,(70\,f/s)$. L\'éditeur dispose de préréglages pour ceux-ci, la valeur pour le parachute de freinage se situant au milieu de la plage. Vous pouvez définir un taux de descente personnalisé en fonction de vos besoins.

Une valeur clé pour déterminer le taux de descente est le coefficient de traînée ($C_D$). La valeur exacte de celui-ci dépendra de divers facteurs, notamment de la forme du parachute. Des préréglages sont fournis pour des parachutes découpés dans un morceau de matériau plat (rond, carré, hexagonal) comme ceux fournis par de nombreux kits, et pour une véritable forme de dôme. Votre fabricant de parachutes peut fournir une meilleure valeur pour ce coefficient.

## Utilisation

![](images/Calc_parachute_size.png )

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Rocket_Calculator.svg" width=16px> [Parachute Size Calculator](Rocket_Parachute_Size_Calculator/fr.md)**.
    -   Sélectionnez l\'option **Rocket → Calculators → <img src="images/Rocket_Calculator.svg" width=16px> Parachute Size Calculator** dans le menu.
2.  Saisissez le poids de votre fusée et les paramètres de votre parachute.

## Calculs

La taille du parachute est déterminée par la masse de la fusée, le taux de descente souhaité et les caractéristiques de traînée du parachute. Le calcul se fait en deux étapes. On calcule d\'abord la surface du parachute :

$$A = { 2mg \over { \rho v_T^2 C_D }}$$

où

$$m =$$ la masse de la fusée

$$v_T =$$vitesse terminale souhaitée

$$C_D =$$coefficient de traînée du parachute

$$\rho = 1.22$$ densité de l\'air, moyenne au niveau de la mer en $kg/m^3$ à $15C$.

$$g = 9.807$$ accélération due à la gravité en $m/s^2$.

Le diamètre est ensuite calculé à partir de la surface en fonction de la forme.

Pour les parachutes hexagonaux :

$$D = \sqrt{ 2A \over sqrt{3}}$$

Pour les parachutes carrés, le diamètre est la longueur de chaque côté.

$$D = \sqrt{A}$$

Pour tous les autres parachutes, la forme est supposée être circulaire.

$$D = \sqrt{ 4A \over \pi }$$

### Unités

Les calculs sont effectués en unités métriques, mais s\'affichent dans les unités de votre choix. Les valeurs peuvent également être saisies dans n\'importe quelle unité en incluant les unités dans la valeur (*ex* 5 oz, ou 23,2 g).

## Références

1.  <http://www.rocketmime.com/rockets/descent.html>
2.  <https://descentratecalculator.onlinetesting.net/>
3.  <https://www.math.net/area-of-a-hexagon>







_ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > Rocket Parachute Size Calculator/fr
