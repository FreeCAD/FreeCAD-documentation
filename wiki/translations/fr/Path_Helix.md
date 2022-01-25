---
- GuiCommand:/fr
   Name:Path Helix
   Name/fr:Path Parcours hélicoïdal 
   MenuLocation:Path → Parcours hélicoïdal
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path Helix/fr

## Description

La commande <img alt="" src=images/Path_Helix.svg  style="width:24px;"> [Path Parcours hélicoïdal](Path_Helix/fr.md) insère une opération d\'interpolation hélicoïdale à la tâche. L\'interpolation hélicoïdale dans le sens des aiguilles d\'une montre produit des commandes G-Code (G2). A l\'inverse, des commandes G-Code (G3). Pourcentage de dépassement spécifie le dépassement concentrique en pourcentage du diamètre de l\'outil.

## Utilisation

-   Sélectionnez l\'**[<img src=images/Workbench_Path.svg style="width:16px"> [atelier Path](Path_Workbench/fr.md)**.
-   Sélectionnez l\' icône **<img src="images/Path_Helix.svg" width=24px>** ou le bouton dans le menu de la barre d\'outils **Path** → **<img src="images/Path_Helix.svg" width=24px> Hélice**. Cela ouvre le panneau de configuration.
-   Choisissez un contrôleur d\'outil et confirmez en appuyant sur **Appliquer**.
-   Tous les trous disponibles compatibles avec l\'outil Hélix du modèle de travail pourront être sélectionnés pour le traitement. Lors de l\'acquittement, l\'outil créera un chemin pour ceux répertoriés dans l\'onglet Géométrie de base. Confirmez que la liste correspond aux trous destinés au traitement. Ajustez avec ajouter, activer ou désactiver, si nécessaire. Notez que les trous peuvent également être sélectionnés par leur bord ainsi que par leurs côtés.
-   Assurez-vous que la profondeur de départ, la profondeur finale et l\'abaissement sont corrects et ajustez au besoin.
-   Assurez-vous que les hauteurs de sécurité et de dégagement sont correctes et ajustez-les au besoin.
-   Dans l\'onglet Opération, spécifiez le pourcentage du point de départ de Helix, de la direction et du dépassement.
-   Cliquez sur **Appliquer** pour créer ou mettre à jour le chemin, sur **OK** pour appliquer et fermer le panneau ou sur **Annuler** pour annuler et fermer le panneau.

## Options

Vide

## Propriétés

### Données

Vide

### Vue

Vide

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Helix/fr
