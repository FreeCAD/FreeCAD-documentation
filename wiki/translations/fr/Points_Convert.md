---
- GuiCommand:/fr
   Name:Points Convert
   Name/fr:Points Conversion
   MenuLocation:Points → Convertir en points...
   Workbenches:[Points](Points_Workbench/fr.md)
---

## Description

La commande **Points Conversion** crée des nuages de points à partir d\'objets de forme ou d\'objets maillés.

Ici, un objet forme fait référence à tout objet avec une propriété {{PropertyData/fr|Shape}}. Les objets créés avec les ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md) sont des objets de forme. Mais il en va de même pour les objets créés avec les ateliers [Sketcher](Sketcher_Workbench/fr.md) et [Draft](Draft_Workbench/fr.md).

## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Sélectionnez l\'option **Points → Convertir en points...** dans le menu.
3.  La boîte de dialogue **Distance** s\'ouvre.
4.  Entrez la **distance maximale**. La valeur doit être comprise dans la plage {{Value|0.05}} - {{Value|10.0}}.
5.  Appuyez sur le bouton **OK** pour fermer la boîte de dialogue et terminer la commande.

## Propriétés

Les objets nuage de points sont des objets [App GeoFeature](App_GeoFeature/fr.md) avec des propriétés supplémentaires suivantes. Sélectionnez l\'option **Show all** dans le menu contextuel [Éditeur de propriétés](Property_editor/fr.md) pour afficher les propriétés masquées.

### Données


{{TitleProperty|Structured points}}

-    {{PropertyData/fr|Height|Integer}}: le nombre de coordonnées Y uniques dans le nuage de points. Cette propriété n\'est disponible que pour les nuages de points créés avec la commande [Points Structure](Points_Structure/fr.md).

-    {{PropertyData/fr|Width|Integer}}: le nombre de coordonnées X uniques dans le nuage de points. Cette propriété n\'est disponible que pour les nuages de points créés avec la commande [Points Structure](Points_Structure/fr.md).

#### Données cachées 


{{TitleProperty|Base}}

-    {{PropertyData/fr|Points|PointsKernel}}: un point PointsKernel associé à cet objet.

-    {{PropertyData/fr|Normal|NormalList}}: une liste de normales. Cette propriété n\'est disponible que pour les nuages de points créés avec la commande [Points Conversion](Points_Convert/fr.md) à partir d\'objets maillés ou d\'objets de forme avec des faces.

### Vue


{{TitleProperty|Base}}

-    {{PropertyView/fr|Point Size|FloatConstraint}}: la taille en pixels des points dans la [Vue 3D](3D_view/fr.md).





{{Points Tools navi

}} 
