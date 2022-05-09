---
- GuiCommand   */fr
   Name   *Draft Snap Center
   Name/fr   *Draft Aimantation Centre
   Workbenches   *[Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso   *[Draft Aimantation](Draft_Snap/fr.md), [Draft Verrouillage de l'aimantation](Draft_Snap_Lock/fr.md)
---

# Draft Snap Center/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Center.svg  style="width   *24px;"> **Draft Aimantation Centre** permet de s\'aimanter au point central des faces et des arêtes circulaires et au point {{PropertyData/fr|Placement}} de [Draft Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md) et [Arch Partie de bâtiment](Arch_BuildingPart/fr.md). Les faces et les arêtes peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

![](images/Draft_Snap_Center_example_arc.png ) 
*Aimantation du deuxième point d'une ligne au centre d'un bord circulaire*

![](images/Draft_Snap_Center_example_buildingpart.png ) 
*Aimantation du deuxième point d'une ligne au point Placement d'un Arch Partie de bâtiment*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activée. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width   *16px;">. [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Centre** n\'est pas actif, faites l\'une des choses suivantes    *
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Center.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** dans le [Draft Widget aimantation](Draft_snap_widget.md) et dans le menu sélectionnez l\'option **<img src="images/Draft_Snap_Center.svg" width=16px> Aimanter au centre (OFF)**.
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Effectuez l\'une des opérations suivantes    *
    -   Pour sélectionner le point central d\'une face ou d\'une arête circulaire    *
        -   Déplacez le curseur sur la face ou l\'arête.
        -   La face ou l\'arête est mise en surbrillance.
    -   Pour sélectionner le point **Placement** d\'un [Draft Proxy pour plan de travail](Draft_WorkingPlaneProxy/fr.md)    *
        -   Déplacez le curseur sur n\'importe quel élément du proxy du plan de travail.
        -   Le proxy du plan de travail n\'est pas mis en évidence.
    -   Pour sélectionner le point **Placement** d\'une [Arch Partie de bâtiment](Arch_BuildingPart/fr.md)    *
        -   Déplacez le curseur sur l\'un des bords du petit symbole d\'axe de la Partie de bâtiment, ou sur le texte à côté qui affiche les **Label** de la Partie de bâtiment et son niveau.
        -   Seuls les bords du symbole d\'axe sont mis en évidence. Le texte n\'est pas mis en évidence.
6.  Si un point est trouvé, il est marqué et l\'icône <img alt="" src=images/Draft_Snap_Center.svg  style="width   *16px;"> s\'affiche près du curseur.
7.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Center/fr
