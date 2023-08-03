---
 GuiCommand:
   Name: Part CheckGeometry‏‎
   Name/fr: Part Vérifier la géométrie
   MenuLocation: Part , Vérifier la géométrie...
   Workbenches: Part_Workbench/fr
---

# Part CheckGeometry/fr

## Description

L\'outil **<img src="images/Part_CheckGeometry.svg" width=16px> [Part Vérifier la géométrie](Part_CheckGeometry/fr.md)** exécute une vérification et indique si la géométrie est un solide valide. L\'outil vérifie si la [Représentation par les Bords](https://fr.wikipedia.org/wiki/B-Rep) (BRep ou [B-rep](Glossary/fr#B.md)) du modèle est valide.



## Utilisation

1.  Sélectionnez une pièce (attention à sélectionner la pièce entière et pas seulement une face pour vérifier la validité du solide).
2.  Lancez l\'outil soit en :
    -   cliquant sur le **<img src="images/Part_CheckGeometry.svg" width=16px> [Vérifier la géométrie...](Part_CheckGeometry/fr.md)** disponible dans la barre d\'outils de l\'atelier Part.
    -   utilisant **Part → <img src="images/Part_CheckGeometry.svg" width=16px> Vérifier la géométrie...** du menu supérieur.
3.  La boîte de dialogue des **Réglages** s\'ouvre sauf si **Sauter cette page des paramètres** est activé. Voir [Options](#Options.md) pour plus d\'informations. Cliquez sur **Lancer la vérification**.

Les résultats seront présentés dans le [panneau des tâches](Task_panel/fr.md). Si la vérification a produit des erreurs : cliquez dans le rapport sur un message d\'erreur spécifique et l\'objet géométrique correspondant (arête, face, etc.) sera mis en surbrillance dans la [vue 3D](3D_view/fr.md).

## Options



### Sauter cette page des paramètres 

Si cette case est cochée, les prochaines utilisations de l\'outil n\'afficheront pas la boîte de dialogue des **Réglages**.



### Exécuter la vérification BOP 

Si cette case est cochée, une vérification supplémentaire des opérations booléennes (BOP) est effectuée.



### Journal des erreurs 

Si cette case est cochée, toutes les erreurs trouvées seront également enregistrées dans la [vue rapport](Report_view/fr.md).



## Contenu des formes 

En plus de détecter les erreurs potentielles de géométrie, cet outil affiche une série de propriétés concernant l\'objet sélectionné :

-   Objet vérifié
-   Type de forme
-   Nombre d\'entités géométriques : sommets, arêtes, fils, faces, coques, solides, compsolides, composés, formes totales\...
-   Propriétés géométriques et de masse :
    -   Aire
    -   Volume
    -   Masse
    -   Longueur
    -   Centre de masse
    -   Orientation
    -   Axe de symétrie
    -   Point de symétrie
    -   Moments
    -   Premier axe d\'inertie
    -   Deuxième axe d\'inertie
    -   Troisième axe d\'inertie
    -   Rayon de giration
    -   Placement global



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être vérifiés à l\'aide de cet outil. Pour les [App Links](App_Link/fr.md), la forme de l\'objet lié est vérifiée. Pour les conteneurs [App Part](App_Part/fr.md), les objets visibles qu\'ils contiennent sont vérifiés en tant que composés. {{Version/fr|0.20}}
-   FreeCAD ne dispose pas de méthodes pour réparer automatiquement la géométrie. Si des défauts sont détectés, les étapes de la création du modèle doivent être examinées et réparées manuellement.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/fr
