---
- GuiCommand:/fr
   Name:TechDraw DiameterDimension
   Name/fr:TechDraw Cote de diamètre
   MenuLocation:TechDraw → Dimensions → Insérer une cote de diamètre
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Cote de rayon](TechDraw_RadiusDimension/fr.md)
---

# TechDraw DiameterDimension/fr

## Description

L\'outil Cote de diamètre ajoute une dimension de diamètre à une vue. La cote peut être appliquée à n\'importe quelle entité circulaire dans le dessin. La dimension sera initialement la distance projetée (c.-à-d. comme indiqué sur le dessin), mais elle peut être remplacée par la distance 3D réelle en utilisant l\'outil **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw Lier une dimension](TechDraw_LinkDimension/fr.md)
**

<img alt="" src=images/TechDraw_Dimension_Diameter_example.png  style="width:130px;"> 
*Mesurer un cercle, indiquant le diamètre*

## Utilisation

1.  Sélectionnez un bord circulaire dans le dessin. (Notez que certains arcs qui semblent être circulaires sont en fait des ellipses ou des B-splines. Vous ne pouvez pas créer de dimension de diamètre dans ces cas-là)
2.  Appuyez sur le bouton **<img src="images/TechDraw_DiameterDimension.svg" width=16px> [Insérer une cote de diamètre](TechDraw_DiameterDimension/fr.md)
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

L\'outil Cote de diamètre peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Diameter"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DiameterDimension/fr
