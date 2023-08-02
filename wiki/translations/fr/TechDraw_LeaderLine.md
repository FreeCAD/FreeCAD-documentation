---
- GuiCommand:
   Name: TechDraw LeaderLine
   Name/fr: TechDraw Ligne de référence
   MenuLocation: TechDraw -> Ajouter des lignes -> Insérer une ligne de référence à la vue
   Workbenches: TechDraw_Workbench/fr
   Version: 0.19
   SeeAlso: TechDraw_RichTextAnnotation/fr, TechDraw_WeldSymbol/fr, TechDraw_LineGroup/fr
---

# TechDraw LeaderLine/fr


</div>

## Description

L\'outil **TechDraw Ligne de référence** ajoute une ligne à une vue. D\'autres objets d\'annotation (tels que [Annotation par texte enrichi](TechDraw_RichTextAnnotation/fr.md)) peuvent être connectés à Ligne de référence pour former des annotations complexes.

![](images/TechDraw_LeaderLine_sample.png )


<div class="mw-translate-fuzzy">



*Ligne de référence ajoutée à View001*


</div>




<div class="mw-translate-fuzzy">

## Utilisation


</div>


<div class="mw-translate-fuzzy">

1.  Sélectionnez une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_LeaderLine.svg" width=16px> Insérer une ligne de référence à la vue**. Une boîte de dialogue s\'ouvrira permettant de dessiner la ligne de repère et d\'assigner des symboles de fin à la ligne.
3.  Cliquez sur **Pick points** puis cliquez dans la page pour définir le point de départ de la ligne.
4.  Déplacez la souris et cliquez sur un autre point pour créer une ligne. Maintenez la touche Ctrl enfoncée pour obtenir des angles multiples de 22,5°.
5.  Maintenant, vous pouvez soit:
    1.  terminer le dessin au trait en double-cliquant ou en appuyant sur **Save Points**.
    2.  ajoutez d\'autres points pour définir davantage de segments de ligne.
6.  Pour terminer la création, appuyez sur **OK** pour fermer la boîte de dialogue.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

1.  Sélectionnez la ligne de référence dans l\'arborescence des documents et double-cliquez dessus.
2.  Une boîte de dialogue s\'ouvrira où vous pourrez changer l\'apparence.
3.  Pour modifier les points, cliquez sur **Edit points** et les points de ligne deviennent visibles dans le dessin.
4.  Faites glisser les points vers un endroit que vous aimez et terminez la modification en cliquant sur **Save changes**.


</div>



## Remarques


<div class="mw-translate-fuzzy">

-   Vous pouvez modifier une Ligne de référence en double-cliquant dessus dans l\'arborescence. Le double-clic dans la zone graphique n\'est pas encore pris en charge. Le ou les segments de la ligne peuvent être modifiés en appuyant sur **Edit points**. Pour quitter la modification des points, appuyez sur **Save changes** ou **Discard changes**.
-   Si vous n\'avez défini aucun point lors de la création de la Ligne de référence, une ligne courte sera placée au centre de la vue. Vous ne pourrez plus ajouter ultérieurement de points.
-   Par défaut, l\'option [TechDraw Préférences](TechDraw_Preferences/fr.md) **Ligne de référence automatique horizontale** est activée. Par conséquent, le dernier segment de ligne sera horizontal. Donc, si vous n\'avez qu\'un seul segment, vous obtenez une ligne horizontale, peu importe où vous avez choisi le deuxième point.
-   Vous pouvez désactiver la fonction horizontale automatique pour les lignes de référence existantes en modifiant la propriété {{PropertyData/fr|Auto Horizontal}}.


</div>



## Propriétés

### Data


{{Properties_Title|Base}}

-    **Start Symbol|Enumeration**: The symbol at the start of the leaderline. Options: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Filled Arrow, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Open Arrow, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Tick, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Dot, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Open Circle, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fork, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Filled Triangle, None.

-    **End Symbol|Enumeration**: The symbol at the end of the leaderline. Idem.

-    **X|Distance**: The X coordinate of the leaderline relative to the View.

-    **Y|Distance**: The Y coordinate of the leaderline relative to the View.


{{Properties_Title|Leader}}

-    **Leader Parent|Link**: The View the leaderline is attached to.

-    **Way Points|VectorList**: The points of the leaderline.

-    **Scalable|Bool**: Specifies if the leaderline scales with **Leader Parent**.

-    **Auto Horizontal|Bool**: Specifies if the last leaderline segment is forced to be horizontal.

### View


{{TitleProperty|Base}}

-    **Keep Label|Bool**: Not used.

-    **Stack Order|Integer**: Over or underlap relative to other drawing objects. <small>(v0.21)</small> 


{{TitleProperty|Line Format}}

-    **Color|Color**: The color of the leaderline.

-    **Line Style|Enumeration**: The style of the leaderline. Options: NoLine, <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot.

-    **Line Width|Length**: The width of the leaderline.



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
