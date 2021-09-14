---
- GuiCommand:/fr
   Name:TechDraw Dimension Radius
   Name/fr:TechDraw Cote de rayon
   MenuLocation:TechDraw → Dimensions → Insérer une nouvelle cote de rayon
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Cote de diamètre](TechDraw_Dimension_Diameter/fr.md)
---

## Description

L\'outil Dimension de Rayon ajoute une dimension de rayon à une vue. La cote peut être appliquée à n\'importe quel bord du dessin qui est un cercle ou un arc de cercle. La distance sera initialement la distance projetée (c\'est-à-dire, comme indiqué sur le dessin), mais elle peut être remplacée par la distance 3D réelle à l\'aide de l\'outil **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Lier une dimension](TechDraw_Dimension_Link/fr.md)**.

<img alt="" src=images/TechDraw_Dimension_Radius_example.png  style="width:130px;"> 
*Mesurer un cercle, indiquant le rayon*

## Comment faire 

1.  Sélectionnez un cercle ou un arc de cercle dans le dessin. (Remarquez que certains arcs qui semblent être circulaires sont en fait des ellipses ou des BSplines. Vous ne pouvez pas créer de cote de rayon dans ces cas-là)
2.  Appuyez sur le bouton **<img src="images/TechDraw_Dimension_Radius.svg" width=16px> [Insérer une nouvelle cote de rayon](TechDraw_Dimension_Radius/fr.md)
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

L\'outil Dimension Radius peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Radius"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}  
