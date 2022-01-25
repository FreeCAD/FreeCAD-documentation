---
- GuiCommand:/fr
   Name:Part Plane
   Name/fr:Part Plan
   MenuLocation:Pièce → [Créer des primitives](Part_Primitives/fr.md) → Plan
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---

# Part Plane/fr

## Description

Créez un plan paramétrique simple de 10 x 10 mm, avec les paramètres de position, longueur et largeur. Par défaut, le plan est positionné à l\'origine (0,0,0).

![](images/PartPlane.png )

## Utilisation

Le plan standard est créé le coin inférieur gauche au point d\'origine `0,0,0`. Pour modifier ces paramètres, ouvrez la section Emplacement et entrez les valeurs désirées dans les champs de saisie respectifs, ou cliquez sur la [vue 3D](3D_view/fr.md) et sélectionnez un point, les coordonnées du point sont enregistrées dans les champs. Dans le menu de Direction, vous pouvez également définir un vecteur standard (X, Y ou Z) perpendiculaire au plan, ou cliquez sur Défini par l\'utilisateur \... pour ouvrir la boîte de dialogue qui vous permet de définir une direction différente (par exemple de direction 1, 0, -1 crée un plan incliné de 45° par rapport à X et Z).

Les propriétés de l\'objet peuvent être modifiées, soit dans l\'[Éditeur de propriétés](Property_editor/fr.md), soit en double-cliquant sur l\'objet dans la [Vue en arborescence](Tree_view/fr.md).

## Propriétés

### Données


{{TitleProperty|Base}}

-    {{PropertyData/fr|Label}}: Nom de l\'objet, par défaut \'Plane\'. L\'utilisateur peut le renommer.

-    {{PropertyData/fr|Placement}}: Le placement de l\'objet est défini par l\'angle, l\'axe et la position ci-dessous.

-    {{PropertyData/fr|Angle}}: Angle de rotation par rapport à l\'axe ci-dessous.

-    {{PropertyData/fr|Axis}}: Définit l\'axe du plan de rotation : X, Y, ou Z. Par défaut, l\'axe Z est choisi, Z = 1.

-    {{PropertyData/fr|Position}}: Position X, Y, Z, par rapport à l\'origine 0, 0, 0.


{{TitleProperty|Plane}}

-    {{PropertyData/fr|Length}}: La longueur est la dimension le long de l\'axe X La valeur par défaut est 10 mm.

-    {{PropertyData/fr|Width}}: La largeur est la dimension de l\'axe Y La valeur par défaut est 10 mm.

### Vue

Vous avez la vue standard des propriétés.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Plane/fr
