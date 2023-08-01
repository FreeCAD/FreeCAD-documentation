---
- GuiCommand:
   Name:Rocket FinCan
   Name/fr:Rocket Échappement avec ailerons
   MenuLocation:Rocket - Échappement avec ailerons
   Workbenches:[Rocket](Rocket_Workbench/fr.md)
   Version:0.19
---

# Rocket FinCan/fr

## Description

Les ailerons sont utilisés pour contrôler aérodynamiquement la direction du vol. Un Échappement avec ailerons est un ensemble complet comprenant des ailerons et un tube de corps, souvent monté sur l\'extérieur du tube de corps principal de la fusée. En option, un Échappement avec ailerons peut comprendre un sabot de lancement.

<img alt="" src=images/FinCan.png  style="width:256px;"> 
*Un Échappement avec ailerons avec un sabot de lancement*

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Rocket_FinCan.svg" width=16px> [Fin Can](Rocket_FinCan.md)**.
    -   Sélectionnez l\'option **Rocket → <img src="images/Rocket_FinCan.svg" width=16px> Fin Can** dans le menu.
    -   Double-cliquez sur un objet Fin dans la [Vue en arborescence](Tree_view/fr.md).
2.  Définissez les options et appuyez sur **OK**.

## Options

### Options des ailerons 

Les options pour l\'Échappement avec ailerons sont les mêmes que pour les ailerons seuls. Voir <img alt="" src=images/Rocket_Fin.svg  style="width:16px;"> [Ailerons](Rocket_Fin/fr.md) pour plus de détails.

Cependant, en raison de la nature monobloc des Échappements avec ailerons, elles ne peuvent pas inclure d\'ailerons à travers la paroi (TTW).

### Options de l\'échappement avec ailerons 

### Options du sabot de lancement 

## Propriétés


{{TitleProperty|Fin Can}}

-    **Fin Type**: définit la forme des ailerons.

-    **Height**: hauteur de l\'aileron.

-    **Profile**: esquisse associée au type d\'aileron personnalisé.

-    **Root Chord**: distance entre les bords d\'attaque et de fuite de l\'aileron à la racine.

-    **Root Cross Section**: forme de la section transversale de l\'aileron à l\'emplanture, voir [Options](#Options.md).

-    **Root Length 1**: l\'utilisation dépend de **Fin Root Cross Section** et s\'appliquera à une longueur conique ou similaire, voir [Options](#Options.md).

-    **Root Length 2**: l\'utilisation dépend de de **Fin Root Cross Section** et s\'appliquera à une longueur conique ou similaire lorsque plusieurs valeurs sont requises, voir [Options](#Options.md).

-    **Root Per Cent**: exprime les propriétés **Fin Root Length 1** et **Fin Root Length 2** en pourcentage de la **Fin Root Chord**.

-    **Root Thickness**: épaisseur maximale à la base de l\'aileron

-    **Sweep Angle**: angle de l\'avant de l\'aileron, avec un avant vertical égal à 0 degré. Cette valeur peut être négative. Le réglage de cette valeur entraînera l\'ajustement de la **Sweep Length**.

-    **Sweep Length**: distance entre l\'avant de l\'emplanture de l\'aileron et l\'avant de l\'extrémité de l\'aileron le long de l\'axe x. Cette valeur peut être négative. Si vous définissez cette valeur, **Sweep Angle** sera ajusté.

-    **Tip Chord**: distance entre le bord d\'attaque et le bord de fuite de l\'aileron à l\'extrémité.

-    **Tip Cross Section**: forme de la section transversale de l\'aileron à l\'extrémité, voir [Options](#Options.md).

-    **Tip Length 1**: l\'utilisation dépend de la **Fin Tip Cross Section** et s\'applique à une longueur conique ou similaire, voir [Options](#Options.md).

-    **Tip Length 2**: l\'utilisation dépend de la **Fin Tip Cross Section** et s\'appliquera à une longueur conique ou similaire lorsque plusieurs valeurs sont requises, voir [Options](#Options.md).

-    **Tip Per Cent**: exprime les propriétés **Fin Tip Length 1** et **Fin Tip Length 2** en pourcentage de la **Fin Tip Chord**.

-    **Tip Thickness**: épaisseur maximale à l\'extrémité de l\'ailette


{{TitleProperty|Rocket Component}}

Ces paramètres sont fournis à titre indicatif et n\'ont aucun effet sur la conception du composant.

-    **Description**: description du composant

-    **Manufacturer**: fabricant lorsqu\'il est connu

-    **Material**: matériau lorsqu\'il est connu

-    **Part Number**: numéro de pièce du fabricant

## Tutoriels et apprentissage 

[Aileron atelier Rocket](https://youtu.be/8MmEVyGkA0I) Tutoriel sur YouTube



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Rocket FinCan/fr
