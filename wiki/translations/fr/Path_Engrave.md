---
- GuiCommand:/fr
   Name:Path Engrave
   Name/fr:Path Gravure
   MenuLocation:Path → Engrave
   Workbenches:[Path](Path_Workbench/fr.md)
---

# Path Engrave/fr

## Description

L\'outil <img alt="" src=images/Path_Engrave.svg  style="width:24px;"> [Path Gravure](Path_Engrave/fr.md) sert principalement à graver une <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;">[Draft Forme à partir d\'un texte](Draft_ShapeString/fr.md) sur une pièce, il peut être utile pour d\'autres types de 2D.

## Utilisation

Vide

## Options

Vide

## Propriétés

### Données

#### Base

-    {{PropertyData/fr|Placement}}:

-    {{PropertyData/fr|Label}}: Nom d\'utilisateur de l\'objet (UTF-8)

#### Profondeur

-    {{PropertyData/fr|Clearance Height}}: hauteur nécessaire pour éviter les pinces et les obstructions.

-    {{PropertyData/fr|Final Depth}}: profondeur finale de l\'outil - valeur la plus basse de Z.

-    {{PropertyData/fr|Safe Height}}: seuil supérieur duquel les mouvements rapides sont autorisés.

-    {{PropertyData/fr|Start Depth}}: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    {{PropertyData/fr|Step Down}}: abaissement incrémentiel de l\'outil.

#### Trajectoire

-    {{PropertyData/fr|Active}}: mettre à False pour empêcher l\'opération de générer du code

-    {{PropertyData/fr|Base}}: géométrie de base pour cette opération

-    {{PropertyData/fr|Comment}}: commentaire facultatif pour cette opération

-    {{PropertyData/fr|Coolant Mode}}: mode de refroidissement pour cette opération

-    {{PropertyData/fr|Cycle Time}}: durée estimée du cycle pour cette opération

-    {{PropertyData/fr|Start Vertex}}: index du sommet pour commencer la trajectoire à partir de

-    {{PropertyData/fr|Tool Controller}}: contrôleur d\'outil qui sera utilisé pour calculer la trajectoire.

-    {{PropertyData/fr|User Label}}: étiquette attribuée par l\'utilisateur

### Cachés

-    {{PropertyData/fr|Base Object}}:

-    {{PropertyData/fr|Base Shapes}}:

-    {{PropertyData/fr|Expression Engine}}:

-    {{PropertyData/fr|Label2}}:

-    {{PropertyData/fr|Path}}:

-    {{PropertyData/fr|Proxy}}:

-    {{PropertyData/fr|Visibility}}:

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
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path Engrave/fr
