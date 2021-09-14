---
- GuiCommand:/fr
   Name:Path DressupDragKnife
   Name/fr:Path Habillage pour lame rotative
   MenuLocation:Path → Path Dressup → Trajectoire additionnelle couteau tangentiel
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Balise d'attache](Path_DressupTag/fr.md), [Path Rampe d'entrée](Path_DressupRampEntry/fr.md), [Path Dégagement d'angles](Path_DressupDogbone/fr.md)
---

## Description

Une lame rotative utilise un tranchant sur un pivot pour couper le matériau en feuille comme le vinyle, le carton et le cuir. Le point de coupe n\'est pas aligné avec le centre de la broche mais suit le mouvement de la broche. Parce que le point de coupe est décalé, le chemin doit être modifié pour dépasser le point d\'extrémité de chaque segment. En outre, la lame rotative est incapable de faire des virages extrêmement serrés. Pour compenser, une \'action de coin\' de pivot est insérée et soulève légèrement la lame puis pivote dans la nouvelle position.

Cet outil ajoute au tracé existant des actions de coin et des extensions de bord pour définir le tracé de la lame.

## Utilisation

1.  Sélectionnez un objet contour ou profil [Path](Path_Workbench/fr.md)
2.  Cliquez sur l\'élément de menu <img alt="" src=images/Path_DressupDragKnife.svg  style="width:16px;"> [Trajectoire additionnelle couteau tangentiel](Path_DressupDragKnife/fr.md)

## Options

-   Filter Angle - Détermine le degré de précision d\'un angle avant l\'insertion d\'une action dans un coin.
-   Offset - Décalage du point de la lame par rapport au centre de la broche.
-   Pivot Height - Détermine à quelle hauteur soulever la lame de coupe pendant une action dans un coin. Cela dépend du matériau et devrait être plus élevé pour les matériaux plus épais. Idéalement, le point doit rester légèrement dans le matériau.





{{Path_Tools_navi

}} 
