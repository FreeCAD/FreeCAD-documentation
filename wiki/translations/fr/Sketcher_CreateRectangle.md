---
 GuiCommand:
   Name: Sketcher CreateRectangle
   Name/fr: Sketcher Rectangle
   MenuLocation: Esquisse , Géométries d'esquisse, Créer un rectangle
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **R**
   SeeAlso: Sketcher_CreateOblong/fr, Sketcher_CreatePolyline/fr
---

# Sketcher CreateRectangle/fr

## Description

Cet outil dessine un rectangle en choisissant deux points opposés. Au démarrage de l\'outil, le pointeur de la souris se transforme en une croix blanche avec une icône de rectangle rouge. Les coordonnées du pointeur sont affichées à côté en bleu en temps réel.

Pour définir un rectangle à l\'aide d\'un point central et d\'un point du bord, utilisez l\'outil [Rectangle centré](Sketcher_CreateRectangle_Center/fr.md).

![](images/SketcherCreateRectangleExample.png‎ )



## Utilisation

-   Après avoir appuyé sur le bouton <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:24px;"> **Rectangle**, cliquez une fois pour définir le premier coin, puis déplacez la souris et une seconde fois pour définir le coin opposé.
-   Appuyez sur **Echap** ou cliquez sur le bouton droit de la souris pour annuler la fonction.



## Remarques

-   Lorsque les outils rectangulaires sont lancés, une section **Paramètres du rectangle** est ajoutée en haut du [panneau des tâches](Task_panel/fr.md) ({{Version/fr|0.22}}). Elle contient :

1.  Une boîte à boutons **Mode** pour choisir l\'un des modes de dessin du rectangle :
    -   Coin, longueur et largeur
    -   Centre, longueur et largeur
    -   3 coins
    -   Centre et deux coins
2.  Une case à cocher **Coins arrondis** pour appliquer des coins arrondis au rectangle.
3.  Une case à cocher **Cadre** pour ajouter un contour avec un décalage constant au rectangle (arrondi).

-   Les trois boutons de cette sélection lancent maintenant le même outil mais avec différentes combinaisons prédéfinies de mode et d\'options qui peuvent encore être modifiées après le premier clic.
-   Si l\'option **Coins arrondis** est activée, que le décalage est vers l\'intérieur et que la valeur du décalage est supérieure au rayon de l\'angle, le contour décalé sera créé sans filets.
-   Les modes **3 coins** et **Centre et deux coins** créent des parallélogrammes plutôt que des rectangles.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRectangle/fr
