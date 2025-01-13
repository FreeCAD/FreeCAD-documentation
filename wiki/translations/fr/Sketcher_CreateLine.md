---
 GuiCommand:
   Name: Sketcher CreateLine
   Name/fr: Sketcher Ligne
   MenuLocation: Esquisse , Géométries d'esquisse , Créer une ligne
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **L**
   SeeAlso: Sketcher_CreatePolyline/fr
---

# Sketcher CreateLine/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateLine.svg  style="width:24px;"> [Sketcher Ligne](Sketcher_CreateLine/fr.md) crée une ligne. {{Version/fr|1.0}} : si le [mode de visibilité des paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) est activé, l\'outil dispose de trois modes.

![](images/Sketcher_LineExample1.png‎ )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateLine.svg" width=16px> [Créer une ligne](Sketcher_CreateLine/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_CreateLine.svg" width=16px> Créer une ligne** du menu.
    -   Utiliser le raccourci clavier : **G** puis **L**.
2.  Le curseur se transforme en croix avec l\'icône du mode d\'outil actuel.
3.  si le [mode de visibilité des paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) est activé, la section **Paramètres de la ligne** ({{Version/fr|1.0}}) est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
4.  Il est possible d\'appuyer sur la touche **M** ou de choisir dans la liste déroulante de la section des paramètres pour changer le mode de l\'outil :
    -   <img alt="" src=images/Sketcher_CreateLineAngleLength.svg  style="width:16px;"> **Point, largeur, angle** : {{Version/fr|1.0}}
        1.  Choisissez le point de départ de la ligne, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
        2.  Choisissez le point d\'arrivée de la ligne, ou avec Dim-OVP : entrez la longueur et/ou l\'angle de la ligne. L\'angle est relatif à l\'axe X du croquis.
    -   <img alt="" src=images/Sketcher_CreateLineLengthWidth.svg  style="width:16px;"> **Point, largeur, hauteur** : {{Version/fr|1.0}}
        1.  Choisissez le point de départ de la ligne, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
        2.  Choisissez le point d\'arrivée de la ligne, ou avec Dim-OVP : entrez sa distance X et/ou Y par rapport au point de départ.
    -   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:16px;"> **2 points** :
        1.  Choisissez le point de départ de la ligne, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
        2.  Choisissez le point d\'arrivée de la ligne, ou avec Pos-OVP : entrez sa coordonnée X et/ou Y.
5.  La ligne est créée et les contraintes Pos-OVP et Dim-OVP applicables sont ajoutées.
6.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des lignes.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/fr
