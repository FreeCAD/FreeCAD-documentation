---
- GuiCommand:
   Name:TechDraw SpreadsheetView
   Name/fr:TechDraw Vue d'un objet Spreadsheet
   MenuLocation:TechDraw → Insérer une vue de feuille de calcul
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md), [Spreadsheet](Spreadsheet_Workbench/fr.md)
---

# TechDraw SpreadsheetView/fr


</div>

## Description

L\'outil **TechDraw Vue d\'un objet Spreadsheet** vous permet de placer une vue d\'une [feuille de calcul](Spreadsheet_Workbench/fr.md) sélectionnée dans une [page](TechDraw_Workbench/fr.md).

![](images/TechDraw_Spreadsheetview.png ) 
*Elément de Spreadsheet inséré dans la page de dessin TechDraw*



## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez une feuille de calcul dans la [Vue en arborescence](Tree_view/fr.md).
2.  Appuyez sur le bouton **<img src="images/TechDraw_SpreadsheetView.svg" width=16px> [Insérer une vue de feuille de calcul](TechDraw_SpreadsheetView/fr.md)
**


</div>



## Remarques

-   Dans {{VersionMinus/fr|0.19}}, certains caractères dans les cellules des feuilles de calcul provoquent des erreurs lorsqu\'ils sont affichés dans une vue de feuille de calcul. Ces caractères doivent être codés en XML. Les caractères actuellement connus sont : {{Incode|&}} (à remplacer par {{Incode|&amp;amp;}}) et {{Incode|&lt;}} (à remplacer par {{Incode|&amp;lt;}}). Voir aussi cette [discussion](https://forum.freecadweb.org/viewtopic.php?p=629853#p629885) dans le forum.



## Propriétés

Voir [TechDraw Vue](TechDraw_View/fr#Propri.C3.A9t.C3.A9s.md)



### Données


{{TitleProperty|Spreadsheet}}

-    **Source|Link**: feuille de calcul à ajouter à la page.

-    **Cell Start|String**: cellule supérieure gauche de la plage de cellules à inclure dans cette vue.

-    **Cell End|String**: cellule inférieure droite de la plage de cellules à inclure dans cette vue.

-    **Font|Font**: nom de la police utilisée pour les textes.

-    **Text Color|Color**: couleur des textes et des lignes qui n\'ont pas de couleur spécifiée dans le tableur.

-    **Text Size|Float**: taille de la police des textes.

-    **Line Width|Float**: largeur des bordures des cellules.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/fr
