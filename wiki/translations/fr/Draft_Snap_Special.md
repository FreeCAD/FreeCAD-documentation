---
 GuiCommand:
   Name: Draft Snap Special
   Name/fr: Draft Aimantation Spécial
   MenuLocation: Aimantation , Aimanter à des points spéciaux
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   Version: 0.17
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Special/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Special.svg  style="width:24px;"> **Draft Aimantation Spécial** permet de s\'aimanter à des [points spéciaux](#Points_sp.C3.A9ciaux_accept.C3.A9s.md) définis par l\'objet. Les objets acceptés sont les [Arch Murs](Arch_Wall/fr.md), les [Arch Structures](Arch_Structure/fr.md) et les [Arch Equipements](Arch_Equipment/fr.md).

![](images/Draft_Snap_Special_example.png ) 
*Aimantation du deuxième point d'une ligne à un point spécial d'un Arch mur, qui est un sommet de son objet Base*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;">. [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Spécial** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Special.svg" width=16px> [Aimanter à des points spéciaux](Draft_Snap_Special/fr.md)** de la barre d\'outils Draft Aimantation.
    -   [Draft](Draft_Workbench/fr.md) : maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Special.svg" width=16px> Aimanter à des points spéciaux**.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_Special.svg" width=16px> Aimanter à des points spéciaux** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Choisissez une commande de Draft et de BIM pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur un objet pris en charge.
6.  L\'objet est mis en évidence.
7.  Si un point spécial est trouvé, il est marqué et l\'icône <img alt="" src=images/Draft_Snap_Special.svg  style="width:16px;"> s\'affiche près du curseur.
8.  Si l\'objet a plusieurs points spéciaux : rapprochez éventuellement le curseur d\'un autre point spécial.
9.  Cliquez pour confirmer le point.



## Points spéciaux acceptés 

-   Les sommets de l\'objet **Base** des <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Arch Murs](Arch_Wall/fr.md).
-   Le point **Placement** des <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Arch Structures](Arch_Structure/fr.md).
-   Les **Snap Points** des <img alt="" src=images/Arch_Equipment.svg  style="width:16px;"> [Arch Equipements](Arch_Equipment/fr.md).



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Special/fr
