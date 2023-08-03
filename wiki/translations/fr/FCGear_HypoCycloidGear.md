---
 GuiCommand:
   Name: FCGear HypoCycloidGear
   Name/fr: FCGear Engrenage hypocycloïde
   MenuLocation: Gear , HypoCycloid Gear
   Workbenches: FCGear_Workbench/fr
   Shortcut: Aucun
   Version: 1.0
   SeeAlso: 
---

# FCGear HypoCycloidGear/fr

## Description

La commande <img alt="" src=images/FCGear_HypoCycloidGear.svg  style="width:16px;"> **FCGear Engrenage hypocycloïde** crée deux disques à cames cannelés et un ensemble de galets qui restent en contact avec la surface extérieure des disques pendant le mouvement.

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-04.png  style="width:200px;"> <img alt="" src=images/FCGear_FCGear_HypoCycloidGear-05.png  style="width:200px;"> 
*A gauche : engrenage hypocycloïde. A droite : engrenage et transparence avec un engrenage inversé et un jeu de galets*

Veuillez fournir une brève description de ce qui peut être réalisé en utilisant un tel train d'engrenages.

## Utilisation

1.  Passez à l\' <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [atelier FCGear](FCGear_Workbench/fr.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le **[<img src=images/FCGear_HypoCycloidGear.svg style="width:16px"> [HypoCycloid Gear](FCGear_HypoCycloidGear/fr.md)** dans la barre d\'outils.
    -   Sélectionnez **Gear → [<img src=images/FCGear_HypoCycloidGear.svg style="width:16px"> HypoCycloid Gear** dans le menu.
3.  Modifiez le paramètre de l\'engrenage en fonction des conditions requises (voir [Propriétés](#Propri.C3.A9t.C3.A9s.md)).

## Propriétés

## Remarques

Le ou les engrenages par défaut s\'affichent comme suit :

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-01.png  style="width:200px;">

Pour afficher les disques à cames et le jeu de galets (broches) dans des couleurs différentes, nous avons besoin de trois objets HypocycloidGear identiques. Leur visibilité peut être modifiée :

-    **show_disk0|Bool**pour le disque à cames principal.

-    **show_disk1|Bool**pour le disque à cames inversé situé au-dessus.

-    **show_pins|Bool**pour le jeu de broches.

<img alt="" src=images/FCGear_FCGear_HypoCycloidGear-02.png  style="width:200px;"> <img alt="" src=images/FCGear_FCGear_HypoCycloidGear-03.png  style="width:200px;"> 
*A gauche : objets HypocycloidGear tels que créés. A droite : objets repositionnés pour obtenir une meilleure vue sur chaque objet*

## Script



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear HypoCycloidGear/fr
