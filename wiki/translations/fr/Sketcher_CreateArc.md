---
 GuiCommand:
   Name: Sketcher Arc
   Name/fr: Sketcher Arc par centre
   MenuLocation: Esquisse , Géométries d'esquisse , Créer un arc à partir du centre
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **A**
   SeeAlso: Sketcher_CreateCircle/fr
---

# Sketcher CreateArc/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateArc.svg  style="width:24px;"> [Sketcher Arc par centre](Sketcher_CreateArc/fr.md) crée un arc par son centre et ses extrémités. {{Version/fr|1.0}} : ou par ses extrémités et un point de l\'arc.

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:400px;"> 
*Arc créé en mode Centre avec des contraintes appliquées automatiquement, définies par la saisie de tous les paramètres de la vue.*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateArc.svg" width=16px> [Arc par son centre et ses extrémités](Sketcher_CreateArc/fr.md)**.
    -   Sélectionnez l\'option **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateArc.svg" width=16px> Créer un arc à partir du centre** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_CreateArc.svg" width=16px> Créer un arc à partir du centre** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **A**.
2.  Le curseur se transforme en croix avec l\'icône du mode d\'outil courant.
3.  La section **Paramètres de l\'arc** ({{Version/fr|1.0}}) est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
4.  Il est possible d\'appuyer sur la touche **M** ou de choisir dans la liste déroulante de la section des paramètres pour changer le mode de l\'outil :
    -   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:16px;"> **Centre** :
        1.  Choisissez le centre de l\'arc, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
        2.  Choisissez le point de départ de l\'arc, cela définit également le rayon, ou avec Dim-OVP : entrez le rayon et/ou l\'angle de départ de l\'arc. L\'angle est relatif à l\'axe X de l\'esquisse. Aucune contrainte n\'est créée pour cet angle.
        3.  Choisissez le point final de l\'arc, ou avec Dim-OVP : entrez l\'angle d\'ouverture de l\'arc.
    -   <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:16px;"> **Cercle par 3 points du bord** : {{Version/fr|1.0}}
        1.  Choisissez les points de départ et d\'arrivée de l\'arc, ou avec Pos-OVP : entrez leurs coordonnées X et/ou Y.
        2.  Choisissez un autre point pour définir le rayon, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y. Aucune contrainte n\'est créée pour ce point.
5.  L\'arc est créé et les contraintes Pos-OVP et Dim-OVP applicables sont ajoutées.
6.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des arcs.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArc/fr
