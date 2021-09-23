---
- GuiCommand:/fr
   Name:Draft Snap Near
   Name/fr:Draft Aimantation Le plus proche
   Workbenches:[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso:[Draft Aimantation](Draft_Snap/fr.md), [Draft Aimantation Verrouiller](Draft_Snap_Lock/fr.md)
---

# Draft Snap Near/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> **Draft Aimantation Le plus proche** permet de s\'aimanter au point le plus proche sur les faces ou les arêtes. Les faces et les arêtes peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

![](images/Draft_Snap_Near_example.png ) *Aimantation du deuxième point d'une ligne au point le plus proche d'une arête*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;">. [Draft Aimantation Verrouiller](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Le plus proche** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Near.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu, sélectionnez l\'option **<img src="images/Draft_Snap_Near.svg" width=16px> Aimantation le plus proche**.
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur une face ou une arête.
6.  La face ou l\'arête est mise en évidence.
7.  Si un point le plus proche est trouvé, il est marqué.
8.  Vous pouvez également déplacer le curseur le long de la face ou de l\'arête pour sélectionner un autre point le plus proche.
9.  Cliquez pour confirmer le point.

## Remarques

-   Ce n\'est pas une bonne idée d\'avoir [Draft Aimantation Le plus proche](Draft_Snap_Near/fr.md) actif en permanence car il est prioritaire sur de nombreuses autres options d\'aimantation.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/fr
