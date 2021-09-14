---
- GuiCommand:/fr
   Name:Part Cylinder
   Name/fr:Part Cylindre
   MenuLocation:Pièce → Primitives → Cylindre
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

## Description

Crée un simple cylindre paramétrique, avec sa position, son angle de remplissage, son rayon et sa hauteur.

## Utilisation

1.  Allez à l\'**<img src="images/Workbench_Part.svg" width=16px> [atelier Part](Part_Workbench/fr.md)**.
2.  Lancez la commande Part Cône de plusieurs manières :
    -   Appuyez sur le bouton **<img src="images/Part_Cylinder.svg" width=16px> Créer un cylindre** dans la barre d\'outils.
    -   Utilisez l\'entrée **Pièce → Primitives → <img src="images/Part_Cylinder.svg" width=16px> Cylindre** dans le menu supérieur.

**Résultat :** le résultat par défaut est un cylindre plein avec un rayon de 2 mm et une hauteur de 10 mm, centré le long de l\'axe z global et attaché au plan xy global.

Les propriétés du cylindre peuvent être éditées ultérieurement, soit dans l\'[Éditeur de propriétés](Property_editor/fr.md), soit en double-cliquant sur le prisme dans la [Vue par arborescence](Tree_view/fr.md).

<img alt="Un cylindre créé avec l\'outil Cylindre" src=images/cylinder.png  style="width:650px;">

## Propriétés

-    {{PropertyData/fr|Angle}}: angle de rotation qui permet la création d\'une portion de cylindre (il est fixé à 360° par défaut)

-    {{PropertyData/fr|Height}}: hauteur est la distance dans l\'axe z

-    {{PropertyData/fr|Radius}}: rayon définit un plan dans l\'axe x-y.

-    {{PropertyData/fr|First Angle}}: angle dans la première direction. {{Version/fr|0.20}}

-    {{PropertyData/fr|Second Angle}}: angle dans la seconde direction. {{Version/fr|0.20}}





 
