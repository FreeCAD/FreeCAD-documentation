---
 GuiCommand:
   Name: Draft Snap Parallel
   Name/fr: Draft Aimantation Parallèle
   MenuLocation: Aimantation , Aimanter à la parallèle 
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Parallel/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:24px;"> **Draft Aimantation Parallèle** permet de s\'aimanter à une ligne imaginaire parallèle à des arêtes droites. Les arêtes peuvent appartenir à des objets de [Draft](Draft_Workbench/fr.md) ou de [BIM](BIM_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

Jusqu\'à 8 arêtes peuvent être référencées par cette option d\'aimantation et par [Draft Aimantation Extension](Draft_Snap_Extension/fr.md), ce qui permet d\'aimanter des intersections virtuelles. Les deux options d\'aimantation peuvent également être combinées avec d\'autres options d\'aimantation.

![](images/Draft_Snap_Parallel_example.png ) 
*Aimantation du deuxième point d'une ligne à une ligne invisible parallèle à une arête*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activée. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Parallèle** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Parallel.svg" width=16px> [Aimanter à la parallèle ](Draft_Snap_Parallel/fr.md)** de la barre d\'outils d\'aimantation.
    -   [Draft](Draft_Workbench/fr.md) : maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Parallel.svg" width=16px> Aimanter à la parallèle**.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_Parallel.svg" width=16px> Aimanter à la parallèle** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Choisissez une commande de Draft et de BIM pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Choisissez un premier point. Cette option d\'aimantation nécessite un point précédent. La ligne d\'aimantation parallèle passera par ce point.
6.  Déplacez le curseur sur une arête droite.
7.  L\'arête est mise en évidence.
8.  Si vous déplacez maintenant le curseur autour du point précédent, vous remarquerez un effet \"magnétique\" lorsque le curseur se trouve sur la ligne d\'aimantation parallèle.
9.  Le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:16px;"> s\'affiche près du curseur.
10. Cliquez pour confirmer le point.



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Parallel/fr
