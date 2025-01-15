---
 GuiCommand:
   Name: Sketcher ToggleConstruction
   Name/fr: Sketcher Géométrie de construction
   MenuLocation: Esquisse , Géométries d'esquisse , Activer/désactiver la géométrie de construction
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **N**
   SeeAlso: 
---

# Sketcher ToggleConstruction/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:24px;"> [Sketcher Géométrie de construction](Sketcher_ToggleConstruction/fr.md) permet de faire basculer les outils de création de géométrie en mode construction ou de faire basculer une géométrie sélectionnée en mode construction ou de la faire basculer en mode construction.

La géométrie de construction est marquée par une [couleur](Sketcher_Preferences/fr#Apparence.md) dédiée (bleu par défaut) et un type de ligne ({{Version/fr|1.0}}). La géométrie de construction n\'est pas visible à l\'extérieur de l\'esquisse, elle est destinée à aider à définir les contraintes et autres géométries à l\'intérieur de l\'esquisse elle-même. Les lignes de construction peuvent toutefois être utilisées comme axe de rotation par [PartDesign Révolution](PartDesign_Revolution/fr.md).

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">



## Utilisation



### Basculer les outils 

1.  Assurez-vous qu\'il n\'y a pas de sélection.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> [Activer/désactiver la géométrie de construction](Sketcher_ToggleConstruction/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_ToggleConstruction.svg" width=16px> Activer/désactiver la géométrie de construction** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Activer/désactiver la géométrie de construction** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **N**.
3.  Le mode des outils de création de géométrie est basculé :
    -   En mode normal, les icônes du menu et de la barre d\'outils sont blanches et créent des géométries régulières (couleur blanche par défaut). L\'icône de cet outil est alors : <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;">.
    -   En mode construction, les icônes du menu et de la barre d\'outils sont bleues et créent des géométries de construction (couleur bleue par défaut). L\'icône de cet outil est alors : <img alt="" src=images/Sketcher_ToggleConstruction_Constr.svg  style="width:16px;">.



### Basculer la géométrie 

1.  Sélectionnez un ou plusieurs éléments dans l\'esquisse.
2.  Lancez l\'outil comme décrit ci-dessus, ou avec l\'option supplémentaire suivante :
    -   Cliquez avec le bouton droit de la souris dans la section **Éléments** de la [fenêtre de dialogue](Sketcher_Dialog/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Activer/désactiver la géométrie de construction** du menu contextuel.
3.  Les éléments sélectionnés passent de la géométrie normale à la géométrie de construction ou vice versa. Leur apparence change en conséquence.
4.  Le mode des outils de création de géométrie n\'est pas modifié.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/fr
