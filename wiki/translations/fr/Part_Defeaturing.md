---
 GuiCommand:
   Name: Part Defeaturing
   Name/fr: Part Supprimer la fonction
   MenuLocation: Part , Supprimer la fonction
   Workbenches: Part_Workbench/fr
   Version: 0.18
   SeeAlso: Defeaturing_Workbench/fr, Macro_Parametric_Defeaturing/fr
---

# Part Defeaturing/fr

## Description

L\'outil **Supprimer la fonction** est destiné à supprimer des fonctions sélectionnées sur le modèle. Dans ce contexte, les nouvelles fonctions sont conçues comme des trous, des protrusions, des espaces, des chanfreins, des congés, etc\... que l\'on retrouve sur le modèle.

L'outil Supprimer la fonction peut être très utile dans différents contextes :

-   Pour éditer un solide importé pour lequel aucun historique des opérations n\'est disponible.
-   Correction des défauts dans le modèle, par exemple combler des vides, des trous, etc\...
-   Simplification du modèle pour l\'analyse numérique, l\'affichage sur des appareils mobiles, etc.

Les entités supprimées sont remplies par l'extension des faces adjacentes, ainsi aucune partie inattendue n\'apparaît dans le résultat. Remarquez que le résultat est une nouvelle forme qui n\'est pas liée à l\'original. De ce fait, il est non paramétrique.

Pour être disponible, cet outil nécessite que FreeCAD soit basé sur Open Cascade 7.3.0 ou supérieur. S\'il n\'est pas disponible dans votre version de FreeCAD, vous pouvez consulter l\'[atelier Defeaturing](Defeaturing_Workbench/fr.md) qui propose des fonctions similaires, même avec les anciennes versions de OCC ou FreeCAD.

![](images/Part_Defeaturing_example.png )



## Utilisation

1.  Sélectionnez la ou les faces de l\'objet à supprimer.
2.  Appuyez sur le bouton **<img src="images/Part_Defeaturing.svg" width=16px> [Supprimer la fonction](Part_Defeaturing/fr.md)**.
3.  Un nouvel objet est créé et intitulé *Defeatured* dans la [vue en arborescence](Tree_view/fr.md) du modèle et l\'objet original est caché de la vue.



## Liens

-   Annonce officielle sur le portail de développement collaboratif d\'Open Cascade [3D Model Defeaturing](https://dev.opencascade.org/index.php?q=node/1211).





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Defeaturing/fr
