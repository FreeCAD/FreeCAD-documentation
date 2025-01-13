---
 GuiCommand:
   Name: Sketcher CreatePoint
   Name/fr: Sketcher Point
   MenuLocation: Esquisse , Géométries d'esquisse , Créer un point
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **Y**
---

# Sketcher CreatePoint/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Sketcher Point](Sketcher_CreatePoint/fr.md) crée un point.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreatePoint.svg" width=16px> [Créer un point](Sketcher_CreatePoint/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_CreatePoint.svg" width=16px> Créer un point** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_CreatePoint.svg" width=16px> Créer un point** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **Y**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  Choisissez un point, ou avec Pos-OVP : entrez sa coordonnée X et/ou Y.
4.  Le point est créé et les contraintes applicables basées sur Pos-OVP sont ajoutées.
5.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des points.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-    {{VersionMinus/fr|0.21}}: les points sont toujours créés en tant que géométrie de construction. Il est possible de les transformer en géométrie normale avec [Sketcher Géométrie de construction](Sketcher_ToggleConstruction/fr.md) pour les rendre visibles en dehors du mode d\'édition de l\'esquisse.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/fr
