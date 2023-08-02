---
- GuiCommand:
   Name: Draft Snap Angle
   Name/fr: Draft Aimantation Angles
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Angle/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> **Draft Aimantation Angle** permet de s\'aimanter aux points cardinaux spéciaux sur les bords circulaires, pour des multiples de 30° et 45°. Les bords peuvent appartenir à des objets [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) mais aussi à des objets créés avec d\'autres [ateliers](Workbenches/fr.md).

![](images/Draft_Snap_Angle_example.png ) 
*Aimantation du deuxième point d'une ligne au point -30° d'un bord circulaire. Les petits cercles magenta indiquent tous les points cardinaux spéciaux disponibles.*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Angle** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Angle.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Maintenez le bouton **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** dans le [Draft Widget aimantation](Draft_snap_widget/fr.md) et dans le menu qui s\'ouvre, sélectionnez l\'option **<img src="images/Draft_Snap_Angle.svg" width=x16px> Aimanter à l'angle (OFF)**.
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Déplacez le curseur sur une arête circulaire.
6.  L\'arête est mise en évidence.
7.  Si un point cardinal est trouvé, il est marqué et l\'icône <img alt="" src=images/Draft_Snap_Angle.svg  style="width:16px;"> s\'affiche près du curseur.
8.  Vous pouvez également rapprocher le curseur d\'un autre point cardinal pour le sélectionner.
9.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Angle/fr
