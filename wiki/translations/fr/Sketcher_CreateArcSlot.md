---
 GuiCommand:
   Name: Sketcher CreateArcSlot
   Name/fr: Sketcher Rainure en arc
   MenuLocation: Esquisse , Géometries d'esquisse , Créer une rainure en arc
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **S** **2**
   Version: 1.0
   SeeAlso: Sketcher_CreateSlot/fr
---

# Sketcher CreateArcSlot/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:24px;"> [Sketcher Rainure en arc](Sketcher_CreateArcSlot/fr.md) crée une rainure en arc, une polyligne fermée composée de deux arcs concentriques parallèles fermés par deux demi-cercles ou deux lignes droites radiales.

<img alt="" src=images/Sketcher_CreateArcSlot_Example.png  style="width:300px;"> 
*Rainures en arc avec des extrémités en arc (à gauche) et des extrémités plates (à droite)*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateArcSlot.svg" width=16px> [Créer une rainure en arc](Sketcher_CreateArcSlot/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géometries d'esquisse → <img src="images/Sketcher_CreateArcSlot.svg" width=16px> Créer une rainure en arc** du menu.
    -   Le raccourci clavier : **G** puis **S**, puis **2**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  La section **Paramètres de la rainure en arc** est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
4.  Appuyez sur la touche **M** ou sélectionnez dans la liste déroulante de la section des paramètres pour changer le mode de l\'outil :
    -   <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:16px;"> **Extrémités arrondies** :
        1.  Choisissez le centre de la rainure en l\'arc, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
        2.  Choisissez le centre du premier demi-cercle, qui définit également le rayon de la ligne centrale (virtuelle) de la rainure, ou avec Dim-OVP : entrez le rayon et/ou l\'angle de départ de la rainure. L\'angle est relatif à l\'axe X de l\'esquisse. Aucune contrainte n\'est créée pour cet angle.
        3.  Choisissez le centre du deuxième demi-cercle, ou avec Dim-OVP : entrez l\'angle d\'ouverture de l\'arc de la ligne centrale.
        4.  Choisissez un point pour définir le rayon des demi-cercles, ou avec Dim-OVP : entrez ce rayon.
    -   <img alt="" src=images/Sketcher_CreateRectangleSlot.svg  style="width:16px;"> **Extrémités plates** :
        1.  Choisissez le centre de la rainure en arc, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
        2.  Choisissez le point de départ du premier arc, cela définit également son rayon, ou avec Dim-OVP : entrez le rayon et/ou l\'angle de départ du premier arc. L\'angle est relatif à l\'axe X de l\'esquisse. Aucune contrainte n\'est créée pour cet angle.
        3.  Choisissez le point final du premier arc, ou avec Dim-OVP : entrez l\'angle d\'ouverture de l\'arc.
        4.  Choisissez un point pour définir la largeur de la fente. Ou avec Dim-OVP : entrez cette largeur.
5.  La rainure est créée et les contraintes applicables basées sur Pos-OVP et Dim-OVP sont ajoutées.
6.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des rainures en arc.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Les points choisis pour définir le rayon des demi-cercles ou le décalage des arcs intérieurs et extérieurs n\'ont pas besoin de toucher la géométrie, la distance entre le curseur et le centre de la rainure contrôle en fait la valeur.
-   En mode **Extrémités arrondies**, le premier rayon s\'applique à un arc central virtuel, alors qu\'il s\'applique à l\'un des arcs de contour en mode **Extrémités plates**.
-   Si la valeur de la largeur en mode **Extrémités plates** est positive, l\'arc contraint devient l\'arc intérieur, pour une valeur négative, ce sera l\'arc extérieur.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcSlot/fr
