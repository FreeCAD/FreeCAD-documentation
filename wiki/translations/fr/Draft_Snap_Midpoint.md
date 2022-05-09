---
- GuiCommand   */fr
   Name   *Draft Snap Midpoint
   Name/fr   *Draft Aimantation Milieu
   Workbenches   *[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso   *[Draft Aimantation](Draft_Snap/fr.md), [Draft Verrouillage de l'aimantation](Draft_Snap_Lock/fr.md)
---

# Draft Snap Midpoint/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width   *24px;"> **Draft Aimantation Milieu** permet de s\'aimanter au point milieu des segments. Les segments peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

Dans la version 0.19 de FreeCAD, cette option d\'aimantation ne fonctionne que pour les segments droits et circulaires.

![](images/Draft_Snap_Midpoint_example.png ) 
*Aimantation du deuxième point d'une ligne au milieu d'une segment*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activée. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width   *16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Milieu** n\'est pas actif, faites l\'une des choses suivantes    *
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Midpoint.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu sélectionnez l\'option **<img src="images/Draft_Snap_Midpoint.svg" width=16px> Aimanter au point milieu (OFF)**.
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur un segment.
6.  Le segment est mis en évidence.
7.  Si un point milieu est trouvé, il est marqué et l\'icône <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width   *16px;"> s\'affiche près du curseur.
8.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Midpoint/fr
