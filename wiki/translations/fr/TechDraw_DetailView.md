---
- GuiCommand:/fr
   Name:TechDraw DetailView
   Name/fr:TechDraw Vue détaillée
   MenuLocation:TechDraw → Insérer une vue de détail
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Vue](TechDraw_View/fr.md), [TechDraw Groupe de projection](TechDraw_ProjectionGroup/fr.md)
---

# TechDraw DetailView/fr

## Description

L\'outil Détail crée une vue d\'une petite zone d\'une vue existante.

![](images/ViewDetail.png ) *Vue détaillée avec vue circulaire d'une vue existante*

## Utilisation

-   Sélectionnez une vue dans la page ou l\'arborescence.
-   Appuyez sur le bouton **<img src="images/TechDraw_DetailView.svg" width=16px> [Inserérer une vue de détail](TechDraw_DetailView/fr.md)** pour créer la vue détaillée.
-   Dans la boîte de dialogue de tâche qui apparaît, vous pouvez définir le rayon de la zone de vue, l\'échelle et la position de la vue. Pour ce dernier, vous pouvez le faire
    -   soit en changeant les coordonnées
    -   ou en appuyant sur le bouton **Drag Highlight**. Dans ce cas, la bordure d\'origine du détail est mise en évidence en gras et avec l\'étiquette *drag*. Cliquez sur la bordure ou l\'étiquette, maintenez le bouton de la souris enfoncé et faites-la glisser à la position souhaitée. Relâchez enfin la souris pour accepter le changement.

La vue détaillée peut être affichée dans une boîte de vue ronde ou carrée. Ceci est contrôlé par le paramètre [préférences](TechDraw_Preferences/fr#Annotation.md) **Forme de contour de la vue détaillée**.

## Propriétés

### Vue détaillée 

-    {{PropertyData/fr|BaseView}}: la vue sur laquelle cette vue détaillée est basée.

-    {{PropertyData/fr|Anchor Point}}: centre de la vue détaillée dans {{PropertyData/fr|BaseView}}.

-    {{PropertyData/fr|Radius}}: taille de la zone dans la {{PropertyData/fr|BaseView}} affichée dans la vue détaillée.

-    {{PropertyData/fr|Scale Type}}: type de l\'échelles. Les choix sont:

    -   *Page*: facteur d\'échelle de la [Page](TechDraw_PageDefault/fr.md) du dessin utilisé
    -   *Automatic*: dans le cas où la vue détaillée serait plus grande que la page, elle sera réduite pour tenir dans la page
    -   *Custom*: facteur d\'échelle personnalisé défini par {{PropertyData/fr|Scale}}

-    {{PropertyData/fr|Scale}}: niveau d\'agrandissement.

-    {{PropertyData/fr|Reference}}: identifiant pour indiquer la zone de {{PropertyData/fr|BaseView}} affichée.

### Base View 

Une vue détaillée hérite de toutes les propriétés applicables de la vue spécifiée comme {{PropertyData/fr|BaseView}}. Dans les propriétés de cette vue, vous pouvez modifier l\'apparence du contour du détail:

-    {{PropertyView/fr|Highlight Adjust}}: angle de rotation dans le sens horaire de la vue de détail.

-    {{PropertyView/fr|Highlight Line Color}}: couleur de ligne pour la forme du contour. Le paramètre par défaut pour cela est le paramètre **Detail Highlight** dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

-    {{PropertyView/fr|Highlight Line Style}}: style de ligne pour la forme du contour. Le paramètre par défaut pour cela est le paramètre **Detail Highlight Style** dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Vue détaillée peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
Detail = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDetail','Detail')
...TBA
```

## Astuces

-   L\'espace autour du contour de la vue et de la bordure de l\'objet de vue est par défaut une zone blanche. Cela signifie qu\'il couvre tout derrière. Parfois, il n\'y a pas assez d\'espace sur la page et vous pouvez économiser de l\'espace en réduisant cette zone blanche inutile.

Pour ce faire, placez la vue Détails dans une [Fenêtre de rognage](TechDraw_ClipGroup/fr.md):

![](images/TechDraw_DetailClipped.png ) *Vue détaillée d'une fenêtre de rognage*

-   Pour les vues de détail avec un contour rond, la position de l\'étiquette de référence dans la vue de base peut être modifiée via la propriété de vue de base {{PropertyView/fr|Highlight Adjust}}.

## Remarques

-   [Une bonne discussion sur la configuration de Anchor](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/fr
