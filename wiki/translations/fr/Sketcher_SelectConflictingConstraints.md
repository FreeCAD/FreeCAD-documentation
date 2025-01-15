---
 GuiCommand:
   Name: Sketcher SelectConflictingConstraints
   Name/fr: Sketcher Contraintes conflictuelles
   MenuLocation: Esquisse , Affichage , Sélectionner les contraintes conflictuelles
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **P** **C**
   Version: 0.15
---

# Sketcher SelectConflictingConstraints/fr

## Description

L\'outil <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:24px;"> [Sketcher Contraintes conflictuelles](Sketcher_SelectConflictingConstraints/fr.md) sélectionne les contraintes conflictuelles dans l\'esquisse.

Si de telles contraintes existent dans une esquisse, la section [Messages du solveur de la boîte de dialogue](Sketcher_Dialog/fr#Messages_du_solveur.md) affiche ce message :

-   Esquisse sur-contrainte : (#, #, #)

Où *(#, #, #)* sont les indices des contraintes. Cliquez sur le texte souligné permet de sélectionner les contraintes en conflit.



## Utilisation

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Cliquez sur le texte souligné dans la fenêtre de dialogue de l\'outil d\'esquisse, comme décrit ci-dessus.
    -   Sélectionnez l\'option **Esquisse → Affichage → [<img src=images/Sketcher_SelectConflictingConstraints.svg style="width:16px"> Sélectionner les contraintes conflictuelles** du menu.
    -   Utilisez le raccourci clavier : **Z** puis **P**, puis **C**.
2.  Les contraintes conflictuelles sont sélectionnées.
3.  Vous pouvez cliquer dans une zone vide de la [vue 3D](3D_view/fr.md) pour effacer la sélection.



## Remarques

-   Les contraintes conflictuelles doivent être supprimées de l\'esquisse.
-   Au lieu des indices proposés, il est également possible de supprimer d\'autres contraintes.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectConflictingConstraints/fr
