---
 GuiCommand:
   Name: Draft Snap Near
   Name/fr: Draft Aimantation Au plus proche
   MenuLocation: Aimantation , Aimanter au plus proche
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Near/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Near.svg  style="width:24px;"> **Draft Aimantation Au plus proche** permet de s\'aimanter au point le plus proche sur les faces et les arêtes. Les faces et les arêtes peuvent appartenir à des objets de [Draft](Draft_Workbench/fr.md) ou de [BIM](BIM_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

![](images/Draft_Snap_Near_example.png ) 
*Aimantation du deuxième point d'une ligne au point le plus proche d'une arête*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Au plus proche** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Near.svg" width=16px> [Aimanter au plus proche](Draft_Snap_Near/fr.md)** de la barre d\'outils Draft Aimantation.
    -   [Draft](Draft_Workbench/fr.md) : maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Near.svg" width=16px> Aimanter au plus proche**.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_Near.svg" width=16px> Aimanter au plus proche** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Choisissez une commande de Draft et de BIM pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur une face ou une arête.
6.  La face ou l\'arête est mise en évidence.
7.  Si un point le plus proche est trouvé, il est marqué.
8.  Vous pouvez également déplacer le curseur le long de la face ou de l\'arête pour sélectionner un autre point le plus proche.
9.  Cliquez pour confirmer le point.



## Remarques

-   Ce n\'est pas une bonne idée d\'avoir [Draft Aimantation Au plus proche](Draft_Snap_Near/fr.md) actif en permanence car il est prioritaire sur de nombreuses autres options d\'aimantation.



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/fr
