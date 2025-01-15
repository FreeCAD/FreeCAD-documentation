---
 GuiCommand:
   Name: Sketcher SelectElementsWithDoFs
   Name/fr: Sketcher Degrés de liberté non contraints
   MenuLocation: Esquisse , Affichage , Sélectionner les degrés de liberté non contraints
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **F**
   Version: 0.18
---

# Sketcher SelectElementsWithDoFs/fr

## Description

L\'outil <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:24px;"> [Sketcher Degrés de liberté non contraints](Sketcher_SelectElementsWithDoFs/fr.md) sélectionne les éléments qui ne sont pas entièrement contraints dans l\'esquisse.

Si de tels éléments existent dans une esquisse, la section [Messages du résolveur de la fenêtre de dialogue de l\'outil d\'esquisse](Sketcher_Dialog/fr#Messages_du_solveur.md) affiche ce message :

-   Esquisse sous-contrainte de : n degré(s) de liberté

Où *n* est le nombre restant de degrés de liberté. Un clic sur le texte souligné permet de sélectionner les éléments sous-contraints.

Notez qu\'une esquisse peut également présenter des contraintes redondantes si l\'un des [messages du solveur](Sketcher_Dialog/fr#Messages_du_solveur.md) est affiché.



## Utilisation

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Cliquez sur le texte souligné dans la fenêtre de dialogue comme décrit ci-dessus.
    -   Sélectionnez l\'option **Esquisse → Affichage → <img src="images/Sketcher_SelectElementsWithDoFs.svg" width=16px> Sélectionner les degrés de liberté non contraints** du menu.
    -   Utilisez le raccourci clavier : **Z** puis **F**.
2.  Les éléments de l\'esquisse sous-contrainte sont sélectionnés.
3.  Vous pouvez cliquer dans une zone vide de la [vue 3D](3D_view/fr.md) pour effacer la sélection.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/fr
