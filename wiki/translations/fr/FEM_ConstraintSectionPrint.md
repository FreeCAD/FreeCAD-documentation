---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintSectionPrint
   Name/fr: FEM Affichage des variables de sortie
   MenuLocation: Modèle , Fonctions d'analyse géométrique , Affichage des variables de sortie
   Workbenches: FEM_Workbench/fr
   Version: 0.19
   SeeAlso: 
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM ConstraintSectionPrint/fr

## Description

Affiche les variables de sortie prédéfinies (forces et moments) dans le fichier de données.


{{Version/fr|1.0}}

: peut également afficher le flux de chaleur et la contrainte de traînée (cette dernière nécessite la prise en charge des analyses de fluides 3D avec CalculiX, qui n\'a pas encore été implémentée).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintSectionPrint.svg" width=16px> [Affichage des variables de sortie](FEM_ConstraintSectionPrint/fr.md)**.
    -   Sélectionner l\'option **Modèle → Fonctions d'analyse géométrique → <img src="images/FEM_ConstraintSectionPrint.svg" width=16px> Affichage des variables de sortie** du menu.
2.  Appuyer sur le bouton **Ajouter** et sélectionner une seule face pour laquelle la sortie sera affichée.
3.  Dans la liste *Variable*, sélectionnez la variable que vous souhaitez imprimer : *Force de section*, *Flux de chaleur* ou *Contrainte de traînée*. {{Version/fr|1.0}}



## Remarques

-   La fonction utilise le jeu de paramètres \*SECTION PRINT de CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintSectionPrint/fr
