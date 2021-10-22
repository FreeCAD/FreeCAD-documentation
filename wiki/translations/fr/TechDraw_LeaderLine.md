---
- GuiCommand:/fr
   Name:TechDraw LeaderLine
   Name/fr:TechDraw Ligne de référence
   MenuLocation:TechDraw → Ajouter des lignes → Insérer une ligne de référence à la vue
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Annotation en texte enrichi](TechDraw_RichTextAnnotation/fr.md), [TechDraw Symbole de soudure](TechDraw_WeldSymbol/fr.md), [TechDraw Groupes de lignes](TechDraw_LineGroup/fr.md)
---

# TechDraw LeaderLine/fr

## Description

L\'outil Ligne de référence ajoute une ligne à une vue. D\'autres objets d\'annotation (tels que [Annotation par texte enrichi](TechDraw_RichTextAnnotation/fr.md)) peuvent être connectés à Ligne de référence pour former des annotations complexes.

![](images/TechDraw_LeaderLine_sample.png ) 
*Ligne de référence ajoutée à View001*

## Utilisation

1.  Sélectionnez une vue.
2.  Appuyez sur le bouton **<img src="images/TechDraw_LeaderLine.svg" width=16px> Insérer une ligne de référence à la vue**. Une boîte de dialogue s\'ouvrira permettant de dessiner la ligne de repère et d\'assigner des symboles de fin à la ligne.
3.  Cliquez sur **Pick points** puis cliquez dans la page pour définir le point de départ de la ligne.
4.  Déplacez la souris et cliquez sur un autre point pour créer une ligne. Maintenez la touche Ctrl enfoncée pour obtenir des angles multiples de 22,5°.
5.  Maintenant, vous pouvez soit:
    1.  terminer le dessin au trait en double-cliquant ou en appuyant sur **Save Points**.
    2.  ajoutez d\'autres points pour définir davantage de segments de ligne.
6.  Pour terminer la création, appuyez sur **OK** pour fermer la boîte de dialogue.

**Remarque:** Si vous n\'avez défini aucun point lors de la création de la ligne de rappel, une ligne courte sera placée au centre de la vue.

### Édition

1.  Sélectionnez la ligne de référence dans l\'arborescence des documents et double-cliquez dessus.
2.  Une boîte de dialogue s\'ouvrira où vous pourrez changer l\'apparence.
3.  Pour modifier les points, cliquez sur **Edit points** et les points de ligne deviennent visibles dans le dessin.
4.  Faites glisser les points vers un endroit que vous aimez et terminez la modification en cliquant sur **Save changes**.

## Propriétés

-    {{PropertyData/fr|X, Y}}: Le point auquel la ligne de référence est connectée à la vue.

-    {{PropertyData/fr|Leader Parent}}: la vue à laquelle la ligne est attachée.

-    {{PropertyData/fr|Start Symbol}}: Le symbole au début: <img alt="" src=images/Arrownone.svg  style="width:20px;"> Aucun, <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Flèche pleine, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Flèche ouverte, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Coché, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Point, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Cercle ouvert, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fourche, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Triangle rempli

-    {{PropertyData/fr|End Symbol}}: le symbole de fin de ligne à l\'autre extrémité.

-    {{PropertyData/fr|WayPoints}}: noeuds sur la ligne de rappel.

-    {{PropertyData/fr|Scalable}}: la ligne de rappel évolue avec LeaderLine Parent.

-    {{PropertyData/fr|Auto Horizontal}}: force le dernier segment de ligne de rappel à être horizontal.

-    {{PropertyView/fr|Color}}: Couleur de stylo pour la ligne de rappel.

-    {{PropertyView/fr|Line Style}}: 0 Pas de ligne, 1 <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continu, 2 <img alt="" src=images/Dash-line.svg  style="width:20px;"> Tiret, 3 <img alt="" src=images/Dot-line.svg  style="width:20px;"> Point , 4 <img alt="" src=images/DashDot-line.svg  style="width:20px;"> Tiret Point, 5 <img alt="" src=images/DashDotDot-line.svg  style="width:20px;"> Tiret Point Point

-    {{PropertyView/fr|Line Width}}: largeur de la ligne de rappel.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Ligne de rappel peut être utilisée dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant la fonction suivante:


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

## Remarques

-   Vous pouvez modifier une ligne de rappel en double-cliquant dessus dans l\'arborescence. Le double-clic dans la zone graphique n\'est pas encore pris en charge. Le ou les segments de ligne peuvent être modifiés en appuyant sur **Edit points**. Pour quitter la modification des points, appuyez sur **Save changes** ou **Discard changes**.
-   Si vous n\'avez défini aucun point lors de la création de la ligne de rappel, une ligne courte sera placée au centre de la vue. Vous ne pourrez plus ajouter ultérieurement de points.
-   Par défaut, l\'option [TechDraw Préférences](TechDraw_Preferences/fr.md) **Ligne de référence automatique horizontale** est activée. Par conséquent, le dernier segment de ligne sera horizontal. Donc, si vous n\'avez qu\'un seul segment, vous obtenez une ligne horizontale, peu importe où vous avez choisi le deuxième point.
-   Vous pouvez désactiver la fonction horizontale automatique pour les lignes de rappel existantes en modifiant la propriété {{PropertyData/fr|Auto Horizontal}}.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/fr
