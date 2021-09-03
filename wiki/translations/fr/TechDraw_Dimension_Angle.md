---
- GuiCommand:/fr
   Name:TechDraw Dimension Angle
   Name/fr:TechDraw  Dimension d'Angle
   MenuLocation:TechDraw → Dimension d'Angle
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Mesure d'angle par 3 pts](TechDraw_Dimension_Angle3Pt/fr.md)
---


</div>

## Description

L\'outil Dimension d\'Angle ajoute une dimension angulaire à une vue. La dimension peut être l\'angle intérieur entre deux bords rectilignes quelconques. La dimension sera initialement l\'angle projeté (c.-à-d. comme indiqué sur le dessin), mais elle peut être remplacée par l\'angle 3D réel à l\'aide de l\'outil **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Lier une dimension](TechDraw_Dimension_Link/fr.md)
**

<img alt="" src=images/TechDraw_Dimension_Angle_example.png  style="width:200px;"> 
*Mesurer l'angle entre deux droites*

## Comment faire {#comment_faire}

1.  Sélectionnez les points ou les arêtes qui définissent votre mesure.
2.  Appuyez sur le bouton**<img src="images/TechDraw_Dimension_Angle.svg" width=16px> [Dimension d'Angle](TechDraw_Dimension_Angle/fr.md)
**
3.  Une dimension sera ajoutée à la vue. La dimension peut être déplacée à la position désirée.
4.  Si nécessaire, ajoutez des tolérances comme décrit dans [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tol.C3.A9rances.md).

Pour modifier les propriétés d\'un objet dimension, double-cliquez dessus dans le dessin ou dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira la [Boîte de dialogue Dimension](TechDraw_Dimension_Length/fr#Bo.C3.AEte_de_dialogue_Dimension.md).

## Limitations

Les objets de dimension sont vulnérables aux \"[problèmes de nommage topologique](topological_naming_problem/fr.md)\". Consultez les informations de l\'outil [TechDraw Dimension Longueur](TechDraw_Dimension_Length/fr.md) pour plus d\'informations.

## Propriétés

Cet objet a les mêmes propriétés que l\'outil [TechDraw Dimension Longueur](TechDraw_Dimension_Length/fr.md). Voir cet outil pour plus de détails.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Angle de cote peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle"
dim1.References2D=[(view1, 'Edge1')]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
