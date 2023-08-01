---
- GuiCommand:/fr
   Name:TechDraw View
   Name/fr:TechDraw Vue
   MenuLocation:TechDraw → Vues de Techdraw → Insérer une vue
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Projection de groupe](TechDraw_ProjectionGroup/fr.md), [TechDraw Vue de coupe](TechDraw_SectionView/fr.md)
---

# TechDraw View/fr

## Description

L\'outil **TechDraw Vue** ajoute une représentation d\'un ou plusieurs objets à une page de dessin. Il s\'agit de la composante de base de l\'atelier TechDraw. La plupart des autres vues sont dérivées d\'une manière ou d\'une autre de Vue.

La Vue dessine n\'importe quel objet qui a une propriété de `Shape`. Vous pouvez sélectionner des [esquisses](Sketcher_Workbench/fr.md), des [PartDesign corps](PartDesign_Body/fr.md), des [Draft objets](Draft_Workbench/fr.md) etc. La Vue extraira également toutes les formes des objets d\'un [Std Part](Std_Part/fr.md) ou d\'un [Std Groupe](Std_Group/fr.md).

![](images/TechDraw_View_example.png ) 
*Vue d'une boîte pleine avec des lignes cachées*



## Utilisation

1.  Faites pivoter la [vue 3D](3D_view/fr.md). À moins qu\'une face ne soit sélectionnée à l\'étape suivante, la direction de la caméra dans la [vue 3D](3D_view/fr.md) détermine la valeur initiale de la propriété **Direction** de la vue.
2.  Sélectionnez un ou plusieurs objets dans la [vue 3D](3D_view/fr.md) ou dans la [vue en arborescence](Tree_view/fr.md). Lors de la sélection dans la vue 3D, la première face sélectionnée détermine la valeur initiale de la propriété **Direction**.
3.  S\'il y a plusieurs pages de dessin dans le document : ajoutez éventuellement la page souhaitée à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
4.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_View.svg" width=16px> [Insérer une vue](TechDraw_View/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Vues de Techdraw → <img src="images/TechDraw_View.svg" width=16px> Insérer une vue** du menu.
5.  S\'il y a plusieurs pages de dessin dans le document et que vous n\'avez pas encore sélectionné de page, la boîte de dialogue **Sélecteur de page** s\'ouvre : {{Version/fr|0.20}}
    1.  Sélectionnez la page souhaitée.
    2.  Appuyez sur le bouton **OK**.



## Propriétés



### Données


{{TitleProperty|Base}}

-    **X|Distance**: position horizontale de la vue sur la page. (1)

-    **Y|Distance**: position verticale de la vue sur la page. (1)

-    **Lock Position|Bool**: empêche les vues d\'être déplacées dans l\'interface graphique si mis à `True`. La vue peut toujours être déplacée en modifiant les propriétés X,Y. (1)

-    **Rotation|Angle**: rotation dans le sens inverse des aiguilles d\'une montre de la vue sur la page en degrés. (1)

-    **Scale Type|Enumeration**: type d\'échelle. Options : (1)

    -   
        {{Value|Page}}
        
        : utilise le paramètre d\'échelle de la [Page](TechDraw_PageDefault/fr.md).

    -   
        {{Value|Automatic}}
        
        : adapte la vue à la page.

    -   
        {{Value|Custom}}
        
        : utilise l\'échelle définie par **Scale**.

-    **Scale|FloatConstant**: la vue sera rendue sur la page dans un rapport échelle:1 par rapport à la source. (1)

-    **Caption|String**: légende de texte courte optionnelle. (1)


{{TitleProperty|Cosmetics}}

-    **Cosmetic Vertexes|TechDraw::PropertyCosmeticVertexList|Hidden**
    

-    **Cosmetic Edges|TechDraw::PropertyCosmeticEdgeList|Hidden**
    

-    **Center Lines|TechDraw::PropertyCenterLineList|Hidden**
    

-    **Geom Formats|TechDraw::PropertyGeomFormatList|Hidden**
    


{{TitleProperty|HLR Parameters}}

-    **Coarse View|Bool**: si `True`, TechDraw utilisera une approximation polygonale pour calculer la géométrie du dessin. Si `False`, TechDraw utilisera un algorithme de précision. CoarseView peut être beaucoup plus rapide pour les modèles complexes. La qualité du dessin est réduite, car chaque courbe est approximée comme une série de segments de ligne courts. Les sommets ne sont pas affichés dans CoarseView, car chaque segment court entraînerait la création de deux nouveaux sommets et l\'affichage devient encombré. Les dimensions linéaires peuvent être ajoutées à une CoarseView, mais il est peu probable qu\'elles soient utiles.

-    **Smooth Visible|Bool**: active/désactive des lignes lisses visibles.

-    **Seam Visible|Bool**: active/désactive des lignes de couture visibles.

-    **Iso Visible|Bool**: active/désactive des lignes isométriques (u,v) visibles.

-    **Hard Hidden|Bool**: active/désactive des lignes cachées.

-    **Smooth Hidden|Bool**: active/désactive des lignes cachées lisses.

-    **Seam Hidden|Bool**: active/désactive des lignes de couture cachées.

-    **Iso Hidden|Bool**: active/désactive des lignes isométriques (u,v) cachées.

-    **Iso Count|Integer**: nombre de lignes isométriques (u,v) à dessiner sur chaque face.


{{TitleProperty|Projection}}

-    **Source|LinkList**: liens vers les objets dessinables à représenter.

-    **XSource|XLLinkList**: liens vers les objets dessinables dans un fichier externe.

-    **Direction|Vector**: ce vecteur contrôle la direction depuis laquelle vous regardez l\'objet. +X est la droite, -X est la gauche, +Y est l\'arrière, -Y est l\'avant (regardant dans l\'écran), +Z est le haut et -Z est le bas. Ainsi, une vue de face est (0,-1,0) et une vue isométrique est (1,-1,1).

-    **XDirection|Vector**: ce vecteur contrôle la rotation de la vue autour de la direction.

-    **Perspective|Bool**: `True` pour une projection en perspective, `False` pour une projection orthogonale.

-    **Focus|Distance**: distance entre la caméra et le plan de projection pour les projections en perspective. Doit être ajustée pour s\'adapter à l\'objet. Trop loin et la perspective est perdue, trop près et l\'objet est déformé.



### Vue


{{TitleProperty|Base}}

-    **Keep Label|Bool**: toujours afficher l\'étiquette de la vue si `True`. (1)

-    **Stack Order|Integer**: sur ou sous le niveau d\'empilement par rapport aux autres vues. (1) {{Version/fr|0.21}}


{{TitleProperty|Decoration}}

-    **Arc Center Marks|Bool**: active/désactive des marques centrales d\'arc de cercle.

-    **Center Scale|Float**: ajustement de la taille des marques centrales d\'arc de cercle, si activé.

-    **Horiz Center Line|Bool**: affiche une ligne centrale horizontale dans la vue.

-    **Section Line Color|Color**: définit la couleur de la ligne de section, le cas échéant.

-    **Section Line Style|Enumeration**: définit le style de ligne de la section, le cas échéant.

-    **Show All Edges|Bool**: affiche temporairement les lignes invisibles.

-    **Show Section Line|Bool**: affiche/masque la ligne de section, le cas échéant.

-    **Vert Center Line|Bool**: affiche une ligne centrale verticale dans la vue.


{{TitleProperty|Highlight}}

-    **Highlight Adjust|Float**: ajuste la rotation de la mise en évidence du détail, le cas échéant.

-    **Highlight Line Color|Color**: définit la couleur de la ligne de surbrillance, le cas échéant.

-    **Highlight Line Style|Enumeration**: définit le style de la ligne de mise en évidence, le cas échéant.


{{TitleProperty|Lines}}

-    **Extra Width|Length**: pas encore implémenté.

-    **Hidden Width|Length**: épaisseur des lignes cachées, si elles sont activées.

-    **Iso Width|Length**: épaisseur des lignes de surface isométriques (u,v) et des lignes de dimension.

-    **Line Width|Length**: épaisseur des lignes visibles. Voir [Groupe de lignes](TechDraw_LineGroup/fr.md).

\(1\) ces propriétés sont communes à tous les types de vues.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Une Vue coupe peut être crée à partir de [macros](Macros/fr.md) et de la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = [box]
view.Direction = (0, 0, 1)

view.X = page.PageWidth / 2
view.Y = page.PageHeight / 2

doc.recompute()
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/fr
