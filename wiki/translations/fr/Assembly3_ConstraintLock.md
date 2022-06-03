---
- GuiCommand   */fr
   Name   *Assembly3 ConstraintLock
   Name/fr   *Assembly3 Contrainte de verrouillage
   Icon   *Assembly_ConstraintLock.svg
   Workbenches   *[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintLock/fr

## Description

Cet outil relie un objet au système de coordonnées global (GCS = global coordinate system) de l\'assemblage en utilisant le système de coordonnées implicite (ICS) d\'un élément sélectionné.

   *   \- Si un sommet est sélectionné, les coordonnées de son ICS sont fixées par rapport au GCS.

       *   L\'objet peut toujours tourner autour du sommet.
   *   \- Si une arête (droite) est sélectionnée, les coordonnées de son ICS et la direction de son axe z sont fixées par rapport au GCS.

L\'objet peut toujours tourner autour de l\'arête.

   *   \- Si une face est sélectionnée, les coordonnées et l\'orientation de son ICS sont fixées par rapport au GCS.

       *   L\'objet est complètement fixé par rapport au GCS.

IL peut être utilisé pour définir l\'ensemble fixe dans un assemblage statique ainsi que dans un système cinématique.

## Utilisation

1.  Placez un objet dans un assemblage.
2.  Sélectionnez un élément de l\'objet.
3.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintLock.svg" width=16px> [Locked](Assembly3_ConstraintLock/fr.md)**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Assembly3 ConstraintLock/fr
