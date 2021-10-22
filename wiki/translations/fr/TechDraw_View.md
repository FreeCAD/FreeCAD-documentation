---
- GuiCommand:/fr
   Name:TechDraw View
   Name/fr:TechDraw Vue
   MenuLocation:TechDraw → Insérer une vue
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Projection de groupe](TechDraw_ProjectionGroup/fr.md), [TechDraw Vue de coupe](TechDraw_SectionView/fr.md)
---

# TechDraw View/fr

## Description

L\'outil Vue ajoute une représentation d\'un ou plusieurs objets à une Page de dessin. C\'est le bloc de construction de base de l\'atelier TechDraw. La plupart des autres vues sont dérivées d\'une manière ou d\'une autre de Nouvelle Vue.

![](images/TechDraw_View_example.png ) 
*Vue d'une boîte pleine avec des lignes cachées*

## Utilisation

1.  Sélectionnez un ou plusieurs objets (Corps, App::Part, Part::Feature, Draft object, \... Voir Remarques) dans la [fenêtre 3D](3D_view/fr.md) ou dans la [vue en arborescence](Tree_view/fr.md).
2.  Si vous avez plusieurs pages de dessin dans votre document, vous devrez également sélectionner la page souhaitée dans l\'arborescence. Utilisez le **Ctrl** pour sélectionner plusieurs éléments dans l\'arborescence.
3.  Appuyez sur le bouton **<img src="images/TechDraw_View.svg" width=16px> [Insérer une vue](TechDraw_View/fr.md)
**

-   La Vue dessine n\'importe quel objet qui a une propriété de `Shape`. Vous pouvez également sélectionner des objets _ ou un [Group](Std_Group/fr.md).

## Propriétés

### Données

-    {{PropertyData/fr|X}}: La position horizontale de la vue sur la page. (1)

-    {{PropertyData/fr|Y}}: La position verticale de la vue sur la page. (1)

-    {{PropertyData/fr|LockPosition}}: Empêche les vues d\'être glissées dans le Gui quand la valeur est True. La vue peut toujours être déplacée en changeant les propriétés X, Y. (1)

-    {{PropertyData/fr|Rotation}}: Rotation antihoraire de la vue sur la page en degrés. (1)

-    {{PropertyData/fr|ScaleType}}: \"Document\": utilise le paramètre d\'échelle de la page. \"Custom\": utilise une échelle unique pour cette vue. \"Automatic\": ajuste la vue à la page. (1)

-    {{PropertyData/fr|Scale}}: Une vue sera rendue sur la page à l\'Échelle: 1 par rapport à la Source. (1)

-    {{PropertyData/fr|Caption}}: Légende de texte court facultative.


{{TitleProperty|Cosmetics}}


{{TitleProperty|HLR Parameters}}

-    {{PropertyData/fr|CoarseView}}: Si Vrai, TechDraw utilisera une approximation de polygone pour calculer la géométrie de dessin. Si faux, TechDraw utilisera un algorithme de précision. CoarseView peut être beaucoup plus rapide pour les modèles complexes. La qualité du dessin est réduite car chaque courbe est approximée par une série de segments courts. Les sommets ne sont pas affichés dans CoarseView, car chaque segment court donnerait deux nouveaux sommets et l\'affichage deviendrait encombré. Des dimensions linéaires peuvent être ajoutées à un CoarseView, mais ne seront probablement pas utilisables.

:   
    **Note:**CoarseView est affecté par un bogue en amont dans OCCT ([\# 3332](https://www.freecadweb.org/tracker/view.php?id=3332)). La position de la vue sur la page est légèrement différente des valeurs X, Y spécifiées.

-    {{PropertyData/fr|Smooth Visible}}: Les lignes lisses visibles sont activées/désactivées.

-    {{PropertyData/fr|Seam Visible}}: Les lignes de couture visibles sont activées/désactivées.

-    {{PropertyData/fr|Iso Visible}}: Les lignes isométriques visibles (u, v) sont activées/désactivées.

-    {{PropertyData/fr|Hard Hidden}}: Les lignes cachées (arêtes réelles) sont activées/désactivées.

-    {{PropertyData/fr|Smooth Hidden}}: Les lignes lisses cachées sont activées/désactivées.

-    {{PropertyData/fr|Seam Hidden}}: Les lignes de couture cachées sont activées/désactivées.

-    {{PropertyData/fr|Iso Hidden}}: Les lignes isométriques cachées (u, v) sont activées/désactivées.

-    {{PropertyData/fr|Iso Count}}: Nombre de lignes isométriques (u, v) à dessiner sur chaque face.


{{TitleProperty|Projection}}

-    {{PropertyData/fr|Source}}: Liens vers les objets projetables à représenter

-    {{PropertyData/fr|Direction}}: Ce vecteur contrôle la direction à partir de laquelle vous visualisez l\'objet. +X est à droite, -X est à gauche, +Y est à l\'arrière, -Y est à l\'avant (regardant dans l\'écran), +Z est en haut et -Z est en bas. Donc, une vue de face est (0,-1,0) et une vue isométrique est (1,-1,1). (1)

-    {{PropertyData/fr|XDirection}}: ce vecteur contrôle la rotation de la vue autour de la direction. {{Version/fr|0.19}}. (1)

-    {{PropertyData/fr|Perspective}}: Vrai pour la projection en perspective, faux pour la projection orthogonale.

-    {{PropertyData/fr|Focus}}: Distance de la caméra au plan de projection pour les projections en perspective. Doit être ajusté pour s\'adapter à l\'objet. Trop loin et la perspective est perdue, trop proche et l\'objet est déformé.

\(1\) ces propriétés sont communes à tous les types de vues.

### Vue

-    {{PropertyView/fr|Keep Label}}: Toujours afficher l\'étiquette de vue si la valeur est sur vrai.

-    {{PropertyView/fr|LineWidth}}: Épaisseur des lignes visibles. Voir [Groupes de lignes](TechDraw_LineGroup/fr.md).

-    {{PropertyView/fr|HiddenWidth}}: L\'épaisseur des lignes cachées, si activé.

-    {{PropertyView/fr|IsoWidth}}: L\'épaisseur des lignes de surface isométriques (u, v) et des lignes de cotes.

-    {{PropertyView/fr|ExtraWidth}}: Pas encore implémenté.

-    {{PropertyView/fr|ShowCenters}}: Les marques de centre des arcs/cercles sont activées / désactivées.

-    {{PropertyView/fr|CenterScale}}: Réglage de la taille de la marque du centre des arcs / cercles, si activé.

-    {{PropertyView/fr|HorizCenterLine}}: Affiche un trait d\'axe horizontal dans la vue.

-    {{PropertyView/fr|VertCenterLine}}: Affiche un trait d\'axe vertical dans la vue.

-    {{PropertyView/fr|ShowSectionLine}}: Affiche/masque la ligne de coupe, le cas échéant.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Nouvelle vue peut être utilisé dans des [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
FreeCAD.ActiveDocument.View.Source = [App.ActiveDocument.Box]
FreeCAD.ActiveDocument.View.Direction = (0.0,0.0,1.0)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/fr
