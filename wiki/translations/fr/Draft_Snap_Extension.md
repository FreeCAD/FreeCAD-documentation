---
- GuiCommand:/fr
   Name:Draft Snap Extension
   Name/fr:Draft Aimantation Extension
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso:[Draft Aimantation](Draft_Snap/fr.md), [Draft Aimantation Verrouiller](Draft_Snap_Lock/fr.md)
---

# Draft Snap Extension/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Extension.svg  style="width:24px;"> **Draft Aimantation Extension** permet de s\'aimanter à une ligne imaginaire qui s\'étend au-delà des extrémités des bords droits. Les bords peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

Jusqu\'à deux arêtes peuvent être référencées par cette option d\'aimantation et par [Draft Aimantation Parallèle](Draft_Snap_Parallel/fr.md), ce qui permet d\'aimanter des intersections virtuelles. Les deux options d\'aimantation peuvent également être combinées avec d\'autres options d\'aimantation.

![](images/Draft_Snap_Extension_example.png ) *Aimantation du deuxième point d'une ligne au prolongement d'une arête*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Aimantation Verrouiller](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Extension** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Extension.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** dans le [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu sélectionnez l\'option **<img src="images/Draft_Snap_Extension.svg" width=16px> Extension de l'aimantation**.
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur une arête droite.
6.  L\'arête est mise en évidence.
7.  Si vous déplacez maintenant le curseur au-delà des extrémités de l\'arête, vous verrez apparaître une ligne en pointillés lorsque le curseur se trouve sur l\'arête prolongée.
8.  Le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Extension.svg  style="width:16px;"> s\'affiche près du curseur.
9.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Extension/fr
