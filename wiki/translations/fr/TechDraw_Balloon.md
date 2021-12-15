---
- GuiCommand:/fr
   Name:TechDraw Balloon
   Name/fr:TechDraw Annotation bulle
   MenuLocation:TechDraw → Annotations → Insérer une annotation bulle
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Annotation](TechDraw_Annotation/fr.md)
---

# TechDraw Balloon/fr

## Description

L\'outil Annotation bulle peut ajouter des bulles avec une ligne de repère dans un dessin.

<img alt="" src=images/Techdraw_balloon.png  style="width:600px;">

## Utilisation

1.  Sélectionnez l\'un des éléments suivants :
    -   Une vue (sur la page ou dans la [Vue en arborescence](Tree_view/fr.md)).
    -   Un sommet dans une vue. {{Version/fr|0.20}}
    -   Une arête dans une vue. {{Version/fr|0.20}}
    -   Une région fermée dans une vue. {{Version/fr|0.20}}
2.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le **<img src="images/TechDraw_Balloon.svg" width=16px> [Insérer une annotation bulle](TechDraw_Balloon/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Annotations → <img src="images/TechDraw_Balloon.svg" width=16px> Insérer une annotation bulle** dans le menu.
3.  Si une vue ou une région a été sélectionnée :
    1.  Le curseur se transforme en une icône bulle.
    2.  Cliquez sur un point de la page pour l\'origine de la bulle.

Pour déplacer la bulle de la bulle, appuyez et maintenez le bouton gauche de la souris sur son centre et faites glisser la souris.

Pour modifier les propriétés d\'une bulle, double-cliquez dessus dans la page ou dans la [Vue en arborescence](Tree_view/fr.md). Cela ouvrira le panneau des tâches de la bulle.

**Remarque:** la position de la bulle est relative à sa vue source et utilise le même facteur d\'échelle.

## Utiliser les séparateurs 

Lorsque vous utilisez une forme de rectangle, vous pouvez ajouter des séparateurs en utilisant \"\|\" dans le texte. Par exemple \"AAA\|TEST\|111\" donne:

<img alt="" src=images/balloon_separator.png  style="width:300px;">

## Propriétés

### Données

-    **Text**: Texte à afficher.

-    **Source View**: vue source de la bulle.

-    **Origin X**: Position x de l\'origine de la bulle par rapport à la vue.

-    **Origin Y**: Position y de l\'origine de la bulle par rapport à la vue.

-    **End Type**: symbole de fin pour la ligne de la bulle. Options: <img alt="" src=images/Arrownone.svg  style="width:20px;"> Rien, <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Flèche pleine, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Flèche ouverte, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Coché, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Point, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Cercle ouvert, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fourche, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Triangle rempli

-    **End Type Scale**: Facteur d\'échelle pour le **Type d\'extrémité**.

-    **Bubble Shape**: Forme de la bulle. Options: <img alt="" src=images/Circular.svg  style="width:20px;"> Circulaire, Rien, <img alt="" src=images/Triangle.svg  style="width:20px;"> Triangle, <img alt="" src=images/Inspection.svg  style="width:20px;"> Inspection, <img alt="" src=images/Hexagon.svg  style="width:20px;"> Hexagone, <img alt="" src=images/TechDraw_Square.svg  style="width:20px;"> Carré, <img alt="" src=images/Rectangle.svg  style="width:20px;"> Rectangle

-    **Shape Scale**: Facteur d\'échelle pour la **Forme**.

-    **Text Wrap**: Longueur d\'habillage de texte. -1 signifie que le texte ne sera jamais encapsulé et que le résultat est dans tous les cas une seule ligne.

-    **Kink Length**: Distance entre la **forme** et le pli de la ligne de repère.

-    **X**: position horizontale de la bulle par rapport à la vue.

### Vue

-    **Color**: couleur du texte de la bulle.

-    **Font**: nom de la police à utiliser pour la bulle.

-    **Fontsize**: dimension du texte en mm.

-    **Line Visible**: si la ligne de bulle est visible.

-    **Line Width**: largeur de ligne de la bulle.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Annotation en bulle peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
bal1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewBalloon','Balloon')
rc = page.addView(bal1)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Balloon/fr
