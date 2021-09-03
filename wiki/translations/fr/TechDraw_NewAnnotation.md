---
- GuiCommand:/fr
   Name:TechDraw Annotation
   Name/fr:TechDraw Annotation
   MenuLocation:TechDraw → Annotations → Insérer une annotation
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[Draft Texte](Draft_Text/fr.md), [Draft Formes à partir texte](Draft_ShapeString/fr.md)
---

## Description

L\'outil Annotation ajoute un bloc de texte à une page de dessin.

<img alt="" src=images/AnnotationSample.png  style="width:250px;"> 
*Annotation dans la page de dessin*

## Utilisation

1.  Si vous avez plusieurs pages de dessin dans votre document, vous devrez sélectionner la page souhaitée dans l\'arborescence.
2.  Appuyez sur le bouton **<img src="images/TechDraw_Annotation.svg" width=24px> [Insérer une annotation](TechDraw_Annotation/fr.md)
**
3.  Un bloc de texte contenant *Texte par défaut* apparaîtra sur la page. Utilisez l\'éditeur de propriétés pour modifier le texte. Faites glisser l\'annotation vers la position souhaitée.
4.  Vous devrez peut-être appuyer sur **<img src="images/Std_Refresh.svg" width=16px> [Std Rafraîchir](Std_Refresh/fr.md)** et/ou **<img src="images/TechDraw_RedrawPage.svg" width=16px> [TechDraw Redessiner](TechDraw_RedrawPage/fr.md)** pour que votre texte change.

![](images/UpdateAnnotation.png ) *Modification de l'annotation via l'éditeur de propriétés*


**Remarque:**

certains caractères interfèrent avec la représentation interne d\'annotation du texte. Plus précisément, ce sont la double citation des symboles `"`, plus petit que `<` et plus grand que `>`. Elles doivent être remplacées par des caractères d\'échappement HTML, `&amp;quot;`, `&amp;lt;`, et `&amp;gt;` respectivement. Voir [Character encodings in HTML](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#HTML_character_references) pour plus de détails.

## Propriétés

L\'annotation hérite de toutes les propriétés de base de la vue à l\'exception de {{PropertyData/fr|Scale}}. Utilisez plutôt la propriété {{PropertyData/fr|TextSize}}.

-    {{PropertyData/fr|Text}}: Le texte à afficher.

-    {{PropertyData/fr|Font}}: Le nom de la police à utiliser. L\'annotation utilisera la meilleure correspondance des polices installées.

-    {{PropertyData/fr|TextColor}}: La couleur du texte

-    {{PropertyData/fr|TextSize}}: La taille du texte en mm.

-    {{PropertyData/fr|MaxWidth}}: La largeur maximale du bloc d\'annotation. -1 indique pas de largeur maximale.

-    {{PropertyData/fr|LineSpace}}: Ajustement d\'interligne (%).

-    {{PropertyData/fr|TextStyle}}: \"Normal\", \"Gras\", \"Italique\", \"Gras-Italique\"

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Annotation peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
anno = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewAnnotation','TestAnno')
anno.Text = ['Different Text']
anno.TextStyle = 'Bold'
rc = page.addView(anno)
```

## Remarques





{{TechDraw Tools navi

}}  
