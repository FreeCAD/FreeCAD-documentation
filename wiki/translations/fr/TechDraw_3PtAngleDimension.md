---
- GuiCommand:/fr
   Name:TechDraw 3PtAngleDimension
   Name/fr:TechDraw Cote angulaire par 3 points
   MenuLocation:TechDraw → Insérer une cote angulaire par 3 points
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.18
   SeeAlso:[TechDraw Cote angulaire](TechDraw_AngleDimension/fr.md)
---

# TechDraw 3PtAngleDimension/fr

## Description

L\'outil Mesure d\'angle par 3 points ajoute une cote angulaire à une vue. La dimension peut être spécifiée en sélectionnant trois sommets dans une vue. **Notez que le second des trois sommets est le sommet de l\'angle**. La Mesure d\'angle par 3 pts sera initialement l\'angle projeté (c\'est-à-dire, comme indiqué sur le dessin) mais peut être remplacé par la distance 3D réelle à l\'aide de l\'outil **<img src="images/TechDraw_LinkDimension.svg" width=16px> [TechDraw Lier une dimension](TechDraw_LinkDimension/fr.md)**.

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Mesurer l'angle entre deux lignes droites à l'aide de trois sommets; le deuxième sommet devrait être le sommet de l'angle*

## Comment faire 

1.  Sélectionnez les points ou les arêtes qui définissent votre mesure.
2.  Appuyez sur le bouton **<img src="images/TechDraw_3PtAngleDimension.svg" width=16px> [Insérer une cote angulaire par 3 points](TechDraw_3PtAngleDimension/fr.md)**.
3.  Une dimension sera ajoutée à la vue. La cote peut être déplacée à la position souhaitée.
4.  Si nécessaire, ajoutez des tolérances comme décrit dans [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tol.C3.A9rances.md).

Pour modifier les propriétés d\'un objet dimension, double-cliquez dessus dans le dessin ou dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira la [Boîte de dialogue Dimension](TechDraw_LengthDimension/fr#Bo.C3.AEte_de_dialogue_Dimension.md).

## Limitations

Les objets Dimension sont vulnérables au \"[problèmes de nommage topologique](Topological_naming_problem/fr.md)\". Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md) pour plus d\'informations.

## Propriétés

Voir [Cote de longueur](TechDraw_LengthDimension/fr#Propri.C3.A9t.C3.A9s/fr.md).

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Cote angulaire par 3 points peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw 3PtAngleDimension/fr
