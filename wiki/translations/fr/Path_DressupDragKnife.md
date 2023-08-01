---
- GuiCommand:
   Name: Path DressupDragKnife
   Name/fr: Path Lame rotative
   MenuLocation: Path - Finition du parcours - Lame rotative
   Workbenches: [Path](Path_Workbench/fr.md)
   SeeAlso: [Path Attaches](Path_DressupTag/fr.md), [Path Rampe d'entrée](Path_DressupRampEntry/fr.md), [Path Dégagement d'angles](Path_DressupDogbone/fr.md)
---

# Path DressupDragKnife/fr

## Description

L\'outil <img alt="" src=images/Path_DressupDragKnife.svg  style="width:24px;"> [Lame rotative](Path_DressupDragKnife/fr.md) utilise un tranchant sur un pivot pour couper le matériau en feuille comme le vinyle, le carton et le cuir. Le point de coupe n\'est pas aligné avec le centre de la broche mais suit le mouvement de la broche. Parce que le point de coupe est décalé, le chemin doit être modifié pour dépasser le point d\'extrémité de chaque segment. En outre, la lame rotative est incapable de faire des virages extrêmement serrés. Pour compenser, une \'action de coin\' de pivot est insérée et soulève légèrement la lame puis pivote dans la nouvelle position.

Cet outil ajoute au tracé existant des actions de coin et des extensions de bord pour définir le tracé de la lame.



## Utilisation

1.  Sélectionnez un contour ou un profil d\'objets [Path](Path_Workbench/fr.md).
2.  Sélectionnez l\'option **Path → Finition du parcours → <img src="images/Path_DressupDragKnife.svg" width=16px> Lame rotative** du menu.

## Options

-   **Précision de l\'angle** : détermine le degré de précision d\'un angle avant l\'insertion d\'une action dans un coin.
-   **Décalage** : décalage du point de la lame par rapport au centre de la broche.
-   **Hauteur du pivot** : détermine à quelle hauteur soulever la lame pendant une action dans un coin. Cela dépend du matériau et devrait être plus élevé pour les matériaux plus épais. Idéalement, le point doit rester légèrement dans le matériau.





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupDragKnife/fr
