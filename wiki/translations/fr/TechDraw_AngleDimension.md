---
- GuiCommand:/fr
   Name:TechDraw AngleDimension
   Name/fr:TechDraw Cote angulaire
   MenuLocation:TechDraw → Dimensions → Insérer une cote d'angulaire
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Cote angulaire par 3 points](TechDraw_Dimension_Angle3Pt/fr.md)
---

## Description

L\'outil Cote angulaire ajoute une dimension angulaire à une vue. La dimension peut être l\'angle intérieur entre deux bords rectilignes quelconques. La dimension sera initialement l\'angle projeté (c.-à-d. comme indiqué sur le dessin), mais elle peut être remplacée par la distance 3D réel à l\'aide de l\'outil **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw Lier une dimension](TechDraw_LinkDimension/fr.md)
**

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Mesurer l'angle entre deux droites*

## Comment faire 

1.  Sélectionnez les points ou les arêtes qui définissent votre mesure.
2.  Appuyez sur le bouton **<img src="images/TechDraw_AngleDimension.svg" width=16px> [Insérer une cote angulaire](TechDraw_AngleDimension/fr.md)
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

L\'outil Cote angulaire peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}} 
