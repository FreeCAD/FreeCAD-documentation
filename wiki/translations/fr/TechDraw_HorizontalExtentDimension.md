---
- GuiCommand   */fr
   Name   *TechDraw HorizontalExtentDimension
   Name/fr   *TechDraw Extension horizontale
   MenuLocation   *TechDraw → Dimensions → Insérer une dimension d'extention horizontale
   Workbenches   *[TechDraw](TechDraw_Workbench/fr.md)
   Version   *0.19
   SeeAlso   *[TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md), [TechDraw Extension verticale](TechDraw_VerticalExtentDimension/fr.md)
---

# TechDraw HorizontalExtentDimension/fr

## Description

L\'outil Extension horizontale ajoute une dimension linéaire à une vue. La cote s\'étend du point le plus à gauche sur les objets sélectionnés au point le plus à droite. Un CosmeticVertex (point cosmétique) sera placé à chaque point.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width   *400px;"> 
*Dimension d'extension horizontale d'un surface BSpline*

## Utilisation

1.  Sélectionnez une vue ou une collection d\'arêtes dans une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Insérer une dimension d'extention horizontale](TechDraw_HorizontalExtentDimension/fr.md)
**
3.  Une dimension sera ajoutée à la vue. La cote peut être déplacée à la position souhaitée.

## Limitations

Les objets Dimension sont vulnérables au \"[problèmes de nommage topologique](Topological_naming_problem/fr.md)\". Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md) pour plus d\'informations.

## Propriétiés

Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr#Propri.C3.A9t.C3.A9s.md). Exceptions notées ci-dessous.

### Données

-    {{PropertyData/fr|MeasureType}}   * `True` - basé sur la géométrie 3D ou \"projeté\" - basé sur le dessin. Normalement pas manipulé directement par l\'utilisateur final. Pas encore implémenté pour Dimension Horizontal Extension.

## Script


**Voir aussi   ***

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Extension horizontale peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes   *


```python
selection = ['Edge1', 'Edge2']                      # or [] for all

TechDraw.makeExtentDim(view1, selection, 0)         # view1 is a DrawViewPart; 0 for horizontal
App.ActiveDocument.DimExtent.Y = -60                # offset dimension line from dimensioned edges in Y direction
App.ActiveDocument.DimExtent.X = 10                 # offset dimension text along dimension line in X direction
App.ActiveDocument.DimExtent.FormatSpec = '%.0f'    # Dimension format

TechDraw.makeExtentDim(view1, selection, 1)         # view1 is a DrawViewPart; 1 for vertical
App.ActiveDocument.DimExtent001.X = -130            # offset dimension line from dimensioned edges in X direction
App.ActiveDocument.DimExtent001.Y = 10              # offset dimension text along dimension line in Y direction
App.ActiveDocument.DimExtent001.FormatSpec = '%.0f'

# Note the dimension names are 'DimExtent', 'DimExtent001' etc in the order created.
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/fr
