---
- GuiCommand:/fr
   Name:Draft Snap Perpendicular
   Name/fr:Draft Aimantation Perpendiculaire
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso:[Draft Aimantation](Draft_Snap/fr.md), [Draft Aimantation Verrouiller](Draft_Snap_Lock/fr.md)
---

# Draft Snap Perpendicular/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:24px;"> **Draft Aimantation Perpendiculaire** permet de s\'aimanter sur le point perpendiculaire des arêtes. Les arêtes peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

Cette option d\'aimantation permet également de trouver des points sur le prolongement des arêtes droites. Les arêtes circulaires sont toujours traitées comme des cercles complets, si une arête circulaire est un arc, le point trouvé peut ne pas se trouver sur l\'arête réelle.

![](images/Draft_Snap_Perpendicular_example.png ) 
*Aimantation du deuxième point d'une ligne au point perpendiculaire sur une arête étendue*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Aimantation Verrouiller](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Perpendiculaire** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Perpendicular.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu, sélectionnez l\'option **<img src="images/Draft_Snap_Perpendicular.svg" width=16px> Aimantation perpendiculaire**.
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Choisissez un premier point. Cette option d\'aimantation nécessite un point précédent. Le point perpendiculaire sera déterminé par rapport à ce point.
6.  Déplacez le curseur sur une arête.
7.  L\'arête est mise en évidence.
8.  Si une perpendiculaire est trouvée, le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:16px;"> s\'affiche près du curseur.
9.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Perpendicular/fr
