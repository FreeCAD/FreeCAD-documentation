---
- GuiCommand:/fr
   Name:TechDraw Dimension Horizontal Extent
   Name/fr:TechDraw Extension horizontale
   MenuLocation:TechDraw → Dimensions → Insérer une dimension d'extention horizontale
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Cote de longueur](TechDraw_Dimension_Length/fr.md), [TechDraw Extension verticale](TechDraw_Dimension_Vertical_Extent/fr.md)
---

## Description

L\'outil Dimension extension horizontale ajoute une dimension linéaire à une vue. La cote s\'étend du point le plus à gauche sur les objets sélectionnés au point le plus à droite. Un CosmeticVertex sera placé à chaque point.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Dimension d'extension horizontale d'un surface BSpline*

## Utilisation

1.  Sélectionnez une vue ou une collection d\'arêtes dans une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_Dimension_Horizontal_Extent.svg" width=16px> [Insérer une dimension d'extention horizontale](TechDraw_Dimension_Horizontal_Extent/fr.md)
**
3.  Une dimension sera ajoutée à la vue. La cote peut être déplacée à la position souhaitée.

## Limitations

Les objets de dimension sont vulnérables aux problèmes de \"[nommage topologique](topological_naming_problem/fr.md)\". Consultez les informations de l\'outil **<img src="images/TechDraw_Dimension_Length.svg" width=16px> [TechDraw Longueur](TechDraw_Dimension_Length/fr.md)** pour plus d\'informations.

## Propriétiés

Cet objet a les mêmes propriétés que l\'outil [TechDraw dimension longueur](TechDraw_Dimension_Length/fr.md). Voir cet outil pour plus de détails. Les exceptions notées.

### Données

-    {{PropertyData/fr|MeasureType}}: `True` - basé sur la géométrie 3D ou \"projeté\" - basé sur le dessin. Normalement pas manipulé directement par l\'utilisateur final. Pas encore implémenté pour Dimension Horizontal Extension.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Dimension Horizontal Extent peut être utilisé dans [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, HORIZONTAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}  
