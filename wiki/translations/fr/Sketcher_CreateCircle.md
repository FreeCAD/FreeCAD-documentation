---
 GuiCommand:
   Name: Sketcher CreateCircle
   Name/fr: Sketcher Cercle par centre
   MenuLocation: Esquisse , Géometries d'esquisse  , Créer un cercle par son centre
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **C**
   SeeAlso: Sketcher_CreateArc/fr
---

# Sketcher CreateCircle/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:24px;"> [Sketcher par centre](Sketcher_CreateCircle/fr.md) crée un cercle par son centre et un point de la circonférence. {{Version/fr|1.0}} : ou bien par trois points de la circonférence.

![](images/Sketcher_CircleExample1.png‎ )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateCircle.svg" width=16px> [Cercle par son centre et un point de la circonférence](Sketcher_CreateCircle/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géometries d'esquisse → <img src="images/Sketcher_CreateCircle.svg" width=16px> Créer un cercle par son centre** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_CreateCircle.svg" width=16px> Créer un cercle par son centre** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **C**.
2.  Le curseur se transforme en croix avec l\'icône du mode d\'outil courant.
3.  La section **Paramètres du cercle** ({{Version/fr|1.0}}) est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
4.  Il est possible d\'appuyer sur la touche **M** ou de choisir dans la liste déroulante de la section des paramètres pour changer le mode de l\'outil :
    -   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:16px;"> **Centre** :
        1.  Choisissez le centre du cercle, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
        2.  Choisissez un point pour définir le rayon du cercle, ou avec Dim-OVP : entrez ce rayon.
    -   <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:16px;"> **Cercle par 3 points du bord** : {{Version/fr|1.0}}
        1.  Choisissez trois points pour définir le cercle, ou avec Pos-OVP : entrez leurs coordonnées X et/ou Y. Aucune contrainte n\'est créée pour ces points.
5.  Le cercle est créé et les contraintes applicables basées sur Pos-OVP et Dim-OVP sont ajoutées.
6.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des cercles.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateCircle/fr
