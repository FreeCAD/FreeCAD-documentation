---
- GuiCommand:/fr
   Name:Points Structure
   Name/fr:Points Structure
   MenuLocation:Points → Nuage de points structuré
   Workbenches:[Points](Points_Workbench/fr.md)
---

# Points Structure/fr

## Description

La commande **Structure des points** crée un nuage de points structuré à partir des points d\'un nuage de points dispersé existant. Un nuage de points structuré présente l\'avantage que la tessellation est beaucoup plus facile.

La commande ne fonctionne que pour les nuages de points dont les points, lorsqu\'ils sont vus depuis une certaine direction, sont organisés dans une grille 2D régulière. Ces nuages de points sont généralement produits par [scanners 3D à lumière structurée](https://fr.wikipedia.org/wiki/Scanner_tridimensionnel#Scanner_%C3%A0_lumi%C3%A8re_structur%C3%A9e) et n\'ont pas de contre-dépouilles. Pour les objets complexes, les nuages de points de différentes directions de vue doivent être combinés.

## Utilisation

1.  La commande suppose que la direction de vue du nuage de points est parallèle à l\'axe Z du système de coordonnées global. Si ce n\'est pas le cas: ajustez {{PropertyData/fr|Placement}} de l\'objet nuage de points en conséquence.
2.  Sélectionnez l\'objet nuage de points.
3.  Sélectionnez l\'option **Points → Nuage de points structuré** dans le menu.

## Propriétés

Voir [Points Conversion](Points_Convert/fr.md).





{{Points Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Structure/fr
