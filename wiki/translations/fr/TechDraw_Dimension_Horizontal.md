---
- GuiCommand:/fr
   Name:TechDraw  Dimension Horizontal
   Name/fr:TechDraw Cote horizontale
   MenuLocation:TechDraw → Dimensions → Insérer une nouvelle cote horizontale
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Shortcut:**Maj** + **H**
   SeeAlso:[TechDraw Cote de longueur](TechDraw_Dimension_Length/fr.md), [TechDraw Cote verticale](TechDraw_Dimension_Vertical/fr.md)
---

## Description

L\'outil Distance Horizontale ajoute une dimension horizontale à une vue. La dimension peut être entre deux sommets, la longueur d\'un bord ou la distance horizontale entre deux bords. La dimension sera initialement la distance projetée (c.-à-d. comme indiqué sur le dessin), mais elle peut être remplacée par la distance 3D réelle en utilisant l\'outil **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Lier une Dimension](TechDraw_Dimension_Link/fr.md)
**

<img alt="" src=images/TechDraw_Dimension_Horizontal_example.png  style="width:200px;"> 
*Dimension de longueur prise à partir de deux nœuds arbitraires de la vue; la distance est mesurée horizontalement*

## Comment faire 

1.  Sélectionnez les points ou les arêtes qui définissent votre mesure.
2.  Appuyez sur le bouton**<img src="images/TechDraw_Dimension_Horizontal.svg" width=16px> [Insérer une cote horizontale](TechDraw_Dimension_Horizontal/fr.md)
**
3.  Une dimension sera ajoutée à la vue. La dimension peut être déplacée à la position désirée.
4.  Si nécessaire, ajoutez des tolérances comme décrit dans [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tol.C3.A9rances.md).

Pour modifier les propriétés d\'un objet dimension, double-cliquez dessus dans le dessin ou dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira la [Boîte de dialogue Dimension](TechDraw_Dimension_Length/fr#Bo.C3.AEte_de_dialogue_Dimension.md).

## Limitations

Les objets de dimension sont vulnérables aux problèmes de \"nommage topologique\". Consultez les informations de l\'outil [TechDraw Dimension Longueur](TechDraw_Dimension_Length/fr.md) pour plus d\'informations.

## Propriétés

Cet objet a les mêmes propriétés que l\'outil [TechDraw Dimension Longueur](TechDraw_Dimension_Length/fr.md). Voir cet outil pour plus de détails.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Dimension Horizontal peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "DistanceX"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
