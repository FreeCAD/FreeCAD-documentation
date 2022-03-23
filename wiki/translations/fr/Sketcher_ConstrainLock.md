---
- GuiCommand:/fr
   Name:Sketcher ConstrainLock
   Name/fr:Sketcher Contrainte fixe
   MenuLocation:Sketch → Contraintes d'esquisse → Contrainte fixe
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**K** **L**
   SeeAlso:[Sketcher Contrainte de blocage](Sketcher_ConstrainBlock/fr.md)
---

# Sketcher ConstrainLock/fr

## Description

La **Contrainte fixe** applique des contraintes **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [distance horizontale](Sketcher_ConstrainDistanceX/fr.md)** et **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [distance verticale](Sketcher_ConstrainDistanceY/fr.md)** aux sommets (points) sélectionnés dans l\'esquisse. Si un seul sommet est sélectionné, les contraintes de distance horizontale et verticale se référeront au point d\'origine de l\'esquisse. Si deux points ou plus sont sélectionnés, des contraintes de distance horizontale et verticale seront ajoutées pour chaque paire de points. Il n\'y a pas d\'invite automatique pour modifier les valeurs des contraintes, elles doivent être modifiées manuellement.

## Utilisation

1.  Sélectionnez un ou plusieurs sommets (points) dans l\'esquisse.
2.  Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainLock.svg style="width:16px"> [Contrainte fixe](Sketcher_ConstrainLock/fr.md)**.
3.  Pour modifier les valeurs des contraintes, double-cliquez sur une valeur de contrainte dans la vue 3D, ou double-cliquez sur la contrainte ou encore cliquez avec le bouton droit de la souris et sélectionnez \"Changer la valeur\" dans la liste des Contraintes de l\'onglet Tâches.

**Remarque :** l\'outil de contrainte peut également être démarré sans sélection préalable, mais il ne fonctionnera alors que sur un seul sommet et référencera les contraintes au point d\'origine de l\'esquisse. Par défaut, la commande sera en mode Continu pour créer de nouvelles contraintes. Appuyez une fois sur le bouton droit de la souris ou sur **ESC** pour quitter la commande.

## Script

La <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Contrainte fixe](Sketcher_ConstrainLock/fr.md) est une commande graphique qui crée une <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Contrainte de distance en X](Sketcher_ConstrainDistanceX/fr.md) et une <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Contrainte de distance en Y](Sketcher_ConstrainDistanceY/fr.md), ce n\'est pas une contrainte en soi. Consultez la page [Sketcher : Écrire un script](Sketcher_scripting/fr.md) pour obtenir des détails et des exemples sur la façon de créer ces contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/fr
