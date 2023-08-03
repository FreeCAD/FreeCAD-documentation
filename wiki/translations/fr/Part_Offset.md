---
 GuiCommand:
   Name: Part Offset
   Name/fr: Part Décalage 3D
   MenuLocation: Part , Décalage 3D...
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_Thickness/fr, Part_Offset2D/fr
---

# Part Offset/fr

## Description

L\'outil <img alt="" src=images/Part_Offset.svg  style="width:24px;"> **Part Décalage 3D** de la pièce crée des copies parallèles d\'une forme sélectionnée à une certaine distance de la forme de base, créant ainsi un nouvel objet.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">

## Utilisation

1.  Sélectionnez un objet à décaler.
2.  Appuyez sur le bouton **<img src="images/Part_Offset.svg" width=16px> [Décalage 3D](Part_Offset/fr.md)**.
3.  Ajustez la distance et les paramètres en fonction de l\'objet d\'origine et de la validité des objets résultants.

## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme objets sources. {{Version/fr|0.20}}

## Exemples

Objet avec petits coins décalés et arrondis (arc).

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">

Le même objet avec des angles vifs (intersection).

<img alt="" src=images/PartOffset3.png  style="width:400" height="200px;">

Le même objet avec une distance importante surchargeant l'espace avant gauche et autorisant les intersections.

<img alt="" src=images/PartOffset2.png  style="width:400" height="200px;">

Forme arbitraire (draft poly en tant que fil) avec un décalage 3D (ignore le paramètre MODE).

<img alt="" src=images/PartOffset4.png  style="width:400" height="200px;">

La même forme avec un décalage 3D comme SKIN et un décalage \"rempli\".

<img alt="" src=images/PartOffset5.png  style="width:400" height="200px;">

Décalage *rempli* avec 2 cylindres créant des coupes booléennes. Le cylindre A passe par le REMPLISSAGE tandis que le cylindre B ne traverse que le REMPLISSAGE et non la forme 2D source.

<img alt="" src=images/PartOffset6.png  style="width:400" height="200px;">

## Propriétés

-    **Offset**: Distance pour décaler les faces de la forme.

-    **Mode**: Mode de création. Skin crée une nouvelle forme autour de la forme source. Pipe (à faire). RectoVerso (à faire).

-    **Join type**: Comment les nouveaux coins sont construits. L\'intersection donne des angles vifs par extension linéaire des arêtes. Arc et Tangent donnent des angles arrondis.

1.  Option : Intersection : Permet aux décalages pointant vers l\'intérieur de \"déborder\" l\'espace en intersectant la forme résultante jusqu\'à ce que des faces opposées soient atteintes.
2.  Option : Auto intersection : (à faire).
3.  Option : Décalage de remplissage : Lorsque la forme était en 2 dimensions, l\'espace entre les 2 formes est rempli. Le remplissage est maintenant un solide, donc la forme source n\'est pas un solide. Ainsi les opérations booléennes peuvent conduire à des résultats étranges. (voir l\'exemple ci-dessous).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/fr
