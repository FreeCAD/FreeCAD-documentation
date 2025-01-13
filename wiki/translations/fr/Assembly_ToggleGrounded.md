---
 GuiCommand:
   Name: Assembly ToggleGrounded
   Name/fr: Assembly Bascule du blocage
   MenuLocation: Assemblage , Activer/désactiver le blocage
   Workbenches: Assembly_Workbench/fr
   Shortcut: **G**
   Version: 1.0
   SeeAlso: 
---

# Assembly ToggleGrounded/fr

## Description

L\'outil <img alt="" src=images/Assembly_ToggleGrounded.svg  style="width:16px;"> [Assembly Bascule du blocage](Assembly_ToggleGrounded/fr.md) fixe la position et l\'orientation d\'une forme par rapport au système de coordonnées de l\'assemblage auquel elle appartient.



## Utilisation

1.  Sélectionnez une ou plusieurs pièces.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Assembly_ToggleGrounded.svg" width=16px> [Activer/désactiver le blocage](Assembly_ToggleGrounded/fr.md)**.
    -   Sélectionnez l\'option **Assemblage → <img src="images/Assembly_ToggleGrounded.svg" width=16px> Activer/désactiver le blocage** du menu.
    -   Utiliser le raccourci clavier : **G**.
3.  Une liaison de blocage est ajoutée pour chaque pièce sélectionnée.



## Remarques

-   Une liaison de blocage affiche une icône de verrou rouge dans la vue 3D, autour du centre de masse du composant mis à la terre. Pour masquer le verrou, désactivez **Visibility** de la liaison.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet **GroundedJoint** est dérivé d\'un [App FeaturePython](App_FeaturePython/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{TitleProperty|Ground}}

-    **Object To Ground|Link**: objet à bloquer.

-    **Placement|Placement**: endroit où la pièce est bloquée. Voir [Placement](Placement/fr.md).





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly ToggleGrounded/fr
