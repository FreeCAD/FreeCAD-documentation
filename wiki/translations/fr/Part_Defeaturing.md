---
 GuiCommand:
   Name: Part Defeaturing
   Name/fr: Part Supprimer la fonctionnalité
   MenuLocation: Part , Supprimer la fonctionnalité
   Workbenches: Part_Workbench/fr
   Version: 0.18
   SeeAlso: Defeaturing_Workbench/fr, Macro_Parametric_Defeaturing/fr
---

# Part Defeaturing/fr

## Description

L\'outil **Supprimer la fonctionnalité** est destiné à supprimer des fonctionnalités sélectionnées sur le modèle. Dans ce contexte, les nouvelles caractéristiques sont conçues comme des trous, des saillies, des espaces, des chanfreins, des congés, etc\... que l\'on retrouve sur le modèle.

L'outil Supprimer la fonctionnalité peut être très utile dans différents contextes:

-   Pour éditer un solide importé pour lequel aucun historique des opérations n\'est disponible.
-   Correction des défauts dans le modèle, par exemple combler des vides, des trous, etc\...
-   Simplification du modèle pour l\'analyse numérique, l\'affichage sur des appareils mobiles, etc.

Les entités supprimées sont remplies par l'extension des faces adjacentes, ainsi aucune partie inattendue n\'apparaît dans le résultat. Veuillez noter que le résultat est une nouvelle forme qui n\'est pas liée à l\'original. De ce fait, il est non paramétrique.

Pour être disponible, cet outil nécessite que FreeCAD soit basé sur Open Cascade 7.3.0 ou supérieur. S\'il n\'est pas disponible dans votre version de FreeCAD, vous pouvez consulter l\'[Atelier Defeaturing](Defeaturing_Workbench/fr.md) complémentaire qui propose des fonctionnalités similaires, même avec les anciennes versions de OCC ou FreeCAD.

![](images/Part_Defeaturing_example.png )

## Utilisation

1.  Sélectionnez la ou les faces de l\'objet à supprimer.
2.  Appuyez sur le bouton **<img src="images/Part_Defeaturing.svg" width=16px> [Supprimer la fonctionnalité](Part_Defeaturing/fr.md)**.
3.  Un nouvel objet est créé et intitulé \'Defeatured\' dans la [vue en arborescence](Tree_view/fr.md) du modèle et l\'objet original est caché de la vue.

## Liens

-   Annonce officielle sur le portail de développement collaboratif Open Cascade [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Defeaturing/fr
