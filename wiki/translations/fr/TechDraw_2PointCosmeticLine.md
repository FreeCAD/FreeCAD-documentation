---
- GuiCommand:/fr
   Name:TechDraw 2PointCosmeticLine
   Name/fr:TechDraw Ligne cosmétique par 2 points
   MenuLocation:TechDraw → Ajouter des lignes → Ajouter une ligne cosmétique par 2 points
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Ligne centrale à une face](TechDraw_FaceCenterLine/fr.md), [TechDraw Ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md)
---

## Description

L\'outil Ligne cosmétique ajoute une ligne cosmétique par deux points. Les points peuvent être 2D ou 3D. La ligne résultante peut être utilisée pour la cotation. L\'apparence de la ligne peut être modifiée à l\'aide de l\'outil [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md).

<img alt="" src=images/CosLine2PointsSample.png  style="width:200px;">


*Ligne cosmétique par 2 points*

## Utilisation

1.  Sélectionnez 2 sommets dans une vue ou 2 sommets dans la vue 3D.
2.  Appuyez sur le bouton **<img src="images/TechDraw-line2points.svg" width=16px> Ajouter une ligne cosmétique par 2 points**.
3.  Une boîte de dialogue s\'ouvre dans laquelle vous pouvez ajuster les coordonnées des 2 points.
4.  Une ligne sera ajoutée pour connecter les 2 sommets sélectionnés. Dans le cas de points 3D, la ligne reliera la projection des points sélectionnés.

Pour supprimer une ligne cosmétique, sélectionnez-la et utilisez le bouton de la barre d\'outils **<img src="images/TechDraw_CosmeticEraser.svg" width=16px> [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md)**.

## Modification des lignes cosmétiques 

Pour modifier les extrémités d\'une ligne cosmétique, **<img src="images/TechDraw-line2points.svg" width=16px> Ajouter une ligne cosmétique par 2 points**.

1.  Sélectionnez la ligne cosmétique.
2.  Appuyez sur **<img src="images/TechDraw-line2points.svg" width=16px> Ajoutez une ligne cosmétique par 2 points**.
3.  Une boîte de dialogue s\'ouvre dans laquelle vous pouvez modifier les coordonnées des extrémités.
4.  Appuyez sur **OK** pour voir vos modifications.

Pour modifier l\'apparence d\'une ligne cosmétique, utilisez [TechDraw Gomme](TechDraw_CosmeticEraser/fr.md).

## Propriétés

Les lignes cosmétiques n\'ont pas de propriétés propres car elles ne sont pas des objets du document final.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les lignes cosmétiques peuvent être créées à l\'aide des méthodes makeCosmeticLine(v1, v2) ou makeCosmeticLine3d(v1, v2) de DrawViewPart.





{{TechDraw Tools navi

}}  
