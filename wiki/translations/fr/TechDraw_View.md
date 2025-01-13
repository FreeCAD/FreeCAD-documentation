---
 GuiCommand:
   Name: TechDraw View
   Name/fr: TechDraw Vue
   MenuLocation: TechDraw , Vues de Techdraw , Insérer une vue
   Workbenches: TechDraw_Workbench/fr
   SeeAlso: TechDraw_ProjectionGroup/fr, TechDraw_SpreadsheetView/fr, TechDraw_ArchView, TechDraw_Symbol/fr, TechDraw_Image/fr
---

# TechDraw View/fr

## Description

L\'outil **TechDraw Vue** ajoute une représentation d\'un ou plusieurs objets à une page de dessin. {{Version/fr|1.0}}: il peut créer un [élément de groupe de projection (une seule vue)](#Propriétés_Groupe_de_projection_d'un_élément.md), un [groupe de projection](TechDraw_ProjectionGroup/fr.md), une [vue de Spreadsheet](TechDraw_SpreadsheetView/fr.md), une [vue de Arch](TechDraw_ArchView.md), un [symbole](TechDraw_Symbol.md) ou une [vue d\'une image](TechDraw_Image.md).

Jusqu\'à la {{VersionMinus/fr|0.21}}, l\'outil ne pouvait créer qu\'une [vue de Part](#Propriétés_Vue_de_Part.md), très similaire à un élément de groupe de projection.

![](images/TechDraw_View_example.png ) 
*Vue d'une boîte pleine avec des lignes cachées*



## Utilisation Groupe de projection d\'élément et Groupe de projection 

1.  Vous pouvez faire pivoter la [vue 3D](3D_view/fr.md). La direction de la caméra dans la vue 3D peut être utilisée pour définir la direction de projection de la vue principale.
2.  Sélectionnez un ou plusieurs objets avec une propriété **Shape** dans la vue 3D ou la [vue en arborescence](Tree_view/fr.md). Vous pouvez également sélectionner des [Std Parts](Std_Part/fr.md) ou des [Std Groupes](Std_Group/fr.md) qui contiennent de tels objets. Lors de la sélection dans la vue 3D, la première face sélectionnée peut être utilisée pour définir la direction de projection de la vue primaire. Ne sélectionnez pas d\'objets en choisissant une face dans la vue 3D si vous souhaitez utiliser la direction en cours de la caméra.
3.  S\'il y a plusieurs pages de dessin dans le document : vous pouvez ajouter la page souhaitée à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
4.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le **<img src="images/TechDraw_View.svg" width=16px> [Insérer une vue](TechDraw_View/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Vues de Techdraw → <img src="images/TechDraw_View.svg" width=16px> Insérer une vue** du menu.
5.  S\'il y a plusieurs pages de dessin dans le document, et si aucune page n\'est affichée dans la [zone de vue principale](Main_view_area/fr.md) et que vous n\'avez pas encore sélectionné de page, la fenêtre de dialogue **Sélecteur de pages** s\'ouvre :
    1.  Sélectionnez la page souhaitée.
    2.  Appuyez sur le bouton **OK**.
6.  Le panneau de tâches **Vue de l\'objet** s\'ouvre. {{Version/fr|1.0}}
7.  Vous pouvez ajuster les paramètres :
    -   **Échelle** : sélectionnez {{Value|Feuille}}, {{Value|Automatique}} ou {{Value|Personnalisée}}. Si la dernière option est sélectionnée, entrez le numérateur et le dénominateur de l\'échelle.
    -   **Direction** : utilisez les boutons disponibles pour ajuster la direction de projection et la rotation de la vue primaire :
        -   Le bouton **[#.## #.## #.##]** au centre indique la direction de projection actuelle. La valeur initiale dépend de la [préférence](TechDraw_Preferences/fr#Général.md) **Utiliser la direction de la caméra 3D**. Appuyez sur le bouton pour ajuster la direction de la vue et la rotation manuellement.
        -   Appuyez sur le bouton **<img src="images/Arrow-up.svg" width=16px>**, **<img src="images/Arrow-down.svg" width=16px>**, **<img src="images/Arrow-left.svg" width=16px>** ou **<img src="images/Arrow-right.svg" width=16px>** pour faire pivoter la direction de projection de 90° autour de l\'axe horizontal ou vertical de la vue.
        -   Appuyez sur le bouton **<img src="images/Arrow-cw.svg" width=16px>** ou **<img src="images/Arrow-ccw.svg" width=16px>** pour faire pivoter la vue de 90° autour de la direction de projection.
        -   Appuyez sur le bouton **<img src="images/TechDraw_ProjFront.svg" width=16px>** pour définir la direction de projection de la vue principale sur la vue standard [Vue de face](Std_ViewFront/fr.md).
        -   Appuyez sur le bouton **<img src="images/TechDraw_CameraOrientation.svg" width=16px>** pour la définir sur la première face sélectionnée, si disponible, ou sinon sur la direction actuelle de la caméra.
    -   **Projections secondaires** : vous pouvez crée des projections secondaires en plus de la vue principale. Au moins une projection secondaire doit être spécifiée pour que toutes les commandes de cette section soient affichées.
8.  Après avoir modifié certains paramètres, il peut être nécessaire d\'appuyer sur le bouton **Appliquer** pour mettre à jour la (les) vue(s).
9.  Appuyez sur le bouton **OK**.
10. Un [groupe de projection d\'un élément](#Propriétés_Groupe_de_projection_d'un_élément.md) ou, s\'il y a une ou plusieurs projections secondaires, un [groupe de projection](TechDraw_ProjectionGroup/fr.md) est inséré.

![](images/TechDraw_View_Taskpanel.png ) 
*[Panneau des tâches](Task_panel/fr.md) Vue de l'objet*



## Utilisation pour d\'autres types de vues 


{{Version/fr|1.0}}

1.  Vous pouvez sélectionner une [feuille de calcul](Spreadsheet_CreateSheet/fr.md) dans la [vue en arborescence](Tree_view/fr.md) ou un [Arch Plan de coupe](Arch_SectionPlane/fr.md) dans la [vue 3D](3D_view/fr.md) ou la vue en arborescence.
2.  Suivez les étapes 3, 4 et 5 comme expliqué [ci-dessus](#Utilisation_Groupe_de_projection_d'élément_et_Groupe_de_projection.md).
3.  Si vous n\'avez pas sélectionné une feuille de calcul ou un plan de coupe de Arch :
    1.  Une fenêtre de dialogue d\'avertissement s\'ouvre :
    2.  Cochez la case **Ne plus afficher ce message** pour éviter cette fenêtre de dialogue à l\'avenir.
    3.  Appuyez sur le bouton **OK**.
    4.  Un navigateur de fichiers s\'ouvre.
    5.  Sélectionnez un fichier SVG ou un fichier image.
    6.  Une [vue de Spreadsheet](TechDraw_SpreadsheetView/fr.md), une [vue de Arch](TechDraw_ArchView/fr.md), un [symbole](TechDraw_Symbol/fr.md) ou une [image](TechDraw_Image/fr.md) est inséré.
4.  Dans le cas d\'une vue de feuille de calcul : ajustez la plage de cellules de la vue en modifiant ses propriétés **Cell Start** et **Cell End**.
5.  Dans le cas d\'un symbole ou d\'une image : vous pouvez modifier sa propriété **Scale** pour ajuster sa taille.



## Propriétés Vue de Part 

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Une vue de Part, en fait un objet {{Incode|TechDraw::DrawViewPart}}, a les propriétés suivantes :



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

-    **Scrub Count|Integer**: le nombre de fois que FreeCAD doit essayer de nettoyer le résultat des lignes cachées supprimées. {{Version/fr|0.21}}


{{TitleProperty|Projection}}

-    **Source|LinkList**: liens vers les objets dessinables à représenter.

-    **XSource|XLLinkList**: liens vers les objets dessinables dans un fichier externe.

-    **Direction|Vector**: ce vecteur contrôle la direction depuis laquelle vous regardez l\'objet. +X est la droite, -X est la gauche, +Y est l\'arrière, -Y est l\'avant (regardant dans l\'écran), +Z est le haut et -Z est le bas. Ainsi, une vue de face est (0,-1,0) et une vue isométrique est (1,-1,1).

-    **XDirection|Vector**: ce vecteur contrôle la rotation de la vue autour de la direction.

-    **Perspective|Bool**: `True` pour une projection en perspective, `False` pour une projection orthogonale.

-    **Focus|Distance**: distance entre le plan de la caméra et le plan de projection pour les projections en perspective. Doit être ajustée pour s\'adapter à l\'objet. Trop loin et la perspective est perdue, trop près et l\'objet est déformé.



### Vue


{{TitleProperty|Base}}

-    **Keep Label|Bool**: toujours afficher l\'étiquette de la vue si `True`. (1)

-    **Stack Order|Integer**: sur ou sous le niveau d\'empilement par rapport aux autres vues. (1) {{Version/fr|0.21}}


{{TitleProperty|Broken View}}

-    **Break Line Style|Enumeration**: définit le style de la ligne de rupture, quand cela est possible. {{Version/fr|1.0}}

-    **Break Line Type|Enumeration**: ajuste le type de représentation de la ligne de rupture sur les vues interrompues, quand cela est possible : {{Value|None}}, {{Value|ZigZag}} or {{Value|Simple}}. {{Version/fr|1.0}}


{{TitleProperty|Decoration}}

-    **Arc Center Marks|Bool**: active/désactive des marques centrales d\'arc de cercle.

-    **Center Scale|Float**: ajustement de la taille des marques centrales d\'arc de cercle, si activé.

-    **Horiz Center Line|Bool**: affiche une ligne centrale horizontale dans la vue.

-    **Show All Edges|Bool**: affiche temporairement les lignes invisibles.

-    **Vert Center Line|Bool**: affiche une ligne centrale verticale dans la vue.


{{TitleProperty|Faces}}

-    **Face Color|Color**: définit la couleur des faces. {{Version/fr|1.0}}

-    **Face Transparency|Percent**: définit la transparence des faces. {{Version/fr|1.0}}


{{TitleProperty|Highlight}}

-    **Highlight Adjust|Float**: ajuste la rotation de la mise en évidence du détail, le cas échéant.

-    **Highlight Line Color|Color**: définit la couleur de la ligne de surbrillance, le cas échéant.

-    **Highlight Line Style|Enumeration**: définit le style de la ligne de mise en évidence, le cas échéant.


{{TitleProperty|Lines}}

-    **Extra Width|Length**: pas encore implémenté.

-    **Hidden Width|Length**: épaisseur des lignes cachées, si elles sont activées.

-    **Iso Width|Length**: épaisseur des lignes de surface isométriques (u,v) et des lignes de dimension.

-    **Line Width|Length**: épaisseur des lignes visibles. Voir [Groupe de lignes](TechDraw_LineGroup/fr.md).


{{TitleProperty|Section Line}}

-    **Include Cut Line|Bool**: affiche/masque la ligne de coupe de la section, quand cela est possible. {{Version/fr|1.0}}

-    **Section Line Color|Color**: définit la couleur de la ligne de la section, quand cela est possible.

-    **Section Line Marks|Bool**: affiche/masque les marques aux changements de direction pour la section complexe, quand cela est possible. <small>(v0.21)</small> 

-    **Section Line Style|Enumeration**: définit le style de ligne de la section, quand cela est possible.

-    **Show Section Line|Bool**: affiche/masque la ligne de section, quand cela est possible.

\(1\) ces propriétés sont communes à tous les types de vues.



## Propriétés Groupe de projection d\'un élément 

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Une groupe de projection d\'un élément, en fait un objet {{Incode|TechDraw::DrawProjGroupItem}}, est dérivée d\'une [vue de Part](TechDraw_View/fr#Propriétés_Vue_de_Part.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données 


{{TitleProperty|Base}}

-    **Type|Enumeration**: le type de vue ({{Value|Front}}, {{Value|Left}}, etc.).

-    **Rotation Vector|Vector**: déclassé, utilisez **XDirection** à la place.



## Propriétés Groupe de projection 

Voir [TechDraw Groupe de projections](TechDraw_ProjectionGroup/fr#Propriétés.md).



## Propriétés Vue de Spreadsheet 

Voir [TechDraw Vue de Spreadsheet](TechDraw_SpreadsheetView/fr#Propriétés.md).



## Propriétés Vue de Arch 

Voir [TechDraw Vue de Arch](TechDraw_ArchView/fr#Propriétés.md).



## Propriétés Symbole 

Voir [TechDraw Symbole](TechDraw_Symbol/fr#Propri.C3.A9t.C3.A9s.md).



## Propriétés Vue d\'une image 

Voir [TechDraw Image](TechDraw_Image/fr#Propri.C3.A9t.C3.A9s.md).



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Une vue de Part peut être crée à partir de [macros](Macros/fr.md) et de la console [Python](Python/fr.md) en utilisant la fonction suivante :


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





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/fr
