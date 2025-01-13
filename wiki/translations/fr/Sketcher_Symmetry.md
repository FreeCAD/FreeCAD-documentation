---
 GuiCommand:
   Name: Sketcher Symmetry
   Name/fr: Sketcher Symétriser
   MenuLocation: Esquisse , Outils d'esquisse , Symétriser
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **S**
   Version: 0.16
   SeeAlso: Sketcher_MirrorSketch/fr
---

# Sketcher Symmetry/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Symmetry.svg  style="width:24px;"> [Sketcher Symétriser](Sketcher_Symmetry/fr.md) crée des copies en mirroir des éléments sélectionnés.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Sélectionnez une ou plusieurs arêtes et/ou points.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_Symmetry.svg style="width:16px"> [Symétriser](Sketcher_Symmetry/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → [<img src=images/Sketcher_Symmetry.svg style="width:16px"> Symétriser** du menu.
    -   Le raccourci clavier : **Z** puis **S**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  La section **Paramètres de symétrie** est ajoutée en haut de la [fenêtre de dialogue](Sketcher_Dialog/fr.md). ({{Version/fr|1.0}})
5.  Vous pouvez appuyer sur la touche **U** ou cochez la case **Supprimer les géométries d\'origine** pour ne conserver que les éléments symétrisés. ({{Version/fr|1.0}})
6.  Vous pouvez également appuyer sur la touche **J** ou cocher la case **Créer des contraintes de symétrie** pour ajouter une [contrainte de symétrie](Sketcher_ConstrainSymmetric/fr.md) entre chaque point d\'origine et symétrisé. ({{Version/fr|1.0}})
7.  Sélectionnez une ligne ou un axe d\'esquisse pour définir la ligne de symétrie, ou un point pour définir le point de symétrie.
8.  Des copies symétrisées sont créées. Les contraintes limitées aux éléments sélectionnés sont également traitées.
    -   Si **Créer des contraintes de symétrie** a été sélectionné des contraintes de symétrie sont ajoutées.
    -   Si **Supprimer les géométries d\'origine** a été sélectionné, la géométrie d\'origine est supprimée.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Symmetry/fr
