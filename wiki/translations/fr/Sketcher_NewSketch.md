---
 GuiCommand:
   Name: Sketcher NewSketch
   Name/fr: Sketcher Créer une esquisse
   MenuLocation: Esquisse , Créer une esquisse
   Workbenches: Sketcher_Workbench/fr
   SeeAlso: PartDesign_NewSketch/fr, Sketcher_MapSketch/fr, Sketcher_ReorientSketch/fr
---

# Sketcher NewSketch/fr

## Description

L\'outil <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Créer une esquisse](Sketcher_NewSketch/fr.md) crée une nouvelle esquisse et ouvre la [boîte de dialogue de Sketcher](Sketcher_Dialog/fr.md) pour l\'éditer.

Remarquez que l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md) possède son propre outil [Esquisse](PartDesign_NewSketch/fr.md). Lorsque vous travaillez sur un [PartDesign Corps](PartDesign_Body/fr.md), cet outil doit être utilisé à la place.



## Utilisation

1.  Si l\'esquisse doit être [ancrée](Part_EditAttachment/fr.md) à une géométrie existante : sélectionnez un objet avec une forme, ou un ou plusieurs sommets, arêtes et/ou faces, et/ou un plan.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_NewSketch.svg" width=16px> [Créer une esquisse](Sketcher_NewSketch.md)**.
    -   Sélectionnez l\'option **Esquisse → <img src="images/Sketcher_NewSketch.svg" width=16px> Créer une esquisse** du menu.
3.  Si la géométrie a été sélectionnée :
    1.  La fenêtre de dialogue **Ancrage de l\'esquisse** s\'ouvre.
    2.  Sélectionnez un [mode d\'ancrage](Part_EditAttachment/fr#Modes_d'ancrage.md) dans la liste déroulante ou sélectionnez **Ne pas ancrer** pour ignorer la sélection.
    3.  Appuyez sur le bouton **OK**.
4.  S\'il n\'y a pas de sélection ou si **Ne pas ancrer** a été sélectionné à l\'étape précédente :
    1.  La fenêtre de dialogue **Sélection du plan** s\'ouvre.
    2.  Spécifiez le plan pour l\'orientation. Le plan est relatif au système de coordonnées local dans lequel se trouve l\'esquisse :
        -   Si la case **Inverser la direction** n\'est pas cochée :
            -   Haut : **Plan XY**
            -   Avant : **Plan XZ**
            -   Droit : **Plan YZ**
        -   Si la case **Sens inverse** est cochée :
            -   Bas : **Plan XY**
            -   Arrière : **Plan XZ**
            -   Gauche : **Plan YZ**
    3.  Vous pouvez changer le **Décalage**. Le décalage est mesuré par rapport à l\'axe Z, Y ou X du système de coordonnées local.
    4.  Appuyez sur le bouton **OK**.
    5.  Une esquisse est créée.
5.  L\'esquisse est mise en mode édition et la [fenêtre de dialogue de Sketcher](Sketcher_Dialog/fr.md) s\'ouvre.
6.  Pour terminer le mode édition, voir <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Sketcher Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md).



## Remarques

-   Les esquisses existantes peuvent être attachées à des objets (différents) avec [Sketcher Ancrer une esquisse](Sketcher_MapSketch/fr.md) ou détachées et réorientées avec [Sketcher Réorienter une esquisse](Sketcher_ReorientSketch/fr.md).





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher NewSketch/fr
