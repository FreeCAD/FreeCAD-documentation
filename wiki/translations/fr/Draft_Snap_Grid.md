---
- GuiCommand   */fr
   Name   *Draft Snap Grid
   Name/fr   *Draft Aimantation Grille
   Workbenches   *[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso   * [Draft Aimantation](Draft_Snap/fr.md), [Draft Verrouillage de l'aimantation](Draft_Snap_Lock/fr.md), [Draft Basculer la grille](Draft_ToggleGrid/fr.md), [Draft Plan de travail](Draft_SelectPlane/fr.md)
---

# Draft Snap Grid/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Grid.svg  style="width   *24px;"> **Draft Aimantation Grille** permet de s\'aimanter aux intersections des lignes de la grille. La grille ne peut être utilisée que si la préférence **Activer la grille** est sélectionnée. Voir [Préférences](#Pr.C3.A9f.C3.A9rences.md).

![](images/Draft_Snap_Grid_example.png ) 
*Aimantation du deuxième point d'une ligne à la grille*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Changez éventuellement le [plan de travail et/ou la grille](Draft_SelectPlane/fr.md).
2.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width   *16px;">. [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
3.  Si **Draft Aimantation Grille** n\'est pas active, faites l\'une des choses suivantes    *
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Grid.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu, sélectionnez l\'option **<img src="images/Draft_Snap_Grid.svg" width=16px> Aimanter sur la grille (OFF)**.
4.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
5.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
6.  La grille est maintenant affichée si elle n\'était pas encore visible.
7.  Déplacez le curseur près de l\'intersection de deux lignes de la grille.
8.  Si une intersection est trouvée, le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Grid.svg  style="width   *16px;"> est affichée près du curseur.
9.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)

-   Pour utiliser la grille, sélectionnez    * **Édition → Préférences... → Draft → Grille et aimantation → Grille → Activer la grille**. Après avoir modifié cette préférence, vous devez redémarrer FreeCAD.
-   D\'autres préférences de grille sont également disponibles    * **Édition → Préférences... → Draft → Grille et aimantation → Grille**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/fr
