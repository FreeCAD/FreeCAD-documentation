---
 TutorialInfo:r
   Topic: Ancrage
   Level: Intermédiaire/avancé
   Author: drmacro
   Time: 1 heure
   FCVersion: 0.19 ou supérieure
   Files: A définir
---

# Advanced Attachment OYX/fr





<img alt="" src=images/AttOYX_Setup.png  style="width:800px;"> 
*Les objets en position initiale*

## Introduction

Cette démonstration traite de l\'utilisation du mode d\'ancrage OYX pour ajuster la position de l\'origine d\'une esquisse comme décrit dans [Part Ancrage](Part_EditAttachment/fr.md), elle n\'est pas exhaustive, mais nous espérons qu\'elle aidera les utilisateurs à expérimenter.

L\'image ci-dessus montre la géométrie utilisée dans cette démonstration.

Le cadre inférieur droit montre la vue supérieure de la scène. Notez que la scène comprend une esquisse contenant un carré et du texte indiquant les axes vertical (Y) et horizontal (X) de l\'esquisse. Le coin inférieur gauche du carré est situé à 0,0,0 de l\'esquisse (l\'origine de l\'esquisse).

L\'origine de l\'esquisse et l\'origine globale (désignée par la [croix du repère](Std_AxisCross/fr.md) rouge, verte et bleue) sont les mêmes. Dans les autres images de l\'image, nous pouvons voir que le carré est à Z=0, donc l\'esquisse est dans le plan XY.

Deux autres esquisses comprennent une géométrie qui sera utilisée pour repositionner l\'esquisse contenant le carré. L\'une des esquisses contient une ligne orange orientée le long de l\'axe Z global dans le plan XZ. L\'autre esquisse contient une ligne jaune dans le plan XY.

## Discussion

Le mode d\'ancrage Aligner O-Y-X est défini comme suit dans [Part Ancrage](Part_EditAttachment/fr.md) : *Fait correspondre l\'origine de l\'objet avec le premier sommet référencé et aligne ses axes de plan vertical et horizontal vers le sommet/long de la ligne*. Elle indique également qu\'il existe plusieurs combinaisons de référence.

:; Combinaisons de référence:

:   sommet, sommet, sommet
:   sommet, sommet, arête
:   sommet, arête, sommet
:   sommet, arête, arête
:   sommet, sommet
:   sommet, arête

Commençons par *Sommet, Sommet, Sommet* (*Vertex, Vertex, Vertex*).

Si nous faisons correspondre la définition à la référence :

Le premier sommet sélectionné positionnera l\'origine de l\'esquisse sur le sommet sélectionné.

Le deuxième sommet sélectionné alignera l\'axe vertical de l\'esquisse (dans la configuration de la démo, cet axe est indiqué par **Y**).

Ainsi, si nous sélectionnons le sommet supérieur/gauche de l\'arête jaune (comme on le voit dans le cadre plus grand de droite) et le sommet inférieur/droit de l\'arête jaune, l\'esquisse est positionnée comme ceci :

<img alt="" src=images/AttOYX_vv.png  style="width:800px;">

:; Remarques :

:   L\'option Aligner O-Y-X est sélectionnée dans la fenêtre de dialogue Ancrage.
:   L\'origine de l\'esquisse se trouve maintenant au sommet supérieur gauche/supérieur de la ligne jaune.
:   L\'axe Y de l\'esquisse est maintenant aligné avec la ligne jaune.
:   L\'axe Z de l\'esquisse est perpendiculaire à la ligne jaune.

Maintenant, si nous ajoutons une troisième référence en sélectionnant le sommet supérieur de l\'arête orange, la situation devient la suivante :

<img alt="" src=images/AttOYX_vvv.png  style="width:800px;">

:; Remarques :

:   L\'axe X de l\'esquisse est maintenant aligné dans la direction du sommet sélectionné de l\'arête orange.



---
⏵ [documentation index](../README.md) > Advanced Attachment OYX/fr
