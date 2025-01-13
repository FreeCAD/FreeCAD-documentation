---
 GuiCommand:
   Name: Draft Snap Midpoint
   Name/fr: Draft Aimantation Milieu
   MenuLocation: Aimantation , Aimanter au point milieu
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Midpoint/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> **Draft Aimantation Milieu** permet de s\'aimanter au point milieu des segments. Les segments peuvent appartenir à des objets de [Draft](Draft_Workbench/fr.md) ou de [BIM](BIM_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

![](images/Draft_Snap_Midpoint_example.png ) 
*Aimantation du deuxième point d'une ligne au milieu d'une segment*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activée. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouiller l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Milieu** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Midpoint.svg" width=16px> [Aimanter au point milieu](Draft_Snap_Midpoint.md)** de la barre d\'outils Draft Aimantation.
    -   [Draft](Draft_Workbench/fr.md) : maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Midpoint.svg" width=16px> Aimanter au point milieu**.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_Midpoint.svg" width=16px> Aimanter au point milieu** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Choisissez une commande de Draft et de BIM pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur un segment.
6.  Le segment est mis en évidence.
7.  Si un point milieu est trouvé, il est marqué et l\'icône <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> s\'affiche près du curseur.
8.  Cliquez pour confirmer le point.



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Midpoint/fr
