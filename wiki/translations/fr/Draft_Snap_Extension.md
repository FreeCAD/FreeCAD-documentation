---
 GuiCommand:
   Name: Draft Snap Extension
   Name/fr: Draft Aimantation Extension
   MenuLocation: Aimantation , Aimanter à l'extension
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Extension/fr



## Description

L\'option <img alt="" src=images/Draft_Snap_Extension.svg  style="width:24px;"> **Draft Aimantation Extension** permet de s\'aimanter à une ligne imaginaire qui s\'étend au-delà des extrémités des bords droits. Les bords peuvent appartenir à des objets de [Draft](Draft_Workbench/fr.md) ou de [BIM](BIM_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

Jusqu\'à 8 arêtes peuvent être référencées par cette option d\'aimantation et par [Draft Aimantation Parallèle](Draft_Snap_Parallel/fr.md), ce qui permet d\'aimanter des intersections virtuelles. Les deux options d\'aimantation peuvent également être combinées avec d\'autres options d\'aimantation.

![](images/Draft_Snap_Extension_example.png ) 
*Aimantation du deuxième point d'une ligne au prolongement d'une arête*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Extension** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Extension.svg" width=x16px> [Aimanter à l'extension](Draft_Snap_Extension/fr.md)** de la barre d\'outils Draft Aimantation.
    -   [Draft](Draft_Workbench/fr.md) : maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** dans le [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Extension.svg" width=16px> Aimanter à l'extension**.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_Extension.svg" width=16px> Aimanter à l'extension** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Choisissez une commande de Draft et de BIM pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur une arête droite.
6.  L\'arête est mise en évidence.
7.  Si vous déplacez maintenant le curseur au-delà des extrémités de l\'arête, vous verrez apparaître une ligne en pointillés lorsque le curseur se trouve sur l\'arête prolongée.
8.  Le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Extension.svg  style="width:16px;"> s\'affiche près du curseur.
9.  Cliquez pour confirmer le point.



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Extension/fr
