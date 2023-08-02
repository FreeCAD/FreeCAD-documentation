---
- GuiCommand:
   Name: Assembly3 ConstraintArcLineTangent
   Name/fr: Assembly3 Contrainte tangence arc ligne
   Icon: Assembly_ConstraintArcLineTangent.svg
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 ConstraintArcLineTangent/fr

## Description

La commande **<img src="images/Assembly_ConstraintArcLineTangent.svg" width=16px> [Arc line tangent](Assembly3_ConstraintArcLineTangent/fr.md)** construit un lien entre deux objets d\'un assemblage. Les éléments sélectionnés de chaque objet ou plus précisément leurs systèmes de coordonnées implicites (ICS) sont utilisés pour positionner un objet par rapport à un autre.

Comme je n'ai pas réussi à faire fonctionner cet outil, voici juste l'énoncé de l'infobulle : 

Ajoutez une contrainte \"Arc line tangent\" pour rendre une ligne tangente à un arc au point de départ ou d\'arrivée de l\'arc.

## Utilisation

1.  Placer deux objets dans un assemblage
2.  Sélectionner un élément d\'arc d\'un objet
3.  Sélectionnez un élément ligne du second objet
4.  Appuyer sur le bouton **<img src="images/Assembly_ConstraintArcLineTangent.svg" width=16px> [Arc line tangent](Assembly3_ConstraintArcLineTangent/fr.md)**.

Selon l\'ordre des lignes sélectionnées, les *erreurs* suivantes apparaissent :

La contrainte "ArcLineTangent" requiert que le 1er élément soit une arête circulaire.
La contrainte "ArcLineTangent" exige que le 1er élément soit une arête d'arc.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintArcLineTangent/fr
