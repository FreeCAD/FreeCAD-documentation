---
 GuiCommand:
   Name: Sketcher CreateSlot
   Name/fr: Sketcher Contour oblong
   MenuLocation: Esquisse , Géométries d'esquisse , Créer un contour oblong
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **S**
   SeeAlso: Sketcher_CreateArcSlot/fr
---

# Sketcher CreateSlot/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Sketcher Contour oblong](Sketcher_CreateSlot/fr.md) crée une contour oblong, une polyligne fermée composée de deux demi-cercles reliés par deux lignes droites parallèles.

![](images/SketcherCreateSlotExample.png‎ )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateSlot.svg" width=16px> [Créer un contour oblong](Sketcher_CreateSlot/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_CreateSlot.svg" width=16px> Créer un contour oblong** du menu.
    -   Le raccourci clavier : **G** puis **S**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  Choisissez le centre du premier demi-cercle, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
4.  Choisissez le centre du deuxième demi-cercle, ou avec Dim-OVP : entrez la distance entre les centres et/ou l\'angle du contour oblong. L\'angle est relatif à l\'axe X de l\'esquisse.
5.  Choisissez un point pour définir le rayon du contour oblong, ou avec Dim-OVP : entrez ce rayon.
6.  Le contour oblong est créé et les contraintes applicables basées sur Pos-OVP et Dim-OVP sont ajoutées.
7.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des emplacements.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-    {{VersionMinus/fr|0.21}}({{Version/fr|0.20}}) : maintenir **Ctrl** lors de la sélection du second centre contraindra le contour oblong à être dessiné horizontalement ou verticalement.

-    {{Version/fr|1.0}}: l\'[aimantation angulaire](Sketcher_Snap/fr.md) peut être utilisée pour contrôler l\'angle du contour oblong.

-    {{Version/fr|0.20}}: un contour oblong peut également être contrainte horizontalement ou verticalement si l\'option des [contraintes automatiques](Sketcher_Workbench/fr#Contraintes_automatiques.md) est activée.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateSlot/fr
