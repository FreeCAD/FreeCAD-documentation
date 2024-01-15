---
 GuiCommand:
   Name: TechDraw LeaderLine
   Name/fr: TechDraw Ligne de référence
   MenuLocation: TechDraw , Ajouter des lignes , Insérer une ligne de référence à la vue
   Workbenches: TechDraw_Workbench/fr
   Version: 0.19
   SeeAlso: TechDraw_RichTextAnnotation/fr, TechDraw_WeldSymbol/fr
---

# TechDraw LeaderLine/fr

## Description

L\'outil **TechDraw Ligne de référence** ajoute une ligne à une vue. D\'autres objets d\'annotation (tels que [Annotation par texte enrichi](TechDraw_RichTextAnnotation/fr.md)) peuvent être connectés à Ligne de référence pour former des annotations complexes.

![](images/TechDraw_LeaderLine_sample.png ) 
*Ligne de référence ajoutée à un vue*



## Utilisation

1.  Sélectionnez une vue.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_LeaderLine.svg" width=16px> [Insérer une ligne de référence à la vue](TechDraw_LeaderLine/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Ajouter des lignes → <img src="images/TechDraw_LeaderLine.svg" width=16px> Insérer une ligne de référence à la vue** du menu.
3.  Un panneau de tâches s\'ouvre.
4.  Appuyez sur le bouton **Choisir des points**.
5.  Choisissez le premier point de la page pour définir le point de départ de la ligne.
6.  Choisissez le point suivant sur la page. Maintenez **Ctrl** enfoncée pour cliquer sur des multiples d\'angles de 22,5°. Vous pouvez utiliser un double-clic au lieu d\'un simple-clic pour terminer la saisie des points.
7.  Vous pouvez ajouter d\'autres points.
8.  Si vous n\'avez pas double-cliqué sur un point : appuyez sur le bouton **Enregistrer les points**.
9.  Vous pouvez modifier le **Symbole de début**, le **Symbole de fin**, la **Couleur**, la **Largeur** et le **Style** de la ligne de référence. Voir [Propriétés](#Propriétés.md) pour plus d\'informations.
10. Appuyez sur le bouton **OK**.



## Édition

1.  Double-cliquez sur une ligne de référence dans l\'arborescence.
2.  Un panneau de tâches s\'ouvre.
3.  Pour modifier les points :
    1.  Appuyez sur le bouton **Modifier les points**.
    2.  La ligne de référence est marquée par des nœuds temporaires.
    3.  Faites glisser un ou plusieurs nœuds vers une nouvelle position.
    4.  Appuyez sur le bouton **Enregistrer les modifications**.
4.  Vous pouvez modifier le **Symbole de début**, le **Symbole de fin**, la **Couleur**, la **Largeur** et le **Style** du repère. Voir [Propriétés](#Propriétés.md) pour plus d\'informations.
5.  Appuyez sur le bouton **OK**.



## Remarques

-   Il n\'est pas possible d\'ajouter ou de supprimer des points d\'une ligne de référence existante.
-   Si aucun point n\'a été spécifié lors de la création, une courte ligne est placée au centre de la vue. Il n\'y a aucun moyen de fixer une telle ligne, elle doit être supprimée.
-   Par défaut, **Ligne de référence horizontale automatique** des [préférences](TechDraw_Preferences/fr#Annotation.md) est cochée. Cela signifie que le dernier segment de ligne des nouvelles lignes de guidage est dessiné horizontalement. S\'il n\'y a qu\'un seul segment, le résultat est une simple ligne horizontale.
-   Vous pouvez désactiver cette fonction d\'horizontalité automatique pour les lignes de référence existantes en modifiant la propriété **Auto Horizontal**.



## Propriétés



### Données


{{Properties_Title|Base}}

-    **Start Symbol|Enumeration**: symbole au début de la ligne de référence. Options : <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Flèche remplie, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Flèche ouverte, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Coche, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Point, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Cercle ouvert, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fourche, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Triangle rempli, Rien.

-    **End Symbol|Enumeration**: symbole à la fin de la ligne de référence. Idem.

-    **X|Distance**: coordonnée X de la ligne de référence par rapport à la vue.

-    **Y|Distance**: coordonnée Y de la ligne de référence par rapport à la vue.


{{Properties_Title|Leader}}

-    **Leader Parent|Link**: vue à laquelle la ligne de référence est attachée.

-    **Way Points|VectorList**: points de la ligne de référence.

-    **Scalable|Bool**: indique si la ligne de référence s\'adapte à **Leader Parent**.

-    **Auto Horizontal|Bool**: indique si le dernier segment de la ligne de référence doit être horizontal.



### Vue


{{TitleProperty|Base}}

-    **Keep Label|Bool**: non utilisé.

-    **Stack Order|Integer**: chevauchement ou sous-chevauchement par rapport à d\'autres objets du dessin. {{Version/fr|0.21}}


{{TitleProperty|Line Format}}

-    **Color|Color**: couleur de la ligne de référence.

-    **Line Style|Enumeration**: style de la ligne de référence. Options : Rien, <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continu, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Tiret, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Point, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tiret Point, <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> Tiret Point Point.

-    **Line Width|Length**: largeur de la ligne de référence.



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Ligne de référence peut être utilisée dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante:


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
leaderObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawLeaderLine','DrawLeaderLine')
FreeCAD.activeDocument().myPage.addView(leaderObj)
FreeCAD.activeDocument().leaderObj.LeaderParent = myBase
#first waypoint is always (0,0,0)  
#rest of waypoints are positions relative to (0,0,0)
leaderObj.WayPoints = [p0,p1,p2]
leaderObj.X = 5
leaderObj.Y = 5
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/fr
