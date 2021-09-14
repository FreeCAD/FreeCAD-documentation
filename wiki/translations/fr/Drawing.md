# Drawing/fr



## Introduction

Dans FreeCAD, le mot \"[Drawing](Drawing/fr.md)\" est normalement utilisé pour faire référence à une projection 2D d\'un [modèle 3D](model/fr.md). Ceci est généralement créé avec l\'[atelier TechDraw](TechDraw_Workbench/fr.md).

## Utilisation

1.  Commencez avec un [modèle 3D](model/fr.md) déjà créé avec par exemple l\'[Atelier PartDesign](PartDesign_Workbench/fr.md). En fait, tout objet qui a une [Shape](Shape/fr.md) y compris les objets 2D, fonctionnera.
2.  Basculez vers l\'[Atelier TechDraw](TechDraw_Workbench/fr.md).
3.  Appuyez sur **<img src=images/TechDraw_PageDefault.svg style="width:16px"> <img src=images/TechDraw_PageTemplate.svg style="width:TechDraw Page par défaut](TechDraw_PageDefault/fr.md)** ou **[16px"> [TechDraw Page selon modèle](TechDraw_PageTemplate/fr.md)** pour créer une page.
4.  Sélectionnez le modèle existant, puis appuyez sur **<img src=images/TechDraw_View.svg style="width:16px"> <img src=images/TechDraw_ProjectionGroup.svg style="width:TechDraw Vue](TechDraw_View/fr.md)** ou **[16px"> [TechDraw Groupe de projections](TechDraw_ProjectionGroup/fr.md)**.
5.  Une projection 2D sur la page sera créée. Vous pouvez maintenant ajuster ses propriétés comme {{PropertyData/fr|Scale}}, {{PropertyData/fr|Rotation}} et {{PropertyData/fr|Direction}}.
6.  Lorsque le dessin est prêt, vous pouvez appuyer sur **<img src=images/TechDraw_ExportPageSVG.svg style="width:16px"> <img src=images/TechDraw_ExportPageDXF.svg style="width:TechDraw Exporter en SVG](TechDraw_ExportPageSVG/fr.md)**, **[16px"> [TechDraw Exporter en DXF](TechDraw_ExportPageDXF/fr.md)** ou utilisez [Std Exporter](Std_Export/fr.md) pour exporter la page aux formats SVG, DXF ou PDF pour une utilisation ultérieure dans un autre logiciel ou pour l\'impression.

## Remarques

Dans un usage informel, un \"Drawing\" peut être n\'importe quelle figure géométrique visible dans la [vue 3D](3D_view/fr.md), et donc son concept peut être confondu avec celui de \"[Corps](Body/fr.md)\", \"[Part](Part/fr.md)\" ou \"[modèle](Model/fr.md)\".

Cependant, lorsque plus de précision est requise, la distinction doit être faite.

-   Un \"[Corps](Body/fr.md)\" ([PartDesign Corps](PartDesign_Body/fr.md)) est un objet dérivé d\'une [Part Feature](Part_Feature/fr.md) classe (`Part::Feature`) créé avec l\'[Atelier PartDesign](PartDesign_Workbench/fr.md).
-   Un \"[Part](Part/fr.md)\" ([App Part](App_Part/fr.md)) est utilisé pour regrouper plusieurs \"[Bodies](Body/fr.md)\" pour former un assemblage.
-   Un \"Drawing\" est une projection 2D d\'un \"Body\" ou d\'une \"Part\".
-   Un \"Drawing\" peut également être créé avec l\'[Atelier Drawing](Drawing_Workbench/fr.md). Cependant, étant donné que ce plan de travail est devenu obsolète en 0.17, vous devriez préférer l\'[Atelier TechDraw](TechDraw_Workbench/fr.md) à la place.


{{TechDraw Tools navi

}} {{Document objects navi}} 

[Category:Glossary](Category:Glossary.md)
