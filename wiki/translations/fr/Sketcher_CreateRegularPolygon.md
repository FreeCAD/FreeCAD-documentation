---
 GuiCommand:
   Name: Sketcher CreateRegularPolygon
   Name/fr: Sketcher Polygone régulier
   MenuLocation: Esquisse , Géométries d'esquisse , Créer un polygone régulier
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **P** **R**
---

# Sketcher CreateRegularPolygon/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:24px;"> [Sketcher Polygone régulier](Sketcher_CreateRegularPolygon/fr.md) crée un polygone régulier.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> [Polygone régulier](Sketcher_CreateRegularPolygon/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> Créer un polygone régulier** dans le menu.
    -   Utilisez le raccourci clavier : **G** puis **P**, puis **R**.
2.  Entrez le **Nombre de côtés** dans la fenêtre de dialogue qui s\'ouvre.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  La section **Paramètres du polygone** ({{Version/fr|1.0}}) est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
5.  Vous pouvez également modifier le nombre de **Côtés** (vous pouvez également le faire après avoir choisi le centre) :
    -   Entrez un nombre supérieur à deux.
    -   Appuyez sur la touche **U** pour augmenter le nombre.
    -   Appuyez sur la touche **J** pour diminuer le nombre.
6.  Choisissez le centre du polygone, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
7.  Choisissez le premier point du polygone, il définit également le rayon du cercle circonscrit. Ou avec Dim-OVP : entrer le rayon du cercle et/ou l\'angle du premier point. L\'angle est relatif à l\'axe X de l\'esquisse. Aucune contrainte n\'est créée pour cet angle.
8.  Le polygone est créé, y compris un cercle de géométrie de construction circonscrit, et les contraintes applicables basées sur Pos-OVP et Dim-OVP sont ajoutées.
9.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des polygones.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Le cercle de la géométrie de construction n\'est pas visible en dehors de l\'esquisse. Il ne peut pas être supprimé sans casser la géométrie du polygone.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRegularPolygon/fr
