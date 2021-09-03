---
- GuiCommand:/fr
   Name:TechDraw Dimension Angle3Pt
   Name/fr:TechDraw Mesure d'angle par 3 pts
   MenuLocation:TechDraw → Insérer une cote angulaire
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.18
   SeeAlso:[TechDraw Mesure d'angle](TechDraw_Dimension_Angle/fr.md)
---


</div>

## Description

L\'outil <img alt="" src=images/TechDraw_Dimension_Angle3Pt.svg  style="width:24px;"> Mesure d\'angle par 3 pts ajoute une cote angulaire à une vue. La dimension peut être spécifiée en sélectionnant trois sommets dans une vue. 
**Notez que le second des trois sommets est le sommet de l\'angle**. Mesure d\'angle par 3 pts sera initialement l\'angle projeté (c\'est-à-dire, comme indiqué sur le dessin), mais cet angle peut être remplacé par l\'angle 3D réel à l\'aide de l\'outil **<img src="images/TechDraw_Dimension_Link.svg" width=16px> [Lier une dimension](TechDraw_Dimension_Link/fr.md)**

<img alt="" src=images/TechDraw_Dimension_Angle3Pt_example.png  style="width:200px;"> 
*Mesurer l'angle entre deux lignes droites à l'aide de trois sommets; le deuxième sommet devrait être le sommet de l'angle*

## Comment faire {#comment_faire}

1.  Sélectionnez les points ou les arêtes qui définissent votre mesure.
2.  Appuyez sur le bouton **<img src="images/TechDraw_Dimension_Angle3Pt.png" width=16px> [Insérer une cote angulaire](TechDraw_Dimension_Angle3Pt/fr.md)**.
3.  Une dimension sera ajoutée à la vue. La cote peut être déplacée à la position souhaitée.
4.  Si nécessaire, ajoutez des tolérances comme décrit dans [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tol.C3.A9rances.md).

Pour modifier les propriétés d\'un objet dimension, double-cliquez dessus dans le dessin ou dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira la [Boîte de dialogue Dimension](TechDraw_Dimension_Length/fr#Bo.C3.AEte_de_dialogue_Dimension.md).

## Limitations

Les objets de dimension sont vulnérables aux \"[problèmes de nommage topologique](topological_naming_problem/fr.md)\". Consultez les informations de l\'outil <img alt="" src=images/TechDraw_Dimension_Length.svg  style="width:16px;"> [TechDraw Dimension de longueur](TechDraw_Dimension_Length/fr.md) pour plus d\'informations.

## Propriétés

Cet objet a les mêmes propriétés que l\'outil [Dimension de longueur](TechDraw_Dimension_Length/fr.md). Voir cet outil pour plus de détails.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Dimension Angle3Pt peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDimension','Dimension')
dim1.Type = "Angle3Pt"
dim1.References2D=[(view1, 'Vertex1',(view1, 'Vertex4'),(view1, 'Vertex2'))]
rc = page.addView(dim1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}  
