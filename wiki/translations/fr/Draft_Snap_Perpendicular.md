---
- GuiCommand   */fr
   Name   *Draft Snap Perpendicular
   Name/fr   *Draft Aimantation Perpendiculaire
   Workbenches   *[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso   *[Draft Aimantation](Draft_Snap/fr.md), [Draft Verrouillage de l'aimantation](Draft_Snap_Lock/fr.md)
---

# Draft Snap Perpendicular/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width   *24px;"> **Draft Aimantation Perpendiculaire** permet de s\'aimanter aux points perpendiculaires sur les faces ({{Version/fr|1.0}}) et les arêtes. Les faces et les arêtes peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

Cette option d\'aimantation permet également de trouver des points sur des faces et des arêtes étendues.

![](images/Draft_Snap_Perpendicular_example.png ) 
*Aimantation du deuxième point d'une ligne au point perpendiculaire sur une arête étendue*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width   *16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Perpendiculaire** n\'est pas actif, faites l\'une des choses suivantes    *
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Perpendicular.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Perpendicular.svg" width=16px> Aimanter à la perpendiculaire (OFF)**.
3.  Choisissez une commande de [Draft](Draft_Workbench/fr.md) ou de [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Choisissez un premier point. Cette option d\'aimantation nécessite un point précédent. Le point perpendiculaire sera déterminé par rapport à ce point.
6.  Déplacez le curseur sur une face ou un bord.
7.  La face ou l\'arête est mise en évidence.
8.  Si un point perpendiculaire est trouvé, le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width   *16px;"> est affichée près du curseur.
9.  S\'il y a plusieurs points perpendiculaires    * déplacez éventuellement le curseur vers un autre point perpendiculaire. {{Version/fr|1.0}}
10. Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Perpendicular/fr
