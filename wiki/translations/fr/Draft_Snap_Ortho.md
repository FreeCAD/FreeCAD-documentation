---
- GuiCommand:
   Name: Draft Snap Ortho
   Name/fr: Draft Aimantation Orthogonal
   Workbenches: Draft_Workbench/fr, Arch_Workbench/fr
   SeeAlso: Draft_Snap/fr, Draft_Snap_Lock/fr
---

# Draft Snap Ortho/fr

## Description

L\'option <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:24px;"> **Draft Aimantation Orthogonal** permet de s\'aimanter sur des lignes imaginaires qui croisent le point précédent à des multiples de 45°. Les lignes et les angles sont relatifs au plan XY du système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md).

![](images/Draft_Snap_Ortho_example.png ) 
*Aimantation du deuxième point d'une ligne à une ligne imaginaire qui fait un angle de 45° avec l'axe X. Les petits cercles magenta indiquent toutes les directions possibles.*

## Utilisation

Pour des informations générales sur l\'aimantation voir [Draft Aimantation](Draft_Snap/fr.md).

1.  Assurez-vous que l\'aimantation est activé. Voir <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;">. [Draft Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md).
2.  Si **Draft Aimantation Orthogonal** n\'est pas actif, faites l\'une des choses suivantes :
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Ortho.svg" width=16px>** de la barre d\'outils Draft Aimantation.
    -   Appuyez sur le bouton **<img src="images/Draft_Snap_Ortho.svg" width=16px>** du [Draft Widget aimantation](Draft_snap_widget/fr.md).
3.  Choisissez une commande [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
4.  Notez que vous pouvez également modifier les options d\'aimantation lorsqu\'une commande est active.
5.  Choisissez un premier point. Cette option d\'aimantation nécessite un point précédent.
6.  Si vous déplacez le curseur autour du point précédent, vous remarquerez un effet \"magnétique\" lorsque le curseur se trouve sur une ligne imaginaire infinie traversant ce point à un angle de 0°, 45°, 90° ou 135°.
7.  Le point est marqué et l\'icône <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:16px;"> s\'affiche près du curseur.
8.  Cliquez pour confirmer le point.

## Préférences

Voir [Draft Préférences](Draft_Snap/fr#Pr.C3.A9f.C3.A9rences.md)



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Ortho/fr
