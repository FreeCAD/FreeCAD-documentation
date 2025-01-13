---
 GuiCommand:
   Name: Draft Snap Intersection
   Name/fr: Draft Aimantation Intersection
   MenuLocation: Aimantation , Aimanter à l'intersection
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Intersection/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:24px;"> **Draft Aimantation Intersection** permet de s\'aimanter à l\'intersection de deux arêtes. Les arêtes peuvent appartenir à des objets de [Draft](Draft_Workbench/fr.md) ou de [BIM](BIM_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

Cette option d\'aimantation trouvera également les intersections apparentes de droites (étendues) si <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Draft Aimantation Plan de travail](Draft_Snap_WorkingPlane/fr.md) est également active.

![](images/Draft_Snap_Intersection_example.png ) 
*Aimantation du deuxième point d'une ligne à l'intersection de deux arêtes*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;">. [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Intersection** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Intersection.svg" width=16px> [Aimanter à l'intersection](Draft_Snap_Intersection/fr.md)** de la barre d\'outils Draft Aimantation.
    -   [Draft](Draft_Workbench/fr.md) : maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** du [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Intersection.svg" width=16px> Aimanter à l'intersection**.
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_Intersection.svg" width=16px> Aimanter à l'intersection** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
3.  Choisissez une commande de Draft et de BIM pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur l\'une des arêtes qui se croisent.
6.  L\'arête est mis en évidence.
7.  Déplacez le curseur sur l\'autre arête.
8.  L\'arête est mise en évidence.
9.  Si une intersection est trouvée, le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> est affichée près du curseur.
10. Si les bords ont plusieurs intersections : déplacez éventuellement le curseur plus près d\'une autre intersection.
11. Cliquez pour confirmer le point.



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Intersection/fr
