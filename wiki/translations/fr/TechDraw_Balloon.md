---
- GuiCommand:/fr
   Name:TechDraw Balloon
   Name/fr:TechDraw Annotation bulle
   MenuLocation:TechDraw → Annotations → Insérer une annotation bulle
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Annotation](TechDraw_Annotation/fr.md)
---

## Description

L\'outil Annotation bulle peut ajouter des bulles avec une ligne de repère dans un dessin.

<img alt="" src=images/Techdraw_balloon.png  style="width:600px;">

## Utilisation

1.  Sélectionnez la vue à laquelle la bulle sera attachée.
2.  Appuyez sur le bouton **<img src="images/TechDraw_Balloon.svg" width=16px> [Insérer une annotation bulle](TechDraw_Balloon/fr.md)**.
3.  Le curseur est maintenant affiché sous forme d'icône bulle. Cliquez sur la page pour placer l\'origine de la bulle à la position souhaitée.
4.  La bulle peut être déplacée à la position désirée. Utilisez CTRL-glisser pour déplacer la bulle et la flèche.
5.  Pour modifier les propriétés de la bulle, double-cliquez dessus dans le dessin ou double-cliquez sur l\'objet bulle dans l\'arborescence du modèle. Cela ouvrira la boîte de dialogue des bulles.

**Remarque:** La position de la bulle est relative à la vue et utilise le même facteur d\'échelle que la vue.

## Utiliser les séparateurs 

Lorsque vous utilisez une forme de rectangle, vous pouvez ajouter des séparateurs en utilisant \"\|\" dans le texte. Par exemple \"AAA\|TEST\|111\" donne:

<img alt="" src=images/balloon_separator.png  style="width:300px;">

## Propriétés

### Données

-    {{PropertyData/fr|Text}}: Texte à afficher.

-    {{PropertyData/fr|Source View}}: vue source de la bulle.

-    {{PropertyData/fr|Origin X}}: Position x de l\'origine de la bulle par rapport à la vue.

-    {{PropertyData/fr|Origin Y}}: Position y de l\'origine de la bulle par rapport à la vue.

-    {{PropertyData/fr|End Type}}: symbole de fin pour la ligne de la bulle. Options: <img alt="" src=images/Arrownone.svg  style="width:20px;"> Rien, <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Flèche pleine, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Flèche ouverte, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Coché, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Point, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Cercle ouvert, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fourche, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Triangle rempli

-    {{PropertyData/fr|End Type Scale}}: Facteur d\'échelle pour le **Type d\'extrémité**.

-    {{PropertyData/fr|Bubble Shape}}: Forme de la bulle. Options: <img alt="" src=images/Circular.svg  style="width:20px;"> Circulaire, Rien, <img alt="" src=images/Triangle.svg  style="width:20px;"> Triangle, <img alt="" src=images/Inspection.svg  style="width:20px;"> Inspection, <img alt="" src=images/Hexagon.svg  style="width:20px;"> Hexagone, <img alt="" src=images/TechDraw_Square.svg  style="width:20px;"> Carré, <img alt="" src=images/Rectangle.svg  style="width:20px;"> Rectangle

-    {{PropertyData/fr|Shape Scale}}: Facteur d\'échelle pour la **Forme**.

-    {{PropertyData/fr|Text Wrap}}: Longueur d\'habillage de texte. -1 signifie que le texte ne sera jamais encapsulé et que le résultat est dans tous les cas une seule ligne.

-    {{PropertyData/fr|Kink Length}}: Distance entre la **forme** et le pli de la ligne de repère.

-    {{PropertyData/fr|X}}: position horizontale de la bulle par rapport à la vue.

### Vue

-    {{PropertyView/fr|Color}}: couleur du texte de la bulle.

-    {{PropertyView/fr|Font}}: nom de la police à utiliser pour la bulle.

-    {{PropertyView/fr|Fontsize}}: dimension du texte en mm.

-    {{PropertyView/fr|Line Visible}}: si la ligne de bulle est visible.

-    {{PropertyView/fr|Line Width}}: largeur de ligne de la bulle.

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
