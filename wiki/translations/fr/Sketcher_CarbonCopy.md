---
 GuiCommand:
   Name: Sketcher CarbonCopy
   Name/fr: Sketcher Copie carbone
   MenuLocation: Esquisse , Outils d'esquisse , Créer une copie carbone
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy/fr

## Description

L\'outil **<img src="images/Sketcher_CarbonCopy.svg" width=24px> [Sketcher Copie carbone](Sketcher_CarbonCopy/fr.md)** copie toutes les géométries et contraintes d\'une autre esquisse dans l\'esquisse active.

Les contraintes dimensionnelles qui existaient avant la fonction de copie restent liées aux contraintes dimensionnelles de l\'esquisse d\'origine via les [expressions](Expressions/fr.md).



## Utilisation

1.  Assurez-vous d\'être en mode édition d\'une [esquisse](Sketcher_NewSketch/fr.md) existant. Cette esquisse est la cible de l\'opération.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CarbonCopy.svg" width=16px> [Créer une copie carbone](Sketcher_CarbonCopy/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_CarbonCopy.svg" width=16px> Créer une copie carbone** dans le menu.
    -   Utilisez le raccourci clavier : **G** puis **W**.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Choisissez une arête dans une autre esquisse. Cette esquisse est la source de l\'opération. Voir [Remarques](#Remarques.md).
5.  Les éléments géométriques ainsi que les contraintes sont copiés dans l\'esquisse active.
6.  Cet outil fonctionne toujours en mode continu : vous pouvez copier d\'autres esquisses.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Dans l\'[atelier PartDesign](PartDesign_Workbench/fr.md), il est possible de sélectionner l\'esquisse à copier au carbone depuis l\'extérieur du [Body](PartDesign_Body/fr.md) de l\'esquisse active, mais uniquement si la touche **Ctrl** est maintenue enfoncée pendant la sélection.
-   L\'esquisse à copier doit être parallèle à l\'esquisse active. Si ce n\'est pas le cas, les touches **Ctrl** et **Alt** doivent être maintenues enfoncées pendant la sélection. Cela fonctionne également pour les esquisses situées en dehors du corps actif.
-   Si le [mode de construction](Sketcher_ToggleConstruction/fr.md) est actif, la géométrie copiée est créée en tant que géométrie de construction.
-   L\'esquisse complète est copiée, il n\'est pas possible de n\'en sélectionner qu\'une partie. Mais après la copie, vous pouvez supprimer les éléments non désirés.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/fr
