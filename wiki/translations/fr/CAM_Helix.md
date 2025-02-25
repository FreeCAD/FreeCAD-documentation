---
 GuiCommand:
   Name: CAM Helix
   Name/fr: CAM Parcours hélicoïdal 
   MenuLocation: CAM , Détourer hélicoïdalement
   Workbenches: CAM_Workbench/fr
---

# CAM Helix/fr

## Description

L\'outil <img alt="" src=images/CAM_Helix.svg  style="width:24px;"> [Parcours hélicoïdal](CAM_Helix/fr.md) ajoute une opération de détourage hélicoïdale à la tâche. Le parcours hélicoïdal dans le sens horaire produit des commandes G-code (G2). Le sens anti-horaire produit des commandes de G-code (G3). Le pourcentage de recouvrement spécifie le recouvrement concentrique en pourcentage du diamètre de l\'outil. Une ou plusieurs parcours hélicoïdales seront créés à des diamètres progressivement différents, pour détourer le trou.



## Utilisation

-   Sélectionnez l\'**[<img src=images/Workbench_CAM.svg style="width:16px"> [atelier CAM](CAM_Workbench/fr.md)**.
-   Sélectionnez l\'icône **<img src="images/CAM_Helix.svg" width=24px>** ou **CAM** → **<img src="images/CAM_Helix.svg" width=24px> Détourer hélicoïdalement** du menu supérieur. Cela ouvre le **<img src="images/CAM_Helix.svg" width=24px>** panneau de configuration du parcours hélicoïdal.
-   Une pop-up \"Choisir un contrôleur d\'outils\" vous invite à sélectionner un contrôleur d\'outils. Dans les anciennes versions, dans l\'onglet **<img src="images/CAM_Helix.svg" width=24px>** Opération, choisissez un contrôleur d\'outil et confirmez en appuyant sur **Appliquer**.
-   Ouvrez l\'onglet Géométrie de base. Tous les trous disponibles compatibles avec l\'outil Parcours hélicoïdal dans le modèle de tâche pourront être sélectionnés pour le traitement. Dans la [vue 3D](3D_view/fr.md), sélectionnez les trous par leur arête ou les faces de leur paroi et ajoutez-les avec le bouton **Ajouter**. Vérifiez qu\'ils apparaissent dans la liste. Confirmez que la liste correspond aux trous destinés à être traités.
-   Pour supprimer des trous, sélectionnez-les dans la liste et appuyez sur le bouton **Supprimer**.
-   S\'assurer que la profondeur de départ, la profondeur finale et le pas de descente (le pas de l\'hélicoïde) sont corrects. Ajustez-les si ce n\'est pas le cas.
-   Assurez-vous que les hauteurs de sécurité et de dégagement sont correctes. Ajustez-les si ce n\'est pas le cas.
-   Dans l\'onglet Opération, spécifiez la surface de départ de l\'hélicoïde (extérieure/intérieure), la direction (sens horaire/sens anti-horaire) et le pourcentage de recouvrement.
-   Cliquez sur **Appliquer** pour créer ou mettre à jour le parcours, **OK** pour appliquer et fermer le panneau, ou **Annuler** pour abandonner et fermer le panneau.

## Options

Un décalage supplémentaire ajoute une marge de matériau à ne pas usiner. Il s\'agit généralement d\'une opération séparée pour permettre une légère finition.



## Commentaires

-   Le pas de descente n\'est pas respecté exactement. Il est toujours arrondi pour donner un nombre complet de tours de la profondeur de départ à la profondeur finale.
-   De même, le pas supérieur n\'est pas respecté exactement. Il est toujours arrondi pour donner un nombre de pas égaux.

Le paramètre d\'avance est constant pour toutes les coupes et est basé sur la position de l\'axe de l\'outil. L\'avance réelle de l\'arête de coupe de l\'outil peut donc varier considérablement entre la coupe la plus intérieure et la surface extérieure. Si les dimensions de la tâche produisent un diamètre de parcours plus petit que le diamètre de l\'outil, cela peut conduire à des vitesses de coupe beaucoup plus rapides que l\'avance donnée pour l\'outil dans le contrôleur d\'outil. Il peut être nécessaire d\'en tenir compte lors de la sélection de \"l\'avance et des vitesses\" pour la tâche.



## Propriétés



### Données

Vide



### Vue

Vide



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Helix/fr
