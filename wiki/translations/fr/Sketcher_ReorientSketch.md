---
 GuiCommand:
   Name: Sketcher ReorientSketch
   Name/fr: Sketcher Réorienter une esquisse
   MenuLocation: Esquisse , Réorienter une esquisse...
   Workbenches: Sketcher_Workbench/fr, PartDesign_Workbench/fr
   SeeAlso: Sketcher_MapSketch/fr, Sketcher_NewSketch/fr
---

# Sketcher ReorientSketch/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:24px;"> [Sketcher Réorienter une esquisse](Sketcher_ReorientSketch/fr.md) place une esquisse sur l\'un des plans principaux avec un décalage facultatif. Il peut également être utilisé pour détacher une esquisse.



## Utilisation

1.  Sélectionnez une esquisse.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ReorientSketch.svg" width=16px> [Réorienter esquisse](Sketcher_ReorientSketch/fr.md)** (non disponible dans l\'[atelier PartDesign](PartDesign_Workbench.md)).
    -   Sélectionnez l\'option **Esquisse → <img src="images/Sketcher_ReorientSketch.svg" width=16px> Réorienter l'esquisse** du menu.

    1.  Si l\'esquisse est attachée :
    2.  La fenêtre de dialogue **L\'esquisse a un support** s\'ouvre.
    3.  Appuyez sur le bouton **Oui** pour détacher l\'esquisse.
3.  La fenêtre de dialogue **Sélection du plan** s\'ouvre.
4.  Vous pouvez appuyer sur le bouton **Annuler** pour ne détacher que l\'esquisse et terminer l\'outil.
5.  Spécifiez le plan pour l\'orientation. Le plan est relatif au système de coordonnées local dans lequel se trouve l\'esquisse :
    -   Si la case **Inverser la direction** n\'est pas cochée :
        -   En haut : **Plan XY**
        -   Devant : **Plan XZ**
        -   A droite : **Plan YZ**
    -   Si la case **Sens inverse** est cochée :
        -   Bas : **Plan XY**
        -   Arrière : **Plan XZ**
        -   Gauche : **Plan YZ**
6.  Vous pouvez changer le **Décalage**. Le décalage est mesuré par rapport à l\'axe Z, Y ou X du système de coordonnées local.
7.  Appuyez sur le bouton **OK**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ReorientSketch/fr
