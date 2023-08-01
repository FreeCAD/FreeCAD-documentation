---
- GuiCommand:
   Name: Sketcher Snap
   Name/fr: Sketcher Aimantation
   Workbenches: [Sketcher](Sketcher_Workbench/fr.md)
   Version: 0.21
   SeeAlso: [Sketcher Grille](Sketcher_Grid/fr.md)
---

# Sketcher Snap/fr



## Description

La commande **Sketcher Aimantation** permet d\'activer l\'aimantation dans toutes les esquisses. Les aimantations et les paramètres de chacune d\'entre elles peuvent être modifiés dans le menu correspondant.

L\'aimantation ne fonctionne que lors de la création d\'une géométrie. Notez que l\'aimantation n\'est qu\'une aide au dessin, il ne produit pas de contraintes supplémentaires.



## Utilisation

1.  Appuyez sur le bouton **<img src="images/Sketcher_Snap.svg" width=16px> [Activer/désactiver l'aimantation](Sketcher_Snap.md)** pour activer l\'aimantation.
2.  Il est possible de cliquer sur la flèche vers le bas à droite du bouton pour ouvrir le menu. Les paramètres de ce menu ne peuvent être modifiés que si l\'accrochage est activé :
    ![](images/Sketcher_Snap_Menu.png )
    -   Si la case **Aimanter à la grille** est cochée, le curseur s\'aimantera aux lignes et aux intersections de la grille. Fonctionne également si la grille est invisible.

    -   Si la case **Aimanter aux objets** est cochée, le curseur se positionnera sur les bords de la géométrie et les points médians des lignes et des arcs.

    -   
        **Angle d'aimantation**
        
        spécifie l\'angle d\'aimantation angulaire. L\'aimantation se produit à des multiples de cette valeur à partir de la direction de l\'axe X positif de l\'esquisse. La touche **Ctrl** doit être maintenue enfoncée pour cet accrochage. Ne fonctionne que lors de la création de certaines géométries, des [lignes](Sketcher_CreateLine/fr.md) par exemple.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Snap/fr
