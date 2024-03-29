---
 GuiCommand:
   Name: TechDraw ShowAll
   Name/fr: TechDraw Montrer tout
   MenuLocation: TechDraw , Ajouter des lignes , Afficher/masquer les arrêtes invisibles
   Workbenches: TechDraw_Workbench/fr
   Version: 0.19
   SeeAlso: TechDraw_DecorateLine/fr
---

# TechDraw ShowAll/fr

## Description

L\'outil **TechDraw Montrer tout** outil permet d\'afficher temporairement, puis de masquer, des lignes invisibles dans une vue. Les lignes peuvent être rendues invisibles avec l\'outil [TechDraw Apparence des lignes](TechDraw_DecorateLine/fr.md). Notez que \"invisible\" est un état cosmétique, à ne pas confondre avec les lignes cachées qui sont des constructions géométriques.



## Utilisation

1.  Sélectionnez une vue avec des lignes invisibles sur une page ou dans la [vue en arborescence](Tree_view/fr.md).
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_ShowAll.svg" width=16px> [Afficher/masquer les arrêtes invisibles](TechDraw_ShowAll/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Ajouter des lignes → <img src="images/TechDraw_ShowAll.svg" width=16px> Afficher/masquer les arrêtes invisibles** du menu.
3.  Toutes les lignes invisibles de la vue sont affichées ou cachées.



## Remarques

-   Pour rendre les lignes invisibles visibles en permanence, utilisez <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;">. [TechDraw Apparence des lignes](TechDraw_DecorateLine/fr.md).



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les effets de l\'outil Montrer tout peut être dupliqué dans la [macro](Macros/fr.md) ou la console [Python](Python/fr.md). 
```python
v = App.ActiveDocument.View
vvo = v.ViewObject
vvo.ShowAllEdges = True
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShowAll/fr
