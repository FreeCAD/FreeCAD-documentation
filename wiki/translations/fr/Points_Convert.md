---
- GuiCommand:/fr
   Name:Points Convert
   Name/fr:Points Convertir
   MenuLocation:Points → Convertir en points...
   Workbenches:[Points](Points_Workbench/fr.md)
---

# Points Convert/fr

## Description

La commande **Points Convertir** crée des nuages de points à partir d\'objets de forme ou d\'objets maillés.

Ici, un objet forme fait référence à tout objet avec une propriété **Shape**. Les objets créés avec les ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md) sont des objets de forme. Mais il en va de même pour les objets créés avec les ateliers [Sketcher](Sketcher_Workbench/fr.md) et [Draft](Draft_Workbench/fr.md).



## Utilisation

1.  Sélectionnez un ou plusieurs objets.
2.  Sélectionnez l\'option **Points → Convertir en points...** dans le menu.
3.  La boîte de dialogue **Distance** s\'ouvre.
4.  Entrez la **distance maximale**. La valeur doit être comprise dans la plage {{Value|0.05}} - {{Value|10.0}}.
5.  Appuyez sur le bouton **OK** pour fermer la boîte de dialogue et terminer la commande.



## Propriétés

Les objets nuage de points sont des objets [App GeoFeature](App_GeoFeature/fr.md) avec des propriétés supplémentaires suivantes. Sélectionnez l\'option **Tout afficher** dans le menu contextuel de l\'[éditeur de propriétés](Property_editor.md) pour afficher les propriétés masquées.



### Données


{{TitleProperty|Structured points}}

-    **Height|Integer**: nombre de coordonnées Y uniques dans le nuage de points. Cette propriété n\'est disponible que pour les nuages de points créés avec la commande [Points Nuage structuré](Points_Structure/fr.md).

-    **Width|Integer**: nombre de coordonnées X uniques dans le nuage de points. Cette propriété n\'est disponible que pour les nuages de points créés avec la commande [Points Nuage structuré](Points_Structure/fr.md).



#### Données cachées 


{{TitleProperty|Base}}

-    **Points|PointsKernel**: un noyau de points associé à cet objet.

-    **Normal|NormalList**: liste de normales. Cette propriété n\'est disponible que pour les nuages de points créés avec la commande [Points Convertir](Points_Convert/fr.md) à partir d\'objets maillés ou d\'objets de forme avec des faces.



### Vue


{{TitleProperty|Base}}

-    **Point Size|FloatConstraint**: taille en pixels des points dans la [Vue 3D](3D_view/fr.md).





{{Points Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Convert/fr
