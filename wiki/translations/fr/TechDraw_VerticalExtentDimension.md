---
- GuiCommand:/fr
   Name:TechDraw VerticalExtentDimension
   Name/fr:TechDraw Extension verticale
   MenuLocation:TechDraw → Dimensions → Insérer une dimension d'extension verticale
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md), [TechDraw Extension horizontale](TechDraw_HorizontalExtentDimension/fr.md)
---

# TechDraw VerticalExtentDimension/fr

## Description

L\'outil Extension verticale ajoute une dimension linéaire à une vue. La dimension s\'étend du point le plus bas sur les objets sélectionnés au point le plus haut. Un CosmeticVertex (point cosmétique) sera placé à chaque point.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Dimension d'extension verticale d'une surface B-spline*

## Utilisation

1.  Sélectionnez une vue ou une collection d\'arêtes dans une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_VerticalExtentDimension.svg" width=16px> [Insérer une dimension d'extension verticale](TechDraw_VerticalExtentDimension/fr.md)**.
3.  Une dimension sera ajoutée à la vue. La cote peut être déplacée à la position souhaitée.

## Limitations

Les objets Dimension sont vulnérables au \"[problèmes de nommage topologique](Topological_naming_problem/fr.md)\". Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md) pour plus d\'informations.

## Propriétés

Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr#Propri.C3.A9t.C3.A9s.md). Exceptions notées ci-dessous.

### Données

-    {{PropertyData/fr|MeasureType}}: `True` - basé sur la géométrie 3D ou \"projeté\" - basé sur le dessin. N\'est normalement pas manipulé directement par l\'utilisateur final. Pas encore implémenté pour Dimension Vertical Extension.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Extension verticale peut être utilisé dans [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, VERTICAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalExtentDimension/fr
