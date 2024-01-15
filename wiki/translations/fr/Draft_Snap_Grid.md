---
 GuiCommand:
   Name: Draft Snap Grid
   Name/fr: Draft Aimantation Grille
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   SeeAlso:  Draft_Snap/fr, Draft_Snap_Lock/fr, Draft_ToggleGrid/fr, Draft_SelectPlane/fr
---

# Draft Snap Grid/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Grid.svg  style="width:24px;"> **Draft Aimantation Grille** permet de s\'aimanter aux intersections des lignes de la grille.

![](images/Draft_Snap_Grid_example.png ) 
*Aimantation du deuxième point d'une ligne à la grille*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Vous pouvez changez le [plan de travail et/ou la grille](Draft_SelectPlane/fr.md).
2.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
3.  Si **Draft Aimantation Grille** n\'est pas active, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Grid.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Grid.svg" width=16px> Aimanter sur la grille**.
4.  Choisissez une commande de [Draft](Draft_Workbench/fr.md) ou de [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
5.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
6.  Si nécessaire, utilisez [Draft Basculer la grille](Draft_ToggleGrid/fr.md) pour afficher la grille. La grille doit être visible pour que cette option fonctionne.
7.  Déplacez le curseur près de l\'intersection de deux lignes de la grille.
8.  Si une intersection est trouvée, le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> est affichée près du curseur.
9.  Cliquez pour confirmer le point.



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)

-   Plusieurs préférences de grille sont disponibles : **Édition → Préférences... → Draft → Grille et aimantation**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/fr
