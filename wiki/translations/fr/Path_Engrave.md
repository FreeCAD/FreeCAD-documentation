---
- GuiCommand:
   Name: Path Engrave
   Name/fr: Path Gravure
   MenuLocation: Path -> Graver
   Workbenches: Path_Workbench/fr
---

# Path Engrave/fr

## Description

L\'outil <img alt="" src=images/Path_Engrave.svg  style="width:24px;"> [Gravure](Path_Engrave/fr.md) sert principalement à graver une <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;">[Draft Forme à partir d\'un texte](Draft_ShapeString/fr.md) sur une pièce, il peut être utile pour d\'autres types de 2D.



## Utilisation

Vide

## Options

Vide



## Propriétés



### Données


{{TitleProperty|Base}}

-    **Placement**:

-    **Label**: nom de l\'objet (UTF-8)


{{TitleProperty|Depth}}

-    **Clearance Height**: hauteur nécessaire pour éviter les pinces et les obstructions.

-    **Final Depth**: profondeur finale de l\'outil - valeur la plus basse de Z.

-    **Safe Height**: seuil supérieur duquel les mouvements rapides sont autorisés.

-    **Start Depth**: profondeur initiale de l\'outil - première profondeur de coupe en Z.

-    **Step Down**: pas de descente incrémentale de l\'outil.


{{TitleProperty|Path}}

-    **Active**: mettre à False pour empêcher l\'opération de générer du code

-    **Base**: géométrie de base pour cette opération

-    **Comment**: commentaire facultatif pour cette opération

-    **Coolant Mode**: mode de refroidissement pour cette opération

-    **Cycle Time**: durée estimée du cycle pour cette opération

-    **Start Vertex**: index du sommet pour commencer le parcours à partir de

-    **Tool Controller**: contrôleur d\'outil qui sera utilisé pour calculer le parcours

-    **User Label**: étiquette attribuée par l\'utilisateur


{{TitleProperty|Hidden}}

-    **Base Object**:

-    **Base Shapes**:

-    **Expression Engine**:

-    **Label2**:

-    **Path**:

-    **Proxy**:

-    **Visibility**:



### Vue

Vide



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Exemple :


```python
#Place code example here.
```





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Engrave/fr
