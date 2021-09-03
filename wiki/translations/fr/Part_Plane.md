---
- GuiCommand:/fr
   Name:Part Plane
   Name/fr:Part Plan
   MenuLocation:Pièce → [Créer des primitives](Part_Primitives/fr.md) → Plan
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Primitives](Part_Primitives/fr.md)
---


</div>

## Description


<div class="mw-translate-fuzzy">

## Description 

Créez un plan paramétrique simple de 10 x 10 mm, avec les paramètres de position, longueur et largeur. Par défaut, le plan est positionné à l\'origine (0,0,0).


</div>

![](images/PartPlane.png )

## Utilisation

Le plan standard est créé le coin inférieur gauche au point d\'origine `0,0,0`. Pour modifier ces paramètres, ouvrez la section Emplacement et entrez les valeurs désirées dans les champs de saisie respectifs, ou cliquez sur la [vue 3D](3D_view/fr.md) et sélectionnez un point, les coordonnées du point sont enregistrées dans les champs. Dans le menu de Direction, vous pouvez également définir un vecteur standard (X, Y ou Z) perpendiculaire au plan, ou cliquez sur Défini par l\'utilisateur \... pour ouvrir la boîte de dialogue qui vous permet de définir une direction différente (par exemple de direction 1, 0, -1 crée un plan incliné de 45° par rapport à X et Z).


<div class="mw-translate-fuzzy">

Les propriétés peuvent être modifiées ultérieurement dans **Vue combinée → Données** après avoir sélectionné l\'élément.


</div>

## Properties

### Data


{{TitleProperty|Base}}

-    **Label**: String name of the object, defaults to \'Plane\'. User may rename it.

-    **Placement**: Placement of feature is defined by below angle, axis and position.

-    **Angle**: Angle of rotation relative to the below axis.

-    **Axis**: Defines the axis of rotation plane: X, Y, or Z. Defaults to Z axis, Z = 1

-    **Position**: Position X, Y, Z, relative to the origin 0, 0, 0.


{{TitleProperty|Plane}}

-    **Length**: Length is the dimension along the X axis The default value is 10 mm

-    **Width**: Width is the size of the Y-axis The default value is 10 mm

### View

You have the standard properties view.


<div class="mw-translate-fuzzy">





</div>


 
