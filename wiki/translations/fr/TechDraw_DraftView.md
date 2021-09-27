---
- GuiCommand:/fr
   Name:TechDraw DraftView
   Name/fr:TechDraw Vue Draft
   MenuLocation:TechDraw → Insérer un objet de l'atelier Draft
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md), [Draft](Draft_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Vue Arch](TechDraw_ArchView/fr.md)
---

# TechDraw DraftView/fr

## Description

L\'outil <img alt="" src=images/TechDraw_DraftView.svg  style="width:24px;"> _, les vues créées avec cet outil sont gérées par <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) et spécialement conçues pour montrer des objets 2D. Voir Remarques.

![](images/TechDraw_DraftView_example.png ) *Éléments Draft tels que des cercles et des réseaux importés dans une page de dessin TechDraw*

## Utilisation

1.  Sélectionnez un brouillon dans la vue 3D ou dans l\'arborescence
2.  Si vous avez plusieurs pages de dessin dans votre document, vous devrez sélectionner la page souhaitée dans l\'arborescence.
3.  Appuyez sur le bouton **<img src="images/TechDraw_DraftView.svg" width=16px> [Insérer un objet de l'atelier Draft](TechDraw_DraftView/fr.md)
**
4.  Une vue d\'un objet Draft apparaîtra sur la page.

### Limitations

Vue Draft est rendu dans l\'atelier [Draft](Draft_Workbench/fr.md). TechDraw a donc un contrôle limité sur son apparence. Vous devrez peut-être apporter des modifications dans Draft pour obtenir la représentation souhaitée.

## Options

-   La création d\'une vue Draft d\'une coupe traitera de manière récursive tous les objets trouvés dans cette coupe. La vue est mise à jour automatiquement lorsque le contenu de la coupe change.
-   Il n\'y a pas de suppression de ligne cachée. Chaque face trouvée dans le ou les objets manipulés sera simplement projetée le long du vecteur Direction, aucune action spécifique n\'est entreprise lorsque les faces se chevauchent.
-   La vue Draft prend également en charge tous les objets Draft qui ne sont pas basés Part, tels que les cotes et les textes.
-   La couleur, la largeur et le motif des lignes peuvent être spécifiés dans les propriétés. Les motifs de ligne peuvent être affinés en donnant directement une valeur [stroke-dasharray](https://www.w3.org/TR/SVG/painting.html#StrokeProperties), telle que 3,5.
-   Les surfaces projetées sont remplies de la couleur de la surface.

## Propriétés

-    {{PropertyData/fr|Source}}: L\'objet Draft à afficher

-    {{PropertyData/fr|LineWidth}}: La largeur des lignes, indépendamment de l\'échelle

-    {{PropertyData/fr|FontSize}}: La taille de tous les textes apparaissant dans cette vue (textes et dimensions)

-    {{PropertyData/fr|Direction}}: La direction de projection à utiliser

-    {{PropertyData/fr|Color}}: La couleur des lignes

-    {{PropertyData/fr|LineStyle}}: Un style de ligne à utiliser pour cette vue. Peut être continu, pointillé, tireté, point ou un motif de ligne SVG comme 0.20,0.20

-    {{PropertyData/fr|LineSpacing}}: L\'espacement à utiliser entre les lignes de textes pour les textes multilignes

Remarque: Vue Draft hérite de toutes les propriétés Vues de base applicables.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Vue Draft peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DraftView/fr
