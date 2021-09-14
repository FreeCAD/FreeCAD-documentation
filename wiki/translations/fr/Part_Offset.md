---
- GuiCommand:/fr
   Name:Part Offset
   Name/fr:Part Décalage 3D
   MenuLocation:Pièce → Décalage 3D...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Évidement](Part_Thickness/fr.md), [Part Décalage 2D](Part_Offset2D/fr.md)
---

## Description

L\'outil Décalage 3D de la pièce crée des copies parallèles d\'une forme sélectionnée à une certaine distance de la forme de base, créant ainsi un nouvel objet.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">

## Utilisation

1.  Sélectionnez l\'objet à partir duquel vous souhaitez créer le décalage.
2.  Appuyez sur le bouton **<img src="images/Part_Offset.svg" width=16px> '''Décalage 3D'''
**
3.  Ajustez la distance et les paramètres en fonction de l\'objet d\'origine et de la validité des objets résultants.

## Propriétés

-    {{PropertyData/fr|Offset}}: distance pour décaler les faces de la forme

-    {{PropertyData/fr|Mode}}: mode de création. Skin crée une nouvelle forme autour de la forme source. Tuyau (à faire). RectoVerso (à faire)

-    {{PropertyData/fr|Join type}}: Comment les nouveaux coins sont construits. L\'intersection donne des angles vifs par extension linéaire des arêtes. Arc et Tangent donnent des angles arrondis.

1.  Optionː intersection: permet aux décalages dirigés vers l\'intérieur de «déborder» de l\'interstice en croisant la forme obtenue jusqu\'à ce que les faces opposées soient atteintes.
2.  Optionː auto intersection (à faire).
3.  Optionː décalage de remplissageː lorsque la forme était bidimensionnelle, l\'espace entre les 2 formes est comblé. Le remplissage est maintenant un solide, donc la forme source n\'est pas un solide. Ainsi, les opérations booléennes peuvent conduire à des résultats étranges. (voir exemple ci-dessous).

## Exemples

Objet avec petits coins décalés et arrondis (arc).

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;"> 

L même objet avec des angles vifs (intersection).

<img alt="" src=images/PartOffset3.png  style="width:400" height="200px;"> 

Le même objet avec une distance importante surchargeant l'espace avant gauche et autorisant les intersections.

<img alt="" src=images/PartOffset2.png  style="width:400" height="200px;"> 

Forme arbitraire (draft poly en tant que fil) avec un décalage 3D (ignore le paramètre MODE).

<img alt="" src=images/PartOffset4.png  style="width:400" height="200px;"> 

La même forme avec un décalage 3D comme SKIN et un décalage \"rempli\".

<img alt="" src=images/PartOffset5.png  style="width:400" height="200px;"> 

Décalage *rempli* avec 2 cylindres créant des coupes booléennes. Le cylindre A passe par le REMPLISSAGE tandis que le cylindre B ne traverse que le REMPLISSAGE et non la forme 2D source.

<img alt="" src=images/PartOffset6.png  style="width:400" height="200px;"> 





  
