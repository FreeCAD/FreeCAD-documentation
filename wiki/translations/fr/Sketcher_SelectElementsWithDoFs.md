---
 GuiCommand:
   Name: Sketcher SelectElementsWithDoFs
   Name/fr: Sketcher Degrés de liberté non contraints
   MenuLocation: Esquisse , Outils d'esquisse , Sélectionner les degrés de liberté non contraints
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **F**
   Version: 0.18
---

# Sketcher SelectElementsWithDoFs/fr

## Description

Cet outil a pour but d\'aider à contraindre complètement une esquisse en mettant en surbrillance verte les éléments d'esquisse avec des degrés de liberté restants (DoF ou Degrees of Freedom).



## Utilisation

Dans la boîte de message du solveur située en haut du [panneau des tâches](Task_Panel/fr.md), le message suivant doit s\'afficher :

-   Dans le cas d\'une esquisse **sous-contrainte** :

> Esquisse sous-contrainte avec X degrés de liberté

où \"X\" est le nombre de degrés de liberté restant dans l\'esquisse. Vous aurez plus d\'informations si vous cliquez sur le lien bleu, ou si vous utilisez le menu.

1.  Les éléments qui ont des degrés de liberté sont maintenant surlignés en vert.
2.  Cliquez n\'importe où dans l\'esquisse pour effacer la couleur de surbrillance.

-   Dans le cas d\'une esquisse **entièrement contrainte** :

> Esquisse entièrement contrainte





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/fr
