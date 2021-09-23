---
- GuiCommand:/fr
   Name:Part Wedge
   Name/fr:Part Pyramide tronquée
   MenuLocation:Pièce → Créer des primitives → Pyramide tronquée
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Wedge/fr

## Description

Crée un objet Pyramide tronquée paramétrique. Par défaut, cette pyramide tronquée a une base carrée plus grande et un carré plus petit en sommet.

## Utilisation

### Dimensions et placement par défaut 

**Placement:** L'orientation par défaut place la base sur le plan XZ et la face supérieure se situe dans la direction de l\'axe Y. L\'angle de la base est située par défaut aux coordonnées d\'origine 0,0,0.

**Face de base :**

-   X : 10 mm
-   Z : 10 mm

**Hauteur:**

-   Y : 0-10 mm

**Face du dessus:**

-   X : 2-8 mm
-   Z : 2-8 mm

![](images/PartWedgeProperty.png ) 

### Entrées paramétriques 

+------------------------------------------------------------------+--------------------------------------------------------------------+
| ![](images/PartWedgeProperty_Inputs.png ) | Utilisation du placement par défaut, les entrées disponibles sont: |
|                                                                  |                                                                    |
|                                                                  | -                                                   |
|                                                                  |     {{PropertyData/fr|X min/max}}                                  |
|                                                                  |                                                                 |
|                                                                  |     : Dimension de la base selon l\'axe X                          |
|                                                                  |                                                                    |
|                                                                  | -                                                   |
|                                                                  |     {{PropertyData/fr|Y min/max}}                                  |
|                                                                  |                                                                 |
|                                                                  |     : Hauteur de la pyramide tronquée                              |
|                                                                  |                                                                    |
|                                                                  | -                                                   |
|                                                                  |     {{PropertyData/fr|Z min/max}}                                  |
|                                                                  |                                                                 |
|                                                                  |     : Dimension de la base selon l\'axe Z                          |
|                                                                  |                                                                    |
|                                                                  | -                                                   |
|                                                                  |     {{PropertyData/fr|X2 min/max}}                                 |
|                                                                  |                                                                 |
|                                                                  |     : Dimension de la face du dessus selon l\'axe X                |
|                                                                  |                                                                    |
|                                                                  | -                                                   |
|                                                                  |     {{PropertyData/fr|Z2 min/max}}                                 |
|                                                                  |                                                                 |
|                                                                  |     : Dimension de la face du dessus selon l\'axe Z                |
+------------------------------------------------------------------+--------------------------------------------------------------------+

### Autres exemples de pyramides tronquées 

![](images/Wedge_examples.png )

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Wedge/fr
