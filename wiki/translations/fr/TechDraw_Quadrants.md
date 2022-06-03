---
- GuiCommand   */fr
   Name   *TechDraw Quadrants
   Name/fr   *TechDraw Sommets quadrants
   MenuLocation   *TechDraw → Ajouter des sommets → Ajouter des sommets de quadrants
   Workbenches   *[TechDraw](TechDraw_Workbench/fr.md)
   Version   *0.19
   SeeAlso   *[TechDraw Point cosmétique](TechDraw_CosmeticVertex/fr.md), [TechDraw Point milieu](TechDraw_Midpoints/fr.md)
---

# TechDraw Quadrants/fr

## Description

L\'outil Sommets quadrants ajoute des [Sommets cosmétiques](TechDraw_CosmeticVertex/fr.md) aux points 90/180/270° d\'un bord circulaire. Le sommet 0° devrait déjà figurer sous forme de sommet géométrique.

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width   *250px;"> 
*Les sommets cosmétiques au quadrant d'un cercle*

## Utilisation

1.  Sélectionnez une ou plusieurs arêtes (circulaires) dans une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_Quadrants.svg" width=16px> Ajouter des sommets de quadrants**.
3.  Les sommets cosmétiques seront ajoutés tous les 90° sur les bords.

**Remarque   *** cet outil peut être utilisé sur n'importe quel bord, pas seulement pour des cercles.

Pour supprimer un sommet de quadrant, sélectionnez-le et utilisez le bouton de la barre d\'outils **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [Gomme](TechDraw_CosmeticEraser/fr.md)**.

## Propriétés

Les points cosmétiques n\'ont pas de propriétés propres car ils ne sont pas des objets de document. Ils partagent les paramètres de couleur et de taille avec des points de géométrie réguliers.

## Script


**Voir aussi   ***

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les points cosmétiques ne sont pas accessibles par [macros](Macros/fr.md) ni par la console [Python](Python/fr.md) pour le moment. Ce bout de code supprimera tous les points cosmétiques de la vue.


```python
>>> v = App.ActiveDocument.View
>>> v.clearCV()
>>> App.activeDocument().recompute()
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Quadrants/fr
