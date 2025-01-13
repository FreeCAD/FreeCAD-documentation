---
 GuiCommand:
   Name: Sketcher Offset
   Name/fr: Sketcher Décaler une géométrie
   MenuLocation: Esquisse , Outils d'esquisse , Décaler une géométrie
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **T**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Offset/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> [Sketcher Décaler](Sketcher_Offset/fr.md) crée des arêtes équidistantes autour des arêtes sélectionnées.

<img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;"> 
*Arêtes équidistantes autour d'une polyligne de construction fermée (O) et ouverte (U)*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Dim-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) des dimensions.

1.  Sélectionnez une ou plusieurs lignes, cercles et/ou arcs de cercle.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_Offset.svg" width=16px> [Décaler la géométrie](Sketcher_Offset/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_Offset.svg" width=16px> Décaler la géométrie** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_Offset.svg" width=16px> Décaler la géométrie** du menu contextuel.
    -   Utilisez le raccourci clavier : **Z** puis **T**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  La section **Paramètres du décalage** est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
5.  Vous pouvez appuyer sur la touche **U** ou cochez la case **Supprimer les géométries d\'origine** pour ne conserver que le nouveau contour.
6.  Appuyez sur la touche **J** ou cochez la case **Ajouter une contrainte de décalage** pour ajouter une contrainte de dimension entre le contour décalé et la géométrie d\'origine.
7.  Appuyez sur la touche **M** ou sélectionnez dans la liste déroulante de la section des paramètres pour changer le mode de l\'outil :
    -   <img alt="" src=images/Sketcher_OffsetArc.svg  style="width:16px;"> 
**Arc**
    -   <img alt="" src=images/Sketcher_OffsetIntersection.svg  style="width:16px;"> 
**Intersection**
8.  Choisissez un point pour définir la distance de décalage, ou avec Dim-OVP : entrez cette distance.
9.  La géométrie est créée et si **Ajouter une contrainte de décalage** a été sélectionné, une contrainte dimensionnelle est ajoutée.

## Limitations

Cet outil présente certaines limitations, principalement dues à des problèmes liés à d\'[OCC](OpenCASCADE/fr.md) :

-   Les types de géométrie suivants ne sont actuellement pas pris en charge : ellipses, B-splines, hyperboles et paraboles.
-   Le décalage d\'une seule ligne peut donner des résultats inattendus.
-   Les profils ouverts sont décalés des deux côtés, ce qui crée un contour fermé.
-   La géométrie externe ne peut pas être décalée directement.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset/fr
