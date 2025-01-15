---
 GuiCommand:
   Name: Sketcher SwitchVirtualSpace
   Name/fr: Sketcher Basculer l'espace virtuel
   MenuLocation: Esquisse , Affichage , Basculer vers/de l'espace virtuel
   Workbenches: Sketcher_Workbench/fr
   Version: 0.17
---

# Sketcher SwitchVirtualSpace/fr

## Description

L\'outil <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:24px;"> [Sketcher Basculer l\'espace virtuel](Sketcher_SwitchVirtualSpace/fr.md) permet d\'afficher/masquer les contraintes ou d\'afficher/masquer l\'espace virtuel visible.

Une esquisse possède deux espaces virtuels qui peuvent contenir des contraintes. Toutes les contraintes sont créées dans l\'espace virtuel principal, mais elles peuvent être masquées, ce qui les déplace dans l\'autre espace virtuel.



## Utilisation



### Afficher/masquer les contraintes 

1.  Sélectionnez une ou plusieurs contraintes. Les contraintes qui ne sont pas visibles dans l\'espace virtuel en cours peuvent être sélectionnées dans la section des [contraintes de la fenêtre de dialogue de l\'esquisse](Sketcher_Dialog/fr#Contraintes.md).
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_SwitchVirtualSpace.svg style="width:16px"> [Basculer vers/de l'espace virtuel](Sketcher_SwitchVirtualSpace/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Affichage → <img src="images/Sketcher_SwitchVirtualSpace.svg" width=16px> Basculer vers/de l'espace virtuel** du menu.
    -   Utiliser le raccourci clavier : **Z** puis **Z**.



### Afficher/masquer l\'espace virtuel 

1.  Assurez-vous qu\'aucune contrainte n\'a été sélectionnée.
2.  Lancez l\'outil comme décrit ci-dessus.
3.  Les contraintes cachées sont rendues visibles et les contraintes non cachées invisibles, ou vice versa.



## Remarques

-   Les contraintes peuvent également être affichées/masquées à partir de la [boîte de dialogue de l\'esquisse](Sketcher_Dialog/fr#Contraintes.md).
-   La configuration de l\'espace virtuel d\'une esquisse n\'est utilisée que dans la session en cours, elle n\'est pas stockée dans le fichier FreeCAD.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SwitchVirtualSpace/fr
