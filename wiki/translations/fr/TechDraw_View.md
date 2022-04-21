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

L\'outil Vue ajoute une représentation d\'un ou plusieurs objets à une page de dessin. Il s\'agit de la composante de base de l\'atelier TechDraw. La plupart des autres vues sont dérivées d\'une manière ou d\'une autre de Vue.

La Vue dessine n\'importe quel objet qui a une propriété de `Shape`. Vous pouvez sélectionner des [esquisses](Sketcher_Workbench/fr.md), des [corps](PartDesign_Body/fr.md), des [objets Draft](Draft_Workbench/fr.md) etc. La Vue extraira également toutes les formes des objets d\'un [Std Part](Std_Part/fr.md) ou d\'un [Std Groupe](Std_Group/fr.md).

![](images/TechDraw_View_example.png ) 
*Vue d'une boîte pleine avec des lignes cachées*

## Utilisation

1.  En outre, vous pouvez faire pivoter la [Vue 3D](3D_view/fr.md). La direction de la caméra dans la [Vue 3D](3D_view/fr.md) détermine la valeur initiale de la propriété **Direction** de la vue.
2.  Sélectionnez un ou plusieurs objets dans la [Vue 3D](3D_view/fr.md) ou la [vue en arborescence](Tree_view/fr.md).
3.  S\'il y a plusieurs pages de dessin dans le document : ajoutez éventuellement la page souhaitée à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md). Ceci n\'est pas possible pour {{VersionMinus/fr|0.19}}.
4.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_View.svg" width=16px> [Insérer une vue](TechDraw_View/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → <img src="images/TechDraw_View.svg" width=16px> Insérer une vue** dans le menu.
5.  S\'il y a plusieurs pages de dessin dans le document et que vous n\'avez pas encore sélectionné de page, la boîte de dialogue **Page Chooser** s\'ouvre : {{Version/fr|0.20}}
    1.  Sélectionnez la page souhaitée.
    2.  Appuyez sur le bouton **OK**.

## Propriétés

### Données


{{TitleProperty|Base}}

-    **X**: La position horizontale de la vue sur la page. (1)

-    **Y**: La position verticale de la vue sur la page. (1)

-    **Lock Position**: Empêche les vues d\'être glissées dans le Gui quand la valeur est True. La vue peut toujours être déplacée en changeant les propriétés X, Y. (1)

-    **Rotation**: Rotation antihoraire de la vue sur la page en degrés. (1)

-    **Scale Type**: \"Document\": utilise le paramètre d\'échelle de la page. \"Custom\": utilise une échelle unique pour cette vue. \"Automatic\": ajuste la vue à la page. (1)

-    **Scale**: Une vue sera rendue sur la page à l\'Échelle: 1 par rapport à la Source. (1)

-    **Caption**: Légende de texte court facultative.

\(1\) ces propriétés sont communes à tous les types de vues.


{{TitleProperty|Cosmetics}}


{{TitleProperty|HLR Parameters}}

-    **Coarse View**: Si Vrai, TechDraw utilisera une approximation de polygone pour calculer la géométrie de dessin. Si faux, TechDraw utilisera un algorithme de précision. CoarseView peut être beaucoup plus rapide pour les modèles complexes. La qualité du dessin est réduite car chaque courbe est approximée par une série de segments courts. Les sommets ne sont pas affichés dans CoarseView, car chaque segment court donnerait deux nouveaux sommets et l\'affichage deviendrait encombré. Des dimensions linéaires peuvent être ajoutées à un CoarseView, mais ne seront probablement pas utilisables.

-    **Smooth Visible**: Les lignes lisses visibles sont activées/désactivées.

-    **Seam Visible**: Les lignes de couture visibles sont activées/désactivées.

-    **Iso Visible**: Les lignes isométriques visibles (u,v) sont activées/désactivées.

-    **Hard Hidden**: Les lignes cachées (arêtes réelles) sont activées/désactivées.

-    **Smooth Hidden**: Les lignes lisses cachées sont activées/désactivées.

-    **Seam Hidden**: Les lignes de couture cachées sont activées/désactivées.

-    **Iso Hidden**: Les lignes isométriques cachées (u,v) sont activées/désactivées.

-    **Iso Count**: Nombre de lignes isométriques (u,v) à dessiner sur chaque face.


{{TitleProperty|Projection}}

-    **Source**: Liens vers les objets projetables à représenter

-    **Direction**: Ce vecteur contrôle la direction à partir de laquelle vous visualisez l\'objet. +X est à droite, -X est à gauche, +Y est à l\'arrière, -Y est à l\'avant (regardant dans l\'écran), +Z est en haut et -Z est en bas. Donc, une vue de face est (0,-1,0) et une vue isométrique est (1,-1,1).

-    **XDirection**: Ce vecteur contrôle la rotation de la vue autour de la direction. {{Version/fr|0.19}}.

-    **Perspective**: Vrai pour la projection en perspective, faux pour la projection orthogonale.

-    **Focus**: Distance de la caméra au plan de projection pour les projections en perspective. Doit être ajusté pour s\'adapter à l\'objet. Trop loin et la perspective est perdue, trop proche et l\'objet est déformé.

### Vue

-    **Keep Label**: Toujours afficher l\'étiquette de vue si la valeur est sur vrai.

-    **LineWidth**: Épaisseur des lignes visibles. Voir [Groupes de lignes](TechDraw_LineGroup/fr.md).

-    **HiddenWidth**: L\'épaisseur des lignes cachées, si activé.

-    **IsoWidth**: L\'épaisseur des lignes de surface isométriques (u,v) et des lignes de cotes.

-    **ExtraWidth**: Pas encore implémenté.

-    **ShowCenters**: Les marques de centre des arcs/cercles sont activées/désactivées.

-    **CenterScale**: Réglage de la taille de la marque du centre des arcs/cercles, si activé.

-    **HorizCenterLine**: Affiche un trait d\'axe horizontal dans la vue.

-    **VertCenterLine**: Affiche un trait d\'axe vertical dans la vue.

-    **ShowSectionLine**: Affiche/masque la ligne de coupe, le cas échéant.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Vue peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
FreeCAD.ActiveDocument.View.Source = [App.ActiveDocument.Box]
FreeCAD.ActiveDocument.View.Direction = (0.0,0.0,1.0)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/fr
