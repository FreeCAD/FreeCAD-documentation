---
 GuiCommand:
   Name: TechDraw ExtensionCreateVertCoordDimension
   Name/fr: TechDraw Cotes parallèles verticales
   MenuLocation: TechDraw , Extensions : cotes , Cotes parallèles verticales
   Workbenches: TechDraw_Workbench/fr
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_ExtensionCreateHorizCoordDimension/fr, TechDraw_ExtensionCreateObliqueCoordDimension/fr
---

# TechDraw ExtensionCreateVertCoordDimension/fr

## Description

L\'outil **TechDraw Cotes parallèles verticales** crée des cotes de coordonnées verticales : plusieurs cotes régulièrement espacées partant de la même ligne de base.

<img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimensionExample.png  style="width:400px;"> 
*A droite, les cotes créées*



## Utilisation

1.  Spécifiez à votre convenance les attributs de ligne avec l\'outil <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width:16px;"> [TechDraw Choix des attributs](TechDraw_ExtensionSelectLineAttributes/fr.md).
2.  Sélectionnez trois sommets ou plus.
3.  L\'ordre de sélection des deux premiers sommets détermine la position de la ligne de base. Si le premier sommet sélectionné se trouve sous le second, la ligne de base est créée au sommet le plus bas, sinon elle est créée au sommet le plus haut.
4.  Il existe plusieurs façons de lancer l\'outil :
    -   
        {{Version/fr|1.0}}
        
        : si la [préférence](TechDraw_Preferences/fr#Cotes.md) **Outils de cotation** est réglée sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite du bouton **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/TechDraw_ExtensionCreateHorizChainDimension.svg" width=16px> Cotes horizontales** du menu déroulant.

    -   Si cette préférence a une valeur différente (et dans {{VersionMinus/fr|0.21}}) : appuyez sur le bouton **<img src="images/TechDraw_ExtensionCreateVertCoordDimension.svg" width=16px> [Cotes parallèles verticales](TechDraw_ExtensionCreateVertCoordDimension/fr.md)**.

    -   Sélectionnez l\'option **TechDraw → Extensions : cotes → <img src="images/TechDraw_ExtensionCreateVertCoordDimension.svg" width=16px> Cotes parallèles verticales** du menu.
5.  Des cotes avec des textes de cotes centrés sont créées.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionCreateVertCoordDimension/fr
