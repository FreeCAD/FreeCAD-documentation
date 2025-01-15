---
 GuiCommand:
   Name: Sketcher Scale
   Name/fr: Sketcher Mise à l'échelle
   MenuLocation: Esquisse , Outils d'esquisse , Mettre à l'échelle
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **P** **S**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Scale/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Scale.svg  style="width:24px;"> [Sketcher Mise à l\'échelle](Sketcher_Scale/fr.md) met à l\'échelle ou peut créer des copies à l\'échelle d\'éléments sélectionnés.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

Pos-OVP = [Paramètres d\'affichage](Sketcher_Preferences/fr#Général.md) de position. {{Version/fr|1.0}}
Dim-OVP = Paramètres d\'affichage des dimensions. {{Version/fr|1.0}}

1.  Sélectionnez une ou plusieurs arêtes et/ou des [objets Point](Sketcher_CreatePoint/fr.md). Les contraintes limitées aux éléments sélectionnés sont également traitées. Si les éléments d\'origine sont à l\'échelle, toutes les autres contraintes qui leur sont associées seront supprimées.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_Scale.svg" width=16px> [Mettre à l'échelle](Sketcher_Scale/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_Scale.svg" width=16px> Mettre à l'échelle** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_Scale.svg" width=16px> Mettre à l'échelle** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **Z** puis **P**, puis **S**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  La section **Paramètres d\'échelle** est ajoutée en haut de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md).
5.  Vous pouvez appuyer sur la touche **U** ou cocher la case **Conserver les géométries d\'origine** pour créer des copies à l\'échelle des éléments sélectionnés.
6.  Choisissez le point de base pour l\'opération de mise à l\'échelle, ou avec Pos-OVP : entrez ses coordonnées X et/ou Y.
7.  Choisissez le point final de la première ligne auxiliaire. Son angle et sa longueur sont arbitraires.
8.  Choisissez le point final de la deuxième ligne auxiliaire. Son angle est également arbitraire. Sa longueur par rapport à la longueur de la première ligne auxiliaire définit le facteur d\'échelle, ou avec Dim-OVP : entrez le facteur d\'échelle.
9.  Les éléments originaux sont mis à l\'échelle ou des copies à l\'échelle sont créées. Aucune contrainte basée sur Pos-OVP ou Dim-OVP n\'est ajoutée.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Scale/fr
