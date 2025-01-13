---
 GuiCommand:
   Name: Draft Snap WorkingPlane
   Name/fr: Draft Aimantation Plan de travail
   MenuLocation: Aimantation , Aimanter au plan de travail
   Workbenches: Draft_Workbench/fr, BIM_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr, Draft_SelectPlane/fr
---

# Draft Snap WorkingPlane/fr



## Description

L\'option <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:24px;"> **Draft Aimantation Plan de travail** projette les points d\'aimantation sur le [plan de travail](Draft_SelectPlane/fr.md) en cours. Elle ne peut être utilisée qu\'en combinaison avec une autre option d\'aimantation.

![](images/Draft_Snap_WorkingPlane_example.png ) 
*Aimantation du deuxième point d'une ligne au point d'extrémité projeté d'une arête*



## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Changez éventuellement de [plan de travail](Draft_SelectPlane/fr.md).
2.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;">. [Draft Verrouiller l\'aimantation](Draft_Snap_Lock/fr.md).
3.  Si **Draft Aimantation Plan de travail** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px> [Aimanter au plan de travail](Draft_Snap_WorkingPlane/fr.md)** de la barre d\'outils Draft Aimantation.
    -   [Draft](Draft_Workbench/fr.md) : appuyez sur le bouton **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px>[Aimanter au plan de travail](Draft_Snap_WorkingPlane/fr.md)** du [Draft Widget d\'aimantation](Draft_snap_widget/fr.md).
    -   [BIM](BIM_Workbench/fr.md) : sélectionnez l\'option **Aimantation → <img src="images/Draft_Snap_WorkingPlane.svg" width=16px> Aimanter au plan de travail** du menu ou dans le menu contextuel de la [vue 3D](3D_view/fr.md).
4.  Assurez-vous qu\'au moins une autre option d\'aimantation est active.
5.  Choisissez une commande de Draft et de BIM pour créer votre géométrie.
6.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
7.  Déplacez le curseur sur l\'objet sur lequel vous souhaitez effectuer l\'aimantation.
8.  L\'objet est mis en surbrillance.
9.  Si un point d\'aimantation est trouvé, il est projeté sur le [plan de travail](Draft_SelectPlane/fr.md) où il est marqué.
10. Cliquez pour confirmer le point.



## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap WorkingPlane/fr
