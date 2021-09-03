 {{TOCright}}

## Introduction

Le [panneau de tâches](Task_panel/fr.md) apparaît dans l\'onglet **Tâches** de la [vue combinée](combo_view/fr.md), l\'un des panneaux importants de l\'[interface](interface/fr.md). Il s'agit d'un espace personnalisable pouvant contenir n'importe quel type de widget graphique, comme des sous-fenêtres, des tableaux, des champs de saisie, des cases à cocher, des sélecteurs, des zones de texte, des boutons, des libellés, des images et d'autres éléments, en fonction de l\'[atelier](Workbenches/fr.md) et de l'outil couramment actifs.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="550px;">


*Le panneau de tâches montrant diverses commandes lorsque l'[atelier PartDesign](PartDesign_Workbench/fr.md) est actif et qu'une [Esquisse (sketch)](Sketch/fr.md) est sélectionnée.*

## Travailler avec le panneau de tâches 

Un panneau de tâches s\'ouvre normalement lorsqu\'un outil nécessitant une entrée de l\'utilisateur est activé, soit en appuyant sur un bouton de la barre d'outils ou en double-cliquant sur un objet. Si l\'outil n\'a pas besoin d\'entrée utilisateur, cela produira le résultat ou échouera, mais n\'affichera pas de panneau de tâches.

L\'entrée utilisateur peut être un élément tel que du texte, des coordonnées de points 3D, certains éléments d\'une liste ou des faces d\'une forme, ou des options pour modifier le fonctionnement de l\'outil.

![](images/FreeCAD_Combo_view_Task_panel_Sketcher.png )


*Panneau de tâches qui s'ouvre lors de la modification d'une [esquisse](Sketch/fr.md). Différents types d'informations sont présentés, tels que les messages du solveur, les options de la grille, les contraintes et les éléments géométriques.*

De nombreuses commandes nécessitent la sélection de formes ou d\'objets présents dans le document. dans ce cas, le panneau de tâches attend que l\'utilisateur sélectionne les objets appropriés dans la [vue arborescente](tree_view/fr.md) ou la [vue 3D](3D_view/fr.md). Lorsqu\'un panneau des tâches est ouvert, il est possible de passer à l\'onglet **Modèle** pour afficher la [vue arborescente](Tree_view/fr.md) afin de choisir un objet. Une fois cette opération effectuée, il est possible de revenir à l\'onglet **Tâches** pour poursuivre la commande. Le panneau des tâches est généralement fermé en cliquant sur le bouton **OK**, ou le bouton **Fermer**, ou en appuyant sur la touche **Echap** du clavier pour annuler la commande.

![](images/FreeCAD_Combo_view_Task_panel_ArchComponent.png )


*Panneau de tâches qui s'ouvre lors de la modification d'un [Arch Composant](Arch_Component/fr.md). Le panneau attend que l'utilisateur sélectionne des objets pouvant être ajoutés ou soustraits du composant.*

**Remarque:** Merci de noter que le passage de l\'onglet **Tâches** à l\'onglet **Modèle** ne met pas fin à la commande active ; la tâche sera toujours exécutée en arrière-plan. Il incombe à l\'utilisateur de mettre fin ou d\'abandonner correctement la commande active avant de lancer une tâche différente ; laisser une tâche en cours peut générer des erreurs lors du lancement d\'autres outils.

## Remarques

-   Les utilisateurs migrant depuis d\'autres solutions de CAO qui utilisent la touche **Echap** dans le cadre de leur flux de travail peuvent obtenir des résultats différents dans FreeCAD. Lorsque **Echap** est pressé dans FC si le panneau des tâches est en cours d\'exécution, le panneau des tâches sera automatiquement fermé. Pour désactiver cette fonctionnalité, veuillez consulter [Touche d\'échappement](Fine-tuning/fr#Touche_d.27.C3.A9chappement.md).

## Script


{{VeryImportantMessage|Veuillez reformuler et mettre à jour cette section}}

Voir [fil de discussion](https://forum.freecadweb.org/viewtopic.php?f=10&t=44170&p=376759#p376759) Appelez un widget de dialogue de tâche pour fermer la vue des tâches. Il peut être fermé avec \"this-\>close()\" mais cela ne ferme que la partie inférieure de la vue, pas cette vue elle-même.

Utilisation de Python: 
```python
Gui.Control.closeDialog()
```

Utilisationen C++: 
```python
Gui::Control().closeDialog();
```


{{Interface navi

}} 
