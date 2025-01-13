---
 GuiCommand:
   Name: Sketcher ToggleDrivingConstraint
   Name/fr: Sketcher Contraintes pilotantes
   MenuLocation: Esquisse , Contraintes d'esquisse , Activer/désactiver les contraintes pilotantes/pilotées
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **K** **X**
   Version: 0.16
   SeeAlso: Sketcher_ToggleActiveConstraint/fr
---

# Sketcher ToggleDrivingConstraint/fr

## Description

L\'outil <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:24px;"> [Sketcher Contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md) permet de basculer les [outils de création de contraintes de dimension](Sketcher_Workbench/fr#Sketcher_CompDimensionTools.md) entre le mode pilotant et le mode référence, ou de basculer les contraintes sélectionnées de dimension entre ces deux modes.

Contrairement aux contraintes de conduite, les contraintes de référence ne contraignent pas l\'esquisse, leur valeur dépend des autres contraintes, elles sont conduites. Elles peuvent être utiles pour vérifier des mesures. Elles peuvent être utilisées dans les [expressions](Expressions/fr.md), mais pas dans l\'esquisse elle-même.

![](images/Sketcher_ToggleConstraint_example.png ) 
*Une contrainte pilotante horizontale (50 mm), une contrainte pilotante verticale (30 mm) et une contrainte pilotante d'angle (75°) ont été définies pour définir l'esquisse. Une cote dite pilotée a été ajoutée sur le segment de ligne incliné pour connaître sa longueur (31.0583 mm).*



## Utilisation



### Basculer les outils 

1.  Assurez-vous qu\'aucune contrainte dimensionnelle n\'a été sélectionnée.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> [Activer/désactiver les contraintes pilotantes/pilotées](Sketcher_ToggleDrivingConstraint/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Contraintes d'esquisse → <img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Activer/désactiver les contraintes pilotantes/pilotées** du menu.
    -   Utilisez le raccourci clavier : **K** puis **X**.
3.  Le mode des outils de création de contraintes de dimension est basculé :
    -   En mode pilotant, les icônes de leur menu et de leur barre d\'outils sont rouges et créent des contraintes pilotante (par défaut de [couleur](Sketcher_Preferences/fr#Apparence.md) rouge). L\'icône de cet outil est alors : <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:16px;">.
    -   En mode référence, les icônes du menu et de la barre d\'outils sont bleues et créent des contraintes de référence (couleur bleue par défaut). L\'icône de cet outil est alors : <img alt="" src=images/Sketcher_ToggleConstraint_Driven.svg  style="width:16px;">.



### Basculer les contraintes 

1.  Sélectionnez une ou plusieurs contraintes dimensionnelles.
2.  Lancez l\'outil comme décrit ci-dessus, ou avec l\'une des options supplémentaires suivantes :
    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez la **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> Activer/désactiver les contraintes pilotantes/pilotées** du menu contextuel.

    -   Cliquez avec le bouton droit de la souris dans la section **Contraintes** de la [fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr.md) et sélectionnez l\'option **Basculer vers/à partir d'une référence** du menu contextuel.
3.  Les contraintes sélectionnées passent du mode pilotant au mode référence ou vice versa. Leur apparence change en conséquence.
4.  Le mode des outils de création de contraintes de dimension n\'est pas modifié.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/fr
