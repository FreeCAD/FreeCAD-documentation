---
- GuiCommand:/fr
   Name:TechDraw ToggleFrame
   Name/fr:TechDraw Bascule des cadres
   MenuLocation:TechDraw → Activer ou désactiver les cadres de vues
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Vue](TechDraw_View/fr.md), [TechDraw Projection de groupe](TechDraw_ProjectionGroup/fr.md)
---

## Description

L\'outil Basculer l\'affichage des cadres active ou désactive l\'affichage des cadres de vue, des étiquettes et des sommets.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width:400px;"> 
*Vue de la projection solide avec les cadres activés et désactivés*

## Utilisation

1.  Si vous avez plusieurs pages de dessin dans votre document, vous devez sélectionner la page souhaitée dans l\'arborescence.
2.  Appuyez sur le bouton **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Activer ou désactiver les cadres de vues](TechDraw_ToggleFrame/fr.md)
**
3.  Si les cadres de vues sont actuellement visibles, ils disparaîtront. Si les cadres de vues ne sont pas visibles, ils apparaîtront.
4.  Il est possible que différentes vues soient dans différents états d\'affichage d\'image. Si cela se produit, appuyez sur le bouton **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Activer ou désactiver les cadres de vues](TechDraw_ToggleFrame/fr.md)** une ou deux fois pour resynchroniser les vues.

## Contexte

Le cadre de vue en pointillé et les points de sommet sont juste pour référence, ils ne font pas réellement partie du dessin donc vous ne les verrez pas une fois que vous exportez la page au format PDF ou SVG.

Le déroulement suggéré est d\'utiliser **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Activer ou désactiver les cadres de vues](TechDraw_ToggleFrame/fr.md)** pour désactiver le cadre entourant la vue ainsi que les points supplémentaires. Avec les points, utilisez les outils de mesure pour sélectionner les arêtes correctes à mesurer puis désactivez le cadre (et les points) pour voir le résultat final. Pas satisfait? Activez à nouveau le cadre (et les points), sélectionnez d\'autres sommets et créez de nouvelles mesures, puis désactivez à nouveau le cadre.

Vous pouvez ajuster la taille des points de sommet dans l\'onglet [TechDraw Préférences d\'échelle](TechDraw_Preferences/fr#.C3.89chelle.md). Veuillez ne pas définir leur taille à zéro, à la bonne taille pour que vous puissiez les récupérer facilement.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Basculer l\'affichage des cadres n\'a actuellement pas d\'interface de programmation.





{{TechDraw Tools navi

}}  
