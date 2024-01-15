---
 GuiCommand:
   Name: Sketcher Offset
   Name/fr: Sketcher Décaler une géométrie
   MenuLocation: Esquisse , Outils d'esquisse , Décaler une géométrie
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **T**
   Version: 0.22
   SeeAlso: 
---

# Sketcher Offset/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> [Sketcher Décaler une géométrie](Sketcher_Offset/fr.md) dessine des bords équidistants autour de bords sélectionnés. Au démarrage de l\'outil, le pointeur de la souris se transforme en une croix blanche avec une icône de décalage rouge :  <img alt="" src=images/Sketcher_Pointer_Create_Offset.svg  style="width:32px;"> .

<img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;"> 
*Arêtes équidistantes autour d'une polyligne de construction fermée (O) et ouverte (U)*



## Utilisation

1.  Sélectionner une ou plusieurs arêtes.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Sketcher_Offset.svg" width=16px> [Décaler une géométrie](Sketcher_Offset/fr.md)**.
    -   Sélectionnez l\'option **Sketcher → Outils Sketcher → <img src="images/Sketcher_Offset.svg" width=16px> Décaler une géométrie** du menu.
    -   Le raccourci clavier : **Z** puis **T**.
3.  Une section **Paramètres du décalage** est ajoutée en haut du [panneau des tâches](Task_panel/fr.md).
4.  Vous pouvez modifier le **Mode** de {{Value|Arc}} (par défaut) à {{Value|Intersection}}.
5.  Vous pouvez cocher la case **Supprimer les géométries d\'origine** pour ne conserver que le nouveau contour.
6.  Vous pouvez cocher la case **Ajouter une contrainte de décalage** pour ajouter une contrainte dimensionnelle entre le contour décalé et la géométrie d\'origine.
7.  Faites glisser le curseur et cliquez, ou entrez une distance pour définir le décalage et terminer la commande. Cette opération supprime également la section **Paramètres du décalage** du panneau des tâches.

Si l\'option **Ajouter une contrainte de décalage** a été activée, le décalage peut être ajusté en modifiant la contrainte dimensionnelle.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset/fr
