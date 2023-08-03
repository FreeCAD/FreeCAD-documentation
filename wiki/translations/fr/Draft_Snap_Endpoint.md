---
 GuiCommand:
   Name: Draft Snap Endpoint
   Name/fr: Draft Aimantation Terminaison
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Endpoint/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> **Draft Aimantation Terminaison** permet de s\'aimanter aux extrémités des arêtes. Les arêtes peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

![](images/Draft_Snap_Endpoint_example.png ) 
*Aimantation du deuxième point d'une ligne au point d'extrémité d'une arête*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activée. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Terminaison** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Endpoint.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Endpoint.svg" width=16px> Aimanter au point d'extrémité (OFF)**.
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur une arête.
6.  L\'arête est mise en évidence.
7.  Si un point final est trouvé, il est marqué et l\'icône <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> s\'affiche près du curseur.
8.  Si vous le souhaitez, vous pouvez rapprocher le curseur de l\'autre extrémité pour sélectionner ce point.
9.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Endpoint/fr
