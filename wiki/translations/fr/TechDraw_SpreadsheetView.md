---
 GuiCommand:
   Name: TechDraw SpreadsheetView
   Name/fr: TechDraw Vue d'un objet Spreadsheet
   MenuLocation: TechDraw , Vues des autres ateliers , Insérer une vue de l'atelier Spreadsheet
   Workbenches: TechDraw_Workbench/fr, Spreadsheet_Workbench/fr
---

# TechDraw SpreadsheetView/fr

## Description

L\'outil **TechDraw Vue d\'un objet Spreadsheet** vous permet de placer une vue d\'une [feuille de calcul](Spreadsheet_Workbench/fr.md) sélectionnée dans une [page](TechDraw_Workbench/fr.md).


{{Version/fr|1.0}}

: l\'outil [TechDraw Vue](TechDraw_View/fr.md) peut également créer une vue d\'un objet de Spreadsheet.

![](images/TechDraw_Spreadsheetview.png ) 
*Elément de Spreadsheet inséré dans la page de dessin TechDraw*



## Utilisation

1.  Sélectionnez un objet Spreadsheet dans la [vue en arborescence](Tree_view/fr.md).
2.  Si le document contient plusieurs pages de dessin : ajoutez la page souhaitée à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
3.  Sélectionnez l\'option **TechDraw → Vues des autres ateliers → <img src="images/TechDraw_SpreadsheetView.svg" width=16px> Insérer une vue de l'atelier Spreadsheet** du menu.
4.  S\'il y a plusieurs pages de dessin dans le document, et si aucune page n\'est affichée dans la [zone de vue principale](Main_view_area/fr.md) et que vous n\'avez pas encore sélectionné de page, la fenêtre de dialogue **Sélecteur de pages** s\'ouvre :
    1.  Sélectionnez la page souhaitée.
    2.  Appuyez sur le bouton **OK**.
5.  Une vue de Spreadsheet est insérée.
6.  Ajustez la plage de cellules de la vue en modifiant ses propriétés **Cell Start** et **Cell End**.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Une vue d\'un objet Spreadsheet, en fait un objet {{Incode|TechDraw::DrawViewSpreadsheet}}, possède les [propriétés](TechDraw_View/fr#Propriétés_Vue_de_Part.md) communes à tous les types de vues. Elle possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Drawing view}}

-    **Symbol|String|Hidden**: code SVG définissant ce symbole.

-    **Editable Texts|StringList**: valeurs de substitution pour les chaînes modifiables de ce symbole.

-    **Owner|Link**: fonction à laquelle ce symbole est rattaché. {{Version/fr|1.0}}


{{TitleProperty|Spreadsheet}}

-    **Source|Link**: feuille de calcul à ajouter à la page.

-    **Cell Start|String**: cellule supérieure gauche de la plage de cellules à inclure dans cette vue.

-    **Cell End|String**: cellule inférieure droite de la plage de cellules à inclure dans cette vue.

-    **Font|Font**: nom de la police utilisée pour les textes.

-    **Text Color|Color**: couleur des textes et des lignes qui n\'ont pas de couleur spécifiée dans le tableur.

-    **Text Size|Float**: taille de la police des textes.

-    **Line Width|Float**: largeur des bordures des cellules.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/fr
