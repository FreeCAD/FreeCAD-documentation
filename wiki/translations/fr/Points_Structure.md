---
 GuiCommand:
   Name: Points Structure
   Name/fr: Points Nuage structuré
   MenuLocation: Points , Nuage structuré de points
   Workbenches: Points_Workbench/fr
---

# Points Structure/fr

## Description

La commande **Points Nuage structuré** crée un nuage structuré de points à partir des points d\'un nuage de points dispersés existant. Un nuage structuré de points présente l\'avantage que la tessellation est beaucoup plus facile.

La commande fonctionne uniquement pour les nuages de points dont les points, lorsqu\'ils sont vus depuis une certaine direction, sont organisés dans une grille 2D régulière. Ces nuages de points sont généralement produits par des [scanners 3D à lumière structurée](https://fr.wikipedia.org/wiki/Scanner_tridimensionnel#Scanner_%C3%A0_lumi%C3%A8re_structur%C3%A9e) et n\'ont pas de contre-dépouilles. Pour les objets complexes, les nuages de points de différentes directions de vue doivent être combinés.



## Utilisation

1.  La commande suppose que la direction de la vue du nuage de points est parallèle à l\'axe Z du système de coordonnées global. Si ce n\'est pas le cas : ajuster **Placement** de l\'objet nuage de points en conséquence.
2.  Sélectionnez l\'objet nuage de points.
3.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le **<img src="images/Points_Structure.svg" width=16px> [Nuage structuré de points](Points_Structure/fr.md)**.
    -   Sélectionnez l\'option **Points → <img src="images/Points_Structure.svg" width=16px> Nuage structuré de points** du menu.



## Propriétés

Voir [Points Convertir](Points_Convert/fr.md).





{{Points Tools navi

}}



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Structure/fr
