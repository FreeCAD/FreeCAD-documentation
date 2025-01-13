---
 GuiCommand:
   Name: BIM Material
   Name/fr: BIM Matériau
   MenuLocation: Gestion , Gérer les matériaux
   Workbenches: BIM_Workbench/fr
---

# BIM Material/fr

## Description

Affiche la fenêtre de dialogue **BIM matériau**. Cette fenêtre de dialogue permet d\'effectuer rapidement et facilement des opérations liées aux matériaux, en mettant l\'accent sur l\'efficacité du travail avec de nombreux objets et de nombreux matériaux.

1.  Créer un nouveau [matériau](Arch_SetMaterial/fr.md) ou [multi-matériau](Arch_MultiMaterial/fr.md).
2.  Attribuer un matériau ou un multimatériau existant à un ou plusieurs objets sélectionnés.

<img alt="" src=images/BIM_materials_screenshot.png  style="width:600px;">



*Le gestionnaire des matériaux*



## Utilisation

1.  Vous pouvez sélectionné un ou plusieurs objets
2.  Appuyez sur le bouton **<img src="images/BIM_Material.svg" width=16px> [Gérer les matériaux](BIM_Material/fr.md)** dans la barre d\'outils.

-   S\'il n\'y a pas de matériau existant dans le document actif, la fenêtre du gestionnaire de matériaux n\'est pas affichée, et un [nouveau matériau](Arch_SetMaterial/fr.md) sera créé.
-   S\'il y a au moins un matériau ou un multi-matériau dans le document, la fenêtre du gestionnaire de matériaux s\'ouvre.



## Outils de gestion des matériaux 

Le gestionnaire des matériaux vous permet de :

-   **Rechercher des matériaux par nom** : utiliser la boîte de recherche
-   **Assigner un matériau à l\'objet ou aux objets sélectionnés** : appuyer sur OK avec un matériau sélectionné l\'affectera à l\'objet (aux objets) sélectionné(s).
-   **Créer un [matériau](Arch_SetMaterial/fr.md)** : appuyez sur le bouton **Créer un nouveau matériau**.
-   **Créer un [multi-matériau](Arch_MultiMaterial/fr.md)** : cliquez sur le bouton **Créer un nouveau multi-matériau**.
-   **Supprimer un matériau** : sélectionnez un matériau et cliquez avec le bouton droit de la souris sur un matériau et choisissez \"Supprimer\"
-   **Supprimer les matériaux inutilisés** : cliquez sur le bouton **Supprimer les matériaux inutilisés**. Tous les matériaux qui ne sont pas utilisés par un objet seront supprimés.
-   **Fusionner les matériaux en double** : cliquez sur le bouton **Fusionner les doublons**. Fusionne les matériaux ayant exactement le même nom (ex. Béton et Béton) ou exactement le même nom avec un suffixe numérique (ex. Béton et Béton001).
-   **Renommer un matériau** : cliquez avec le bouton droit de la souris sur un matériau et choisissez \"Renommer\"
-   **Dupliquer un matériau** : cliquez avec le bouton droit de la souris sur un matériau et choisissez \"Dupliquer\". Cela créera une copie complète et indépendante du matériau choisi avec les mêmes paramètres.
-   **Fusionner deux matériaux ensemble** : faites un clic droit sur un matériau et choisissez \"Fusionner vers\...\", puis sélectionnez un autre matériau. Le premier matériau sera supprimé et tous les objets qui utilisaient le premier matériau se verront attribuer le second.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Material/fr
