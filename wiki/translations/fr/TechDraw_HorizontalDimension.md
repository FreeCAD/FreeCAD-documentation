---
- GuiCommand:/fr
   Name:TechDraw HorizontalDimension
   Name/fr:TechDraw Cote horizontale
   MenuLocation:TechDraw → Dimensions → Insérer une cote horizontale
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Shortcut:**Maj** + **H**
   SeeAlso:[TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md), [TechDraw Cote verticale](TechDraw_VerticalDimension/fr.md)
---

# TechDraw HorizontalDimension/fr

## Description

L\'outil Cote horizontale ajoute une dimension horizontale à une vue. La dimension peut être entre deux sommets, la longueur d\'un bord ou la distance horizontale entre deux bords. La dimension sera initialement la distance projetée (c.-à-d. comme indiqué sur le dessin), mais elle peut être remplacée par la distance 3D réelle en utilisant l\'outil **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw Lier une dimension](TechDraw_LinkDimension/fr.md)
**

<img alt="" src=images/TechDraw_Dimension_Horizontal_example.png  style="width:200px;"> 
*Dimension de longueur prise à partir de deux nœuds arbitraires de la vue; la distance est mesurée horizontalement*

## Comment faire 

1.  Sélectionnez les points ou les arêtes qui définissent votre mesure.
2.  Appuyez sur le bouton **<img src="images/TechDraw_HorizontalDimension.svg" width=16px> [Insérer une cote horizontale](TechDraw_HorizontalDimension/fr.md)
**
3.  Une dimension sera ajoutée à la vue. La dimension peut être déplacée à la position désirée.
4.  Si nécessaire, ajoutez des tolérances comme décrit dans [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tol.C3.A9rances.md).

Pour modifier les propriétés d\'un objet dimension, double-cliquez dessus dans le dessin ou dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira la [Boîte de dialogue Dimension](TechDraw_LengthDimension/fr#Bo.C3.AEte_de_dialogue_Dimension.md).

## Limitations

Les objets Dimension sont vulnérables au \"[problèmes de nommage topologique](Topological_naming_problem/fr.md)\". Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md) pour plus d\'informations.

## Propriétés

Voir [Cote de longueur](TechDraw_LengthDimension/fr#Propri.C3.A9t.C3.A9s/fr.md).

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Cote horizontale peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalDimension/fr
