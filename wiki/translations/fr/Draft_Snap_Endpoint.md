---
 GuiCommand:
   Name: Draft Snap Endpoint
   Name/fr: Draft Aimantation Extrémité
   MenuLocation: Aimantation , Aimanter au point d'extrémité 
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Endpoint/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> **Draft Aimantation Extrémité** permet de s\'aimanter aux extrémités des arêtes. Les arêtes peuvent appartenir à des objets de [Draft](Draft_Workbench/fr.md) ou de [BIM](BIM_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

![](images/Draft_Snap_Endpoint_example.png ) 
*Aimantation du deuxième point d'une ligne à l'extrémité d'une arête*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activée. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouiller l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Extrémité** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Endpoint.svg" width=16px> [Aimanter au point d'extrémité](Draft_Snap_Endpoint/fr.md)** de la barre d\'outils Draft Aimantation.
    -   [Draft](Draft_Workbench/fr.md): maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Endpoint.svg" width=16px> Aimanter au point d'extrémité**.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_Endpoint.svg" width=16px> Aimanter au point d'extrémité** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Choisissez une commande de Draft ou de BIM pour créer votre géométrie.
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
