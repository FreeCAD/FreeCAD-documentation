---
 GuiCommand:
   Name: Sketcher SelectRedundantConstraints
   Name/fr: Sketcher Contraintes redondantes
   MenuLocation: Esquisse , Affichage , Selectionner les contraintes redondantes
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **P** **R**
   Version: 0.15
---

# Sketcher SelectRedundantConstraints/fr

## Description

L\'outil <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:24px;"> [Sketcher Contraintes redondantes](Sketcher_SelectRedundantConstraints/fr.md) sélectionne les contraintes redondantes dans l\'esquisse.

Si de telles contraintes existent dans une esquisse, la section [Messages du solveur de la boîte de dialogue](Sketcher_Dialog/fr#Messages_du_solveur.md) affiche ce message :

-   Esquisse avec contraintes redondantes : (#, #, #)

Où *(#, #, #)* sont les indices des contraintes. Cliquez sur le texte souligné permet de sélectionner les contraintes en conflit.

Notez qu\'une esquisse peut également présenter des contraintes redondantes si l\'un des [messages du solveur](Sketcher_Dialog/fr#Messages_du_solveur.md) est affiché.



## Utilisation

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Cliquez sur le texte souligné dans la fenêtre de dialogue comme décrit ci-dessus.
    -   Sélectionnez l\'option **Esquisse → Affichage → [<img src=images/Sketcher_SelectRedundantConstraints.svg style="width:16px"> Selectionner les contraintes redondantes** du menu.
    -   Utilisez le raccourci clavier : **Z** puis **P**, puis **R**.
2.  Les contraintes redondantes sont sélectionnées.
3.  Cliquez éventuellement dans une zone vide de la [vue 3D](3D_view/fr.md) pour effacer la sélection.



## Remarques

-   Les contraintes redondantes doivent être supprimées de l\'esquisse.
-   Au lieu des indices proposés, il est également possible de supprimer d\'autres contraintes.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectRedundantConstraints/fr
