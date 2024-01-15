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

![](images/TechDraw_Spreadsheetview.png ) 
*Elément de Spreadsheet inséré dans la page de dessin TechDraw*



## Utilisation

1.  Sélectionnez une seule feuille de calcul dans la [vue en arborescence](Tree_view/fr.md).
2.  Si le document contient plusieurs pages de dessin : ajoutez la page souhaitée à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
3.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_SpreadsheetView.svg" width=16px> [Insérer une vue de l'atelier Spreadsheet](TechDraw_SpreadsheetView/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Vues des autres ateliers → <img src="images/TechDraw_SpreadsheetView.svg" width=16px> Insérer une vue de l'atelier Spreadsheet** du menu.
4.  S\'il y a plusieurs pages de dessin dans le document et que vous n\'avez pas encore sélectionné de page, la boîte de dialogue **Sélecteur de page** s\'ouvre : {{Version/fr|0.20}}
    1.  Sélectionnez la page désirée.
    2.  Appuyez sur le bouton **OK**.
5.  Ajustez la plage de cellules de la vue en modifiant ses propriétés **Cell Start** et **Cell End**.



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
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SpreadsheetView/fr
