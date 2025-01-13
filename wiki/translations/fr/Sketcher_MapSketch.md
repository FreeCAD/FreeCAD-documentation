---
 GuiCommand:
   Name: Sketcher_MapSketch
   Name/fr: Sketcher Ancrer une esquisse
   MenuLocation: Esquisse , Ancrer une esquisse...
   Workbenches: Sketcher_Workbench/fr, PartDesign_Workbench/fr
   SeeAlso: Sketcher_ReorientSketch/fr, Sketcher_NewSketch/fr
---

# Sketcher MapSketch/fr



## Description

L\'outil <img alt="" src=images/Sketcher_MapSketch.svg  style="width:24px;"> [Sketcher Ancrer une esquisse](Sketcher_MapSketch/fr.md) permet d\'ancrer une esquisse à la géométrie sélectionnée.

Les cas d\'utilisation typiques sont les suivants :

-   L\'esquisse a été créée sur un plan standard (XY, XZ ou YZ) et vous souhaitez l\'ancrer à la face d\'un solide afin de construire une nouvelle fonction.
-   L\'esquisse a été ancrée à une face spécifique d\'un solide mais vous devez l\'ancrer à une autre face.
-   Un modèle cassé doit être réparé.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">



## Utilisation

1.  Sélectionnez un objet avec une forme, ou un ou plusieurs sommets, arêtes, et/ou faces, et/ou un plan.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le **<img src="images/Sketcher_MapSketch.svg" width=16px> [Ancrer l'esquisse...](Sketcher_MapSketch/fr.md)**.
    -   Sélectionnez le bouton **Esquisse → <img src="images/Sketcher_MapSketch.svg" width=16px> [Ancrer l'esquisse...](Sketcher_MapSketch/fr.md)** du menu.
3.  La boîte de dialogue **Sélectionner une esquisse** s\'ouvre.
4.  Sélectionnez une esquisse dans la liste déroulante.
5.  Appuyez sur le bouton **OK**.
6.  La boîte de dialogue **Ancrage de l\'esquisse** s\'ouvre.
7.  Sélectionnez un [mode d\'ancrage](Part_EditAttachment/fr#Modes_d'ancrage.md) dans la liste déroulante, ou sélectionnez **Ne pas ancrer** pour désancrer l\'esquisse.
8.  Appuyez sur le bouton **OK**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/fr
